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
from ibm_cloud_networking_services import CustomPagesV1

crn = 'testString'
zone_identifier = 'testString'

service = CustomPagesV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn,
    zone_identifier=zone_identifier
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: ListInstanceCustomPages
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_instance_custom_pages
#-----------------------------------------------------------------------------
class TestListInstanceCustomPages():

    #--------------------------------------------------------
    # list_instance_custom_pages()
    #--------------------------------------------------------
    @responses.activate
    def test_list_instance_custom_pages_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/custom_pages'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "basic_challenge", "description": "Basic Challenge", "required_tokens": ["::CAPTCHA_BOX::"], "preview_target": "block:basic-sec-captcha", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "url": "https://www.example.com/basic_challenge_error.html", "state": "customized"}], "result_info": {"page": 1, "per_page": 20, "total_pages": 1, "count": 10, "total_count": 10}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_instance_custom_pages()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_instance_custom_pages_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_instance_custom_pages_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/custom_pages'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "basic_challenge", "description": "Basic Challenge", "required_tokens": ["::CAPTCHA_BOX::"], "preview_target": "block:basic-sec-captcha", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "url": "https://www.example.com/basic_challenge_error.html", "state": "customized"}], "result_info": {"page": 1, "per_page": 20, "total_pages": 1, "count": 10, "total_count": 10}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_instance_custom_pages()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: ListInstanceCustomPages
##############################################################################

