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
from ibm_cloud_networking_services.waf_api_v1 import *

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

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_waf_settings()
    #--------------------------------------------------------
    @responses.activate
    def test_get_waf_settings_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/waf')
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
    # test_get_waf_settings_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_waf_settings_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/waf')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "waf", "value": "true", "editable": true, "modified_on": "2018-01-10T05:13:13.967946Z"}}'
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
                service.get_waf_settings(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_waf_settings
#-----------------------------------------------------------------------------
class TestUpdateWafSettings():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_waf_settings()
    #--------------------------------------------------------
    @responses.activate
    def test_update_waf_settings_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/waf')
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
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'on'


    #--------------------------------------------------------
    # test_update_waf_settings_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_waf_settings_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/waf')
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


    #--------------------------------------------------------
    # test_update_waf_settings_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_waf_settings_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/waf')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "waf", "value": "true", "editable": true, "modified_on": "2018-01-10T05:13:13.967946Z"}}'
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
                service.update_waf_settings(**req_copy)



# endregion
##############################################################################
# End of Service: WAF
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for WafResponseResult
#-----------------------------------------------------------------------------
class TestWafResponseResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for WafResponseResult
    #--------------------------------------------------------
    def test_waf_response_result_serialization(self):

        # Construct a json representation of a WafResponseResult model
        waf_response_result_model_json = {}
        waf_response_result_model_json['id'] = 'waf'
        waf_response_result_model_json['value'] = 'true'
        waf_response_result_model_json['editable'] = True
        waf_response_result_model_json['modified_on'] = '2018-01-10T05:13:13.967946Z'

        # Construct a model instance of WafResponseResult by calling from_dict on the json representation
        waf_response_result_model = WafResponseResult.from_dict(waf_response_result_model_json)
        assert waf_response_result_model != False

        # Construct a model instance of WafResponseResult by calling from_dict on the json representation
        waf_response_result_model_dict = WafResponseResult.from_dict(waf_response_result_model_json).__dict__
        waf_response_result_model2 = WafResponseResult(**waf_response_result_model_dict)

        # Verify the model instances are equivalent
        assert waf_response_result_model == waf_response_result_model2

        # Convert model instance back to dict and verify no loss of data
        waf_response_result_model_json2 = waf_response_result_model.to_dict()
        assert waf_response_result_model_json2 == waf_response_result_model_json

#-----------------------------------------------------------------------------
# Test Class for WafResponse
#-----------------------------------------------------------------------------
class TestWafResponse():

    #--------------------------------------------------------
    # Test serialization/deserialization for WafResponse
    #--------------------------------------------------------
    def test_waf_response_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        waf_response_result_model = {} # WafResponseResult
        waf_response_result_model['id'] = 'waf'
        waf_response_result_model['value'] = 'true'
        waf_response_result_model['editable'] = True
        waf_response_result_model['modified_on'] = '2018-01-10T05:13:13.967946Z'

        # Construct a json representation of a WafResponse model
        waf_response_model_json = {}
        waf_response_model_json['success'] = True
        waf_response_model_json['errors'] = [['testString']]
        waf_response_model_json['messages'] = [['testString']]
        waf_response_model_json['result'] = waf_response_result_model

        # Construct a model instance of WafResponse by calling from_dict on the json representation
        waf_response_model = WafResponse.from_dict(waf_response_model_json)
        assert waf_response_model != False

        # Construct a model instance of WafResponse by calling from_dict on the json representation
        waf_response_model_dict = WafResponse.from_dict(waf_response_model_json).__dict__
        waf_response_model2 = WafResponse(**waf_response_model_dict)

        # Verify the model instances are equivalent
        assert waf_response_model == waf_response_model2

        # Convert model instance back to dict and verify no loss of data
        waf_response_model_json2 = waf_response_model.to_dict()
        assert waf_response_model_json2 == waf_response_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
