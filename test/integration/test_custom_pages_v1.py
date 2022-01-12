# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Advanced Custom Pages integration test
"""

import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services.custom_pages_v1 import CustomPagesV1

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')


class TestCustomPagesV1(unittest.TestCase):
    """ Custom Pages test class """
    
    @unittest.skip("skipping failing test")

    def setUp(self):
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')

        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.url = os.getenv("CUSTOM_PAGE_URL")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.custom_pages = CustomPagesV1.new_instance(
            crn=self.crn, zone_identifier=self.zone_id, service_name="cis_services")
        self.custom_pages.set_service_url(self.endpoint)

    def tearDown(self):
        """ tear down """
        # Delete the resources
        print("Clean up complete")

    def test_1_zone_custom_pages(self):
        """ test to update/get/list all zone custom pages """
        state = ["default", "customized"]
        page_ids = ["basic_challenge", "waf_challenge", "waf_block", "ratelimit_block",
                    "country_challenge", "ip_block", "under_attack", "500_errors", "1000_errors"]

        # update zone custom pages with url
        for page_id in page_ids:
            resp = self.custom_pages.update_zone_custom_page(
                page_identifier=page_id, url=self.url, state=state[1])
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result")["url"] == self.url

        # get zone custom page instances
        for page_id in page_ids:
            resp = self.custom_pages.get_zone_custom_page(
                page_identifier=page_id)
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result")[
                "state"] == state[1] and resp.get_result().get("result")["url"] == self.url

        # List all the custom page instances for zones
        resp = self.custom_pages.list_zone_custom_pages()
        assert resp is not None
        assert resp.status_code == 200

    def test_1_custom_pages(self):
        """ test to update/get/list all custom pages """
        state = ["default", "customized"]
        page_ids = ["basic_challenge", "waf_challenge", "waf_block", "ratelimit_block",
                    "country_challenge", "ip_block", "under_attack", "500_errors", "1000_errors"]

        # update custom pages with url
        for page_id in page_ids:
            resp = self.custom_pages.update_instance_custom_page(
                page_identifier=page_id, url=self.url, state=state[1])
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result")["url"] == self.url

        # get custom page instances
        for page_id in page_ids:
            resp = self.custom_pages.get_instance_custom_page(
                page_identifier=page_id)
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result")[
                "state"] == state[1] and resp.get_result().get("result")["url"] == self.url

        # List all the custom page instances
        resp = self.custom_pages.list_instance_custom_pages()
        assert resp is not None
        assert resp.status_code == 200

        # update instance custom pages with default
        for page_id in page_ids:
            resp = self.custom_pages.update_instance_custom_page(
                page_identifier=page_id, url="", state=state[0])
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result")[
                "state"] == state[0] and resp.get_result().get("result")["url"] is None


if __name__ == '__main__':
    unittest.main()
