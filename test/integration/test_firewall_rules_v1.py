# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.

"""
Integration test code to execute firewall access rules api
"""

import os
import unittest
from dotenv import load_dotenv, find_dotenv
from ibm_cloud_networking_services import FirewallRulesV1
from ibm_cloud_networking_services.filters_v1 import FiltersV1

configFile = "cis.env"

# load the .env file containing your environment variables
try:
    load_dotenv(find_dotenv(filename="cis.env"))
except:
    print('warning: no cis.env file loaded')


class TestFirewallRules(unittest.TestCase):
    """ Test class to call Firewall Access Rules API functions """

    def setUp(self):
        if not os.path.exists(configFile):
            raise unittest.SkipTest(
                'External configuration not available, skipping...')
        self.crn = os.getenv("CRN")
        self.zone_id = os.getenv("ZONE_ID")
        self.endpoint = os.getenv("API_ENDPOINT")
        self.x_auth_user_token = os.getenv("CIS_SERVICES_APIKEY")
        self.rule = FirewallRulesV1.new_instance(service_name='cis_services')
        self.service = FiltersV1.new_instance(
            service_name="cis_services")
        self.service.set_service_url(self.endpoint)
        self.rule.set_service_url(self.endpoint)
        self._clean_firewall_rules()
        self._clean_filters()

    def tearDown(self):
        """ tear down """
        # Delete the resources
        print("Clean up complete")

    def _clean_firewall_rules(self):
        # list all rules
        resp = self.rule.list_all_firewall_rules(x_auth_user_token=self.x_auth_user_token,
                                                 crn=self.crn,
                                                 zone_identifier=self.zone_id)
        assert resp is not None
        assert resp.status_code == 200
      #  rules = {}
        resp = resp.get_result().get("result");
        for record in resp:
            # delete rule
            self.rule.delete_firewall_rules(
                x_auth_user_token=self.x_auth_user_token,
                crn=self.crn,
                zone_identifier=self.zone_id,
                id=record.get("id")
            )
    def _clean_filters(self):
        response = self.service.list_all_filters(
            x_auth_user_token = self.x_auth_user_token,
            crn = self.crn,
            zone_identifier = self.zone_id
            )
        assert response is not None
        assert response.status_code == 200
        resp = response.get_result().get("result")
        for record in resp:
            self.service.delete_filter(
                x_auth_user_token = self.x_auth_user_token,
                crn = self.crn,
                zone_identifier = self.zone_id,
                filter_identifier = record.get("id")
            )
    def _create_filter(self, expression, description):
        filter_input_model = {}
        filter_input_model['expression'] = expression
        filter_input_model['paused'] = False
        filter_input_model['description'] = description
        filter_input = [filter_input_model]

        response = self.service.create_filter(
            x_auth_user_token=self.x_auth_user_token,
            crn=self.crn,
            zone_identifier=self.zone_id,
            filter_input=filter_input
        )
        assert response is not None and response.get_status_code() == 200
        filter_id = response.get_result()['result'][0]['id']
        return filter_id

    def test_1_create_firewall_rule_mode_action(self):
        # Construct a dict representation of a FirewallRuleInputWithFilterIdFilter model
        filter_id = self._create_filter(expression='not http.request.uri.path matches "^/test/.*$"', description='not /test')
        firewall_rule_input_filter_model = {}
        firewall_rule_input_filter_model['id'] = filter_id

        # Construct a dict representation of a FirewallRuleInputWithFilterId model
        firewall_rule_input = {}
        firewall_rule_input["filter"] = firewall_rule_input_filter_model
        firewall_rule_input['action'] = 'js_challenge'
        firewall_rule_input['description'] = 'JS challenge site'
        firewall_rule_input_with_filter_id = [firewall_rule_input]

        resp = self.rule.create_firewall_rules(
            x_auth_user_token = self.x_auth_user_token,
            crn = self.crn,
            zone_identifier = self.zone_id,
            firewall_rule_input_with_filter_id = firewall_rule_input_with_filter_id,
        )

        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")[0]["id"] is not None

    def test_1_list_firewall_rules_mode_action(self):

        # Construct a dict representation of a FirewallRuleInputWithFilterIdFilter model
        filter_id = self._create_filter(expression='not http.request.uri.path matches "^/test/.*$"',
                                        description='not /test')
        firewall_rule_input_filter_model = {}
        firewall_rule_input_filter_model['id'] = filter_id

        # Construct a dict representation of a FirewallRuleInputWithFilterId model
        firewall_rule_input = {}
        firewall_rule_input["filter"] = firewall_rule_input_filter_model
        firewall_rule_input['action'] = 'js_challenge'
        firewall_rule_input['description'] = 'JS challenge site'
        firewall_rule_input_with_filter_id = [firewall_rule_input]

        resp = self.rule.create_firewall_rules(
            x_auth_user_token=self.x_auth_user_token,
            crn=self.crn,
            zone_identifier=self.zone_id,
            firewall_rule_input_with_filter_id=firewall_rule_input_with_filter_id,
        )

        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")[0]["id"] is not None

        resp = self.rule.list_all_firewall_rules(
            x_auth_user_token=self.x_auth_user_token,
            crn=self.crn,
            zone_identifier=self.zone_id,
            firewall_rule_input_with_filter_id=firewall_rule_input_with_filter_id,
        )
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")[0]["id"] is not None

    def test_1_update_firewall_rules_mode_action(self):

        # Construct a dict representation of a FirewallRuleInputWithFilterIdFilter model
        filter_id = self._create_filter(expression='not http.request.uri.path matches "^/test/.*$"',
                                        description='not /test')
        firewall_rule_input_filter_model = {}
        firewall_rule_input_filter_model['id'] = filter_id

        # Construct a dict representation of a FirewallRuleInputWithFilterId model
        firewall_rule_input = {}
        firewall_rule_input["filter"] = firewall_rule_input_filter_model
        firewall_rule_input['action'] = 'js_challenge'
        firewall_rule_input['description'] = 'JS challenge site'
        firewall_rule_input_with_filter_id = [firewall_rule_input]

        resp = self.rule.create_firewall_rules(
            x_auth_user_token=self.x_auth_user_token,
            crn=self.crn,
            zone_identifier=self.zone_id,
            firewall_rule_input_with_filter_id=firewall_rule_input_with_filter_id,
        )

        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")[0]["id"] is not None

        filter_id = resp.get_result()['result'][0]['filter']['id']
        firewall_id = resp.get_result().get("result")[0]["id"]

        firewall_rule_update_filter_model = {}
        firewall_rule_update_filter_model['id'] = filter_id

        # Construct a dict representation of a FirewallRuleInputWithFilterId model
        firewall_rule_update = {}
        firewall_rule_update["id"] = firewall_id
        firewall_rule_update['action'] = 'js_challenge'
        firewall_rule_update['paused'] = False
        firewall_rule_update['description'] = 'JS challenge site for firewall'
        firewall_rule_update["filter"] = firewall_rule_update_filter_model
        firewall_rule_update_with_filter_id = [firewall_rule_update]
        resp = self.rule.update_firewll_rules(
            x_auth_user_token=self.x_auth_user_token,
            crn=self.crn,
            zone_identifier=self.zone_id,
            firewall_rules_update_input_item=firewall_rule_update_with_filter_id,
        )
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")[0]["id"] is not None
        assert resp.get_result()['result'][0]['description'] == firewall_rule_update_with_filter_id[0]['description']

    def test_1_delete_firewall_rules_mode_action(self):

        # Construct a dict representation of a FirewallRuleInputWithFilterIdFilter model
        filter_id = self._create_filter(expression='not http.request.uri.path matches "^/test/.*$"',
                                        description='not /test')
        firewall_rule_input_filter_model = {}
        firewall_rule_input_filter_model['id'] = filter_id

        # Construct a dict representation of a FirewallRuleInputWithFilterId model
        firewall_rule_input = {}
        firewall_rule_input["filter"] = firewall_rule_input_filter_model
        firewall_rule_input['action'] = 'js_challenge'
        firewall_rule_input['description'] = 'JS challenge site'
        firewall_rule_input_with_filter_id = [firewall_rule_input]

        resp = self.rule.create_firewall_rules(
            x_auth_user_token=self.x_auth_user_token,
            crn=self.crn,
            zone_identifier=self.zone_id,
            firewall_rule_input_with_filter_id=firewall_rule_input_with_filter_id,
        )

        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")[0]["id"] is not None

        firewall_id = resp.get_result().get("result")[0]["id"]

        resp = self.rule.delete_firewall_rules(
            x_auth_user_token=self.x_auth_user_token,
            crn=self.crn,
            zone_identifier=self.zone_id,
            id=firewall_id,
        )
        assert resp is not None
        assert resp.status_code == 200

        resp = self.rule.list_all_firewall_rules(
            x_auth_user_token=self.x_auth_user_token,
            crn=self.crn,
            zone_identifier=self.zone_id,
            firewall_rule_input_with_filter_id=firewall_rule_input_with_filter_id,
        )
        assert resp is not None
        assert resp.status_code == 200
        assert len(resp.get_result().get("result")) == 0

    def test_1_delete_firewall_rule_mode_action(self):

        # Construct a dict representation of a FirewallRuleInputWithFilterIdFilter model
        filter_id = self._create_filter(expression='not http.request.uri.path matches "^/test/.*$"',
                                        description='not /test')
        firewall_rule_input_filter_model = {}
        firewall_rule_input_filter_model['id'] = filter_id

        # Construct a dict representation of a FirewallRuleInputWithFilterId model
        firewall_rule_input = {}
        firewall_rule_input["filter"] = firewall_rule_input_filter_model
        firewall_rule_input['action'] = 'js_challenge'
        firewall_rule_input['description'] = 'JS challenge site'
        firewall_rule_input_with_filter_id = [firewall_rule_input]

        resp = self.rule.create_firewall_rules(
            x_auth_user_token=self.x_auth_user_token,
            crn=self.crn,
            zone_identifier=self.zone_id,
            firewall_rule_input_with_filter_id=firewall_rule_input_with_filter_id,
        )

        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")[0]["id"] is not None

        firewall_id = resp.get_result().get("result")[0]["id"]

        resp = self.rule.delete_firewall_rule(
            x_auth_user_token=self.x_auth_user_token,
            crn=self.crn,
            zone_identifier=self.zone_id,
            firewall_rule_identifier=firewall_id,
        )
        assert resp is not None
        assert resp.status_code == 200

        resp = self.rule.list_all_firewall_rules(
            x_auth_user_token=self.x_auth_user_token,
            crn=self.crn,
            zone_identifier=self.zone_id,
            firewall_rule_input_with_filter_id=firewall_rule_input_with_filter_id,
        )
        assert resp is not None
        assert resp.status_code == 200
        assert len(resp.get_result().get("result")) == 0

    def test_1_get_firewall_rule_mode_action(self):

        # Construct a dict representation of a FirewallRuleInputWithFilterIdFilter model
        filter_id = self._create_filter(expression='not http.request.uri.path matches "^/test/.*$"',
                                        description='not /test')
        firewall_rule_input_filter_model = {}
        firewall_rule_input_filter_model['id'] = filter_id

        # Construct a dict representation of a FirewallRuleInputWithFilterId model
        firewall_rule_input = {}
        firewall_rule_input["filter"] = firewall_rule_input_filter_model
        firewall_rule_input['action'] = 'js_challenge'
        firewall_rule_input['description'] = 'JS challenge site'
        firewall_rule_input_with_filter_id = [firewall_rule_input]

        resp = self.rule.create_firewall_rules(
            x_auth_user_token=self.x_auth_user_token,
            crn=self.crn,
            zone_identifier=self.zone_id,
            firewall_rule_input_with_filter_id=firewall_rule_input_with_filter_id,
        )

        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")[0]["id"] is not None

        firewall_id = resp.get_result().get("result")[0]["id"]

        resp = self.rule.get_firewall_rule(
            x_auth_user_token=self.x_auth_user_token,
            crn=self.crn,
            zone_identifier=self.zone_id,
            firewall_rule_identifier=firewall_id,
        )
        assert resp is not None
        assert resp.status_code == 200
        get_firewall_id = resp.get_result()['result']['id']
        assert get_firewall_id == firewall_id
        assert resp.get_result()['result']['action'] == 'js_challenge'

    def test_1_update_firewall_rule_mode_action(self):
         # Construct a dict representation of a FirewallRuleInputWithFilterIdFilter model
        filter_id = self._create_filter(expression='not http.request.uri.path matches "^/test/.*$"',
                                    description='not /test')
        firewall_rule_input_filter_model = {}
        firewall_rule_input_filter_model['id'] = filter_id

        # Construct a dict representation of a FirewallRuleInputWithFilterId model
        firewall_rule_input = {}
        firewall_rule_input["filter"] = firewall_rule_input_filter_model
        firewall_rule_input['action'] = 'js_challenge'
        firewall_rule_input['description'] = 'JS challenge site'
        firewall_rule_input_with_filter_id = [firewall_rule_input]

        resp = self.rule.create_firewall_rules(
            x_auth_user_token=self.x_auth_user_token,
            crn=self.crn,
            zone_identifier=self.zone_id,
            firewall_rule_input_with_filter_id=firewall_rule_input_with_filter_id,
        )

        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result().get("result")[0]["id"] is not None
        filter_id = resp.get_result()['result'][0]['filter']['id']
        firewall_id = resp.get_result().get("result")[0]["id"]
        firewall_rule_update_filter_model = {}
        firewall_rule_update_filter_model['id'] = filter_id
        resp = self.rule.update_firewall_rule(
            x_auth_user_token=self.x_auth_user_token,
            crn=self.crn,
            zone_identifier=self.zone_id,
            firewall_rule_identifier=firewall_id,
            action = "js_challenge",
            paused = False,
            description = "Update firewall rule",
            filter = firewall_rule_update_filter_model
        )
        assert resp is not None
        assert resp.status_code == 200
        assert resp.get_result()['result']['description'] == 'Update firewall rule'
        assert resp.get_result()['result']['id'] == firewall_id

if __name__ == '__main__':
    unittest.main()
