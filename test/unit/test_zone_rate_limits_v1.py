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

    #--------------------------------------------------------
    # list_all_zone_rate_limits()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_zone_rate_limits_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/rate_limits'
        mock_response = '{"success": true, "errors": [["[]"]], "messages": [["[]"]], "result": [{"id": "92f17202ed8bd63d69a66b86a49a8f6b", "disabled": false, "description": "Prevent multiple login failures to mitigate brute force attacks", "bypass": [{"name": "url", "value": "example.com/*"}], "threshold": 1000, "period": 60, "correlate": {"by": "nat"}, "action": {"mode": "simulate", "timeout": 60, "response": {"content_type": "text/plain", "body": "This request has been rate-limited."}}, "match": {"request": {"methods": ["_ALL_"], "schemes": ["_ALL_"], "url": "*.example.org/path*"}, "response": {"status": [403], "headers": [{"name": "Cf-Cache-Status", "op": "ne", "value": "HIT"}], "origin_traffic": false}}}], "result_info": {"page": 1, "per_page": 10, "count": 1, "total_count": 1}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        page = 38
        per_page = 38

        # Invoke method
        response = service.list_all_zone_rate_limits(
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
    # test_list_all_zone_rate_limits_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_zone_rate_limits_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/rate_limits'
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


#-----------------------------------------------------------------------------
# Test Class for create_zone_rate_limits
#-----------------------------------------------------------------------------
class TestCreateZoneRateLimits():

    #--------------------------------------------------------
    # create_zone_rate_limits()
    #--------------------------------------------------------
    @responses.activate
    def test_create_zone_rate_limits_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/rate_limits'
        mock_response = '{"success": true, "errors": [["[]"]], "messages": [["[]"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "disabled": false, "description": "Prevent multiple login failures to mitigate brute force attacks", "bypass": [{"name": "url", "value": "example.com/*"}], "threshold": 1000, "period": 60, "correlate": {"by": "nat"}, "action": {"mode": "simulate", "timeout": 60, "response": {"content_type": "text/plain", "body": "This request has been rate-limited."}}, "match": {"request": {"methods": ["_ALL_"], "schemes": ["_ALL_"], "url": "*.example.org/path*"}, "response": {"status": [403], "headers": [{"name": "Cf-Cache-Status", "op": "ne", "value": "HIT"}], "origin_traffic": false}}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a RatelimitInputActionResponse model
        ratelimit_input_action_response_model =  {
            'content_type': 'text/plain',
            'body': 'This request has been rate-limited.'
        }
        # Construct a dict representation of a RatelimitInputAction model
        ratelimit_input_action_model =  {
            'mode': 'simulate',
            'timeout': 60,
            'response': ratelimit_input_action_response_model
        }
        # Construct a dict representation of a RatelimitInputMatchResponseHeadersItem model
        ratelimit_input_match_response_headers_item_model =  {
            'name': 'Cf-Cache-Status',
            'op': 'ne',
            'value': 'HIT'
        }
        # Construct a dict representation of a RatelimitInputMatchRequest model
        ratelimit_input_match_request_model =  {
            'methods': ['GET'],
            'schemes': ['HTTP'],
            'url': '*.example.org/path*'
        }
        # Construct a dict representation of a RatelimitInputMatchResponse model
        ratelimit_input_match_response_model =  {
            'status': [403],
            'headers': [ratelimit_input_match_response_headers_item_model],
            'origin_traffic': False
        }
        # Construct a dict representation of a RatelimitInputMatch model
        ratelimit_input_match_model =  {
            'request': ratelimit_input_match_request_model,
            'response': ratelimit_input_match_response_model
        }
        # Construct a dict representation of a RatelimitInputBypassItem model
        ratelimit_input_bypass_item_model =  {
            'name': 'url',
            'value': 'api.example.com/*'
        }
        # Construct a dict representation of a RatelimitInputCorrelate model
        ratelimit_input_correlate_model =  {
            'by': 'nat'
        }

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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['threshold'] == threshold
        assert req_body['period'] == period
        assert req_body['action'] == action
        assert req_body['match'] == match
        assert req_body['disabled'] == disabled
        assert req_body['description'] == description
        assert req_body['bypass'] == bypass
        assert req_body['correlate'] == correlate


    #--------------------------------------------------------
    # test_create_zone_rate_limits_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_zone_rate_limits_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/rate_limits'
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


#-----------------------------------------------------------------------------
# Test Class for delete_zone_rate_limit
#-----------------------------------------------------------------------------
class TestDeleteZoneRateLimit():

    #--------------------------------------------------------
    # delete_zone_rate_limit()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_zone_rate_limit_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/rate_limits/testString'
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
            rate_limit_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_zone_rate_limit_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_zone_rate_limit_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/rate_limits/testString'
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
            rate_limit_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_rate_limit
#-----------------------------------------------------------------------------
class TestGetRateLimit():

    #--------------------------------------------------------
    # get_rate_limit()
    #--------------------------------------------------------
    @responses.activate
    def test_get_rate_limit_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/rate_limits/testString'
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
            rate_limit_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_rate_limit_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_rate_limit_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/rate_limits/testString'
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
            rate_limit_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for update_rate_limit
#-----------------------------------------------------------------------------
class TestUpdateRateLimit():

    #--------------------------------------------------------
    # update_rate_limit()
    #--------------------------------------------------------
    @responses.activate
    def test_update_rate_limit_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/rate_limits/testString'
        mock_response = '{"success": true, "errors": [["[]"]], "messages": [["[]"]], "result": {"id": "92f17202ed8bd63d69a66b86a49a8f6b", "disabled": false, "description": "Prevent multiple login failures to mitigate brute force attacks", "bypass": [{"name": "url", "value": "example.com/*"}], "threshold": 1000, "period": 60, "correlate": {"by": "nat"}, "action": {"mode": "simulate", "timeout": 60, "response": {"content_type": "text/plain", "body": "This request has been rate-limited."}}, "match": {"request": {"methods": ["_ALL_"], "schemes": ["_ALL_"], "url": "*.example.org/path*"}, "response": {"status": [403], "headers": [{"name": "Cf-Cache-Status", "op": "ne", "value": "HIT"}], "origin_traffic": false}}}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a RatelimitInputActionResponse model
        ratelimit_input_action_response_model =  {
            'content_type': 'text/plain',
            'body': 'This request has been rate-limited.'
        }
        # Construct a dict representation of a RatelimitInputAction model
        ratelimit_input_action_model =  {
            'mode': 'simulate',
            'timeout': 60,
            'response': ratelimit_input_action_response_model
        }
        # Construct a dict representation of a RatelimitInputMatchResponseHeadersItem model
        ratelimit_input_match_response_headers_item_model =  {
            'name': 'Cf-Cache-Status',
            'op': 'ne',
            'value': 'HIT'
        }
        # Construct a dict representation of a RatelimitInputMatchRequest model
        ratelimit_input_match_request_model =  {
            'methods': ['GET'],
            'schemes': ['HTTP'],
            'url': '*.example.org/path*'
        }
        # Construct a dict representation of a RatelimitInputMatchResponse model
        ratelimit_input_match_response_model =  {
            'status': [403],
            'headers': [ratelimit_input_match_response_headers_item_model],
            'origin_traffic': False
        }
        # Construct a dict representation of a RatelimitInputMatch model
        ratelimit_input_match_model =  {
            'request': ratelimit_input_match_request_model,
            'response': ratelimit_input_match_response_model
        }
        # Construct a dict representation of a RatelimitInputBypassItem model
        ratelimit_input_bypass_item_model =  {
            'name': 'url',
            'value': 'api.example.com/*'
        }
        # Construct a dict representation of a RatelimitInputCorrelate model
        ratelimit_input_correlate_model =  {
            'by': 'nat'
        }

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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['threshold'] == threshold
        assert req_body['period'] == period
        assert req_body['action'] == action
        assert req_body['match'] == match
        assert req_body['disabled'] == disabled
        assert req_body['description'] == description
        assert req_body['bypass'] == bypass
        assert req_body['correlate'] == correlate


    #--------------------------------------------------------
    # test_update_rate_limit_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_rate_limit_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/rate_limits/testString'
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
            rate_limit_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: ZoneRateLimits
##############################################################################

