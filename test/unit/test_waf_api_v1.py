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
from ibm_cloud_networking_services.waf_api_v1 import WafApiV1

crn = 'testString'
zone_id = 'testString'

service = WafApiV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn,
    zone_id=zone_id
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: WAF
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_waf_settings
#-----------------------------------------------------------------------------
class TestGetWafSettings():

    #--------------------------------------------------------
    # get_waf_settings()
    #--------------------------------------------------------
    @responses.activate
    def test_get_waf_settings_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/waf'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "waf", "value": "true", "editable": true, "modified_on": "2018-01-10T05:13:13.967946Z"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_waf_settings()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_waf_settings_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_waf_settings_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/waf'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "waf", "value": "true", "editable": true, "modified_on": "2018-01-10T05:13:13.967946Z"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_waf_settings()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for update_waf_settings
#-----------------------------------------------------------------------------
class TestUpdateWafSettings():

    #--------------------------------------------------------
    # update_waf_settings()
    #--------------------------------------------------------
    @responses.activate
    def test_update_waf_settings_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/waf'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "waf", "value": "true", "editable": true, "modified_on": "2018-01-10T05:13:13.967946Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'on'

        # Invoke method
        response = service.update_waf_settings(
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_waf_settings_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_waf_settings_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/waf'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "waf", "value": "true", "editable": true, "modified_on": "2018-01-10T05:13:13.967946Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_waf_settings()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: WAF
##############################################################################

