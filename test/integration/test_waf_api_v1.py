# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Integration test code to execute waf api
"""

import os
import unittest
from ibm_cloud_networking_services import WafApiV1


class TestWafApiV1(unittest.TestCase):
    """ WAF API test class """

    def setUp(self):
        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.waf = WafApiV1.new_instance(
            crn=self.crn, zone_id=self.zone_id, service_name="cis_services")
        self.waf.set_service_url(self.endpoint)

    def tearDown(self):
        """ tear down """
        # Delete the resources
        print("Clean up complete")

    def test_1_waf_setting(self):
        """ test to set/get WAF value """

        values = ["on", "off"]

        for value in values:
            resp = self.waf.update_waf_settings(value=value)
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result")["value"] == value

            resp = self.waf.get_waf_settings()
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result")["value"] == value


if __name__ == '__main__':
    unittest.main()
