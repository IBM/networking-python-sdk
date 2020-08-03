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

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_security_level_setting()
    #--------------------------------------------------------
    @responses.activate
    def test_get_security_level_setting_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/security_level')
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
    # test_get_security_level_setting_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_security_level_setting_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/security_level')
        mock_response = '{"result": {"id": "security_level", "value": "medium", "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}, "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
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
                service.get_security_level_setting(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for set_security_level_setting
#-----------------------------------------------------------------------------
class TestSetSecurityLevelSetting():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # set_security_level_setting()
    #--------------------------------------------------------
    @responses.activate
    def test_set_security_level_setting_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/security_level')
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
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'under_attack'


    #--------------------------------------------------------
    # test_set_security_level_setting_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_set_security_level_setting_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/security_level')
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


    #--------------------------------------------------------
    # test_set_security_level_setting_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_set_security_level_setting_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/security_level')
        mock_response = '{"result": {"id": "security_level", "value": "medium", "editable": true, "modified_on": "2014-01-01T05:20:00.12345Z"}, "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
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
                service.set_security_level_setting(**req_copy)



# endregion
##############################################################################
# End of Service: SecurityLevelSetting
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for SecurityLevelSettingRespMessagesItem
#-----------------------------------------------------------------------------
class TestSecurityLevelSettingRespMessagesItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for SecurityLevelSettingRespMessagesItem
    #--------------------------------------------------------
    def test_security_level_setting_resp_messages_item_serialization(self):

        # Construct a json representation of a SecurityLevelSettingRespMessagesItem model
        security_level_setting_resp_messages_item_model_json = {}
        security_level_setting_resp_messages_item_model_json['status'] = 'OK'

        # Construct a model instance of SecurityLevelSettingRespMessagesItem by calling from_dict on the json representation
        security_level_setting_resp_messages_item_model = SecurityLevelSettingRespMessagesItem.from_dict(security_level_setting_resp_messages_item_model_json)
        assert security_level_setting_resp_messages_item_model != False

        # Construct a model instance of SecurityLevelSettingRespMessagesItem by calling from_dict on the json representation
        security_level_setting_resp_messages_item_model_dict = SecurityLevelSettingRespMessagesItem.from_dict(security_level_setting_resp_messages_item_model_json).__dict__
        security_level_setting_resp_messages_item_model2 = SecurityLevelSettingRespMessagesItem(**security_level_setting_resp_messages_item_model_dict)

        # Verify the model instances are equivalent
        assert security_level_setting_resp_messages_item_model == security_level_setting_resp_messages_item_model2

        # Convert model instance back to dict and verify no loss of data
        security_level_setting_resp_messages_item_model_json2 = security_level_setting_resp_messages_item_model.to_dict()
        assert security_level_setting_resp_messages_item_model_json2 == security_level_setting_resp_messages_item_model_json

#-----------------------------------------------------------------------------
# Test Class for SecurityLevelSettingRespResult
#-----------------------------------------------------------------------------
class TestSecurityLevelSettingRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for SecurityLevelSettingRespResult
    #--------------------------------------------------------
    def test_security_level_setting_resp_result_serialization(self):

        # Construct a json representation of a SecurityLevelSettingRespResult model
        security_level_setting_resp_result_model_json = {}
        security_level_setting_resp_result_model_json['id'] = 'security_level'
        security_level_setting_resp_result_model_json['value'] = 'medium'
        security_level_setting_resp_result_model_json['editable'] = True
        security_level_setting_resp_result_model_json['modified_on'] = '2014-01-01T05:20:00.12345Z'

        # Construct a model instance of SecurityLevelSettingRespResult by calling from_dict on the json representation
        security_level_setting_resp_result_model = SecurityLevelSettingRespResult.from_dict(security_level_setting_resp_result_model_json)
        assert security_level_setting_resp_result_model != False

        # Construct a model instance of SecurityLevelSettingRespResult by calling from_dict on the json representation
        security_level_setting_resp_result_model_dict = SecurityLevelSettingRespResult.from_dict(security_level_setting_resp_result_model_json).__dict__
        security_level_setting_resp_result_model2 = SecurityLevelSettingRespResult(**security_level_setting_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert security_level_setting_resp_result_model == security_level_setting_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        security_level_setting_resp_result_model_json2 = security_level_setting_resp_result_model.to_dict()
        assert security_level_setting_resp_result_model_json2 == security_level_setting_resp_result_model_json

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
        result_info_model_json['per_page'] = 2
        result_info_model_json['count'] = 1
        result_info_model_json['total_count'] = 200

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

#-----------------------------------------------------------------------------
# Test Class for SecurityLevelSettingResp
#-----------------------------------------------------------------------------
class TestSecurityLevelSettingResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for SecurityLevelSettingResp
    #--------------------------------------------------------
    def test_security_level_setting_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        result_info_model = {} # ResultInfo
        result_info_model['page'] = 1
        result_info_model['per_page'] = 2
        result_info_model['count'] = 1
        result_info_model['total_count'] = 200

        security_level_setting_resp_messages_item_model = {} # SecurityLevelSettingRespMessagesItem
        security_level_setting_resp_messages_item_model['status'] = 'OK'

        security_level_setting_resp_result_model = {} # SecurityLevelSettingRespResult
        security_level_setting_resp_result_model['id'] = 'security_level'
        security_level_setting_resp_result_model['value'] = 'medium'
        security_level_setting_resp_result_model['editable'] = True
        security_level_setting_resp_result_model['modified_on'] = '2014-01-01T05:20:00.12345Z'

        # Construct a json representation of a SecurityLevelSettingResp model
        security_level_setting_resp_model_json = {}
        security_level_setting_resp_model_json['result'] = security_level_setting_resp_result_model
        security_level_setting_resp_model_json['result_info'] = result_info_model
        security_level_setting_resp_model_json['success'] = True
        security_level_setting_resp_model_json['errors'] = [['testString']]
        security_level_setting_resp_model_json['messages'] = [security_level_setting_resp_messages_item_model]

        # Construct a model instance of SecurityLevelSettingResp by calling from_dict on the json representation
        security_level_setting_resp_model = SecurityLevelSettingResp.from_dict(security_level_setting_resp_model_json)
        assert security_level_setting_resp_model != False

        # Construct a model instance of SecurityLevelSettingResp by calling from_dict on the json representation
        security_level_setting_resp_model_dict = SecurityLevelSettingResp.from_dict(security_level_setting_resp_model_json).__dict__
        security_level_setting_resp_model2 = SecurityLevelSettingResp(**security_level_setting_resp_model_dict)

        # Verify the model instances are equivalent
        assert security_level_setting_resp_model == security_level_setting_resp_model2

        # Convert model instance back to dict and verify no loss of data
        security_level_setting_resp_model_json2 = security_level_setting_resp_model.to_dict()
        assert security_level_setting_resp_model_json2 == security_level_setting_resp_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
