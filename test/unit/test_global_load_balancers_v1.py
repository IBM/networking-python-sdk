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
import responses
from ibm_cloud_networking_services import *


service = GlobalLoadBalancersV1(
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

    #--------------------------------------------------------
    # list_load_balancers()
    #--------------------------------------------------------
    @responses.activate
    def test_list_load_balancers_all_params(self):
        # Set up mock
        url = base_url + '/instances/testString/dnszones/testString/load_balancers'
        mock_response = '{"load_balancers": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": {"us-south-1": ["us_south_1"], "us-south-2": ["us_south_2"], "us-south-3": ["us_south_3"], "us-east-1": ["us_east_1"], "us-east-2": ["us_east_2"], "us-east-3": ["us_east_3"], "eu-gb-1": ["eu_gb_1"], "eu-gb-2": ["eu_gb_2"], "eu-gb-3": ["eu_gb_3"], "eu-de-1": ["eu_de_1"], "eu-de-2": ["eu_de_2"], "eu-de-3": ["eu_de_3"], "au-syd-1": ["au_syd_1"], "au-syd-2": ["au_syd_2"], "au-syd-3": ["au_syd_3"], "jp-tok-1": ["jp_tok_1"], "jp-tok-2": ["jp_tok_2"], "jp-tok-3": ["jp_tok_3"]}, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}], "offset": 1, "limit": 20, "count": 1, "total_count": 200, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/zones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/load_balancers?page=1&per_page=20"}, "next": {"href": "https://api.pdns.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/zones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/load_balancers?page=2&per_page=20"}}'
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
            x_correlation_id=x_correlation_id
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
        url = base_url + '/instances/testString/dnszones/testString/load_balancers'
        mock_response = '{"load_balancers": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": {"us-south-1": ["us_south_1"], "us-south-2": ["us_south_2"], "us-south-3": ["us_south_3"], "us-east-1": ["us_east_1"], "us-east-2": ["us_east_2"], "us-east-3": ["us_east_3"], "eu-gb-1": ["eu_gb_1"], "eu-gb-2": ["eu_gb_2"], "eu-gb-3": ["eu_gb_3"], "eu-de-1": ["eu_de_1"], "eu-de-2": ["eu_de_2"], "eu-de-3": ["eu_de_3"], "au-syd-1": ["au_syd_1"], "au-syd-2": ["au_syd_2"], "au-syd-3": ["au_syd_3"], "jp-tok-1": ["jp_tok_1"], "jp-tok-2": ["jp_tok_2"], "jp-tok-3": ["jp_tok_3"]}, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}], "offset": 1, "limit": 20, "count": 1, "total_count": 200, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/zones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/load_balancers?page=1&per_page=20"}, "next": {"href": "https://api.pdns.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/zones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/load_balancers?page=2&per_page=20"}}'
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
            dnszone_id
        )

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
        url = base_url + '/instances/testString/dnszones/testString/load_balancers'
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": {"us-south-1": ["us_south_1"], "us-south-2": ["us_south_2"], "us-south-3": ["us_south_3"], "us-east-1": ["us_east_1"], "us-east-2": ["us_east_2"], "us-east-3": ["us_east_3"], "eu-gb-1": ["eu_gb_1"], "eu-gb-2": ["eu_gb_2"], "eu-gb-3": ["eu_gb_3"], "eu-de-1": ["eu_de_1"], "eu-de-2": ["eu_de_2"], "eu-de-3": ["eu_de_3"], "au-syd-1": ["au_syd_1"], "au-syd-2": ["au_syd_2"], "au-syd-3": ["au_syd_3"], "jp-tok-1": ["jp_tok_1"], "jp-tok-2": ["jp_tok_2"], "jp-tok-3": ["jp_tok_3"]}, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a AzPools model
        az_pools_model =  {
            'us_south_1': ['testString'],
            'us_south_2': ['testString'],
            'us_south_3': ['testString'],
            'us_east_1': ['testString'],
            'us_east_2': ['testString'],
            'us_east_3': ['testString'],
            'eu_gb_1': ['testString'],
            'eu_gb_2': ['testString'],
            'eu_gb_3': ['testString'],
            'eu_de_1': ['testString'],
            'eu_de_2': ['testString'],
            'eu_de_3': ['testString'],
            'au_syd_1': ['testString'],
            'au_syd_2': ['testString'],
            'au_syd_3': ['testString'],
            'jp_tok_1': ['testString'],
            'jp_tok_2': ['testString'],
            'jp_tok_3': ['testString']
        }

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        name = 'glb.example.com'
        fallback_pool = '24ccf79a-4ae0-4769-b4c8-17f8f230072e'
        default_pools = ['testString']
        description = 'Load balancer for glb.example.com.'
        enabled = True
        ttl = 120
        az_pools = az_pools_model
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
            x_correlation_id=x_correlation_id
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
        assert req_body['enabled'] == enabled
        assert req_body['ttl'] == ttl
        assert req_body['az_pools'] == az_pools


    #--------------------------------------------------------
    # test_create_load_balancer_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_load_balancer_required_params(self):
        # Set up mock
        url = base_url + '/instances/testString/dnszones/testString/load_balancers'
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": {"us-south-1": ["us_south_1"], "us-south-2": ["us_south_2"], "us-south-3": ["us_south_3"], "us-east-1": ["us_east_1"], "us-east-2": ["us_east_2"], "us-east-3": ["us_east_3"], "eu-gb-1": ["eu_gb_1"], "eu-gb-2": ["eu_gb_2"], "eu-gb-3": ["eu_gb_3"], "eu-de-1": ["eu_de_1"], "eu-de-2": ["eu_de_2"], "eu-de-3": ["eu_de_3"], "au-syd-1": ["au_syd_1"], "au-syd-2": ["au_syd_2"], "au-syd-3": ["au_syd_3"], "jp-tok-1": ["jp_tok_1"], "jp-tok-2": ["jp_tok_2"], "jp-tok-3": ["jp_tok_3"]}, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}'
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
            dnszone_id
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
        url = base_url + '/instances/testString/dnszones/testString/load_balancers/testString'
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
            x_correlation_id=x_correlation_id
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
        url = base_url + '/instances/testString/dnszones/testString/load_balancers/testString'
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
            lb_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


