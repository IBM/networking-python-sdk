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
from ibm_cloud_networking_services.routing_v1 import *

crn = 'testString'
zone_identifier = 'testString'

service = RoutingV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn,
    zone_identifier=zone_identifier
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: Routing
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_smart_routing
#-----------------------------------------------------------------------------
class TestGetSmartRouting():

    #--------------------------------------------------------
    # get_smart_routing()
    #--------------------------------------------------------
    @responses.activate
    def test_get_smart_routing_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/routing/smart_routing'
        mock_response = '{"result": {"id": "smart_routing", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_smart_routing()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_smart_routing_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_smart_routing_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/routing/smart_routing'
        mock_response = '{"result": {"id": "smart_routing", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_smart_routing()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for update_smart_routing
#-----------------------------------------------------------------------------
class TestUpdateSmartRouting():

    #--------------------------------------------------------
    # update_smart_routing()
    #--------------------------------------------------------
    @responses.activate
    def test_update_smart_routing_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/routing/smart_routing'
        mock_response = '{"result": {"id": "smart_routing", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'false'

        # Invoke method
        response = service.update_smart_routing(
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_update_smart_routing_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_smart_routing_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/routing/smart_routing'
        mock_response = '{"result": {"id": "smart_routing", "value": "false", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.update_smart_routing()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: Routing
##############################################################################

