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
from ibm_cloud_networking_services.dns_global_load_balancers_v1 import *


service = DnsGlobalLoadBalancersV1(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://api.dns-svcs.cloud.ibm.com/v1'
service.set_service_url(base_url)

##############################################################################
# Start of Service: GlobalLoadBalancers
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_load_balancers
#-----------------------------------------------------------------------------
class TestListLoadBalancers():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # list_load_balancers()
    #--------------------------------------------------------
    @responses.activate
    def test_list_load_balancers_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/load_balancers')
        mock_response = '{"load_balancers": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "description": "Load balancer for glb.example.com.", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": [{"availability_zone": "us-south-1", "pools": ["0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d"]}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}], "offset": 1, "limit": 20, "count": 1, "total_count": 200, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?limit=20"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?offset=20&limit=20"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = service.list_load_balancers(
            instance_id,
            dnszone_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_load_balancers_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_load_balancers_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/load_balancers')
        mock_response = '{"load_balancers": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "description": "Load balancer for glb.example.com.", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": [{"availability_zone": "us-south-1", "pools": ["0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d"]}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}], "offset": 1, "limit": 20, "count": 1, "total_count": 200, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?limit=20"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?offset=20&limit=20"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Invoke method
        response = service.list_load_balancers(
            instance_id,
            dnszone_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_load_balancers_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_load_balancers_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/load_balancers')
        mock_response = '{"load_balancers": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "description": "Load balancer for glb.example.com.", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": [{"availability_zone": "us-south-1", "pools": ["0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d"]}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}], "offset": 1, "limit": 20, "count": 1, "total_count": 200, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?limit=20"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?offset=20&limit=20"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_load_balancers(**req_copy)



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
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/load_balancers')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "description": "Load balancer for glb.example.com.", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": [{"availability_zone": "us-south-1", "pools": ["0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d"]}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a LoadBalancerAzPoolsItem model
        load_balancer_az_pools_item_model = {}
        load_balancer_az_pools_item_model['availability_zone'] = 'us-south-1'
        load_balancer_az_pools_item_model['pools'] = ['0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d']

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        name = 'glb.example.com'
        fallback_pool = '24ccf79a-4ae0-4769-b4c8-17f8f230072e'
        default_pools = ['testString']
        description = 'Load balancer for glb.example.com.'
        enabled = True
        ttl = 120
        az_pools = [load_balancer_az_pools_item_model]
        x_correlation_id = 'testString'

        # Invoke method
        response = service.create_load_balancer(
            instance_id,
            dnszone_id,
            name=name,
            fallback_pool=fallback_pool,
            default_pools=default_pools,
            description=description,
            enabled=enabled,
            ttl=ttl,
            az_pools=az_pools,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'glb.example.com'
        assert req_body['fallback_pool'] == '24ccf79a-4ae0-4769-b4c8-17f8f230072e'
        assert req_body['default_pools'] == ['testString']
        assert req_body['description'] == 'Load balancer for glb.example.com.'
        assert req_body['enabled'] == True
        assert req_body['ttl'] == 120
        assert req_body['az_pools'] == [load_balancer_az_pools_item_model]


    #--------------------------------------------------------
    # test_create_load_balancer_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_load_balancer_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/load_balancers')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "description": "Load balancer for glb.example.com.", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": [{"availability_zone": "us-south-1", "pools": ["0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d"]}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Invoke method
        response = service.create_load_balancer(
            instance_id,
            dnszone_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_create_load_balancer_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_load_balancer_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/load_balancers')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "description": "Load balancer for glb.example.com.", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": [{"availability_zone": "us-south-1", "pools": ["0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d"]}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.create_load_balancer(**req_copy)



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
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/load_balancers/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        lb_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = service.delete_load_balancer(
            instance_id,
            dnszone_id,
            lb_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_delete_load_balancer_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_load_balancer_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/load_balancers/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        lb_id = 'testString'

        # Invoke method
        response = service.delete_load_balancer(
            instance_id,
            dnszone_id,
            lb_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_delete_load_balancer_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_load_balancer_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/load_balancers/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        lb_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
            "lb_id": lb_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_load_balancer(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_load_balancer
#-----------------------------------------------------------------------------
class TestGetLoadBalancer():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_load_balancer()
    #--------------------------------------------------------
    @responses.activate
    def test_get_load_balancer_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/load_balancers/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "description": "Load balancer for glb.example.com.", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": [{"availability_zone": "us-south-1", "pools": ["0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d"]}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        lb_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = service.get_load_balancer(
            instance_id,
            dnszone_id,
            lb_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_load_balancer_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_load_balancer_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/load_balancers/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "description": "Load balancer for glb.example.com.", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": [{"availability_zone": "us-south-1", "pools": ["0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d"]}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        lb_id = 'testString'

        # Invoke method
        response = service.get_load_balancer(
            instance_id,
            dnszone_id,
            lb_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_load_balancer_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_load_balancer_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/load_balancers/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "description": "Load balancer for glb.example.com.", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": [{"availability_zone": "us-south-1", "pools": ["0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d"]}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        lb_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
            "lb_id": lb_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_load_balancer(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_load_balancer
#-----------------------------------------------------------------------------
class TestUpdateLoadBalancer():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_load_balancer()
    #--------------------------------------------------------
    @responses.activate
    def test_update_load_balancer_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/load_balancers/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "description": "Load balancer for glb.example.com.", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": [{"availability_zone": "us-south-1", "pools": ["0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d"]}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a LoadBalancerAzPoolsItem model
        load_balancer_az_pools_item_model = {}
        load_balancer_az_pools_item_model['availability_zone'] = 'us-south-1'
        load_balancer_az_pools_item_model['pools'] = ['0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d']

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        lb_id = 'testString'
        name = 'glb.example.com'
        description = 'Load balancer for glb.example.com.'
        enabled = True
        ttl = 120
        fallback_pool = '24ccf79a-4ae0-4769-b4c8-17f8f230072e'
        default_pools = ['testString']
        az_pools = [load_balancer_az_pools_item_model]
        x_correlation_id = 'testString'

        # Invoke method
        response = service.update_load_balancer(
            instance_id,
            dnszone_id,
            lb_id,
            name=name,
            description=description,
            enabled=enabled,
            ttl=ttl,
            fallback_pool=fallback_pool,
            default_pools=default_pools,
            az_pools=az_pools,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'glb.example.com'
        assert req_body['description'] == 'Load balancer for glb.example.com.'
        assert req_body['enabled'] == True
        assert req_body['ttl'] == 120
        assert req_body['fallback_pool'] == '24ccf79a-4ae0-4769-b4c8-17f8f230072e'
        assert req_body['default_pools'] == ['testString']
        assert req_body['az_pools'] == [load_balancer_az_pools_item_model]


    #--------------------------------------------------------
    # test_update_load_balancer_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_load_balancer_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/load_balancers/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "description": "Load balancer for glb.example.com.", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": [{"availability_zone": "us-south-1", "pools": ["0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d"]}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        lb_id = 'testString'

        # Invoke method
        response = service.update_load_balancer(
            instance_id,
            dnszone_id,
            lb_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_load_balancer_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_load_balancer_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/dnszones/testString/load_balancers/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "description": "Load balancer for glb.example.com.", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": [{"availability_zone": "us-south-1", "pools": ["0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d"]}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        lb_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
            "lb_id": lb_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_load_balancer(**req_copy)



# endregion
##############################################################################
# End of Service: GlobalLoadBalancers
##############################################################################

##############################################################################
# Start of Service: Pools
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_pools
#-----------------------------------------------------------------------------
class TestListPools():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # list_pools()
    #--------------------------------------------------------
    @responses.activate
    def test_list_pools_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/pools')
        mock_response = '{"pools": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "health": true, "health_failure_reason": "health_failure_reason"}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_channel": "https://mywebsite.com/dns/webhook", "health": "HEALTHY", "healthcheck_region": "us-south", "healthcheck_subnets": ["0716-a4c0c123-594c-4ef4-ace3-a08858540b5e"], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}], "offset": 1, "limit": 20, "count": 1, "total_count": 200, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?limit=20"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?offset=20&limit=20"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = service.list_pools(
            instance_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_pools_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_pools_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/pools')
        mock_response = '{"pools": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "health": true, "health_failure_reason": "health_failure_reason"}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_channel": "https://mywebsite.com/dns/webhook", "health": "HEALTHY", "healthcheck_region": "us-south", "healthcheck_subnets": ["0716-a4c0c123-594c-4ef4-ace3-a08858540b5e"], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}], "offset": 1, "limit": 20, "count": 1, "total_count": 200, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?limit=20"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?offset=20&limit=20"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = service.list_pools(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_pools_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_pools_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/pools')
        mock_response = '{"pools": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "health": true, "health_failure_reason": "health_failure_reason"}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_channel": "https://mywebsite.com/dns/webhook", "health": "HEALTHY", "healthcheck_region": "us-south", "healthcheck_subnets": ["0716-a4c0c123-594c-4ef4-ace3-a08858540b5e"], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}], "offset": 1, "limit": 20, "count": 1, "total_count": 200, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?limit=20"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?offset=20&limit=20"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_pools(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for create_pool
#-----------------------------------------------------------------------------
class TestCreatePool():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # create_pool()
    #--------------------------------------------------------
    @responses.activate
    def test_create_pool_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/pools')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "health": true, "health_failure_reason": "health_failure_reason"}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_channel": "https://mywebsite.com/dns/webhook", "health": "HEALTHY", "healthcheck_region": "us-south", "healthcheck_subnets": ["0716-a4c0c123-594c-4ef4-ace3-a08858540b5e"], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a OriginInput model
        origin_input_model = {}
        origin_input_model['name'] = 'app-server-1'
        origin_input_model['description'] = 'description of the origin server'
        origin_input_model['address'] = '10.10.16.8'
        origin_input_model['enabled'] = True

        # Set up parameter values
        instance_id = 'testString'
        name = 'dal10-az-pool'
        origins = [origin_input_model]
        description = 'Load balancer pool for dal10 availability zone.'
        enabled = True
        healthy_origins_threshold = 1
        monitor = '7dd6841c-264e-11ea-88df-062967242a6a'
        notification_channel = 'https://mywebsite.com/dns/webhook'
        healthcheck_region = 'us-south'
        healthcheck_subnets = ['0716-a4c0c123-594c-4ef4-ace3-a08858540b5e']
        x_correlation_id = 'testString'

        # Invoke method
        response = service.create_pool(
            instance_id,
            name=name,
            origins=origins,
            description=description,
            enabled=enabled,
            healthy_origins_threshold=healthy_origins_threshold,
            monitor=monitor,
            notification_channel=notification_channel,
            healthcheck_region=healthcheck_region,
            healthcheck_subnets=healthcheck_subnets,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'dal10-az-pool'
        assert req_body['origins'] == [origin_input_model]
        assert req_body['description'] == 'Load balancer pool for dal10 availability zone.'
        assert req_body['enabled'] == True
        assert req_body['healthy_origins_threshold'] == 1
        assert req_body['monitor'] == '7dd6841c-264e-11ea-88df-062967242a6a'
        assert req_body['notification_channel'] == 'https://mywebsite.com/dns/webhook'
        assert req_body['healthcheck_region'] == 'us-south'
        assert req_body['healthcheck_subnets'] == ['0716-a4c0c123-594c-4ef4-ace3-a08858540b5e']


    #--------------------------------------------------------
    # test_create_pool_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_pool_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/pools')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "health": true, "health_failure_reason": "health_failure_reason"}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_channel": "https://mywebsite.com/dns/webhook", "health": "HEALTHY", "healthcheck_region": "us-south", "healthcheck_subnets": ["0716-a4c0c123-594c-4ef4-ace3-a08858540b5e"], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = service.create_pool(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_create_pool_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_pool_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/pools')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "health": true, "health_failure_reason": "health_failure_reason"}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_channel": "https://mywebsite.com/dns/webhook", "health": "HEALTHY", "healthcheck_region": "us-south", "healthcheck_subnets": ["0716-a4c0c123-594c-4ef4-ace3-a08858540b5e"], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.create_pool(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_pool
#-----------------------------------------------------------------------------
class TestDeletePool():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # delete_pool()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_pool_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/pools/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        pool_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = service.delete_pool(
            instance_id,
            pool_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_delete_pool_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_pool_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/pools/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        pool_id = 'testString'

        # Invoke method
        response = service.delete_pool(
            instance_id,
            pool_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_delete_pool_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_pool_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/pools/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        pool_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "pool_id": pool_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_pool(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_pool
#-----------------------------------------------------------------------------
class TestGetPool():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_pool()
    #--------------------------------------------------------
    @responses.activate
    def test_get_pool_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/pools/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "health": true, "health_failure_reason": "health_failure_reason"}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_channel": "https://mywebsite.com/dns/webhook", "health": "HEALTHY", "healthcheck_region": "us-south", "healthcheck_subnets": ["0716-a4c0c123-594c-4ef4-ace3-a08858540b5e"], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        pool_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = service.get_pool(
            instance_id,
            pool_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_pool_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_pool_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/pools/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "health": true, "health_failure_reason": "health_failure_reason"}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_channel": "https://mywebsite.com/dns/webhook", "health": "HEALTHY", "healthcheck_region": "us-south", "healthcheck_subnets": ["0716-a4c0c123-594c-4ef4-ace3-a08858540b5e"], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        pool_id = 'testString'

        # Invoke method
        response = service.get_pool(
            instance_id,
            pool_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_pool_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_pool_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/pools/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "health": true, "health_failure_reason": "health_failure_reason"}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_channel": "https://mywebsite.com/dns/webhook", "health": "HEALTHY", "healthcheck_region": "us-south", "healthcheck_subnets": ["0716-a4c0c123-594c-4ef4-ace3-a08858540b5e"], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        pool_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "pool_id": pool_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_pool(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_pool
#-----------------------------------------------------------------------------
class TestUpdatePool():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_pool()
    #--------------------------------------------------------
    @responses.activate
    def test_update_pool_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/pools/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "health": true, "health_failure_reason": "health_failure_reason"}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_channel": "https://mywebsite.com/dns/webhook", "health": "HEALTHY", "healthcheck_region": "us-south", "healthcheck_subnets": ["0716-a4c0c123-594c-4ef4-ace3-a08858540b5e"], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a OriginInput model
        origin_input_model = {}
        origin_input_model['name'] = 'app-server-1'
        origin_input_model['description'] = 'description of the origin server'
        origin_input_model['address'] = '10.10.16.8'
        origin_input_model['enabled'] = True

        # Set up parameter values
        instance_id = 'testString'
        pool_id = 'testString'
        name = 'dal10-az-pool'
        description = 'Load balancer pool for dal10 availability zone.'
        enabled = True
        healthy_origins_threshold = 1
        origins = [origin_input_model]
        monitor = '7dd6841c-264e-11ea-88df-062967242a6a'
        notification_channel = 'https://mywebsite.com/dns/webhook'
        healthcheck_region = 'us-south'
        healthcheck_subnets = ['0716-a4c0c123-594c-4ef4-ace3-a08858540b5e']
        x_correlation_id = 'testString'

        # Invoke method
        response = service.update_pool(
            instance_id,
            pool_id,
            name=name,
            description=description,
            enabled=enabled,
            healthy_origins_threshold=healthy_origins_threshold,
            origins=origins,
            monitor=monitor,
            notification_channel=notification_channel,
            healthcheck_region=healthcheck_region,
            healthcheck_subnets=healthcheck_subnets,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'dal10-az-pool'
        assert req_body['description'] == 'Load balancer pool for dal10 availability zone.'
        assert req_body['enabled'] == True
        assert req_body['healthy_origins_threshold'] == 1
        assert req_body['origins'] == [origin_input_model]
        assert req_body['monitor'] == '7dd6841c-264e-11ea-88df-062967242a6a'
        assert req_body['notification_channel'] == 'https://mywebsite.com/dns/webhook'
        assert req_body['healthcheck_region'] == 'us-south'
        assert req_body['healthcheck_subnets'] == ['0716-a4c0c123-594c-4ef4-ace3-a08858540b5e']


    #--------------------------------------------------------
    # test_update_pool_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_pool_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/pools/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "health": true, "health_failure_reason": "health_failure_reason"}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_channel": "https://mywebsite.com/dns/webhook", "health": "HEALTHY", "healthcheck_region": "us-south", "healthcheck_subnets": ["0716-a4c0c123-594c-4ef4-ace3-a08858540b5e"], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        pool_id = 'testString'

        # Invoke method
        response = service.update_pool(
            instance_id,
            pool_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_pool_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_pool_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/pools/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "health": true, "health_failure_reason": "health_failure_reason"}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_channel": "https://mywebsite.com/dns/webhook", "health": "HEALTHY", "healthcheck_region": "us-south", "healthcheck_subnets": ["0716-a4c0c123-594c-4ef4-ace3-a08858540b5e"], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        pool_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "pool_id": pool_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_pool(**req_copy)



# endregion
##############################################################################
# End of Service: Pools
##############################################################################

##############################################################################
# Start of Service: Monitors
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_monitors
#-----------------------------------------------------------------------------
class TestListMonitors():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # list_monitors()
    #--------------------------------------------------------
    @responses.activate
    def test_list_monitors_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/monitors')
        mock_response = '{"monitors": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Load balancer monitor for glb.example.com.", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}], "offset": 1, "limit": 20, "count": 1, "total_count": 200, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?limit=20"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?offset=20&limit=20"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = service.list_monitors(
            instance_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_monitors_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_monitors_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/monitors')
        mock_response = '{"monitors": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Load balancer monitor for glb.example.com.", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}], "offset": 1, "limit": 20, "count": 1, "total_count": 200, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?limit=20"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?offset=20&limit=20"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = service.list_monitors(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_monitors_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_monitors_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/monitors')
        mock_response = '{"monitors": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Load balancer monitor for glb.example.com.", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}], "offset": 1, "limit": 20, "count": 1, "total_count": 200, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?limit=20"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?offset=20&limit=20"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_monitors(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for create_monitor
#-----------------------------------------------------------------------------
class TestCreateMonitor():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # create_monitor()
    #--------------------------------------------------------
    @responses.activate
    def test_create_monitor_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/monitors')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Load balancer monitor for glb.example.com.", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a HealthcheckHeader model
        healthcheck_header_model = {}
        healthcheck_header_model['name'] = 'Host'
        healthcheck_header_model['value'] = ['origin.example.com']

        # Set up parameter values
        instance_id = 'testString'
        name = 'healthcheck-monitor'
        type = 'HTTPS'
        description = 'Load balancer monitor for glb.example.com.'
        port = 8080
        interval = 60
        retries = 2
        timeout = 5
        method = 'GET'
        path = '/health'
        headers_ = [healthcheck_header_model]
        allow_insecure = False
        expected_codes = '200'
        expected_body = 'alive'
        x_correlation_id = 'testString'

        # Invoke method
        response = service.create_monitor(
            instance_id,
            name=name,
            type=type,
            description=description,
            port=port,
            interval=interval,
            retries=retries,
            timeout=timeout,
            method=method,
            path=path,
            headers_=headers_,
            allow_insecure=allow_insecure,
            expected_codes=expected_codes,
            expected_body=expected_body,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'healthcheck-monitor'
        assert req_body['type'] == 'HTTPS'
        assert req_body['description'] == 'Load balancer monitor for glb.example.com.'
        assert req_body['port'] == 8080
        assert req_body['interval'] == 60
        assert req_body['retries'] == 2
        assert req_body['timeout'] == 5
        assert req_body['method'] == 'GET'
        assert req_body['path'] == '/health'
        assert req_body['headers'] == [healthcheck_header_model]
        assert req_body['allow_insecure'] == False
        assert req_body['expected_codes'] == '200'
        assert req_body['expected_body'] == 'alive'


    #--------------------------------------------------------
    # test_create_monitor_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_monitor_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/monitors')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Load balancer monitor for glb.example.com.", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = service.create_monitor(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_create_monitor_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_monitor_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/monitors')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Load balancer monitor for glb.example.com.", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.create_monitor(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_monitor
#-----------------------------------------------------------------------------
class TestDeleteMonitor():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # delete_monitor()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_monitor_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/monitors/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        monitor_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = service.delete_monitor(
            instance_id,
            monitor_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_delete_monitor_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_monitor_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/monitors/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        monitor_id = 'testString'

        # Invoke method
        response = service.delete_monitor(
            instance_id,
            monitor_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_delete_monitor_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_monitor_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/monitors/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        monitor_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "monitor_id": monitor_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_monitor(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_monitor
#-----------------------------------------------------------------------------
class TestGetMonitor():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_monitor()
    #--------------------------------------------------------
    @responses.activate
    def test_get_monitor_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/monitors/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Load balancer monitor for glb.example.com.", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        monitor_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = service.get_monitor(
            instance_id,
            monitor_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_monitor_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_monitor_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/monitors/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Load balancer monitor for glb.example.com.", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        monitor_id = 'testString'

        # Invoke method
        response = service.get_monitor(
            instance_id,
            monitor_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_monitor_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_monitor_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/monitors/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Load balancer monitor for glb.example.com.", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        monitor_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "monitor_id": monitor_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_monitor(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_monitor
#-----------------------------------------------------------------------------
class TestUpdateMonitor():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_monitor()
    #--------------------------------------------------------
    @responses.activate
    def test_update_monitor_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/monitors/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Load balancer monitor for glb.example.com.", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a HealthcheckHeader model
        healthcheck_header_model = {}
        healthcheck_header_model['name'] = 'Host'
        healthcheck_header_model['value'] = ['origin.example.com']

        # Set up parameter values
        instance_id = 'testString'
        monitor_id = 'testString'
        name = 'healthcheck-monitor'
        description = 'Load balancer monitor for glb.example.com.'
        type = 'HTTPS'
        port = 8080
        interval = 60
        retries = 2
        timeout = 5
        method = 'GET'
        path = '/health'
        headers_ = [healthcheck_header_model]
        allow_insecure = False
        expected_codes = '200'
        expected_body = 'alive'
        x_correlation_id = 'testString'

        # Invoke method
        response = service.update_monitor(
            instance_id,
            monitor_id,
            name=name,
            description=description,
            type=type,
            port=port,
            interval=interval,
            retries=retries,
            timeout=timeout,
            method=method,
            path=path,
            headers_=headers_,
            allow_insecure=allow_insecure,
            expected_codes=expected_codes,
            expected_body=expected_body,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'healthcheck-monitor'
        assert req_body['description'] == 'Load balancer monitor for glb.example.com.'
        assert req_body['type'] == 'HTTPS'
        assert req_body['port'] == 8080
        assert req_body['interval'] == 60
        assert req_body['retries'] == 2
        assert req_body['timeout'] == 5
        assert req_body['method'] == 'GET'
        assert req_body['path'] == '/health'
        assert req_body['headers'] == [healthcheck_header_model]
        assert req_body['allow_insecure'] == False
        assert req_body['expected_codes'] == '200'
        assert req_body['expected_body'] == 'alive'


    #--------------------------------------------------------
    # test_update_monitor_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_monitor_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/monitors/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Load balancer monitor for glb.example.com.", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        monitor_id = 'testString'

        # Invoke method
        response = service.update_monitor(
            instance_id,
            monitor_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_monitor_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_monitor_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/instances/testString/monitors/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Load balancer monitor for glb.example.com.", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        monitor_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "monitor_id": monitor_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_monitor(**req_copy)



# endregion
##############################################################################
# End of Service: Monitors
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for LoadBalancerAzPoolsItem
#-----------------------------------------------------------------------------
class TestLoadBalancerAzPoolsItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for LoadBalancerAzPoolsItem
    #--------------------------------------------------------
    def test_load_balancer_az_pools_item_serialization(self):

        # Construct a json representation of a LoadBalancerAzPoolsItem model
        load_balancer_az_pools_item_model_json = {}
        load_balancer_az_pools_item_model_json['availability_zone'] = 'us-south-1'
        load_balancer_az_pools_item_model_json['pools'] = ['0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d']

        # Construct a model instance of LoadBalancerAzPoolsItem by calling from_dict on the json representation
        load_balancer_az_pools_item_model = LoadBalancerAzPoolsItem.from_dict(load_balancer_az_pools_item_model_json)
        assert load_balancer_az_pools_item_model != False

        # Construct a model instance of LoadBalancerAzPoolsItem by calling from_dict on the json representation
        load_balancer_az_pools_item_model_dict = LoadBalancerAzPoolsItem.from_dict(load_balancer_az_pools_item_model_json).__dict__
        load_balancer_az_pools_item_model2 = LoadBalancerAzPoolsItem(**load_balancer_az_pools_item_model_dict)

        # Verify the model instances are equivalent
        assert load_balancer_az_pools_item_model == load_balancer_az_pools_item_model2

        # Convert model instance back to dict and verify no loss of data
        load_balancer_az_pools_item_model_json2 = load_balancer_az_pools_item_model.to_dict()
        assert load_balancer_az_pools_item_model_json2 == load_balancer_az_pools_item_model_json

#-----------------------------------------------------------------------------
# Test Class for FirstHref
#-----------------------------------------------------------------------------
class TestFirstHref():

    #--------------------------------------------------------
    # Test serialization/deserialization for FirstHref
    #--------------------------------------------------------
    def test_first_href_serialization(self):

        # Construct a json representation of a FirstHref model
        first_href_model_json = {}
        first_href_model_json['href'] = 'https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?limit=20'

        # Construct a model instance of FirstHref by calling from_dict on the json representation
        first_href_model = FirstHref.from_dict(first_href_model_json)
        assert first_href_model != False

        # Construct a model instance of FirstHref by calling from_dict on the json representation
        first_href_model_dict = FirstHref.from_dict(first_href_model_json).__dict__
        first_href_model2 = FirstHref(**first_href_model_dict)

        # Verify the model instances are equivalent
        assert first_href_model == first_href_model2

        # Convert model instance back to dict and verify no loss of data
        first_href_model_json2 = first_href_model.to_dict()
        assert first_href_model_json2 == first_href_model_json

#-----------------------------------------------------------------------------
# Test Class for HealthcheckHeader
#-----------------------------------------------------------------------------
class TestHealthcheckHeader():

    #--------------------------------------------------------
    # Test serialization/deserialization for HealthcheckHeader
    #--------------------------------------------------------
    def test_healthcheck_header_serialization(self):

        # Construct a json representation of a HealthcheckHeader model
        healthcheck_header_model_json = {}
        healthcheck_header_model_json['name'] = 'Host'
        healthcheck_header_model_json['value'] = ['origin.example.com']

        # Construct a model instance of HealthcheckHeader by calling from_dict on the json representation
        healthcheck_header_model = HealthcheckHeader.from_dict(healthcheck_header_model_json)
        assert healthcheck_header_model != False

        # Construct a model instance of HealthcheckHeader by calling from_dict on the json representation
        healthcheck_header_model_dict = HealthcheckHeader.from_dict(healthcheck_header_model_json).__dict__
        healthcheck_header_model2 = HealthcheckHeader(**healthcheck_header_model_dict)

        # Verify the model instances are equivalent
        assert healthcheck_header_model == healthcheck_header_model2

        # Convert model instance back to dict and verify no loss of data
        healthcheck_header_model_json2 = healthcheck_header_model.to_dict()
        assert healthcheck_header_model_json2 == healthcheck_header_model_json

#-----------------------------------------------------------------------------
# Test Class for ListLoadBalancers
#-----------------------------------------------------------------------------
class TestListLoadBalancers():

    #--------------------------------------------------------
    # Test serialization/deserialization for ListLoadBalancers
    #--------------------------------------------------------
    def test_list_load_balancers_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        load_balancer_az_pools_item_model = {} # LoadBalancerAzPoolsItem
        load_balancer_az_pools_item_model['availability_zone'] = 'us-south-1'
        load_balancer_az_pools_item_model['pools'] = ['0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d']

        first_href_model = {} # FirstHref
        first_href_model['href'] = 'https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?limit=20'

        load_balancer_model = {} # LoadBalancer
        load_balancer_model['id'] = '5365b73c-ce6f-4d6f-ad9f-d9c131b26370'
        load_balancer_model['name'] = 'glb.example.com'
        load_balancer_model['description'] = 'Load balancer for glb.example.com.'
        load_balancer_model['enabled'] = True
        load_balancer_model['ttl'] = 120
        load_balancer_model['health'] = 'DEGRADED'
        load_balancer_model['fallback_pool'] = '24ccf79a-4ae0-4769-b4c8-17f8f230072e'
        load_balancer_model['default_pools'] = ['testString']
        load_balancer_model['az_pools'] = [load_balancer_az_pools_item_model]
        load_balancer_model['created_on'] = '2019-01-01T05:20:00.12345Z'
        load_balancer_model['modified_on'] = '2019-01-01T05:20:00.12345Z'

        next_href_model = {} # NextHref
        next_href_model['href'] = 'https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?offset=20&limit=20'

        # Construct a json representation of a ListLoadBalancers model
        list_load_balancers_model_json = {}
        list_load_balancers_model_json['load_balancers'] = [load_balancer_model]
        list_load_balancers_model_json['offset'] = 1
        list_load_balancers_model_json['limit'] = 20
        list_load_balancers_model_json['count'] = 1
        list_load_balancers_model_json['total_count'] = 200
        list_load_balancers_model_json['first'] = first_href_model
        list_load_balancers_model_json['next'] = next_href_model

        # Construct a model instance of ListLoadBalancers by calling from_dict on the json representation
        list_load_balancers_model = ListLoadBalancers.from_dict(list_load_balancers_model_json)
        assert list_load_balancers_model != False

        # Construct a model instance of ListLoadBalancers by calling from_dict on the json representation
        list_load_balancers_model_dict = ListLoadBalancers.from_dict(list_load_balancers_model_json).__dict__
        list_load_balancers_model2 = ListLoadBalancers(**list_load_balancers_model_dict)

        # Verify the model instances are equivalent
        assert list_load_balancers_model == list_load_balancers_model2

        # Convert model instance back to dict and verify no loss of data
        list_load_balancers_model_json2 = list_load_balancers_model.to_dict()
        assert list_load_balancers_model_json2 == list_load_balancers_model_json

#-----------------------------------------------------------------------------
# Test Class for ListMonitors
#-----------------------------------------------------------------------------
class TestListMonitors():

    #--------------------------------------------------------
    # Test serialization/deserialization for ListMonitors
    #--------------------------------------------------------
    def test_list_monitors_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        healthcheck_header_model = {} # HealthcheckHeader
        healthcheck_header_model['name'] = 'Host'
        healthcheck_header_model['value'] = ['origin.example.com']

        first_href_model = {} # FirstHref
        first_href_model['href'] = 'https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?limit=20'

        monitor_model = {} # Monitor
        monitor_model['id'] = '5365b73c-ce6f-4d6f-ad9f-d9c131b26370'
        monitor_model['name'] = 'healthcheck-monitor'
        monitor_model['description'] = 'Load balancer monitor for glb.example.com.'
        monitor_model['type'] = 'HTTPS'
        monitor_model['port'] = 8080
        monitor_model['interval'] = 60
        monitor_model['retries'] = 2
        monitor_model['timeout'] = 5
        monitor_model['method'] = 'GET'
        monitor_model['path'] = '/health'
        monitor_model['headers'] = [healthcheck_header_model]
        monitor_model['allow_insecure'] = False
        monitor_model['expected_codes'] = '200'
        monitor_model['expected_body'] = 'alive'
        monitor_model['created_on'] = '2019-01-01T05:20:00.12345Z'
        monitor_model['modified_on'] = '2019-01-01T05:20:00.12345Z'

        next_href_model = {} # NextHref
        next_href_model['href'] = 'https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?offset=20&limit=20'

        # Construct a json representation of a ListMonitors model
        list_monitors_model_json = {}
        list_monitors_model_json['monitors'] = [monitor_model]
        list_monitors_model_json['offset'] = 1
        list_monitors_model_json['limit'] = 20
        list_monitors_model_json['count'] = 1
        list_monitors_model_json['total_count'] = 200
        list_monitors_model_json['first'] = first_href_model
        list_monitors_model_json['next'] = next_href_model

        # Construct a model instance of ListMonitors by calling from_dict on the json representation
        list_monitors_model = ListMonitors.from_dict(list_monitors_model_json)
        assert list_monitors_model != False

        # Construct a model instance of ListMonitors by calling from_dict on the json representation
        list_monitors_model_dict = ListMonitors.from_dict(list_monitors_model_json).__dict__
        list_monitors_model2 = ListMonitors(**list_monitors_model_dict)

        # Verify the model instances are equivalent
        assert list_monitors_model == list_monitors_model2

        # Convert model instance back to dict and verify no loss of data
        list_monitors_model_json2 = list_monitors_model.to_dict()
        assert list_monitors_model_json2 == list_monitors_model_json

#-----------------------------------------------------------------------------
# Test Class for ListPools
#-----------------------------------------------------------------------------
class TestListPools():

    #--------------------------------------------------------
    # Test serialization/deserialization for ListPools
    #--------------------------------------------------------
    def test_list_pools_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        origin_model = {} # Origin
        origin_model['name'] = 'app-server-1'
        origin_model['description'] = 'description of the origin server'
        origin_model['address'] = '10.10.16.8'
        origin_model['enabled'] = True
        origin_model['health'] = True
        origin_model['health_failure_reason'] = 'testString'

        first_href_model = {} # FirstHref
        first_href_model['href'] = 'https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?limit=20'

        next_href_model = {} # NextHref
        next_href_model['href'] = 'https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?offset=20&limit=20'

        pool_model = {} # Pool
        pool_model['id'] = '5365b73c-ce6f-4d6f-ad9f-d9c131b26370'
        pool_model['name'] = 'dal10-az-pool'
        pool_model['description'] = 'Load balancer pool for dal10 availability zone.'
        pool_model['enabled'] = True
        pool_model['healthy_origins_threshold'] = 1
        pool_model['origins'] = [origin_model]
        pool_model['monitor'] = '7dd6841c-264e-11ea-88df-062967242a6a'
        pool_model['notification_channel'] = 'https://mywebsite.com/dns/webhook'
        pool_model['health'] = 'HEALTHY'
        pool_model['healthcheck_region'] = 'us-south'
        pool_model['healthcheck_subnets'] = ['0716-a4c0c123-594c-4ef4-ace3-a08858540b5e']
        pool_model['created_on'] = '2019-01-01T05:20:00.12345Z'
        pool_model['modified_on'] = '2019-01-01T05:20:00.12345Z'

        # Construct a json representation of a ListPools model
        list_pools_model_json = {}
        list_pools_model_json['pools'] = [pool_model]
        list_pools_model_json['offset'] = 1
        list_pools_model_json['limit'] = 20
        list_pools_model_json['count'] = 1
        list_pools_model_json['total_count'] = 200
        list_pools_model_json['first'] = first_href_model
        list_pools_model_json['next'] = next_href_model

        # Construct a model instance of ListPools by calling from_dict on the json representation
        list_pools_model = ListPools.from_dict(list_pools_model_json)
        assert list_pools_model != False

        # Construct a model instance of ListPools by calling from_dict on the json representation
        list_pools_model_dict = ListPools.from_dict(list_pools_model_json).__dict__
        list_pools_model2 = ListPools(**list_pools_model_dict)

        # Verify the model instances are equivalent
        assert list_pools_model == list_pools_model2

        # Convert model instance back to dict and verify no loss of data
        list_pools_model_json2 = list_pools_model.to_dict()
        assert list_pools_model_json2 == list_pools_model_json

#-----------------------------------------------------------------------------
# Test Class for LoadBalancer
#-----------------------------------------------------------------------------
class TestLoadBalancer():

    #--------------------------------------------------------
    # Test serialization/deserialization for LoadBalancer
    #--------------------------------------------------------
    def test_load_balancer_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        load_balancer_az_pools_item_model = {} # LoadBalancerAzPoolsItem
        load_balancer_az_pools_item_model['availability_zone'] = 'us-south-1'
        load_balancer_az_pools_item_model['pools'] = ['0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d']

        # Construct a json representation of a LoadBalancer model
        load_balancer_model_json = {}
        load_balancer_model_json['id'] = '5365b73c-ce6f-4d6f-ad9f-d9c131b26370'
        load_balancer_model_json['name'] = 'glb.example.com'
        load_balancer_model_json['description'] = 'Load balancer for glb.example.com.'
        load_balancer_model_json['enabled'] = True
        load_balancer_model_json['ttl'] = 120
        load_balancer_model_json['health'] = 'DEGRADED'
        load_balancer_model_json['fallback_pool'] = '24ccf79a-4ae0-4769-b4c8-17f8f230072e'
        load_balancer_model_json['default_pools'] = ['testString']
        load_balancer_model_json['az_pools'] = [load_balancer_az_pools_item_model]
        load_balancer_model_json['created_on'] = '2019-01-01T05:20:00.12345Z'
        load_balancer_model_json['modified_on'] = '2019-01-01T05:20:00.12345Z'

        # Construct a model instance of LoadBalancer by calling from_dict on the json representation
        load_balancer_model = LoadBalancer.from_dict(load_balancer_model_json)
        assert load_balancer_model != False

        # Construct a model instance of LoadBalancer by calling from_dict on the json representation
        load_balancer_model_dict = LoadBalancer.from_dict(load_balancer_model_json).__dict__
        load_balancer_model2 = LoadBalancer(**load_balancer_model_dict)

        # Verify the model instances are equivalent
        assert load_balancer_model == load_balancer_model2

        # Convert model instance back to dict and verify no loss of data
        load_balancer_model_json2 = load_balancer_model.to_dict()
        assert load_balancer_model_json2 == load_balancer_model_json

#-----------------------------------------------------------------------------
# Test Class for Monitor
#-----------------------------------------------------------------------------
class TestMonitor():

    #--------------------------------------------------------
    # Test serialization/deserialization for Monitor
    #--------------------------------------------------------
    def test_monitor_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        healthcheck_header_model = {} # HealthcheckHeader
        healthcheck_header_model['name'] = 'Host'
        healthcheck_header_model['value'] = ['origin.example.com']

        # Construct a json representation of a Monitor model
        monitor_model_json = {}
        monitor_model_json['id'] = '5365b73c-ce6f-4d6f-ad9f-d9c131b26370'
        monitor_model_json['name'] = 'healthcheck-monitor'
        monitor_model_json['description'] = 'Load balancer monitor for glb.example.com.'
        monitor_model_json['type'] = 'HTTPS'
        monitor_model_json['port'] = 8080
        monitor_model_json['interval'] = 60
        monitor_model_json['retries'] = 2
        monitor_model_json['timeout'] = 5
        monitor_model_json['method'] = 'GET'
        monitor_model_json['path'] = '/health'
        monitor_model_json['headers'] = [healthcheck_header_model]
        monitor_model_json['allow_insecure'] = False
        monitor_model_json['expected_codes'] = '200'
        monitor_model_json['expected_body'] = 'alive'
        monitor_model_json['created_on'] = '2019-01-01T05:20:00.12345Z'
        monitor_model_json['modified_on'] = '2019-01-01T05:20:00.12345Z'

        # Construct a model instance of Monitor by calling from_dict on the json representation
        monitor_model = Monitor.from_dict(monitor_model_json)
        assert monitor_model != False

        # Construct a model instance of Monitor by calling from_dict on the json representation
        monitor_model_dict = Monitor.from_dict(monitor_model_json).__dict__
        monitor_model2 = Monitor(**monitor_model_dict)

        # Verify the model instances are equivalent
        assert monitor_model == monitor_model2

        # Convert model instance back to dict and verify no loss of data
        monitor_model_json2 = monitor_model.to_dict()
        assert monitor_model_json2 == monitor_model_json

#-----------------------------------------------------------------------------
# Test Class for NextHref
#-----------------------------------------------------------------------------
class TestNextHref():

    #--------------------------------------------------------
    # Test serialization/deserialization for NextHref
    #--------------------------------------------------------
    def test_next_href_serialization(self):

        # Construct a json representation of a NextHref model
        next_href_model_json = {}
        next_href_model_json['href'] = 'https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/resource_records?offset=20&limit=20'

        # Construct a model instance of NextHref by calling from_dict on the json representation
        next_href_model = NextHref.from_dict(next_href_model_json)
        assert next_href_model != False

        # Construct a model instance of NextHref by calling from_dict on the json representation
        next_href_model_dict = NextHref.from_dict(next_href_model_json).__dict__
        next_href_model2 = NextHref(**next_href_model_dict)

        # Verify the model instances are equivalent
        assert next_href_model == next_href_model2

        # Convert model instance back to dict and verify no loss of data
        next_href_model_json2 = next_href_model.to_dict()
        assert next_href_model_json2 == next_href_model_json

#-----------------------------------------------------------------------------
# Test Class for Origin
#-----------------------------------------------------------------------------
class TestOrigin():

    #--------------------------------------------------------
    # Test serialization/deserialization for Origin
    #--------------------------------------------------------
    def test_origin_serialization(self):

        # Construct a json representation of a Origin model
        origin_model_json = {}
        origin_model_json['name'] = 'app-server-1'
        origin_model_json['description'] = 'description of the origin server'
        origin_model_json['address'] = '10.10.16.8'
        origin_model_json['enabled'] = True
        origin_model_json['health'] = True
        origin_model_json['health_failure_reason'] = 'testString'

        # Construct a model instance of Origin by calling from_dict on the json representation
        origin_model = Origin.from_dict(origin_model_json)
        assert origin_model != False

        # Construct a model instance of Origin by calling from_dict on the json representation
        origin_model_dict = Origin.from_dict(origin_model_json).__dict__
        origin_model2 = Origin(**origin_model_dict)

        # Verify the model instances are equivalent
        assert origin_model == origin_model2

        # Convert model instance back to dict and verify no loss of data
        origin_model_json2 = origin_model.to_dict()
        assert origin_model_json2 == origin_model_json

#-----------------------------------------------------------------------------
# Test Class for OriginInput
#-----------------------------------------------------------------------------
class TestOriginInput():

    #--------------------------------------------------------
    # Test serialization/deserialization for OriginInput
    #--------------------------------------------------------
    def test_origin_input_serialization(self):

        # Construct a json representation of a OriginInput model
        origin_input_model_json = {}
        origin_input_model_json['name'] = 'app-server-1'
        origin_input_model_json['description'] = 'description of the origin server'
        origin_input_model_json['address'] = '10.10.16.8'
        origin_input_model_json['enabled'] = True

        # Construct a model instance of OriginInput by calling from_dict on the json representation
        origin_input_model = OriginInput.from_dict(origin_input_model_json)
        assert origin_input_model != False

        # Construct a model instance of OriginInput by calling from_dict on the json representation
        origin_input_model_dict = OriginInput.from_dict(origin_input_model_json).__dict__
        origin_input_model2 = OriginInput(**origin_input_model_dict)

        # Verify the model instances are equivalent
        assert origin_input_model == origin_input_model2

        # Convert model instance back to dict and verify no loss of data
        origin_input_model_json2 = origin_input_model.to_dict()
        assert origin_input_model_json2 == origin_input_model_json

#-----------------------------------------------------------------------------
# Test Class for Pool
#-----------------------------------------------------------------------------
class TestPool():

    #--------------------------------------------------------
    # Test serialization/deserialization for Pool
    #--------------------------------------------------------
    def test_pool_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        origin_model = {} # Origin
        origin_model['name'] = 'app-server-1'
        origin_model['description'] = 'description of the origin server'
        origin_model['address'] = '10.10.16.8'
        origin_model['enabled'] = True
        origin_model['health'] = True
        origin_model['health_failure_reason'] = 'testString'

        # Construct a json representation of a Pool model
        pool_model_json = {}
        pool_model_json['id'] = '5365b73c-ce6f-4d6f-ad9f-d9c131b26370'
        pool_model_json['name'] = 'dal10-az-pool'
        pool_model_json['description'] = 'Load balancer pool for dal10 availability zone.'
        pool_model_json['enabled'] = True
        pool_model_json['healthy_origins_threshold'] = 1
        pool_model_json['origins'] = [origin_model]
        pool_model_json['monitor'] = '7dd6841c-264e-11ea-88df-062967242a6a'
        pool_model_json['notification_channel'] = 'https://mywebsite.com/dns/webhook'
        pool_model_json['health'] = 'HEALTHY'
        pool_model_json['healthcheck_region'] = 'us-south'
        pool_model_json['healthcheck_subnets'] = ['0716-a4c0c123-594c-4ef4-ace3-a08858540b5e']
        pool_model_json['created_on'] = '2019-01-01T05:20:00.12345Z'
        pool_model_json['modified_on'] = '2019-01-01T05:20:00.12345Z'

        # Construct a model instance of Pool by calling from_dict on the json representation
        pool_model = Pool.from_dict(pool_model_json)
        assert pool_model != False

        # Construct a model instance of Pool by calling from_dict on the json representation
        pool_model_dict = Pool.from_dict(pool_model_json).__dict__
        pool_model2 = Pool(**pool_model_dict)

        # Verify the model instances are equivalent
        assert pool_model == pool_model2

        # Convert model instance back to dict and verify no loss of data
        pool_model_json2 = pool_model.to_dict()
        assert pool_model_json2 == pool_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