#-----------------------------------------------------------------------------
# Test Class for get_load_balancer
#-----------------------------------------------------------------------------
class TestGetLoadBalancer():

    #--------------------------------------------------------
    # get_load_balancer()
    #--------------------------------------------------------
    @responses.activate
    def test_get_load_balancer_all_params(self):
        # Set up mock
        url = base_url + '/instances/testString/dnszones/testString/load_balancers/testString'
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": {"us-south-1": ["us_south_1"], "us-south-2": ["us_south_2"], "us-south-3": ["us_south_3"], "us-east-1": ["us_east_1"], "us-east-2": ["us_east_2"], "us-east-3": ["us_east_3"], "eu-gb-1": ["eu_gb_1"], "eu-gb-2": ["eu_gb_2"], "eu-gb-3": ["eu_gb_3"], "eu-de-1": ["eu_de_1"], "eu-de-2": ["eu_de_2"], "eu-de-3": ["eu_de_3"], "au-syd-1": ["au_syd_1"], "au-syd-2": ["au_syd_2"], "au-syd-3": ["au_syd_3"], "jp-tok-1": ["jp_tok_1"], "jp-tok-2": ["jp_tok_2"], "jp-tok-3": ["jp_tok_3"]}, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}'
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
            x_correlation_id=x_correlation_id
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
        url = base_url + '/instances/testString/dnszones/testString/load_balancers/testString'
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": {"us-south-1": ["us_south_1"], "us-south-2": ["us_south_2"], "us-south-3": ["us_south_3"], "us-east-1": ["us_east_1"], "us-east-2": ["us_east_2"], "us-east-3": ["us_east_3"], "eu-gb-1": ["eu_gb_1"], "eu-gb-2": ["eu_gb_2"], "eu-gb-3": ["eu_gb_3"], "eu-de-1": ["eu_de_1"], "eu-de-2": ["eu_de_2"], "eu-de-3": ["eu_de_3"], "au-syd-1": ["au_syd_1"], "au-syd-2": ["au_syd_2"], "au-syd-3": ["au_syd_3"], "jp-tok-1": ["jp_tok_1"], "jp-tok-2": ["jp_tok_2"], "jp-tok-3": ["jp_tok_3"]}, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}'
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
            lb_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for update_load_balancer
