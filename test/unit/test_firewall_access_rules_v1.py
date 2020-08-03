# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.
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

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import re
import requests
import responses
from ibm_cloud_networking_services.firewall_access_rules_v1 import *

crn = 'testString'

service = FirewallAccessRulesV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: InstanceLevelFirewallAccessRules
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_all_account_access_rules
#-----------------------------------------------------------------------------
class TestListAllAccountAccessRules():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # list_all_account_access_rules()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_account_access_rules_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/firewall/access_rules/rules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "92f17202ed8bd63d69a66b86a49a8f6b", "notes": "This rule is set because of an event that occurred and caused X.", "allowed_modes": ["block"], "mode": "block", "scope": {"type": "account"}, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "configuration": {"target": "ip", "value": "ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ"}}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        notes = 'testString'
        mode = 'block'
        configuration_target = 'ip'
        configuration_value = '1.2.3.4'
        page = 38
        per_page = 5
        order = 'target'
        direction = 'asc'
        match = 'any'

        # Invoke method
        response = service.list_all_account_access_rules(
            notes=notes,
            mode=mode,
            configuration_target=configuration_target,
            configuration_value=configuration_value,
            page=page,
            per_page=per_page,
            order=order,
            direction=direction,
            match=match,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'notes={}'.format(notes) in query_string
        assert 'mode={}'.format(mode) in query_string
        assert 'configuration.target={}'.format(configuration_target) in query_string
        assert 'configuration.value={}'.format(configuration_value) in query_string
        assert 'page={}'.format(page) in query_string
        assert 'per_page={}'.format(per_page) in query_string
        assert 'order={}'.format(order) in query_string
        assert 'direction={}'.format(direction) in query_string
        assert 'match={}'.format(match) in query_string


    #--------------------------------------------------------
    # test_list_all_account_access_rules_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_account_access_rules_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/firewall/access_rules/rules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "92f17202ed8bd63d69a66b86a49a8f6b", "notes": "This rule is set because of an event that occurred and caused X.", "allowed_modes": ["block"], "mode": "block", "scope": {"type": "account"}, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "configuration": {"target": "ip", "value": "ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ"}}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_all_account_access_rules()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_all_account_access_rules_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_account_access_rules_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/firewall/access_rules/rules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "92f17202ed8bd63d69a66b86a49a8f6b", "notes": "This rule is set because of an event that occurred and caused X.", "allowed_modes": ["block"], "mode": "block", "scope": {"type": "account"}, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "configuration": {"target": "ip", "value": "ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ"}}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_all_account_access_rules(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for create_account_access_rule
#-----------------------------------------------------------------------------
class TestCreateAccountAccessRule():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # create_account_access_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_create_account_access_rule_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/firewall/access_rules/rules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "notes": "This rule is set because of an event that occurred and caused X.", "allowed_modes": ["block"], "mode": "block", "scope": {"type": "account"}, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "configuration": {"target": "ip", "value": "ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a AccountAccessRuleInputConfiguration model
        account_access_rule_input_configuration_model = {}
        account_access_rule_input_configuration_model['target'] = 'ip'
        account_access_rule_input_configuration_model['value'] = 'ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ'

        # Set up parameter values
        mode = 'block'
        notes = 'This rule is added because of event X that occurred on date xyz'
        configuration = account_access_rule_input_configuration_model

        # Invoke method
        response = service.create_account_access_rule(
            mode=mode,
            notes=notes,
            configuration=configuration,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['mode'] == 'block'
        assert req_body['notes'] == 'This rule is added because of event X that occurred on date xyz'
        assert req_body['configuration'] == account_access_rule_input_configuration_model


    #--------------------------------------------------------
    # test_create_account_access_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_account_access_rule_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/firewall/access_rules/rules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "notes": "This rule is set because of an event that occurred and caused X.", "allowed_modes": ["block"], "mode": "block", "scope": {"type": "account"}, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "configuration": {"target": "ip", "value": "ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.create_account_access_rule()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_create_account_access_rule_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_account_access_rule_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/firewall/access_rules/rules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "notes": "This rule is set because of an event that occurred and caused X.", "allowed_modes": ["block"], "mode": "block", "scope": {"type": "account"}, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "configuration": {"target": "ip", "value": "ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.create_account_access_rule(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_account_access_rule
#-----------------------------------------------------------------------------
class TestDeleteAccountAccessRule():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # delete_account_access_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_account_access_rule_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/firewall/access_rules/rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        accessrule_identifier = 'testString'

        # Invoke method
        response = service.delete_account_access_rule(
            accessrule_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_account_access_rule_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_account_access_rule_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/firewall/access_rules/rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        accessrule_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "accessrule_identifier": accessrule_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_account_access_rule(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_account_access_rule
#-----------------------------------------------------------------------------
class TestGetAccountAccessRule():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_account_access_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_get_account_access_rule_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/firewall/access_rules/rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "notes": "This rule is set because of an event that occurred and caused X.", "allowed_modes": ["block"], "mode": "block", "scope": {"type": "account"}, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "configuration": {"target": "ip", "value": "ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ"}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        accessrule_identifier = 'testString'

        # Invoke method
        response = service.get_account_access_rule(
            accessrule_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_account_access_rule_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_account_access_rule_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/firewall/access_rules/rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "notes": "This rule is set because of an event that occurred and caused X.", "allowed_modes": ["block"], "mode": "block", "scope": {"type": "account"}, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "configuration": {"target": "ip", "value": "ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ"}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        accessrule_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "accessrule_identifier": accessrule_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_account_access_rule(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_account_access_rule
#-----------------------------------------------------------------------------
class TestUpdateAccountAccessRule():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_account_access_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_update_account_access_rule_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/firewall/access_rules/rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "notes": "This rule is set because of an event that occurred and caused X.", "allowed_modes": ["block"], "mode": "block", "scope": {"type": "account"}, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "configuration": {"target": "ip", "value": "ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ"}}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        accessrule_identifier = 'testString'
        mode = 'block'
        notes = 'This rule is added because of event X that occurred on date xyz'

        # Invoke method
        response = service.update_account_access_rule(
            accessrule_identifier,
            mode=mode,
            notes=notes,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['mode'] == 'block'
        assert req_body['notes'] == 'This rule is added because of event X that occurred on date xyz'


    #--------------------------------------------------------
    # test_update_account_access_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_account_access_rule_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/firewall/access_rules/rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "notes": "This rule is set because of an event that occurred and caused X.", "allowed_modes": ["block"], "mode": "block", "scope": {"type": "account"}, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "configuration": {"target": "ip", "value": "ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ"}}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        accessrule_identifier = 'testString'

        # Invoke method
        response = service.update_account_access_rule(
            accessrule_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_account_access_rule_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_account_access_rule_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/firewall/access_rules/rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "notes": "This rule is set because of an event that occurred and caused X.", "allowed_modes": ["block"], "mode": "block", "scope": {"type": "account"}, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "configuration": {"target": "ip", "value": "ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ"}}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        accessrule_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "accessrule_identifier": accessrule_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_account_access_rule(**req_copy)



# endregion
##############################################################################
# End of Service: InstanceLevelFirewallAccessRules
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for AccountAccessRuleInputConfiguration
#-----------------------------------------------------------------------------
class TestAccountAccessRuleInputConfiguration():

    #--------------------------------------------------------
    # Test serialization/deserialization for AccountAccessRuleInputConfiguration
    #--------------------------------------------------------
    def test_account_access_rule_input_configuration_serialization(self):

        # Construct a json representation of a AccountAccessRuleInputConfiguration model
        account_access_rule_input_configuration_model_json = {}
        account_access_rule_input_configuration_model_json['target'] = 'ip'
        account_access_rule_input_configuration_model_json['value'] = 'ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ'

        # Construct a model instance of AccountAccessRuleInputConfiguration by calling from_dict on the json representation
        account_access_rule_input_configuration_model = AccountAccessRuleInputConfiguration.from_dict(account_access_rule_input_configuration_model_json)
        assert account_access_rule_input_configuration_model != False

        # Construct a model instance of AccountAccessRuleInputConfiguration by calling from_dict on the json representation
        account_access_rule_input_configuration_model_dict = AccountAccessRuleInputConfiguration.from_dict(account_access_rule_input_configuration_model_json).__dict__
        account_access_rule_input_configuration_model2 = AccountAccessRuleInputConfiguration(**account_access_rule_input_configuration_model_dict)

        # Verify the model instances are equivalent
        assert account_access_rule_input_configuration_model == account_access_rule_input_configuration_model2

        # Convert model instance back to dict and verify no loss of data
        account_access_rule_input_configuration_model_json2 = account_access_rule_input_configuration_model.to_dict()
        assert account_access_rule_input_configuration_model_json2 == account_access_rule_input_configuration_model_json

#-----------------------------------------------------------------------------
# Test Class for AccountAccessRuleObjectConfiguration
#-----------------------------------------------------------------------------
class TestAccountAccessRuleObjectConfiguration():

    #--------------------------------------------------------
    # Test serialization/deserialization for AccountAccessRuleObjectConfiguration
    #--------------------------------------------------------
    def test_account_access_rule_object_configuration_serialization(self):

        # Construct a json representation of a AccountAccessRuleObjectConfiguration model
        account_access_rule_object_configuration_model_json = {}
        account_access_rule_object_configuration_model_json['target'] = 'ip'
        account_access_rule_object_configuration_model_json['value'] = 'ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ'

        # Construct a model instance of AccountAccessRuleObjectConfiguration by calling from_dict on the json representation
        account_access_rule_object_configuration_model = AccountAccessRuleObjectConfiguration.from_dict(account_access_rule_object_configuration_model_json)
        assert account_access_rule_object_configuration_model != False

        # Construct a model instance of AccountAccessRuleObjectConfiguration by calling from_dict on the json representation
        account_access_rule_object_configuration_model_dict = AccountAccessRuleObjectConfiguration.from_dict(account_access_rule_object_configuration_model_json).__dict__
        account_access_rule_object_configuration_model2 = AccountAccessRuleObjectConfiguration(**account_access_rule_object_configuration_model_dict)

        # Verify the model instances are equivalent
        assert account_access_rule_object_configuration_model == account_access_rule_object_configuration_model2

        # Convert model instance back to dict and verify no loss of data
        account_access_rule_object_configuration_model_json2 = account_access_rule_object_configuration_model.to_dict()
        assert account_access_rule_object_configuration_model_json2 == account_access_rule_object_configuration_model_json

#-----------------------------------------------------------------------------
# Test Class for AccountAccessRuleObjectScope
#-----------------------------------------------------------------------------
class TestAccountAccessRuleObjectScope():

    #--------------------------------------------------------
    # Test serialization/deserialization for AccountAccessRuleObjectScope
    #--------------------------------------------------------
    def test_account_access_rule_object_scope_serialization(self):

        # Construct a json representation of a AccountAccessRuleObjectScope model
        account_access_rule_object_scope_model_json = {}
        account_access_rule_object_scope_model_json['type'] = 'account'

        # Construct a model instance of AccountAccessRuleObjectScope by calling from_dict on the json representation
        account_access_rule_object_scope_model = AccountAccessRuleObjectScope.from_dict(account_access_rule_object_scope_model_json)
        assert account_access_rule_object_scope_model != False

        # Construct a model instance of AccountAccessRuleObjectScope by calling from_dict on the json representation
        account_access_rule_object_scope_model_dict = AccountAccessRuleObjectScope.from_dict(account_access_rule_object_scope_model_json).__dict__
        account_access_rule_object_scope_model2 = AccountAccessRuleObjectScope(**account_access_rule_object_scope_model_dict)

        # Verify the model instances are equivalent
        assert account_access_rule_object_scope_model == account_access_rule_object_scope_model2

        # Convert model instance back to dict and verify no loss of data
        account_access_rule_object_scope_model_json2 = account_access_rule_object_scope_model.to_dict()
        assert account_access_rule_object_scope_model_json2 == account_access_rule_object_scope_model_json

#-----------------------------------------------------------------------------
# Test Class for DeleteAccountAccessRuleRespResult
#-----------------------------------------------------------------------------
class TestDeleteAccountAccessRuleRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for DeleteAccountAccessRuleRespResult
    #--------------------------------------------------------
    def test_delete_account_access_rule_resp_result_serialization(self):

        # Construct a json representation of a DeleteAccountAccessRuleRespResult model
        delete_account_access_rule_resp_result_model_json = {}
        delete_account_access_rule_resp_result_model_json['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'

        # Construct a model instance of DeleteAccountAccessRuleRespResult by calling from_dict on the json representation
        delete_account_access_rule_resp_result_model = DeleteAccountAccessRuleRespResult.from_dict(delete_account_access_rule_resp_result_model_json)
        assert delete_account_access_rule_resp_result_model != False

        # Construct a model instance of DeleteAccountAccessRuleRespResult by calling from_dict on the json representation
        delete_account_access_rule_resp_result_model_dict = DeleteAccountAccessRuleRespResult.from_dict(delete_account_access_rule_resp_result_model_json).__dict__
        delete_account_access_rule_resp_result_model2 = DeleteAccountAccessRuleRespResult(**delete_account_access_rule_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert delete_account_access_rule_resp_result_model == delete_account_access_rule_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        delete_account_access_rule_resp_result_model_json2 = delete_account_access_rule_resp_result_model.to_dict()
        assert delete_account_access_rule_resp_result_model_json2 == delete_account_access_rule_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for ListAccountAccessRulesRespResultInfo
#-----------------------------------------------------------------------------
class TestListAccountAccessRulesRespResultInfo():

    #--------------------------------------------------------
    # Test serialization/deserialization for ListAccountAccessRulesRespResultInfo
    #--------------------------------------------------------
    def test_list_account_access_rules_resp_result_info_serialization(self):

        # Construct a json representation of a ListAccountAccessRulesRespResultInfo model
        list_account_access_rules_resp_result_info_model_json = {}
        list_account_access_rules_resp_result_info_model_json['page'] = 1
        list_account_access_rules_resp_result_info_model_json['per_page'] = 2
        list_account_access_rules_resp_result_info_model_json['count'] = 1
        list_account_access_rules_resp_result_info_model_json['total_count'] = 200

        # Construct a model instance of ListAccountAccessRulesRespResultInfo by calling from_dict on the json representation
        list_account_access_rules_resp_result_info_model = ListAccountAccessRulesRespResultInfo.from_dict(list_account_access_rules_resp_result_info_model_json)
        assert list_account_access_rules_resp_result_info_model != False

        # Construct a model instance of ListAccountAccessRulesRespResultInfo by calling from_dict on the json representation
        list_account_access_rules_resp_result_info_model_dict = ListAccountAccessRulesRespResultInfo.from_dict(list_account_access_rules_resp_result_info_model_json).__dict__
        list_account_access_rules_resp_result_info_model2 = ListAccountAccessRulesRespResultInfo(**list_account_access_rules_resp_result_info_model_dict)

        # Verify the model instances are equivalent
        assert list_account_access_rules_resp_result_info_model == list_account_access_rules_resp_result_info_model2

        # Convert model instance back to dict and verify no loss of data
        list_account_access_rules_resp_result_info_model_json2 = list_account_access_rules_resp_result_info_model.to_dict()
        assert list_account_access_rules_resp_result_info_model_json2 == list_account_access_rules_resp_result_info_model_json

#-----------------------------------------------------------------------------
# Test Class for AccountAccessRuleObject
#-----------------------------------------------------------------------------
class TestAccountAccessRuleObject():

    #--------------------------------------------------------
    # Test serialization/deserialization for AccountAccessRuleObject
    #--------------------------------------------------------
    def test_account_access_rule_object_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        account_access_rule_object_configuration_model = {} # AccountAccessRuleObjectConfiguration
        account_access_rule_object_configuration_model['target'] = 'ip'
        account_access_rule_object_configuration_model['value'] = 'ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ'

        account_access_rule_object_scope_model = {} # AccountAccessRuleObjectScope
        account_access_rule_object_scope_model['type'] = 'account'

        # Construct a json representation of a AccountAccessRuleObject model
        account_access_rule_object_model_json = {}
        account_access_rule_object_model_json['id'] = '92f17202ed8bd63d69a66b86a49a8f6b'
        account_access_rule_object_model_json['notes'] = 'This rule is set because of an event that occurred and caused X.'
        account_access_rule_object_model_json['allowed_modes'] = ['block']
        account_access_rule_object_model_json['mode'] = 'block'
        account_access_rule_object_model_json['scope'] = account_access_rule_object_scope_model
        account_access_rule_object_model_json['created_on'] = '2020-01-28T18:40:40.123456Z'
        account_access_rule_object_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'
        account_access_rule_object_model_json['configuration'] = account_access_rule_object_configuration_model

        # Construct a model instance of AccountAccessRuleObject by calling from_dict on the json representation
        account_access_rule_object_model = AccountAccessRuleObject.from_dict(account_access_rule_object_model_json)
        assert account_access_rule_object_model != False

        # Construct a model instance of AccountAccessRuleObject by calling from_dict on the json representation
        account_access_rule_object_model_dict = AccountAccessRuleObject.from_dict(account_access_rule_object_model_json).__dict__
        account_access_rule_object_model2 = AccountAccessRuleObject(**account_access_rule_object_model_dict)

        # Verify the model instances are equivalent
        assert account_access_rule_object_model == account_access_rule_object_model2

        # Convert model instance back to dict and verify no loss of data
        account_access_rule_object_model_json2 = account_access_rule_object_model.to_dict()
        assert account_access_rule_object_model_json2 == account_access_rule_object_model_json

#-----------------------------------------------------------------------------
# Test Class for AccountAccessRuleResp
#-----------------------------------------------------------------------------
class TestAccountAccessRuleResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for AccountAccessRuleResp
    #--------------------------------------------------------
    def test_account_access_rule_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        account_access_rule_object_configuration_model = {} # AccountAccessRuleObjectConfiguration
        account_access_rule_object_configuration_model['target'] = 'ip'
        account_access_rule_object_configuration_model['value'] = 'ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ'

        account_access_rule_object_scope_model = {} # AccountAccessRuleObjectScope
        account_access_rule_object_scope_model['type'] = 'account'

        account_access_rule_object_model = {} # AccountAccessRuleObject
        account_access_rule_object_model['id'] = '92f17202ed8bd63d69a66b86a49a8f6b'
        account_access_rule_object_model['notes'] = 'This rule is set because of an event that occurred and caused X.'
        account_access_rule_object_model['allowed_modes'] = ['block']
        account_access_rule_object_model['mode'] = 'block'
        account_access_rule_object_model['scope'] = account_access_rule_object_scope_model
        account_access_rule_object_model['created_on'] = '2020-01-28T18:40:40.123456Z'
        account_access_rule_object_model['modified_on'] = '2020-01-28T18:40:40.123456Z'
        account_access_rule_object_model['configuration'] = account_access_rule_object_configuration_model

        # Construct a json representation of a AccountAccessRuleResp model
        account_access_rule_resp_model_json = {}
        account_access_rule_resp_model_json['success'] = True
        account_access_rule_resp_model_json['errors'] = [['testString']]
        account_access_rule_resp_model_json['messages'] = [['testString']]
        account_access_rule_resp_model_json['result'] = account_access_rule_object_model

        # Construct a model instance of AccountAccessRuleResp by calling from_dict on the json representation
        account_access_rule_resp_model = AccountAccessRuleResp.from_dict(account_access_rule_resp_model_json)
        assert account_access_rule_resp_model != False

        # Construct a model instance of AccountAccessRuleResp by calling from_dict on the json representation
        account_access_rule_resp_model_dict = AccountAccessRuleResp.from_dict(account_access_rule_resp_model_json).__dict__
        account_access_rule_resp_model2 = AccountAccessRuleResp(**account_access_rule_resp_model_dict)

        # Verify the model instances are equivalent
        assert account_access_rule_resp_model == account_access_rule_resp_model2

        # Convert model instance back to dict and verify no loss of data
        account_access_rule_resp_model_json2 = account_access_rule_resp_model.to_dict()
        assert account_access_rule_resp_model_json2 == account_access_rule_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for DeleteAccountAccessRuleResp
#-----------------------------------------------------------------------------
class TestDeleteAccountAccessRuleResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for DeleteAccountAccessRuleResp
    #--------------------------------------------------------
    def test_delete_account_access_rule_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        delete_account_access_rule_resp_result_model = {} # DeleteAccountAccessRuleRespResult
        delete_account_access_rule_resp_result_model['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'

        # Construct a json representation of a DeleteAccountAccessRuleResp model
        delete_account_access_rule_resp_model_json = {}
        delete_account_access_rule_resp_model_json['success'] = True
        delete_account_access_rule_resp_model_json['errors'] = [['testString']]
        delete_account_access_rule_resp_model_json['messages'] = [['testString']]
        delete_account_access_rule_resp_model_json['result'] = delete_account_access_rule_resp_result_model

        # Construct a model instance of DeleteAccountAccessRuleResp by calling from_dict on the json representation
        delete_account_access_rule_resp_model = DeleteAccountAccessRuleResp.from_dict(delete_account_access_rule_resp_model_json)
        assert delete_account_access_rule_resp_model != False

        # Construct a model instance of DeleteAccountAccessRuleResp by calling from_dict on the json representation
        delete_account_access_rule_resp_model_dict = DeleteAccountAccessRuleResp.from_dict(delete_account_access_rule_resp_model_json).__dict__
        delete_account_access_rule_resp_model2 = DeleteAccountAccessRuleResp(**delete_account_access_rule_resp_model_dict)

        # Verify the model instances are equivalent
        assert delete_account_access_rule_resp_model == delete_account_access_rule_resp_model2

        # Convert model instance back to dict and verify no loss of data
        delete_account_access_rule_resp_model_json2 = delete_account_access_rule_resp_model.to_dict()
        assert delete_account_access_rule_resp_model_json2 == delete_account_access_rule_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for ListAccountAccessRulesResp
#-----------------------------------------------------------------------------
class TestListAccountAccessRulesResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for ListAccountAccessRulesResp
    #--------------------------------------------------------
    def test_list_account_access_rules_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        account_access_rule_object_configuration_model = {} # AccountAccessRuleObjectConfiguration
        account_access_rule_object_configuration_model['target'] = 'ip'
        account_access_rule_object_configuration_model['value'] = 'ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ'

        account_access_rule_object_scope_model = {} # AccountAccessRuleObjectScope
        account_access_rule_object_scope_model['type'] = 'account'

        account_access_rule_object_model = {} # AccountAccessRuleObject
        account_access_rule_object_model['id'] = '92f17202ed8bd63d69a66b86a49a8f6b'
        account_access_rule_object_model['notes'] = 'This rule is set because of an event that occurred and caused X.'
        account_access_rule_object_model['allowed_modes'] = ['block']
        account_access_rule_object_model['mode'] = 'block'
        account_access_rule_object_model['scope'] = account_access_rule_object_scope_model
        account_access_rule_object_model['created_on'] = '2020-01-28T18:40:40.123456Z'
        account_access_rule_object_model['modified_on'] = '2020-01-28T18:40:40.123456Z'
        account_access_rule_object_model['configuration'] = account_access_rule_object_configuration_model

        list_account_access_rules_resp_result_info_model = {} # ListAccountAccessRulesRespResultInfo
        list_account_access_rules_resp_result_info_model['page'] = 1
        list_account_access_rules_resp_result_info_model['per_page'] = 2
        list_account_access_rules_resp_result_info_model['count'] = 1
        list_account_access_rules_resp_result_info_model['total_count'] = 200

        # Construct a json representation of a ListAccountAccessRulesResp model
        list_account_access_rules_resp_model_json = {}
        list_account_access_rules_resp_model_json['success'] = True
        list_account_access_rules_resp_model_json['errors'] = [['testString']]
        list_account_access_rules_resp_model_json['messages'] = [['testString']]
        list_account_access_rules_resp_model_json['result'] = [account_access_rule_object_model]
        list_account_access_rules_resp_model_json['result_info'] = list_account_access_rules_resp_result_info_model

        # Construct a model instance of ListAccountAccessRulesResp by calling from_dict on the json representation
        list_account_access_rules_resp_model = ListAccountAccessRulesResp.from_dict(list_account_access_rules_resp_model_json)
        assert list_account_access_rules_resp_model != False

        # Construct a model instance of ListAccountAccessRulesResp by calling from_dict on the json representation
        list_account_access_rules_resp_model_dict = ListAccountAccessRulesResp.from_dict(list_account_access_rules_resp_model_json).__dict__
        list_account_access_rules_resp_model2 = ListAccountAccessRulesResp(**list_account_access_rules_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_account_access_rules_resp_model == list_account_access_rules_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_account_access_rules_resp_model_json2 = list_account_access_rules_resp_model.to_dict()
        assert list_account_access_rules_resp_model_json2 == list_account_access_rules_resp_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
