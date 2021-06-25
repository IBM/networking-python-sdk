# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Integration test code for page rule service
"""

import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services.page_rule_api_v1 import PageRuleApiV1

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')


class TestPageRuleApiV1(unittest.TestCase):
    """ Page Rule API test class """

    @unittest.skip("skipping")

    def setUp(self):
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')

        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.url = os.getenv("URL_MATCH")
        self.url_change = os.getenv("CHANGE_URL_MATCH")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.rule = PageRuleApiV1.new_instance(
            crn=self.crn, zone_id=self.zone_id, service_name="cis_services")
        self.rule.set_service_url(self.endpoint)
        self._clean_up_page_rules()

    def tearDown(self):
        """ tear down """
        # Delete the resources
        self._clean_up_page_rules()
        print("Clean up complete")

    def _clean_up_page_rules(self):
        resp = self.rule.list_page_rules()
        assert resp is not None
        assert resp.status_code == 200
        if resp.get_result().get('result') is not None:
            rules = resp.get_result().get('result')
            for rule in rules:
                self.rule.delete_page_rule(rule_id=rule.get("id"))

    def test_1_page_rule_url_action(self):
        """ test to create/update/change/delete/get page rule url value """

        target = [
            {
                "target": "url",
                "constraint": {
                    "operator": "matches",
                    "value": self.url
                }
            }
        ]
        action = [
            {
                "id": "disable_security"
            },
            {
                "id": "browser_check",
                "value": "off"
            }
        ]
        # create page rule
        resp = self.rule.create_page_rule(targets=target, actions=action,
                                          priority=1, status="active")
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get('result')['targets'][0].get(
            'constraint').get('value') == self.url

        rule_id = resp.get_result().get('result')["id"]
        target = [
            {
                "target": "url",
                "constraint": {
                    "operator": "matches",
                    "value": self.url_change
                }
            }
        ]

        # change page rule
        resp = self.rule.change_page_rule(rule_id=rule_id, targets=target, actions=action,
                                          priority=1, status="active")
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get('result')['targets'][0].get(
            'constraint').get('value') == self.url_change

        target = [
            {
                "target": "url",
                "constraint": {
                    "operator": "matches",
                    "value": self.url
                }
            }
        ]

        # update page rule
        resp = self.rule.update_page_rule(rule_id=rule_id, targets=target, actions=action,
                                          priority=1, status="active")
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get('result')['targets'][0].get(
            'constraint').get('value') == self.url

        # get page rule
        resp = self.rule.get_page_rule(
            rule_id=rule_id)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get('result')['targets'][0].get(
            'constraint').get('value') == self.url

        # delete page rule
        resp = self.rule.delete_page_rule(
            rule_id=rule_id)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get('result')['id'] == rule_id

    def test_1_page_rule_browser_check_action(self):
        """ test to create/update/change/delete/get page rule browser check value """

        target = [
            {
                "target": "url",
                "constraint": {
                    "operator": "matches",
                    "value": self.url
                }
            }
        ]
        action = [
            {
                "id": "browser_check",
                "value": "off"
            }
        ]

        # create page rule
        resp = self.rule.create_page_rule(targets=target, actions=action,
                                          priority=1, status="active")
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get('result')['targets'][0].get(
            'constraint').get('value') == self.url

        rule_id = resp.get_result().get('result')["id"]
        action = [
            {
                "id": "browser_check",
                "value": "on"
            }
        ]

        # change page rule
        resp = self.rule.change_page_rule(rule_id=rule_id, targets=target, actions=action,
                                          priority=1, status="active")
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get('result')['targets'][0].get(
            'constraint').get('value') == self.url
        assert resp.get_result().get('result')['actions'][0].get(
            'id') == 'browser_check' and resp.get_result().get('result')['actions'][0].get(
            'value') == 'on'

        action = [
            {
                "id": "browser_check",
                "value": "off"
            }
        ]

        # update page rule
        resp = self.rule.update_page_rule(rule_id=rule_id, targets=target, actions=action,
                                          priority=1, status="active")
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get('result')['targets'][0].get(
            'constraint').get('value') == self.url
        assert resp.get_result().get('result')['actions'][0].get(
            'id') == 'browser_check' and resp.get_result().get('result')['actions'][0].get(
            'value') == 'off'

        # get page rule
        resp = self.rule.get_page_rule(
            rule_id=rule_id)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get('result')['targets'][0].get(
            'constraint').get('value') == self.url

        # delete page rule
        resp = self.rule.delete_page_rule(
            rule_id=rule_id)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get('result')['id'] == rule_id

    def test_1_page_rule_disable_security_action(self):
        """ test to create/update/change/delete/get page rule disable security value """

        target = [
            {
                "target": "url",
                "constraint": {
                    "operator": "matches",
                    "value": self.url
                }
            }
        ]
        action = [
            {
                "id": "disable_security"
            }
        ]

        # create page rule
        resp = self.rule.create_page_rule(targets=target, actions=action,
                                          priority=1, status="active")
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get('result')['targets'][0].get(
            'constraint').get('value') == self.url

        rule_id = resp.get_result().get('result')["id"]
        action = [
            {
                "id": "browser_check",
                "value": "off"
            }
        ]

        # update page rule
        resp = self.rule.update_page_rule(rule_id=rule_id, targets=target, actions=action,
                                          priority=1, status="active")
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get('result')['targets'][0].get(
            'constraint').get('value') == self.url
        for i in range(len(resp.get_result().get('result')['actions'])):
            assert resp.get_result().get('result')['actions'][i].get(
                "id") != "disable_security"

        # get page rule
        resp = self.rule.get_page_rule(
            rule_id=rule_id)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get('result')['targets'][0].get(
            'constraint').get('value') == self.url
        for i in range(len(resp.get_result().get('result')['actions'])):
            assert resp.get_result().get('result')['actions'][i].get(
                "id") != "disable_security"

        # delete page rule
        resp = self.rule.delete_page_rule(
            rule_id=rule_id)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get('result')['id'] == rule_id

    def test_1_page_rule_server_exclude_action(self):
        """ test to create/update/change/delete/get page rule service side exclude value """
        action_id = "server_side_exclude"
        target = [
            {
                "target": "url",
                "constraint": {
                    "operator": "matches",
                    "value": self.url
                }
            }
        ]
        action = [
            {
                "id": action_id,
                "value": "off"
            }
        ]

        # create page rule
        resp = self.rule.create_page_rule(targets=target, actions=action,
                                          priority=1, status="active")
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get('result')['targets'][0].get(
            'constraint').get('value') == self.url

        rule_id = resp.get_result().get('result')["id"]
        action = [
            {
                "id": action_id,
                "value": "on"
            }
        ]

        # change page rule
        resp = self.rule.change_page_rule(rule_id=rule_id, targets=target, actions=action,
                                          priority=1, status="active")
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get('result')['targets'][0].get(
            'constraint').get('value') == self.url
        assert resp.get_result().get('result')['actions'][0].get(
            'id') == action_id and resp.get_result().get('result')['actions'][0].get(
            'value') == 'on'

        action = [
            {
                "id": action_id,
                "value": "off"
            }
        ]

        # update page rule
        resp = self.rule.update_page_rule(rule_id=rule_id, targets=target, actions=action,
                                          priority=1, status="active")
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get('result')['targets'][0].get(
            'constraint').get('value') == self.url
        assert resp.get_result().get('result')['actions'][0].get(
            'id') == action_id and resp.get_result().get('result')['actions'][0].get(
            'value') == 'off'

        # get page rule
        resp = self.rule.get_page_rule(
            rule_id=rule_id)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get('result')['targets'][0].get(
            'constraint').get('value') == self.url
        assert resp.get_result().get('result')['actions'][0].get(
            'id') == action_id and resp.get_result().get('result')['actions'][0].get(
            'value') == 'off'

        # delete page rule
        resp = self.rule.delete_page_rule(
            rule_id=rule_id)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get('result')['id'] == rule_id

    def test_1_page_rule_url_forward_settings(self):
        """ test to create/update/change/delete/get page forward rule settings """
        action_id = "forwarding_url"
        target = [
            {
                "target": "url",
                "constraint": {
                    "operator": "matches",
                    "value": self.url
                }
            }
        ]
        action = [
            {
                "id": action_id,
                "value": {
                    "url": "https://" + self.url_change,
                    "status_code": 301
                }
            }
        ]

        # create page rule
        resp = self.rule.create_page_rule(targets=target, actions=action,
                                          priority=1, status="active")
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get('result')['targets'][0].get(
            'constraint').get('value') == self.url
        rule_id = resp.get_result().get('result')["id"]

        value = {
            "url": "https://" + self.url_change,
            "status_code": 302
        }
        action = [
            {
                "id": action_id,
                "value": value
            }
        ]

        # change page rule
        resp = self.rule.change_page_rule(rule_id=rule_id, targets=target, actions=action,
                                          priority=1, status="active")
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get('result')['targets'][0].get(
            'constraint').get('value') == self.url
        assert resp.get_result().get('result')['actions'][0].get(
            'id') == action_id and resp.get_result().get('result')['actions'][0].get(
            'value') == value

       # get page rule
        resp = self.rule.get_page_rule(
            rule_id=rule_id)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get('result')['targets'][0].get(
            'constraint').get('value') == self.url
        assert resp.get_result().get('result')['actions'][0].get(
            'id') == action_id and resp.get_result().get('result')['actions'][0].get(
            'value') == value

        value = {
            "url": "https://" + self.url_change,
            "status_code": 301
        }
        action = [
            {
                "id": action_id,
                "value": value
            }
        ]
        # update page rule
        resp = self.rule.update_page_rule(rule_id=rule_id, targets=target, actions=action,
                                          priority=1, status="active")
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get('result')['targets'][0].get(
            'constraint').get('value') == self.url
        assert resp.get_result().get('result')['actions'][0].get(
            'id') == action_id and resp.get_result().get('result')['actions'][0].get(
            'value') == value

        # get page rule
        resp = self.rule.get_page_rule(
            rule_id=rule_id)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get('result')['targets'][0].get(
            'constraint').get('value') == self.url
        assert resp.get_result().get('result')['actions'][0].get(
            'id') == action_id and resp.get_result().get('result')['actions'][0].get(
            'value') == value

        # delete page rule
        resp = self.rule.delete_page_rule(
            rule_id=rule_id)
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get('result')['id'] == rule_id

    def test_1_page_rule_all_setting(self):
        """ test to create/update/change/delete/get page rule setting """

        actions = {
            "browser_check": ["on", "off"],
            "server_side_exclude": ["on", "off"],
            "email_obfuscation": ["on", "off"],
            "ip_geolocation": ["on", "off"],
            "explicit_cache_control": ["on", "off"],
            "cache_deception_armor": ["on", "off"],
            "waf": ["on", "off"],
            "ssl": ["strict", "off", "flexible", "full"],
            "browser_cache_ttl": [1800, 3600, 7200, 10800, 14400, 18000, 28800, 43200, 57600, 72000, 86400, 172800, 259200, 345600, 432000, 691200, 1382400, 2073600, 2678400, 5356800, 16070400, 31536000],
            "security_level": ["essentially_off", "low", "medium", "high", "under_attack"],
            "cache_level": ["bypass", "aggressive", "basic", "simplified", "cache_everything"],
            "edge_cache_ttl": [1800, 3600, 7200, 10800, 14400, 18000, 28800, 43200, 57600, 72000, 86400, 172800, 259200, 345600, 432000, 518400, 604800, 1209600, 2419200],
        }

        target = [
            {
                "target": "url",
                "constraint": {
                    "operator": "matches",
                    "value": self.url
                }
            }
        ]

        # for loop for create page rule
        for action_id in actions.keys():
            action = [
                {
                    "id": action_id,
                    "value": actions.get(action_id)[0]
                }
            ]
            print("Test Case : ", action_id)

            # create page rule
            resp = self.rule.create_page_rule(targets=target, actions=action,
                                              priority=1, status="active")
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get('result')['targets'][0].get(
                'constraint').get('value') == self.url
            rule_id = resp.get_result().get('result')["id"]

            # for loop to get values corresponding to actions
            for value in actions.get(action_id):
                action = [
                    {
                        "id": action_id,
                        "value": value
                    }
                ]

                # change page rule
                resp = self.rule.change_page_rule(rule_id=rule_id, targets=target, actions=action,
                                                  priority=1, status="active")
                assert resp is not None
                assert resp.status_code == 200
                assert resp.get_result().get('result')['targets'][0].get(
                    'constraint').get('value') == self.url
                assert resp.get_result().get('result')['actions'][0].get(
                    'id') == action_id and resp.get_result().get('result')['actions'][0].get(
                    'value') == value

                # get page rule
                resp = self.rule.get_page_rule(rule_id=rule_id)
                assert resp is not None
                assert resp.status_code == 200
                assert resp.get_result().get('result')['targets'][0].get(
                    'constraint').get('value') == self.url
                assert resp.get_result().get('result')['actions'][0].get(
                    'id') == action_id and resp.get_result().get('result')['actions'][0].get(
                    'value') == value

            for value in actions.get(action_id):
                action = [
                    {
                        "id": action_id,
                        "value": value
                    }
                ]
                # update page rule
                resp = self.rule.update_page_rule(rule_id=rule_id, targets=target, actions=action,
                                                  priority=1, status="active")
                assert resp is not None
                assert resp.status_code == 200
                assert resp.get_result().get('result')['targets'][0].get(
                    'constraint').get('value') == self.url
                assert resp.get_result().get('result')['actions'][0].get(
                    'id') == action_id and resp.get_result().get('result')['actions'][0].get(
                    'value') == value

                # get page rule
                resp = self.rule.get_page_rule(rule_id=rule_id)
                assert resp is not None
                assert resp.status_code == 200
                assert resp.get_result().get('result')['targets'][0].get(
                    'constraint').get('value') == self.url
                assert resp.get_result().get('result')['actions'][0].get(
                    'id') == action_id and resp.get_result().get('result')['actions'][0].get(
                    'value') == value

            # delete page rule
            resp = self.rule.delete_page_rule(
                rule_id=rule_id)
            assert resp is not None
            assert resp.status_code == 200
            assert resp.get_result().get('result')['id'] == rule_id


if __name__ == '__main__':
    unittest.main()