#-----------------------------------------------------------------------------
class TestUpdateLoadBalancer():

    #--------------------------------------------------------
    # update_load_balancer()
    #--------------------------------------------------------
    @responses.activate
    def test_update_load_balancer_all_params(self):
        # Set up mock
        url = base_url + '/instances/testString/dnszones/testString/load_balancers/testString'
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": {"us-south-1": ["us_south_1"], "us-south-2": ["us_south_2"], "us-south-3": ["us_south_3"], "us-east-1": ["us_east_1"], "us-east-2": ["us_east_2"], "us-east-3": ["us_east_3"], "eu-gb-1": ["eu_gb_1"], "eu-gb-2": ["eu_gb_2"], "eu-gb-3": ["eu_gb_3"], "eu-de-1": ["eu_de_1"], "eu-de-2": ["eu_de_2"], "eu-de-3": ["eu_de_3"], "au-syd-1": ["au_syd_1"], "au-syd-2": ["au_syd_2"], "au-syd-3": ["au_syd_3"], "jp-tok-1": ["jp_tok_1"], "jp-tok-2": ["jp_tok_2"], "jp-tok-3": ["jp_tok_3"]}, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a AzPools model
        az_pools_model =  {
            'us_south_1': ['testString'],
            'us_south_2': ['testString'],
            'us_south_3': ['testString'],
            'us_east_1': ['testString'],
            'us_east_2': ['testString'],
            'us_east_3': ['testString'],
            'eu_gb_1': ['testString'],
            'eu_gb_2': ['testString'],
            'eu_gb_3': ['testString'],
            'eu_de_1': ['testString'],
            'eu_de_2': ['testString'],
            'eu_de_3': ['testString'],
            'au_syd_1': ['testString'],
            'au_syd_2': ['testString'],
            'au_syd_3': ['testString'],
            'jp_tok_1': ['testString'],
            'jp_tok_2': ['testString'],
            'jp_tok_3': ['testString']
        }

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
        az_pools = az_pools_model
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
            x_correlation_id=x_correlation_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['description'] == description
        assert req_body['enabled'] == enabled
        assert req_body['ttl'] == ttl
        assert req_body['fallback_pool'] == fallback_pool
        assert req_body['default_pools'] == default_pools
        assert req_body['az_pools'] == az_pools


    #--------------------------------------------------------
    # test_update_load_balancer_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_load_balancer_required_params(self):
        # Set up mock
        url = base_url + '/instances/testString/dnszones/testString/load_balancers/testString'
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": {"us-south-1": ["us_south_1"], "us-south-2": ["us_south_2"], "us-south-3": ["us_south_3"], "us-east-1": ["us_east_1"], "us-east-2": ["us_east_2"], "us-east-3": ["us_east_3"], "eu-gb-1": ["eu_gb_1"], "eu-gb-2": ["eu_gb_2"], "eu-gb-3": ["eu_gb_3"], "eu-de-1": ["eu_de_1"], "eu-de-2": ["eu_de_2"], "eu-de-3": ["eu_de_3"], "au-syd-1": ["au_syd_1"], "au-syd-2": ["au_syd_2"], "au-syd-3": ["au_syd_3"], "jp-tok-1": ["jp_tok_1"], "jp-tok-2": ["jp_tok_2"], "jp-tok-3": ["jp_tok_3"]}, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}'
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
            lb_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


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

    #--------------------------------------------------------
    # list_pools()
    #--------------------------------------------------------
    @responses.activate
    def test_list_pools_all_params(self):
        # Set up mock
        url = base_url + '/instances/testString/pools'
        mock_response = '{"pools": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "minimum_origins": 1, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "weight": 1}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_type": "email", "notification_channel": "xxx@mail.example.com", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}], "offset": 1, "limit": 20, "count": 1, "total_count": 200, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/zones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/load_balancers?page=1&per_page=20"}, "next": {"href": "https://api.pdns.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/zones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/load_balancers?page=2&per_page=20"}}'
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
            x_correlation_id=x_correlation_id
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
        url = base_url + '/instances/testString/pools'
        mock_response = '{"pools": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "minimum_origins": 1, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "weight": 1}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_type": "email", "notification_channel": "xxx@mail.example.com", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}], "offset": 1, "limit": 20, "count": 1, "total_count": 200, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/zones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/load_balancers?page=1&per_page=20"}, "next": {"href": "https://api.pdns.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/zones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/load_balancers?page=2&per_page=20"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = service.list_pools(
            instance_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for create_pool
