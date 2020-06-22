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

    #--------------------------------------------------------
    # list_all_load_balancers()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_load_balancers_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/load_balancers'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "699d98642c564d2e855e9661899b7252", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Load Balancer for www.example.com", "name": "www.example.com", "ttl": 30, "fallback_pool": "17b5962d775c646f3f9725cbc7a53df4", "default_pools": ["default_pools"], "region_pools": ["unknown property type: region_pools"], "pop_pools": ["unknown property type: pop_pools"], "proxied": true, "enabled": true, "session_affinity": "ip_cookie", "steering_policy": "dynamic_latency"}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
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
    # test_list_all_load_balancers_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_load_balancers_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/load_balancers'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "699d98642c564d2e855e9661899b7252", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Load Balancer for www.example.com", "name": "www.example.com", "ttl": 30, "fallback_pool": "17b5962d775c646f3f9725cbc7a53df4", "default_pools": ["default_pools"], "region_pools": ["unknown property type: region_pools"], "pop_pools": ["unknown property type: pop_pools"], "proxied": true, "enabled": true, "session_affinity": "ip_cookie", "steering_policy": "dynamic_latency"}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
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


#-----------------------------------------------------------------------------
# Test Class for create_load_balancer
#-----------------------------------------------------------------------------
class TestCreateLoadBalancer():

    #--------------------------------------------------------
    # create_load_balancer()
    #--------------------------------------------------------
    @responses.activate
    def test_create_load_balancer_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/load_balancers'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "699d98642c564d2e855e9661899b7252", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Load Balancer for www.example.com", "name": "www.example.com", "ttl": 30, "fallback_pool": "17b5962d775c646f3f9725cbc7a53df4", "default_pools": ["default_pools"], "region_pools": ["unknown property type: region_pools"], "pop_pools": ["unknown property type: pop_pools"], "proxied": true, "enabled": true, "session_affinity": "ip_cookie", "steering_policy": "dynamic_latency"}}'
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
        region_pools = ['unknown type: object']
        pop_pools = ['unknown type: object']
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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['fallback_pool'] == fallback_pool
        assert req_body['default_pools'] == default_pools
        assert req_body['description'] == description
        assert req_body['ttl'] == ttl
        assert req_body['region_pools'] == region_pools
        assert req_body['pop_pools'] == pop_pools
        assert req_body['proxied'] == proxied
        assert req_body['enabled'] == enabled
        assert req_body['session_affinity'] == session_affinity
        assert req_body['steering_policy'] == steering_policy


    #--------------------------------------------------------
    # test_create_load_balancer_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_load_balancer_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/load_balancers'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "699d98642c564d2e855e9661899b7252", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Load Balancer for www.example.com", "name": "www.example.com", "ttl": 30, "fallback_pool": "17b5962d775c646f3f9725cbc7a53df4", "default_pools": ["default_pools"], "region_pools": ["unknown property type: region_pools"], "pop_pools": ["unknown property type: pop_pools"], "proxied": true, "enabled": true, "session_affinity": "ip_cookie", "steering_policy": "dynamic_latency"}}'
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


#-----------------------------------------------------------------------------
# Test Class for edit_load_balancer
#-----------------------------------------------------------------------------
class TestEditLoadBalancer():

    #--------------------------------------------------------
    # edit_load_balancer()
    #--------------------------------------------------------
    @responses.activate
    def test_edit_load_balancer_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/load_balancers/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "699d98642c564d2e855e9661899b7252", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Load Balancer for www.example.com", "name": "www.example.com", "ttl": 30, "fallback_pool": "17b5962d775c646f3f9725cbc7a53df4", "default_pools": ["default_pools"], "region_pools": ["unknown property type: region_pools"], "pop_pools": ["unknown property type: pop_pools"], "proxied": true, "enabled": true, "session_affinity": "ip_cookie", "steering_policy": "dynamic_latency"}}'
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
        region_pools = ['unknown type: object']
        pop_pools = ['unknown type: object']
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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['fallback_pool'] == fallback_pool
        assert req_body['default_pools'] == default_pools
        assert req_body['description'] == description
        assert req_body['ttl'] == ttl
        assert req_body['region_pools'] == region_pools
        assert req_body['pop_pools'] == pop_pools
        assert req_body['proxied'] == proxied
        assert req_body['enabled'] == enabled
        assert req_body['session_affinity'] == session_affinity
        assert req_body['steering_policy'] == steering_policy


    #--------------------------------------------------------
    # test_edit_load_balancer_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_edit_load_balancer_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/load_balancers/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "699d98642c564d2e855e9661899b7252", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Load Balancer for www.example.com", "name": "www.example.com", "ttl": 30, "fallback_pool": "17b5962d775c646f3f9725cbc7a53df4", "default_pools": ["default_pools"], "region_pools": ["unknown property type: region_pools"], "pop_pools": ["unknown property type: pop_pools"], "proxied": true, "enabled": true, "session_affinity": "ip_cookie", "steering_policy": "dynamic_latency"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        load_balancer_identifier = 'testString'

        # Invoke method
        response = service.edit_load_balancer(
            load_balancer_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for delete_load_balancer
#-----------------------------------------------------------------------------
class TestDeleteLoadBalancer():

    #--------------------------------------------------------
    # delete_load_balancer()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_load_balancer_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/load_balancers/testString'
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
            load_balancer_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_load_balancer_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_load_balancer_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/load_balancers/testString'
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
            load_balancer_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_load_balancer_settings
#-----------------------------------------------------------------------------
class TestGetLoadBalancerSettings():

    #--------------------------------------------------------
    # get_load_balancer_settings()
    #--------------------------------------------------------
    @responses.activate
    def test_get_load_balancer_settings_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/load_balancers/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "699d98642c564d2e855e9661899b7252", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Load Balancer for www.example.com", "name": "www.example.com", "ttl": 30, "fallback_pool": "17b5962d775c646f3f9725cbc7a53df4", "default_pools": ["default_pools"], "region_pools": ["unknown property type: region_pools"], "pop_pools": ["unknown property type: pop_pools"], "proxied": true, "enabled": true, "session_affinity": "ip_cookie", "steering_policy": "dynamic_latency"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        load_balancer_identifier = 'testString'

        # Invoke method
        response = service.get_load_balancer_settings(
            load_balancer_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_load_balancer_settings_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_load_balancer_settings_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/load_balancers/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "699d98642c564d2e855e9661899b7252", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Load Balancer for www.example.com", "name": "www.example.com", "ttl": 30, "fallback_pool": "17b5962d775c646f3f9725cbc7a53df4", "default_pools": ["default_pools"], "region_pools": ["unknown property type: region_pools"], "pop_pools": ["unknown property type: pop_pools"], "proxied": true, "enabled": true, "session_affinity": "ip_cookie", "steering_policy": "dynamic_latency"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        load_balancer_identifier = 'testString'

        # Invoke method
        response = service.get_load_balancer_settings(
            load_balancer_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GlobalLoadBalancer
##############################################################################

