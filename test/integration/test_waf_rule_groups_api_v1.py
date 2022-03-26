# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.
"""
Integration test code to execute waf rule groups api functions
"""
import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services.waf_rule_groups_api_v1 import WafRuleGroupsApiV1
from ibm_cloud_networking_services.waf_rule_packages_api_v1 import WafRulePackagesApiV1

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')


class TestWafRuleGroupsApiV1 (unittest.TestCase):

    @unittest.skip("Authentication failing")

    def setUp(self):
        """ test case setup """
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')

        self.endpoint = os.getenv("API_ENDPOINT")
        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        # create waf rule groups api record class object
        self.wafRuleGroupsApi = WafRuleGroupsApiV1.new_instance(
            crn=self.crn, zone_id=self.zone_id, service_name="cis_services")
        self.wafRuleGroupsApi.set_service_url(self.endpoint)
        self.wafRulePackagesApi = WafRulePackagesApiV1.new_instance(
            crn=self.crn, zone_id=self.zone_id, service_name="cis_services")
        self.wafRulePackagesApi.set_service_url(self.endpoint)

    def tearDown(self):
        """ tear down """
        # Delete the resources
        print("Clean up complete")

    ################## waf_rule_groups positive integration test cases ###################

    def test_1_waf_rule_groups(self):
        """ list all waf rule groups """

        response = self.wafRulePackagesApi.list_waf_packages()
        assert response is not None and response.result.get("success") is True

        results = response.result.get("result")
        all_waf_pkg_ids = []
        # extract all package ids
        for i in results:
            all_waf_pkg_ids.append(str(i.get("id")))
        check = True
        # list waf rule groups for each package id
        for i in all_waf_pkg_ids:
            self.pkg_id = str(i)
            response = self.wafRuleGroupsApi.list_waf_rule_groups(
                pkg_id=self.pkg_id).get_result()
            assert response is not None and response.get('success') is True
            if len(response.get("result")) != 0 and check is True:
                # store a single group id details to be used in later test cases
                grp_res = response.get("result")
                self.group_id = grp_res[0].get("id")
                self.name = grp_res[0].get("name")
                self.mode = grp_res[0].get("mode")
                self.rules_count = grp_res[0].get("rules_count")
                self.pkg_id2 = self.pkg_id
                check = False

        """list particular waf rule group on the basis of name and other params"""
        self.page = 1
        self.per_page = 50
        self.order = "mode"
        self.direction = "desc"
        self.match = "all"

        response = self.wafRuleGroupsApi.list_waf_rule_groups(pkg_id=self.pkg_id2, name=self.name, mode=self.mode, rules_count=self.rules_count,
                                                              page=self.page, per_page=self.per_page, order=self.order, direction=self.direction, match=self.match).get_result()
        assert response is not None and response.get("success") is True

        """ get waf rule group """
        response = self.wafRuleGroupsApi.get_waf_rule_group(
            pkg_id=self.pkg_id2, group_id=self.group_id).get_result()
        assert response is not None and response.get('success') is True

        """ update waf rule group """
        if self.mode == "on":
            mode_list = ["off", "on"]
        elif self.mode == "off":
            mode_list = ["on", "off"]
        for self.mode in mode_list:
            response = self.wafRuleGroupsApi.update_waf_rule_group(
                pkg_id=self.pkg_id2, group_id=self.group_id, mode=self.mode).get_result()
            assert response is not None and response.get('success') is True

    ################## Negative test cases ###################

    def test_2_waf_rule_groups(self):
        self.pkg_id = "c504870194831cd12c3fc0284f294abb"
        self.group_id = "c504870194831cd12c3fc0284f294abb"
        self.mode = ""
        """ list waf rule group method without pkg_id """
        with self.assertRaises(ValueError) as val:
            self.wafRuleGroupsApi.list_waf_rule_groups(
                pkg_id=None).get_result()
            self.assertEqual(val.exception.msg, 'pkg_id must be provided')

        """ get waf rule group method without pkg_id """
        with self.assertRaises(ValueError) as val:
            self.wafRuleGroupsApi.get_waf_rule_group(
                pkg_id=None, group_id=self.group_id).get_result()
            self.assertEqual(val.exception.msg, 'pkg_id must be provided')

        """ get waf rule group method without group_id """
        with self.assertRaises(ValueError) as val:
            self.wafRuleGroupsApi.get_waf_rule_group(
                pkg_id=self.pkg_id, group_id=None).get_result()
            self.assertEqual(val.exception.msg, 'group_id must be provided')

        """ update waf rule group method without pkg_id """
        with self.assertRaises(ValueError) as val:
            self.wafRuleGroupsApi.update_waf_rule_group(
                pkg_id=None, group_id=self.group_id, mode=self.mode).get_result()
            self.assertEqual(val.exception.msg, 'pkg_id must be provided')

        """ update waf rule group method without group_id """
        with self.assertRaises(ValueError) as val:
            self.wafRuleGroupsApi.update_waf_rule_group(
                pkg_id=self.pkg_id, group_id=None, mode=self.mode).get_result()
            self.assertEqual(val.exception.msg, 'group_id must be provided')


if __name__ == '__main__':
    unittest.main()
