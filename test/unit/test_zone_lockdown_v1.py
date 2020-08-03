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

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # list_all_zone_lockown_rules()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_zone_lockown_rules_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/lockdowns')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "372e67954025e0ba6aaa6d586b9e0b59", "paused": false, "description": "Restrict access to these endpoints to requests from a known IP address", "urls": ["api.mysite.com/some/endpoint*"], "configurations": [{"target": "ip", "value": "198.51.100.4 if target=ip, 2.2.2.0/24 if target=ip_range"}]}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        page = 38
        per_page = 5

        # Invoke method
        response = service.list_all_zone_lockown_rules(
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
    # test_list_all_zone_lockown_rules_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_zone_lockown_rules_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/lockdowns')
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


    #--------------------------------------------------------
    # test_list_all_zone_lockown_rules_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_zone_lockown_rules_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/lockdowns')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "372e67954025e0ba6aaa6d586b9e0b59", "paused": false, "description": "Restrict access to these endpoints to requests from a known IP address", "urls": ["api.mysite.com/some/endpoint*"], "configurations": [{"target": "ip", "value": "198.51.100.4 if target=ip, 2.2.2.0/24 if target=ip_range"}]}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
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
                service.list_all_zone_lockown_rules(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for create_zone_lockdown_rule
#-----------------------------------------------------------------------------
class TestCreateZoneLockdownRule():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # create_zone_lockdown_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_create_zone_lockdown_rule_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/lockdowns')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "372e67954025e0ba6aaa6d586b9e0b59", "paused": false, "description": "Restrict access to these endpoints to requests from a known IP address", "urls": ["api.mysite.com/some/endpoint*"], "configurations": [{"target": "ip", "value": "198.51.100.4 if target=ip, 2.2.2.0/24 if target=ip_range"}]}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a LockdownInputConfigurationsItem model
        lockdown_input_configurations_item_model = {}
        lockdown_input_configurations_item_model['target'] = 'ip'
        lockdown_input_configurations_item_model['value'] = '198.51.100.4 if target=ip, 2.2.2.0/24 if target=ip_range'

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
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['urls'] == ['api.mysite.com/some/endpoint*']
        assert req_body['configurations'] == [lockdown_input_configurations_item_model]
        assert req_body['id'] == '372e67954025e0ba6aaa6d586b9e0b59'
        assert req_body['paused'] == False
        assert req_body['description'] == 'Restrict access to these endpoints to requests from a known IP address'


    #--------------------------------------------------------
    # test_create_zone_lockdown_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_zone_lockdown_rule_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/lockdowns')
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


    #--------------------------------------------------------
    # test_create_zone_lockdown_rule_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_zone_lockdown_rule_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/lockdowns')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "372e67954025e0ba6aaa6d586b9e0b59", "paused": false, "description": "Restrict access to these endpoints to requests from a known IP address", "urls": ["api.mysite.com/some/endpoint*"], "configurations": [{"target": "ip", "value": "198.51.100.4 if target=ip, 2.2.2.0/24 if target=ip_range"}]}}'
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
                service.create_zone_lockdown_rule(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_zone_lockdown_rule
#-----------------------------------------------------------------------------
class TestDeleteZoneLockdownRule():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # delete_zone_lockdown_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_zone_lockdown_rule_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/lockdowns/testString')
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
            lockdown_rule_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_zone_lockdown_rule_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_zone_lockdown_rule_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/lockdowns/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        lockdown_rule_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "lockdown_rule_identifier": lockdown_rule_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_zone_lockdown_rule(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_lockdown
#-----------------------------------------------------------------------------
class TestGetLockdown():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_lockdown()
    #--------------------------------------------------------
    @responses.activate
    def test_get_lockdown_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/lockdowns/testString')
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
            lockdown_rule_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_lockdown_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_lockdown_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/lockdowns/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "372e67954025e0ba6aaa6d586b9e0b59", "paused": false, "description": "Restrict access to these endpoints to requests from a known IP address", "urls": ["api.mysite.com/some/endpoint*"], "configurations": [{"target": "ip", "value": "198.51.100.4 if target=ip, 2.2.2.0/24 if target=ip_range"}]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        lockdown_rule_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "lockdown_rule_identifier": lockdown_rule_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_lockdown(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_lockdown_rule
#-----------------------------------------------------------------------------
class TestUpdateLockdownRule():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_lockdown_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_update_lockdown_rule_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/lockdowns/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "372e67954025e0ba6aaa6d586b9e0b59", "paused": false, "description": "Restrict access to these endpoints to requests from a known IP address", "urls": ["api.mysite.com/some/endpoint*"], "configurations": [{"target": "ip", "value": "198.51.100.4 if target=ip, 2.2.2.0/24 if target=ip_range"}]}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a LockdownInputConfigurationsItem model
        lockdown_input_configurations_item_model = {}
        lockdown_input_configurations_item_model['target'] = 'ip'
        lockdown_input_configurations_item_model['value'] = '198.51.100.4 if target=ip, 2.2.2.0/24 if target=ip_range'

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
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['urls'] == ['api.mysite.com/some/endpoint*']
        assert req_body['configurations'] == [lockdown_input_configurations_item_model]
        assert req_body['id'] == '372e67954025e0ba6aaa6d586b9e0b59'
        assert req_body['paused'] == False
        assert req_body['description'] == 'Restrict access to these endpoints to requests from a known IP address'


    #--------------------------------------------------------
    # test_update_lockdown_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_lockdown_rule_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/lockdowns/testString')
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
            lockdown_rule_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_lockdown_rule_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_lockdown_rule_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/lockdowns/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "372e67954025e0ba6aaa6d586b9e0b59", "paused": false, "description": "Restrict access to these endpoints to requests from a known IP address", "urls": ["api.mysite.com/some/endpoint*"], "configurations": [{"target": "ip", "value": "198.51.100.4 if target=ip, 2.2.2.0/24 if target=ip_range"}]}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        lockdown_rule_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "lockdown_rule_identifier": lockdown_rule_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_lockdown_rule(**req_copy)



# endregion
##############################################################################
# End of Service: ZoneLockdownRules
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for DeleteLockdownRespResult
#-----------------------------------------------------------------------------
class TestDeleteLockdownRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for DeleteLockdownRespResult
    #--------------------------------------------------------
    def test_delete_lockdown_resp_result_serialization(self):

        # Construct a json representation of a DeleteLockdownRespResult model
        delete_lockdown_resp_result_model_json = {}
        delete_lockdown_resp_result_model_json['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'

        # Construct a model instance of DeleteLockdownRespResult by calling from_dict on the json representation
        delete_lockdown_resp_result_model = DeleteLockdownRespResult.from_dict(delete_lockdown_resp_result_model_json)
        assert delete_lockdown_resp_result_model != False

        # Construct a model instance of DeleteLockdownRespResult by calling from_dict on the json representation
        delete_lockdown_resp_result_model_dict = DeleteLockdownRespResult.from_dict(delete_lockdown_resp_result_model_json).__dict__
        delete_lockdown_resp_result_model2 = DeleteLockdownRespResult(**delete_lockdown_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert delete_lockdown_resp_result_model == delete_lockdown_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        delete_lockdown_resp_result_model_json2 = delete_lockdown_resp_result_model.to_dict()
        assert delete_lockdown_resp_result_model_json2 == delete_lockdown_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for ListLockdownRespResultInfo
#-----------------------------------------------------------------------------
class TestListLockdownRespResultInfo():

    #--------------------------------------------------------
    # Test serialization/deserialization for ListLockdownRespResultInfo
    #--------------------------------------------------------
    def test_list_lockdown_resp_result_info_serialization(self):

        # Construct a json representation of a ListLockdownRespResultInfo model
        list_lockdown_resp_result_info_model_json = {}
        list_lockdown_resp_result_info_model_json['page'] = 1
        list_lockdown_resp_result_info_model_json['per_page'] = 2
        list_lockdown_resp_result_info_model_json['count'] = 1
        list_lockdown_resp_result_info_model_json['total_count'] = 200

        # Construct a model instance of ListLockdownRespResultInfo by calling from_dict on the json representation
        list_lockdown_resp_result_info_model = ListLockdownRespResultInfo.from_dict(list_lockdown_resp_result_info_model_json)
        assert list_lockdown_resp_result_info_model != False

        # Construct a model instance of ListLockdownRespResultInfo by calling from_dict on the json representation
        list_lockdown_resp_result_info_model_dict = ListLockdownRespResultInfo.from_dict(list_lockdown_resp_result_info_model_json).__dict__
        list_lockdown_resp_result_info_model2 = ListLockdownRespResultInfo(**list_lockdown_resp_result_info_model_dict)

        # Verify the model instances are equivalent
        assert list_lockdown_resp_result_info_model == list_lockdown_resp_result_info_model2

        # Convert model instance back to dict and verify no loss of data
        list_lockdown_resp_result_info_model_json2 = list_lockdown_resp_result_info_model.to_dict()
        assert list_lockdown_resp_result_info_model_json2 == list_lockdown_resp_result_info_model_json

#-----------------------------------------------------------------------------
# Test Class for LockdownInputConfigurationsItem
#-----------------------------------------------------------------------------
class TestLockdownInputConfigurationsItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for LockdownInputConfigurationsItem
    #--------------------------------------------------------
    def test_lockdown_input_configurations_item_serialization(self):

        # Construct a json representation of a LockdownInputConfigurationsItem model
        lockdown_input_configurations_item_model_json = {}
        lockdown_input_configurations_item_model_json['target'] = 'ip'
        lockdown_input_configurations_item_model_json['value'] = '198.51.100.4 if target=ip, 2.2.2.0/24 if target=ip_range'

        # Construct a model instance of LockdownInputConfigurationsItem by calling from_dict on the json representation
        lockdown_input_configurations_item_model = LockdownInputConfigurationsItem.from_dict(lockdown_input_configurations_item_model_json)
        assert lockdown_input_configurations_item_model != False

        # Construct a model instance of LockdownInputConfigurationsItem by calling from_dict on the json representation
        lockdown_input_configurations_item_model_dict = LockdownInputConfigurationsItem.from_dict(lockdown_input_configurations_item_model_json).__dict__
        lockdown_input_configurations_item_model2 = LockdownInputConfigurationsItem(**lockdown_input_configurations_item_model_dict)

        # Verify the model instances are equivalent
        assert lockdown_input_configurations_item_model == lockdown_input_configurations_item_model2

        # Convert model instance back to dict and verify no loss of data
        lockdown_input_configurations_item_model_json2 = lockdown_input_configurations_item_model.to_dict()
        assert lockdown_input_configurations_item_model_json2 == lockdown_input_configurations_item_model_json

#-----------------------------------------------------------------------------
# Test Class for LockdownObjectConfigurationsItem
#-----------------------------------------------------------------------------
class TestLockdownObjectConfigurationsItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for LockdownObjectConfigurationsItem
    #--------------------------------------------------------
    def test_lockdown_object_configurations_item_serialization(self):

        # Construct a json representation of a LockdownObjectConfigurationsItem model
        lockdown_object_configurations_item_model_json = {}
        lockdown_object_configurations_item_model_json['target'] = 'ip'
        lockdown_object_configurations_item_model_json['value'] = '198.51.100.4 if target=ip, 2.2.2.0/24 if target=ip_range'

        # Construct a model instance of LockdownObjectConfigurationsItem by calling from_dict on the json representation
        lockdown_object_configurations_item_model = LockdownObjectConfigurationsItem.from_dict(lockdown_object_configurations_item_model_json)
        assert lockdown_object_configurations_item_model != False

        # Construct a model instance of LockdownObjectConfigurationsItem by calling from_dict on the json representation
        lockdown_object_configurations_item_model_dict = LockdownObjectConfigurationsItem.from_dict(lockdown_object_configurations_item_model_json).__dict__
        lockdown_object_configurations_item_model2 = LockdownObjectConfigurationsItem(**lockdown_object_configurations_item_model_dict)

        # Verify the model instances are equivalent
        assert lockdown_object_configurations_item_model == lockdown_object_configurations_item_model2

        # Convert model instance back to dict and verify no loss of data
        lockdown_object_configurations_item_model_json2 = lockdown_object_configurations_item_model.to_dict()
        assert lockdown_object_configurations_item_model_json2 == lockdown_object_configurations_item_model_json

#-----------------------------------------------------------------------------
# Test Class for DeleteLockdownResp
#-----------------------------------------------------------------------------
class TestDeleteLockdownResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for DeleteLockdownResp
    #--------------------------------------------------------
    def test_delete_lockdown_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        delete_lockdown_resp_result_model = {} # DeleteLockdownRespResult
        delete_lockdown_resp_result_model['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'

        # Construct a json representation of a DeleteLockdownResp model
        delete_lockdown_resp_model_json = {}
        delete_lockdown_resp_model_json['success'] = True
        delete_lockdown_resp_model_json['errors'] = [['testString']]
        delete_lockdown_resp_model_json['messages'] = [['testString']]
        delete_lockdown_resp_model_json['result'] = delete_lockdown_resp_result_model

        # Construct a model instance of DeleteLockdownResp by calling from_dict on the json representation
        delete_lockdown_resp_model = DeleteLockdownResp.from_dict(delete_lockdown_resp_model_json)
        assert delete_lockdown_resp_model != False

        # Construct a model instance of DeleteLockdownResp by calling from_dict on the json representation
        delete_lockdown_resp_model_dict = DeleteLockdownResp.from_dict(delete_lockdown_resp_model_json).__dict__
        delete_lockdown_resp_model2 = DeleteLockdownResp(**delete_lockdown_resp_model_dict)

        # Verify the model instances are equivalent
        assert delete_lockdown_resp_model == delete_lockdown_resp_model2

        # Convert model instance back to dict and verify no loss of data
        delete_lockdown_resp_model_json2 = delete_lockdown_resp_model.to_dict()
        assert delete_lockdown_resp_model_json2 == delete_lockdown_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for ListLockdownResp
#-----------------------------------------------------------------------------
class TestListLockdownResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for ListLockdownResp
    #--------------------------------------------------------
    def test_list_lockdown_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        lockdown_object_configurations_item_model = {} # LockdownObjectConfigurationsItem
        lockdown_object_configurations_item_model['target'] = 'ip'
        lockdown_object_configurations_item_model['value'] = '198.51.100.4 if target=ip, 2.2.2.0/24 if target=ip_range'

        list_lockdown_resp_result_info_model = {} # ListLockdownRespResultInfo
        list_lockdown_resp_result_info_model['page'] = 1
        list_lockdown_resp_result_info_model['per_page'] = 2
        list_lockdown_resp_result_info_model['count'] = 1
        list_lockdown_resp_result_info_model['total_count'] = 200

        lockdown_object_model = {} # LockdownObject
        lockdown_object_model['id'] = '372e67954025e0ba6aaa6d586b9e0b59'
        lockdown_object_model['paused'] = False
        lockdown_object_model['description'] = 'Restrict access to these endpoints to requests from a known IP address'
        lockdown_object_model['urls'] = ['api.mysite.com/some/endpoint*']
        lockdown_object_model['configurations'] = [lockdown_object_configurations_item_model]

        # Construct a json representation of a ListLockdownResp model
        list_lockdown_resp_model_json = {}
        list_lockdown_resp_model_json['success'] = True
        list_lockdown_resp_model_json['errors'] = [['testString']]
        list_lockdown_resp_model_json['messages'] = [['testString']]
        list_lockdown_resp_model_json['result'] = [lockdown_object_model]
        list_lockdown_resp_model_json['result_info'] = list_lockdown_resp_result_info_model

        # Construct a model instance of ListLockdownResp by calling from_dict on the json representation
        list_lockdown_resp_model = ListLockdownResp.from_dict(list_lockdown_resp_model_json)
        assert list_lockdown_resp_model != False

        # Construct a model instance of ListLockdownResp by calling from_dict on the json representation
        list_lockdown_resp_model_dict = ListLockdownResp.from_dict(list_lockdown_resp_model_json).__dict__
        list_lockdown_resp_model2 = ListLockdownResp(**list_lockdown_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_lockdown_resp_model == list_lockdown_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_lockdown_resp_model_json2 = list_lockdown_resp_model.to_dict()
        assert list_lockdown_resp_model_json2 == list_lockdown_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for LockdownObject
#-----------------------------------------------------------------------------
class TestLockdownObject():

    #--------------------------------------------------------
    # Test serialization/deserialization for LockdownObject
    #--------------------------------------------------------
    def test_lockdown_object_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        lockdown_object_configurations_item_model = {} # LockdownObjectConfigurationsItem
        lockdown_object_configurations_item_model['target'] = 'ip'
        lockdown_object_configurations_item_model['value'] = '198.51.100.4 if target=ip, 2.2.2.0/24 if target=ip_range'

        # Construct a json representation of a LockdownObject model
        lockdown_object_model_json = {}
        lockdown_object_model_json['id'] = '372e67954025e0ba6aaa6d586b9e0b59'
        lockdown_object_model_json['paused'] = False
        lockdown_object_model_json['description'] = 'Restrict access to these endpoints to requests from a known IP address'
        lockdown_object_model_json['urls'] = ['api.mysite.com/some/endpoint*']
        lockdown_object_model_json['configurations'] = [lockdown_object_configurations_item_model]

        # Construct a model instance of LockdownObject by calling from_dict on the json representation
        lockdown_object_model = LockdownObject.from_dict(lockdown_object_model_json)
        assert lockdown_object_model != False

        # Construct a model instance of LockdownObject by calling from_dict on the json representation
        lockdown_object_model_dict = LockdownObject.from_dict(lockdown_object_model_json).__dict__
        lockdown_object_model2 = LockdownObject(**lockdown_object_model_dict)

        # Verify the model instances are equivalent
        assert lockdown_object_model == lockdown_object_model2

        # Convert model instance back to dict and verify no loss of data
        lockdown_object_model_json2 = lockdown_object_model.to_dict()
        assert lockdown_object_model_json2 == lockdown_object_model_json

#-----------------------------------------------------------------------------
# Test Class for LockdownResp
#-----------------------------------------------------------------------------
class TestLockdownResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for LockdownResp
    #--------------------------------------------------------
    def test_lockdown_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        lockdown_object_configurations_item_model = {} # LockdownObjectConfigurationsItem
        lockdown_object_configurations_item_model['target'] = 'ip'
        lockdown_object_configurations_item_model['value'] = '198.51.100.4 if target=ip, 2.2.2.0/24 if target=ip_range'

        lockdown_object_model = {} # LockdownObject
        lockdown_object_model['id'] = '372e67954025e0ba6aaa6d586b9e0b59'
        lockdown_object_model['paused'] = False
        lockdown_object_model['description'] = 'Restrict access to these endpoints to requests from a known IP address'
        lockdown_object_model['urls'] = ['api.mysite.com/some/endpoint*']
        lockdown_object_model['configurations'] = [lockdown_object_configurations_item_model]

        # Construct a json representation of a LockdownResp model
        lockdown_resp_model_json = {}
        lockdown_resp_model_json['success'] = True
        lockdown_resp_model_json['errors'] = [['testString']]
        lockdown_resp_model_json['messages'] = [['testString']]
        lockdown_resp_model_json['result'] = lockdown_object_model

        # Construct a model instance of LockdownResp by calling from_dict on the json representation
        lockdown_resp_model = LockdownResp.from_dict(lockdown_resp_model_json)
        assert lockdown_resp_model != False

        # Construct a model instance of LockdownResp by calling from_dict on the json representation
        lockdown_resp_model_dict = LockdownResp.from_dict(lockdown_resp_model_json).__dict__
        lockdown_resp_model2 = LockdownResp(**lockdown_resp_model_dict)

        # Verify the model instances are equivalent
        assert lockdown_resp_model == lockdown_resp_model2

        # Convert model instance back to dict and verify no loss of data
        lockdown_resp_model_json2 = lockdown_resp_model.to_dict()
        assert lockdown_resp_model_json2 == lockdown_resp_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
