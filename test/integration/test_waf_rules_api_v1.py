# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.
"""
Integration test code to execute waf rules api functions
"""
import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services.waf_rules_api_v1 import WafRulesApiV1
from ibm_cloud_networking_services.waf_rule_packages_api_v1 import WafRulePackagesApiV1

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')


class TestWafRulesApiV1 (unittest.TestCase):

    @unittest.skip("Authentication failing")

    def setUp(self):
        """ test case setup """
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')

        self.endpoint = os.getenv("API_ENDPOINT")
        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        # create waf rules api record class object
        self.wafRulesApi = WafRulesApiV1.new_instance(
            crn=self.crn, zone_id=self.zone_id, service_name="cis_services")
        self.wafRulesApi.set_service_url(self.endpoint)
        self.wafRulePackagesApi = WafRulePackagesApiV1.new_instance(
            crn=self.crn, zone_id=self.zone_id, service_name="cis_services")
        self.wafRulePackagesApi.set_service_url(self.endpoint)

    def tearDown(self):
        """ tear down """
        # Delete the resources
        print("Clean up complete")

    ################## list_waf_rules ###################

    def test_1_waf_rules(self):
        """ test for success """
        response = self.wafRulePackagesApi.list_waf_packages()
        assert response is not None and response.result.get("success") is True

        results = response.result.get("result")
        all_waf_pkg_ids = []
        # extract all package ids
        for i in results:
            all_waf_pkg_ids.append(str(i.get("id")))
        check = True
        # list waf rule for each package id
        for i in all_waf_pkg_ids:
            self.package_id = str(i)
            response = self.wafRulesApi.list_waf_rules(
                package_id=self.package_id).get_result()
            assert response is not None and response.get('success') is True
            if len(response.get("result")) != 0 and check is True:
                # store a single rule id details, to be used in later test cases
                rule_res = response.get("result")
                self.identifier = rule_res[0].get("id")
                self.mode = rule_res[0].get("mode")
                self.priority = rule_res[0].get("priority")
                self.group_id = rule_res[0].get("group").get("id")
                self.description = rule_res[0].get("description")
                self.pkg_id = self.package_id
                check = False

        """list particular waf rules on the basis of mode, priority and other params"""
        self.match = "all"
        self.order = "status"
        self.direction = "asc"
        self.page = 1
        self.per_page = 10

        response = self.wafRulesApi.list_waf_rules(package_id=self.pkg_id, mode=self.mode, priority=self.priority, match=self.match, order=self.order,
                                                   group_id=self.group_id, description=self.description, direction=self.direction, page=self.page, per_page=self.per_page).get_result()
        assert response is not None and response.get("success") is True

        """get waf rule"""
        response = self.wafRulesApi.get_waf_rule(
            package_id=self.pkg_id, identifier=self.identifier).get_result()
        assert response is not None and response.get('success') is True

        """update waf rule"""
        cis_modes = ['default', 'disable', 'simulate', 'block', 'challenge']
        owasp_modes = ['on', 'off']
        if self.mode in owasp_modes:
            mode_list = owasp_modes
            mode_name = "owasp"
        else:
            mode_list = cis_modes
            mode_name = "cis"

        for m in mode_list:
            if m != self.mode:
                new_mode = m
                break

        if mode_name == "cis":
            self.cis = {"mode": new_mode}
            self.owasp = None
        else:
            self.owasp = {"mode": new_mode}
            self.cis = None

        response = self.wafRulesApi.update_waf_rule(
            package_id=self.pkg_id, identifier=self.identifier, cis=self.cis, owasp=self.owasp).get_result()
        assert response is not None and response.get('success') is True

    ################## Negative test cases ###################

    def test_2_waf_rules(self):
        self.identifier = ""
        self.package_id = ""
        self.cis = ""
        self.owasp = ""
        """ list waf rule method without package_id """
        with self.assertRaises(ValueError) as val:
            self.wafRulesApi.list_waf_rules(package_id=None).get_result()
            self.assertEqual(val.exception.msg, 'package_id must be provided')

        """ get waf rule method without package_id """
        with self.assertRaises(ValueError) as val:
            self.wafRulesApi.get_waf_rule(
                package_id=None, identifier=self.identifier).get_result()
            self.assertEqual(val.exception.msg, 'package_id must be provided')

        """ get waf rule method without identifier """
        with self.assertRaises(ValueError) as val:
            self.wafRulesApi.get_waf_rule(
                package_id=self.package_id, identifier=None).get_result()
            self.assertEqual(val.exception.msg, 'identifier must be provided')

        """ update waf rule method without package_id """
        with self.assertRaises(ValueError) as val:
            self.wafRulesApi.update_waf_rule(
                package_id=None, identifier=self.identifier, cis=self.cis, owasp=self.owasp).get_result()
            self.assertEqual(val.exception.msg, 'package_id must be provided')

        """ update waf rule method without identifier """
        with self.assertRaises(ValueError) as val:
            self.wafRulesApi.update_waf_rule(
                package_id=self.package_id, identifier=None, cis=self.cis, owasp=self.owasp).get_result()
            self.assertEqual(val.exception.msg, 'identifier must be provided')


if __name__ == '__main__':
    unittest.main()
