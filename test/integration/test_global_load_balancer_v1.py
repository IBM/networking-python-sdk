# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Integration test code to execute global load balancer functions
"""

import os
import unittest
import uuid
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services.global_load_balancer_v1 import GlobalLoadBalancerV1
from ibm_cloud_networking_services.global_load_balancer_pools_v0 import GlobalLoadBalancerPoolsV0
from ibm_cloud_networking_services.global_load_balancer_monitor_v1 import GlobalLoadBalancerMonitorV1
from ibm_cloud_networking_services.zones_v1 import ZonesV1

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')


class TestGlobalLoadBalancerV1 (unittest.TestCase):
    def setUp(self):
        """ test case setup """
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')

        self.endpoint = os.getenv("API_ENDPOINT")
        self.crn = os.getenv("CRN")

        # create zones record class object
        self.zones = ZonesV1.new_instance(
            crn=self.crn, service_name="cis_services")
        self.zones.set_service_url(self.endpoint)

        # create zone
        self.zone_name = "uuid-" + \
            str(uuid.uuid1())[1:6] + ".sdk.cistest-load.com"
        response = self.zones.create_zone(
            name=self.zone_name).get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        self.zone_identifier = result.get('id')

        # create global load balancer record class object
        self.globalLoadBalancer = GlobalLoadBalancerV1.new_instance(
            crn=self.crn, zone_identifier=self.zone_identifier, service_name="cis_services")
        self.globalLoadBalancer.set_service_url(self.endpoint)
        self.globalLoadBalancerPools = GlobalLoadBalancerPoolsV0.new_instance(
            crn=self.crn, service_name="cis_services")
        self.globalLoadBalancerPools.set_service_url(self.endpoint)
        # create global load balancer monitor record class object
        self.globalLoadBalancerMonitor = GlobalLoadBalancerMonitorV1.new_instance(
            crn=self.crn, service_name="cis_services")
        self.globalLoadBalancerMonitor.set_service_url(self.endpoint)

        # create load balancer monitor
        response = self.globalLoadBalancerMonitor.create_load_balancer_monitor(
            expected_codes="2xx", type="http", description="Test LB montior1", method="GET", port=80,
            path="/auto/test", header={"Host": ["example.com"], "X-App-ID": ["abc123"]}, timeout=3, retries=0,
            interval=90, follow_redirects=True, expected_body="alive", allow_insecure=True).get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        self.monitor_identifier = result.get('id')

        # create load balancer monitor pool 1
        response = self.globalLoadBalancerPools.create_load_balancer_pool(
            name="test-lb-pool1", check_regions=["WEU", "ENAM"],
            origins=[{"name": "app-server-1", "address": "www.test.com",
                      "enabled": True, "weight": 0.5}],
            description="Test GLB Pool 1", minimum_origins=1, enabled=True,
            monitor=self.monitor_identifier, notification_email="notify@in.ibm.com").get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        self.pool_identifier1 = result.get('id')

        # create load balancer monitor pool 2
        response = self.globalLoadBalancerPools.create_load_balancer_pool(
            name="test-lb-pool2", check_regions=["WEU", "ENAM"],
            origins=[{"name": "app-server-2", "address": "www.test2.com",
                      "enabled": True, "weight": 0.5}],
            description="Test GLB Pool 2", minimum_origins=1, enabled=True,
            monitor=self.monitor_identifier, notification_email="notify@in.ibm.com").get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        self.pool_identifier2 = result.get('id')

        self._cleanup_load_balancers()

    def tearDown(self):
        """ tear down lb monitor pools"""
        monitor_pool_list = [self.pool_identifier1, self.pool_identifier2]
        for pool_id in monitor_pool_list:
            response = self.globalLoadBalancerPools.delete_load_balancer_pool(
                pool_identifier=pool_id).get_result()
            assert response is not None and response.get('success') is True

        """ tear down lb monitor """
        response = self.globalLoadBalancerMonitor.delete_load_balancer_monitor(
            monitor_identifier=self.monitor_identifier).get_result()
        assert response is not None and response.get('success') is True

        """ tear down zone """
        response = self.zones.delete_zone(
            zone_identifier=self.zone_identifier).get_result()
        assert response is not None and response.get('success') is True

        # Delete the resources
        print("Clean up complete")

    def _cleanup_load_balancers(self):
        response = self.globalLoadBalancer.list_all_load_balancers(
        )
        assert response is not None
        assert response.status_code == 200
        load_balancers = {}
        load_balancers = response.get_result().get("result")
        for load_balancer in load_balancers:
            self.globalLoadBalancer.delete_load_balancer(
                load_balancer_identifier=load_balancer.get("id"))

    ################## global load balancers integration test cases ###################

    def test_1_load_balancers(self):
        """ create load balancer """
        self.name = "test_lb1."+self.zone_name
        self.default_pools = [self.pool_identifier1]
        self.fallback_pool = self.pool_identifier2
        self.description = "Test load balancer 1"
        self.ttl = 60
        self.region_pools = None
        self.pop_pools = None
        self.proxied = False
        self.enabled = False
        self.session_affinity = "cookie"
        self.steering_policy = "dynamic_latency"
        response = self.globalLoadBalancer.create_load_balancer(
            name=self.name,
            fallback_pool=self.fallback_pool, default_pools=self.default_pools,
            description=self.description, ttl=self.ttl, region_pools=self.region_pools,
            pop_pools=self.pop_pools, proxied=self.proxied, enabled=self.enabled,
            session_affinity=self.session_affinity, steering_policy=self.steering_policy).get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        self.load_balancer_identifier = result.get('id')

        """ list load balancers """
        response = self.globalLoadBalancer.list_all_load_balancers(
        ).get_result()
        assert response is not None and response.get('success') is True

        """ get load balancer """
        response = self.globalLoadBalancer.get_load_balancer_settings(
            load_balancer_identifier=self.load_balancer_identifier).get_result()
        assert response is not None and response.get('success') is True

        """ edit load balancer """
        self.description = "Test load balancer 2"
        self.ttl = 50
        self.region_pools = None
        self.pop_pools = None
        self.proxied = False
        self.enabled = True
        self.session_affinity = "ip_cookie"
        self.steering_policy = "random"
        response = self.globalLoadBalancer.edit_load_balancer(
            zone_identifier=self.zone_identifier,
            load_balancer_identifier=self.load_balancer_identifier, name=self.name,
            fallback_pool=self.fallback_pool, default_pools=self.default_pools,
            description=self.description, ttl=self.ttl, region_pools=self.region_pools,
            pop_pools=self.pop_pools, proxied=self.proxied, enabled=self.enabled,
            session_affinity=self.session_affinity, steering_policy=self.steering_policy).get_result()
        assert response is not None and response.get('success') is True

        """ delete load balancer """
        response = self.globalLoadBalancer.delete_load_balancer(
            load_balancer_identifier=self.load_balancer_identifier).get_result()
        assert response is not None and response.get('success') is True

    ################## Negative test cases ###################

    def test_2_load_balancers(self):
        """variables"""
        self.name = "test_lb1."+self.zone_name
        self.default_pools = [self.pool_identifier1]
        self.fallback_pool = self.pool_identifier2
        self.description = "Test load balancer 1"
        self.ttl = 60
        self.region_pools = None
        self.pop_pools = None
        self.proxied = False
        self.enabled = False
        self.session_affinity = "cookie"
        self.steering_policy = "dynamic_latency"
        self.load_balancer_identifier = "7e18c0979bfd05c96a064636c1415c20"

        """ get load balancer method without load_balancer_identifier """
        with self.assertRaises(ValueError) as val:
            self.globalLoadBalancer.get_load_balancer_settings(
                load_balancer_identifier=None).get_result()
            self.assertEqual(val.exception.msg,
                             'load_balancer_identifier must be provided')

        """ delete load balancer method without load_balancer_identifier """
        with self.assertRaises(ValueError) as val:
            self.globalLoadBalancer.delete_load_balancer(
                load_balancer_identifier=None).get_result()
            self.assertEqual(val.exception.msg,
                             'load_balancer_identifier must be provided')

        """ edit load balancer method without load_balancer_identifier """
        with self.assertRaises(ValueError) as val:
            self.globalLoadBalancer.edit_load_balancer(
                load_balancer_identifier=None, name=self.name, fallback_pool=self.fallback_pool,
                default_pools=self.default_pools, description=self.description, ttl=self.ttl,
                region_pools=self.region_pools, pop_pools=self.pop_pools, proxied=self.proxied).get_result()
            self.assertEqual(val.exception.msg,
                             'load_balancer_identifier must be provided')


if __name__ == '__main__':
    unittest.main()
