# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.
"""
Integration test code to execute waf rule packages api functions
"""
import os
import unittest
from ibm_cloud_networking_services.waf_rule_packages_api_v1 import WafRulePackagesApiV1


class TestWafRulePackagesApiV1 (unittest.TestCase):
    def setUp(self):
        """ test case setup """
        self.endpoint = os.getenv("API_ENDPOINT")
        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        # create waf rule packages api record class object
        self.wafRulePackagesApi = WafRulePackagesApiV1.new_instance(
            crn=self.crn, zone_id=self.zone_id, service_name="cis_services")
        self.wafRulePackagesApi.set_service_url(self.endpoint)

    def tearDown(self):
        """ tear down """
        # Delete the resources
        print("Clean up complete")

    ################## waf rule packages positive integration test cases ###################

    def test_1_waf_rule_packages(self):
        """ list waf packages on the basis of specific name """
        self.name = "USER"
        self.page = 1
        self.per_page = 50
        self.order = "status"
        self.direction = "desc"
        self.match = "all"
        response = self.wafRulePackagesApi.list_waf_packages(
            page=self.page, per_page=self.per_page, order=self.order, direction=self.direction, match=self.match).get_result()
        assert response is not None and response.get('success') is True

        """ list all waf packages  """
        self.name = None
        self.page = 1
        self.per_page = 50
        self.order = "status"
        self.direction = "desc"
        self.match = "all"
        response = self.wafRulePackagesApi.list_waf_packages(
            page=self.page, per_page=self.per_page, order=self.order, direction=self.direction, match=self.match).get_result()
        assert response is not None and response.get('success') is True
        results = response.get("result")
        anomaly_waf_pkg_id = None
        all_waf_pkg_ids = []
        for i in results:
            all_waf_pkg_ids.append(str(i.get("id")))
            if str(i.get("detection_mode")) == "anomaly":
                anomaly_waf_pkg_id = str(i.get("id"))

        """ get particular waf package  """
        for self.package_id in all_waf_pkg_ids:
            response = self.wafRulePackagesApi.get_waf_package(
                package_id=self.package_id).get_result()
            assert response is not None and response.get('success') is True

        """ update particular waf package  """
        sens = ["high", "medium", "low", "off"]
        am = ["simulate", "block", "challenge"]

        for self.sensitivity in sens:
            for self.action_mode in am:
                response = self.wafRulePackagesApi.update_waf_package(
                    package_id=anomaly_waf_pkg_id, sensitivity=self.sensitivity, action_mode=self.action_mode).get_result()
                assert response is not None and response.get('success') is True

    ################## Negative test cases ###################

    def test_2_waf_rule_packages(self):
        self.sensitivity = ""
        self.action_mode = ""

        """ get waf package method without package_id """
        with self.assertRaises(ValueError) as val:
            self.wafRulePackagesApi.get_waf_package(
                package_id=None).get_result()
            self.assertEqual(val.exception.msg, 'package_id must be provided')

        """ update waf package method without package_id """
        with self.assertRaises(ValueError) as val:
            self.wafRulePackagesApi.update_waf_package(
                package_id=None, sensitivity=self.sensitivity, action_mode=self.action_mode).get_result()
            self.assertEqual(val.exception.msg, 'package_id must be provided')


if __name__ == '__main__':
    unittest.main()
