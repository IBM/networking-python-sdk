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
from ibm_cloud_networking_services.firewall_api_v1 import *

crn = 'testString'
zone_identifier = 'testString'

service = FirewallApiV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn,
    zone_identifier=zone_identifier
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: SecurityLevelSetting
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_security_level_setting
#-----------------------------------------------------------------------------
class TestGetSecurityLevelSetting():

    #--------------------------------------------------------
    # get_security_level_setting()
    #--------------------------------------------------------
    @responses.activate
    def test_get_security_level_setting_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/security_level'
        mock_response = '{"result": {"id": "security_level", "value": "medium", "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}, "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_security_level_setting()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_security_level_setting_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_security_level_setting_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/security_level'
        mock_response = '{"result": {"id": "security_level", "value": "medium", "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}, "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_security_level_setting()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for set_security_level_setting
#-----------------------------------------------------------------------------
class TestSetSecurityLevelSetting():

    #--------------------------------------------------------
    # set_security_level_setting()
    #--------------------------------------------------------
    @responses.activate
    def test_set_security_level_setting_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/security_level'
        mock_response = '{"result": {"id": "security_level", "value": "medium", "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}, "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'under_attack'

        # Invoke method
        response = service.set_security_level_setting(
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_set_security_level_setting_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_set_security_level_setting_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/security_level'
        mock_response = '{"result": {"id": "security_level", "value": "medium", "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}, "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.set_security_level_setting()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: SecurityLevelSetting
##############################################################################

