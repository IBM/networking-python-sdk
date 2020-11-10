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

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # list_all_load_balancer_pools()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_load_balancer_pools_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/load_balancers/pools')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "17b5962d775c646f3f9725cbc7a53df4", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Primary data center - Provider XYZ", "name": "primary-dc-1", "enabled": true, "healthy": true, "monitor": "f1aba936b94213e5b8dca0c0dbf1f9cc", "minimum_origins": 1, "check_regions": ["WNAM"], "origins": [{"name": "app-server-1", "address": "0.0.0.0", "enabled": true, "healthy": true, "weight": 1, "disabled_at": "2014-01-01T05:20:00.12345Z", "failure_reason": "HTTP Timeout occured"}], "notification_email": "someone@example.com"}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
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
    # test_list_all_load_balancer_pools_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_load_balancer_pools_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/load_balancers/pools')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "17b5962d775c646f3f9725cbc7a53df4", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Primary data center - Provider XYZ", "name": "primary-dc-1", "enabled": true, "healthy": true, "monitor": "f1aba936b94213e5b8dca0c0dbf1f9cc", "minimum_origins": 1, "check_regions": ["WNAM"], "origins": [{"name": "app-server-1", "address": "0.0.0.0", "enabled": true, "healthy": true, "weight": 1, "disabled_at": "2014-01-01T05:20:00.12345Z", "failure_reason": "HTTP Timeout occured"}], "notification_email": "someone@example.com"}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
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
                service.list_all_load_balancer_pools(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for create_load_balancer_pool
#-----------------------------------------------------------------------------
class TestCreateLoadBalancerPool():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # create_load_balancer_pool()
    #--------------------------------------------------------
    @responses.activate
    def test_create_load_balancer_pool_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/load_balancers/pools')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "17b5962d775c646f3f9725cbc7a53df4", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Primary data center - Provider XYZ", "name": "primary-dc-1", "enabled": true, "healthy": true, "monitor": "f1aba936b94213e5b8dca0c0dbf1f9cc", "minimum_origins": 1, "check_regions": ["WNAM"], "origins": [{"name": "app-server-1", "address": "0.0.0.0", "enabled": true, "healthy": true, "weight": 1, "disabled_at": "2014-01-01T05:20:00.12345Z", "failure_reason": "HTTP Timeout occured"}], "notification_email": "someone@example.com"}, "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a LoadBalancerPoolReqOriginsItem model
        load_balancer_pool_req_origins_item_model = {}
        load_balancer_pool_req_origins_item_model['name'] = 'app-server-1'
        load_balancer_pool_req_origins_item_model['address'] = '0.0.0.0'
        load_balancer_pool_req_origins_item_model['enabled'] = True
        load_balancer_pool_req_origins_item_model['weight'] = 1

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
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'primary-dc-1'
        assert req_body['check_regions'] == ['WNAM']
        assert req_body['origins'] == [load_balancer_pool_req_origins_item_model]
        assert req_body['description'] == 'Primary data center - Provider XYZ'
        assert req_body['minimum_origins'] == 2
        assert req_body['enabled'] == True
        assert req_body['monitor'] == 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        assert req_body['notification_email'] == 'someone@example.com'


    #--------------------------------------------------------
    # test_create_load_balancer_pool_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_load_balancer_pool_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/load_balancers/pools')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "17b5962d775c646f3f9725cbc7a53df4", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Primary data center - Provider XYZ", "name": "primary-dc-1", "enabled": true, "healthy": true, "monitor": "f1aba936b94213e5b8dca0c0dbf1f9cc", "minimum_origins": 1, "check_regions": ["WNAM"], "origins": [{"name": "app-server-1", "address": "0.0.0.0", "enabled": true, "healthy": true, "weight": 1, "disabled_at": "2014-01-01T05:20:00.12345Z", "failure_reason": "HTTP Timeout occured"}], "notification_email": "someone@example.com"}, "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
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


    #--------------------------------------------------------
    # test_create_load_balancer_pool_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_load_balancer_pool_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/load_balancers/pools')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "17b5962d775c646f3f9725cbc7a53df4", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Primary data center - Provider XYZ", "name": "primary-dc-1", "enabled": true, "healthy": true, "monitor": "f1aba936b94213e5b8dca0c0dbf1f9cc", "minimum_origins": 1, "check_regions": ["WNAM"], "origins": [{"name": "app-server-1", "address": "0.0.0.0", "enabled": true, "healthy": true, "weight": 1, "disabled_at": "2014-01-01T05:20:00.12345Z", "failure_reason": "HTTP Timeout occured"}], "notification_email": "someone@example.com"}, "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
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
                service.create_load_balancer_pool(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_load_balancer_pool
#-----------------------------------------------------------------------------
class TestGetLoadBalancerPool():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_load_balancer_pool()
    #--------------------------------------------------------
    @responses.activate
    def test_get_load_balancer_pool_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/load_balancers/pools/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "17b5962d775c646f3f9725cbc7a53df4", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Primary data center - Provider XYZ", "name": "primary-dc-1", "enabled": true, "healthy": true, "monitor": "f1aba936b94213e5b8dca0c0dbf1f9cc", "minimum_origins": 1, "check_regions": ["WNAM"], "origins": [{"name": "app-server-1", "address": "0.0.0.0", "enabled": true, "healthy": true, "weight": 1, "disabled_at": "2014-01-01T05:20:00.12345Z", "failure_reason": "HTTP Timeout occured"}], "notification_email": "someone@example.com"}, "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pool_identifier = 'testString'

        # Invoke method
        response = service.get_load_balancer_pool(
            pool_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_load_balancer_pool_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_load_balancer_pool_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/load_balancers/pools/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "17b5962d775c646f3f9725cbc7a53df4", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Primary data center - Provider XYZ", "name": "primary-dc-1", "enabled": true, "healthy": true, "monitor": "f1aba936b94213e5b8dca0c0dbf1f9cc", "minimum_origins": 1, "check_regions": ["WNAM"], "origins": [{"name": "app-server-1", "address": "0.0.0.0", "enabled": true, "healthy": true, "weight": 1, "disabled_at": "2014-01-01T05:20:00.12345Z", "failure_reason": "HTTP Timeout occured"}], "notification_email": "someone@example.com"}, "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pool_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pool_identifier": pool_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_load_balancer_pool(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_load_balancer_pool
#-----------------------------------------------------------------------------
class TestDeleteLoadBalancerPool():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # delete_load_balancer_pool()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_load_balancer_pool_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/load_balancers/pools/testString')
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
            pool_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_load_balancer_pool_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_load_balancer_pool_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/load_balancers/pools/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "17b5962d775c646f3f9725cbc7a53df4"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pool_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pool_identifier": pool_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_load_balancer_pool(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for edit_load_balancer_pool
#-----------------------------------------------------------------------------
class TestEditLoadBalancerPool():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # edit_load_balancer_pool()
    #--------------------------------------------------------
    @responses.activate
    def test_edit_load_balancer_pool_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/load_balancers/pools/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "17b5962d775c646f3f9725cbc7a53df4", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Primary data center - Provider XYZ", "name": "primary-dc-1", "enabled": true, "healthy": true, "monitor": "f1aba936b94213e5b8dca0c0dbf1f9cc", "minimum_origins": 1, "check_regions": ["WNAM"], "origins": [{"name": "app-server-1", "address": "0.0.0.0", "enabled": true, "healthy": true, "weight": 1, "disabled_at": "2014-01-01T05:20:00.12345Z", "failure_reason": "HTTP Timeout occured"}], "notification_email": "someone@example.com"}, "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a LoadBalancerPoolReqOriginsItem model
        load_balancer_pool_req_origins_item_model = {}
        load_balancer_pool_req_origins_item_model['name'] = 'app-server-1'
        load_balancer_pool_req_origins_item_model['address'] = '0.0.0.0'
        load_balancer_pool_req_origins_item_model['enabled'] = True
        load_balancer_pool_req_origins_item_model['weight'] = 1

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
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'primary-dc-1'
        assert req_body['check_regions'] == ['WNAM']
        assert req_body['origins'] == [load_balancer_pool_req_origins_item_model]
        assert req_body['description'] == 'Primary data center - Provider XYZ'
        assert req_body['minimum_origins'] == 2
        assert req_body['enabled'] == True
        assert req_body['monitor'] == 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        assert req_body['notification_email'] == 'someone@example.com'


    #--------------------------------------------------------
    # test_edit_load_balancer_pool_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_edit_load_balancer_pool_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/load_balancers/pools/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "17b5962d775c646f3f9725cbc7a53df4", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Primary data center - Provider XYZ", "name": "primary-dc-1", "enabled": true, "healthy": true, "monitor": "f1aba936b94213e5b8dca0c0dbf1f9cc", "minimum_origins": 1, "check_regions": ["WNAM"], "origins": [{"name": "app-server-1", "address": "0.0.0.0", "enabled": true, "healthy": true, "weight": 1, "disabled_at": "2014-01-01T05:20:00.12345Z", "failure_reason": "HTTP Timeout occured"}], "notification_email": "someone@example.com"}, "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pool_identifier = 'testString'

        # Invoke method
        response = service.edit_load_balancer_pool(
            pool_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_edit_load_balancer_pool_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_edit_load_balancer_pool_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/load_balancers/pools/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "17b5962d775c646f3f9725cbc7a53df4", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "description": "Primary data center - Provider XYZ", "name": "primary-dc-1", "enabled": true, "healthy": true, "monitor": "f1aba936b94213e5b8dca0c0dbf1f9cc", "minimum_origins": 1, "check_regions": ["WNAM"], "origins": [{"name": "app-server-1", "address": "0.0.0.0", "enabled": true, "healthy": true, "weight": 1, "disabled_at": "2014-01-01T05:20:00.12345Z", "failure_reason": "HTTP Timeout occured"}], "notification_email": "someone@example.com"}, "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pool_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pool_identifier": pool_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.edit_load_balancer_pool(**req_copy)



# endregion
##############################################################################
# End of Service: GlobalLoadBalancerPool
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for DeleteLoadBalancerPoolRespResult
#-----------------------------------------------------------------------------
class TestDeleteLoadBalancerPoolRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for DeleteLoadBalancerPoolRespResult
    #--------------------------------------------------------
    def test_delete_load_balancer_pool_resp_result_serialization(self):

        # Construct a json representation of a DeleteLoadBalancerPoolRespResult model
        delete_load_balancer_pool_resp_result_model_json = {}
        delete_load_balancer_pool_resp_result_model_json['id'] = '17b5962d775c646f3f9725cbc7a53df4'

        # Construct a model instance of DeleteLoadBalancerPoolRespResult by calling from_dict on the json representation
        delete_load_balancer_pool_resp_result_model = DeleteLoadBalancerPoolRespResult.from_dict(delete_load_balancer_pool_resp_result_model_json)
        assert delete_load_balancer_pool_resp_result_model != False

        # Construct a model instance of DeleteLoadBalancerPoolRespResult by calling from_dict on the json representation
        delete_load_balancer_pool_resp_result_model_dict = DeleteLoadBalancerPoolRespResult.from_dict(delete_load_balancer_pool_resp_result_model_json).__dict__
        delete_load_balancer_pool_resp_result_model2 = DeleteLoadBalancerPoolRespResult(**delete_load_balancer_pool_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert delete_load_balancer_pool_resp_result_model == delete_load_balancer_pool_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        delete_load_balancer_pool_resp_result_model_json2 = delete_load_balancer_pool_resp_result_model.to_dict()
        assert delete_load_balancer_pool_resp_result_model_json2 == delete_load_balancer_pool_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for LoadBalancerPoolPackOriginsItem
#-----------------------------------------------------------------------------
class TestLoadBalancerPoolPackOriginsItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for LoadBalancerPoolPackOriginsItem
    #--------------------------------------------------------
    def test_load_balancer_pool_pack_origins_item_serialization(self):

        # Construct a json representation of a LoadBalancerPoolPackOriginsItem model
        load_balancer_pool_pack_origins_item_model_json = {}
        load_balancer_pool_pack_origins_item_model_json['name'] = 'app-server-1'
        load_balancer_pool_pack_origins_item_model_json['address'] = '0.0.0.0'
        load_balancer_pool_pack_origins_item_model_json['enabled'] = True
        load_balancer_pool_pack_origins_item_model_json['healthy'] = True
        load_balancer_pool_pack_origins_item_model_json['weight'] = 1
        load_balancer_pool_pack_origins_item_model_json['disabled_at'] = '2014-01-01T05:20:00.12345Z'
        load_balancer_pool_pack_origins_item_model_json['failure_reason'] = 'HTTP Timeout occured'

        # Construct a model instance of LoadBalancerPoolPackOriginsItem by calling from_dict on the json representation
        load_balancer_pool_pack_origins_item_model = LoadBalancerPoolPackOriginsItem.from_dict(load_balancer_pool_pack_origins_item_model_json)
        assert load_balancer_pool_pack_origins_item_model != False

        # Construct a model instance of LoadBalancerPoolPackOriginsItem by calling from_dict on the json representation
        load_balancer_pool_pack_origins_item_model_dict = LoadBalancerPoolPackOriginsItem.from_dict(load_balancer_pool_pack_origins_item_model_json).__dict__
        load_balancer_pool_pack_origins_item_model2 = LoadBalancerPoolPackOriginsItem(**load_balancer_pool_pack_origins_item_model_dict)

        # Verify the model instances are equivalent
        assert load_balancer_pool_pack_origins_item_model == load_balancer_pool_pack_origins_item_model2

        # Convert model instance back to dict and verify no loss of data
        load_balancer_pool_pack_origins_item_model_json2 = load_balancer_pool_pack_origins_item_model.to_dict()
        assert load_balancer_pool_pack_origins_item_model_json2 == load_balancer_pool_pack_origins_item_model_json

#-----------------------------------------------------------------------------
# Test Class for LoadBalancerPoolReqOriginsItem
#-----------------------------------------------------------------------------
class TestLoadBalancerPoolReqOriginsItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for LoadBalancerPoolReqOriginsItem
    #--------------------------------------------------------
    def test_load_balancer_pool_req_origins_item_serialization(self):

        # Construct a json representation of a LoadBalancerPoolReqOriginsItem model
        load_balancer_pool_req_origins_item_model_json = {}
        load_balancer_pool_req_origins_item_model_json['name'] = 'app-server-1'
        load_balancer_pool_req_origins_item_model_json['address'] = '0.0.0.0'
        load_balancer_pool_req_origins_item_model_json['enabled'] = True
        load_balancer_pool_req_origins_item_model_json['weight'] = 1

        # Construct a model instance of LoadBalancerPoolReqOriginsItem by calling from_dict on the json representation
        load_balancer_pool_req_origins_item_model = LoadBalancerPoolReqOriginsItem.from_dict(load_balancer_pool_req_origins_item_model_json)
        assert load_balancer_pool_req_origins_item_model != False

        # Construct a model instance of LoadBalancerPoolReqOriginsItem by calling from_dict on the json representation
        load_balancer_pool_req_origins_item_model_dict = LoadBalancerPoolReqOriginsItem.from_dict(load_balancer_pool_req_origins_item_model_json).__dict__
        load_balancer_pool_req_origins_item_model2 = LoadBalancerPoolReqOriginsItem(**load_balancer_pool_req_origins_item_model_dict)

        # Verify the model instances are equivalent
        assert load_balancer_pool_req_origins_item_model == load_balancer_pool_req_origins_item_model2

        # Convert model instance back to dict and verify no loss of data
        load_balancer_pool_req_origins_item_model_json2 = load_balancer_pool_req_origins_item_model.to_dict()
        assert load_balancer_pool_req_origins_item_model_json2 == load_balancer_pool_req_origins_item_model_json

#-----------------------------------------------------------------------------
# Test Class for DeleteLoadBalancerPoolResp
#-----------------------------------------------------------------------------
class TestDeleteLoadBalancerPoolResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for DeleteLoadBalancerPoolResp
    #--------------------------------------------------------
    def test_delete_load_balancer_pool_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        delete_load_balancer_pool_resp_result_model = {} # DeleteLoadBalancerPoolRespResult
        delete_load_balancer_pool_resp_result_model['id'] = '17b5962d775c646f3f9725cbc7a53df4'

        # Construct a json representation of a DeleteLoadBalancerPoolResp model
        delete_load_balancer_pool_resp_model_json = {}
        delete_load_balancer_pool_resp_model_json['success'] = True
        delete_load_balancer_pool_resp_model_json['errors'] = [['testString']]
        delete_load_balancer_pool_resp_model_json['messages'] = [['testString']]
        delete_load_balancer_pool_resp_model_json['result'] = delete_load_balancer_pool_resp_result_model

        # Construct a model instance of DeleteLoadBalancerPoolResp by calling from_dict on the json representation
        delete_load_balancer_pool_resp_model = DeleteLoadBalancerPoolResp.from_dict(delete_load_balancer_pool_resp_model_json)
        assert delete_load_balancer_pool_resp_model != False

        # Construct a model instance of DeleteLoadBalancerPoolResp by calling from_dict on the json representation
        delete_load_balancer_pool_resp_model_dict = DeleteLoadBalancerPoolResp.from_dict(delete_load_balancer_pool_resp_model_json).__dict__
        delete_load_balancer_pool_resp_model2 = DeleteLoadBalancerPoolResp(**delete_load_balancer_pool_resp_model_dict)

        # Verify the model instances are equivalent
        assert delete_load_balancer_pool_resp_model == delete_load_balancer_pool_resp_model2

        # Convert model instance back to dict and verify no loss of data
        delete_load_balancer_pool_resp_model_json2 = delete_load_balancer_pool_resp_model.to_dict()
        assert delete_load_balancer_pool_resp_model_json2 == delete_load_balancer_pool_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for ListLoadBalancerPoolsResp
#-----------------------------------------------------------------------------
class TestListLoadBalancerPoolsResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for ListLoadBalancerPoolsResp
    #--------------------------------------------------------
    def test_list_load_balancer_pools_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        load_balancer_pool_pack_origins_item_model = {} # LoadBalancerPoolPackOriginsItem
        load_balancer_pool_pack_origins_item_model['name'] = 'app-server-1'
        load_balancer_pool_pack_origins_item_model['address'] = '0.0.0.0'
        load_balancer_pool_pack_origins_item_model['enabled'] = True
        load_balancer_pool_pack_origins_item_model['healthy'] = True
        load_balancer_pool_pack_origins_item_model['weight'] = 1
        load_balancer_pool_pack_origins_item_model['disabled_at'] = '2014-01-01T05:20:00.12345Z'
        load_balancer_pool_pack_origins_item_model['failure_reason'] = 'HTTP Timeout occured'

        load_balancer_pool_pack_model = {} # LoadBalancerPoolPack
        load_balancer_pool_pack_model['id'] = '17b5962d775c646f3f9725cbc7a53df4'
        load_balancer_pool_pack_model['created_on'] = '2014-01-01T05:20:00.12345Z'
        load_balancer_pool_pack_model['modified_on'] = '2014-01-01T05:20:00.12345Z'
        load_balancer_pool_pack_model['description'] = 'Primary data center - Provider XYZ'
        load_balancer_pool_pack_model['name'] = 'primary-dc-1'
        load_balancer_pool_pack_model['enabled'] = True
        load_balancer_pool_pack_model['healthy'] = True
        load_balancer_pool_pack_model['monitor'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        load_balancer_pool_pack_model['minimum_origins'] = 1
        load_balancer_pool_pack_model['check_regions'] = ['WNAM']
        load_balancer_pool_pack_model['origins'] = [load_balancer_pool_pack_origins_item_model]
        load_balancer_pool_pack_model['notification_email'] = 'someone@example.com'

        result_info_model = {} # ResultInfo
        result_info_model['page'] = 1
        result_info_model['per_page'] = 20
        result_info_model['count'] = 1
        result_info_model['total_count'] = 2000

        # Construct a json representation of a ListLoadBalancerPoolsResp model
        list_load_balancer_pools_resp_model_json = {}
        list_load_balancer_pools_resp_model_json['success'] = True
        list_load_balancer_pools_resp_model_json['errors'] = [['testString']]
        list_load_balancer_pools_resp_model_json['messages'] = [['testString']]
        list_load_balancer_pools_resp_model_json['result'] = [load_balancer_pool_pack_model]
        list_load_balancer_pools_resp_model_json['result_info'] = result_info_model

        # Construct a model instance of ListLoadBalancerPoolsResp by calling from_dict on the json representation
        list_load_balancer_pools_resp_model = ListLoadBalancerPoolsResp.from_dict(list_load_balancer_pools_resp_model_json)
        assert list_load_balancer_pools_resp_model != False

        # Construct a model instance of ListLoadBalancerPoolsResp by calling from_dict on the json representation
        list_load_balancer_pools_resp_model_dict = ListLoadBalancerPoolsResp.from_dict(list_load_balancer_pools_resp_model_json).__dict__
        list_load_balancer_pools_resp_model2 = ListLoadBalancerPoolsResp(**list_load_balancer_pools_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_load_balancer_pools_resp_model == list_load_balancer_pools_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_load_balancer_pools_resp_model_json2 = list_load_balancer_pools_resp_model.to_dict()
        assert list_load_balancer_pools_resp_model_json2 == list_load_balancer_pools_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for LoadBalancerPoolPack
#-----------------------------------------------------------------------------
class TestLoadBalancerPoolPack():

    #--------------------------------------------------------
    # Test serialization/deserialization for LoadBalancerPoolPack
    #--------------------------------------------------------
    def test_load_balancer_pool_pack_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        load_balancer_pool_pack_origins_item_model = {} # LoadBalancerPoolPackOriginsItem
        load_balancer_pool_pack_origins_item_model['name'] = 'app-server-1'
        load_balancer_pool_pack_origins_item_model['address'] = '0.0.0.0'
        load_balancer_pool_pack_origins_item_model['enabled'] = True
        load_balancer_pool_pack_origins_item_model['healthy'] = True
        load_balancer_pool_pack_origins_item_model['weight'] = 1
        load_balancer_pool_pack_origins_item_model['disabled_at'] = '2014-01-01T05:20:00.12345Z'
        load_balancer_pool_pack_origins_item_model['failure_reason'] = 'HTTP Timeout occured'

        # Construct a json representation of a LoadBalancerPoolPack model
        load_balancer_pool_pack_model_json = {}
        load_balancer_pool_pack_model_json['id'] = '17b5962d775c646f3f9725cbc7a53df4'
        load_balancer_pool_pack_model_json['created_on'] = '2014-01-01T05:20:00.12345Z'
        load_balancer_pool_pack_model_json['modified_on'] = '2014-01-01T05:20:00.12345Z'
        load_balancer_pool_pack_model_json['description'] = 'Primary data center - Provider XYZ'
        load_balancer_pool_pack_model_json['name'] = 'primary-dc-1'
        load_balancer_pool_pack_model_json['enabled'] = True
        load_balancer_pool_pack_model_json['healthy'] = True
        load_balancer_pool_pack_model_json['monitor'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        load_balancer_pool_pack_model_json['minimum_origins'] = 1
        load_balancer_pool_pack_model_json['check_regions'] = ['WNAM']
        load_balancer_pool_pack_model_json['origins'] = [load_balancer_pool_pack_origins_item_model]
        load_balancer_pool_pack_model_json['notification_email'] = 'someone@example.com'

        # Construct a model instance of LoadBalancerPoolPack by calling from_dict on the json representation
        load_balancer_pool_pack_model = LoadBalancerPoolPack.from_dict(load_balancer_pool_pack_model_json)
        assert load_balancer_pool_pack_model != False

        # Construct a model instance of LoadBalancerPoolPack by calling from_dict on the json representation
        load_balancer_pool_pack_model_dict = LoadBalancerPoolPack.from_dict(load_balancer_pool_pack_model_json).__dict__
        load_balancer_pool_pack_model2 = LoadBalancerPoolPack(**load_balancer_pool_pack_model_dict)

        # Verify the model instances are equivalent
        assert load_balancer_pool_pack_model == load_balancer_pool_pack_model2

        # Convert model instance back to dict and verify no loss of data
        load_balancer_pool_pack_model_json2 = load_balancer_pool_pack_model.to_dict()
        assert load_balancer_pool_pack_model_json2 == load_balancer_pool_pack_model_json

#-----------------------------------------------------------------------------
# Test Class for LoadBalancerPoolResp
#-----------------------------------------------------------------------------
class TestLoadBalancerPoolResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for LoadBalancerPoolResp
    #--------------------------------------------------------
    def test_load_balancer_pool_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        load_balancer_pool_pack_origins_item_model = {} # LoadBalancerPoolPackOriginsItem
        load_balancer_pool_pack_origins_item_model['name'] = 'app-server-1'
        load_balancer_pool_pack_origins_item_model['address'] = '0.0.0.0'
        load_balancer_pool_pack_origins_item_model['enabled'] = True
        load_balancer_pool_pack_origins_item_model['healthy'] = True
        load_balancer_pool_pack_origins_item_model['weight'] = 1
        load_balancer_pool_pack_origins_item_model['disabled_at'] = '2014-01-01T05:20:00.12345Z'
        load_balancer_pool_pack_origins_item_model['failure_reason'] = 'HTTP Timeout occured'

        load_balancer_pool_pack_model = {} # LoadBalancerPoolPack
        load_balancer_pool_pack_model['id'] = '17b5962d775c646f3f9725cbc7a53df4'
        load_balancer_pool_pack_model['created_on'] = '2014-01-01T05:20:00.12345Z'
        load_balancer_pool_pack_model['modified_on'] = '2014-01-01T05:20:00.12345Z'
        load_balancer_pool_pack_model['description'] = 'Primary data center - Provider XYZ'
        load_balancer_pool_pack_model['name'] = 'primary-dc-1'
        load_balancer_pool_pack_model['enabled'] = True
        load_balancer_pool_pack_model['healthy'] = True
        load_balancer_pool_pack_model['monitor'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        load_balancer_pool_pack_model['minimum_origins'] = 1
        load_balancer_pool_pack_model['check_regions'] = ['WNAM']
        load_balancer_pool_pack_model['origins'] = [load_balancer_pool_pack_origins_item_model]
        load_balancer_pool_pack_model['notification_email'] = 'someone@example.com'

        result_info_model = {} # ResultInfo
        result_info_model['page'] = 1
        result_info_model['per_page'] = 20
        result_info_model['count'] = 1
        result_info_model['total_count'] = 2000

        # Construct a json representation of a LoadBalancerPoolResp model
        load_balancer_pool_resp_model_json = {}
        load_balancer_pool_resp_model_json['success'] = True
        load_balancer_pool_resp_model_json['errors'] = [['testString']]
        load_balancer_pool_resp_model_json['messages'] = [['testString']]
        load_balancer_pool_resp_model_json['result'] = load_balancer_pool_pack_model
        load_balancer_pool_resp_model_json['result_info'] = result_info_model

        # Construct a model instance of LoadBalancerPoolResp by calling from_dict on the json representation
        load_balancer_pool_resp_model = LoadBalancerPoolResp.from_dict(load_balancer_pool_resp_model_json)
        assert load_balancer_pool_resp_model != False

        # Construct a model instance of LoadBalancerPoolResp by calling from_dict on the json representation
        load_balancer_pool_resp_model_dict = LoadBalancerPoolResp.from_dict(load_balancer_pool_resp_model_json).__dict__
        load_balancer_pool_resp_model2 = LoadBalancerPoolResp(**load_balancer_pool_resp_model_dict)

        # Verify the model instances are equivalent
        assert load_balancer_pool_resp_model == load_balancer_pool_resp_model2

        # Convert model instance back to dict and verify no loss of data
        load_balancer_pool_resp_model_json2 = load_balancer_pool_resp_model.to_dict()
        assert load_balancer_pool_resp_model_json2 == load_balancer_pool_resp_model_json

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
