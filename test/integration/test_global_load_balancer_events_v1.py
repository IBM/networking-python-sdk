# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Integration test code to execute global load balancer events functions
"""

import os
import unittest
from ibm_cloud_networking_services.global_load_balancer_events_v1 import GlobalLoadBalancerEventsV1


class TestGlobalLoadBalancerEventsV1 (unittest.TestCase):
    def setUp(self):
        """ test case setup """
        self.endpoint = os.getenv("API_ENDPOINT")
        self.crn = os.getenv("CRN")
        # create global load balancer events record class object
        self.globalLoadBalancerEvents = GlobalLoadBalancerEventsV1.new_instance(
            crn=self.crn, service_name="cis_services")
        self.globalLoadBalancerEvents.set_service_url(self.endpoint)

    def tearDown(self):
        """ tear down """
        # Delete the resources
        print("Clean up complete")

    ################## get_load_balancer_events ###################
    def test_1_get_load_balancer_events(self):
        """ test for success """
        response = self.globalLoadBalancerEvents.get_load_balancer_events().get_result()
        assert response is not None and response.get('success') is True

if __name__ == '__main__':
    unittest.main()