##############################################################################
# Start of Service: GetACustomPageForAGivenInstance
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_instance_custom_page
#-----------------------------------------------------------------------------
class TestGetInstanceCustomPage():

    #--------------------------------------------------------
    # get_instance_custom_page()
    #--------------------------------------------------------
    @responses.activate
    def test_get_instance_custom_page_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/custom_pages/basic_challenge'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "basic_challenge", "description": "Basic Challenge", "required_tokens": ["::CAPTCHA_BOX::"], "preview_target": "block:basic-sec-captcha", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "url": "https://www.example.com/basic_challenge_error.html", "state": "customized"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        page_identifier = 'basic_challenge'

        # Invoke method
        response = service.get_instance_custom_page(
            page_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_instance_custom_page_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_instance_custom_page_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/custom_pages/basic_challenge'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "basic_challenge", "description": "Basic Challenge", "required_tokens": ["::CAPTCHA_BOX::"], "preview_target": "block:basic-sec-captcha", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "url": "https://www.example.com/basic_challenge_error.html", "state": "customized"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        page_identifier = 'basic_challenge'

        # Invoke method
        response = service.get_instance_custom_page(
            page_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetACustomPageForAGivenInstance
##############################################################################

##############################################################################
# Start of Service: UpdateACustomPageForAGivenInstance
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_instance_custom_page
#-----------------------------------------------------------------------------
class TestUpdateInstanceCustomPage():

    #--------------------------------------------------------
    # update_instance_custom_page()
    #--------------------------------------------------------
    @responses.activate
    def test_update_instance_custom_page_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/custom_pages/basic_challenge'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "basic_challenge", "description": "Basic Challenge", "required_tokens": ["::CAPTCHA_BOX::"], "preview_target": "block:basic-sec-captcha", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "url": "https://www.example.com/basic_challenge_error.html", "state": "customized"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        page_identifier = 'basic_challenge'
        url = 'https://www.example.com/basic_challenge_error.html'
        state = 'customized'

        # Invoke method
        response = service.update_instance_custom_page(
            page_identifier,
            url=url,
            state=state,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['url'] == url
        assert req_body['state'] == state


    #--------------------------------------------------------
    # test_update_instance_custom_page_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_instance_custom_page_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/custom_pages/basic_challenge'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "basic_challenge", "description": "Basic Challenge", "required_tokens": ["::CAPTCHA_BOX::"], "preview_target": "block:basic-sec-captcha", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "url": "https://www.example.com/basic_challenge_error.html", "state": "customized"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        page_identifier = 'basic_challenge'

        # Invoke method
        response = service.update_instance_custom_page(
            page_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateACustomPageForAGivenInstance
##############################################################################

##############################################################################
# Start of Service: ListZoneCustomPages
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_zone_custom_pages
#-----------------------------------------------------------------------------
class TestListZoneCustomPages():

    #--------------------------------------------------------
    # list_zone_custom_pages()
    #--------------------------------------------------------
    @responses.activate
    def test_list_zone_custom_pages_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/custom_pages'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "basic_challenge", "description": "Basic Challenge", "required_tokens": ["::CAPTCHA_BOX::"], "preview_target": "block:basic-sec-captcha", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "url": "https://www.example.com/basic_challenge_error.html", "state": "customized"}], "result_info": {"page": 1, "per_page": 20, "total_pages": 1, "count": 10, "total_count": 10}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_zone_custom_pages()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_zone_custom_pages_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_zone_custom_pages_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/custom_pages'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "basic_challenge", "description": "Basic Challenge", "required_tokens": ["::CAPTCHA_BOX::"], "preview_target": "block:basic-sec-captcha", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "url": "https://www.example.com/basic_challenge_error.html", "state": "customized"}], "result_info": {"page": 1, "per_page": 20, "total_pages": 1, "count": 10, "total_count": 10}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_zone_custom_pages()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: ListZoneCustomPages
##############################################################################

##############################################################################
# Start of Service: GetACustomPageForAGivenZone
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_zone_custom_page
#-----------------------------------------------------------------------------
class TestGetZoneCustomPage():

    #--------------------------------------------------------
    # get_zone_custom_page()
    #--------------------------------------------------------
    @responses.activate
    def test_get_zone_custom_page_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/custom_pages/basic_challenge'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "basic_challenge", "description": "Basic Challenge", "required_tokens": ["::CAPTCHA_BOX::"], "preview_target": "block:basic-sec-captcha", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "url": "https://www.example.com/basic_challenge_error.html", "state": "customized"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        page_identifier = 'basic_challenge'

        # Invoke method
        response = service.get_zone_custom_page(
            page_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_zone_custom_page_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_zone_custom_page_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/custom_pages/basic_challenge'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "basic_challenge", "description": "Basic Challenge", "required_tokens": ["::CAPTCHA_BOX::"], "preview_target": "block:basic-sec-captcha", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "url": "https://www.example.com/basic_challenge_error.html", "state": "customized"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        page_identifier = 'basic_challenge'

        # Invoke method
        response = service.get_zone_custom_page(
            page_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: GetACustomPageForAGivenZone
##############################################################################

##############################################################################
# Start of Service: UpdateACustomPageForAGivenZone
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for update_zone_custom_page
#-----------------------------------------------------------------------------
class TestUpdateZoneCustomPage():

    #--------------------------------------------------------
    # update_zone_custom_page()
    #--------------------------------------------------------
    @responses.activate
    def test_update_zone_custom_page_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/custom_pages/basic_challenge'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "basic_challenge", "description": "Basic Challenge", "required_tokens": ["::CAPTCHA_BOX::"], "preview_target": "block:basic-sec-captcha", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "url": "https://www.example.com/basic_challenge_error.html", "state": "customized"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        page_identifier = 'basic_challenge'
        url = 'https://www.example.com/basic_challenge_error.html'
        state = 'customized'

        # Invoke method
        response = service.update_zone_custom_page(
            page_identifier,
            url=url,
            state=state,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['url'] == url
        assert req_body['state'] == state


    #--------------------------------------------------------
    # test_update_zone_custom_page_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_zone_custom_page_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/custom_pages/basic_challenge'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "basic_challenge", "description": "Basic Challenge", "required_tokens": ["::CAPTCHA_BOX::"], "preview_target": "block:basic-sec-captcha", "created_on": "2019-01-01T12:00:00", "modified_on": "2019-01-01T12:00:00", "url": "https://www.example.com/basic_challenge_error.html", "state": "customized"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        page_identifier = 'basic_challenge'

        # Invoke method
        response = service.update_zone_custom_page(
            page_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: UpdateACustomPageForAGivenZone
##############################################################################

