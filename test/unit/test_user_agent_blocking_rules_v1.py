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

    #--------------------------------------------------------
    # list_all_zone_user_agent_rules()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_zone_user_agent_rules_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/firewall/ua_rules'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "92f17202ed8bd63d69a66b86a49a8f6b", "paused": true, "description": "Prevent access from abusive clients identified by this UserAgent to mitigate DDoS attack", "mode": "block", "configuration": {"target": "ua", "value": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4"}}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        page = 38
        per_page = 38

        # Invoke method
        response = service.list_all_zone_user_agent_rules(
            page=page,
            per_page=per_page
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
        url = base_url + '/v1/testString/zones/testString/firewall/ua_rules'
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


#-----------------------------------------------------------------------------
# Test Class for create_zone_user_agent_rule
#-----------------------------------------------------------------------------
class TestCreateZoneUserAgentRule():

    #--------------------------------------------------------
    # create_zone_user_agent_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_create_zone_user_agent_rule_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/firewall/ua_rules'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "paused": true, "description": "Prevent access from abusive clients identified by this UserAgent to mitigate DDoS attack", "mode": "block", "configuration": {"target": "ua", "value": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a UseragentRuleInputConfiguration model
        useragent_rule_input_configuration_model =  {
            'target': 'ua',
            'value': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4'
        }

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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['mode'] == mode
        assert req_body['configuration'] == configuration
        assert req_body['paused'] == paused
        assert req_body['description'] == description


    #--------------------------------------------------------
    # test_create_zone_user_agent_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_zone_user_agent_rule_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/firewall/ua_rules'
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


#-----------------------------------------------------------------------------
# Test Class for delete_zone_user_agent_rule
#-----------------------------------------------------------------------------
class TestDeleteZoneUserAgentRule():

    #--------------------------------------------------------
    # delete_zone_user_agent_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_zone_user_agent_rule_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/firewall/ua_rules/testString'
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
            useragent_rule_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_zone_user_agent_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_zone_user_agent_rule_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/firewall/ua_rules/testString'
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
            useragent_rule_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_user_agent_rule
#-----------------------------------------------------------------------------
class TestGetUserAgentRule():

    #--------------------------------------------------------
    # get_user_agent_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_get_user_agent_rule_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/firewall/ua_rules/testString'
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
            useragent_rule_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_user_agent_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_user_agent_rule_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/firewall/ua_rules/testString'
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
            useragent_rule_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for update_user_agent_rule
#-----------------------------------------------------------------------------
class TestUpdateUserAgentRule():

    #--------------------------------------------------------
    # update_user_agent_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_update_user_agent_rule_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/firewall/ua_rules/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "paused": true, "description": "Prevent access from abusive clients identified by this UserAgent to mitigate DDoS attack", "mode": "block", "configuration": {"target": "ua", "value": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4"}}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a UseragentRuleInputConfiguration model
        useragent_rule_input_configuration_model =  {
            'target': 'ua',
            'value': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4'
        }

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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['mode'] == mode
        assert req_body['configuration'] == configuration
        assert req_body['paused'] == paused
        assert req_body['description'] == description


    #--------------------------------------------------------
    # test_update_user_agent_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_user_agent_rule_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/firewall/ua_rules/testString'
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
            useragent_rule_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UserAgentBlockingRules
##############################################################################

