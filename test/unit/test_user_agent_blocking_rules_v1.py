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
from ibm_cloud_networking_services.user_agent_blocking_rules_v1 import *

crn = 'testString'
zone_identifier = 'testString'

service = UserAgentBlockingRulesV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn,
    zone_identifier=zone_identifier
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: UserAgentBlockingRules
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_all_zone_user_agent_rules
#-----------------------------------------------------------------------------
class TestListAllZoneUserAgentRules():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # list_all_zone_user_agent_rules()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_zone_user_agent_rules_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/ua_rules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "92f17202ed8bd63d69a66b86a49a8f6b", "paused": true, "description": "Prevent access from abusive clients identified by this UserAgent to mitigate DDoS attack", "mode": "block", "configuration": {"target": "ua", "value": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4"}}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        page = 38
        per_page = 5

        # Invoke method
        response = service.list_all_zone_user_agent_rules(
            page=page,
            per_page=per_page,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'page={}'.format(page) in query_string
        assert 'per_page={}'.format(per_page) in query_string


    #--------------------------------------------------------
    # test_list_all_zone_user_agent_rules_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_zone_user_agent_rules_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/ua_rules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "92f17202ed8bd63d69a66b86a49a8f6b", "paused": true, "description": "Prevent access from abusive clients identified by this UserAgent to mitigate DDoS attack", "mode": "block", "configuration": {"target": "ua", "value": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4"}}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_all_zone_user_agent_rules()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_all_zone_user_agent_rules_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_zone_user_agent_rules_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/ua_rules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "92f17202ed8bd63d69a66b86a49a8f6b", "paused": true, "description": "Prevent access from abusive clients identified by this UserAgent to mitigate DDoS attack", "mode": "block", "configuration": {"target": "ua", "value": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4"}}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
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
                service.list_all_zone_user_agent_rules(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for create_zone_user_agent_rule
#-----------------------------------------------------------------------------
class TestCreateZoneUserAgentRule():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # create_zone_user_agent_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_create_zone_user_agent_rule_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/ua_rules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "paused": true, "description": "Prevent access from abusive clients identified by this UserAgent to mitigate DDoS attack", "mode": "block", "configuration": {"target": "ua", "value": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a UseragentRuleInputConfiguration model
        useragent_rule_input_configuration_model = {}
        useragent_rule_input_configuration_model['target'] = 'ua'
        useragent_rule_input_configuration_model['value'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4'

        # Set up parameter values
        mode = 'block'
        configuration = useragent_rule_input_configuration_model
        paused = True
        description = 'Prevent access from abusive clients identified by this UserAgent to mitigate DDoS attack'

        # Invoke method
        response = service.create_zone_user_agent_rule(
            mode=mode,
            configuration=configuration,
            paused=paused,
            description=description,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['mode'] == 'block'
        assert req_body['configuration'] == useragent_rule_input_configuration_model
        assert req_body['paused'] == True
        assert req_body['description'] == 'Prevent access from abusive clients identified by this UserAgent to mitigate DDoS attack'


    #--------------------------------------------------------
    # test_create_zone_user_agent_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_zone_user_agent_rule_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/ua_rules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "paused": true, "description": "Prevent access from abusive clients identified by this UserAgent to mitigate DDoS attack", "mode": "block", "configuration": {"target": "ua", "value": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.create_zone_user_agent_rule()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_create_zone_user_agent_rule_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_zone_user_agent_rule_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/ua_rules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "paused": true, "description": "Prevent access from abusive clients identified by this UserAgent to mitigate DDoS attack", "mode": "block", "configuration": {"target": "ua", "value": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4"}}}'
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
                service.create_zone_user_agent_rule(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_zone_user_agent_rule
#-----------------------------------------------------------------------------
class TestDeleteZoneUserAgentRule():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # delete_zone_user_agent_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_zone_user_agent_rule_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/ua_rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        useragent_rule_identifier = 'testString'

        # Invoke method
        response = service.delete_zone_user_agent_rule(
            useragent_rule_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_zone_user_agent_rule_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_zone_user_agent_rule_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/ua_rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        useragent_rule_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "useragent_rule_identifier": useragent_rule_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_zone_user_agent_rule(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_user_agent_rule
#-----------------------------------------------------------------------------
class TestGetUserAgentRule():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_user_agent_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_get_user_agent_rule_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/ua_rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "paused": true, "description": "Prevent access from abusive clients identified by this UserAgent to mitigate DDoS attack", "mode": "block", "configuration": {"target": "ua", "value": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4"}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        useragent_rule_identifier = 'testString'

        # Invoke method
        response = service.get_user_agent_rule(
            useragent_rule_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_user_agent_rule_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_user_agent_rule_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/ua_rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "paused": true, "description": "Prevent access from abusive clients identified by this UserAgent to mitigate DDoS attack", "mode": "block", "configuration": {"target": "ua", "value": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4"}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        useragent_rule_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "useragent_rule_identifier": useragent_rule_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_user_agent_rule(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_user_agent_rule
#-----------------------------------------------------------------------------
class TestUpdateUserAgentRule():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_user_agent_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_update_user_agent_rule_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/ua_rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "paused": true, "description": "Prevent access from abusive clients identified by this UserAgent to mitigate DDoS attack", "mode": "block", "configuration": {"target": "ua", "value": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4"}}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a UseragentRuleInputConfiguration model
        useragent_rule_input_configuration_model = {}
        useragent_rule_input_configuration_model['target'] = 'ua'
        useragent_rule_input_configuration_model['value'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4'

        # Set up parameter values
        useragent_rule_identifier = 'testString'
        mode = 'block'
        configuration = useragent_rule_input_configuration_model
        paused = True
        description = 'Prevent access from abusive clients identified by this UserAgent to mitigate DDoS attack'

        # Invoke method
        response = service.update_user_agent_rule(
            useragent_rule_identifier,
            mode=mode,
            configuration=configuration,
            paused=paused,
            description=description,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['mode'] == 'block'
        assert req_body['configuration'] == useragent_rule_input_configuration_model
        assert req_body['paused'] == True
        assert req_body['description'] == 'Prevent access from abusive clients identified by this UserAgent to mitigate DDoS attack'


    #--------------------------------------------------------
    # test_update_user_agent_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_user_agent_rule_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/ua_rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "paused": true, "description": "Prevent access from abusive clients identified by this UserAgent to mitigate DDoS attack", "mode": "block", "configuration": {"target": "ua", "value": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4"}}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        useragent_rule_identifier = 'testString'

        # Invoke method
        response = service.update_user_agent_rule(
            useragent_rule_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_user_agent_rule_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_user_agent_rule_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/ua_rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "paused": true, "description": "Prevent access from abusive clients identified by this UserAgent to mitigate DDoS attack", "mode": "block", "configuration": {"target": "ua", "value": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4"}}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        useragent_rule_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "useragent_rule_identifier": useragent_rule_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_user_agent_rule(**req_copy)



# endregion
##############################################################################
# End of Service: UserAgentBlockingRules
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for DeleteUseragentRuleRespResult
#-----------------------------------------------------------------------------
class TestDeleteUseragentRuleRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for DeleteUseragentRuleRespResult
    #--------------------------------------------------------
    def test_delete_useragent_rule_resp_result_serialization(self):

        # Construct a json representation of a DeleteUseragentRuleRespResult model
        delete_useragent_rule_resp_result_model_json = {}
        delete_useragent_rule_resp_result_model_json['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'

        # Construct a model instance of DeleteUseragentRuleRespResult by calling from_dict on the json representation
        delete_useragent_rule_resp_result_model = DeleteUseragentRuleRespResult.from_dict(delete_useragent_rule_resp_result_model_json)
        assert delete_useragent_rule_resp_result_model != False

        # Construct a model instance of DeleteUseragentRuleRespResult by calling from_dict on the json representation
        delete_useragent_rule_resp_result_model_dict = DeleteUseragentRuleRespResult.from_dict(delete_useragent_rule_resp_result_model_json).__dict__
        delete_useragent_rule_resp_result_model2 = DeleteUseragentRuleRespResult(**delete_useragent_rule_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert delete_useragent_rule_resp_result_model == delete_useragent_rule_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        delete_useragent_rule_resp_result_model_json2 = delete_useragent_rule_resp_result_model.to_dict()
        assert delete_useragent_rule_resp_result_model_json2 == delete_useragent_rule_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for ListUseragentRulesRespResultInfo
#-----------------------------------------------------------------------------
class TestListUseragentRulesRespResultInfo():

    #--------------------------------------------------------
    # Test serialization/deserialization for ListUseragentRulesRespResultInfo
    #--------------------------------------------------------
    def test_list_useragent_rules_resp_result_info_serialization(self):

        # Construct a json representation of a ListUseragentRulesRespResultInfo model
        list_useragent_rules_resp_result_info_model_json = {}
        list_useragent_rules_resp_result_info_model_json['page'] = 1
        list_useragent_rules_resp_result_info_model_json['per_page'] = 2
        list_useragent_rules_resp_result_info_model_json['count'] = 1
        list_useragent_rules_resp_result_info_model_json['total_count'] = 200

        # Construct a model instance of ListUseragentRulesRespResultInfo by calling from_dict on the json representation
        list_useragent_rules_resp_result_info_model = ListUseragentRulesRespResultInfo.from_dict(list_useragent_rules_resp_result_info_model_json)
        assert list_useragent_rules_resp_result_info_model != False

        # Construct a model instance of ListUseragentRulesRespResultInfo by calling from_dict on the json representation
        list_useragent_rules_resp_result_info_model_dict = ListUseragentRulesRespResultInfo.from_dict(list_useragent_rules_resp_result_info_model_json).__dict__
        list_useragent_rules_resp_result_info_model2 = ListUseragentRulesRespResultInfo(**list_useragent_rules_resp_result_info_model_dict)

        # Verify the model instances are equivalent
        assert list_useragent_rules_resp_result_info_model == list_useragent_rules_resp_result_info_model2

        # Convert model instance back to dict and verify no loss of data
        list_useragent_rules_resp_result_info_model_json2 = list_useragent_rules_resp_result_info_model.to_dict()
        assert list_useragent_rules_resp_result_info_model_json2 == list_useragent_rules_resp_result_info_model_json

#-----------------------------------------------------------------------------
# Test Class for UseragentRuleInputConfiguration
#-----------------------------------------------------------------------------
class TestUseragentRuleInputConfiguration():

    #--------------------------------------------------------
    # Test serialization/deserialization for UseragentRuleInputConfiguration
    #--------------------------------------------------------
    def test_useragent_rule_input_configuration_serialization(self):

        # Construct a json representation of a UseragentRuleInputConfiguration model
        useragent_rule_input_configuration_model_json = {}
        useragent_rule_input_configuration_model_json['target'] = 'ua'
        useragent_rule_input_configuration_model_json['value'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4'

        # Construct a model instance of UseragentRuleInputConfiguration by calling from_dict on the json representation
        useragent_rule_input_configuration_model = UseragentRuleInputConfiguration.from_dict(useragent_rule_input_configuration_model_json)
        assert useragent_rule_input_configuration_model != False

        # Construct a model instance of UseragentRuleInputConfiguration by calling from_dict on the json representation
        useragent_rule_input_configuration_model_dict = UseragentRuleInputConfiguration.from_dict(useragent_rule_input_configuration_model_json).__dict__
        useragent_rule_input_configuration_model2 = UseragentRuleInputConfiguration(**useragent_rule_input_configuration_model_dict)

        # Verify the model instances are equivalent
        assert useragent_rule_input_configuration_model == useragent_rule_input_configuration_model2

        # Convert model instance back to dict and verify no loss of data
        useragent_rule_input_configuration_model_json2 = useragent_rule_input_configuration_model.to_dict()
        assert useragent_rule_input_configuration_model_json2 == useragent_rule_input_configuration_model_json

#-----------------------------------------------------------------------------
# Test Class for UseragentRuleObjectConfiguration
#-----------------------------------------------------------------------------
class TestUseragentRuleObjectConfiguration():

    #--------------------------------------------------------
    # Test serialization/deserialization for UseragentRuleObjectConfiguration
    #--------------------------------------------------------
    def test_useragent_rule_object_configuration_serialization(self):

        # Construct a json representation of a UseragentRuleObjectConfiguration model
        useragent_rule_object_configuration_model_json = {}
        useragent_rule_object_configuration_model_json['target'] = 'ua'
        useragent_rule_object_configuration_model_json['value'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4'

        # Construct a model instance of UseragentRuleObjectConfiguration by calling from_dict on the json representation
        useragent_rule_object_configuration_model = UseragentRuleObjectConfiguration.from_dict(useragent_rule_object_configuration_model_json)
        assert useragent_rule_object_configuration_model != False

        # Construct a model instance of UseragentRuleObjectConfiguration by calling from_dict on the json representation
        useragent_rule_object_configuration_model_dict = UseragentRuleObjectConfiguration.from_dict(useragent_rule_object_configuration_model_json).__dict__
        useragent_rule_object_configuration_model2 = UseragentRuleObjectConfiguration(**useragent_rule_object_configuration_model_dict)

        # Verify the model instances are equivalent
        assert useragent_rule_object_configuration_model == useragent_rule_object_configuration_model2

        # Convert model instance back to dict and verify no loss of data
        useragent_rule_object_configuration_model_json2 = useragent_rule_object_configuration_model.to_dict()
        assert useragent_rule_object_configuration_model_json2 == useragent_rule_object_configuration_model_json

#-----------------------------------------------------------------------------
# Test Class for DeleteUseragentRuleResp
#-----------------------------------------------------------------------------
class TestDeleteUseragentRuleResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for DeleteUseragentRuleResp
    #--------------------------------------------------------
    def test_delete_useragent_rule_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        delete_useragent_rule_resp_result_model = {} # DeleteUseragentRuleRespResult
        delete_useragent_rule_resp_result_model['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'

        # Construct a json representation of a DeleteUseragentRuleResp model
        delete_useragent_rule_resp_model_json = {}
        delete_useragent_rule_resp_model_json['success'] = True
        delete_useragent_rule_resp_model_json['errors'] = [['testString']]
        delete_useragent_rule_resp_model_json['messages'] = [['testString']]
        delete_useragent_rule_resp_model_json['result'] = delete_useragent_rule_resp_result_model

        # Construct a model instance of DeleteUseragentRuleResp by calling from_dict on the json representation
        delete_useragent_rule_resp_model = DeleteUseragentRuleResp.from_dict(delete_useragent_rule_resp_model_json)
        assert delete_useragent_rule_resp_model != False

        # Construct a model instance of DeleteUseragentRuleResp by calling from_dict on the json representation
        delete_useragent_rule_resp_model_dict = DeleteUseragentRuleResp.from_dict(delete_useragent_rule_resp_model_json).__dict__
        delete_useragent_rule_resp_model2 = DeleteUseragentRuleResp(**delete_useragent_rule_resp_model_dict)

        # Verify the model instances are equivalent
        assert delete_useragent_rule_resp_model == delete_useragent_rule_resp_model2

        # Convert model instance back to dict and verify no loss of data
        delete_useragent_rule_resp_model_json2 = delete_useragent_rule_resp_model.to_dict()
        assert delete_useragent_rule_resp_model_json2 == delete_useragent_rule_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for ListUseragentRulesResp
#-----------------------------------------------------------------------------
class TestListUseragentRulesResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for ListUseragentRulesResp
    #--------------------------------------------------------
    def test_list_useragent_rules_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        useragent_rule_object_configuration_model = {} # UseragentRuleObjectConfiguration
        useragent_rule_object_configuration_model['target'] = 'ua'
        useragent_rule_object_configuration_model['value'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4'

        list_useragent_rules_resp_result_info_model = {} # ListUseragentRulesRespResultInfo
        list_useragent_rules_resp_result_info_model['page'] = 1
        list_useragent_rules_resp_result_info_model['per_page'] = 2
        list_useragent_rules_resp_result_info_model['count'] = 1
        list_useragent_rules_resp_result_info_model['total_count'] = 200

        useragent_rule_object_model = {} # UseragentRuleObject
        useragent_rule_object_model['id'] = '92f17202ed8bd63d69a66b86a49a8f6b'
        useragent_rule_object_model['paused'] = True
        useragent_rule_object_model['description'] = 'Prevent access from abusive clients identified by this UserAgent to mitigate DDoS attack'
        useragent_rule_object_model['mode'] = 'block'
        useragent_rule_object_model['configuration'] = useragent_rule_object_configuration_model

        # Construct a json representation of a ListUseragentRulesResp model
        list_useragent_rules_resp_model_json = {}
        list_useragent_rules_resp_model_json['success'] = True
        list_useragent_rules_resp_model_json['errors'] = [['testString']]
        list_useragent_rules_resp_model_json['messages'] = [['testString']]
        list_useragent_rules_resp_model_json['result'] = [useragent_rule_object_model]
        list_useragent_rules_resp_model_json['result_info'] = list_useragent_rules_resp_result_info_model

        # Construct a model instance of ListUseragentRulesResp by calling from_dict on the json representation
        list_useragent_rules_resp_model = ListUseragentRulesResp.from_dict(list_useragent_rules_resp_model_json)
        assert list_useragent_rules_resp_model != False

        # Construct a model instance of ListUseragentRulesResp by calling from_dict on the json representation
        list_useragent_rules_resp_model_dict = ListUseragentRulesResp.from_dict(list_useragent_rules_resp_model_json).__dict__
        list_useragent_rules_resp_model2 = ListUseragentRulesResp(**list_useragent_rules_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_useragent_rules_resp_model == list_useragent_rules_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_useragent_rules_resp_model_json2 = list_useragent_rules_resp_model.to_dict()
        assert list_useragent_rules_resp_model_json2 == list_useragent_rules_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for UseragentRuleObject
#-----------------------------------------------------------------------------
class TestUseragentRuleObject():

    #--------------------------------------------------------
    # Test serialization/deserialization for UseragentRuleObject
    #--------------------------------------------------------
    def test_useragent_rule_object_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        useragent_rule_object_configuration_model = {} # UseragentRuleObjectConfiguration
        useragent_rule_object_configuration_model['target'] = 'ua'
        useragent_rule_object_configuration_model['value'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4'

        # Construct a json representation of a UseragentRuleObject model
        useragent_rule_object_model_json = {}
        useragent_rule_object_model_json['id'] = '92f17202ed8bd63d69a66b86a49a8f6b'
        useragent_rule_object_model_json['paused'] = True
        useragent_rule_object_model_json['description'] = 'Prevent access from abusive clients identified by this UserAgent to mitigate DDoS attack'
        useragent_rule_object_model_json['mode'] = 'block'
        useragent_rule_object_model_json['configuration'] = useragent_rule_object_configuration_model

        # Construct a model instance of UseragentRuleObject by calling from_dict on the json representation
        useragent_rule_object_model = UseragentRuleObject.from_dict(useragent_rule_object_model_json)
        assert useragent_rule_object_model != False

        # Construct a model instance of UseragentRuleObject by calling from_dict on the json representation
        useragent_rule_object_model_dict = UseragentRuleObject.from_dict(useragent_rule_object_model_json).__dict__
        useragent_rule_object_model2 = UseragentRuleObject(**useragent_rule_object_model_dict)

        # Verify the model instances are equivalent
        assert useragent_rule_object_model == useragent_rule_object_model2

        # Convert model instance back to dict and verify no loss of data
        useragent_rule_object_model_json2 = useragent_rule_object_model.to_dict()
        assert useragent_rule_object_model_json2 == useragent_rule_object_model_json

#-----------------------------------------------------------------------------
# Test Class for UseragentRuleResp
#-----------------------------------------------------------------------------
class TestUseragentRuleResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for UseragentRuleResp
    #--------------------------------------------------------
    def test_useragent_rule_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        useragent_rule_object_configuration_model = {} # UseragentRuleObjectConfiguration
        useragent_rule_object_configuration_model['target'] = 'ua'
        useragent_rule_object_configuration_model['value'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4'

        useragent_rule_object_model = {} # UseragentRuleObject
        useragent_rule_object_model['id'] = '92f17202ed8bd63d69a66b86a49a8f6b'
        useragent_rule_object_model['paused'] = True
        useragent_rule_object_model['description'] = 'Prevent access from abusive clients identified by this UserAgent to mitigate DDoS attack'
        useragent_rule_object_model['mode'] = 'block'
        useragent_rule_object_model['configuration'] = useragent_rule_object_configuration_model

        # Construct a json representation of a UseragentRuleResp model
        useragent_rule_resp_model_json = {}
        useragent_rule_resp_model_json['success'] = True
        useragent_rule_resp_model_json['errors'] = [['testString']]
        useragent_rule_resp_model_json['messages'] = [['testString']]
        useragent_rule_resp_model_json['result'] = useragent_rule_object_model

        # Construct a model instance of UseragentRuleResp by calling from_dict on the json representation
        useragent_rule_resp_model = UseragentRuleResp.from_dict(useragent_rule_resp_model_json)
        assert useragent_rule_resp_model != False

        # Construct a model instance of UseragentRuleResp by calling from_dict on the json representation
        useragent_rule_resp_model_dict = UseragentRuleResp.from_dict(useragent_rule_resp_model_json).__dict__
        useragent_rule_resp_model2 = UseragentRuleResp(**useragent_rule_resp_model_dict)

        # Verify the model instances are equivalent
        assert useragent_rule_resp_model == useragent_rule_resp_model2

        # Convert model instance back to dict and verify no loss of data
        useragent_rule_resp_model_json2 = useragent_rule_resp_model.to_dict()
        assert useragent_rule_resp_model_json2 == useragent_rule_resp_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
