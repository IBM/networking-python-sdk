# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2021.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Unit Tests for FirewallRulesV1
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import re
import requests
import responses
import urllib
from ibm_cloud_networking_services.firewall_rules_v1 import *


_service = FirewallRulesV1(
    authenticator=NoAuthAuthenticator()
    )

_base_url = 'https://api.cis.cloud.ibm.com'
_service.set_service_url(_base_url)

##############################################################################
# Start of Service: FirewallRules
##############################################################################
# region

class TestListAllFirewallRules():
    """
    Test Class for list_all_firewall_rules
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_all_firewall_rules_all_params(self):
        """
        list_all_firewall_rules()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/zones/testString/firewall/rules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "52161eb6af4241bb9d4b32394be72fdf", "paused": false, "description": "JS challenge site", "action": "js_challenge", "filter": {"id": "6f58318e7fa2477a23112e8118c66f61", "paused": true, "description": "Login from office", "expression": "ip.src eq 93.184.216.0 and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")"}, "created_on": "2019-01-01T05:20:00.123Z", "modified_on": "2019-01-01T05:20:00.123Z"}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        x_auth_user_token = 'testString'
        crn = 'testString'
        zone_identifier = 'testString'

        # Invoke method
        response = _service.list_all_firewall_rules(
            x_auth_user_token,
            crn,
            zone_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_all_firewall_rules_value_error(self):
        """
        test_list_all_firewall_rules_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/zones/testString/firewall/rules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "52161eb6af4241bb9d4b32394be72fdf", "paused": false, "description": "JS challenge site", "action": "js_challenge", "filter": {"id": "6f58318e7fa2477a23112e8118c66f61", "paused": true, "description": "Login from office", "expression": "ip.src eq 93.184.216.0 and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")"}, "created_on": "2019-01-01T05:20:00.123Z", "modified_on": "2019-01-01T05:20:00.123Z"}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        x_auth_user_token = 'testString'
        crn = 'testString'
        zone_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "x_auth_user_token": x_auth_user_token,
            "crn": crn,
            "zone_identifier": zone_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_all_firewall_rules(**req_copy)



class TestCreateFirewallRules():
    """
    Test Class for create_firewall_rules
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_firewall_rules_all_params(self):
        """
        create_firewall_rules()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/zones/testString/firewall/rules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "52161eb6af4241bb9d4b32394be72fdf", "paused": false, "description": "JS challenge site", "action": "js_challenge", "filter": {"id": "6f58318e7fa2477a23112e8118c66f61", "paused": true, "description": "Login from office", "expression": "ip.src eq 93.184.216.0 and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")"}, "created_on": "2019-01-01T05:20:00.123Z", "modified_on": "2019-01-01T05:20:00.123Z"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a FirewallRuleInputWithFilterIdFilter model
        firewall_rule_input_with_filter_id_filter_model = {}
        firewall_rule_input_with_filter_id_filter_model['id'] = '6f58318e7fa2477a23112e8118c66f61'

        # Construct a dict representation of a FirewallRuleInputWithFilterId model
        firewall_rule_input_with_filter_id_model = {}
        firewall_rule_input_with_filter_id_model['filter'] = firewall_rule_input_with_filter_id_filter_model
        firewall_rule_input_with_filter_id_model['action'] = 'js_challenge'
        firewall_rule_input_with_filter_id_model['description'] = 'JS challenge site'

        # Set up parameter values
        x_auth_user_token = 'testString'
        crn = 'testString'
        zone_identifier = 'testString'
        firewall_rule_input_with_filter_id = [firewall_rule_input_with_filter_id_model]

        # Invoke method
        response = _service.create_firewall_rules(
            x_auth_user_token,
            crn,
            zone_identifier,
            firewall_rule_input_with_filter_id=firewall_rule_input_with_filter_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == firewall_rule_input_with_filter_id


    @responses.activate
    def test_create_firewall_rules_required_params(self):
        """
        test_create_firewall_rules_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/zones/testString/firewall/rules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "52161eb6af4241bb9d4b32394be72fdf", "paused": false, "description": "JS challenge site", "action": "js_challenge", "filter": {"id": "6f58318e7fa2477a23112e8118c66f61", "paused": true, "description": "Login from office", "expression": "ip.src eq 93.184.216.0 and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")"}, "created_on": "2019-01-01T05:20:00.123Z", "modified_on": "2019-01-01T05:20:00.123Z"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        x_auth_user_token = 'testString'
        crn = 'testString'
        zone_identifier = 'testString'

        # Invoke method
        response = _service.create_firewall_rules(
            x_auth_user_token,
            crn,
            zone_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_create_firewall_rules_value_error(self):
        """
        test_create_firewall_rules_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/zones/testString/firewall/rules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "52161eb6af4241bb9d4b32394be72fdf", "paused": false, "description": "JS challenge site", "action": "js_challenge", "filter": {"id": "6f58318e7fa2477a23112e8118c66f61", "paused": true, "description": "Login from office", "expression": "ip.src eq 93.184.216.0 and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")"}, "created_on": "2019-01-01T05:20:00.123Z", "modified_on": "2019-01-01T05:20:00.123Z"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        x_auth_user_token = 'testString'
        crn = 'testString'
        zone_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "x_auth_user_token": x_auth_user_token,
            "crn": crn,
            "zone_identifier": zone_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_firewall_rules(**req_copy)



class TestUpdateFirewllRules():
    """
    Test Class for update_firewll_rules
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_firewll_rules_all_params(self):
        """
        update_firewll_rules()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/zones/testString/firewall/rules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "52161eb6af4241bb9d4b32394be72fdf", "paused": false, "description": "JS challenge site", "action": "js_challenge", "filter": {"id": "6f58318e7fa2477a23112e8118c66f61", "paused": true, "description": "Login from office", "expression": "ip.src eq 93.184.216.0 and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")"}, "created_on": "2019-01-01T05:20:00.123Z", "modified_on": "2019-01-01T05:20:00.123Z"}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a FirewallRulesUpdateInputItemFilter model
        firewall_rules_update_input_item_filter_model = {}
        firewall_rules_update_input_item_filter_model['id'] = '6f58318e7fa2477a23112e8118c66f61'

        # Construct a dict representation of a FirewallRulesUpdateInputItem model
        firewall_rules_update_input_item_model = {}
        firewall_rules_update_input_item_model['id'] = '52161eb6af4241bb9d4b32394be72fdf'
        firewall_rules_update_input_item_model['action'] = 'js_challenge'
        firewall_rules_update_input_item_model['paused'] = False
        firewall_rules_update_input_item_model['description'] = 'JS challenge site'
        firewall_rules_update_input_item_model['filter'] = firewall_rules_update_input_item_filter_model

        # Set up parameter values
        x_auth_user_token = 'testString'
        crn = 'testString'
        zone_identifier = 'testString'
        firewall_rules_update_input_item = [firewall_rules_update_input_item_model]

        # Invoke method
        response = _service.update_firewll_rules(
            x_auth_user_token,
            crn,
            zone_identifier,
            firewall_rules_update_input_item=firewall_rules_update_input_item,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == firewall_rules_update_input_item


    @responses.activate
    def test_update_firewll_rules_required_params(self):
        """
        test_update_firewll_rules_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/zones/testString/firewall/rules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "52161eb6af4241bb9d4b32394be72fdf", "paused": false, "description": "JS challenge site", "action": "js_challenge", "filter": {"id": "6f58318e7fa2477a23112e8118c66f61", "paused": true, "description": "Login from office", "expression": "ip.src eq 93.184.216.0 and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")"}, "created_on": "2019-01-01T05:20:00.123Z", "modified_on": "2019-01-01T05:20:00.123Z"}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        x_auth_user_token = 'testString'
        crn = 'testString'
        zone_identifier = 'testString'

        # Invoke method
        response = _service.update_firewll_rules(
            x_auth_user_token,
            crn,
            zone_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_update_firewll_rules_value_error(self):
        """
        test_update_firewll_rules_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/zones/testString/firewall/rules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "52161eb6af4241bb9d4b32394be72fdf", "paused": false, "description": "JS challenge site", "action": "js_challenge", "filter": {"id": "6f58318e7fa2477a23112e8118c66f61", "paused": true, "description": "Login from office", "expression": "ip.src eq 93.184.216.0 and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")"}, "created_on": "2019-01-01T05:20:00.123Z", "modified_on": "2019-01-01T05:20:00.123Z"}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        x_auth_user_token = 'testString'
        crn = 'testString'
        zone_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "x_auth_user_token": x_auth_user_token,
            "crn": crn,
            "zone_identifier": zone_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_firewll_rules(**req_copy)



class TestDeleteFirewallRules():
    """
    Test Class for delete_firewall_rules
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_firewall_rules_all_params(self):
        """
        delete_firewall_rules()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/zones/testString/firewall/rules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "f2d427378e7542acb295380d352e2ebd"}]}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        x_auth_user_token = 'testString'
        crn = 'testString'
        zone_identifier = 'testString'
        id = 'f2d427378e7542acb295380d352e2ebd'

        # Invoke method
        response = _service.delete_firewall_rules(
            x_auth_user_token,
            crn,
            zone_identifier,
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'id={}'.format(id) in query_string


    @responses.activate
    def test_delete_firewall_rules_value_error(self):
        """
        test_delete_firewall_rules_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/zones/testString/firewall/rules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "f2d427378e7542acb295380d352e2ebd"}]}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        x_auth_user_token = 'testString'
        crn = 'testString'
        zone_identifier = 'testString'
        id = 'f2d427378e7542acb295380d352e2ebd'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "x_auth_user_token": x_auth_user_token,
            "crn": crn,
            "zone_identifier": zone_identifier,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_firewall_rules(**req_copy)



