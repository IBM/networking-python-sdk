# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Integration test code to execute global load balancer monitor functions
"""

import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services.global_load_balancer_monitor_v1 import GlobalLoadBalancerMonitorV1

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')


class TestGlobalLoadBalancerMonitorV1 (unittest.TestCase):

    @unittest.skip("Authentication failing")
    
    def setUp(self):
        """ test case setup """
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')

        self.endpoint = os.getenv("API_ENDPOINT")
        self.crn = os.getenv("CRN")
        # create global load balancer monitor record class object
        self.globalLoadBalancerMonitor = GlobalLoadBalancerMonitorV1.new_instance(
            crn=self.crn, service_name="cis_services")
        self.globalLoadBalancerMonitor.set_service_url(self.endpoint)
        self._cleanup_monitors()

    def tearDown(self):
        """ tear down """
        # Delete the resources
        self._cleanup_monitors()
        print("Clean up complete")

    def _cleanup_monitors(self):
        response = self.globalLoadBalancerMonitor.list_all_load_balancer_monitors()
        assert response is not None
        assert response.status_code == 200
        monitors = {}
        monitors = response.get_result().get("result")
        for monitor in monitors:
            self.globalLoadBalancerMonitor.delete_load_balancer_monitor(
                monitor_identifier=monitor.get("id"))

    ################## load_balancer_monitors integration test cases ###################

    def test_1_load_balancer_monitors(self):
        """ create GLB monitor """
        """ create GLB monitor for http/https type """
        self.expected_body = "alive"
        self.expected_codes = "2xx"
        self.type = "http"
        self.description = "Test LB montior1"
        self.method = "GET"
        self.port = 80
        self.path = "/auto/test"
        self.header = {"Host": ["example.com"], "X-App-ID": ["abc123"]}
        self.timeout = 3
        self.retries = 0
        self.interval = 90
        self.follow_redirects = True
        self.allow_insecure = True

        response = self.globalLoadBalancerMonitor.create_load_balancer_monitor(
            expected_codes=self.expected_codes, type=self.type,
            description=self.description, method=self.method, port=self.port,
            path=self.path, header=self.header, timeout=self.timeout, retries=self.retries,
            interval=self.interval, follow_redirects=self.follow_redirects,
            expected_body=self.expected_body, allow_insecure=self.allow_insecure).get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        monitor_id1 = result.get('id')

        """ create GLB monitor for tcp type """
        self.type = "tcp"
        self.description = "Test LB montior2"
        self.method = "GET"
        self.port = 20
        self.path = "/auto/test"
        self.header = {"Host": ["example.com"], "X-App-ID": ["abc123"]}
        self.timeout = 3
        self.retries = 0
        self.interval = 90

        response = self.globalLoadBalancerMonitor.create_load_balancer_monitor(
            type=self.type, description=self.description,
            method=self.method, port=self.port, path=self.path, header=self.header,
            timeout=self.timeout, retries=self.retries, interval=self.interval).get_result()
        assert response is not None and response.get('success') is True
        result = response.get('result')
        monitor_id2 = result.get('id')

        """ list all GLB monitors """
        response = self.globalLoadBalancerMonitor.list_all_load_balancer_monitors(
        ).get_result()
        assert response is not None and response.get('success') is True

        """ get GLB monitor """
        monitor_list = [monitor_id1, monitor_id2]
        for self.monitor_identifier in monitor_list:
            response = self.globalLoadBalancerMonitor.get_load_balancer_monitor(
                monitor_identifier=self.monitor_identifier).get_result()
            assert response is not None and response.get('success') is True

        """edit GLB monitor"""
        """ edit GLB monitor for http/https"""

        self.expected_body = "new page"
        self.expected_codes = "2xx"
        self.type = "https"
        self.description = "Test LB montior3"
        self.method = "GET"
        self.port = 80
        self.path = "/auto/test"
        self.header = {"Host": ["example.com"], "X-App-ID": ["abc123"]}
        self.timeout = 3
        self.retries = 0
        self.interval = 90
        self.follow_redirects = False
        self.allow_insecure = False

        response = self.globalLoadBalancerMonitor.edit_load_balancer_monitor(
            monitor_identifier=monitor_id1,
            expected_codes=self.expected_codes, type=self.type, description=self.description,
            method=self.method, port=self.port, path=self.path, header=self.header, timeout=self.timeout,
            retries=self.retries, interval=self.interval, follow_redirects=self.follow_redirects,
            expected_body=self.expected_body, allow_insecure=self.allow_insecure).get_result()
        assert response is not None and response.get('success') is True

        """ edit GLB monitor for tcp"""

        self.type = "tcp"
        self.description = "Test LB montior4"
        self.method = "GET"
        self.port = 20
        self.path = "/"
        self.header = {"Host": ["example.com"], "X-App-ID": ["abc123"]}
        self.timeout = 3
        self.retries = 0
        self.interval = 90

        response = self.globalLoadBalancerMonitor.edit_load_balancer_monitor(
            monitor_identifier=monitor_id2, type=self.type, description=self.description,
            method=self.method, port=self.port, path=self.path, header=self.header, timeout=self.timeout,
            retries=self.retries, interval=self.interval).get_result()
        assert response is not None and response.get('success') is True

        """delete GLB monitor """
        for self.monitor_identifier in monitor_list:
            response = self.globalLoadBalancerMonitor.delete_load_balancer_monitor(
                monitor_identifier=self.monitor_identifier).get_result()
            assert response is not None and response.get('success') is True

    ################## Negative test cases ###################

    def test_2_load_balancer_monitors(self):
        """ variables """
        self.expected_body = "alive"
        self.expected_codes = "2xx"
        self.type = "https"
        self.description = "Test LB montior1"
        self.method = "GET"
        self.port = 80
        self.path = "/auto/test"
        self.header = {"Host": ["example.com"], "X-App-ID": ["abc123"]}
        self.timeout = 3
        self.retries = 0
        self.interval = 90
        self.monitor_identifier = "bbf53e07352ba94da066eedb9be97a2b"
        self.follow_redirects = False
        self.allow_insecure = False

        """ get load balancer monitor method without monitor_identifier """
        with self.assertRaises(ValueError) as val:
            self.globalLoadBalancerMonitor.get_load_balancer_monitor(
                monitor_identifier=None).get_result()
            self.assertEqual(val.exception.msg,
                             'monitor_identifier must be provided')

        """ edit load balancer method without monitor_identifier """
        with self.assertRaises(ValueError) as val:
            self.globalLoadBalancerMonitor.edit_load_balancer_monitor(
                monitor_identifier=None,
                expected_codes=self.expected_codes, type=self.type, description=self.description,
                method=self.method, port=self.port, path=self.path, header=self.header, timeout=self.timeout,
                retries=self.retries, interval=self.interval, expected_body=self.expected_body).get_result()
            self.assertEqual(val.exception.msg,
                             'monitor_identifier must be provided')

        """ delete load balancer monitor method without monitor_identifier """
        with self.assertRaises(ValueError) as val:
            self.globalLoadBalancerMonitor.delete_load_balancer_monitor(
                monitor_identifier=None).get_result()
            self.assertEqual(val.exception.msg,
                             'monitor_identifier must be provided')


if __name__ == '__main__':
    unittest.main()
