# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Integration test code to execute caching api
"""

import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services.caching_api_v1 import CachingApiV1

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')


class TestCachingApiV1(unittest.TestCase):
    """ Test class to call Caching API functions """

    def setUp(self):
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')
        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.cache = CachingApiV1.new_instance(
            crn=self.crn, zone_id=self.zone_id, service_name="cis_services")
        self.cache.set_service_url(self.endpoint)

    def test_1_purge_by_urls(self):
        resp = self.cache.purge_by_urls(
            files=["http://www.example.com/cat_picture.jpg"])
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("success") == True

    def test_1_purge_by_cache_tags(self):
        resp = self.cache.purge_by_cache_tags(
            tags=["some-tags"])
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("success") == True

    def test_1_purge_by_hosts(self):
        resp = self.cache.purge_by_hosts(
            hosts=["www.example-host.com"])
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("success") == True

    def test_1_cache_level_setting(self):
        """ test method get/update cache level settings """
        values = ["basic", "simplified", "aggressive"]

        for value in values:
            resp = self.cache.update_cache_level(
                value=value)
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result")["value"] == value

            resp = self.cache.get_cache_level()
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result")["value"] == value

    def test_1_browser_cache_ttl(self):
        """ test method get/update browser cache ttl value """
        values = [0, 31536000, 14400]

        for value in values:
            resp = self.cache.update_browser_cache_ttl(
                value=value)
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result")["value"] == value

            resp = self.cache.get_browser_cache_ttl()
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result")["value"] == value

    def test_1_development_mode_setting(self):
        """ test method to get/update development mode setting """

        values = ["on", "off"]

        for value in values:
            resp = self.cache.update_development_mode(
                value=value)
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result")["value"] == value

            resp = self.cache.get_development_mode()
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result")["value"] == value

    def test_1_string_sort_setting(self):
        """ test method to get/update string sort setting """

        values = ["on", "off"]

        for value in values:
            resp = self.cache.update_query_string_sort(
                value=value)
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result")["value"] == value

            resp = self.cache.get_query_string_sort()
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get("result")["value"] == value

    def test_1_purge_all(self):
        resp = self.cache.purge_all()
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("success") == True


if __name__ == '__main__':
    unittest.main()
