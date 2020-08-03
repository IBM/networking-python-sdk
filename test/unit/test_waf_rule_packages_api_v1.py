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
from ibm_cloud_networking_services.waf_rule_packages_api_v1 import *

crn = 'testString'
zone_id = 'testString'

service = WafRulePackagesApiV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn,
    zone_id=zone_id
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: WAFRulePackages
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_waf_packages
#-----------------------------------------------------------------------------
class TestListWafPackages():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # list_waf_packages()
    #--------------------------------------------------------
    @responses.activate
    def test_list_waf_packages_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/waf/packages')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "a25a9a7e9c00afc1fb2e0245519d725b", "name": "WordPress rules", "description": "Common WordPress exploit protections", "detection_mode": "traditional", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "status": "active"}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        name = 'Wordpress-rules'
        page = 1
        per_page = 50
        order = 'status'
        direction = 'desc'
        match = 'all'

        # Invoke method
        response = service.list_waf_packages(
            name=name,
            page=page,
            per_page=per_page,
            order=order,
            direction=direction,
            match=match,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'name={}'.format(name) in query_string
        assert 'page={}'.format(page) in query_string
        assert 'per_page={}'.format(per_page) in query_string
        assert 'order={}'.format(order) in query_string
        assert 'direction={}'.format(direction) in query_string
        assert 'match={}'.format(match) in query_string


    #--------------------------------------------------------
    # test_list_waf_packages_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_waf_packages_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/waf/packages')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "a25a9a7e9c00afc1fb2e0245519d725b", "name": "WordPress rules", "description": "Common WordPress exploit protections", "detection_mode": "traditional", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "status": "active"}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_waf_packages()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_waf_packages_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_waf_packages_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/waf/packages')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "a25a9a7e9c00afc1fb2e0245519d725b", "name": "WordPress rules", "description": "Common WordPress exploit protections", "detection_mode": "traditional", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "status": "active"}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
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
                service.list_waf_packages(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_waf_package
#-----------------------------------------------------------------------------
class TestGetWafPackage():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_waf_package()
    #--------------------------------------------------------
    @responses.activate
    def test_get_waf_package_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "a25a9a7e9c00afc1fb2e0245519d725b", "name": "WordPress rules", "description": "Common WordPress exploit protections", "detection_mode": "traditional", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "status": "active", "sensitivity": "high", "action_mode": "challenge"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        package_id = 'testString'

        # Invoke method
        response = service.get_waf_package(
            package_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_waf_package_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_waf_package_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "a25a9a7e9c00afc1fb2e0245519d725b", "name": "WordPress rules", "description": "Common WordPress exploit protections", "detection_mode": "traditional", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "status": "active", "sensitivity": "high", "action_mode": "challenge"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        package_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "package_id": package_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_waf_package(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_waf_package
#-----------------------------------------------------------------------------
class TestUpdateWafPackage():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_waf_package()
    #--------------------------------------------------------
    @responses.activate
    def test_update_waf_package_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "a25a9a7e9c00afc1fb2e0245519d725b", "name": "WordPress rules", "description": "Common WordPress exploit protections", "detection_mode": "traditional", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "status": "active", "sensitivity": "high", "action_mode": "challenge"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        package_id = 'testString'
        sensitivity = 'high'
        action_mode = 'simulate'

        # Invoke method
        response = service.update_waf_package(
            package_id,
            sensitivity=sensitivity,
            action_mode=action_mode,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['sensitivity'] == 'high'
        assert req_body['action_mode'] == 'simulate'


    #--------------------------------------------------------
    # test_update_waf_package_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_waf_package_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "a25a9a7e9c00afc1fb2e0245519d725b", "name": "WordPress rules", "description": "Common WordPress exploit protections", "detection_mode": "traditional", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "status": "active", "sensitivity": "high", "action_mode": "challenge"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        package_id = 'testString'

        # Invoke method
        response = service.update_waf_package(
            package_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_waf_package_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_waf_package_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "a25a9a7e9c00afc1fb2e0245519d725b", "name": "WordPress rules", "description": "Common WordPress exploit protections", "detection_mode": "traditional", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "status": "active", "sensitivity": "high", "action_mode": "challenge"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        package_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "package_id": package_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_waf_package(**req_copy)



# endregion
##############################################################################
# End of Service: WAFRulePackages
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for WafPackageResponseResult
#-----------------------------------------------------------------------------
class TestWafPackageResponseResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for WafPackageResponseResult
    #--------------------------------------------------------
    def test_waf_package_response_result_serialization(self):

        # Construct a json representation of a WafPackageResponseResult model
        waf_package_response_result_model_json = {}
        waf_package_response_result_model_json['id'] = 'a25a9a7e9c00afc1fb2e0245519d725b'
        waf_package_response_result_model_json['name'] = 'WordPress rules'
        waf_package_response_result_model_json['description'] = 'Common WordPress exploit protections'
        waf_package_response_result_model_json['detection_mode'] = 'traditional'
        waf_package_response_result_model_json['zone_id'] = '023e105f4ecef8ad9ca31a8372d0c353'
        waf_package_response_result_model_json['status'] = 'active'
        waf_package_response_result_model_json['sensitivity'] = 'high'
        waf_package_response_result_model_json['action_mode'] = 'challenge'

        # Construct a model instance of WafPackageResponseResult by calling from_dict on the json representation
        waf_package_response_result_model = WafPackageResponseResult.from_dict(waf_package_response_result_model_json)
        assert waf_package_response_result_model != False

        # Construct a model instance of WafPackageResponseResult by calling from_dict on the json representation
        waf_package_response_result_model_dict = WafPackageResponseResult.from_dict(waf_package_response_result_model_json).__dict__
        waf_package_response_result_model2 = WafPackageResponseResult(**waf_package_response_result_model_dict)

        # Verify the model instances are equivalent
        assert waf_package_response_result_model == waf_package_response_result_model2

        # Convert model instance back to dict and verify no loss of data
        waf_package_response_result_model_json2 = waf_package_response_result_model.to_dict()
        assert waf_package_response_result_model_json2 == waf_package_response_result_model_json

#-----------------------------------------------------------------------------
# Test Class for WafPackagesResponseResultInfo
#-----------------------------------------------------------------------------
class TestWafPackagesResponseResultInfo():

    #--------------------------------------------------------
    # Test serialization/deserialization for WafPackagesResponseResultInfo
    #--------------------------------------------------------
    def test_waf_packages_response_result_info_serialization(self):

        # Construct a json representation of a WafPackagesResponseResultInfo model
        waf_packages_response_result_info_model_json = {}
        waf_packages_response_result_info_model_json['page'] = 1
        waf_packages_response_result_info_model_json['per_page'] = 2
        waf_packages_response_result_info_model_json['count'] = 1
        waf_packages_response_result_info_model_json['total_count'] = 200

        # Construct a model instance of WafPackagesResponseResultInfo by calling from_dict on the json representation
        waf_packages_response_result_info_model = WafPackagesResponseResultInfo.from_dict(waf_packages_response_result_info_model_json)
        assert waf_packages_response_result_info_model != False

        # Construct a model instance of WafPackagesResponseResultInfo by calling from_dict on the json representation
        waf_packages_response_result_info_model_dict = WafPackagesResponseResultInfo.from_dict(waf_packages_response_result_info_model_json).__dict__
        waf_packages_response_result_info_model2 = WafPackagesResponseResultInfo(**waf_packages_response_result_info_model_dict)

        # Verify the model instances are equivalent
        assert waf_packages_response_result_info_model == waf_packages_response_result_info_model2

        # Convert model instance back to dict and verify no loss of data
        waf_packages_response_result_info_model_json2 = waf_packages_response_result_info_model.to_dict()
        assert waf_packages_response_result_info_model_json2 == waf_packages_response_result_info_model_json

#-----------------------------------------------------------------------------
# Test Class for WafPackagesResponseResultItem
#-----------------------------------------------------------------------------
class TestWafPackagesResponseResultItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for WafPackagesResponseResultItem
    #--------------------------------------------------------
    def test_waf_packages_response_result_item_serialization(self):

        # Construct a json representation of a WafPackagesResponseResultItem model
        waf_packages_response_result_item_model_json = {}
        waf_packages_response_result_item_model_json['id'] = 'a25a9a7e9c00afc1fb2e0245519d725b'
        waf_packages_response_result_item_model_json['name'] = 'WordPress rules'
        waf_packages_response_result_item_model_json['description'] = 'Common WordPress exploit protections'
        waf_packages_response_result_item_model_json['detection_mode'] = 'traditional'
        waf_packages_response_result_item_model_json['zone_id'] = '023e105f4ecef8ad9ca31a8372d0c353'
        waf_packages_response_result_item_model_json['status'] = 'active'

        # Construct a model instance of WafPackagesResponseResultItem by calling from_dict on the json representation
        waf_packages_response_result_item_model = WafPackagesResponseResultItem.from_dict(waf_packages_response_result_item_model_json)
        assert waf_packages_response_result_item_model != False

        # Construct a model instance of WafPackagesResponseResultItem by calling from_dict on the json representation
        waf_packages_response_result_item_model_dict = WafPackagesResponseResultItem.from_dict(waf_packages_response_result_item_model_json).__dict__
        waf_packages_response_result_item_model2 = WafPackagesResponseResultItem(**waf_packages_response_result_item_model_dict)

        # Verify the model instances are equivalent
        assert waf_packages_response_result_item_model == waf_packages_response_result_item_model2

        # Convert model instance back to dict and verify no loss of data
        waf_packages_response_result_item_model_json2 = waf_packages_response_result_item_model.to_dict()
        assert waf_packages_response_result_item_model_json2 == waf_packages_response_result_item_model_json

#-----------------------------------------------------------------------------
# Test Class for WafPackageResponse
#-----------------------------------------------------------------------------
class TestWafPackageResponse():

    #--------------------------------------------------------
    # Test serialization/deserialization for WafPackageResponse
    #--------------------------------------------------------
    def test_waf_package_response_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        waf_package_response_result_model = {} # WafPackageResponseResult
        waf_package_response_result_model['id'] = 'a25a9a7e9c00afc1fb2e0245519d725b'
        waf_package_response_result_model['name'] = 'WordPress rules'
        waf_package_response_result_model['description'] = 'Common WordPress exploit protections'
        waf_package_response_result_model['detection_mode'] = 'traditional'
        waf_package_response_result_model['zone_id'] = '023e105f4ecef8ad9ca31a8372d0c353'
        waf_package_response_result_model['status'] = 'active'
        waf_package_response_result_model['sensitivity'] = 'high'
        waf_package_response_result_model['action_mode'] = 'challenge'

        # Construct a json representation of a WafPackageResponse model
        waf_package_response_model_json = {}
        waf_package_response_model_json['success'] = True
        waf_package_response_model_json['errors'] = [['testString']]
        waf_package_response_model_json['messages'] = [['testString']]
        waf_package_response_model_json['result'] = waf_package_response_result_model

        # Construct a model instance of WafPackageResponse by calling from_dict on the json representation
        waf_package_response_model = WafPackageResponse.from_dict(waf_package_response_model_json)
        assert waf_package_response_model != False

        # Construct a model instance of WafPackageResponse by calling from_dict on the json representation
        waf_package_response_model_dict = WafPackageResponse.from_dict(waf_package_response_model_json).__dict__
        waf_package_response_model2 = WafPackageResponse(**waf_package_response_model_dict)

        # Verify the model instances are equivalent
        assert waf_package_response_model == waf_package_response_model2

        # Convert model instance back to dict and verify no loss of data
        waf_package_response_model_json2 = waf_package_response_model.to_dict()
        assert waf_package_response_model_json2 == waf_package_response_model_json

#-----------------------------------------------------------------------------
# Test Class for WafPackagesResponse
#-----------------------------------------------------------------------------
class TestWafPackagesResponse():

    #--------------------------------------------------------
    # Test serialization/deserialization for WafPackagesResponse
    #--------------------------------------------------------
    def test_waf_packages_response_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        waf_packages_response_result_info_model = {} # WafPackagesResponseResultInfo
        waf_packages_response_result_info_model['page'] = 1
        waf_packages_response_result_info_model['per_page'] = 2
        waf_packages_response_result_info_model['count'] = 1
        waf_packages_response_result_info_model['total_count'] = 200

        waf_packages_response_result_item_model = {} # WafPackagesResponseResultItem
        waf_packages_response_result_item_model['id'] = 'a25a9a7e9c00afc1fb2e0245519d725b'
        waf_packages_response_result_item_model['name'] = 'WordPress rules'
        waf_packages_response_result_item_model['description'] = 'Common WordPress exploit protections'
        waf_packages_response_result_item_model['detection_mode'] = 'traditional'
        waf_packages_response_result_item_model['zone_id'] = '023e105f4ecef8ad9ca31a8372d0c353'
        waf_packages_response_result_item_model['status'] = 'active'

        # Construct a json representation of a WafPackagesResponse model
        waf_packages_response_model_json = {}
        waf_packages_response_model_json['success'] = True
        waf_packages_response_model_json['errors'] = [['testString']]
        waf_packages_response_model_json['messages'] = [['testString']]
        waf_packages_response_model_json['result'] = [waf_packages_response_result_item_model]
        waf_packages_response_model_json['result_info'] = waf_packages_response_result_info_model

        # Construct a model instance of WafPackagesResponse by calling from_dict on the json representation
        waf_packages_response_model = WafPackagesResponse.from_dict(waf_packages_response_model_json)
        assert waf_packages_response_model != False

        # Construct a model instance of WafPackagesResponse by calling from_dict on the json representation
        waf_packages_response_model_dict = WafPackagesResponse.from_dict(waf_packages_response_model_json).__dict__
        waf_packages_response_model2 = WafPackagesResponse(**waf_packages_response_model_dict)

        # Verify the model instances are equivalent
        assert waf_packages_response_model == waf_packages_response_model2

        # Convert model instance back to dict and verify no loss of data
        waf_packages_response_model_json2 = waf_packages_response_model.to_dict()
        assert waf_packages_response_model_json2 == waf_packages_response_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
