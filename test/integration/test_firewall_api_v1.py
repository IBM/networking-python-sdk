# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Integration test code to execute firewall security level setting
"""

import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services import FirewallApiV1

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')


class TestFirewallApiV1(unittest.TestCase):
    """ Test class to call Firewall API functions """

    @unittest.skip("Authentication failing")

    def setUp(self):
        """ test case setup """
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')

        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.firewall = FirewallApiV1.new_instance(
            crn=self.crn, zone_identifier=self.zone_id, service_name="cis_services")
        self.firewall.set_service_url(self.endpoint)

    def tearDown(self):
        """ tear down """
        # Delete the resources
        print("Clean up complete")

    def test_1_firewall_security_level_actions(self):
        """ test to set/get security level setting to essentially_off/low/medium/high/under_attack """

        values = ["essentially_off", "low", "high", "under_attack", "medium"]

        for value in values:
            resp = self.firewall.set_security_level_setting(value=value)
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result")["value"] == value

            resp = self.firewall.get_security_level_setting()
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result")["value"] == value


if __name__ == '__main__':
    unittest.main()
