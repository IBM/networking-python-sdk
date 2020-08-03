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
from ibm_cloud_networking_services.zone_rate_limits_v1 import *

crn = 'testString'
zone_identifier = 'testString'

service = ZoneRateLimitsV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn,
    zone_identifier=zone_identifier
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: ZoneRateLimits
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_all_zone_rate_limits
#-----------------------------------------------------------------------------
class TestListAllZoneRateLimits():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # list_all_zone_rate_limits()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_zone_rate_limits_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/rate_limits')
        mock_response = '{"success": true, "errors": [["[]"]], "messages": [["[]"]], "result": [{"id": "92f17202ed8bd63d69a66b86a49a8f6b", "disabled": false, "description": "Prevent multiple login failures to mitigate brute force attacks", "bypass": [{"name": "url", "value": "example.com/*"}], "threshold": 1000, "period": 60, "correlate": {"by": "nat"}, "action": {"mode": "simulate", "timeout": 60, "response": {"content_type": "text/plain", "body": "This request has been rate-limited."}}, "match": {"request": {"methods": ["_ALL_"], "schemes": ["_ALL_"], "url": "*.example.org/path*"}, "response": {"status": [403], "headers": [{"name": "Cf-Cache-Status", "op": "ne", "value": "HIT"}], "origin_traffic": false}}}], "result_info": {"page": 1, "per_page": 10, "count": 1, "total_count": 1}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        page = 38
        per_page = 5

        # Invoke method
        response = service.list_all_zone_rate_limits(
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
    # test_list_all_zone_rate_limits_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_zone_rate_limits_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/rate_limits')
        mock_response = '{"success": true, "errors": [["[]"]], "messages": [["[]"]], "result": [{"id": "92f17202ed8bd63d69a66b86a49a8f6b", "disabled": false, "description": "Prevent multiple login failures to mitigate brute force attacks", "bypass": [{"name": "url", "value": "example.com/*"}], "threshold": 1000, "period": 60, "correlate": {"by": "nat"}, "action": {"mode": "simulate", "timeout": 60, "response": {"content_type": "text/plain", "body": "This request has been rate-limited."}}, "match": {"request": {"methods": ["_ALL_"], "schemes": ["_ALL_"], "url": "*.example.org/path*"}, "response": {"status": [403], "headers": [{"name": "Cf-Cache-Status", "op": "ne", "value": "HIT"}], "origin_traffic": false}}}], "result_info": {"page": 1, "per_page": 10, "count": 1, "total_count": 1}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_all_zone_rate_limits()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_all_zone_rate_limits_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_zone_rate_limits_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/rate_limits')
        mock_response = '{"success": true, "errors": [["[]"]], "messages": [["[]"]], "result": [{"id": "92f17202ed8bd63d69a66b86a49a8f6b", "disabled": false, "description": "Prevent multiple login failures to mitigate brute force attacks", "bypass": [{"name": "url", "value": "example.com/*"}], "threshold": 1000, "period": 60, "correlate": {"by": "nat"}, "action": {"mode": "simulate", "timeout": 60, "response": {"content_type": "text/plain", "body": "This request has been rate-limited."}}, "match": {"request": {"methods": ["_ALL_"], "schemes": ["_ALL_"], "url": "*.example.org/path*"}, "response": {"status": [403], "headers": [{"name": "Cf-Cache-Status", "op": "ne", "value": "HIT"}], "origin_traffic": false}}}], "result_info": {"page": 1, "per_page": 10, "count": 1, "total_count": 1}}'
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
                service.list_all_zone_rate_limits(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for create_zone_rate_limits
#-----------------------------------------------------------------------------
class TestCreateZoneRateLimits():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # create_zone_rate_limits()
    #--------------------------------------------------------
    @responses.activate
    def test_create_zone_rate_limits_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/rate_limits')
        mock_response = '{"success": true, "errors": [["[]"]], "messages": [["[]"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "disabled": false, "description": "Prevent multiple login failures to mitigate brute force attacks", "bypass": [{"name": "url", "value": "example.com/*"}], "threshold": 1000, "period": 60, "correlate": {"by": "nat"}, "action": {"mode": "simulate", "timeout": 60, "response": {"content_type": "text/plain", "body": "This request has been rate-limited."}}, "match": {"request": {"methods": ["_ALL_"], "schemes": ["_ALL_"], "url": "*.example.org/path*"}, "response": {"status": [403], "headers": [{"name": "Cf-Cache-Status", "op": "ne", "value": "HIT"}], "origin_traffic": false}}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a RatelimitInputActionResponse model
        ratelimit_input_action_response_model = {}
        ratelimit_input_action_response_model['content_type'] = 'text/plain'
        ratelimit_input_action_response_model['body'] = 'This request has been rate-limited.'

        # Construct a dict representation of a RatelimitInputAction model
        ratelimit_input_action_model = {}
        ratelimit_input_action_model['mode'] = 'simulate'
        ratelimit_input_action_model['timeout'] = 60
        ratelimit_input_action_model['response'] = ratelimit_input_action_response_model

        # Construct a dict representation of a RatelimitInputMatchResponseHeadersItem model
        ratelimit_input_match_response_headers_item_model = {}
        ratelimit_input_match_response_headers_item_model['name'] = 'Cf-Cache-Status'
        ratelimit_input_match_response_headers_item_model['op'] = 'ne'
        ratelimit_input_match_response_headers_item_model['value'] = 'HIT'

        # Construct a dict representation of a RatelimitInputMatchRequest model
        ratelimit_input_match_request_model = {}
        ratelimit_input_match_request_model['methods'] = ['GET']
        ratelimit_input_match_request_model['schemes'] = ['HTTP']
        ratelimit_input_match_request_model['url'] = '*.example.org/path*'

        # Construct a dict representation of a RatelimitInputMatchResponse model
        ratelimit_input_match_response_model = {}
        ratelimit_input_match_response_model['status'] = [403]
        ratelimit_input_match_response_model['headers'] = [ratelimit_input_match_response_headers_item_model]
        ratelimit_input_match_response_model['origin_traffic'] = False

        # Construct a dict representation of a RatelimitInputMatch model
        ratelimit_input_match_model = {}
        ratelimit_input_match_model['request'] = ratelimit_input_match_request_model
        ratelimit_input_match_model['response'] = ratelimit_input_match_response_model

        # Construct a dict representation of a RatelimitInputBypassItem model
        ratelimit_input_bypass_item_model = {}
        ratelimit_input_bypass_item_model['name'] = 'url'
        ratelimit_input_bypass_item_model['value'] = 'api.example.com/*'

        # Construct a dict representation of a RatelimitInputCorrelate model
        ratelimit_input_correlate_model = {}
        ratelimit_input_correlate_model['by'] = 'nat'

        # Set up parameter values
        threshold = 1000
        period = 60
        action = ratelimit_input_action_model
        match = ratelimit_input_match_model
        disabled = False
        description = 'Prevent multiple login failures to mitigate brute force attacks'
        bypass = [ratelimit_input_bypass_item_model]
        correlate = ratelimit_input_correlate_model

        # Invoke method
        response = service.create_zone_rate_limits(
            threshold=threshold,
            period=period,
            action=action,
            match=match,
            disabled=disabled,
            description=description,
            bypass=bypass,
            correlate=correlate,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['threshold'] == 1000
        assert req_body['period'] == 60
        assert req_body['action'] == ratelimit_input_action_model
        assert req_body['match'] == ratelimit_input_match_model
        assert req_body['disabled'] == False
        assert req_body['description'] == 'Prevent multiple login failures to mitigate brute force attacks'
        assert req_body['bypass'] == [ratelimit_input_bypass_item_model]
        assert req_body['correlate'] == ratelimit_input_correlate_model


    #--------------------------------------------------------
    # test_create_zone_rate_limits_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_zone_rate_limits_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/rate_limits')
        mock_response = '{"success": true, "errors": [["[]"]], "messages": [["[]"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "disabled": false, "description": "Prevent multiple login failures to mitigate brute force attacks", "bypass": [{"name": "url", "value": "example.com/*"}], "threshold": 1000, "period": 60, "correlate": {"by": "nat"}, "action": {"mode": "simulate", "timeout": 60, "response": {"content_type": "text/plain", "body": "This request has been rate-limited."}}, "match": {"request": {"methods": ["_ALL_"], "schemes": ["_ALL_"], "url": "*.example.org/path*"}, "response": {"status": [403], "headers": [{"name": "Cf-Cache-Status", "op": "ne", "value": "HIT"}], "origin_traffic": false}}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.create_zone_rate_limits()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_create_zone_rate_limits_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_zone_rate_limits_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/rate_limits')
        mock_response = '{"success": true, "errors": [["[]"]], "messages": [["[]"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "disabled": false, "description": "Prevent multiple login failures to mitigate brute force attacks", "bypass": [{"name": "url", "value": "example.com/*"}], "threshold": 1000, "period": 60, "correlate": {"by": "nat"}, "action": {"mode": "simulate", "timeout": 60, "response": {"content_type": "text/plain", "body": "This request has been rate-limited."}}, "match": {"request": {"methods": ["_ALL_"], "schemes": ["_ALL_"], "url": "*.example.org/path*"}, "response": {"status": [403], "headers": [{"name": "Cf-Cache-Status", "op": "ne", "value": "HIT"}], "origin_traffic": false}}}}'
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
                service.create_zone_rate_limits(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_zone_rate_limit
#-----------------------------------------------------------------------------
class TestDeleteZoneRateLimit():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # delete_zone_rate_limit()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_zone_rate_limit_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/rate_limits/testString')
        mock_response = '{"success": true, "errors": [["[]"]], "messages": [["[]"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rate_limit_identifier = 'testString'

        # Invoke method
        response = service.delete_zone_rate_limit(
            rate_limit_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_zone_rate_limit_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_zone_rate_limit_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/rate_limits/testString')
        mock_response = '{"success": true, "errors": [["[]"]], "messages": [["[]"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rate_limit_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "rate_limit_identifier": rate_limit_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_zone_rate_limit(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_rate_limit
#-----------------------------------------------------------------------------
class TestGetRateLimit():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_rate_limit()
    #--------------------------------------------------------
    @responses.activate
    def test_get_rate_limit_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/rate_limits/testString')
        mock_response = '{"success": true, "errors": [["[]"]], "messages": [["[]"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "disabled": false, "description": "Prevent multiple login failures to mitigate brute force attacks", "bypass": [{"name": "url", "value": "example.com/*"}], "threshold": 1000, "period": 60, "correlate": {"by": "nat"}, "action": {"mode": "simulate", "timeout": 60, "response": {"content_type": "text/plain", "body": "This request has been rate-limited."}}, "match": {"request": {"methods": ["_ALL_"], "schemes": ["_ALL_"], "url": "*.example.org/path*"}, "response": {"status": [403], "headers": [{"name": "Cf-Cache-Status", "op": "ne", "value": "HIT"}], "origin_traffic": false}}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rate_limit_identifier = 'testString'

        # Invoke method
        response = service.get_rate_limit(
            rate_limit_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_rate_limit_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_rate_limit_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/rate_limits/testString')
        mock_response = '{"success": true, "errors": [["[]"]], "messages": [["[]"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "disabled": false, "description": "Prevent multiple login failures to mitigate brute force attacks", "bypass": [{"name": "url", "value": "example.com/*"}], "threshold": 1000, "period": 60, "correlate": {"by": "nat"}, "action": {"mode": "simulate", "timeout": 60, "response": {"content_type": "text/plain", "body": "This request has been rate-limited."}}, "match": {"request": {"methods": ["_ALL_"], "schemes": ["_ALL_"], "url": "*.example.org/path*"}, "response": {"status": [403], "headers": [{"name": "Cf-Cache-Status", "op": "ne", "value": "HIT"}], "origin_traffic": false}}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rate_limit_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "rate_limit_identifier": rate_limit_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_rate_limit(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_rate_limit
#-----------------------------------------------------------------------------
class TestUpdateRateLimit():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_rate_limit()
    #--------------------------------------------------------
    @responses.activate
    def test_update_rate_limit_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/rate_limits/testString')
        mock_response = '{"success": true, "errors": [["[]"]], "messages": [["[]"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "disabled": false, "description": "Prevent multiple login failures to mitigate brute force attacks", "bypass": [{"name": "url", "value": "example.com/*"}], "threshold": 1000, "period": 60, "correlate": {"by": "nat"}, "action": {"mode": "simulate", "timeout": 60, "response": {"content_type": "text/plain", "body": "This request has been rate-limited."}}, "match": {"request": {"methods": ["_ALL_"], "schemes": ["_ALL_"], "url": "*.example.org/path*"}, "response": {"status": [403], "headers": [{"name": "Cf-Cache-Status", "op": "ne", "value": "HIT"}], "origin_traffic": false}}}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a RatelimitInputActionResponse model
        ratelimit_input_action_response_model = {}
        ratelimit_input_action_response_model['content_type'] = 'text/plain'
        ratelimit_input_action_response_model['body'] = 'This request has been rate-limited.'

        # Construct a dict representation of a RatelimitInputAction model
        ratelimit_input_action_model = {}
        ratelimit_input_action_model['mode'] = 'simulate'
        ratelimit_input_action_model['timeout'] = 60
        ratelimit_input_action_model['response'] = ratelimit_input_action_response_model

        # Construct a dict representation of a RatelimitInputMatchResponseHeadersItem model
        ratelimit_input_match_response_headers_item_model = {}
        ratelimit_input_match_response_headers_item_model['name'] = 'Cf-Cache-Status'
        ratelimit_input_match_response_headers_item_model['op'] = 'ne'
        ratelimit_input_match_response_headers_item_model['value'] = 'HIT'

        # Construct a dict representation of a RatelimitInputMatchRequest model
        ratelimit_input_match_request_model = {}
        ratelimit_input_match_request_model['methods'] = ['GET']
        ratelimit_input_match_request_model['schemes'] = ['HTTP']
        ratelimit_input_match_request_model['url'] = '*.example.org/path*'

        # Construct a dict representation of a RatelimitInputMatchResponse model
        ratelimit_input_match_response_model = {}
        ratelimit_input_match_response_model['status'] = [403]
        ratelimit_input_match_response_model['headers'] = [ratelimit_input_match_response_headers_item_model]
        ratelimit_input_match_response_model['origin_traffic'] = False

        # Construct a dict representation of a RatelimitInputMatch model
        ratelimit_input_match_model = {}
        ratelimit_input_match_model['request'] = ratelimit_input_match_request_model
        ratelimit_input_match_model['response'] = ratelimit_input_match_response_model

        # Construct a dict representation of a RatelimitInputBypassItem model
        ratelimit_input_bypass_item_model = {}
        ratelimit_input_bypass_item_model['name'] = 'url'
        ratelimit_input_bypass_item_model['value'] = 'api.example.com/*'

        # Construct a dict representation of a RatelimitInputCorrelate model
        ratelimit_input_correlate_model = {}
        ratelimit_input_correlate_model['by'] = 'nat'

        # Set up parameter values
        rate_limit_identifier = 'testString'
        threshold = 1000
        period = 60
        action = ratelimit_input_action_model
        match = ratelimit_input_match_model
        disabled = False
        description = 'Prevent multiple login failures to mitigate brute force attacks'
        bypass = [ratelimit_input_bypass_item_model]
        correlate = ratelimit_input_correlate_model

        # Invoke method
        response = service.update_rate_limit(
            rate_limit_identifier,
            threshold=threshold,
            period=period,
            action=action,
            match=match,
            disabled=disabled,
            description=description,
            bypass=bypass,
            correlate=correlate,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['threshold'] == 1000
        assert req_body['period'] == 60
        assert req_body['action'] == ratelimit_input_action_model
        assert req_body['match'] == ratelimit_input_match_model
        assert req_body['disabled'] == False
        assert req_body['description'] == 'Prevent multiple login failures to mitigate brute force attacks'
        assert req_body['bypass'] == [ratelimit_input_bypass_item_model]
        assert req_body['correlate'] == ratelimit_input_correlate_model


    #--------------------------------------------------------
    # test_update_rate_limit_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_rate_limit_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/rate_limits/testString')
        mock_response = '{"success": true, "errors": [["[]"]], "messages": [["[]"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "disabled": false, "description": "Prevent multiple login failures to mitigate brute force attacks", "bypass": [{"name": "url", "value": "example.com/*"}], "threshold": 1000, "period": 60, "correlate": {"by": "nat"}, "action": {"mode": "simulate", "timeout": 60, "response": {"content_type": "text/plain", "body": "This request has been rate-limited."}}, "match": {"request": {"methods": ["_ALL_"], "schemes": ["_ALL_"], "url": "*.example.org/path*"}, "response": {"status": [403], "headers": [{"name": "Cf-Cache-Status", "op": "ne", "value": "HIT"}], "origin_traffic": false}}}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rate_limit_identifier = 'testString'

        # Invoke method
        response = service.update_rate_limit(
            rate_limit_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_rate_limit_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_rate_limit_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/rate_limits/testString')
        mock_response = '{"success": true, "errors": [["[]"]], "messages": [["[]"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "disabled": false, "description": "Prevent multiple login failures to mitigate brute force attacks", "bypass": [{"name": "url", "value": "example.com/*"}], "threshold": 1000, "period": 60, "correlate": {"by": "nat"}, "action": {"mode": "simulate", "timeout": 60, "response": {"content_type": "text/plain", "body": "This request has been rate-limited."}}, "match": {"request": {"methods": ["_ALL_"], "schemes": ["_ALL_"], "url": "*.example.org/path*"}, "response": {"status": [403], "headers": [{"name": "Cf-Cache-Status", "op": "ne", "value": "HIT"}], "origin_traffic": false}}}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rate_limit_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "rate_limit_identifier": rate_limit_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_rate_limit(**req_copy)



# endregion
##############################################################################
# End of Service: ZoneRateLimits
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for DeleteRateLimitRespResult
#-----------------------------------------------------------------------------
class TestDeleteRateLimitRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for DeleteRateLimitRespResult
    #--------------------------------------------------------
    def test_delete_rate_limit_resp_result_serialization(self):

        # Construct a json representation of a DeleteRateLimitRespResult model
        delete_rate_limit_resp_result_model_json = {}
        delete_rate_limit_resp_result_model_json['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'

        # Construct a model instance of DeleteRateLimitRespResult by calling from_dict on the json representation
        delete_rate_limit_resp_result_model = DeleteRateLimitRespResult.from_dict(delete_rate_limit_resp_result_model_json)
        assert delete_rate_limit_resp_result_model != False

        # Construct a model instance of DeleteRateLimitRespResult by calling from_dict on the json representation
        delete_rate_limit_resp_result_model_dict = DeleteRateLimitRespResult.from_dict(delete_rate_limit_resp_result_model_json).__dict__
        delete_rate_limit_resp_result_model2 = DeleteRateLimitRespResult(**delete_rate_limit_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert delete_rate_limit_resp_result_model == delete_rate_limit_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        delete_rate_limit_resp_result_model_json2 = delete_rate_limit_resp_result_model.to_dict()
        assert delete_rate_limit_resp_result_model_json2 == delete_rate_limit_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for ListRatelimitRespResultInfo
#-----------------------------------------------------------------------------
class TestListRatelimitRespResultInfo():

    #--------------------------------------------------------
    # Test serialization/deserialization for ListRatelimitRespResultInfo
    #--------------------------------------------------------
    def test_list_ratelimit_resp_result_info_serialization(self):

        # Construct a json representation of a ListRatelimitRespResultInfo model
        list_ratelimit_resp_result_info_model_json = {}
        list_ratelimit_resp_result_info_model_json['page'] = 1
        list_ratelimit_resp_result_info_model_json['per_page'] = 10
        list_ratelimit_resp_result_info_model_json['count'] = 1
        list_ratelimit_resp_result_info_model_json['total_count'] = 1

        # Construct a model instance of ListRatelimitRespResultInfo by calling from_dict on the json representation
        list_ratelimit_resp_result_info_model = ListRatelimitRespResultInfo.from_dict(list_ratelimit_resp_result_info_model_json)
        assert list_ratelimit_resp_result_info_model != False

        # Construct a model instance of ListRatelimitRespResultInfo by calling from_dict on the json representation
        list_ratelimit_resp_result_info_model_dict = ListRatelimitRespResultInfo.from_dict(list_ratelimit_resp_result_info_model_json).__dict__
        list_ratelimit_resp_result_info_model2 = ListRatelimitRespResultInfo(**list_ratelimit_resp_result_info_model_dict)

        # Verify the model instances are equivalent
        assert list_ratelimit_resp_result_info_model == list_ratelimit_resp_result_info_model2

        # Convert model instance back to dict and verify no loss of data
        list_ratelimit_resp_result_info_model_json2 = list_ratelimit_resp_result_info_model.to_dict()
        assert list_ratelimit_resp_result_info_model_json2 == list_ratelimit_resp_result_info_model_json

#-----------------------------------------------------------------------------
# Test Class for RatelimitInputAction
#-----------------------------------------------------------------------------
class TestRatelimitInputAction():

    #--------------------------------------------------------
    # Test serialization/deserialization for RatelimitInputAction
    #--------------------------------------------------------
    def test_ratelimit_input_action_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        ratelimit_input_action_response_model = {} # RatelimitInputActionResponse
        ratelimit_input_action_response_model['content_type'] = 'text/plain'
        ratelimit_input_action_response_model['body'] = 'This request has been rate-limited.'

        # Construct a json representation of a RatelimitInputAction model
        ratelimit_input_action_model_json = {}
        ratelimit_input_action_model_json['mode'] = 'simulate'
        ratelimit_input_action_model_json['timeout'] = 60
        ratelimit_input_action_model_json['response'] = ratelimit_input_action_response_model

        # Construct a model instance of RatelimitInputAction by calling from_dict on the json representation
        ratelimit_input_action_model = RatelimitInputAction.from_dict(ratelimit_input_action_model_json)
        assert ratelimit_input_action_model != False

        # Construct a model instance of RatelimitInputAction by calling from_dict on the json representation
        ratelimit_input_action_model_dict = RatelimitInputAction.from_dict(ratelimit_input_action_model_json).__dict__
        ratelimit_input_action_model2 = RatelimitInputAction(**ratelimit_input_action_model_dict)

        # Verify the model instances are equivalent
        assert ratelimit_input_action_model == ratelimit_input_action_model2

        # Convert model instance back to dict and verify no loss of data
        ratelimit_input_action_model_json2 = ratelimit_input_action_model.to_dict()
        assert ratelimit_input_action_model_json2 == ratelimit_input_action_model_json

#-----------------------------------------------------------------------------
# Test Class for RatelimitInputActionResponse
#-----------------------------------------------------------------------------
class TestRatelimitInputActionResponse():

    #--------------------------------------------------------
    # Test serialization/deserialization for RatelimitInputActionResponse
    #--------------------------------------------------------
    def test_ratelimit_input_action_response_serialization(self):

        # Construct a json representation of a RatelimitInputActionResponse model
        ratelimit_input_action_response_model_json = {}
        ratelimit_input_action_response_model_json['content_type'] = 'text/plain'
        ratelimit_input_action_response_model_json['body'] = 'This request has been rate-limited.'

        # Construct a model instance of RatelimitInputActionResponse by calling from_dict on the json representation
        ratelimit_input_action_response_model = RatelimitInputActionResponse.from_dict(ratelimit_input_action_response_model_json)
        assert ratelimit_input_action_response_model != False

        # Construct a model instance of RatelimitInputActionResponse by calling from_dict on the json representation
        ratelimit_input_action_response_model_dict = RatelimitInputActionResponse.from_dict(ratelimit_input_action_response_model_json).__dict__
        ratelimit_input_action_response_model2 = RatelimitInputActionResponse(**ratelimit_input_action_response_model_dict)

        # Verify the model instances are equivalent
        assert ratelimit_input_action_response_model == ratelimit_input_action_response_model2

        # Convert model instance back to dict and verify no loss of data
        ratelimit_input_action_response_model_json2 = ratelimit_input_action_response_model.to_dict()
        assert ratelimit_input_action_response_model_json2 == ratelimit_input_action_response_model_json

#-----------------------------------------------------------------------------
# Test Class for RatelimitInputBypassItem
#-----------------------------------------------------------------------------
class TestRatelimitInputBypassItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for RatelimitInputBypassItem
    #--------------------------------------------------------
    def test_ratelimit_input_bypass_item_serialization(self):

        # Construct a json representation of a RatelimitInputBypassItem model
        ratelimit_input_bypass_item_model_json = {}
        ratelimit_input_bypass_item_model_json['name'] = 'url'
        ratelimit_input_bypass_item_model_json['value'] = 'api.example.com/*'

        # Construct a model instance of RatelimitInputBypassItem by calling from_dict on the json representation
        ratelimit_input_bypass_item_model = RatelimitInputBypassItem.from_dict(ratelimit_input_bypass_item_model_json)
        assert ratelimit_input_bypass_item_model != False

        # Construct a model instance of RatelimitInputBypassItem by calling from_dict on the json representation
        ratelimit_input_bypass_item_model_dict = RatelimitInputBypassItem.from_dict(ratelimit_input_bypass_item_model_json).__dict__
        ratelimit_input_bypass_item_model2 = RatelimitInputBypassItem(**ratelimit_input_bypass_item_model_dict)

        # Verify the model instances are equivalent
        assert ratelimit_input_bypass_item_model == ratelimit_input_bypass_item_model2

        # Convert model instance back to dict and verify no loss of data
        ratelimit_input_bypass_item_model_json2 = ratelimit_input_bypass_item_model.to_dict()
        assert ratelimit_input_bypass_item_model_json2 == ratelimit_input_bypass_item_model_json

#-----------------------------------------------------------------------------
# Test Class for RatelimitInputCorrelate
#-----------------------------------------------------------------------------
class TestRatelimitInputCorrelate():

    #--------------------------------------------------------
    # Test serialization/deserialization for RatelimitInputCorrelate
    #--------------------------------------------------------
    def test_ratelimit_input_correlate_serialization(self):

        # Construct a json representation of a RatelimitInputCorrelate model
        ratelimit_input_correlate_model_json = {}
        ratelimit_input_correlate_model_json['by'] = 'nat'

        # Construct a model instance of RatelimitInputCorrelate by calling from_dict on the json representation
        ratelimit_input_correlate_model = RatelimitInputCorrelate.from_dict(ratelimit_input_correlate_model_json)
        assert ratelimit_input_correlate_model != False

        # Construct a model instance of RatelimitInputCorrelate by calling from_dict on the json representation
        ratelimit_input_correlate_model_dict = RatelimitInputCorrelate.from_dict(ratelimit_input_correlate_model_json).__dict__
        ratelimit_input_correlate_model2 = RatelimitInputCorrelate(**ratelimit_input_correlate_model_dict)

        # Verify the model instances are equivalent
        assert ratelimit_input_correlate_model == ratelimit_input_correlate_model2

        # Convert model instance back to dict and verify no loss of data
        ratelimit_input_correlate_model_json2 = ratelimit_input_correlate_model.to_dict()
        assert ratelimit_input_correlate_model_json2 == ratelimit_input_correlate_model_json

#-----------------------------------------------------------------------------
# Test Class for RatelimitInputMatch
#-----------------------------------------------------------------------------
class TestRatelimitInputMatch():

    #--------------------------------------------------------
    # Test serialization/deserialization for RatelimitInputMatch
    #--------------------------------------------------------
    def test_ratelimit_input_match_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        ratelimit_input_match_response_headers_item_model = {} # RatelimitInputMatchResponseHeadersItem
        ratelimit_input_match_response_headers_item_model['name'] = 'Cf-Cache-Status'
        ratelimit_input_match_response_headers_item_model['op'] = 'ne'
        ratelimit_input_match_response_headers_item_model['value'] = 'HIT'

        ratelimit_input_match_request_model = {} # RatelimitInputMatchRequest
        ratelimit_input_match_request_model['methods'] = ['GET']
        ratelimit_input_match_request_model['schemes'] = ['HTTP']
        ratelimit_input_match_request_model['url'] = '*.example.org/path*'

        ratelimit_input_match_response_model = {} # RatelimitInputMatchResponse
        ratelimit_input_match_response_model['status'] = [403]
        ratelimit_input_match_response_model['headers'] = [ratelimit_input_match_response_headers_item_model]
        ratelimit_input_match_response_model['origin_traffic'] = False

        # Construct a json representation of a RatelimitInputMatch model
        ratelimit_input_match_model_json = {}
        ratelimit_input_match_model_json['request'] = ratelimit_input_match_request_model
        ratelimit_input_match_model_json['response'] = ratelimit_input_match_response_model

        # Construct a model instance of RatelimitInputMatch by calling from_dict on the json representation
        ratelimit_input_match_model = RatelimitInputMatch.from_dict(ratelimit_input_match_model_json)
        assert ratelimit_input_match_model != False

        # Construct a model instance of RatelimitInputMatch by calling from_dict on the json representation
        ratelimit_input_match_model_dict = RatelimitInputMatch.from_dict(ratelimit_input_match_model_json).__dict__
        ratelimit_input_match_model2 = RatelimitInputMatch(**ratelimit_input_match_model_dict)

        # Verify the model instances are equivalent
        assert ratelimit_input_match_model == ratelimit_input_match_model2

        # Convert model instance back to dict and verify no loss of data
        ratelimit_input_match_model_json2 = ratelimit_input_match_model.to_dict()
        assert ratelimit_input_match_model_json2 == ratelimit_input_match_model_json

#-----------------------------------------------------------------------------
# Test Class for RatelimitInputMatchRequest
#-----------------------------------------------------------------------------
class TestRatelimitInputMatchRequest():

    #--------------------------------------------------------
    # Test serialization/deserialization for RatelimitInputMatchRequest
    #--------------------------------------------------------
    def test_ratelimit_input_match_request_serialization(self):

        # Construct a json representation of a RatelimitInputMatchRequest model
        ratelimit_input_match_request_model_json = {}
        ratelimit_input_match_request_model_json['methods'] = ['GET']
        ratelimit_input_match_request_model_json['schemes'] = ['HTTP']
        ratelimit_input_match_request_model_json['url'] = '*.example.org/path*'

        # Construct a model instance of RatelimitInputMatchRequest by calling from_dict on the json representation
        ratelimit_input_match_request_model = RatelimitInputMatchRequest.from_dict(ratelimit_input_match_request_model_json)
        assert ratelimit_input_match_request_model != False

        # Construct a model instance of RatelimitInputMatchRequest by calling from_dict on the json representation
        ratelimit_input_match_request_model_dict = RatelimitInputMatchRequest.from_dict(ratelimit_input_match_request_model_json).__dict__
        ratelimit_input_match_request_model2 = RatelimitInputMatchRequest(**ratelimit_input_match_request_model_dict)

        # Verify the model instances are equivalent
        assert ratelimit_input_match_request_model == ratelimit_input_match_request_model2

        # Convert model instance back to dict and verify no loss of data
        ratelimit_input_match_request_model_json2 = ratelimit_input_match_request_model.to_dict()
        assert ratelimit_input_match_request_model_json2 == ratelimit_input_match_request_model_json

#-----------------------------------------------------------------------------
# Test Class for RatelimitInputMatchResponse
#-----------------------------------------------------------------------------
class TestRatelimitInputMatchResponse():

    #--------------------------------------------------------
    # Test serialization/deserialization for RatelimitInputMatchResponse
    #--------------------------------------------------------
    def test_ratelimit_input_match_response_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        ratelimit_input_match_response_headers_item_model = {} # RatelimitInputMatchResponseHeadersItem
        ratelimit_input_match_response_headers_item_model['name'] = 'Cf-Cache-Status'
        ratelimit_input_match_response_headers_item_model['op'] = 'ne'
        ratelimit_input_match_response_headers_item_model['value'] = 'HIT'

        # Construct a json representation of a RatelimitInputMatchResponse model
        ratelimit_input_match_response_model_json = {}
        ratelimit_input_match_response_model_json['status'] = [403]
        ratelimit_input_match_response_model_json['headers'] = [ratelimit_input_match_response_headers_item_model]
        ratelimit_input_match_response_model_json['origin_traffic'] = False

        # Construct a model instance of RatelimitInputMatchResponse by calling from_dict on the json representation
        ratelimit_input_match_response_model = RatelimitInputMatchResponse.from_dict(ratelimit_input_match_response_model_json)
        assert ratelimit_input_match_response_model != False

        # Construct a model instance of RatelimitInputMatchResponse by calling from_dict on the json representation
        ratelimit_input_match_response_model_dict = RatelimitInputMatchResponse.from_dict(ratelimit_input_match_response_model_json).__dict__
        ratelimit_input_match_response_model2 = RatelimitInputMatchResponse(**ratelimit_input_match_response_model_dict)

        # Verify the model instances are equivalent
        assert ratelimit_input_match_response_model == ratelimit_input_match_response_model2

        # Convert model instance back to dict and verify no loss of data
        ratelimit_input_match_response_model_json2 = ratelimit_input_match_response_model.to_dict()
        assert ratelimit_input_match_response_model_json2 == ratelimit_input_match_response_model_json

#-----------------------------------------------------------------------------
# Test Class for RatelimitInputMatchResponseHeadersItem
#-----------------------------------------------------------------------------
class TestRatelimitInputMatchResponseHeadersItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for RatelimitInputMatchResponseHeadersItem
    #--------------------------------------------------------
    def test_ratelimit_input_match_response_headers_item_serialization(self):

        # Construct a json representation of a RatelimitInputMatchResponseHeadersItem model
        ratelimit_input_match_response_headers_item_model_json = {}
        ratelimit_input_match_response_headers_item_model_json['name'] = 'Cf-Cache-Status'
        ratelimit_input_match_response_headers_item_model_json['op'] = 'ne'
        ratelimit_input_match_response_headers_item_model_json['value'] = 'HIT'

        # Construct a model instance of RatelimitInputMatchResponseHeadersItem by calling from_dict on the json representation
        ratelimit_input_match_response_headers_item_model = RatelimitInputMatchResponseHeadersItem.from_dict(ratelimit_input_match_response_headers_item_model_json)
        assert ratelimit_input_match_response_headers_item_model != False

        # Construct a model instance of RatelimitInputMatchResponseHeadersItem by calling from_dict on the json representation
        ratelimit_input_match_response_headers_item_model_dict = RatelimitInputMatchResponseHeadersItem.from_dict(ratelimit_input_match_response_headers_item_model_json).__dict__
        ratelimit_input_match_response_headers_item_model2 = RatelimitInputMatchResponseHeadersItem(**ratelimit_input_match_response_headers_item_model_dict)

        # Verify the model instances are equivalent
        assert ratelimit_input_match_response_headers_item_model == ratelimit_input_match_response_headers_item_model2

        # Convert model instance back to dict and verify no loss of data
        ratelimit_input_match_response_headers_item_model_json2 = ratelimit_input_match_response_headers_item_model.to_dict()
        assert ratelimit_input_match_response_headers_item_model_json2 == ratelimit_input_match_response_headers_item_model_json

#-----------------------------------------------------------------------------
# Test Class for RatelimitObjectAction
#-----------------------------------------------------------------------------
class TestRatelimitObjectAction():

    #--------------------------------------------------------
    # Test serialization/deserialization for RatelimitObjectAction
    #--------------------------------------------------------
    def test_ratelimit_object_action_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        ratelimit_object_action_response_model = {} # RatelimitObjectActionResponse
        ratelimit_object_action_response_model['content_type'] = 'text/plain'
        ratelimit_object_action_response_model['body'] = 'This request has been rate-limited.'

        # Construct a json representation of a RatelimitObjectAction model
        ratelimit_object_action_model_json = {}
        ratelimit_object_action_model_json['mode'] = 'simulate'
        ratelimit_object_action_model_json['timeout'] = 60
        ratelimit_object_action_model_json['response'] = ratelimit_object_action_response_model

        # Construct a model instance of RatelimitObjectAction by calling from_dict on the json representation
        ratelimit_object_action_model = RatelimitObjectAction.from_dict(ratelimit_object_action_model_json)
        assert ratelimit_object_action_model != False

        # Construct a model instance of RatelimitObjectAction by calling from_dict on the json representation
        ratelimit_object_action_model_dict = RatelimitObjectAction.from_dict(ratelimit_object_action_model_json).__dict__
        ratelimit_object_action_model2 = RatelimitObjectAction(**ratelimit_object_action_model_dict)

        # Verify the model instances are equivalent
        assert ratelimit_object_action_model == ratelimit_object_action_model2

        # Convert model instance back to dict and verify no loss of data
        ratelimit_object_action_model_json2 = ratelimit_object_action_model.to_dict()
        assert ratelimit_object_action_model_json2 == ratelimit_object_action_model_json

#-----------------------------------------------------------------------------
# Test Class for RatelimitObjectActionResponse
#-----------------------------------------------------------------------------
class TestRatelimitObjectActionResponse():

    #--------------------------------------------------------
    # Test serialization/deserialization for RatelimitObjectActionResponse
    #--------------------------------------------------------
    def test_ratelimit_object_action_response_serialization(self):

        # Construct a json representation of a RatelimitObjectActionResponse model
        ratelimit_object_action_response_model_json = {}
        ratelimit_object_action_response_model_json['content_type'] = 'text/plain'
        ratelimit_object_action_response_model_json['body'] = 'This request has been rate-limited.'

        # Construct a model instance of RatelimitObjectActionResponse by calling from_dict on the json representation
        ratelimit_object_action_response_model = RatelimitObjectActionResponse.from_dict(ratelimit_object_action_response_model_json)
        assert ratelimit_object_action_response_model != False

        # Construct a model instance of RatelimitObjectActionResponse by calling from_dict on the json representation
        ratelimit_object_action_response_model_dict = RatelimitObjectActionResponse.from_dict(ratelimit_object_action_response_model_json).__dict__
        ratelimit_object_action_response_model2 = RatelimitObjectActionResponse(**ratelimit_object_action_response_model_dict)

        # Verify the model instances are equivalent
        assert ratelimit_object_action_response_model == ratelimit_object_action_response_model2

        # Convert model instance back to dict and verify no loss of data
        ratelimit_object_action_response_model_json2 = ratelimit_object_action_response_model.to_dict()
        assert ratelimit_object_action_response_model_json2 == ratelimit_object_action_response_model_json

#-----------------------------------------------------------------------------
# Test Class for RatelimitObjectBypassItem
#-----------------------------------------------------------------------------
class TestRatelimitObjectBypassItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for RatelimitObjectBypassItem
    #--------------------------------------------------------
    def test_ratelimit_object_bypass_item_serialization(self):

        # Construct a json representation of a RatelimitObjectBypassItem model
        ratelimit_object_bypass_item_model_json = {}
        ratelimit_object_bypass_item_model_json['name'] = 'url'
        ratelimit_object_bypass_item_model_json['value'] = 'example.com/*'

        # Construct a model instance of RatelimitObjectBypassItem by calling from_dict on the json representation
        ratelimit_object_bypass_item_model = RatelimitObjectBypassItem.from_dict(ratelimit_object_bypass_item_model_json)
        assert ratelimit_object_bypass_item_model != False

        # Construct a model instance of RatelimitObjectBypassItem by calling from_dict on the json representation
        ratelimit_object_bypass_item_model_dict = RatelimitObjectBypassItem.from_dict(ratelimit_object_bypass_item_model_json).__dict__
        ratelimit_object_bypass_item_model2 = RatelimitObjectBypassItem(**ratelimit_object_bypass_item_model_dict)

        # Verify the model instances are equivalent
        assert ratelimit_object_bypass_item_model == ratelimit_object_bypass_item_model2

        # Convert model instance back to dict and verify no loss of data
        ratelimit_object_bypass_item_model_json2 = ratelimit_object_bypass_item_model.to_dict()
        assert ratelimit_object_bypass_item_model_json2 == ratelimit_object_bypass_item_model_json

#-----------------------------------------------------------------------------
# Test Class for RatelimitObjectCorrelate
#-----------------------------------------------------------------------------
class TestRatelimitObjectCorrelate():

    #--------------------------------------------------------
    # Test serialization/deserialization for RatelimitObjectCorrelate
    #--------------------------------------------------------
    def test_ratelimit_object_correlate_serialization(self):

        # Construct a json representation of a RatelimitObjectCorrelate model
        ratelimit_object_correlate_model_json = {}
        ratelimit_object_correlate_model_json['by'] = 'nat'

        # Construct a model instance of RatelimitObjectCorrelate by calling from_dict on the json representation
        ratelimit_object_correlate_model = RatelimitObjectCorrelate.from_dict(ratelimit_object_correlate_model_json)
        assert ratelimit_object_correlate_model != False

        # Construct a model instance of RatelimitObjectCorrelate by calling from_dict on the json representation
        ratelimit_object_correlate_model_dict = RatelimitObjectCorrelate.from_dict(ratelimit_object_correlate_model_json).__dict__
        ratelimit_object_correlate_model2 = RatelimitObjectCorrelate(**ratelimit_object_correlate_model_dict)

        # Verify the model instances are equivalent
        assert ratelimit_object_correlate_model == ratelimit_object_correlate_model2

        # Convert model instance back to dict and verify no loss of data
        ratelimit_object_correlate_model_json2 = ratelimit_object_correlate_model.to_dict()
        assert ratelimit_object_correlate_model_json2 == ratelimit_object_correlate_model_json

#-----------------------------------------------------------------------------
# Test Class for RatelimitObjectMatch
#-----------------------------------------------------------------------------
class TestRatelimitObjectMatch():

    #--------------------------------------------------------
    # Test serialization/deserialization for RatelimitObjectMatch
    #--------------------------------------------------------
    def test_ratelimit_object_match_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        ratelimit_object_match_response_headers_item_model = {} # RatelimitObjectMatchResponseHeadersItem
        ratelimit_object_match_response_headers_item_model['name'] = 'Cf-Cache-Status'
        ratelimit_object_match_response_headers_item_model['op'] = 'ne'
        ratelimit_object_match_response_headers_item_model['value'] = 'HIT'

        ratelimit_object_match_request_model = {} # RatelimitObjectMatchRequest
        ratelimit_object_match_request_model['methods'] = ['_ALL_']
        ratelimit_object_match_request_model['schemes'] = ['_ALL_']
        ratelimit_object_match_request_model['url'] = '*.example.org/path*'

        ratelimit_object_match_response_model = {} # RatelimitObjectMatchResponse
        ratelimit_object_match_response_model['status'] = [403]
        ratelimit_object_match_response_model['headers'] = [ratelimit_object_match_response_headers_item_model]
        ratelimit_object_match_response_model['origin_traffic'] = False

        # Construct a json representation of a RatelimitObjectMatch model
        ratelimit_object_match_model_json = {}
        ratelimit_object_match_model_json['request'] = ratelimit_object_match_request_model
        ratelimit_object_match_model_json['response'] = ratelimit_object_match_response_model

        # Construct a model instance of RatelimitObjectMatch by calling from_dict on the json representation
        ratelimit_object_match_model = RatelimitObjectMatch.from_dict(ratelimit_object_match_model_json)
        assert ratelimit_object_match_model != False

        # Construct a model instance of RatelimitObjectMatch by calling from_dict on the json representation
        ratelimit_object_match_model_dict = RatelimitObjectMatch.from_dict(ratelimit_object_match_model_json).__dict__
        ratelimit_object_match_model2 = RatelimitObjectMatch(**ratelimit_object_match_model_dict)

        # Verify the model instances are equivalent
        assert ratelimit_object_match_model == ratelimit_object_match_model2

        # Convert model instance back to dict and verify no loss of data
        ratelimit_object_match_model_json2 = ratelimit_object_match_model.to_dict()
        assert ratelimit_object_match_model_json2 == ratelimit_object_match_model_json

#-----------------------------------------------------------------------------
# Test Class for RatelimitObjectMatchRequest
#-----------------------------------------------------------------------------
class TestRatelimitObjectMatchRequest():

    #--------------------------------------------------------
    # Test serialization/deserialization for RatelimitObjectMatchRequest
    #--------------------------------------------------------
    def test_ratelimit_object_match_request_serialization(self):

        # Construct a json representation of a RatelimitObjectMatchRequest model
        ratelimit_object_match_request_model_json = {}
        ratelimit_object_match_request_model_json['methods'] = ['_ALL_']
        ratelimit_object_match_request_model_json['schemes'] = ['_ALL_']
        ratelimit_object_match_request_model_json['url'] = '*.example.org/path*'

        # Construct a model instance of RatelimitObjectMatchRequest by calling from_dict on the json representation
        ratelimit_object_match_request_model = RatelimitObjectMatchRequest.from_dict(ratelimit_object_match_request_model_json)
        assert ratelimit_object_match_request_model != False

        # Construct a model instance of RatelimitObjectMatchRequest by calling from_dict on the json representation
        ratelimit_object_match_request_model_dict = RatelimitObjectMatchRequest.from_dict(ratelimit_object_match_request_model_json).__dict__
        ratelimit_object_match_request_model2 = RatelimitObjectMatchRequest(**ratelimit_object_match_request_model_dict)

        # Verify the model instances are equivalent
        assert ratelimit_object_match_request_model == ratelimit_object_match_request_model2

        # Convert model instance back to dict and verify no loss of data
        ratelimit_object_match_request_model_json2 = ratelimit_object_match_request_model.to_dict()
        assert ratelimit_object_match_request_model_json2 == ratelimit_object_match_request_model_json

#-----------------------------------------------------------------------------
# Test Class for RatelimitObjectMatchResponse
#-----------------------------------------------------------------------------
class TestRatelimitObjectMatchResponse():

    #--------------------------------------------------------
    # Test serialization/deserialization for RatelimitObjectMatchResponse
    #--------------------------------------------------------
    def test_ratelimit_object_match_response_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        ratelimit_object_match_response_headers_item_model = {} # RatelimitObjectMatchResponseHeadersItem
        ratelimit_object_match_response_headers_item_model['name'] = 'Cf-Cache-Status'
        ratelimit_object_match_response_headers_item_model['op'] = 'ne'
        ratelimit_object_match_response_headers_item_model['value'] = 'HIT'

        # Construct a json representation of a RatelimitObjectMatchResponse model
        ratelimit_object_match_response_model_json = {}
        ratelimit_object_match_response_model_json['status'] = [403]
        ratelimit_object_match_response_model_json['headers'] = [ratelimit_object_match_response_headers_item_model]
        ratelimit_object_match_response_model_json['origin_traffic'] = False

        # Construct a model instance of RatelimitObjectMatchResponse by calling from_dict on the json representation
        ratelimit_object_match_response_model = RatelimitObjectMatchResponse.from_dict(ratelimit_object_match_response_model_json)
        assert ratelimit_object_match_response_model != False

        # Construct a model instance of RatelimitObjectMatchResponse by calling from_dict on the json representation
        ratelimit_object_match_response_model_dict = RatelimitObjectMatchResponse.from_dict(ratelimit_object_match_response_model_json).__dict__
        ratelimit_object_match_response_model2 = RatelimitObjectMatchResponse(**ratelimit_object_match_response_model_dict)

        # Verify the model instances are equivalent
        assert ratelimit_object_match_response_model == ratelimit_object_match_response_model2

        # Convert model instance back to dict and verify no loss of data
        ratelimit_object_match_response_model_json2 = ratelimit_object_match_response_model.to_dict()
        assert ratelimit_object_match_response_model_json2 == ratelimit_object_match_response_model_json

#-----------------------------------------------------------------------------
# Test Class for RatelimitObjectMatchResponseHeadersItem
#-----------------------------------------------------------------------------
class TestRatelimitObjectMatchResponseHeadersItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for RatelimitObjectMatchResponseHeadersItem
    #--------------------------------------------------------
    def test_ratelimit_object_match_response_headers_item_serialization(self):

        # Construct a json representation of a RatelimitObjectMatchResponseHeadersItem model
        ratelimit_object_match_response_headers_item_model_json = {}
        ratelimit_object_match_response_headers_item_model_json['name'] = 'Cf-Cache-Status'
        ratelimit_object_match_response_headers_item_model_json['op'] = 'ne'
        ratelimit_object_match_response_headers_item_model_json['value'] = 'HIT'

        # Construct a model instance of RatelimitObjectMatchResponseHeadersItem by calling from_dict on the json representation
        ratelimit_object_match_response_headers_item_model = RatelimitObjectMatchResponseHeadersItem.from_dict(ratelimit_object_match_response_headers_item_model_json)
        assert ratelimit_object_match_response_headers_item_model != False

        # Construct a model instance of RatelimitObjectMatchResponseHeadersItem by calling from_dict on the json representation
        ratelimit_object_match_response_headers_item_model_dict = RatelimitObjectMatchResponseHeadersItem.from_dict(ratelimit_object_match_response_headers_item_model_json).__dict__
        ratelimit_object_match_response_headers_item_model2 = RatelimitObjectMatchResponseHeadersItem(**ratelimit_object_match_response_headers_item_model_dict)

        # Verify the model instances are equivalent
        assert ratelimit_object_match_response_headers_item_model == ratelimit_object_match_response_headers_item_model2

        # Convert model instance back to dict and verify no loss of data
        ratelimit_object_match_response_headers_item_model_json2 = ratelimit_object_match_response_headers_item_model.to_dict()
        assert ratelimit_object_match_response_headers_item_model_json2 == ratelimit_object_match_response_headers_item_model_json

#-----------------------------------------------------------------------------
# Test Class for DeleteRateLimitResp
#-----------------------------------------------------------------------------
class TestDeleteRateLimitResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for DeleteRateLimitResp
    #--------------------------------------------------------
    def test_delete_rate_limit_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        delete_rate_limit_resp_result_model = {} # DeleteRateLimitRespResult
        delete_rate_limit_resp_result_model['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'

        # Construct a json representation of a DeleteRateLimitResp model
        delete_rate_limit_resp_model_json = {}
        delete_rate_limit_resp_model_json['success'] = True
        delete_rate_limit_resp_model_json['errors'] = [['[]']]
        delete_rate_limit_resp_model_json['messages'] = [['[]']]
        delete_rate_limit_resp_model_json['result'] = delete_rate_limit_resp_result_model

        # Construct a model instance of DeleteRateLimitResp by calling from_dict on the json representation
        delete_rate_limit_resp_model = DeleteRateLimitResp.from_dict(delete_rate_limit_resp_model_json)
        assert delete_rate_limit_resp_model != False

        # Construct a model instance of DeleteRateLimitResp by calling from_dict on the json representation
        delete_rate_limit_resp_model_dict = DeleteRateLimitResp.from_dict(delete_rate_limit_resp_model_json).__dict__
        delete_rate_limit_resp_model2 = DeleteRateLimitResp(**delete_rate_limit_resp_model_dict)

        # Verify the model instances are equivalent
        assert delete_rate_limit_resp_model == delete_rate_limit_resp_model2

        # Convert model instance back to dict and verify no loss of data
        delete_rate_limit_resp_model_json2 = delete_rate_limit_resp_model.to_dict()
        assert delete_rate_limit_resp_model_json2 == delete_rate_limit_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for ListRatelimitResp
#-----------------------------------------------------------------------------
class TestListRatelimitResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for ListRatelimitResp
    #--------------------------------------------------------
    def test_list_ratelimit_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        ratelimit_object_match_response_headers_item_model = {} # RatelimitObjectMatchResponseHeadersItem
        ratelimit_object_match_response_headers_item_model['name'] = 'Cf-Cache-Status'
        ratelimit_object_match_response_headers_item_model['op'] = 'ne'
        ratelimit_object_match_response_headers_item_model['value'] = 'HIT'

        ratelimit_object_action_response_model = {} # RatelimitObjectActionResponse
        ratelimit_object_action_response_model['content_type'] = 'text/plain'
        ratelimit_object_action_response_model['body'] = 'This request has been rate-limited.'

        ratelimit_object_match_request_model = {} # RatelimitObjectMatchRequest
        ratelimit_object_match_request_model['methods'] = ['_ALL_']
        ratelimit_object_match_request_model['schemes'] = ['_ALL_']
        ratelimit_object_match_request_model['url'] = '*.example.org/path*'

        ratelimit_object_match_response_model = {} # RatelimitObjectMatchResponse
        ratelimit_object_match_response_model['status'] = [403]
        ratelimit_object_match_response_model['headers'] = [ratelimit_object_match_response_headers_item_model]
        ratelimit_object_match_response_model['origin_traffic'] = False

        ratelimit_object_action_model = {} # RatelimitObjectAction
        ratelimit_object_action_model['mode'] = 'simulate'
        ratelimit_object_action_model['timeout'] = 60
        ratelimit_object_action_model['response'] = ratelimit_object_action_response_model

        ratelimit_object_bypass_item_model = {} # RatelimitObjectBypassItem
        ratelimit_object_bypass_item_model['name'] = 'url'
        ratelimit_object_bypass_item_model['value'] = 'example.com/*'

        ratelimit_object_correlate_model = {} # RatelimitObjectCorrelate
        ratelimit_object_correlate_model['by'] = 'nat'

        ratelimit_object_match_model = {} # RatelimitObjectMatch
        ratelimit_object_match_model['request'] = ratelimit_object_match_request_model
        ratelimit_object_match_model['response'] = ratelimit_object_match_response_model

        list_ratelimit_resp_result_info_model = {} # ListRatelimitRespResultInfo
        list_ratelimit_resp_result_info_model['page'] = 1
        list_ratelimit_resp_result_info_model['per_page'] = 10
        list_ratelimit_resp_result_info_model['count'] = 1
        list_ratelimit_resp_result_info_model['total_count'] = 1

        ratelimit_object_model = {} # RatelimitObject
        ratelimit_object_model['id'] = '92f17202ed8bd63d69a66b86a49a8f6b'
        ratelimit_object_model['disabled'] = False
        ratelimit_object_model['description'] = 'Prevent multiple login failures to mitigate brute force attacks'
        ratelimit_object_model['bypass'] = [ratelimit_object_bypass_item_model]
        ratelimit_object_model['threshold'] = 1000
        ratelimit_object_model['period'] = 60
        ratelimit_object_model['correlate'] = ratelimit_object_correlate_model
        ratelimit_object_model['action'] = ratelimit_object_action_model
        ratelimit_object_model['match'] = ratelimit_object_match_model

        # Construct a json representation of a ListRatelimitResp model
        list_ratelimit_resp_model_json = {}
        list_ratelimit_resp_model_json['success'] = True
        list_ratelimit_resp_model_json['errors'] = [['[]']]
        list_ratelimit_resp_model_json['messages'] = [['[]']]
        list_ratelimit_resp_model_json['result'] = [ratelimit_object_model]
        list_ratelimit_resp_model_json['result_info'] = list_ratelimit_resp_result_info_model

        # Construct a model instance of ListRatelimitResp by calling from_dict on the json representation
        list_ratelimit_resp_model = ListRatelimitResp.from_dict(list_ratelimit_resp_model_json)
        assert list_ratelimit_resp_model != False

        # Construct a model instance of ListRatelimitResp by calling from_dict on the json representation
        list_ratelimit_resp_model_dict = ListRatelimitResp.from_dict(list_ratelimit_resp_model_json).__dict__
        list_ratelimit_resp_model2 = ListRatelimitResp(**list_ratelimit_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_ratelimit_resp_model == list_ratelimit_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_ratelimit_resp_model_json2 = list_ratelimit_resp_model.to_dict()
        assert list_ratelimit_resp_model_json2 == list_ratelimit_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for RatelimitObject
#-----------------------------------------------------------------------------
class TestRatelimitObject():

    #--------------------------------------------------------
    # Test serialization/deserialization for RatelimitObject
    #--------------------------------------------------------
    def test_ratelimit_object_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        ratelimit_object_match_response_headers_item_model = {} # RatelimitObjectMatchResponseHeadersItem
        ratelimit_object_match_response_headers_item_model['name'] = 'Cf-Cache-Status'
        ratelimit_object_match_response_headers_item_model['op'] = 'ne'
        ratelimit_object_match_response_headers_item_model['value'] = 'HIT'

        ratelimit_object_action_response_model = {} # RatelimitObjectActionResponse
        ratelimit_object_action_response_model['content_type'] = 'text/plain'
        ratelimit_object_action_response_model['body'] = 'This request has been rate-limited.'

        ratelimit_object_match_request_model = {} # RatelimitObjectMatchRequest
        ratelimit_object_match_request_model['methods'] = ['_ALL_']
        ratelimit_object_match_request_model['schemes'] = ['_ALL_']
        ratelimit_object_match_request_model['url'] = '*.example.org/path*'

        ratelimit_object_match_response_model = {} # RatelimitObjectMatchResponse
        ratelimit_object_match_response_model['status'] = [403]
        ratelimit_object_match_response_model['headers'] = [ratelimit_object_match_response_headers_item_model]
        ratelimit_object_match_response_model['origin_traffic'] = False

        ratelimit_object_action_model = {} # RatelimitObjectAction
        ratelimit_object_action_model['mode'] = 'simulate'
        ratelimit_object_action_model['timeout'] = 60
        ratelimit_object_action_model['response'] = ratelimit_object_action_response_model

        ratelimit_object_bypass_item_model = {} # RatelimitObjectBypassItem
        ratelimit_object_bypass_item_model['name'] = 'url'
        ratelimit_object_bypass_item_model['value'] = 'example.com/*'

        ratelimit_object_correlate_model = {} # RatelimitObjectCorrelate
        ratelimit_object_correlate_model['by'] = 'nat'

        ratelimit_object_match_model = {} # RatelimitObjectMatch
        ratelimit_object_match_model['request'] = ratelimit_object_match_request_model
        ratelimit_object_match_model['response'] = ratelimit_object_match_response_model

        # Construct a json representation of a RatelimitObject model
        ratelimit_object_model_json = {}
        ratelimit_object_model_json['id'] = '92f17202ed8bd63d69a66b86a49a8f6b'
        ratelimit_object_model_json['disabled'] = False
        ratelimit_object_model_json['description'] = 'Prevent multiple login failures to mitigate brute force attacks'
        ratelimit_object_model_json['bypass'] = [ratelimit_object_bypass_item_model]
        ratelimit_object_model_json['threshold'] = 1000
        ratelimit_object_model_json['period'] = 60
        ratelimit_object_model_json['correlate'] = ratelimit_object_correlate_model
        ratelimit_object_model_json['action'] = ratelimit_object_action_model
        ratelimit_object_model_json['match'] = ratelimit_object_match_model

        # Construct a model instance of RatelimitObject by calling from_dict on the json representation
        ratelimit_object_model = RatelimitObject.from_dict(ratelimit_object_model_json)
        assert ratelimit_object_model != False

        # Construct a model instance of RatelimitObject by calling from_dict on the json representation
        ratelimit_object_model_dict = RatelimitObject.from_dict(ratelimit_object_model_json).__dict__
        ratelimit_object_model2 = RatelimitObject(**ratelimit_object_model_dict)

        # Verify the model instances are equivalent
        assert ratelimit_object_model == ratelimit_object_model2

        # Convert model instance back to dict and verify no loss of data
        ratelimit_object_model_json2 = ratelimit_object_model.to_dict()
        assert ratelimit_object_model_json2 == ratelimit_object_model_json

#-----------------------------------------------------------------------------
# Test Class for RatelimitResp
#-----------------------------------------------------------------------------
class TestRatelimitResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for RatelimitResp
    #--------------------------------------------------------
    def test_ratelimit_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        ratelimit_object_match_response_headers_item_model = {} # RatelimitObjectMatchResponseHeadersItem
        ratelimit_object_match_response_headers_item_model['name'] = 'Cf-Cache-Status'
        ratelimit_object_match_response_headers_item_model['op'] = 'ne'
        ratelimit_object_match_response_headers_item_model['value'] = 'HIT'

        ratelimit_object_action_response_model = {} # RatelimitObjectActionResponse
        ratelimit_object_action_response_model['content_type'] = 'text/plain'
        ratelimit_object_action_response_model['body'] = 'This request has been rate-limited.'

        ratelimit_object_match_request_model = {} # RatelimitObjectMatchRequest
        ratelimit_object_match_request_model['methods'] = ['_ALL_']
        ratelimit_object_match_request_model['schemes'] = ['_ALL_']
        ratelimit_object_match_request_model['url'] = '*.example.org/path*'

        ratelimit_object_match_response_model = {} # RatelimitObjectMatchResponse
        ratelimit_object_match_response_model['status'] = [403]
        ratelimit_object_match_response_model['headers'] = [ratelimit_object_match_response_headers_item_model]
        ratelimit_object_match_response_model['origin_traffic'] = False

        ratelimit_object_action_model = {} # RatelimitObjectAction
        ratelimit_object_action_model['mode'] = 'simulate'
        ratelimit_object_action_model['timeout'] = 60
        ratelimit_object_action_model['response'] = ratelimit_object_action_response_model

        ratelimit_object_bypass_item_model = {} # RatelimitObjectBypassItem
        ratelimit_object_bypass_item_model['name'] = 'url'
        ratelimit_object_bypass_item_model['value'] = 'example.com/*'

        ratelimit_object_correlate_model = {} # RatelimitObjectCorrelate
        ratelimit_object_correlate_model['by'] = 'nat'

        ratelimit_object_match_model = {} # RatelimitObjectMatch
        ratelimit_object_match_model['request'] = ratelimit_object_match_request_model
        ratelimit_object_match_model['response'] = ratelimit_object_match_response_model

        ratelimit_object_model = {} # RatelimitObject
        ratelimit_object_model['id'] = '92f17202ed8bd63d69a66b86a49a8f6b'
        ratelimit_object_model['disabled'] = False
        ratelimit_object_model['description'] = 'Prevent multiple login failures to mitigate brute force attacks'
        ratelimit_object_model['bypass'] = [ratelimit_object_bypass_item_model]
        ratelimit_object_model['threshold'] = 1000
        ratelimit_object_model['period'] = 60
        ratelimit_object_model['correlate'] = ratelimit_object_correlate_model
        ratelimit_object_model['action'] = ratelimit_object_action_model
        ratelimit_object_model['match'] = ratelimit_object_match_model

        # Construct a json representation of a RatelimitResp model
        ratelimit_resp_model_json = {}
        ratelimit_resp_model_json['success'] = True
        ratelimit_resp_model_json['errors'] = [['[]']]
        ratelimit_resp_model_json['messages'] = [['[]']]
        ratelimit_resp_model_json['result'] = ratelimit_object_model

        # Construct a model instance of RatelimitResp by calling from_dict on the json representation
        ratelimit_resp_model = RatelimitResp.from_dict(ratelimit_resp_model_json)
        assert ratelimit_resp_model != False

        # Construct a model instance of RatelimitResp by calling from_dict on the json representation
        ratelimit_resp_model_dict = RatelimitResp.from_dict(ratelimit_resp_model_json).__dict__
        ratelimit_resp_model2 = RatelimitResp(**ratelimit_resp_model_dict)

        # Verify the model instances are equivalent
        assert ratelimit_resp_model == ratelimit_resp_model2

        # Convert model instance back to dict and verify no loss of data
        ratelimit_resp_model_json2 = ratelimit_resp_model.to_dict()
        assert ratelimit_resp_model_json2 == ratelimit_resp_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
