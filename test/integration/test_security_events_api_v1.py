# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Integration test code for security events
"""

import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services.security_events_api_v1 import SecurityEventsApiV1

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')


class TestSecurityEventsApiV1(unittest.TestCase):
    """ Security Events API test class """

    @unittest.skip("skipping")

    def setUp(self):
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')

        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.event = SecurityEventsApiV1.new_instance(
            crn=self.crn, zone_id=self.zone_id, service_name="cis_services")
        self.event.set_service_url(self.endpoint)

    def tearDown(self):
        """ tear down """
        # Delete the resources
        print("Clean up complete")

    def test_1_security_events(self):
        resp = self.event.security_events()
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("success") == True


if __name__ == '__main__':
    unittest.main()
