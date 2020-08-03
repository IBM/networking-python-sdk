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
from ibm_cloud_networking_services.waf_rules_api_v1 import *

crn = 'testString'
zone_id = 'testString'

service = WafRulesApiV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn,
    zone_id=zone_id
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: WAFRules
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_waf_rules
#-----------------------------------------------------------------------------
class TestListWafRules():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # list_waf_rules()
    #--------------------------------------------------------
    @responses.activate
    def test_list_waf_rules_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString/rules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "f939de3be84e66e757adcdcb87908023", "description": "SQL-injection-prevention-for-SELECT-statements", "priority": "5", "group": {"id": "de677e5818985db1285d0e80225f06e5", "name": "Project abc"}, "package_id": "a25a9a7e9c00afc1fb2e0245519d725b", "allowed_modes": ["allowed_modes"], "mode": "on"}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        package_id = 'testString'
        mode = 'on'
        priority = '5'
        match = 'all'
        order = 'status'
        group_id = 'de677e5818985db1285d0e80225f06e5'
        description = 'SQL-injection-prevention-for-SELECT-statements'
        direction = 'desc'
        page = 1
        per_page = 50

        # Invoke method
        response = service.list_waf_rules(
            package_id,
            mode=mode,
            priority=priority,
            match=match,
            order=order,
            group_id=group_id,
            description=description,
            direction=direction,
            page=page,
            per_page=per_page,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'mode={}'.format(mode) in query_string
        assert 'priority={}'.format(priority) in query_string
        assert 'match={}'.format(match) in query_string
        assert 'order={}'.format(order) in query_string
        assert 'group_id={}'.format(group_id) in query_string
        assert 'description={}'.format(description) in query_string
        assert 'direction={}'.format(direction) in query_string
        assert 'page={}'.format(page) in query_string
        assert 'per_page={}'.format(per_page) in query_string


    #--------------------------------------------------------
    # test_list_waf_rules_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_waf_rules_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString/rules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "f939de3be84e66e757adcdcb87908023", "description": "SQL-injection-prevention-for-SELECT-statements", "priority": "5", "group": {"id": "de677e5818985db1285d0e80225f06e5", "name": "Project abc"}, "package_id": "a25a9a7e9c00afc1fb2e0245519d725b", "allowed_modes": ["allowed_modes"], "mode": "on"}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        package_id = 'testString'

        # Invoke method
        response = service.list_waf_rules(
            package_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_waf_rules_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_waf_rules_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString/rules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "f939de3be84e66e757adcdcb87908023", "description": "SQL-injection-prevention-for-SELECT-statements", "priority": "5", "group": {"id": "de677e5818985db1285d0e80225f06e5", "name": "Project abc"}, "package_id": "a25a9a7e9c00afc1fb2e0245519d725b", "allowed_modes": ["allowed_modes"], "mode": "on"}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
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
                service.list_waf_rules(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_waf_rule
#-----------------------------------------------------------------------------
class TestGetWafRule():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_waf_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_get_waf_rule_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString/rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f939de3be84e66e757adcdcb87908023", "description": "SQL-injection-prevention-for-SELECT-statements", "priority": "5", "group": {"id": "de677e5818985db1285d0e80225f06e5", "name": "Project abc"}, "package_id": "a25a9a7e9c00afc1fb2e0245519d725b", "allowed_modes": ["allowed_modes"], "mode": "on"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        package_id = 'testString'
        identifier = 'testString'

        # Invoke method
        response = service.get_waf_rule(
            package_id,
            identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_waf_rule_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_waf_rule_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString/rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f939de3be84e66e757adcdcb87908023", "description": "SQL-injection-prevention-for-SELECT-statements", "priority": "5", "group": {"id": "de677e5818985db1285d0e80225f06e5", "name": "Project abc"}, "package_id": "a25a9a7e9c00afc1fb2e0245519d725b", "allowed_modes": ["allowed_modes"], "mode": "on"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        package_id = 'testString'
        identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "package_id": package_id,
            "identifier": identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_waf_rule(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_waf_rule
#-----------------------------------------------------------------------------
class TestUpdateWafRule():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_waf_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_update_waf_rule_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString/rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f939de3be84e66e757adcdcb87908023", "description": "SQL-injection-prevention-for-SELECT-statements", "priority": "5", "group": {"id": "de677e5818985db1285d0e80225f06e5", "name": "Project abc"}, "package_id": "a25a9a7e9c00afc1fb2e0245519d725b", "allowed_modes": ["allowed_modes"], "mode": "on"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a WafRuleBodyCis model
        waf_rule_body_cis_model = {}
        waf_rule_body_cis_model['mode'] = 'default'

        # Construct a dict representation of a WafRuleBodyOwasp model
        waf_rule_body_owasp_model = {}
        waf_rule_body_owasp_model['mode'] = 'on'

        # Set up parameter values
        package_id = 'testString'
        identifier = 'testString'
        cis = waf_rule_body_cis_model
        owasp = waf_rule_body_owasp_model

        # Invoke method
        response = service.update_waf_rule(
            package_id,
            identifier,
            cis=cis,
            owasp=owasp,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['cis'] == waf_rule_body_cis_model
        assert req_body['owasp'] == waf_rule_body_owasp_model


    #--------------------------------------------------------
    # test_update_waf_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_waf_rule_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString/rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f939de3be84e66e757adcdcb87908023", "description": "SQL-injection-prevention-for-SELECT-statements", "priority": "5", "group": {"id": "de677e5818985db1285d0e80225f06e5", "name": "Project abc"}, "package_id": "a25a9a7e9c00afc1fb2e0245519d725b", "allowed_modes": ["allowed_modes"], "mode": "on"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        package_id = 'testString'
        identifier = 'testString'

        # Invoke method
        response = service.update_waf_rule(
            package_id,
            identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_waf_rule_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_waf_rule_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString/rules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f939de3be84e66e757adcdcb87908023", "description": "SQL-injection-prevention-for-SELECT-statements", "priority": "5", "group": {"id": "de677e5818985db1285d0e80225f06e5", "name": "Project abc"}, "package_id": "a25a9a7e9c00afc1fb2e0245519d725b", "allowed_modes": ["allowed_modes"], "mode": "on"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        package_id = 'testString'
        identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "package_id": package_id,
            "identifier": identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_waf_rule(**req_copy)



# endregion
##############################################################################
# End of Service: WAFRules
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for WafRuleBodyCis
#-----------------------------------------------------------------------------
class TestWafRuleBodyCis():

    #--------------------------------------------------------
    # Test serialization/deserialization for WafRuleBodyCis
    #--------------------------------------------------------
    def test_waf_rule_body_cis_serialization(self):

        # Construct a json representation of a WafRuleBodyCis model
        waf_rule_body_cis_model_json = {}
        waf_rule_body_cis_model_json['mode'] = 'default'

        # Construct a model instance of WafRuleBodyCis by calling from_dict on the json representation
        waf_rule_body_cis_model = WafRuleBodyCis.from_dict(waf_rule_body_cis_model_json)
        assert waf_rule_body_cis_model != False

        # Construct a model instance of WafRuleBodyCis by calling from_dict on the json representation
        waf_rule_body_cis_model_dict = WafRuleBodyCis.from_dict(waf_rule_body_cis_model_json).__dict__
        waf_rule_body_cis_model2 = WafRuleBodyCis(**waf_rule_body_cis_model_dict)

        # Verify the model instances are equivalent
        assert waf_rule_body_cis_model == waf_rule_body_cis_model2

        # Convert model instance back to dict and verify no loss of data
        waf_rule_body_cis_model_json2 = waf_rule_body_cis_model.to_dict()
        assert waf_rule_body_cis_model_json2 == waf_rule_body_cis_model_json

#-----------------------------------------------------------------------------
# Test Class for WafRuleBodyOwasp
#-----------------------------------------------------------------------------
class TestWafRuleBodyOwasp():

    #--------------------------------------------------------
    # Test serialization/deserialization for WafRuleBodyOwasp
    #--------------------------------------------------------
    def test_waf_rule_body_owasp_serialization(self):

        # Construct a json representation of a WafRuleBodyOwasp model
        waf_rule_body_owasp_model_json = {}
        waf_rule_body_owasp_model_json['mode'] = 'on'

        # Construct a model instance of WafRuleBodyOwasp by calling from_dict on the json representation
        waf_rule_body_owasp_model = WafRuleBodyOwasp.from_dict(waf_rule_body_owasp_model_json)
        assert waf_rule_body_owasp_model != False

        # Construct a model instance of WafRuleBodyOwasp by calling from_dict on the json representation
        waf_rule_body_owasp_model_dict = WafRuleBodyOwasp.from_dict(waf_rule_body_owasp_model_json).__dict__
        waf_rule_body_owasp_model2 = WafRuleBodyOwasp(**waf_rule_body_owasp_model_dict)

        # Verify the model instances are equivalent
        assert waf_rule_body_owasp_model == waf_rule_body_owasp_model2

        # Convert model instance back to dict and verify no loss of data
        waf_rule_body_owasp_model_json2 = waf_rule_body_owasp_model.to_dict()
        assert waf_rule_body_owasp_model_json2 == waf_rule_body_owasp_model_json

#-----------------------------------------------------------------------------
# Test Class for WafRuleResponseResult
#-----------------------------------------------------------------------------
class TestWafRuleResponseResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for WafRuleResponseResult
    #--------------------------------------------------------
    def test_waf_rule_response_result_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        waf_rule_response_result_group_model = {} # WafRuleResponseResultGroup
        waf_rule_response_result_group_model['id'] = 'de677e5818985db1285d0e80225f06e5'
        waf_rule_response_result_group_model['name'] = 'Project abc'

        # Construct a json representation of a WafRuleResponseResult model
        waf_rule_response_result_model_json = {}
        waf_rule_response_result_model_json['id'] = 'f939de3be84e66e757adcdcb87908023'
        waf_rule_response_result_model_json['description'] = 'SQL-injection-prevention-for-SELECT-statements'
        waf_rule_response_result_model_json['priority'] = '5'
        waf_rule_response_result_model_json['group'] = waf_rule_response_result_group_model
        waf_rule_response_result_model_json['package_id'] = 'a25a9a7e9c00afc1fb2e0245519d725b'
        waf_rule_response_result_model_json['allowed_modes'] = ['testString']
        waf_rule_response_result_model_json['mode'] = 'on'

        # Construct a model instance of WafRuleResponseResult by calling from_dict on the json representation
        waf_rule_response_result_model = WafRuleResponseResult.from_dict(waf_rule_response_result_model_json)
        assert waf_rule_response_result_model != False

        # Construct a model instance of WafRuleResponseResult by calling from_dict on the json representation
        waf_rule_response_result_model_dict = WafRuleResponseResult.from_dict(waf_rule_response_result_model_json).__dict__
        waf_rule_response_result_model2 = WafRuleResponseResult(**waf_rule_response_result_model_dict)

        # Verify the model instances are equivalent
        assert waf_rule_response_result_model == waf_rule_response_result_model2

        # Convert model instance back to dict and verify no loss of data
        waf_rule_response_result_model_json2 = waf_rule_response_result_model.to_dict()
        assert waf_rule_response_result_model_json2 == waf_rule_response_result_model_json

#-----------------------------------------------------------------------------
# Test Class for WafRuleResponseResultGroup
#-----------------------------------------------------------------------------
class TestWafRuleResponseResultGroup():

    #--------------------------------------------------------
    # Test serialization/deserialization for WafRuleResponseResultGroup
    #--------------------------------------------------------
    def test_waf_rule_response_result_group_serialization(self):

        # Construct a json representation of a WafRuleResponseResultGroup model
        waf_rule_response_result_group_model_json = {}
        waf_rule_response_result_group_model_json['id'] = 'de677e5818985db1285d0e80225f06e5'
        waf_rule_response_result_group_model_json['name'] = 'Project abc'

        # Construct a model instance of WafRuleResponseResultGroup by calling from_dict on the json representation
        waf_rule_response_result_group_model = WafRuleResponseResultGroup.from_dict(waf_rule_response_result_group_model_json)
        assert waf_rule_response_result_group_model != False

        # Construct a model instance of WafRuleResponseResultGroup by calling from_dict on the json representation
        waf_rule_response_result_group_model_dict = WafRuleResponseResultGroup.from_dict(waf_rule_response_result_group_model_json).__dict__
        waf_rule_response_result_group_model2 = WafRuleResponseResultGroup(**waf_rule_response_result_group_model_dict)

        # Verify the model instances are equivalent
        assert waf_rule_response_result_group_model == waf_rule_response_result_group_model2

        # Convert model instance back to dict and verify no loss of data
        waf_rule_response_result_group_model_json2 = waf_rule_response_result_group_model.to_dict()
        assert waf_rule_response_result_group_model_json2 == waf_rule_response_result_group_model_json

#-----------------------------------------------------------------------------
# Test Class for WafRulesResponseResultInfo
#-----------------------------------------------------------------------------
class TestWafRulesResponseResultInfo():

    #--------------------------------------------------------
    # Test serialization/deserialization for WafRulesResponseResultInfo
    #--------------------------------------------------------
    def test_waf_rules_response_result_info_serialization(self):

        # Construct a json representation of a WafRulesResponseResultInfo model
        waf_rules_response_result_info_model_json = {}
        waf_rules_response_result_info_model_json['page'] = 1
        waf_rules_response_result_info_model_json['per_page'] = 20
        waf_rules_response_result_info_model_json['count'] = 1
        waf_rules_response_result_info_model_json['total_count'] = 2000

        # Construct a model instance of WafRulesResponseResultInfo by calling from_dict on the json representation
        waf_rules_response_result_info_model = WafRulesResponseResultInfo.from_dict(waf_rules_response_result_info_model_json)
        assert waf_rules_response_result_info_model != False

        # Construct a model instance of WafRulesResponseResultInfo by calling from_dict on the json representation
        waf_rules_response_result_info_model_dict = WafRulesResponseResultInfo.from_dict(waf_rules_response_result_info_model_json).__dict__
        waf_rules_response_result_info_model2 = WafRulesResponseResultInfo(**waf_rules_response_result_info_model_dict)

        # Verify the model instances are equivalent
        assert waf_rules_response_result_info_model == waf_rules_response_result_info_model2

        # Convert model instance back to dict and verify no loss of data
        waf_rules_response_result_info_model_json2 = waf_rules_response_result_info_model.to_dict()
        assert waf_rules_response_result_info_model_json2 == waf_rules_response_result_info_model_json

#-----------------------------------------------------------------------------
# Test Class for WafRulesResponseResultItem
#-----------------------------------------------------------------------------
class TestWafRulesResponseResultItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for WafRulesResponseResultItem
    #--------------------------------------------------------
    def test_waf_rules_response_result_item_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        waf_rules_response_result_item_group_model = {} # WafRulesResponseResultItemGroup
        waf_rules_response_result_item_group_model['id'] = 'de677e5818985db1285d0e80225f06e5'
        waf_rules_response_result_item_group_model['name'] = 'Project abc'

        # Construct a json representation of a WafRulesResponseResultItem model
        waf_rules_response_result_item_model_json = {}
        waf_rules_response_result_item_model_json['id'] = 'f939de3be84e66e757adcdcb87908023'
        waf_rules_response_result_item_model_json['description'] = 'SQL-injection-prevention-for-SELECT-statements'
        waf_rules_response_result_item_model_json['priority'] = '5'
        waf_rules_response_result_item_model_json['group'] = waf_rules_response_result_item_group_model
        waf_rules_response_result_item_model_json['package_id'] = 'a25a9a7e9c00afc1fb2e0245519d725b'
        waf_rules_response_result_item_model_json['allowed_modes'] = ['testString']
        waf_rules_response_result_item_model_json['mode'] = 'on'

        # Construct a model instance of WafRulesResponseResultItem by calling from_dict on the json representation
        waf_rules_response_result_item_model = WafRulesResponseResultItem.from_dict(waf_rules_response_result_item_model_json)
        assert waf_rules_response_result_item_model != False

        # Construct a model instance of WafRulesResponseResultItem by calling from_dict on the json representation
        waf_rules_response_result_item_model_dict = WafRulesResponseResultItem.from_dict(waf_rules_response_result_item_model_json).__dict__
        waf_rules_response_result_item_model2 = WafRulesResponseResultItem(**waf_rules_response_result_item_model_dict)

        # Verify the model instances are equivalent
        assert waf_rules_response_result_item_model == waf_rules_response_result_item_model2

        # Convert model instance back to dict and verify no loss of data
        waf_rules_response_result_item_model_json2 = waf_rules_response_result_item_model.to_dict()
        assert waf_rules_response_result_item_model_json2 == waf_rules_response_result_item_model_json

#-----------------------------------------------------------------------------
# Test Class for WafRulesResponseResultItemGroup
#-----------------------------------------------------------------------------
class TestWafRulesResponseResultItemGroup():

    #--------------------------------------------------------
    # Test serialization/deserialization for WafRulesResponseResultItemGroup
    #--------------------------------------------------------
    def test_waf_rules_response_result_item_group_serialization(self):

        # Construct a json representation of a WafRulesResponseResultItemGroup model
        waf_rules_response_result_item_group_model_json = {}
        waf_rules_response_result_item_group_model_json['id'] = 'de677e5818985db1285d0e80225f06e5'
        waf_rules_response_result_item_group_model_json['name'] = 'Project abc'

        # Construct a model instance of WafRulesResponseResultItemGroup by calling from_dict on the json representation
        waf_rules_response_result_item_group_model = WafRulesResponseResultItemGroup.from_dict(waf_rules_response_result_item_group_model_json)
        assert waf_rules_response_result_item_group_model != False

        # Construct a model instance of WafRulesResponseResultItemGroup by calling from_dict on the json representation
        waf_rules_response_result_item_group_model_dict = WafRulesResponseResultItemGroup.from_dict(waf_rules_response_result_item_group_model_json).__dict__
        waf_rules_response_result_item_group_model2 = WafRulesResponseResultItemGroup(**waf_rules_response_result_item_group_model_dict)

        # Verify the model instances are equivalent
        assert waf_rules_response_result_item_group_model == waf_rules_response_result_item_group_model2

        # Convert model instance back to dict and verify no loss of data
        waf_rules_response_result_item_group_model_json2 = waf_rules_response_result_item_group_model.to_dict()
        assert waf_rules_response_result_item_group_model_json2 == waf_rules_response_result_item_group_model_json

#-----------------------------------------------------------------------------
# Test Class for WafRuleResponse
#-----------------------------------------------------------------------------
class TestWafRuleResponse():

    #--------------------------------------------------------
    # Test serialization/deserialization for WafRuleResponse
    #--------------------------------------------------------
    def test_waf_rule_response_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        waf_rule_response_result_group_model = {} # WafRuleResponseResultGroup
        waf_rule_response_result_group_model['id'] = 'de677e5818985db1285d0e80225f06e5'
        waf_rule_response_result_group_model['name'] = 'Project abc'

        waf_rule_response_result_model = {} # WafRuleResponseResult
        waf_rule_response_result_model['id'] = 'f939de3be84e66e757adcdcb87908023'
        waf_rule_response_result_model['description'] = 'SQL-injection-prevention-for-SELECT-statements'
        waf_rule_response_result_model['priority'] = '5'
        waf_rule_response_result_model['group'] = waf_rule_response_result_group_model
        waf_rule_response_result_model['package_id'] = 'a25a9a7e9c00afc1fb2e0245519d725b'
        waf_rule_response_result_model['allowed_modes'] = ['testString']
        waf_rule_response_result_model['mode'] = 'on'

        # Construct a json representation of a WafRuleResponse model
        waf_rule_response_model_json = {}
        waf_rule_response_model_json['success'] = True
        waf_rule_response_model_json['errors'] = [['testString']]
        waf_rule_response_model_json['messages'] = [['testString']]
        waf_rule_response_model_json['result'] = waf_rule_response_result_model

        # Construct a model instance of WafRuleResponse by calling from_dict on the json representation
        waf_rule_response_model = WafRuleResponse.from_dict(waf_rule_response_model_json)
        assert waf_rule_response_model != False

        # Construct a model instance of WafRuleResponse by calling from_dict on the json representation
        waf_rule_response_model_dict = WafRuleResponse.from_dict(waf_rule_response_model_json).__dict__
        waf_rule_response_model2 = WafRuleResponse(**waf_rule_response_model_dict)

        # Verify the model instances are equivalent
        assert waf_rule_response_model == waf_rule_response_model2

        # Convert model instance back to dict and verify no loss of data
        waf_rule_response_model_json2 = waf_rule_response_model.to_dict()
        assert waf_rule_response_model_json2 == waf_rule_response_model_json

#-----------------------------------------------------------------------------
# Test Class for WafRulesResponse
#-----------------------------------------------------------------------------
class TestWafRulesResponse():

    #--------------------------------------------------------
    # Test serialization/deserialization for WafRulesResponse
    #--------------------------------------------------------
    def test_waf_rules_response_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        waf_rules_response_result_item_group_model = {} # WafRulesResponseResultItemGroup
        waf_rules_response_result_item_group_model['id'] = 'de677e5818985db1285d0e80225f06e5'
        waf_rules_response_result_item_group_model['name'] = 'Project abc'

        waf_rules_response_result_info_model = {} # WafRulesResponseResultInfo
        waf_rules_response_result_info_model['page'] = 1
        waf_rules_response_result_info_model['per_page'] = 20
        waf_rules_response_result_info_model['count'] = 1
        waf_rules_response_result_info_model['total_count'] = 2000

        waf_rules_response_result_item_model = {} # WafRulesResponseResultItem
        waf_rules_response_result_item_model['id'] = 'f939de3be84e66e757adcdcb87908023'
        waf_rules_response_result_item_model['description'] = 'SQL-injection-prevention-for-SELECT-statements'
        waf_rules_response_result_item_model['priority'] = '5'
        waf_rules_response_result_item_model['group'] = waf_rules_response_result_item_group_model
        waf_rules_response_result_item_model['package_id'] = 'a25a9a7e9c00afc1fb2e0245519d725b'
        waf_rules_response_result_item_model['allowed_modes'] = ['testString']
        waf_rules_response_result_item_model['mode'] = 'on'

        # Construct a json representation of a WafRulesResponse model
        waf_rules_response_model_json = {}
        waf_rules_response_model_json['success'] = True
        waf_rules_response_model_json['errors'] = [['testString']]
        waf_rules_response_model_json['messages'] = [['testString']]
        waf_rules_response_model_json['result'] = [waf_rules_response_result_item_model]
        waf_rules_response_model_json['result_info'] = waf_rules_response_result_info_model

        # Construct a model instance of WafRulesResponse by calling from_dict on the json representation
        waf_rules_response_model = WafRulesResponse.from_dict(waf_rules_response_model_json)
        assert waf_rules_response_model != False

        # Construct a model instance of WafRulesResponse by calling from_dict on the json representation
        waf_rules_response_model_dict = WafRulesResponse.from_dict(waf_rules_response_model_json).__dict__
        waf_rules_response_model2 = WafRulesResponse(**waf_rules_response_model_dict)

        # Verify the model instances are equivalent
        assert waf_rules_response_model == waf_rules_response_model2

        # Convert model instance back to dict and verify no loss of data
        waf_rules_response_model_json2 = waf_rules_response_model.to_dict()
        assert waf_rules_response_model_json2 == waf_rules_response_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