#-----------------------------------------------------------------------------
class TestCreatePool():

    #--------------------------------------------------------
    # create_pool()
    #--------------------------------------------------------
    @responses.activate
    def test_create_pool_all_params(self):
        # Set up mock
        url = base_url + '/instances/testString/pools'
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "minimum_origins": 1, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "weight": 1}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_type": "email", "notification_channel": "xxx@mail.example.com", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Origin model
        origin_model =  {
            'name': 'app-server-1',
            'description': 'description of the origin server',
            'address': '10.10.16.8',
            'enabled': True,
            'weight': 1
        }

        # Set up parameter values
        instance_id = 'testString'
        name = 'dal10-az-pool'
        origins = [origin_model]
        description = 'Load balancer pool for dal10 availability zone.'
        enabled = True
        minimum_origins = 1
        healthy_origins_threshold = 1
        monitor = '7dd6841c-264e-11ea-88df-062967242a6a'
        notification_type = 'email'
        notification_channel = 'xxx@mail.example.com'
        x_correlation_id = 'testString'

        # Invoke method
        response = service.create_pool(
            instance_id,
            name=name,
            origins=origins,
            description=description,
            enabled=enabled,
            minimum_origins=minimum_origins,
            healthy_origins_threshold=healthy_origins_threshold,
            monitor=monitor,
            notification_type=notification_type,
            notification_channel=notification_channel,
            x_correlation_id=x_correlation_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['origins'] == origins
        assert req_body['description'] == description
        assert req_body['enabled'] == enabled
        assert req_body['minimum_origins'] == minimum_origins
        assert req_body['healthy_origins_threshold'] == healthy_origins_threshold
        assert req_body['monitor'] == monitor
        assert req_body['notification_type'] == notification_type
        assert req_body['notification_channel'] == notification_channel


    #--------------------------------------------------------
    # test_create_pool_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_pool_required_params(self):
        # Set up mock
        url = base_url + '/instances/testString/pools'
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "minimum_origins": 1, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "weight": 1}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_type": "email", "notification_channel": "xxx@mail.example.com", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = service.create_pool(
            instance_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for delete_pool
#-----------------------------------------------------------------------------
class TestDeletePool():

    #--------------------------------------------------------
    # delete_pool()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_pool_all_params(self):
        # Set up mock
        url = base_url + '/instances/testString/pools/testString'
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
            x_correlation_id=x_correlation_id
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
        url = base_url + '/instances/testString/pools/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        pool_id = 'testString'

        # Invoke method
        response = service.delete_pool(
            instance_id,
            pool_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


#-----------------------------------------------------------------------------
# Test Class for get_pool
#-----------------------------------------------------------------------------
class TestGetPool():

    #--------------------------------------------------------
    # get_pool()
    #--------------------------------------------------------
    @responses.activate
    def test_get_pool_all_params(self):
        # Set up mock
        url = base_url + '/instances/testString/pools/testString'
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "minimum_origins": 1, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "weight": 1}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_type": "email", "notification_channel": "xxx@mail.example.com", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}'
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
            x_correlation_id=x_correlation_id
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
        url = base_url + '/instances/testString/pools/testString'
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "minimum_origins": 1, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "weight": 1}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_type": "email", "notification_channel": "xxx@mail.example.com", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}'
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
            pool_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for update_pool
