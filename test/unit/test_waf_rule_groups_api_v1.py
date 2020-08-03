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
from ibm_cloud_networking_services.waf_rule_groups_api_v1 import *

crn = 'testString'
zone_id = 'testString'

service = WafRuleGroupsApiV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn,
    zone_id=zone_id
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: WAFRuleGroups
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_waf_rule_groups
#-----------------------------------------------------------------------------
class TestListWafRuleGroups():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # list_waf_rule_groups()
    #--------------------------------------------------------
    @responses.activate
    def test_list_waf_rule_groups_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString/groups')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "a25a9a7e9c00afc1fb2e0245519d725b", "name": "Project Honey Pot", "description": "Group designed to protect against IP addresses that are a threat and typically used to launch DDoS attacks", "rules_count": 10, "modified_rules_count": 10, "package_id": "a25a9a7e9c00afc1fb2e0245519d725b", "mode": "on", "allowed_modes": ["allowed_modes"]}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pkg_id = 'testString'
        name = 'Wordpress-rules'
        mode = 'true'
        rules_count = '10'
        page = 1
        per_page = 50
        order = 'status'
        direction = 'desc'
        match = 'all'

        # Invoke method
        response = service.list_waf_rule_groups(
            pkg_id,
            name=name,
            mode=mode,
            rules_count=rules_count,
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
        assert 'mode={}'.format(mode) in query_string
        assert 'rules_count={}'.format(rules_count) in query_string
        assert 'page={}'.format(page) in query_string
        assert 'per_page={}'.format(per_page) in query_string
        assert 'order={}'.format(order) in query_string
        assert 'direction={}'.format(direction) in query_string
        assert 'match={}'.format(match) in query_string


    #--------------------------------------------------------
    # test_list_waf_rule_groups_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_waf_rule_groups_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString/groups')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "a25a9a7e9c00afc1fb2e0245519d725b", "name": "Project Honey Pot", "description": "Group designed to protect against IP addresses that are a threat and typically used to launch DDoS attacks", "rules_count": 10, "modified_rules_count": 10, "package_id": "a25a9a7e9c00afc1fb2e0245519d725b", "mode": "on", "allowed_modes": ["allowed_modes"]}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pkg_id = 'testString'

        # Invoke method
        response = service.list_waf_rule_groups(
            pkg_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_waf_rule_groups_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_waf_rule_groups_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString/groups')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "a25a9a7e9c00afc1fb2e0245519d725b", "name": "Project Honey Pot", "description": "Group designed to protect against IP addresses that are a threat and typically used to launch DDoS attacks", "rules_count": 10, "modified_rules_count": 10, "package_id": "a25a9a7e9c00afc1fb2e0245519d725b", "mode": "on", "allowed_modes": ["allowed_modes"]}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pkg_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pkg_id": pkg_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_waf_rule_groups(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_waf_rule_group
#-----------------------------------------------------------------------------
class TestGetWafRuleGroup():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_waf_rule_group()
    #--------------------------------------------------------
    @responses.activate
    def test_get_waf_rule_group_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString/groups/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "a25a9a7e9c00afc1fb2e0245519d725b", "name": "Project Honey Pot", "description": "Group designed to protect against IP addresses that are a threat and typically used to launch DDoS attacks", "rules_count": 10, "modified_rules_count": 10, "package_id": "a25a9a7e9c00afc1fb2e0245519d725b", "mode": "on", "allowed_modes": ["allowed_modes"]}, "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pkg_id = 'testString'
        group_id = 'testString'

        # Invoke method
        response = service.get_waf_rule_group(
            pkg_id,
            group_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_waf_rule_group_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_waf_rule_group_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString/groups/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "a25a9a7e9c00afc1fb2e0245519d725b", "name": "Project Honey Pot", "description": "Group designed to protect against IP addresses that are a threat and typically used to launch DDoS attacks", "rules_count": 10, "modified_rules_count": 10, "package_id": "a25a9a7e9c00afc1fb2e0245519d725b", "mode": "on", "allowed_modes": ["allowed_modes"]}, "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pkg_id = 'testString'
        group_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pkg_id": pkg_id,
            "group_id": group_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_waf_rule_group(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_waf_rule_group
#-----------------------------------------------------------------------------
class TestUpdateWafRuleGroup():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_waf_rule_group()
    #--------------------------------------------------------
    @responses.activate
    def test_update_waf_rule_group_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString/groups/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "a25a9a7e9c00afc1fb2e0245519d725b", "name": "Project Honey Pot", "description": "Group designed to protect against IP addresses that are a threat and typically used to launch DDoS attacks", "rules_count": 10, "modified_rules_count": 10, "package_id": "a25a9a7e9c00afc1fb2e0245519d725b", "mode": "on", "allowed_modes": ["allowed_modes"]}, "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pkg_id = 'testString'
        group_id = 'testString'
        mode = 'on'

        # Invoke method
        response = service.update_waf_rule_group(
            pkg_id,
            group_id,
            mode=mode,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['mode'] == 'on'


    #--------------------------------------------------------
    # test_update_waf_rule_group_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_waf_rule_group_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString/groups/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "a25a9a7e9c00afc1fb2e0245519d725b", "name": "Project Honey Pot", "description": "Group designed to protect against IP addresses that are a threat and typically used to launch DDoS attacks", "rules_count": 10, "modified_rules_count": 10, "package_id": "a25a9a7e9c00afc1fb2e0245519d725b", "mode": "on", "allowed_modes": ["allowed_modes"]}, "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pkg_id = 'testString'
        group_id = 'testString'

        # Invoke method
        response = service.update_waf_rule_group(
            pkg_id,
            group_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_waf_rule_group_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_waf_rule_group_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString/groups/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "a25a9a7e9c00afc1fb2e0245519d725b", "name": "Project Honey Pot", "description": "Group designed to protect against IP addresses that are a threat and typically used to launch DDoS attacks", "rules_count": 10, "modified_rules_count": 10, "package_id": "a25a9a7e9c00afc1fb2e0245519d725b", "mode": "on", "allowed_modes": ["allowed_modes"]}, "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pkg_id = 'testString'
        group_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "pkg_id": pkg_id,
            "group_id": group_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_waf_rule_group(**req_copy)



# endregion
##############################################################################
# End of Service: WAFRuleGroups
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for WafGroupResponseResultInfo
#-----------------------------------------------------------------------------
class TestWafGroupResponseResultInfo():

    #--------------------------------------------------------
    # Test serialization/deserialization for WafGroupResponseResultInfo
    #--------------------------------------------------------
    def test_waf_group_response_result_info_serialization(self):

        # Construct a json representation of a WafGroupResponseResultInfo model
        waf_group_response_result_info_model_json = {}
        waf_group_response_result_info_model_json['page'] = 1
        waf_group_response_result_info_model_json['per_page'] = 2
        waf_group_response_result_info_model_json['count'] = 1
        waf_group_response_result_info_model_json['total_count'] = 200

        # Construct a model instance of WafGroupResponseResultInfo by calling from_dict on the json representation
        waf_group_response_result_info_model = WafGroupResponseResultInfo.from_dict(waf_group_response_result_info_model_json)
        assert waf_group_response_result_info_model != False

        # Construct a model instance of WafGroupResponseResultInfo by calling from_dict on the json representation
        waf_group_response_result_info_model_dict = WafGroupResponseResultInfo.from_dict(waf_group_response_result_info_model_json).__dict__
        waf_group_response_result_info_model2 = WafGroupResponseResultInfo(**waf_group_response_result_info_model_dict)

        # Verify the model instances are equivalent
        assert waf_group_response_result_info_model == waf_group_response_result_info_model2

        # Convert model instance back to dict and verify no loss of data
        waf_group_response_result_info_model_json2 = waf_group_response_result_info_model.to_dict()
        assert waf_group_response_result_info_model_json2 == waf_group_response_result_info_model_json

#-----------------------------------------------------------------------------
# Test Class for WafGroupsResponseResultInfo
#-----------------------------------------------------------------------------
class TestWafGroupsResponseResultInfo():

    #--------------------------------------------------------
    # Test serialization/deserialization for WafGroupsResponseResultInfo
    #--------------------------------------------------------
    def test_waf_groups_response_result_info_serialization(self):

        # Construct a json representation of a WafGroupsResponseResultInfo model
        waf_groups_response_result_info_model_json = {}
        waf_groups_response_result_info_model_json['page'] = 1
        waf_groups_response_result_info_model_json['per_page'] = 2
        waf_groups_response_result_info_model_json['count'] = 1
        waf_groups_response_result_info_model_json['total_count'] = 200

        # Construct a model instance of WafGroupsResponseResultInfo by calling from_dict on the json representation
        waf_groups_response_result_info_model = WafGroupsResponseResultInfo.from_dict(waf_groups_response_result_info_model_json)
        assert waf_groups_response_result_info_model != False

        # Construct a model instance of WafGroupsResponseResultInfo by calling from_dict on the json representation
        waf_groups_response_result_info_model_dict = WafGroupsResponseResultInfo.from_dict(waf_groups_response_result_info_model_json).__dict__
        waf_groups_response_result_info_model2 = WafGroupsResponseResultInfo(**waf_groups_response_result_info_model_dict)

        # Verify the model instances are equivalent
        assert waf_groups_response_result_info_model == waf_groups_response_result_info_model2

        # Convert model instance back to dict and verify no loss of data
        waf_groups_response_result_info_model_json2 = waf_groups_response_result_info_model.to_dict()
        assert waf_groups_response_result_info_model_json2 == waf_groups_response_result_info_model_json

#-----------------------------------------------------------------------------
# Test Class for WafGroupResponse
#-----------------------------------------------------------------------------
class TestWafGroupResponse():

    #--------------------------------------------------------
    # Test serialization/deserialization for WafGroupResponse
    #--------------------------------------------------------
    def test_waf_group_response_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        waf_group_response_result_info_model = {} # WafGroupResponseResultInfo
        waf_group_response_result_info_model['page'] = 1
        waf_group_response_result_info_model['per_page'] = 2
        waf_group_response_result_info_model['count'] = 1
        waf_group_response_result_info_model['total_count'] = 200

        waf_rule_properties_model = {} # WafRuleProperties
        waf_rule_properties_model['id'] = 'a25a9a7e9c00afc1fb2e0245519d725b'
        waf_rule_properties_model['name'] = 'Project Honey Pot'
        waf_rule_properties_model['description'] = 'Group designed to protect against IP addresses that are a threat and typically used to launch DDoS attacks'
        waf_rule_properties_model['rules_count'] = 10
        waf_rule_properties_model['modified_rules_count'] = 10
        waf_rule_properties_model['package_id'] = 'a25a9a7e9c00afc1fb2e0245519d725b'
        waf_rule_properties_model['mode'] = 'on'
        waf_rule_properties_model['allowed_modes'] = ['testString']

        # Construct a json representation of a WafGroupResponse model
        waf_group_response_model_json = {}
        waf_group_response_model_json['success'] = True
        waf_group_response_model_json['errors'] = [['testString']]
        waf_group_response_model_json['messages'] = [['testString']]
        waf_group_response_model_json['result'] = waf_rule_properties_model
        waf_group_response_model_json['result_info'] = waf_group_response_result_info_model

        # Construct a model instance of WafGroupResponse by calling from_dict on the json representation
        waf_group_response_model = WafGroupResponse.from_dict(waf_group_response_model_json)
        assert waf_group_response_model != False

        # Construct a model instance of WafGroupResponse by calling from_dict on the json representation
        waf_group_response_model_dict = WafGroupResponse.from_dict(waf_group_response_model_json).__dict__
        waf_group_response_model2 = WafGroupResponse(**waf_group_response_model_dict)

        # Verify the model instances are equivalent
        assert waf_group_response_model == waf_group_response_model2

        # Convert model instance back to dict and verify no loss of data
        waf_group_response_model_json2 = waf_group_response_model.to_dict()
        assert waf_group_response_model_json2 == waf_group_response_model_json

#-----------------------------------------------------------------------------
# Test Class for WafGroupsResponse
#-----------------------------------------------------------------------------
class TestWafGroupsResponse():

    #--------------------------------------------------------
    # Test serialization/deserialization for WafGroupsResponse
    #--------------------------------------------------------
    def test_waf_groups_response_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        waf_groups_response_result_info_model = {} # WafGroupsResponseResultInfo
        waf_groups_response_result_info_model['page'] = 1
        waf_groups_response_result_info_model['per_page'] = 2
        waf_groups_response_result_info_model['count'] = 1
        waf_groups_response_result_info_model['total_count'] = 200

        waf_rule_properties_model = {} # WafRuleProperties
        waf_rule_properties_model['id'] = 'a25a9a7e9c00afc1fb2e0245519d725b'
        waf_rule_properties_model['name'] = 'Project Honey Pot'
        waf_rule_properties_model['description'] = 'Group designed to protect against IP addresses that are a threat and typically used to launch DDoS attacks'
        waf_rule_properties_model['rules_count'] = 10
        waf_rule_properties_model['modified_rules_count'] = 10
        waf_rule_properties_model['package_id'] = 'a25a9a7e9c00afc1fb2e0245519d725b'
        waf_rule_properties_model['mode'] = 'on'
        waf_rule_properties_model['allowed_modes'] = ['testString']

        # Construct a json representation of a WafGroupsResponse model
        waf_groups_response_model_json = {}
        waf_groups_response_model_json['success'] = True
        waf_groups_response_model_json['errors'] = [['testString']]
        waf_groups_response_model_json['messages'] = [['testString']]
        waf_groups_response_model_json['result'] = [waf_rule_properties_model]
        waf_groups_response_model_json['result_info'] = waf_groups_response_result_info_model

        # Construct a model instance of WafGroupsResponse by calling from_dict on the json representation
        waf_groups_response_model = WafGroupsResponse.from_dict(waf_groups_response_model_json)
        assert waf_groups_response_model != False

        # Construct a model instance of WafGroupsResponse by calling from_dict on the json representation
        waf_groups_response_model_dict = WafGroupsResponse.from_dict(waf_groups_response_model_json).__dict__
        waf_groups_response_model2 = WafGroupsResponse(**waf_groups_response_model_dict)

        # Verify the model instances are equivalent
        assert waf_groups_response_model == waf_groups_response_model2

        # Convert model instance back to dict and verify no loss of data
        waf_groups_response_model_json2 = waf_groups_response_model.to_dict()
        assert waf_groups_response_model_json2 == waf_groups_response_model_json

#-----------------------------------------------------------------------------
# Test Class for WafRuleProperties
#-----------------------------------------------------------------------------
class TestWafRuleProperties():

    #--------------------------------------------------------
    # Test serialization/deserialization for WafRuleProperties
    #--------------------------------------------------------
    def test_waf_rule_properties_serialization(self):

        # Construct a json representation of a WafRuleProperties model
        waf_rule_properties_model_json = {}
        waf_rule_properties_model_json['id'] = 'a25a9a7e9c00afc1fb2e0245519d725b'
        waf_rule_properties_model_json['name'] = 'Project Honey Pot'
        waf_rule_properties_model_json['description'] = 'Group designed to protect against IP addresses that are a threat and typically used to launch DDoS attacks'
        waf_rule_properties_model_json['rules_count'] = 10
        waf_rule_properties_model_json['modified_rules_count'] = 10
        waf_rule_properties_model_json['package_id'] = 'a25a9a7e9c00afc1fb2e0245519d725b'
        waf_rule_properties_model_json['mode'] = 'on'
        waf_rule_properties_model_json['allowed_modes'] = ['testString']

        # Construct a model instance of WafRuleProperties by calling from_dict on the json representation
        waf_rule_properties_model = WafRuleProperties.from_dict(waf_rule_properties_model_json)
        assert waf_rule_properties_model != False

        # Construct a model instance of WafRuleProperties by calling from_dict on the json representation
        waf_rule_properties_model_dict = WafRuleProperties.from_dict(waf_rule_properties_model_json).__dict__
        waf_rule_properties_model2 = WafRuleProperties(**waf_rule_properties_model_dict)

        # Verify the model instances are equivalent
        assert waf_rule_properties_model == waf_rule_properties_model2

        # Convert model instance back to dict and verify no loss of data
        waf_rule_properties_model_json2 = waf_rule_properties_model.to_dict()
        assert waf_rule_properties_model_json2 == waf_rule_properties_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
