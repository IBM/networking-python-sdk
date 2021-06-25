# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Integration test code to execute user agent blocking rules functions
"""

import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services.user_agent_blocking_rules_v1 import UserAgentBlockingRulesV1

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')


class TestUserAgentBlockingRulesV1 (unittest.TestCase):
    @unittest.skip("skipping")

    def setUp(self):
        """ test case setup """
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')

        self.endpoint = os.getenv("API_ENDPOINT")
        self.crn = os.getenv("CRN")
        self.zone_identifier = os.getenv("ZONE_ID")
        # create user agent blocking rules record class object
        self.userAgentBlockingRules = UserAgentBlockingRulesV1.new_instance(
            crn=self.crn, zone_identifier=self.zone_identifier, service_name="cis_services")
        self.userAgentBlockingRules.set_service_url(self.endpoint)

    def tearDown(self):
        """ tear down """
        # Delete the resources
        print("Clean up complete")

    ################## user agent rule positive integration test cases ###################

    def test_1_user_agent_rule(self):
        """create a user agent rule"""
        modes = ["block", "challenge", "js_challenge"]
        val_string = "Mozilla/{0}.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4"
        rule_id = []
        x = 5
        for self.mode in modes:
            self.configuration = {"target": "ua",
                                  "value": val_string.format(str(x))}
            self.paused = True
            self.description = "Test user agent rule for {0}".format(self.mode)
            response = self.userAgentBlockingRules.create_zone_user_agent_rule(
                mode=self.mode, configuration=self.configuration, paused=self.paused, description=self.description).get_result()
            x = x+1
            assert response is not None and response.get('success') is True
            assert response.get("result")["id"] is not None
            rule_id.append(response.get("result")["id"])

        """get user agent rule"""
        for self.useragent_rule_identifier in rule_id:
            response = self.userAgentBlockingRules.get_user_agent_rule(
                useragent_rule_identifier=self.useragent_rule_identifier).get_result()
            assert response is not None and response.get('success') is True

        """list all user agent rules"""
        self.page = 1
        self.per_page = 20
        response = self.userAgentBlockingRules.list_all_zone_user_agent_rules(
            page=self.page, per_page=self.per_page).get_result()
        assert response is not None and response.get('success') is True

        """update user agent rule"""
        self.useragent_rule_identifier = rule_id[0]
        self.mode = "challenge"
        self.configuration = {"target": "ua",
                              "value": val_string.format(str(x))}
        self.paused = False
        self.description = "Test user agent rule for challenge 2"
        response = self.userAgentBlockingRules.update_user_agent_rule(
            useragent_rule_identifier=self.useragent_rule_identifier, mode=self.mode, configuration=self.configuration, paused=self.paused, description=self.description).get_result()
        assert response is not None and response.get('success') is True

        """delete user agent rule"""
        for self.useragent_rule_identifier in rule_id:
            response = self.userAgentBlockingRules.delete_zone_user_agent_rule(
                useragent_rule_identifier=self.useragent_rule_identifier).get_result()
            assert response is not None and response.get('success') is True

    ################## Negative test cases ###################

    def test_2_user_agent_rule(self):
        """variables assignments"""
        self.mode = "block"
        self.configuration = {"target": "ua",
                              "value": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4"
                              }
        self.paused = True
        self.description = "Test user agent rule"
        self.useragent_rule_identifier = "0218ec392eb34aebaff2106e8a1914ae"

        """ update user agent rule method without useragent_rule_identifier """
        with self.assertRaises(ValueError) as val:
            self.userAgentBlockingRules.update_user_agent_rule(
                useragent_rule_identifier=None, mode=self.mode, configuration=self.configuration, paused=self.paused, description=self.description).get_result()
            self.assertEqual(val.exception.msg,
                             'useragent_rule_identifier must be provided')

        """ get user agent rule method without useragent_rule_identifier """
        with self.assertRaises(ValueError) as val:
            self.userAgentBlockingRules.get_user_agent_rule(
                useragent_rule_identifier=None).get_result()
            self.assertEqual(val.exception.msg,
                             'useragent_rule_identifier must be provided')

        """ delete user agent rule method without useragent_rule_identifier """
        with self.assertRaises(ValueError) as val:
            self.userAgentBlockingRules.delete_zone_user_agent_rule(
                useragent_rule_identifier=None).get_result()
            self.assertEqual(val.exception.msg,
                             'useragent_rule_identifier must be provided')


if __name__ == '__main__':
    unittest.main()
