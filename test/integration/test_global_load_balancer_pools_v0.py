# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Integration test code to execute global load balancer pools functions
"""

import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services.global_load_balancer_pools_v0 import GlobalLoadBalancerPoolsV0
from ibm_cloud_networking_services.global_load_balancer_monitor_v1 import GlobalLoadBalancerMonitorV1

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')


class TestGlobalLoadBalancerPoolsV0 (unittest.TestCase):

    @unittest.skip("Authentication failing")

    def setUp(self):
        """ test case setup """
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')

        self.endpoint = os.getenv("API_ENDPOINT")
        self.crn = os.getenv("CRN")
        self.globalLoadBalancerPools = GlobalLoadBalancerPoolsV0.new_instance(
            crn=self.crn, service_name="cis_services")
        self.globalLoadBalancerPools.set_service_url(self.endpoint)
        # create global load balancer monitor record class object
        self.globalLoadBalancerMonitor = GlobalLoadBalancerMonitorV1.new_instance(
            crn=self.crn, service_name="cis_services")
        self.globalLoadBalancerMonitor.set_service_url(self.endpoint)

        # create load balancer monitor to be used in creating pool
        response = self.globalLoadBalancerMonitor.create_load_balancer_monitor(
            expected_codes="2xx", type="http", description="Test LB montior1", method="GET", port=80,
            path="/auto/test", header={"Host": ["example.com"], "X-App-ID": ["abc123"]}, timeout=3, retries=0,
            interval=90, follow_redirects=True, expected_body="alive", allow_insecure=True).get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        self.monitor_identifier = result.get('id')

        self._cleanup_pools()

    def tearDown(self):
        """ tear down global load balancer monitor"""
        response = self.globalLoadBalancerMonitor.delete_load_balancer_monitor(
            monitor_identifier=self.monitor_identifier).get_result()
        assert response is not None and response.get('success') is True
        # Delete the resources
        print("Clean up complete")

    def _cleanup_pools(self):
        response = self.globalLoadBalancerPools.list_all_load_balancer_pools()
        assert response is not None
        assert response.status_code == 200
        pools = {}
        pools = response.get_result().get("result")
        for pool in pools:
            self.globalLoadBalancerPools.delete_load_balancer_pool(
                pool_identifier=pool.get("id"))

    ################## load_balancer_pools integration test cases ###################

    def test_1_load_balancer_pools(self):
        """ create load balancer pool """
        self.name = "test-lb-pool12"
        self.check_regions = ["WEU", "ENAM"]
        self.origins = [{"name": "app-server-1",
                         "address": "www.test.com", "enabled": True, "weight": 0.5}]
        self.description = "Test GLB Pool 1"
        self.minimum_origins = 1
        self.enabled = True
        self.notification_email = "notify@in.ibm.com"
        response = self.globalLoadBalancerPools.create_load_balancer_pool(
            name=self.name, check_regions=self.check_regions, origins=self.origins,
            description=self.description, minimum_origins=self.minimum_origins, enabled=self.enabled,
            monitor=self.monitor_identifier, notification_email=self.notification_email).get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        self.pool_identifier = result.get('id')

        """list load balancer pools"""
        response = self.globalLoadBalancerPools.list_all_load_balancer_pools().get_result()
        assert response is not None and response.get('success') is True

        """ get load balancer pool """
        response = self.globalLoadBalancerPools.get_load_balancer_pool(
            pool_identifier=self.pool_identifier).get_result()
        assert response is not None and response.get('success') is True

        """ edit load balancer pool """
        self.name = "test-lb-pool12"
        self.check_regions = ["WEU", "ENAM"]
        self.origins = [{"name": "app-server-2",
                         "address": "www.test2.com", "enabled": True, "weight": 0.5}]
        self.description = "Test GLB Pool 2"
        self.minimum_origins = 1
        self.enabled = True
        self.notification_email = "notify@in.ibm.com"
        response = self.globalLoadBalancerPools.edit_load_balancer_pool(
            pool_identifier=self.pool_identifier, name=self.name,
            check_regions=self.check_regions, origins=self.origins, description=self.description,
            minimum_origins=self.minimum_origins, enabled=self.enabled, monitor=self.monitor_identifier,
            notification_email=self.notification_email).get_result()
        assert response is not None and response.get('success') is True

        """ delete load balancer pool """
        response = self.globalLoadBalancerPools.delete_load_balancer_pool(
            pool_identifier=self.pool_identifier).get_result()
        assert response is not None and response.get('success') is True

    ################## Negative test cases ###################

    def test_2_load_balancer_pools(self):
        """variables"""
        self.name = "test-lb-pool1"
        self.check_regions = ["WEU", "ENAM"]
        self.origins = [{"name": "app-server-1",
                         "address": "www.test.com", "enabled": True, "weight": 0.5}]
        self.description = "Test GLB Pool 1"
        self.minimum_origins = 1
        self.enabled = True
        self.notification_email = "notify@in.ibm.com"
        self.pool_identifier = "ddde5a417bb303b897f6037c86e4e1da"
        self.monitor = "bbf53e07352ba94da066eedb9be97a2b"

        """ get load balancer pool method without pool_identifier """
        with self.assertRaises(ValueError) as val:
            self.globalLoadBalancerPools.get_load_balancer_pool(
                pool_identifier=None).get_result()
            self.assertEqual(val.exception.msg,
                             'pool_identifier must be provided')

        """ delete load balancer pool method without pool_identifier """
        with self.assertRaises(ValueError) as val:
            self.globalLoadBalancerPools.delete_load_balancer_pool(
                pool_identifier=None).get_result()
            self.assertEqual(val.exception.msg,
                             'pool_identifier must be provided')

        """ edit load balancer pool method without pool_identifier """
        with self.assertRaises(ValueError) as val:
            self.globalLoadBalancerPools.edit_load_balancer_pool(
                pool_identifier=None, name=self.name, check_regions=self.check_regions, origins=self.origins, description=self.description, minimum_origins=self.minimum_origins, enabled=self.enabled, monitor=self.monitor, notification_email=self.notification_email).get_result()
            self.assertEqual(val.exception.msg,
                             'pool_identifier must be provided')


if __name__ == '__main__':
    unittest.main()
