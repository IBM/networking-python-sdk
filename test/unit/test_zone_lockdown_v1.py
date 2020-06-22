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
from ibm_cloud_networking_services.zone_lockdown_v1 import *

crn = 'testString'
zone_identifier = 'testString'

service = ZoneLockdownV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn,
    zone_identifier=zone_identifier
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: ZoneLockdownRules
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_all_zone_lockown_rules
#-----------------------------------------------------------------------------
class TestListAllZoneLockownRules():

    #--------------------------------------------------------
    # list_all_zone_lockown_rules()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_zone_lockown_rules_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/firewall/lockdowns'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "372e67954025e0ba6aaa6d586b9e0b59", "paused": false, "description": "Restrict access to these endpoints to requests from a known IP address", "urls": ["api.mysite.com/some/endpoint*"], "configurations": [{"target": "ip", "value": "198.51.100.4 if target=ip, 2.2.2.0/24 if target=ip_range"}]}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        page = 38
        per_page = 38

        # Invoke method
        response = service.list_all_zone_lockown_rules(
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
    # test_list_all_zone_lockown_rules_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_zone_lockown_rules_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/firewall/lockdowns'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "372e67954025e0ba6aaa6d586b9e0b59", "paused": false, "description": "Restrict access to these endpoints to requests from a known IP address", "urls": ["api.mysite.com/some/endpoint*"], "configurations": [{"target": "ip", "value": "198.51.100.4 if target=ip, 2.2.2.0/24 if target=ip_range"}]}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_all_zone_lockown_rules()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for create_zone_lockdown_rule
#-----------------------------------------------------------------------------
class TestCreateZoneLockdownRule():

    #--------------------------------------------------------
    # create_zone_lockdown_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_create_zone_lockdown_rule_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/firewall/lockdowns'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "372e67954025e0ba6aaa6d586b9e0b59", "paused": false, "description": "Restrict access to these endpoints to requests from a known IP address", "urls": ["api.mysite.com/some/endpoint*"], "configurations": [{"target": "ip", "value": "198.51.100.4 if target=ip, 2.2.2.0/24 if target=ip_range"}]}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a LockdownInputConfigurationsItem model
        lockdown_input_configurations_item_model =  {
            'target': 'ip',
            'value': '198.51.100.4 if target=ip, 2.2.2.0/24 if target=ip_range'
        }

        # Set up parameter values
        urls = ['api.mysite.com/some/endpoint*']
        configurations = [lockdown_input_configurations_item_model]
        id = '372e67954025e0ba6aaa6d586b9e0b59'
        paused = False
        description = 'Restrict access to these endpoints to requests from a known IP address'

        # Invoke method
        response = service.create_zone_lockdown_rule(
            urls=urls,
            configurations=configurations,
            id=id,
            paused=paused,
            description=description,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['urls'] == urls
        assert req_body['configurations'] == configurations
        assert req_body['id'] == id
        assert req_body['paused'] == paused
        assert req_body['description'] == description


    #--------------------------------------------------------
    # test_create_zone_lockdown_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_zone_lockdown_rule_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/firewall/lockdowns'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "372e67954025e0ba6aaa6d586b9e0b59", "paused": false, "description": "Restrict access to these endpoints to requests from a known IP address", "urls": ["api.mysite.com/some/endpoint*"], "configurations": [{"target": "ip", "value": "198.51.100.4 if target=ip, 2.2.2.0/24 if target=ip_range"}]}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.create_zone_lockdown_rule()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for delete_zone_lockdown_rule
#-----------------------------------------------------------------------------
class TestDeleteZoneLockdownRule():

    #--------------------------------------------------------
    # delete_zone_lockdown_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_zone_lockdown_rule_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/firewall/lockdowns/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        lockdown_rule_identifier = 'testString'

        # Invoke method
        response = service.delete_zone_lockdown_rule(
            lockdown_rule_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_zone_lockdown_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_zone_lockdown_rule_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/firewall/lockdowns/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        lockdown_rule_identifier = 'testString'

        # Invoke method
        response = service.delete_zone_lockdown_rule(
            lockdown_rule_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_lockdown
#-----------------------------------------------------------------------------
class TestGetLockdown():

    #--------------------------------------------------------
    # get_lockdown()
    #--------------------------------------------------------
    @responses.activate
    def test_get_lockdown_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/firewall/lockdowns/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "372e67954025e0ba6aaa6d586b9e0b59", "paused": false, "description": "Restrict access to these endpoints to requests from a known IP address", "urls": ["api.mysite.com/some/endpoint*"], "configurations": [{"target": "ip", "value": "198.51.100.4 if target=ip, 2.2.2.0/24 if target=ip_range"}]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        lockdown_rule_identifier = 'testString'

        # Invoke method
        response = service.get_lockdown(
            lockdown_rule_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_lockdown_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_lockdown_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/firewall/lockdowns/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "372e67954025e0ba6aaa6d586b9e0b59", "paused": false, "description": "Restrict access to these endpoints to requests from a known IP address", "urls": ["api.mysite.com/some/endpoint*"], "configurations": [{"target": "ip", "value": "198.51.100.4 if target=ip, 2.2.2.0/24 if target=ip_range"}]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        lockdown_rule_identifier = 'testString'

        # Invoke method
        response = service.get_lockdown(
            lockdown_rule_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for update_lockdown_rule
#-----------------------------------------------------------------------------
class TestUpdateLockdownRule():

    #--------------------------------------------------------
    # update_lockdown_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_update_lockdown_rule_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/firewall/lockdowns/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "372e67954025e0ba6aaa6d586b9e0b59", "paused": false, "description": "Restrict access to these endpoints to requests from a known IP address", "urls": ["api.mysite.com/some/endpoint*"], "configurations": [{"target": "ip", "value": "198.51.100.4 if target=ip, 2.2.2.0/24 if target=ip_range"}]}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a LockdownInputConfigurationsItem model
        lockdown_input_configurations_item_model =  {
            'target': 'ip',
            'value': '198.51.100.4 if target=ip, 2.2.2.0/24 if target=ip_range'
        }

        # Set up parameter values
        lockdown_rule_identifier = 'testString'
        urls = ['api.mysite.com/some/endpoint*']
        configurations = [lockdown_input_configurations_item_model]
        id = '372e67954025e0ba6aaa6d586b9e0b59'
        paused = False
        description = 'Restrict access to these endpoints to requests from a known IP address'

        # Invoke method
        response = service.update_lockdown_rule(
            lockdown_rule_identifier,
            urls=urls,
            configurations=configurations,
            id=id,
            paused=paused,
            description=description,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['urls'] == urls
        assert req_body['configurations'] == configurations
        assert req_body['id'] == id
        assert req_body['paused'] == paused
        assert req_body['description'] == description


    #--------------------------------------------------------
    # test_update_lockdown_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_lockdown_rule_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/firewall/lockdowns/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "372e67954025e0ba6aaa6d586b9e0b59", "paused": false, "description": "Restrict access to these endpoints to requests from a known IP address", "urls": ["api.mysite.com/some/endpoint*"], "configurations": [{"target": "ip", "value": "198.51.100.4 if target=ip, 2.2.2.0/24 if target=ip_range"}]}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        lockdown_rule_identifier = 'testString'

        # Invoke method
        response = service.update_lockdown_rule(
            lockdown_rule_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: ZoneLockdownRules
##############################################################################

