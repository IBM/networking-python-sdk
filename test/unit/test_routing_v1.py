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
import re
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

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_smart_routing()
    #--------------------------------------------------------
    @responses.activate
    def test_get_smart_routing_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/routing/smart_routing')
        mock_response = '{"result": {"id": "smart_routing", "value": "off", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
    # test_get_smart_routing_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_smart_routing_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/routing/smart_routing')
        mock_response = '{"result": {"id": "smart_routing", "value": "off", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                service.get_smart_routing(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_smart_routing
#-----------------------------------------------------------------------------
class TestUpdateSmartRouting():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_smart_routing()
    #--------------------------------------------------------
    @responses.activate
    def test_update_smart_routing_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/routing/smart_routing')
        mock_response = '{"result": {"id": "smart_routing", "value": "off", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'off'

        # Invoke method
        response = service.update_smart_routing(
            value=value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'off'


    #--------------------------------------------------------
    # test_update_smart_routing_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_smart_routing_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/routing/smart_routing')
        mock_response = '{"result": {"id": "smart_routing", "value": "off", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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


    #--------------------------------------------------------
    # test_update_smart_routing_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_smart_routing_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/routing/smart_routing')
        mock_response = '{"result": {"id": "smart_routing", "value": "off", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(responses.PATCH,
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
                service.update_smart_routing(**req_copy)



# endregion
##############################################################################
# End of Service: Routing
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for SmartRoutingRespResult
#-----------------------------------------------------------------------------
class TestSmartRoutingRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for SmartRoutingRespResult
    #--------------------------------------------------------
    def test_smart_routing_resp_result_serialization(self):

        # Construct a json representation of a SmartRoutingRespResult model
        smart_routing_resp_result_model_json = {}
        smart_routing_resp_result_model_json['id'] = 'smart_routing'
        smart_routing_resp_result_model_json['value'] = 'off'
        smart_routing_resp_result_model_json['editable'] = True
        smart_routing_resp_result_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of SmartRoutingRespResult by calling from_dict on the json representation
        smart_routing_resp_result_model = SmartRoutingRespResult.from_dict(smart_routing_resp_result_model_json)
        assert smart_routing_resp_result_model != False

        # Construct a model instance of SmartRoutingRespResult by calling from_dict on the json representation
        smart_routing_resp_result_model_dict = SmartRoutingRespResult.from_dict(smart_routing_resp_result_model_json).__dict__
        smart_routing_resp_result_model2 = SmartRoutingRespResult(**smart_routing_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert smart_routing_resp_result_model == smart_routing_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        smart_routing_resp_result_model_json2 = smart_routing_resp_result_model.to_dict()
        assert smart_routing_resp_result_model_json2 == smart_routing_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for SmartRoutingResp
#-----------------------------------------------------------------------------
class TestSmartRoutingResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for SmartRoutingResp
    #--------------------------------------------------------
    def test_smart_routing_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        smart_routing_resp_result_model = {} # SmartRoutingRespResult
        smart_routing_resp_result_model['id'] = 'smart_routing'
        smart_routing_resp_result_model['value'] = 'off'
        smart_routing_resp_result_model['editable'] = True
        smart_routing_resp_result_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a SmartRoutingResp model
        smart_routing_resp_model_json = {}
        smart_routing_resp_model_json['result'] = smart_routing_resp_result_model
        smart_routing_resp_model_json['success'] = True
        smart_routing_resp_model_json['errors'] = [['testString']]
        smart_routing_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of SmartRoutingResp by calling from_dict on the json representation
        smart_routing_resp_model = SmartRoutingResp.from_dict(smart_routing_resp_model_json)
        assert smart_routing_resp_model != False

        # Construct a model instance of SmartRoutingResp by calling from_dict on the json representation
        smart_routing_resp_model_dict = SmartRoutingResp.from_dict(smart_routing_resp_model_json).__dict__
        smart_routing_resp_model2 = SmartRoutingResp(**smart_routing_resp_model_dict)

        # Verify the model instances are equivalent
        assert smart_routing_resp_model == smart_routing_resp_model2

        # Convert model instance back to dict and verify no loss of data
        smart_routing_resp_model_json2 = smart_routing_resp_model.to_dict()
        assert smart_routing_resp_model_json2 == smart_routing_resp_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
