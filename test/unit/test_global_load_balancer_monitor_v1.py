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
import responses
from ibm_cloud_networking_services.global_load_balancer_monitor_v1 import *

crn = 'testString'

service = GlobalLoadBalancerMonitorV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: GlobalLoadBalancerMonitor
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_all_load_balancer_monitors
#-----------------------------------------------------------------------------
class TestListAllLoadBalancerMonitors():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # list_all_load_balancer_monitors()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_load_balancer_monitors_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/load_balancers/monitors')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "type": "http", "description": "Login page monitor", "method": "GET", "port": 8080, "path": "/", "timeout": 5, "retries": 2, "interval": 60, "expected_body": "alive", "expected_codes": "2xx", "follow_redirects": true, "allow_insecure": true, "header": {"mapKey": ["inner"]}}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_all_load_balancer_monitors()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_all_load_balancer_monitors_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_load_balancer_monitors_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/load_balancers/monitors')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "type": "http", "description": "Login page monitor", "method": "GET", "port": 8080, "path": "/", "timeout": 5, "retries": 2, "interval": 60, "expected_body": "alive", "expected_codes": "2xx", "follow_redirects": true, "allow_insecure": true, "header": {"mapKey": ["inner"]}}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
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
                service.list_all_load_balancer_monitors(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for create_load_balancer_monitor
#-----------------------------------------------------------------------------
class TestCreateLoadBalancerMonitor():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # create_load_balancer_monitor()
    #--------------------------------------------------------
    @responses.activate
    def test_create_load_balancer_monitor_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/load_balancers/monitors')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "type": "http", "description": "Login page monitor", "method": "GET", "port": 8080, "path": "/", "timeout": 5, "retries": 2, "interval": 60, "expected_body": "alive", "expected_codes": "2xx", "follow_redirects": true, "allow_insecure": true, "header": {"mapKey": ["inner"]}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        expected_codes = '2xx'
        type = 'http'
        description = 'Login page monitor'
        method = 'GET'
        port = 8080
        path = '/'
        timeout = 5
        retries = 2
        interval = 60
        follow_redirects = True
        expected_body = 'alive'
        allow_insecure = True
        header = {}

        # Invoke method
        response = service.create_load_balancer_monitor(
            expected_codes=expected_codes,
            type=type,
            description=description,
            method=method,
            port=port,
            path=path,
            timeout=timeout,
            retries=retries,
            interval=interval,
            follow_redirects=follow_redirects,
            expected_body=expected_body,
            allow_insecure=allow_insecure,
            header=header,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['expected_codes'] == '2xx'
        assert req_body['type'] == 'http'
        assert req_body['description'] == 'Login page monitor'
        assert req_body['method'] == 'GET'
        assert req_body['port'] == 8080
        assert req_body['path'] == '/'
        assert req_body['timeout'] == 5
        assert req_body['retries'] == 2
        assert req_body['interval'] == 60
        assert req_body['follow_redirects'] == True
        assert req_body['expected_body'] == 'alive'
        assert req_body['allow_insecure'] == True
        assert req_body['header'] == {}


    #--------------------------------------------------------
    # test_create_load_balancer_monitor_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_load_balancer_monitor_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/load_balancers/monitors')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "type": "http", "description": "Login page monitor", "method": "GET", "port": 8080, "path": "/", "timeout": 5, "retries": 2, "interval": 60, "expected_body": "alive", "expected_codes": "2xx", "follow_redirects": true, "allow_insecure": true, "header": {"mapKey": ["inner"]}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.create_load_balancer_monitor()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_create_load_balancer_monitor_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_load_balancer_monitor_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/load_balancers/monitors')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "type": "http", "description": "Login page monitor", "method": "GET", "port": 8080, "path": "/", "timeout": 5, "retries": 2, "interval": 60, "expected_body": "alive", "expected_codes": "2xx", "follow_redirects": true, "allow_insecure": true, "header": {"mapKey": ["inner"]}}}'
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
                service.create_load_balancer_monitor(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for edit_load_balancer_monitor
#-----------------------------------------------------------------------------
class TestEditLoadBalancerMonitor():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # edit_load_balancer_monitor()
    #--------------------------------------------------------
    @responses.activate
    def test_edit_load_balancer_monitor_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/load_balancers/monitors/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "type": "http", "description": "Login page monitor", "method": "GET", "port": 8080, "path": "/", "timeout": 5, "retries": 2, "interval": 60, "expected_body": "alive", "expected_codes": "2xx", "follow_redirects": true, "allow_insecure": true, "header": {"mapKey": ["inner"]}}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        monitor_identifier = 'testString'
        expected_codes = '2xx'
        type = 'http'
        description = 'Login page monitor'
        method = 'GET'
        port = 8080
        path = '/'
        timeout = 5
        retries = 2
        interval = 60
        follow_redirects = True
        expected_body = 'alive'
        allow_insecure = True
        header = {}

        # Invoke method
        response = service.edit_load_balancer_monitor(
            monitor_identifier,
            expected_codes=expected_codes,
            type=type,
            description=description,
            method=method,
            port=port,
            path=path,
            timeout=timeout,
            retries=retries,
            interval=interval,
            follow_redirects=follow_redirects,
            expected_body=expected_body,
            allow_insecure=allow_insecure,
            header=header,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['expected_codes'] == '2xx'
        assert req_body['type'] == 'http'
        assert req_body['description'] == 'Login page monitor'
        assert req_body['method'] == 'GET'
        assert req_body['port'] == 8080
        assert req_body['path'] == '/'
        assert req_body['timeout'] == 5
        assert req_body['retries'] == 2
        assert req_body['interval'] == 60
        assert req_body['follow_redirects'] == True
        assert req_body['expected_body'] == 'alive'
        assert req_body['allow_insecure'] == True
        assert req_body['header'] == {}


    #--------------------------------------------------------
    # test_edit_load_balancer_monitor_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_edit_load_balancer_monitor_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/load_balancers/monitors/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "type": "http", "description": "Login page monitor", "method": "GET", "port": 8080, "path": "/", "timeout": 5, "retries": 2, "interval": 60, "expected_body": "alive", "expected_codes": "2xx", "follow_redirects": true, "allow_insecure": true, "header": {"mapKey": ["inner"]}}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        monitor_identifier = 'testString'

        # Invoke method
        response = service.edit_load_balancer_monitor(
            monitor_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_edit_load_balancer_monitor_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_edit_load_balancer_monitor_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/load_balancers/monitors/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "type": "http", "description": "Login page monitor", "method": "GET", "port": 8080, "path": "/", "timeout": 5, "retries": 2, "interval": 60, "expected_body": "alive", "expected_codes": "2xx", "follow_redirects": true, "allow_insecure": true, "header": {"mapKey": ["inner"]}}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        monitor_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "monitor_identifier": monitor_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.edit_load_balancer_monitor(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_load_balancer_monitor
#-----------------------------------------------------------------------------
class TestDeleteLoadBalancerMonitor():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # delete_load_balancer_monitor()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_load_balancer_monitor_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/load_balancers/monitors/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        monitor_identifier = 'testString'

        # Invoke method
        response = service.delete_load_balancer_monitor(
            monitor_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_load_balancer_monitor_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_load_balancer_monitor_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/load_balancers/monitors/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        monitor_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "monitor_identifier": monitor_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_load_balancer_monitor(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_load_balancer_monitor
#-----------------------------------------------------------------------------
class TestGetLoadBalancerMonitor():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_load_balancer_monitor()
    #--------------------------------------------------------
    @responses.activate
    def test_get_load_balancer_monitor_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/load_balancers/monitors/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "type": "http", "description": "Login page monitor", "method": "GET", "port": 8080, "path": "/", "timeout": 5, "retries": 2, "interval": 60, "expected_body": "alive", "expected_codes": "2xx", "follow_redirects": true, "allow_insecure": true, "header": {"mapKey": ["inner"]}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        monitor_identifier = 'testString'

        # Invoke method
        response = service.get_load_balancer_monitor(
            monitor_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_load_balancer_monitor_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_load_balancer_monitor_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/load_balancers/monitors/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "type": "http", "description": "Login page monitor", "method": "GET", "port": 8080, "path": "/", "timeout": 5, "retries": 2, "interval": 60, "expected_body": "alive", "expected_codes": "2xx", "follow_redirects": true, "allow_insecure": true, "header": {"mapKey": ["inner"]}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        monitor_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "monitor_identifier": monitor_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_load_balancer_monitor(**req_copy)



# endregion
##############################################################################
# End of Service: GlobalLoadBalancerMonitor
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for DeleteMonitorRespResult
#-----------------------------------------------------------------------------
class TestDeleteMonitorRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for DeleteMonitorRespResult
    #--------------------------------------------------------
    def test_delete_monitor_resp_result_serialization(self):

        # Construct a json representation of a DeleteMonitorRespResult model
        delete_monitor_resp_result_model_json = {}
        delete_monitor_resp_result_model_json['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'

        # Construct a model instance of DeleteMonitorRespResult by calling from_dict on the json representation
        delete_monitor_resp_result_model = DeleteMonitorRespResult.from_dict(delete_monitor_resp_result_model_json)
        assert delete_monitor_resp_result_model != False

        # Construct a model instance of DeleteMonitorRespResult by calling from_dict on the json representation
        delete_monitor_resp_result_model_dict = DeleteMonitorRespResult.from_dict(delete_monitor_resp_result_model_json).__dict__
        delete_monitor_resp_result_model2 = DeleteMonitorRespResult(**delete_monitor_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert delete_monitor_resp_result_model == delete_monitor_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        delete_monitor_resp_result_model_json2 = delete_monitor_resp_result_model.to_dict()
        assert delete_monitor_resp_result_model_json2 == delete_monitor_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for DeleteMonitorResp
#-----------------------------------------------------------------------------
class TestDeleteMonitorResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for DeleteMonitorResp
    #--------------------------------------------------------
    def test_delete_monitor_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        delete_monitor_resp_result_model = {} # DeleteMonitorRespResult
        delete_monitor_resp_result_model['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'

        # Construct a json representation of a DeleteMonitorResp model
        delete_monitor_resp_model_json = {}
        delete_monitor_resp_model_json['success'] = True
        delete_monitor_resp_model_json['errors'] = [['testString']]
        delete_monitor_resp_model_json['messages'] = [['testString']]
        delete_monitor_resp_model_json['result'] = delete_monitor_resp_result_model

        # Construct a model instance of DeleteMonitorResp by calling from_dict on the json representation
        delete_monitor_resp_model = DeleteMonitorResp.from_dict(delete_monitor_resp_model_json)
        assert delete_monitor_resp_model != False

        # Construct a model instance of DeleteMonitorResp by calling from_dict on the json representation
        delete_monitor_resp_model_dict = DeleteMonitorResp.from_dict(delete_monitor_resp_model_json).__dict__
        delete_monitor_resp_model2 = DeleteMonitorResp(**delete_monitor_resp_model_dict)

        # Verify the model instances are equivalent
        assert delete_monitor_resp_model == delete_monitor_resp_model2

        # Convert model instance back to dict and verify no loss of data
        delete_monitor_resp_model_json2 = delete_monitor_resp_model.to_dict()
        assert delete_monitor_resp_model_json2 == delete_monitor_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for ListMonitorResp
#-----------------------------------------------------------------------------
class TestListMonitorResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for ListMonitorResp
    #--------------------------------------------------------
    def test_list_monitor_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        monitor_pack_model = {} # MonitorPack
        monitor_pack_model['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        monitor_pack_model['created_on'] = '2014-01-01T05:20:00.12345Z'
        monitor_pack_model['modified_on'] = '2014-01-01T05:20:00.12345Z'
        monitor_pack_model['type'] = 'http'
        monitor_pack_model['description'] = 'Login page monitor'
        monitor_pack_model['method'] = 'GET'
        monitor_pack_model['port'] = 8080
        monitor_pack_model['path'] = '/'
        monitor_pack_model['timeout'] = 5
        monitor_pack_model['retries'] = 2
        monitor_pack_model['interval'] = 60
        monitor_pack_model['expected_body'] = 'alive'
        monitor_pack_model['expected_codes'] = '2xx'
        monitor_pack_model['follow_redirects'] = True
        monitor_pack_model['allow_insecure'] = True
        monitor_pack_model['header'] = {}

        result_info_model = {} # ResultInfo
        result_info_model['page'] = 1
        result_info_model['per_page'] = 20
        result_info_model['count'] = 1
        result_info_model['total_count'] = 2000

        # Construct a json representation of a ListMonitorResp model
        list_monitor_resp_model_json = {}
        list_monitor_resp_model_json['success'] = True
        list_monitor_resp_model_json['errors'] = [['testString']]
        list_monitor_resp_model_json['messages'] = [['testString']]
        list_monitor_resp_model_json['result'] = [monitor_pack_model]
        list_monitor_resp_model_json['result_info'] = result_info_model

        # Construct a model instance of ListMonitorResp by calling from_dict on the json representation
        list_monitor_resp_model = ListMonitorResp.from_dict(list_monitor_resp_model_json)
        assert list_monitor_resp_model != False

        # Construct a model instance of ListMonitorResp by calling from_dict on the json representation
        list_monitor_resp_model_dict = ListMonitorResp.from_dict(list_monitor_resp_model_json).__dict__
        list_monitor_resp_model2 = ListMonitorResp(**list_monitor_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_monitor_resp_model == list_monitor_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_monitor_resp_model_json2 = list_monitor_resp_model.to_dict()
        assert list_monitor_resp_model_json2 == list_monitor_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for MonitorPack
#-----------------------------------------------------------------------------
class TestMonitorPack():

    #--------------------------------------------------------
    # Test serialization/deserialization for MonitorPack
    #--------------------------------------------------------
    def test_monitor_pack_serialization(self):

        # Construct a json representation of a MonitorPack model
        monitor_pack_model_json = {}
        monitor_pack_model_json['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        monitor_pack_model_json['created_on'] = '2014-01-01T05:20:00.12345Z'
        monitor_pack_model_json['modified_on'] = '2014-01-01T05:20:00.12345Z'
        monitor_pack_model_json['type'] = 'http'
        monitor_pack_model_json['description'] = 'Login page monitor'
        monitor_pack_model_json['method'] = 'GET'
        monitor_pack_model_json['port'] = 8080
        monitor_pack_model_json['path'] = '/'
        monitor_pack_model_json['timeout'] = 5
        monitor_pack_model_json['retries'] = 2
        monitor_pack_model_json['interval'] = 60
        monitor_pack_model_json['expected_body'] = 'alive'
        monitor_pack_model_json['expected_codes'] = '2xx'
        monitor_pack_model_json['follow_redirects'] = True
        monitor_pack_model_json['allow_insecure'] = True
        monitor_pack_model_json['header'] = {}

        # Construct a model instance of MonitorPack by calling from_dict on the json representation
        monitor_pack_model = MonitorPack.from_dict(monitor_pack_model_json)
        assert monitor_pack_model != False

        # Construct a model instance of MonitorPack by calling from_dict on the json representation
        monitor_pack_model_dict = MonitorPack.from_dict(monitor_pack_model_json).__dict__
        monitor_pack_model2 = MonitorPack(**monitor_pack_model_dict)

        # Verify the model instances are equivalent
        assert monitor_pack_model == monitor_pack_model2

        # Convert model instance back to dict and verify no loss of data
        monitor_pack_model_json2 = monitor_pack_model.to_dict()
        assert monitor_pack_model_json2 == monitor_pack_model_json

#-----------------------------------------------------------------------------
# Test Class for MonitorResp
#-----------------------------------------------------------------------------
class TestMonitorResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for MonitorResp
    #--------------------------------------------------------
    def test_monitor_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        monitor_pack_model = {} # MonitorPack
        monitor_pack_model['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        monitor_pack_model['created_on'] = '2014-01-01T05:20:00.12345Z'
        monitor_pack_model['modified_on'] = '2014-01-01T05:20:00.12345Z'
        monitor_pack_model['type'] = 'http'
        monitor_pack_model['description'] = 'Login page monitor'
        monitor_pack_model['method'] = 'GET'
        monitor_pack_model['port'] = 8080
        monitor_pack_model['path'] = '/'
        monitor_pack_model['timeout'] = 5
        monitor_pack_model['retries'] = 2
        monitor_pack_model['interval'] = 60
        monitor_pack_model['expected_body'] = 'alive'
        monitor_pack_model['expected_codes'] = '2xx'
        monitor_pack_model['follow_redirects'] = True
        monitor_pack_model['allow_insecure'] = True
        monitor_pack_model['header'] = {}

        # Construct a json representation of a MonitorResp model
        monitor_resp_model_json = {}
        monitor_resp_model_json['success'] = True
        monitor_resp_model_json['errors'] = [['testString']]
        monitor_resp_model_json['messages'] = [['testString']]
        monitor_resp_model_json['result'] = monitor_pack_model

        # Construct a model instance of MonitorResp by calling from_dict on the json representation
        monitor_resp_model = MonitorResp.from_dict(monitor_resp_model_json)
        assert monitor_resp_model != False

        # Construct a model instance of MonitorResp by calling from_dict on the json representation
        monitor_resp_model_dict = MonitorResp.from_dict(monitor_resp_model_json).__dict__
        monitor_resp_model2 = MonitorResp(**monitor_resp_model_dict)

        # Verify the model instances are equivalent
        assert monitor_resp_model == monitor_resp_model2

        # Convert model instance back to dict and verify no loss of data
        monitor_resp_model_json2 = monitor_resp_model.to_dict()
        assert monitor_resp_model_json2 == monitor_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for ResultInfo
#-----------------------------------------------------------------------------
class TestResultInfo():

    #--------------------------------------------------------
    # Test serialization/deserialization for ResultInfo
    #--------------------------------------------------------
    def test_result_info_serialization(self):

        # Construct a json representation of a ResultInfo model
        result_info_model_json = {}
        result_info_model_json['page'] = 1
        result_info_model_json['per_page'] = 20
        result_info_model_json['count'] = 1
        result_info_model_json['total_count'] = 2000

        # Construct a model instance of ResultInfo by calling from_dict on the json representation
        result_info_model = ResultInfo.from_dict(result_info_model_json)
        assert result_info_model != False

        # Construct a model instance of ResultInfo by calling from_dict on the json representation
        result_info_model_dict = ResultInfo.from_dict(result_info_model_json).__dict__
        result_info_model2 = ResultInfo(**result_info_model_dict)

        # Verify the model instances are equivalent
        assert result_info_model == result_info_model2

        # Convert model instance back to dict and verify no loss of data
        result_info_model_json2 = result_info_model.to_dict()
        assert result_info_model_json2 == result_info_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