#-----------------------------------------------------------------------------
class TestUpdatePool():

    #--------------------------------------------------------
    # update_pool()
    #--------------------------------------------------------
    @responses.activate
    def test_update_pool_all_params(self):
        # Set up mock
        url = base_url + '/instances/testString/pools/testString'
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "minimum_origins": 1, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "weight": 1}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_type": "email", "notification_channel": "xxx@mail.example.com", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Origin model
        origin_model =  {
            'name': 'app-server-1',
            'description': 'description of the origin server',
            'address': '10.10.16.8',
            'enabled': True,
            'weight': 1
        }

        # Set up parameter values
        instance_id = 'testString'
        pool_id = 'testString'
        name = 'dal10-az-pool'
        description = 'Load balancer pool for dal10 availability zone.'
        enabled = True
        minimum_origins = 1
        healthy_origins_threshold = 1
        origins = [origin_model]
        monitor = '7dd6841c-264e-11ea-88df-062967242a6a'
        notification_type = 'email'
        notification_channel = 'xxx@mail.example.com'
        x_correlation_id = 'testString'

        # Invoke method
        response = service.update_pool(
            instance_id,
            pool_id,
            name=name,
            description=description,
            enabled=enabled,
            minimum_origins=minimum_origins,
            healthy_origins_threshold=healthy_origins_threshold,
            origins=origins,
            monitor=monitor,
            notification_type=notification_type,
            notification_channel=notification_channel,
            x_correlation_id=x_correlation_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['description'] == description
        assert req_body['enabled'] == enabled
        assert req_body['minimum_origins'] == minimum_origins
        assert req_body['healthy_origins_threshold'] == healthy_origins_threshold
        assert req_body['origins'] == origins
        assert req_body['monitor'] == monitor
        assert req_body['notification_type'] == notification_type
        assert req_body['notification_channel'] == notification_channel


    #--------------------------------------------------------
    # test_update_pool_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_pool_required_params(self):
        # Set up mock
        url = base_url + '/instances/testString/pools/testString'
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "minimum_origins": 1, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "weight": 1}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_type": "email", "notification_channel": "xxx@mail.example.com", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}'
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
            pool_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


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

    #--------------------------------------------------------
    # list_monitors()
    #--------------------------------------------------------
    @responses.activate
    def test_list_monitors_all_params(self):
        # Set up mock
        url = base_url + '/instances/testString/monitors'
        mock_response = '{"monitors": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Health check monitor", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "follow_redirects": false, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}], "offset": 1, "limit": 20, "count": 1, "total_count": 200, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/zones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/load_balancers?page=1&per_page=20"}, "next": {"href": "https://api.pdns.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/zones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/load_balancers?page=2&per_page=20"}}'
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
            x_correlation_id=x_correlation_id
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
        url = base_url + '/instances/testString/monitors'
        mock_response = '{"monitors": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Health check monitor", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "follow_redirects": false, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}], "offset": 1, "limit": 20, "count": 1, "total_count": 200, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/zones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/load_balancers?page=1&per_page=20"}, "next": {"href": "https://api.pdns.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/zones/example.com:d04d3a7a-7f6d-47d4-b811-08c5478fa1a4/load_balancers?page=2&per_page=20"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = service.list_monitors(
            instance_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for create_monitor
