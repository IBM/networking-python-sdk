"""
Integration test code to execute global load balancer functions
"""
import os
import unittest

from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services import DnsZonesV1
from ibm_cloud_networking_services.global_load_balancers_v1 import GlobalLoadBalancersV1

configFile = "pdns.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="pdns.env"))
except:
    print('warning: no pdns.env file loaded')


class TestGlobalLoadBalancersV1 (unittest.TestCase):
    
    @unittest.skip("skipping failing test")

    def setUp(self):
        """ test case setup """

        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')

        self.instance_id = os.getenv("INSTANCE_ID")
        self.zone_id = ""

        # create zone class object
        self.zone = DnsZonesV1.new_instance(service_name="pdns_services")

        # create global load balancers record class object
        self.globalLoadBalancers = GlobalLoadBalancersV1.new_instance(
            service_name="pdns_services")
        self._create_dns_zones()

    def tearDown(self):
        """ tear down """
        # Delete Global load balancers
        self._clean_dns_globalloadbalancers()
        print("Clean up complete")

    def _create_dns_zones(self):
        name = "test.example36.com"
        label = "us-south"
        resp = self.zone.create_dnszone(
            instance_id=self.instance_id, name=name, label=label)
        assert resp is not None
        assert resp.status_code == 200
        self.zone_id = resp.get_result().get("id")

    def _clean_dns_globalloadbalancers(self):
        #delete all dns Load Balancer
        response = self.globalLoadBalancers.list_load_balancers(instance_id=self.instance_id, dnszone_id=self.zone_id)
        assert response is not None
        assert response.status_code == 200
        loadbalancers = {}
        loadbalancers = response.get_result().get("load_balancers")
        for loadbalancer in loadbalancers:
            self.globalLoadBalancers.delete_load_balancer(instance_id=self.instance_id, dnszone_id=self.zone_id, lb_id=loadbalancer.get("id"))
            assert response is not None
        #delete all dns Pools
        response = self.globalLoadBalancers.list_pools(instance_id=self.instance_id)
        assert response is not None
        assert response.status_code == 200
        pools = {}
        pools = response.get_result().get("pools")
        for pool in pools:
            self.globalLoadBalancers.delete_pool(instance_id=self.instance_id, pool_id=pool.get("id"))
            assert response is not None
        # delete all dns Monitors
        response = self.globalLoadBalancers.list_monitors(instance_id=self.instance_id)
        assert response is not None
        assert response.status_code == 200
        monitors = {}
        monitors = response.get_result().get("monitors")
        for monitor in monitors:
            self.globalLoadBalancers.delete_monitor(instance_id=self.instance_id, monitor_id=monitor.get("id"))
            assert response is not None
        # delete dns zones
        response = self.zone.list_dnszones(instance_id=self.instance_id)
        assert response is not None
        assert response.status_code == 200
        result = response.get_result().get("dnszones")
        for zone in result:
            self.zone.delete_dnszone(
                instance_id=self.instance_id, dnszone_id=zone.get("id"))

    ################## global load balancers integration test cases ##################
    def test_1_dns_globalloadbalancers(self):

        """ create,get,update,delete GLB monitor """

        name='testmonitor1'
        lbtype='HTTP'
        description='Creating testmonitor1'
        port=8080
        interval=60
        retries=0
        timeout=5
        method='GET'
        path="helth"
        header = {"Host": ["example.com"], "X-App-ID": ["abc123"]}
        allow_insecure= True
        expected_body="alive"
        #Create monitor
        response = self.globalLoadBalancers.create_monitor(instance_id=self.instance_id, name=name, type=lbtype, description=description, port=port, interval=interval, retries=retries, timeout=timeout)
        assert response is not None
        assert response.status_code == 200
        self.monitor_id = response.get_result().get("id")
        assert name== response.get_result().get("name")
        assert lbtype== response.get_result().get("type")
        assert description== response.get_result().get("description")
        assert interval== response.get_result().get("interval")
        #Get monitor
        response = self.globalLoadBalancers.get_monitor(instance_id=self.instance_id, monitor_id=self.monitor_id)
        assert response is not None
        assert response.status_code == 200
        #Update monitor
        lbtype='HTTPS'
        description='Updating testmonitor1'
        interval=70
        timeout=10
        response = self.globalLoadBalancers.update_monitor(instance_id=self.instance_id, monitor_id=self.monitor_id,type=lbtype, description=description, interval=interval, timeout=timeout)
        assert response is not None
        assert response.status_code == 200
        assert lbtype== response.get_result().get("type")
        assert description== response.get_result().get("description")

        """ createcreate,get,update,delete  GLB Pool """

        #Create Pools
        name = "testPool"
        origins = [{"name": "app-server-1",
                         "address": "10.10.10.8", "enabled": True}]
        description = "create testpool"
        enabled = True
        healthy_origins_threshold=1
        response = self.globalLoadBalancers.create_pool(instance_id=self.instance_id, name=name, origins=origins, description=description, enabled=enabled, healthy_origins_threshold=healthy_origins_threshold)
        assert response is not None
        assert response.status_code == 200
        self.pool_id = response.get_result().get("id")
        assert name== response.get_result().get("name")
        assert description== response.get_result().get("description")
        assert enabled== response.get_result().get("enabled")
        assert healthy_origins_threshold== response.get_result().get("healthy_origins_threshold")
        #GET pool
        response = self.globalLoadBalancers.get_pool(instance_id=self.instance_id, pool_id=self.pool_id)
        assert response is not None
        assert response.status_code == 200
        #Update pool
        name = "updatetestPool"
        description = "update testpool"
        response = self.globalLoadBalancers.update_pool(instance_id=self.instance_id, pool_id=self.pool_id, name=name, description=description)
        assert response is not None
        assert response.status_code == 200
        assert name== response.get_result().get("name")
        assert description== response.get_result().get("description")

        """ create,get,update,list,delete GLB LB """

        name='testloadbalancer'
        description='Creating testloadbalancer'
        default_pools=[self.pool_id]
        enabled=True
        ttl=120
        #Create Load balancer
        response = self.globalLoadBalancers.create_load_balancer(instance_id=self.instance_id, dnszone_id=self.zone_id, name=name, fallback_pool=self.pool_id, default_pools=default_pools, description=description, enabled=enabled, ttl=ttl)
        assert response is not None
        assert response.status_code == 200
        self.loadbalancer_id = response.get_result().get("id")
        assert description== response.get_result().get("description")
        assert enabled== response.get_result().get("enabled")
        assert ttl== response.get_result().get("ttl")
        #GET Load balancer
        response = self.globalLoadBalancers.get_load_balancer(instance_id=self.instance_id, dnszone_id=self.zone_id, lb_id=self.loadbalancer_id)
        assert response is not None
        assert response.status_code == 200
        #Update Load balancer
        name = "updatetestLoadbalancer"
        description = "update testLoadbalancer"
        response = self.globalLoadBalancers.update_load_balancer(instance_id=self.instance_id, dnszone_id=self.zone_id, lb_id=self.loadbalancer_id, name=name, description=description)
        assert response is not None
        assert response.status_code == 200
        assert description== response.get_result().get("description")
        #List Load balancer
        response = self.globalLoadBalancers.list_load_balancers(instance_id=self.instance_id, dnszone_id=self.zone_id)
        assert response is not None
        assert response.status_code == 200

        #Delete Load balancer/Pool/Monitor
        response = self.globalLoadBalancers.delete_load_balancer(instance_id=self.instance_id, dnszone_id=self.zone_id, lb_id=self.loadbalancer_id)
        assert response is not None
        assert response.status_code == 204
        response = self.globalLoadBalancers.delete_pool(instance_id=self.instance_id, pool_id=self.pool_id)
        assert response is not None
        assert response.status_code == 204
        response = self.globalLoadBalancers.delete_monitor(instance_id=self.instance_id, monitor_id=self.monitor_id)
        assert response is not None
        assert response.status_code == 204

    def test_2_list_dns_globalloadbalancers(self):

        #List monitor
        for i in range(3):
            name='testmonitor'+str(i)
            lbtype='HTTP'
            description='Creating testmonitor '+str(i)
            response = self.globalLoadBalancers.create_monitor(instance_id=self.instance_id, name=name, type=lbtype, description=description)
            assert response is not None
            assert response.status_code == 200
        response = self.globalLoadBalancers.list_monitors(instance_id=self.instance_id)
        assert response is not None
        assert response.status_code == 200

        #List Pools
        for i in range(3):
            name = "testPool"+str(i)
            origins = [{"name": "app-server-"+str(i),
                         "address": "10.10.10.8", "enabled": True}]
            description = "create testpool"+str(i)
            enabled = True
            healthy_origins_threshold=1
            response = self.globalLoadBalancers.create_pool(instance_id=self.instance_id, name=name, origins=origins, description=description, enabled=enabled, healthy_origins_threshold=healthy_origins_threshold)
            assert response is not None
            assert response.status_code == 200
        response = self.globalLoadBalancers.list_pools(instance_id=self.instance_id)
        assert response is not None
        assert response.status_code == 200

if __name__ == '__main__':
    unittest.main()
