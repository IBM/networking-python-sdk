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

    #--------------------------------------------------------
    # list_waf_rules()
    #--------------------------------------------------------
    @responses.activate
    def test_list_waf_rules_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString/rules'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "f939de3be84e66e757adcdcb87908023", "description": "SQL injection prevention for SELECT statements", "priority": 5, "group": {"id": "de677e5818985db1285d0e80225f06e5", "name": "Project abc"}, "package_id": "a25a9a7e9c00afc1fb2e0245519d725b", "allowed_modes": ["[true,false]"], "mode": "true"}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        package_id = 'testString'
        mode = 'testString'
        priority = 36.0
        match = 'testString'
        order = 'testString'
        group_id = 'testString'
        description = 'testString'
        direction = 'testString'
        page = 36.0
        per_page = 36.0

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
            per_page=per_page
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
        url = base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString/rules'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "f939de3be84e66e757adcdcb87908023", "description": "SQL injection prevention for SELECT statements", "priority": 5, "group": {"id": "de677e5818985db1285d0e80225f06e5", "name": "Project abc"}, "package_id": "a25a9a7e9c00afc1fb2e0245519d725b", "allowed_modes": ["[true,false]"], "mode": "true"}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        package_id = 'testString'

        # Invoke method
        response = service.list_waf_rules(
            package_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_waf_rule
#-----------------------------------------------------------------------------
class TestGetWafRule():

    #--------------------------------------------------------
    # get_waf_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_get_waf_rule_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString/rules/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f939de3be84e66e757adcdcb87908023", "description": "SQL injection prevention for SELECT statements", "priority": 5, "group": {"id": "de677e5818985db1285d0e80225f06e5", "name": "Project abc"}, "package_id": "a25a9a7e9c00afc1fb2e0245519d725b", "allowed_modes": ["[true,false]"], "mode": "true"}}'
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
            identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_waf_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_waf_rule_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString/rules/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f939de3be84e66e757adcdcb87908023", "description": "SQL injection prevention for SELECT statements", "priority": 5, "group": {"id": "de677e5818985db1285d0e80225f06e5", "name": "Project abc"}, "package_id": "a25a9a7e9c00afc1fb2e0245519d725b", "allowed_modes": ["[true,false]"], "mode": "true"}}'
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
            identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for update_waf_rule
#-----------------------------------------------------------------------------
class TestUpdateWafRule():

    #--------------------------------------------------------
    # update_waf_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_update_waf_rule_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString/rules/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f939de3be84e66e757adcdcb87908023", "description": "SQL injection prevention for SELECT statements", "priority": 5, "group": {"id": "de677e5818985db1285d0e80225f06e5", "name": "Project abc"}, "package_id": "a25a9a7e9c00afc1fb2e0245519d725b", "allowed_modes": ["[true,false]"], "mode": "true"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a WafRuleBodyCis model
        waf_rule_body_cis_model =  {
            'mode': 'default'
        }
        # Construct a dict representation of a WafRuleBodyOwasp model
        waf_rule_body_owasp_model =  {
            'mode': 'true'
        }

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
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['cis'] == cis
        assert req_body['owasp'] == owasp


    #--------------------------------------------------------
    # test_update_waf_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_waf_rule_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString/rules/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f939de3be84e66e757adcdcb87908023", "description": "SQL injection prevention for SELECT statements", "priority": 5, "group": {"id": "de677e5818985db1285d0e80225f06e5", "name": "Project abc"}, "package_id": "a25a9a7e9c00afc1fb2e0245519d725b", "allowed_modes": ["[true,false]"], "mode": "true"}}'
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
            identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: WAFRules
##############################################################################

