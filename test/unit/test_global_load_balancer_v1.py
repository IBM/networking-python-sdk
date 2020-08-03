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
from ibm_cloud_networking_services.global_load_balancer_v1 import *

crn = 'testString'
zone_identifier = 'testString'

service = GlobalLoadBalancerV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn,
    zone_identifier=zone_identifier
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: GlobalLoadBalancer
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_all_load_balancers
#-----------------------------------------------------------------------------
class TestListAllLoadBalancers():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # list_all_load_balancers()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_load_balancers_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/load_balancers')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "699d98642c564d2e855e9661899b7252", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Load Balancer for www.example.com", "name": "www.example.com", "ttl": 30, "fallback_pool": "17b5962d775c646f3f9725cbc7a53df4", "default_pools": ["default_pools"], "region_pools": {"anyKey": "anyValue"}, "pop_pools": {"anyKey": "anyValue"}, "proxied": true, "enabled": true, "session_affinity": "ip_cookie", "steering_policy": "dynamic_latency"}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_all_load_balancers()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_all_load_balancers_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_load_balancers_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/load_balancers')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "699d98642c564d2e855e9661899b7252", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Load Balancer for www.example.com", "name": "www.example.com", "ttl": 30, "fallback_pool": "17b5962d775c646f3f9725cbc7a53df4", "default_pools": ["default_pools"], "region_pools": {"anyKey": "anyValue"}, "pop_pools": {"anyKey": "anyValue"}, "proxied": true, "enabled": true, "session_affinity": "ip_cookie", "steering_policy": "dynamic_latency"}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
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
                service.list_all_load_balancers(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for create_load_balancer
#-----------------------------------------------------------------------------
class TestCreateLoadBalancer():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # create_load_balancer()
    #--------------------------------------------------------
    @responses.activate
    def test_create_load_balancer_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/load_balancers')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "699d98642c564d2e855e9661899b7252", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Load Balancer for www.example.com", "name": "www.example.com", "ttl": 30, "fallback_pool": "17b5962d775c646f3f9725cbc7a53df4", "default_pools": ["default_pools"], "region_pools": {"anyKey": "anyValue"}, "pop_pools": {"anyKey": "anyValue"}, "proxied": true, "enabled": true, "session_affinity": "ip_cookie", "steering_policy": "dynamic_latency"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        name = 'www.example.com'
        fallback_pool = '17b5962d775c646f3f9725cbc7a53df4'
        default_pools = ['testString']
        description = 'Load Balancer for www.example.com'
        ttl = 30
        region_pools = { 'foo': 'bar' }
        pop_pools = { 'foo': 'bar' }
        proxied = True
        enabled = True
        session_affinity = 'ip_cookie'
        steering_policy = 'dynamic_latency'

        # Invoke method
        response = service.create_load_balancer(
            name=name,
            fallback_pool=fallback_pool,
            default_pools=default_pools,
            description=description,
            ttl=ttl,
            region_pools=region_pools,
            pop_pools=pop_pools,
            proxied=proxied,
            enabled=enabled,
            session_affinity=session_affinity,
            steering_policy=steering_policy,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'www.example.com'
        assert req_body['fallback_pool'] == '17b5962d775c646f3f9725cbc7a53df4'
        assert req_body['default_pools'] == ['testString']
        assert req_body['description'] == 'Load Balancer for www.example.com'
        assert req_body['ttl'] == 30
        assert req_body['region_pools'] == { 'foo': 'bar' }
        assert req_body['pop_pools'] == { 'foo': 'bar' }
        assert req_body['proxied'] == True
        assert req_body['enabled'] == True
        assert req_body['session_affinity'] == 'ip_cookie'
        assert req_body['steering_policy'] == 'dynamic_latency'


    #--------------------------------------------------------
    # test_create_load_balancer_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_load_balancer_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/load_balancers')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "699d98642c564d2e855e9661899b7252", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Load Balancer for www.example.com", "name": "www.example.com", "ttl": 30, "fallback_pool": "17b5962d775c646f3f9725cbc7a53df4", "default_pools": ["default_pools"], "region_pools": {"anyKey": "anyValue"}, "pop_pools": {"anyKey": "anyValue"}, "proxied": true, "enabled": true, "session_affinity": "ip_cookie", "steering_policy": "dynamic_latency"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.create_load_balancer()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_create_load_balancer_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_load_balancer_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/load_balancers')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "699d98642c564d2e855e9661899b7252", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Load Balancer for www.example.com", "name": "www.example.com", "ttl": 30, "fallback_pool": "17b5962d775c646f3f9725cbc7a53df4", "default_pools": ["default_pools"], "region_pools": {"anyKey": "anyValue"}, "pop_pools": {"anyKey": "anyValue"}, "proxied": true, "enabled": true, "session_affinity": "ip_cookie", "steering_policy": "dynamic_latency"}}'
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
                service.create_load_balancer(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for edit_load_balancer
#-----------------------------------------------------------------------------
class TestEditLoadBalancer():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # edit_load_balancer()
    #--------------------------------------------------------
    @responses.activate
    def test_edit_load_balancer_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/load_balancers/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "699d98642c564d2e855e9661899b7252", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Load Balancer for www.example.com", "name": "www.example.com", "ttl": 30, "fallback_pool": "17b5962d775c646f3f9725cbc7a53df4", "default_pools": ["default_pools"], "region_pools": {"anyKey": "anyValue"}, "pop_pools": {"anyKey": "anyValue"}, "proxied": true, "enabled": true, "session_affinity": "ip_cookie", "steering_policy": "dynamic_latency"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        load_balancer_identifier = 'testString'
        name = 'www.example.com'
        fallback_pool = '17b5962d775c646f3f9725cbc7a53df4'
        default_pools = ['testString']
        description = 'Load Balancer for www.example.com'
        ttl = 30
        region_pools = { 'foo': 'bar' }
        pop_pools = { 'foo': 'bar' }
        proxied = True
        enabled = True
        session_affinity = 'ip_cookie'
        steering_policy = 'dynamic_latency'

        # Invoke method
        response = service.edit_load_balancer(
            load_balancer_identifier,
            name=name,
            fallback_pool=fallback_pool,
            default_pools=default_pools,
            description=description,
            ttl=ttl,
            region_pools=region_pools,
            pop_pools=pop_pools,
            proxied=proxied,
            enabled=enabled,
            session_affinity=session_affinity,
            steering_policy=steering_policy,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'www.example.com'
        assert req_body['fallback_pool'] == '17b5962d775c646f3f9725cbc7a53df4'
        assert req_body['default_pools'] == ['testString']
        assert req_body['description'] == 'Load Balancer for www.example.com'
        assert req_body['ttl'] == 30
        assert req_body['region_pools'] == { 'foo': 'bar' }
        assert req_body['pop_pools'] == { 'foo': 'bar' }
        assert req_body['proxied'] == True
        assert req_body['enabled'] == True
        assert req_body['session_affinity'] == 'ip_cookie'
        assert req_body['steering_policy'] == 'dynamic_latency'


    #--------------------------------------------------------
    # test_edit_load_balancer_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_edit_load_balancer_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/load_balancers/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "699d98642c564d2e855e9661899b7252", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Load Balancer for www.example.com", "name": "www.example.com", "ttl": 30, "fallback_pool": "17b5962d775c646f3f9725cbc7a53df4", "default_pools": ["default_pools"], "region_pools": {"anyKey": "anyValue"}, "pop_pools": {"anyKey": "anyValue"}, "proxied": true, "enabled": true, "session_affinity": "ip_cookie", "steering_policy": "dynamic_latency"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        load_balancer_identifier = 'testString'

        # Invoke method
        response = service.edit_load_balancer(
            load_balancer_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_edit_load_balancer_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_edit_load_balancer_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/load_balancers/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "699d98642c564d2e855e9661899b7252", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Load Balancer for www.example.com", "name": "www.example.com", "ttl": 30, "fallback_pool": "17b5962d775c646f3f9725cbc7a53df4", "default_pools": ["default_pools"], "region_pools": {"anyKey": "anyValue"}, "pop_pools": {"anyKey": "anyValue"}, "proxied": true, "enabled": true, "session_affinity": "ip_cookie", "steering_policy": "dynamic_latency"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        load_balancer_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "load_balancer_identifier": load_balancer_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.edit_load_balancer(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_load_balancer
#-----------------------------------------------------------------------------
class TestDeleteLoadBalancer():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # delete_load_balancer()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_load_balancer_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/load_balancers/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "699d98642c564d2e855e9661899b7252"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        load_balancer_identifier = 'testString'

        # Invoke method
        response = service.delete_load_balancer(
            load_balancer_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_load_balancer_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_load_balancer_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/load_balancers/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "699d98642c564d2e855e9661899b7252"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        load_balancer_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "load_balancer_identifier": load_balancer_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_load_balancer(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_load_balancer_settings
#-----------------------------------------------------------------------------
class TestGetLoadBalancerSettings():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_load_balancer_settings()
    #--------------------------------------------------------
    @responses.activate
    def test_get_load_balancer_settings_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/load_balancers/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "699d98642c564d2e855e9661899b7252", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Load Balancer for www.example.com", "name": "www.example.com", "ttl": 30, "fallback_pool": "17b5962d775c646f3f9725cbc7a53df4", "default_pools": ["default_pools"], "region_pools": {"anyKey": "anyValue"}, "pop_pools": {"anyKey": "anyValue"}, "proxied": true, "enabled": true, "session_affinity": "ip_cookie", "steering_policy": "dynamic_latency"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        load_balancer_identifier = 'testString'

        # Invoke method
        response = service.get_load_balancer_settings(
            load_balancer_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_load_balancer_settings_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_load_balancer_settings_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/load_balancers/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "699d98642c564d2e855e9661899b7252", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Load Balancer for www.example.com", "name": "www.example.com", "ttl": 30, "fallback_pool": "17b5962d775c646f3f9725cbc7a53df4", "default_pools": ["default_pools"], "region_pools": {"anyKey": "anyValue"}, "pop_pools": {"anyKey": "anyValue"}, "proxied": true, "enabled": true, "session_affinity": "ip_cookie", "steering_policy": "dynamic_latency"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        load_balancer_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "load_balancer_identifier": load_balancer_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_load_balancer_settings(**req_copy)



# endregion
##############################################################################
# End of Service: GlobalLoadBalancer
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for DeleteLoadBalancersRespResult
#-----------------------------------------------------------------------------
class TestDeleteLoadBalancersRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for DeleteLoadBalancersRespResult
    #--------------------------------------------------------
    def test_delete_load_balancers_resp_result_serialization(self):

        # Construct a json representation of a DeleteLoadBalancersRespResult model
        delete_load_balancers_resp_result_model_json = {}
        delete_load_balancers_resp_result_model_json['id'] = '699d98642c564d2e855e9661899b7252'

        # Construct a model instance of DeleteLoadBalancersRespResult by calling from_dict on the json representation
        delete_load_balancers_resp_result_model = DeleteLoadBalancersRespResult.from_dict(delete_load_balancers_resp_result_model_json)
        assert delete_load_balancers_resp_result_model != False

        # Construct a model instance of DeleteLoadBalancersRespResult by calling from_dict on the json representation
        delete_load_balancers_resp_result_model_dict = DeleteLoadBalancersRespResult.from_dict(delete_load_balancers_resp_result_model_json).__dict__
        delete_load_balancers_resp_result_model2 = DeleteLoadBalancersRespResult(**delete_load_balancers_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert delete_load_balancers_resp_result_model == delete_load_balancers_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        delete_load_balancers_resp_result_model_json2 = delete_load_balancers_resp_result_model.to_dict()
        assert delete_load_balancers_resp_result_model_json2 == delete_load_balancers_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for DeleteLoadBalancersResp
#-----------------------------------------------------------------------------
class TestDeleteLoadBalancersResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for DeleteLoadBalancersResp
    #--------------------------------------------------------
    def test_delete_load_balancers_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        delete_load_balancers_resp_result_model = {} # DeleteLoadBalancersRespResult
        delete_load_balancers_resp_result_model['id'] = '699d98642c564d2e855e9661899b7252'

        # Construct a json representation of a DeleteLoadBalancersResp model
        delete_load_balancers_resp_model_json = {}
        delete_load_balancers_resp_model_json['success'] = True
        delete_load_balancers_resp_model_json['errors'] = [['testString']]
        delete_load_balancers_resp_model_json['messages'] = [['testString']]
        delete_load_balancers_resp_model_json['result'] = delete_load_balancers_resp_result_model

        # Construct a model instance of DeleteLoadBalancersResp by calling from_dict on the json representation
        delete_load_balancers_resp_model = DeleteLoadBalancersResp.from_dict(delete_load_balancers_resp_model_json)
        assert delete_load_balancers_resp_model != False

        # Construct a model instance of DeleteLoadBalancersResp by calling from_dict on the json representation
        delete_load_balancers_resp_model_dict = DeleteLoadBalancersResp.from_dict(delete_load_balancers_resp_model_json).__dict__
        delete_load_balancers_resp_model2 = DeleteLoadBalancersResp(**delete_load_balancers_resp_model_dict)

        # Verify the model instances are equivalent
        assert delete_load_balancers_resp_model == delete_load_balancers_resp_model2

        # Convert model instance back to dict and verify no loss of data
        delete_load_balancers_resp_model_json2 = delete_load_balancers_resp_model.to_dict()
        assert delete_load_balancers_resp_model_json2 == delete_load_balancers_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for ListLoadBalancersResp
#-----------------------------------------------------------------------------
class TestListLoadBalancersResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for ListLoadBalancersResp
    #--------------------------------------------------------
    def test_list_load_balancers_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        load_balancer_pack_model = {} # LoadBalancerPack
        load_balancer_pack_model['id'] = '699d98642c564d2e855e9661899b7252'
        load_balancer_pack_model['created_on'] = '2014-01-01T05:20:00.12345Z'
        load_balancer_pack_model['modified_on'] = '2014-01-01T05:20:00.12345Z'
        load_balancer_pack_model['description'] = 'Load Balancer for www.example.com'
        load_balancer_pack_model['name'] = 'www.example.com'
        load_balancer_pack_model['ttl'] = 30
        load_balancer_pack_model['fallback_pool'] = '17b5962d775c646f3f9725cbc7a53df4'
        load_balancer_pack_model['default_pools'] = ['testString']
        load_balancer_pack_model['region_pools'] = { 'foo': 'bar' }
        load_balancer_pack_model['pop_pools'] = { 'foo': 'bar' }
        load_balancer_pack_model['proxied'] = True
        load_balancer_pack_model['enabled'] = True
        load_balancer_pack_model['session_affinity'] = 'ip_cookie'
        load_balancer_pack_model['steering_policy'] = 'dynamic_latency'

        result_info_model = {} # ResultInfo
        result_info_model['page'] = 1
        result_info_model['per_page'] = 20
        result_info_model['count'] = 1
        result_info_model['total_count'] = 2000

        # Construct a json representation of a ListLoadBalancersResp model
        list_load_balancers_resp_model_json = {}
        list_load_balancers_resp_model_json['success'] = True
        list_load_balancers_resp_model_json['errors'] = [['testString']]
        list_load_balancers_resp_model_json['messages'] = [['testString']]
        list_load_balancers_resp_model_json['result'] = [load_balancer_pack_model]
        list_load_balancers_resp_model_json['result_info'] = result_info_model

        # Construct a model instance of ListLoadBalancersResp by calling from_dict on the json representation
        list_load_balancers_resp_model = ListLoadBalancersResp.from_dict(list_load_balancers_resp_model_json)
        assert list_load_balancers_resp_model != False

        # Construct a model instance of ListLoadBalancersResp by calling from_dict on the json representation
        list_load_balancers_resp_model_dict = ListLoadBalancersResp.from_dict(list_load_balancers_resp_model_json).__dict__
        list_load_balancers_resp_model2 = ListLoadBalancersResp(**list_load_balancers_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_load_balancers_resp_model == list_load_balancers_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_load_balancers_resp_model_json2 = list_load_balancers_resp_model.to_dict()
        assert list_load_balancers_resp_model_json2 == list_load_balancers_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for LoadBalancerPack
#-----------------------------------------------------------------------------
class TestLoadBalancerPack():

    #--------------------------------------------------------
    # Test serialization/deserialization for LoadBalancerPack
    #--------------------------------------------------------
    def test_load_balancer_pack_serialization(self):

        # Construct a json representation of a LoadBalancerPack model
        load_balancer_pack_model_json = {}
        load_balancer_pack_model_json['id'] = '699d98642c564d2e855e9661899b7252'
        load_balancer_pack_model_json['created_on'] = '2014-01-01T05:20:00.12345Z'
        load_balancer_pack_model_json['modified_on'] = '2014-01-01T05:20:00.12345Z'
        load_balancer_pack_model_json['description'] = 'Load Balancer for www.example.com'
        load_balancer_pack_model_json['name'] = 'www.example.com'
        load_balancer_pack_model_json['ttl'] = 30
        load_balancer_pack_model_json['fallback_pool'] = '17b5962d775c646f3f9725cbc7a53df4'
        load_balancer_pack_model_json['default_pools'] = ['testString']
        load_balancer_pack_model_json['region_pools'] = { 'foo': 'bar' }
        load_balancer_pack_model_json['pop_pools'] = { 'foo': 'bar' }
        load_balancer_pack_model_json['proxied'] = True
        load_balancer_pack_model_json['enabled'] = True
        load_balancer_pack_model_json['session_affinity'] = 'ip_cookie'
        load_balancer_pack_model_json['steering_policy'] = 'dynamic_latency'

        # Construct a model instance of LoadBalancerPack by calling from_dict on the json representation
        load_balancer_pack_model = LoadBalancerPack.from_dict(load_balancer_pack_model_json)
        assert load_balancer_pack_model != False

        # Construct a model instance of LoadBalancerPack by calling from_dict on the json representation
        load_balancer_pack_model_dict = LoadBalancerPack.from_dict(load_balancer_pack_model_json).__dict__
        load_balancer_pack_model2 = LoadBalancerPack(**load_balancer_pack_model_dict)

        # Verify the model instances are equivalent
        assert load_balancer_pack_model == load_balancer_pack_model2

        # Convert model instance back to dict and verify no loss of data
        load_balancer_pack_model_json2 = load_balancer_pack_model.to_dict()
        assert load_balancer_pack_model_json2 == load_balancer_pack_model_json

#-----------------------------------------------------------------------------
# Test Class for LoadBalancersResp
#-----------------------------------------------------------------------------
class TestLoadBalancersResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for LoadBalancersResp
    #--------------------------------------------------------
    def test_load_balancers_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        load_balancer_pack_model = {} # LoadBalancerPack
        load_balancer_pack_model['id'] = '699d98642c564d2e855e9661899b7252'
        load_balancer_pack_model['created_on'] = '2014-01-01T05:20:00.12345Z'
        load_balancer_pack_model['modified_on'] = '2014-01-01T05:20:00.12345Z'
        load_balancer_pack_model['description'] = 'Load Balancer for www.example.com'
        load_balancer_pack_model['name'] = 'www.example.com'
        load_balancer_pack_model['ttl'] = 30
        load_balancer_pack_model['fallback_pool'] = '17b5962d775c646f3f9725cbc7a53df4'
        load_balancer_pack_model['default_pools'] = ['testString']
        load_balancer_pack_model['region_pools'] = { 'foo': 'bar' }
        load_balancer_pack_model['pop_pools'] = { 'foo': 'bar' }
        load_balancer_pack_model['proxied'] = True
        load_balancer_pack_model['enabled'] = True
        load_balancer_pack_model['session_affinity'] = 'ip_cookie'
        load_balancer_pack_model['steering_policy'] = 'dynamic_latency'

        # Construct a json representation of a LoadBalancersResp model
        load_balancers_resp_model_json = {}
        load_balancers_resp_model_json['success'] = True
        load_balancers_resp_model_json['errors'] = [['testString']]
        load_balancers_resp_model_json['messages'] = [['testString']]
        load_balancers_resp_model_json['result'] = load_balancer_pack_model

        # Construct a model instance of LoadBalancersResp by calling from_dict on the json representation
        load_balancers_resp_model = LoadBalancersResp.from_dict(load_balancers_resp_model_json)
        assert load_balancers_resp_model != False

        # Construct a model instance of LoadBalancersResp by calling from_dict on the json representation
        load_balancers_resp_model_dict = LoadBalancersResp.from_dict(load_balancers_resp_model_json).__dict__
        load_balancers_resp_model2 = LoadBalancersResp(**load_balancers_resp_model_dict)

        # Verify the model instances are equivalent
        assert load_balancers_resp_model == load_balancers_resp_model2

        # Convert model instance back to dict and verify no loss of data
        load_balancers_resp_model_json2 = load_balancers_resp_model.to_dict()
        assert load_balancers_resp_model_json2 == load_balancers_resp_model_json

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