class TestDeleteFirewallRule():
    """
    Test Class for delete_firewall_rule
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_firewall_rule_all_params(self):
        """
        delete_firewall_rule()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/zones/testString/firewall/rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f2d427378e7542acb295380d352e2ebd"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        x_auth_user_token = 'testString'
        crn = 'testString'
        zone_identifier = 'testString'
        firewall_rule_identifier = 'testString'

        # Invoke method
        response = _service.delete_firewall_rule(
            x_auth_user_token,
            crn,
            zone_identifier,
            firewall_rule_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_firewall_rule_value_error(self):
        """
        test_delete_firewall_rule_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/zones/testString/firewall/rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f2d427378e7542acb295380d352e2ebd"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        x_auth_user_token = 'testString'
        crn = 'testString'
        zone_identifier = 'testString'
        firewall_rule_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "x_auth_user_token": x_auth_user_token,
            "crn": crn,
            "zone_identifier": zone_identifier,
            "firewall_rule_identifier": firewall_rule_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_firewall_rule(**req_copy)



class TestGetFirewallRule():
    """
    Test Class for get_firewall_rule
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_firewall_rule_all_params(self):
        """
        get_firewall_rule()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/zones/testString/firewall/rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "52161eb6af4241bb9d4b32394be72fdf", "paused": false, "description": "JS challenge site", "action": "js_challenge", "filter": {"id": "6f58318e7fa2477a23112e8118c66f61", "paused": true, "description": "Login from office", "expression": "ip.src eq 93.184.216.0 and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")"}, "created_on": "2019-01-01T05:20:00.123Z", "modified_on": "2019-01-01T05:20:00.123Z"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        x_auth_user_token = 'testString'
        crn = 'testString'
        zone_identifier = 'testString'
        firewall_rule_identifier = 'testString'

        # Invoke method
        response = _service.get_firewall_rule(
            x_auth_user_token,
            crn,
            zone_identifier,
            firewall_rule_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_firewall_rule_value_error(self):
        """
        test_get_firewall_rule_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/zones/testString/firewall/rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "52161eb6af4241bb9d4b32394be72fdf", "paused": false, "description": "JS challenge site", "action": "js_challenge", "filter": {"id": "6f58318e7fa2477a23112e8118c66f61", "paused": true, "description": "Login from office", "expression": "ip.src eq 93.184.216.0 and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")"}, "created_on": "2019-01-01T05:20:00.123Z", "modified_on": "2019-01-01T05:20:00.123Z"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        x_auth_user_token = 'testString'
        crn = 'testString'
        zone_identifier = 'testString'
        firewall_rule_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "x_auth_user_token": x_auth_user_token,
            "crn": crn,
            "zone_identifier": zone_identifier,
            "firewall_rule_identifier": firewall_rule_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_firewall_rule(**req_copy)



class TestUpdateFirewallRule():
    """
    Test Class for update_firewall_rule
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_firewall_rule_all_params(self):
        """
        update_firewall_rule()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/zones/testString/firewall/rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "52161eb6af4241bb9d4b32394be72fdf", "paused": false, "description": "JS challenge site", "action": "js_challenge", "filter": {"id": "6f58318e7fa2477a23112e8118c66f61", "paused": true, "description": "Login from office", "expression": "ip.src eq 93.184.216.0 and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")"}, "created_on": "2019-01-01T05:20:00.123Z", "modified_on": "2019-01-01T05:20:00.123Z"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a FirewallRuleUpdateInputFilter model
        firewall_rule_update_input_filter_model = {}
        firewall_rule_update_input_filter_model['id'] = '6f58318e7fa2477a23112e8118c66f61'

        # Set up parameter values
        x_auth_user_token = 'testString'
        crn = 'testString'
        zone_identifier = 'testString'
        firewall_rule_identifier = 'testString'
        action = 'js_challenge'
        paused = False
        description = 'JS challenge site'
        filter = firewall_rule_update_input_filter_model

        # Invoke method
        response = _service.update_firewall_rule(
            x_auth_user_token,
            crn,
            zone_identifier,
            firewall_rule_identifier,
            action=action,
            paused=paused,
            description=description,
            filter=filter,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['action'] == 'js_challenge'
        assert req_body['paused'] == False
        assert req_body['description'] == 'JS challenge site'
        assert req_body['filter'] == firewall_rule_update_input_filter_model


    @responses.activate
    def test_update_firewall_rule_required_params(self):
        """
        test_update_firewall_rule_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/zones/testString/firewall/rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "52161eb6af4241bb9d4b32394be72fdf", "paused": false, "description": "JS challenge site", "action": "js_challenge", "filter": {"id": "6f58318e7fa2477a23112e8118c66f61", "paused": true, "description": "Login from office", "expression": "ip.src eq 93.184.216.0 and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")"}, "created_on": "2019-01-01T05:20:00.123Z", "modified_on": "2019-01-01T05:20:00.123Z"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        x_auth_user_token = 'testString'
        crn = 'testString'
        zone_identifier = 'testString'
        firewall_rule_identifier = 'testString'

        # Invoke method
        response = _service.update_firewall_rule(
            x_auth_user_token,
            crn,
            zone_identifier,
            firewall_rule_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_update_firewall_rule_value_error(self):
        """
        test_update_firewall_rule_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/testString/zones/testString/firewall/rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "52161eb6af4241bb9d4b32394be72fdf", "paused": false, "description": "JS challenge site", "action": "js_challenge", "filter": {"id": "6f58318e7fa2477a23112e8118c66f61", "paused": true, "description": "Login from office", "expression": "ip.src eq 93.184.216.0 and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")"}, "created_on": "2019-01-01T05:20:00.123Z", "modified_on": "2019-01-01T05:20:00.123Z"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        x_auth_user_token = 'testString'
        crn = 'testString'
        zone_identifier = 'testString'
        firewall_rule_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "x_auth_user_token": x_auth_user_token,
            "crn": crn,
            "zone_identifier": zone_identifier,
            "firewall_rule_identifier": firewall_rule_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_firewall_rule(**req_copy)



# endregion
##############################################################################
# End of Service: FirewallRules
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestDeleteFirewallRuleRespResult():
    """
    Test Class for DeleteFirewallRuleRespResult
    """

    def test_delete_firewall_rule_resp_result_serialization(self):
        """
        Test serialization/deserialization for DeleteFirewallRuleRespResult
        """

        # Construct a json representation of a DeleteFirewallRuleRespResult model
        delete_firewall_rule_resp_result_model_json = {}
        delete_firewall_rule_resp_result_model_json['id'] = 'f2d427378e7542acb295380d352e2ebd'

        # Construct a model instance of DeleteFirewallRuleRespResult by calling from_dict on the json representation
        delete_firewall_rule_resp_result_model = DeleteFirewallRuleRespResult.from_dict(delete_firewall_rule_resp_result_model_json)
        assert delete_firewall_rule_resp_result_model != False

        # Construct a model instance of DeleteFirewallRuleRespResult by calling from_dict on the json representation
        delete_firewall_rule_resp_result_model_dict = DeleteFirewallRuleRespResult.from_dict(delete_firewall_rule_resp_result_model_json).__dict__
        delete_firewall_rule_resp_result_model2 = DeleteFirewallRuleRespResult(**delete_firewall_rule_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert delete_firewall_rule_resp_result_model == delete_firewall_rule_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        delete_firewall_rule_resp_result_model_json2 = delete_firewall_rule_resp_result_model.to_dict()
        assert delete_firewall_rule_resp_result_model_json2 == delete_firewall_rule_resp_result_model_json

class TestDeleteFirewallRulesRespResultItem():
    """
    Test Class for DeleteFirewallRulesRespResultItem
    """

    def test_delete_firewall_rules_resp_result_item_serialization(self):
        """
        Test serialization/deserialization for DeleteFirewallRulesRespResultItem
        """

        # Construct a json representation of a DeleteFirewallRulesRespResultItem model
        delete_firewall_rules_resp_result_item_model_json = {}
        delete_firewall_rules_resp_result_item_model_json['id'] = 'f2d427378e7542acb295380d352e2ebd'

        # Construct a model instance of DeleteFirewallRulesRespResultItem by calling from_dict on the json representation
        delete_firewall_rules_resp_result_item_model = DeleteFirewallRulesRespResultItem.from_dict(delete_firewall_rules_resp_result_item_model_json)
        assert delete_firewall_rules_resp_result_item_model != False

        # Construct a model instance of DeleteFirewallRulesRespResultItem by calling from_dict on the json representation
        delete_firewall_rules_resp_result_item_model_dict = DeleteFirewallRulesRespResultItem.from_dict(delete_firewall_rules_resp_result_item_model_json).__dict__
        delete_firewall_rules_resp_result_item_model2 = DeleteFirewallRulesRespResultItem(**delete_firewall_rules_resp_result_item_model_dict)

        # Verify the model instances are equivalent
        assert delete_firewall_rules_resp_result_item_model == delete_firewall_rules_resp_result_item_model2

        # Convert model instance back to dict and verify no loss of data
        delete_firewall_rules_resp_result_item_model_json2 = delete_firewall_rules_resp_result_item_model.to_dict()
        assert delete_firewall_rules_resp_result_item_model_json2 == delete_firewall_rules_resp_result_item_model_json

class TestFirewallRuleInputWithFilterIdFilter():
    """
    Test Class for FirewallRuleInputWithFilterIdFilter
    """

    def test_firewall_rule_input_with_filter_id_filter_serialization(self):
        """
        Test serialization/deserialization for FirewallRuleInputWithFilterIdFilter
        """

        # Construct a json representation of a FirewallRuleInputWithFilterIdFilter model
        firewall_rule_input_with_filter_id_filter_model_json = {}
        firewall_rule_input_with_filter_id_filter_model_json['id'] = '6f58318e7fa2477a23112e8118c66f61'

        # Construct a model instance of FirewallRuleInputWithFilterIdFilter by calling from_dict on the json representation
        firewall_rule_input_with_filter_id_filter_model = FirewallRuleInputWithFilterIdFilter.from_dict(firewall_rule_input_with_filter_id_filter_model_json)
        assert firewall_rule_input_with_filter_id_filter_model != False

        # Construct a model instance of FirewallRuleInputWithFilterIdFilter by calling from_dict on the json representation
        firewall_rule_input_with_filter_id_filter_model_dict = FirewallRuleInputWithFilterIdFilter.from_dict(firewall_rule_input_with_filter_id_filter_model_json).__dict__
        firewall_rule_input_with_filter_id_filter_model2 = FirewallRuleInputWithFilterIdFilter(**firewall_rule_input_with_filter_id_filter_model_dict)

        # Verify the model instances are equivalent
        assert firewall_rule_input_with_filter_id_filter_model == firewall_rule_input_with_filter_id_filter_model2

        # Convert model instance back to dict and verify no loss of data
        firewall_rule_input_with_filter_id_filter_model_json2 = firewall_rule_input_with_filter_id_filter_model.to_dict()
        assert firewall_rule_input_with_filter_id_filter_model_json2 == firewall_rule_input_with_filter_id_filter_model_json

class TestFirewallRuleObjectFilter():
    """
    Test Class for FirewallRuleObjectFilter
    """

    def test_firewall_rule_object_filter_serialization(self):
        """
        Test serialization/deserialization for FirewallRuleObjectFilter
        """

        # Construct a json representation of a FirewallRuleObjectFilter model
        firewall_rule_object_filter_model_json = {}
        firewall_rule_object_filter_model_json['id'] = '6f58318e7fa2477a23112e8118c66f61'
        firewall_rule_object_filter_model_json['paused'] = True
        firewall_rule_object_filter_model_json['description'] = 'Login from office'
        firewall_rule_object_filter_model_json['expression'] = 'ip.src eq 93.184.216.0 and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")'

        # Construct a model instance of FirewallRuleObjectFilter by calling from_dict on the json representation
        firewall_rule_object_filter_model = FirewallRuleObjectFilter.from_dict(firewall_rule_object_filter_model_json)
        assert firewall_rule_object_filter_model != False

        # Construct a model instance of FirewallRuleObjectFilter by calling from_dict on the json representation
        firewall_rule_object_filter_model_dict = FirewallRuleObjectFilter.from_dict(firewall_rule_object_filter_model_json).__dict__
        firewall_rule_object_filter_model2 = FirewallRuleObjectFilter(**firewall_rule_object_filter_model_dict)

        # Verify the model instances are equivalent
        assert firewall_rule_object_filter_model == firewall_rule_object_filter_model2

        # Convert model instance back to dict and verify no loss of data
        firewall_rule_object_filter_model_json2 = firewall_rule_object_filter_model.to_dict()
        assert firewall_rule_object_filter_model_json2 == firewall_rule_object_filter_model_json

class TestFirewallRuleUpdateInputFilter():
    """
    Test Class for FirewallRuleUpdateInputFilter
    """

    def test_firewall_rule_update_input_filter_serialization(self):
        """
        Test serialization/deserialization for FirewallRuleUpdateInputFilter
        """

        # Construct a json representation of a FirewallRuleUpdateInputFilter model
        firewall_rule_update_input_filter_model_json = {}
        firewall_rule_update_input_filter_model_json['id'] = '6f58318e7fa2477a23112e8118c66f61'

        # Construct a model instance of FirewallRuleUpdateInputFilter by calling from_dict on the json representation
        firewall_rule_update_input_filter_model = FirewallRuleUpdateInputFilter.from_dict(firewall_rule_update_input_filter_model_json)
        assert firewall_rule_update_input_filter_model != False

        # Construct a model instance of FirewallRuleUpdateInputFilter by calling from_dict on the json representation
        firewall_rule_update_input_filter_model_dict = FirewallRuleUpdateInputFilter.from_dict(firewall_rule_update_input_filter_model_json).__dict__
        firewall_rule_update_input_filter_model2 = FirewallRuleUpdateInputFilter(**firewall_rule_update_input_filter_model_dict)

        # Verify the model instances are equivalent
        assert firewall_rule_update_input_filter_model == firewall_rule_update_input_filter_model2

        # Convert model instance back to dict and verify no loss of data
        firewall_rule_update_input_filter_model_json2 = firewall_rule_update_input_filter_model.to_dict()
        assert firewall_rule_update_input_filter_model_json2 == firewall_rule_update_input_filter_model_json

class TestFirewallRulesUpdateInputItem():
    """
    Test Class for FirewallRulesUpdateInputItem
    """

    def test_firewall_rules_update_input_item_serialization(self):
        """
        Test serialization/deserialization for FirewallRulesUpdateInputItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        firewall_rules_update_input_item_filter_model = {} # FirewallRulesUpdateInputItemFilter
        firewall_rules_update_input_item_filter_model['id'] = '6f58318e7fa2477a23112e8118c66f61'

        # Construct a json representation of a FirewallRulesUpdateInputItem model
        firewall_rules_update_input_item_model_json = {}
        firewall_rules_update_input_item_model_json['id'] = '52161eb6af4241bb9d4b32394be72fdf'
        firewall_rules_update_input_item_model_json['action'] = 'js_challenge'
        firewall_rules_update_input_item_model_json['paused'] = False
        firewall_rules_update_input_item_model_json['description'] = 'JS challenge site'
        firewall_rules_update_input_item_model_json['filter'] = firewall_rules_update_input_item_filter_model

        # Construct a model instance of FirewallRulesUpdateInputItem by calling from_dict on the json representation
        firewall_rules_update_input_item_model = FirewallRulesUpdateInputItem.from_dict(firewall_rules_update_input_item_model_json)
        assert firewall_rules_update_input_item_model != False

        # Construct a model instance of FirewallRulesUpdateInputItem by calling from_dict on the json representation
        firewall_rules_update_input_item_model_dict = FirewallRulesUpdateInputItem.from_dict(firewall_rules_update_input_item_model_json).__dict__
        firewall_rules_update_input_item_model2 = FirewallRulesUpdateInputItem(**firewall_rules_update_input_item_model_dict)

        # Verify the model instances are equivalent
        assert firewall_rules_update_input_item_model == firewall_rules_update_input_item_model2

        # Convert model instance back to dict and verify no loss of data
        firewall_rules_update_input_item_model_json2 = firewall_rules_update_input_item_model.to_dict()
        assert firewall_rules_update_input_item_model_json2 == firewall_rules_update_input_item_model_json

class TestFirewallRulesUpdateInputItemFilter():
    """
    Test Class for FirewallRulesUpdateInputItemFilter
    """

    def test_firewall_rules_update_input_item_filter_serialization(self):
        """
        Test serialization/deserialization for FirewallRulesUpdateInputItemFilter
        """

        # Construct a json representation of a FirewallRulesUpdateInputItemFilter model
        firewall_rules_update_input_item_filter_model_json = {}
        firewall_rules_update_input_item_filter_model_json['id'] = '6f58318e7fa2477a23112e8118c66f61'

        # Construct a model instance of FirewallRulesUpdateInputItemFilter by calling from_dict on the json representation
        firewall_rules_update_input_item_filter_model = FirewallRulesUpdateInputItemFilter.from_dict(firewall_rules_update_input_item_filter_model_json)
        assert firewall_rules_update_input_item_filter_model != False

        # Construct a model instance of FirewallRulesUpdateInputItemFilter by calling from_dict on the json representation
        firewall_rules_update_input_item_filter_model_dict = FirewallRulesUpdateInputItemFilter.from_dict(firewall_rules_update_input_item_filter_model_json).__dict__
        firewall_rules_update_input_item_filter_model2 = FirewallRulesUpdateInputItemFilter(**firewall_rules_update_input_item_filter_model_dict)

        # Verify the model instances are equivalent
        assert firewall_rules_update_input_item_filter_model == firewall_rules_update_input_item_filter_model2

        # Convert model instance back to dict and verify no loss of data
        firewall_rules_update_input_item_filter_model_json2 = firewall_rules_update_input_item_filter_model.to_dict()
        assert firewall_rules_update_input_item_filter_model_json2 == firewall_rules_update_input_item_filter_model_json

class TestListFirewallRulesRespResultInfo():
    """
    Test Class for ListFirewallRulesRespResultInfo
    """

    def test_list_firewall_rules_resp_result_info_serialization(self):
        """
        Test serialization/deserialization for ListFirewallRulesRespResultInfo
        """

        # Construct a json representation of a ListFirewallRulesRespResultInfo model
        list_firewall_rules_resp_result_info_model_json = {}
        list_firewall_rules_resp_result_info_model_json['page'] = 1
        list_firewall_rules_resp_result_info_model_json['per_page'] = 2
        list_firewall_rules_resp_result_info_model_json['count'] = 1
        list_firewall_rules_resp_result_info_model_json['total_count'] = 200

        # Construct a model instance of ListFirewallRulesRespResultInfo by calling from_dict on the json representation
        list_firewall_rules_resp_result_info_model = ListFirewallRulesRespResultInfo.from_dict(list_firewall_rules_resp_result_info_model_json)
        assert list_firewall_rules_resp_result_info_model != False

        # Construct a model instance of ListFirewallRulesRespResultInfo by calling from_dict on the json representation
        list_firewall_rules_resp_result_info_model_dict = ListFirewallRulesRespResultInfo.from_dict(list_firewall_rules_resp_result_info_model_json).__dict__
        list_firewall_rules_resp_result_info_model2 = ListFirewallRulesRespResultInfo(**list_firewall_rules_resp_result_info_model_dict)

        # Verify the model instances are equivalent
        assert list_firewall_rules_resp_result_info_model == list_firewall_rules_resp_result_info_model2

        # Convert model instance back to dict and verify no loss of data
        list_firewall_rules_resp_result_info_model_json2 = list_firewall_rules_resp_result_info_model.to_dict()
        assert list_firewall_rules_resp_result_info_model_json2 == list_firewall_rules_resp_result_info_model_json

class TestDeleteFirewallRuleResp():
    """
    Test Class for DeleteFirewallRuleResp
    """

    def test_delete_firewall_rule_resp_serialization(self):
        """
        Test serialization/deserialization for DeleteFirewallRuleResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        delete_firewall_rule_resp_result_model = {} # DeleteFirewallRuleRespResult
        delete_firewall_rule_resp_result_model['id'] = 'f2d427378e7542acb295380d352e2ebd'

        # Construct a json representation of a DeleteFirewallRuleResp model
        delete_firewall_rule_resp_model_json = {}
        delete_firewall_rule_resp_model_json['success'] = True
        delete_firewall_rule_resp_model_json['errors'] = [['testString']]
        delete_firewall_rule_resp_model_json['messages'] = [['testString']]
        delete_firewall_rule_resp_model_json['result'] = delete_firewall_rule_resp_result_model

        # Construct a model instance of DeleteFirewallRuleResp by calling from_dict on the json representation
        delete_firewall_rule_resp_model = DeleteFirewallRuleResp.from_dict(delete_firewall_rule_resp_model_json)
        assert delete_firewall_rule_resp_model != False

        # Construct a model instance of DeleteFirewallRuleResp by calling from_dict on the json representation
        delete_firewall_rule_resp_model_dict = DeleteFirewallRuleResp.from_dict(delete_firewall_rule_resp_model_json).__dict__
        delete_firewall_rule_resp_model2 = DeleteFirewallRuleResp(**delete_firewall_rule_resp_model_dict)

        # Verify the model instances are equivalent
        assert delete_firewall_rule_resp_model == delete_firewall_rule_resp_model2

        # Convert model instance back to dict and verify no loss of data
        delete_firewall_rule_resp_model_json2 = delete_firewall_rule_resp_model.to_dict()
        assert delete_firewall_rule_resp_model_json2 == delete_firewall_rule_resp_model_json

class TestDeleteFirewallRulesResp():
    """
    Test Class for DeleteFirewallRulesResp
    """

    def test_delete_firewall_rules_resp_serialization(self):
        """
        Test serialization/deserialization for DeleteFirewallRulesResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        delete_firewall_rules_resp_result_item_model = {} # DeleteFirewallRulesRespResultItem
        delete_firewall_rules_resp_result_item_model['id'] = 'f2d427378e7542acb295380d352e2ebd'

        # Construct a json representation of a DeleteFirewallRulesResp model
        delete_firewall_rules_resp_model_json = {}
        delete_firewall_rules_resp_model_json['success'] = True
        delete_firewall_rules_resp_model_json['errors'] = [['testString']]
        delete_firewall_rules_resp_model_json['messages'] = [['testString']]
        delete_firewall_rules_resp_model_json['result'] = [delete_firewall_rules_resp_result_item_model]

        # Construct a model instance of DeleteFirewallRulesResp by calling from_dict on the json representation
        delete_firewall_rules_resp_model = DeleteFirewallRulesResp.from_dict(delete_firewall_rules_resp_model_json)
        assert delete_firewall_rules_resp_model != False

        # Construct a model instance of DeleteFirewallRulesResp by calling from_dict on the json representation
        delete_firewall_rules_resp_model_dict = DeleteFirewallRulesResp.from_dict(delete_firewall_rules_resp_model_json).__dict__
        delete_firewall_rules_resp_model2 = DeleteFirewallRulesResp(**delete_firewall_rules_resp_model_dict)

        # Verify the model instances are equivalent
        assert delete_firewall_rules_resp_model == delete_firewall_rules_resp_model2

        # Convert model instance back to dict and verify no loss of data
        delete_firewall_rules_resp_model_json2 = delete_firewall_rules_resp_model.to_dict()
        assert delete_firewall_rules_resp_model_json2 == delete_firewall_rules_resp_model_json

class TestFirewallRuleInputWithFilterId():
    """
    Test Class for FirewallRuleInputWithFilterId
    """

    def test_firewall_rule_input_with_filter_id_serialization(self):
        """
        Test serialization/deserialization for FirewallRuleInputWithFilterId
        """

        # Construct dict forms of any model objects needed in order to build this model.

        firewall_rule_input_with_filter_id_filter_model = {} # FirewallRuleInputWithFilterIdFilter
        firewall_rule_input_with_filter_id_filter_model['id'] = '6f58318e7fa2477a23112e8118c66f61'

        # Construct a json representation of a FirewallRuleInputWithFilterId model
        firewall_rule_input_with_filter_id_model_json = {}
        firewall_rule_input_with_filter_id_model_json['filter'] = firewall_rule_input_with_filter_id_filter_model
        firewall_rule_input_with_filter_id_model_json['action'] = 'js_challenge'
        firewall_rule_input_with_filter_id_model_json['description'] = 'JS challenge site'

        # Construct a model instance of FirewallRuleInputWithFilterId by calling from_dict on the json representation
        firewall_rule_input_with_filter_id_model = FirewallRuleInputWithFilterId.from_dict(firewall_rule_input_with_filter_id_model_json)
        assert firewall_rule_input_with_filter_id_model != False

        # Construct a model instance of FirewallRuleInputWithFilterId by calling from_dict on the json representation
        firewall_rule_input_with_filter_id_model_dict = FirewallRuleInputWithFilterId.from_dict(firewall_rule_input_with_filter_id_model_json).__dict__
        firewall_rule_input_with_filter_id_model2 = FirewallRuleInputWithFilterId(**firewall_rule_input_with_filter_id_model_dict)

        # Verify the model instances are equivalent
        assert firewall_rule_input_with_filter_id_model == firewall_rule_input_with_filter_id_model2

        # Convert model instance back to dict and verify no loss of data
        firewall_rule_input_with_filter_id_model_json2 = firewall_rule_input_with_filter_id_model.to_dict()
        assert firewall_rule_input_with_filter_id_model_json2 == firewall_rule_input_with_filter_id_model_json

class TestFirewallRuleObject():
    """
    Test Class for FirewallRuleObject
    """

    def test_firewall_rule_object_serialization(self):
        """
        Test serialization/deserialization for FirewallRuleObject
        """

        # Construct dict forms of any model objects needed in order to build this model.

        firewall_rule_object_filter_model = {} # FirewallRuleObjectFilter
        firewall_rule_object_filter_model['id'] = '6f58318e7fa2477a23112e8118c66f61'
        firewall_rule_object_filter_model['paused'] = True
        firewall_rule_object_filter_model['description'] = 'Login from office'
        firewall_rule_object_filter_model['expression'] = 'ip.src eq 93.184.216.0 and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")'

        # Construct a json representation of a FirewallRuleObject model
        firewall_rule_object_model_json = {}
        firewall_rule_object_model_json['id'] = '52161eb6af4241bb9d4b32394be72fdf'
        firewall_rule_object_model_json['paused'] = False
        firewall_rule_object_model_json['description'] = 'JS challenge site'
        firewall_rule_object_model_json['action'] = 'js_challenge'
        firewall_rule_object_model_json['filter'] = firewall_rule_object_filter_model
        firewall_rule_object_model_json['created_on'] = '2019-01-01T05:20:00.123Z'
        firewall_rule_object_model_json['modified_on'] = '2019-01-01T05:20:00.123Z'

        # Construct a model instance of FirewallRuleObject by calling from_dict on the json representation
        firewall_rule_object_model = FirewallRuleObject.from_dict(firewall_rule_object_model_json)
        assert firewall_rule_object_model != False

        # Construct a model instance of FirewallRuleObject by calling from_dict on the json representation
        firewall_rule_object_model_dict = FirewallRuleObject.from_dict(firewall_rule_object_model_json).__dict__
        firewall_rule_object_model2 = FirewallRuleObject(**firewall_rule_object_model_dict)

        # Verify the model instances are equivalent
        assert firewall_rule_object_model == firewall_rule_object_model2

        # Convert model instance back to dict and verify no loss of data
        firewall_rule_object_model_json2 = firewall_rule_object_model.to_dict()
        assert firewall_rule_object_model_json2 == firewall_rule_object_model_json

class TestFirewallRuleResp():
    """
    Test Class for FirewallRuleResp
    """

    def test_firewall_rule_resp_serialization(self):
        """
        Test serialization/deserialization for FirewallRuleResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        firewall_rule_object_filter_model = {} # FirewallRuleObjectFilter
        firewall_rule_object_filter_model['id'] = '6f58318e7fa2477a23112e8118c66f61'
        firewall_rule_object_filter_model['paused'] = True
        firewall_rule_object_filter_model['description'] = 'Login from office'
        firewall_rule_object_filter_model['expression'] = 'ip.src eq 93.184.216.0 and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")'

        firewall_rule_object_model = {} # FirewallRuleObject
        firewall_rule_object_model['id'] = '52161eb6af4241bb9d4b32394be72fdf'
        firewall_rule_object_model['paused'] = False
        firewall_rule_object_model['description'] = 'JS challenge site'
        firewall_rule_object_model['action'] = 'js_challenge'
        firewall_rule_object_model['filter'] = firewall_rule_object_filter_model
        firewall_rule_object_model['created_on'] = '2019-01-01T05:20:00.123Z'
        firewall_rule_object_model['modified_on'] = '2019-01-01T05:20:00.123Z'

        # Construct a json representation of a FirewallRuleResp model
        firewall_rule_resp_model_json = {}
        firewall_rule_resp_model_json['success'] = True
        firewall_rule_resp_model_json['errors'] = [['testString']]
        firewall_rule_resp_model_json['messages'] = [['testString']]
        firewall_rule_resp_model_json['result'] = firewall_rule_object_model

        # Construct a model instance of FirewallRuleResp by calling from_dict on the json representation
        firewall_rule_resp_model = FirewallRuleResp.from_dict(firewall_rule_resp_model_json)
        assert firewall_rule_resp_model != False

        # Construct a model instance of FirewallRuleResp by calling from_dict on the json representation
        firewall_rule_resp_model_dict = FirewallRuleResp.from_dict(firewall_rule_resp_model_json).__dict__
        firewall_rule_resp_model2 = FirewallRuleResp(**firewall_rule_resp_model_dict)

        # Verify the model instances are equivalent
        assert firewall_rule_resp_model == firewall_rule_resp_model2

        # Convert model instance back to dict and verify no loss of data
        firewall_rule_resp_model_json2 = firewall_rule_resp_model.to_dict()
        assert firewall_rule_resp_model_json2 == firewall_rule_resp_model_json

class TestFirewallRulesResp():
    """
    Test Class for FirewallRulesResp
    """

    def test_firewall_rules_resp_serialization(self):
        """
        Test serialization/deserialization for FirewallRulesResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        firewall_rule_object_filter_model = {} # FirewallRuleObjectFilter
        firewall_rule_object_filter_model['id'] = '6f58318e7fa2477a23112e8118c66f61'
        firewall_rule_object_filter_model['paused'] = True
        firewall_rule_object_filter_model['description'] = 'Login from office'
        firewall_rule_object_filter_model['expression'] = 'ip.src eq 93.184.216.0 and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")'

        firewall_rule_object_model = {} # FirewallRuleObject
        firewall_rule_object_model['id'] = '52161eb6af4241bb9d4b32394be72fdf'
        firewall_rule_object_model['paused'] = False
        firewall_rule_object_model['description'] = 'JS challenge site'
        firewall_rule_object_model['action'] = 'js_challenge'
        firewall_rule_object_model['filter'] = firewall_rule_object_filter_model
        firewall_rule_object_model['created_on'] = '2019-01-01T05:20:00.123Z'
        firewall_rule_object_model['modified_on'] = '2019-01-01T05:20:00.123Z'

        # Construct a json representation of a FirewallRulesResp model
        firewall_rules_resp_model_json = {}
        firewall_rules_resp_model_json['success'] = True
        firewall_rules_resp_model_json['errors'] = [['testString']]
        firewall_rules_resp_model_json['messages'] = [['testString']]
        firewall_rules_resp_model_json['result'] = [firewall_rule_object_model]

        # Construct a model instance of FirewallRulesResp by calling from_dict on the json representation
        firewall_rules_resp_model = FirewallRulesResp.from_dict(firewall_rules_resp_model_json)
        assert firewall_rules_resp_model != False

        # Construct a model instance of FirewallRulesResp by calling from_dict on the json representation
        firewall_rules_resp_model_dict = FirewallRulesResp.from_dict(firewall_rules_resp_model_json).__dict__
        firewall_rules_resp_model2 = FirewallRulesResp(**firewall_rules_resp_model_dict)

        # Verify the model instances are equivalent
        assert firewall_rules_resp_model == firewall_rules_resp_model2

        # Convert model instance back to dict and verify no loss of data
        firewall_rules_resp_model_json2 = firewall_rules_resp_model.to_dict()
        assert firewall_rules_resp_model_json2 == firewall_rules_resp_model_json

class TestListFirewallRulesResp():
    """
    Test Class for ListFirewallRulesResp
    """

    def test_list_firewall_rules_resp_serialization(self):
        """
        Test serialization/deserialization for ListFirewallRulesResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        firewall_rule_object_filter_model = {} # FirewallRuleObjectFilter
        firewall_rule_object_filter_model['id'] = '6f58318e7fa2477a23112e8118c66f61'
        firewall_rule_object_filter_model['paused'] = True
        firewall_rule_object_filter_model['description'] = 'Login from office'
        firewall_rule_object_filter_model['expression'] = 'ip.src eq 93.184.216.0 and (http.request.uri.path ~ \"^.*/wp-login.php$\" or http.request.uri.path ~ \"^.*/xmlrpc.php$\")'

        firewall_rule_object_model = {} # FirewallRuleObject
        firewall_rule_object_model['id'] = '52161eb6af4241bb9d4b32394be72fdf'
        firewall_rule_object_model['paused'] = False
        firewall_rule_object_model['description'] = 'JS challenge site'
        firewall_rule_object_model['action'] = 'js_challenge'
        firewall_rule_object_model['filter'] = firewall_rule_object_filter_model
        firewall_rule_object_model['created_on'] = '2019-01-01T05:20:00.123Z'
        firewall_rule_object_model['modified_on'] = '2019-01-01T05:20:00.123Z'

        list_firewall_rules_resp_result_info_model = {} # ListFirewallRulesRespResultInfo
        list_firewall_rules_resp_result_info_model['page'] = 1
        list_firewall_rules_resp_result_info_model['per_page'] = 2
        list_firewall_rules_resp_result_info_model['count'] = 1
        list_firewall_rules_resp_result_info_model['total_count'] = 200

        # Construct a json representation of a ListFirewallRulesResp model
        list_firewall_rules_resp_model_json = {}
        list_firewall_rules_resp_model_json['success'] = True
        list_firewall_rules_resp_model_json['errors'] = [['testString']]
        list_firewall_rules_resp_model_json['messages'] = [['testString']]
        list_firewall_rules_resp_model_json['result'] = [firewall_rule_object_model]
        list_firewall_rules_resp_model_json['result_info'] = list_firewall_rules_resp_result_info_model

        # Construct a model instance of ListFirewallRulesResp by calling from_dict on the json representation
        list_firewall_rules_resp_model = ListFirewallRulesResp.from_dict(list_firewall_rules_resp_model_json)
        assert list_firewall_rules_resp_model != False

        # Construct a model instance of ListFirewallRulesResp by calling from_dict on the json representation
        list_firewall_rules_resp_model_dict = ListFirewallRulesResp.from_dict(list_firewall_rules_resp_model_json).__dict__
        list_firewall_rules_resp_model2 = ListFirewallRulesResp(**list_firewall_rules_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_firewall_rules_resp_model == list_firewall_rules_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_firewall_rules_resp_model_json2 = list_firewall_rules_resp_model.to_dict()
        assert list_firewall_rules_resp_model_json2 == list_firewall_rules_resp_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