#-----------------------------------------------------------------------------
class TestCreateMonitor():

    #--------------------------------------------------------
    # create_monitor()
    #--------------------------------------------------------
    @responses.activate
    def test_create_monitor_all_params(self):
        # Set up mock
        url = base_url + '/instances/testString/monitors'
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Health check monitor", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "follow_redirects": false, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a HealthcheckHeader model
        healthcheck_header_model =  {
            'name': 'Host',
            'value': ['origin.example.com']
        }

        # Set up parameter values
        instance_id = 'testString'
        name = 'healthcheck-monitor'
        type = 'HTTPS'
        description = 'Health check monitor'
        port = 8080
        interval = 60
        retries = 2
        timeout = 5
        method = 'GET'
        path = '/health'
        headers = [healthcheck_header_model]
        allow_insecure = False
        expected_codes = '200'
        expected_body = 'alive'
        follow_redirects = False
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
            headers=headers,
            allow_insecure=allow_insecure,
            expected_codes=expected_codes,
            expected_body=expected_body,
            follow_redirects=follow_redirects,
            x_correlation_id=x_correlation_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['type'] == type
        assert req_body['description'] == description
        assert req_body['port'] == port
        assert req_body['interval'] == interval
        assert req_body['retries'] == retries
        assert req_body['timeout'] == timeout
        assert req_body['method'] == method
        assert req_body['path'] == path
        assert req_body['headers'] == headers
        assert req_body['allow_insecure'] == allow_insecure
        assert req_body['expected_codes'] == expected_codes
        assert req_body['expected_body'] == expected_body
        assert req_body['follow_redirects'] == follow_redirects


    #--------------------------------------------------------
    # test_create_monitor_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_monitor_required_params(self):
        # Set up mock
        url = base_url + '/instances/testString/monitors'
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Health check monitor", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "follow_redirects": false, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = service.create_monitor(
            instance_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for delete_monitor
#-----------------------------------------------------------------------------
class TestDeleteMonitor():

    #--------------------------------------------------------
    # delete_monitor()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_monitor_all_params(self):
        # Set up mock
        url = base_url + '/instances/testString/monitors/testString'
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
            x_correlation_id=x_correlation_id
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
        url = base_url + '/instances/testString/monitors/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        monitor_id = 'testString'

        # Invoke method
        response = service.delete_monitor(
            instance_id,
            monitor_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


#-----------------------------------------------------------------------------
# Test Class for get_monitor
#-----------------------------------------------------------------------------
class TestGetMonitor():

    #--------------------------------------------------------
    # get_monitor()
    #--------------------------------------------------------
    @responses.activate
    def test_get_monitor_all_params(self):
        # Set up mock
        url = base_url + '/instances/testString/monitors/testString'
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Health check monitor", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "follow_redirects": false, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}'
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
            x_correlation_id=x_correlation_id
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
        url = base_url + '/instances/testString/monitors/testString'
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Health check monitor", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "follow_redirects": false, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}'
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
            monitor_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for update_monitor
#-----------------------------------------------------------------------------
class TestUpdateMonitor():

    #--------------------------------------------------------
    # update_monitor()
    #--------------------------------------------------------
    @responses.activate
    def test_update_monitor_all_params(self):
        # Set up mock
        url = base_url + '/instances/testString/monitors/testString'
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Health check monitor", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "follow_redirects": false, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a HealthcheckHeader model
        healthcheck_header_model =  {
            'name': 'Host',
            'value': ['origin.example.com']
        }

        # Set up parameter values
        instance_id = 'testString'
        monitor_id = 'testString'
        name = 'healthcheck-monitor'
        description = 'Health check monitor'
        type = 'HTTPS'
        port = 8080
        interval = 60
        retries = 2
        timeout = 5
        method = 'GET'
        path = '/health'
        headers = [healthcheck_header_model]
        allow_insecure = False
        expected_codes = '200'
        expected_body = 'alive'
        follow_redirects = False
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
            headers=headers,
            allow_insecure=allow_insecure,
            expected_codes=expected_codes,
            expected_body=expected_body,
            follow_redirects=follow_redirects,
            x_correlation_id=x_correlation_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['description'] == description
        assert req_body['type'] == type
        assert req_body['port'] == port
        assert req_body['interval'] == interval
        assert req_body['retries'] == retries
        assert req_body['timeout'] == timeout
        assert req_body['method'] == method
        assert req_body['path'] == path
        assert req_body['headers'] == headers
        assert req_body['allow_insecure'] == allow_insecure
        assert req_body['expected_codes'] == expected_codes
        assert req_body['expected_body'] == expected_body
        assert req_body['follow_redirects'] == follow_redirects


    #--------------------------------------------------------
    # test_update_monitor_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_monitor_required_params(self):
        # Set up mock
        url = base_url + '/instances/testString/monitors/testString'
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Health check monitor", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "follow_redirects": false, "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00"}'
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
            monitor_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: Monitors
##############################################################################

