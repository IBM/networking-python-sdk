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
from ibm_cloud_networking_services.global_load_balancer_pools_v0 import *

crn = 'testString'

service = GlobalLoadBalancerPoolsV0(
    authenticator=NoAuthAuthenticator(),
    crn=crn
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: GlobalLoadBalancerPool
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_all_load_balancer_pools
#-----------------------------------------------------------------------------
class TestListAllLoadBalancerPools():

    #--------------------------------------------------------
    # list_all_load_balancer_pools()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_load_balancer_pools_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/load_balancers/pools'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "17b5962d775c646f3f9725cbc7a53df4", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Primary data center - Provider XYZ", "name": "primary-dc-1", "enabled": true, "healthy": true, "monitor": "f1aba936b94213e5b8dca0c0dbf1f9cc", "origins": [{"name": "app-server-1", "address": "0.0.0.0", "enabled": true, "healthy": true}], "notification_email": "someone@example.com"}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_all_load_balancer_pools()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_all_load_balancer_pools_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_load_balancer_pools_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/load_balancers/pools'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "17b5962d775c646f3f9725cbc7a53df4", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Primary data center - Provider XYZ", "name": "primary-dc-1", "enabled": true, "healthy": true, "monitor": "f1aba936b94213e5b8dca0c0dbf1f9cc", "origins": [{"name": "app-server-1", "address": "0.0.0.0", "enabled": true, "healthy": true}], "notification_email": "someone@example.com"}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_all_load_balancer_pools()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for create_load_balancer_pool
#-----------------------------------------------------------------------------
class TestCreateLoadBalancerPool():

    #--------------------------------------------------------
    # create_load_balancer_pool()
    #--------------------------------------------------------
    @responses.activate
    def test_create_load_balancer_pool_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/load_balancers/pools'
        mock_response = '{"id": "17b5962d775c646f3f9725cbc7a53df4", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Primary data center - Provider XYZ", "name": "primary-dc-1", "enabled": true, "healthy": true, "monitor": "f1aba936b94213e5b8dca0c0dbf1f9cc", "origins": [{"name": "app-server-1", "address": "0.0.0.0", "enabled": true, "healthy": true}], "notification_email": "someone@example.com"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a LoadBalancerPoolReqOriginsItem model
        load_balancer_pool_req_origins_item_model =  {
            'name': 'app-server-1',
            'address': '0.0.0.0',
            'enabled': True
        }

        # Set up parameter values
        name = 'primary-dc-1'
        check_regions = ['WNAM']
        origins = [load_balancer_pool_req_origins_item_model]
        description = 'Primary data center - Provider XYZ'
        minimum_origins = 2
        enabled = True
        monitor = 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        notification_email = 'someone@example.com'

        # Invoke method
        response = service.create_load_balancer_pool(
            name=name,
            check_regions=check_regions,
            origins=origins,
            description=description,
            minimum_origins=minimum_origins,
            enabled=enabled,
            monitor=monitor,
            notification_email=notification_email,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['check_regions'] == check_regions
        assert req_body['origins'] == origins
        assert req_body['description'] == description
        assert req_body['minimum_origins'] == minimum_origins
        assert req_body['enabled'] == enabled
        assert req_body['monitor'] == monitor
        assert req_body['notification_email'] == notification_email


    #--------------------------------------------------------
    # test_create_load_balancer_pool_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_load_balancer_pool_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/load_balancers/pools'
        mock_response = '{"id": "17b5962d775c646f3f9725cbc7a53df4", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Primary data center - Provider XYZ", "name": "primary-dc-1", "enabled": true, "healthy": true, "monitor": "f1aba936b94213e5b8dca0c0dbf1f9cc", "origins": [{"name": "app-server-1", "address": "0.0.0.0", "enabled": true, "healthy": true}], "notification_email": "someone@example.com"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.create_load_balancer_pool()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_load_balancer_pool
#-----------------------------------------------------------------------------
class TestGetLoadBalancerPool():

    #--------------------------------------------------------
    # get_load_balancer_pool()
    #--------------------------------------------------------
    @responses.activate
    def test_get_load_balancer_pool_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/load_balancers/pools/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "17b5962d775c646f3f9725cbc7a53df4", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Primary data center - Provider XYZ", "name": "primary-dc-1", "enabled": true, "healthy": true, "monitor": "f1aba936b94213e5b8dca0c0dbf1f9cc", "origins": [{"name": "app-server-1", "address": "0.0.0.0", "enabled": true, "healthy": true}], "notification_email": "someone@example.com"}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pool_identifier = 'testString'

        # Invoke method
        response = service.get_load_balancer_pool(
            pool_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_load_balancer_pool_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_load_balancer_pool_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/load_balancers/pools/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "17b5962d775c646f3f9725cbc7a53df4", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Primary data center - Provider XYZ", "name": "primary-dc-1", "enabled": true, "healthy": true, "monitor": "f1aba936b94213e5b8dca0c0dbf1f9cc", "origins": [{"name": "app-server-1", "address": "0.0.0.0", "enabled": true, "healthy": true}], "notification_email": "someone@example.com"}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pool_identifier = 'testString'

        # Invoke method
        response = service.get_load_balancer_pool(
            pool_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for delete_load_balancer_pool
#-----------------------------------------------------------------------------
class TestDeleteLoadBalancerPool():

    #--------------------------------------------------------
    # delete_load_balancer_pool()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_load_balancer_pool_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/load_balancers/pools/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "17b5962d775c646f3f9725cbc7a53df4"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pool_identifier = 'testString'

        # Invoke method
        response = service.delete_load_balancer_pool(
            pool_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_load_balancer_pool_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_load_balancer_pool_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/load_balancers/pools/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "17b5962d775c646f3f9725cbc7a53df4"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pool_identifier = 'testString'

        # Invoke method
        response = service.delete_load_balancer_pool(
            pool_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for edit_load_balancer_pool
#-----------------------------------------------------------------------------
class TestEditLoadBalancerPool():

    #--------------------------------------------------------
    # edit_load_balancer_pool()
    #--------------------------------------------------------
    @responses.activate
    def test_edit_load_balancer_pool_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/load_balancers/pools/testString'
        mock_response = '{"name": "primary-dc-1", "check_regions": ["WNAM"], "origins": [{"name": "app-server-1", "address": "0.0.0.0", "enabled": true}], "description": "Primary data center - Provider XYZ", "minimum_origins": 2, "enabled": true, "monitor": "f1aba936b94213e5b8dca0c0dbf1f9cc", "notification_email": "someone@example.com"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a LoadBalancerPoolReqOriginsItem model
        load_balancer_pool_req_origins_item_model =  {
            'name': 'app-server-1',
            'address': '0.0.0.0',
            'enabled': True
        }

        # Set up parameter values
        pool_identifier = 'testString'
        name = 'primary-dc-1'
        check_regions = ['WNAM']
        origins = [load_balancer_pool_req_origins_item_model]
        description = 'Primary data center - Provider XYZ'
        minimum_origins = 2
        enabled = True
        monitor = 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        notification_email = 'someone@example.com'

        # Invoke method
        response = service.edit_load_balancer_pool(
            pool_identifier,
            name=name,
            check_regions=check_regions,
            origins=origins,
            description=description,
            minimum_origins=minimum_origins,
            enabled=enabled,
            monitor=monitor,
            notification_email=notification_email,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == name
        assert req_body['check_regions'] == check_regions
        assert req_body['origins'] == origins
        assert req_body['description'] == description
        assert req_body['minimum_origins'] == minimum_origins
        assert req_body['enabled'] == enabled
        assert req_body['monitor'] == monitor
        assert req_body['notification_email'] == notification_email


    #--------------------------------------------------------
    # test_edit_load_balancer_pool_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_edit_load_balancer_pool_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/load_balancers/pools/testString'
        mock_response = '{"name": "primary-dc-1", "check_regions": ["WNAM"], "origins": [{"name": "app-server-1", "address": "0.0.0.0", "enabled": true}], "description": "Primary data center - Provider XYZ", "minimum_origins": 2, "enabled": true, "monitor": "f1aba936b94213e5b8dca0c0dbf1f9cc", "notification_email": "someone@example.com"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pool_identifier = 'testString'

        # Invoke method
        response = service.edit_load_balancer_pool(
            pool_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GlobalLoadBalancerPool
##############################################################################

