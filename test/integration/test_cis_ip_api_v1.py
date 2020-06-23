# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Integration test code to execute cis ip api functions
"""
import os
import unittest
from ibm_cloud_networking_services.cis_ip_api_v1 import CisIpApiV1

class TestCisIpApiV1 (unittest.TestCase):
    def setUp(self):
        """ test case setup """
        self.endpoint = os.getenv("API_ENDPOINT")
        # create cis ip api record class object
        self.cisIpApi = CisIpApiV1.new_instance(service_name="cis_services")
        self.cisIpApi.set_service_url(self.endpoint)

    def tearDown(self):
        """ tear down """
        # Delete the resources
        print("Clean up complete")

    ################## list_ips ###################
    def test_1_list_ips(self):
        """ test for success """
        response = self.cisIpApi.list_ips().get_result()
        assert response is not None and response.get('success') is True

if __name__ == '__main__':
    unittest.main()
