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

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import re
import requests
import responses
from ibm_cloud_networking_services.zone_firewall_access_rules_v1 import *

crn = 'testString'
zone_identifier = 'testString'

service = ZoneFirewallAccessRulesV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn,
    zone_identifier=zone_identifier
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: ZoneFirewallAccessRules
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_all_zone_access_rules
#-----------------------------------------------------------------------------
class TestListAllZoneAccessRules():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # list_all_zone_access_rules()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_zone_access_rules_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/access_rules/rules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "92f17202ed8bd63d69a66b86a49a8f6b", "notes": "This rule is set because of an event that occurred and caused X.", "allowed_modes": ["block"], "mode": "block", "scope": {"type": "account"}, "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "configuration": {"target": "ip", "value": "ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ"}}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
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
        order = 'configuration.target'
        direction = 'asc'
        match = 'any'

        # Invoke method
        response = service.list_all_zone_access_rules(
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
    # test_list_all_zone_access_rules_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_zone_access_rules_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/access_rules/rules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "92f17202ed8bd63d69a66b86a49a8f6b", "notes": "This rule is set because of an event that occurred and caused X.", "allowed_modes": ["block"], "mode": "block", "scope": {"type": "account"}, "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "configuration": {"target": "ip", "value": "ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ"}}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_all_zone_access_rules()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_all_zone_access_rules_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_zone_access_rules_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/access_rules/rules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "92f17202ed8bd63d69a66b86a49a8f6b", "notes": "This rule is set because of an event that occurred and caused X.", "allowed_modes": ["block"], "mode": "block", "scope": {"type": "account"}, "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "configuration": {"target": "ip", "value": "ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ"}}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
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
                service.list_all_zone_access_rules(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for create_zone_access_rule
#-----------------------------------------------------------------------------
class TestCreateZoneAccessRule():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # create_zone_access_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_create_zone_access_rule_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/access_rules/rules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "notes": "This rule is set because of an event that occurred and caused X.", "allowed_modes": ["block"], "mode": "block", "scope": {"type": "account"}, "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "configuration": {"target": "ip", "value": "ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ZoneAccessRuleInputConfiguration model
        zone_access_rule_input_configuration_model = {}
        zone_access_rule_input_configuration_model['target'] = 'ip'
        zone_access_rule_input_configuration_model['value'] = 'ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ'

        # Set up parameter values
        mode = 'block'
        notes = 'This rule is added because of event X that occurred on date xyz'
        configuration = zone_access_rule_input_configuration_model

        # Invoke method
        response = service.create_zone_access_rule(
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
        assert req_body['configuration'] == zone_access_rule_input_configuration_model


    #--------------------------------------------------------
    # test_create_zone_access_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_zone_access_rule_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/access_rules/rules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "notes": "This rule is set because of an event that occurred and caused X.", "allowed_modes": ["block"], "mode": "block", "scope": {"type": "account"}, "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "configuration": {"target": "ip", "value": "ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.create_zone_access_rule()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_create_zone_access_rule_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_zone_access_rule_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/access_rules/rules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "notes": "This rule is set because of an event that occurred and caused X.", "allowed_modes": ["block"], "mode": "block", "scope": {"type": "account"}, "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "configuration": {"target": "ip", "value": "ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ"}}}'
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
                service.create_zone_access_rule(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_zone_access_rule
#-----------------------------------------------------------------------------
class TestDeleteZoneAccessRule():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # delete_zone_access_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_zone_access_rule_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/access_rules/rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        accessrule_identifier = 'testString'

        # Invoke method
        response = service.delete_zone_access_rule(
            accessrule_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_zone_access_rule_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_zone_access_rule_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/access_rules/rules/testString')
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
                service.delete_zone_access_rule(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_zone_access_rule
#-----------------------------------------------------------------------------
class TestGetZoneAccessRule():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_zone_access_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_get_zone_access_rule_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/access_rules/rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "notes": "This rule is set because of an event that occurred and caused X.", "allowed_modes": ["block"], "mode": "block", "scope": {"type": "account"}, "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "configuration": {"target": "ip", "value": "ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ"}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        accessrule_identifier = 'testString'

        # Invoke method
        response = service.get_zone_access_rule(
            accessrule_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_zone_access_rule_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_zone_access_rule_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/access_rules/rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "notes": "This rule is set because of an event that occurred and caused X.", "allowed_modes": ["block"], "mode": "block", "scope": {"type": "account"}, "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "configuration": {"target": "ip", "value": "ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ"}}}'
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
                service.get_zone_access_rule(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_zone_access_rule
#-----------------------------------------------------------------------------
class TestUpdateZoneAccessRule():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_zone_access_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_update_zone_access_rule_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/access_rules/rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "notes": "This rule is set because of an event that occurred and caused X.", "allowed_modes": ["block"], "mode": "block", "scope": {"type": "account"}, "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "configuration": {"target": "ip", "value": "ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ"}}}'
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
        response = service.update_zone_access_rule(
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
    # test_update_zone_access_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_zone_access_rule_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/access_rules/rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "notes": "This rule is set because of an event that occurred and caused X.", "allowed_modes": ["block"], "mode": "block", "scope": {"type": "account"}, "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "configuration": {"target": "ip", "value": "ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ"}}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        accessrule_identifier = 'testString'

        # Invoke method
        response = service.update_zone_access_rule(
            accessrule_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_zone_access_rule_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_zone_access_rule_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/access_rules/rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "notes": "This rule is set because of an event that occurred and caused X.", "allowed_modes": ["block"], "mode": "block", "scope": {"type": "account"}, "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "configuration": {"target": "ip", "value": "ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ"}}}'
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
                service.update_zone_access_rule(**req_copy)



# endregion
##############################################################################
# End of Service: ZoneFirewallAccessRules
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for DeleteZoneAccessRuleRespResult
#-----------------------------------------------------------------------------
class TestDeleteZoneAccessRuleRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for DeleteZoneAccessRuleRespResult
    #--------------------------------------------------------
    def test_delete_zone_access_rule_resp_result_serialization(self):

        # Construct a json representation of a DeleteZoneAccessRuleRespResult model
        delete_zone_access_rule_resp_result_model_json = {}
        delete_zone_access_rule_resp_result_model_json['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'

        # Construct a model instance of DeleteZoneAccessRuleRespResult by calling from_dict on the json representation
        delete_zone_access_rule_resp_result_model = DeleteZoneAccessRuleRespResult.from_dict(delete_zone_access_rule_resp_result_model_json)
        assert delete_zone_access_rule_resp_result_model != False

        # Construct a model instance of DeleteZoneAccessRuleRespResult by calling from_dict on the json representation
        delete_zone_access_rule_resp_result_model_dict = DeleteZoneAccessRuleRespResult.from_dict(delete_zone_access_rule_resp_result_model_json).__dict__
        delete_zone_access_rule_resp_result_model2 = DeleteZoneAccessRuleRespResult(**delete_zone_access_rule_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert delete_zone_access_rule_resp_result_model == delete_zone_access_rule_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        delete_zone_access_rule_resp_result_model_json2 = delete_zone_access_rule_resp_result_model.to_dict()
        assert delete_zone_access_rule_resp_result_model_json2 == delete_zone_access_rule_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for ListZoneAccessRulesRespResultInfo
#-----------------------------------------------------------------------------
class TestListZoneAccessRulesRespResultInfo():

    #--------------------------------------------------------
    # Test serialization/deserialization for ListZoneAccessRulesRespResultInfo
    #--------------------------------------------------------
    def test_list_zone_access_rules_resp_result_info_serialization(self):

        # Construct a json representation of a ListZoneAccessRulesRespResultInfo model
        list_zone_access_rules_resp_result_info_model_json = {}
        list_zone_access_rules_resp_result_info_model_json['page'] = 1
        list_zone_access_rules_resp_result_info_model_json['per_page'] = 2
        list_zone_access_rules_resp_result_info_model_json['count'] = 1
        list_zone_access_rules_resp_result_info_model_json['total_count'] = 200

        # Construct a model instance of ListZoneAccessRulesRespResultInfo by calling from_dict on the json representation
        list_zone_access_rules_resp_result_info_model = ListZoneAccessRulesRespResultInfo.from_dict(list_zone_access_rules_resp_result_info_model_json)
        assert list_zone_access_rules_resp_result_info_model != False

        # Construct a model instance of ListZoneAccessRulesRespResultInfo by calling from_dict on the json representation
        list_zone_access_rules_resp_result_info_model_dict = ListZoneAccessRulesRespResultInfo.from_dict(list_zone_access_rules_resp_result_info_model_json).__dict__
        list_zone_access_rules_resp_result_info_model2 = ListZoneAccessRulesRespResultInfo(**list_zone_access_rules_resp_result_info_model_dict)

        # Verify the model instances are equivalent
        assert list_zone_access_rules_resp_result_info_model == list_zone_access_rules_resp_result_info_model2

        # Convert model instance back to dict and verify no loss of data
        list_zone_access_rules_resp_result_info_model_json2 = list_zone_access_rules_resp_result_info_model.to_dict()
        assert list_zone_access_rules_resp_result_info_model_json2 == list_zone_access_rules_resp_result_info_model_json

#-----------------------------------------------------------------------------
# Test Class for ZoneAccessRuleInputConfiguration
#-----------------------------------------------------------------------------
class TestZoneAccessRuleInputConfiguration():

    #--------------------------------------------------------
    # Test serialization/deserialization for ZoneAccessRuleInputConfiguration
    #--------------------------------------------------------
    def test_zone_access_rule_input_configuration_serialization(self):

        # Construct a json representation of a ZoneAccessRuleInputConfiguration model
        zone_access_rule_input_configuration_model_json = {}
        zone_access_rule_input_configuration_model_json['target'] = 'ip'
        zone_access_rule_input_configuration_model_json['value'] = 'ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ'

        # Construct a model instance of ZoneAccessRuleInputConfiguration by calling from_dict on the json representation
        zone_access_rule_input_configuration_model = ZoneAccessRuleInputConfiguration.from_dict(zone_access_rule_input_configuration_model_json)
        assert zone_access_rule_input_configuration_model != False

        # Construct a model instance of ZoneAccessRuleInputConfiguration by calling from_dict on the json representation
        zone_access_rule_input_configuration_model_dict = ZoneAccessRuleInputConfiguration.from_dict(zone_access_rule_input_configuration_model_json).__dict__
        zone_access_rule_input_configuration_model2 = ZoneAccessRuleInputConfiguration(**zone_access_rule_input_configuration_model_dict)

        # Verify the model instances are equivalent
        assert zone_access_rule_input_configuration_model == zone_access_rule_input_configuration_model2

        # Convert model instance back to dict and verify no loss of data
        zone_access_rule_input_configuration_model_json2 = zone_access_rule_input_configuration_model.to_dict()
        assert zone_access_rule_input_configuration_model_json2 == zone_access_rule_input_configuration_model_json

#-----------------------------------------------------------------------------
# Test Class for ZoneAccessRuleObjectConfiguration
#-----------------------------------------------------------------------------
class TestZoneAccessRuleObjectConfiguration():

    #--------------------------------------------------------
    # Test serialization/deserialization for ZoneAccessRuleObjectConfiguration
    #--------------------------------------------------------
    def test_zone_access_rule_object_configuration_serialization(self):

        # Construct a json representation of a ZoneAccessRuleObjectConfiguration model
        zone_access_rule_object_configuration_model_json = {}
        zone_access_rule_object_configuration_model_json['target'] = 'ip'
        zone_access_rule_object_configuration_model_json['value'] = 'ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ'

        # Construct a model instance of ZoneAccessRuleObjectConfiguration by calling from_dict on the json representation
        zone_access_rule_object_configuration_model = ZoneAccessRuleObjectConfiguration.from_dict(zone_access_rule_object_configuration_model_json)
        assert zone_access_rule_object_configuration_model != False

        # Construct a model instance of ZoneAccessRuleObjectConfiguration by calling from_dict on the json representation
        zone_access_rule_object_configuration_model_dict = ZoneAccessRuleObjectConfiguration.from_dict(zone_access_rule_object_configuration_model_json).__dict__
        zone_access_rule_object_configuration_model2 = ZoneAccessRuleObjectConfiguration(**zone_access_rule_object_configuration_model_dict)

        # Verify the model instances are equivalent
        assert zone_access_rule_object_configuration_model == zone_access_rule_object_configuration_model2

        # Convert model instance back to dict and verify no loss of data
        zone_access_rule_object_configuration_model_json2 = zone_access_rule_object_configuration_model.to_dict()
        assert zone_access_rule_object_configuration_model_json2 == zone_access_rule_object_configuration_model_json

#-----------------------------------------------------------------------------
# Test Class for ZoneAccessRuleObjectScope
#-----------------------------------------------------------------------------
class TestZoneAccessRuleObjectScope():

    #--------------------------------------------------------
    # Test serialization/deserialization for ZoneAccessRuleObjectScope
    #--------------------------------------------------------
    def test_zone_access_rule_object_scope_serialization(self):

        # Construct a json representation of a ZoneAccessRuleObjectScope model
        zone_access_rule_object_scope_model_json = {}
        zone_access_rule_object_scope_model_json['type'] = 'account'

        # Construct a model instance of ZoneAccessRuleObjectScope by calling from_dict on the json representation
        zone_access_rule_object_scope_model = ZoneAccessRuleObjectScope.from_dict(zone_access_rule_object_scope_model_json)
        assert zone_access_rule_object_scope_model != False

        # Construct a model instance of ZoneAccessRuleObjectScope by calling from_dict on the json representation
        zone_access_rule_object_scope_model_dict = ZoneAccessRuleObjectScope.from_dict(zone_access_rule_object_scope_model_json).__dict__
        zone_access_rule_object_scope_model2 = ZoneAccessRuleObjectScope(**zone_access_rule_object_scope_model_dict)

        # Verify the model instances are equivalent
        assert zone_access_rule_object_scope_model == zone_access_rule_object_scope_model2

        # Convert model instance back to dict and verify no loss of data
        zone_access_rule_object_scope_model_json2 = zone_access_rule_object_scope_model.to_dict()
        assert zone_access_rule_object_scope_model_json2 == zone_access_rule_object_scope_model_json

#-----------------------------------------------------------------------------
# Test Class for DeleteZoneAccessRuleResp
#-----------------------------------------------------------------------------
class TestDeleteZoneAccessRuleResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for DeleteZoneAccessRuleResp
    #--------------------------------------------------------
    def test_delete_zone_access_rule_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        delete_zone_access_rule_resp_result_model = {} # DeleteZoneAccessRuleRespResult
        delete_zone_access_rule_resp_result_model['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'

        # Construct a json representation of a DeleteZoneAccessRuleResp model
        delete_zone_access_rule_resp_model_json = {}
        delete_zone_access_rule_resp_model_json['success'] = True
        delete_zone_access_rule_resp_model_json['errors'] = [['testString']]
        delete_zone_access_rule_resp_model_json['messages'] = [['testString']]
        delete_zone_access_rule_resp_model_json['result'] = delete_zone_access_rule_resp_result_model

        # Construct a model instance of DeleteZoneAccessRuleResp by calling from_dict on the json representation
        delete_zone_access_rule_resp_model = DeleteZoneAccessRuleResp.from_dict(delete_zone_access_rule_resp_model_json)
        assert delete_zone_access_rule_resp_model != False

        # Construct a model instance of DeleteZoneAccessRuleResp by calling from_dict on the json representation
        delete_zone_access_rule_resp_model_dict = DeleteZoneAccessRuleResp.from_dict(delete_zone_access_rule_resp_model_json).__dict__
        delete_zone_access_rule_resp_model2 = DeleteZoneAccessRuleResp(**delete_zone_access_rule_resp_model_dict)

        # Verify the model instances are equivalent
        assert delete_zone_access_rule_resp_model == delete_zone_access_rule_resp_model2

        # Convert model instance back to dict and verify no loss of data
        delete_zone_access_rule_resp_model_json2 = delete_zone_access_rule_resp_model.to_dict()
        assert delete_zone_access_rule_resp_model_json2 == delete_zone_access_rule_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for ListZoneAccessRulesResp
#-----------------------------------------------------------------------------
class TestListZoneAccessRulesResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for ListZoneAccessRulesResp
    #--------------------------------------------------------
    def test_list_zone_access_rules_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        zone_access_rule_object_configuration_model = {} # ZoneAccessRuleObjectConfiguration
        zone_access_rule_object_configuration_model['target'] = 'ip'
        zone_access_rule_object_configuration_model['value'] = 'ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ'

        zone_access_rule_object_scope_model = {} # ZoneAccessRuleObjectScope
        zone_access_rule_object_scope_model['type'] = 'account'

        list_zone_access_rules_resp_result_info_model = {} # ListZoneAccessRulesRespResultInfo
        list_zone_access_rules_resp_result_info_model['page'] = 1
        list_zone_access_rules_resp_result_info_model['per_page'] = 2
        list_zone_access_rules_resp_result_info_model['count'] = 1
        list_zone_access_rules_resp_result_info_model['total_count'] = 200

        zone_access_rule_object_model = {} # ZoneAccessRuleObject
        zone_access_rule_object_model['id'] = '92f17202ed8bd63d69a66b86a49a8f6b'
        zone_access_rule_object_model['notes'] = 'This rule is set because of an event that occurred and caused X.'
        zone_access_rule_object_model['allowed_modes'] = ['block']
        zone_access_rule_object_model['mode'] = 'block'
        zone_access_rule_object_model['scope'] = zone_access_rule_object_scope_model
        zone_access_rule_object_model['created_on'] = '2014-01-01T05:20:00.12345Z'
        zone_access_rule_object_model['modified_on'] = '2014-01-01T05:20:00.12345Z'
        zone_access_rule_object_model['configuration'] = zone_access_rule_object_configuration_model

        # Construct a json representation of a ListZoneAccessRulesResp model
        list_zone_access_rules_resp_model_json = {}
        list_zone_access_rules_resp_model_json['success'] = True
        list_zone_access_rules_resp_model_json['errors'] = [['testString']]
        list_zone_access_rules_resp_model_json['messages'] = [['testString']]
        list_zone_access_rules_resp_model_json['result'] = [zone_access_rule_object_model]
        list_zone_access_rules_resp_model_json['result_info'] = list_zone_access_rules_resp_result_info_model

        # Construct a model instance of ListZoneAccessRulesResp by calling from_dict on the json representation
        list_zone_access_rules_resp_model = ListZoneAccessRulesResp.from_dict(list_zone_access_rules_resp_model_json)
        assert list_zone_access_rules_resp_model != False

        # Construct a model instance of ListZoneAccessRulesResp by calling from_dict on the json representation
        list_zone_access_rules_resp_model_dict = ListZoneAccessRulesResp.from_dict(list_zone_access_rules_resp_model_json).__dict__
        list_zone_access_rules_resp_model2 = ListZoneAccessRulesResp(**list_zone_access_rules_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_zone_access_rules_resp_model == list_zone_access_rules_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_zone_access_rules_resp_model_json2 = list_zone_access_rules_resp_model.to_dict()
        assert list_zone_access_rules_resp_model_json2 == list_zone_access_rules_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for ZoneAccessRuleObject
#-----------------------------------------------------------------------------
class TestZoneAccessRuleObject():

    #--------------------------------------------------------
    # Test serialization/deserialization for ZoneAccessRuleObject
    #--------------------------------------------------------
    def test_zone_access_rule_object_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        zone_access_rule_object_configuration_model = {} # ZoneAccessRuleObjectConfiguration
        zone_access_rule_object_configuration_model['target'] = 'ip'
        zone_access_rule_object_configuration_model['value'] = 'ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ'

        zone_access_rule_object_scope_model = {} # ZoneAccessRuleObjectScope
        zone_access_rule_object_scope_model['type'] = 'account'

        # Construct a json representation of a ZoneAccessRuleObject model
        zone_access_rule_object_model_json = {}
        zone_access_rule_object_model_json['id'] = '92f17202ed8bd63d69a66b86a49a8f6b'
        zone_access_rule_object_model_json['notes'] = 'This rule is set because of an event that occurred and caused X.'
        zone_access_rule_object_model_json['allowed_modes'] = ['block']
        zone_access_rule_object_model_json['mode'] = 'block'
        zone_access_rule_object_model_json['scope'] = zone_access_rule_object_scope_model
        zone_access_rule_object_model_json['created_on'] = '2014-01-01T05:20:00.12345Z'
        zone_access_rule_object_model_json['modified_on'] = '2014-01-01T05:20:00.12345Z'
        zone_access_rule_object_model_json['configuration'] = zone_access_rule_object_configuration_model

        # Construct a model instance of ZoneAccessRuleObject by calling from_dict on the json representation
        zone_access_rule_object_model = ZoneAccessRuleObject.from_dict(zone_access_rule_object_model_json)
        assert zone_access_rule_object_model != False

        # Construct a model instance of ZoneAccessRuleObject by calling from_dict on the json representation
        zone_access_rule_object_model_dict = ZoneAccessRuleObject.from_dict(zone_access_rule_object_model_json).__dict__
        zone_access_rule_object_model2 = ZoneAccessRuleObject(**zone_access_rule_object_model_dict)

        # Verify the model instances are equivalent
        assert zone_access_rule_object_model == zone_access_rule_object_model2

        # Convert model instance back to dict and verify no loss of data
        zone_access_rule_object_model_json2 = zone_access_rule_object_model.to_dict()
        assert zone_access_rule_object_model_json2 == zone_access_rule_object_model_json

#-----------------------------------------------------------------------------
# Test Class for ZoneAccessRuleResp
#-----------------------------------------------------------------------------
class TestZoneAccessRuleResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for ZoneAccessRuleResp
    #--------------------------------------------------------
    def test_zone_access_rule_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        zone_access_rule_object_configuration_model = {} # ZoneAccessRuleObjectConfiguration
        zone_access_rule_object_configuration_model['target'] = 'ip'
        zone_access_rule_object_configuration_model['value'] = 'ip example 198.51.100.4; ip_range example 198.51.100.4/16 ; asn example AS12345; country example AZ'

        zone_access_rule_object_scope_model = {} # ZoneAccessRuleObjectScope
        zone_access_rule_object_scope_model['type'] = 'account'

        zone_access_rule_object_model = {} # ZoneAccessRuleObject
        zone_access_rule_object_model['id'] = '92f17202ed8bd63d69a66b86a49a8f6b'
        zone_access_rule_object_model['notes'] = 'This rule is set because of an event that occurred and caused X.'
        zone_access_rule_object_model['allowed_modes'] = ['block']
        zone_access_rule_object_model['mode'] = 'block'
        zone_access_rule_object_model['scope'] = zone_access_rule_object_scope_model
        zone_access_rule_object_model['created_on'] = '2014-01-01T05:20:00.12345Z'
        zone_access_rule_object_model['modified_on'] = '2014-01-01T05:20:00.12345Z'
        zone_access_rule_object_model['configuration'] = zone_access_rule_object_configuration_model

        # Construct a json representation of a ZoneAccessRuleResp model
        zone_access_rule_resp_model_json = {}
        zone_access_rule_resp_model_json['success'] = True
        zone_access_rule_resp_model_json['errors'] = [['testString']]
        zone_access_rule_resp_model_json['messages'] = [['testString']]
        zone_access_rule_resp_model_json['result'] = zone_access_rule_object_model

        # Construct a model instance of ZoneAccessRuleResp by calling from_dict on the json representation
        zone_access_rule_resp_model = ZoneAccessRuleResp.from_dict(zone_access_rule_resp_model_json)
        assert zone_access_rule_resp_model != False

        # Construct a model instance of ZoneAccessRuleResp by calling from_dict on the json representation
        zone_access_rule_resp_model_dict = ZoneAccessRuleResp.from_dict(zone_access_rule_resp_model_json).__dict__
        zone_access_rule_resp_model2 = ZoneAccessRuleResp(**zone_access_rule_resp_model_dict)

        # Verify the model instances are equivalent
        assert zone_access_rule_resp_model == zone_access_rule_resp_model2

        # Convert model instance back to dict and verify no loss of data
        zone_access_rule_resp_model_json2 = zone_access_rule_resp_model.to_dict()
        assert zone_access_rule_resp_model_json2 == zone_access_rule_resp_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
