# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Integration test code for Routing
"""

import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services.routing_v1 import RoutingV1

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')


class TestRoutingApiV1(unittest.TestCase):
    """ Routing API test class """

    @unittest.skip("skipping")

    def setUp(self):
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')

        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.route = RoutingV1.new_instance(
            crn=self.crn, zone_identifier=self.zone_id, service_name="cis_services")
        self.route.set_service_url(self.endpoint)

    def tearDown(self):
        """ tear down """
        # Delete the resources
        print("Clean up complete")

    def test_1_routing_smart_routing(self):
        value = "on"
        resp = self.route.update_smart_routing(value=value)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")["id"] == "smart_routing"
        assert resp.get_result().get("result")["value"] == value

        resp = self.route.get_smart_routing()
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")["id"] == "smart_routing"
        assert resp.get_result().get("result")["value"] == value

        value = "off"
        resp = self.route.update_smart_routing(value=value)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")["id"] == "smart_routing"
        assert resp.get_result().get("result")["value"] == value


if __name__ == '__main__':
    unittest.main()
