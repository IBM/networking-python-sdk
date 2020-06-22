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

    #--------------------------------------------------------
    # list_waf_rule_groups()
    #--------------------------------------------------------
    @responses.activate
    def test_list_waf_rule_groups_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString/groups'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [[{"id": "a25a9a7e9c00afc1fb2e0245519d725b", "name": "Project Honey Pot", "description": "Group designed to protect against IP addresses that are a threat and typically used to launch DDoS attacks", "rules_count": 10, "modified_rules_count": 10, "package_id": "a25a9a7e9c00afc1fb2e0245519d725b", "mode": "true", "allowed_modes": ["[true,false]"]}]], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pkg_id = 'testString'
        name = 'testString'
        mode = 'true'
        rules_count = 'testString'
        page = 38
        per_page = 38
        order = 'testString'
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
            match=match
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
        url = base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString/groups'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [[{"id": "a25a9a7e9c00afc1fb2e0245519d725b", "name": "Project Honey Pot", "description": "Group designed to protect against IP addresses that are a threat and typically used to launch DDoS attacks", "rules_count": 10, "modified_rules_count": 10, "package_id": "a25a9a7e9c00afc1fb2e0245519d725b", "mode": "true", "allowed_modes": ["[true,false]"]}]], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pkg_id = 'testString'

        # Invoke method
        response = service.list_waf_rule_groups(
            pkg_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_waf_rule_group
#-----------------------------------------------------------------------------
class TestGetWafRuleGroup():

    #--------------------------------------------------------
    # get_waf_rule_group()
    #--------------------------------------------------------
    @responses.activate
    def test_get_waf_rule_group_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString/groups/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "a25a9a7e9c00afc1fb2e0245519d725b", "name": "Project Honey Pot", "description": "Group designed to protect against IP addresses that are a threat and typically used to launch DDoS attacks", "rules_count": 10, "modified_rules_count": 10, "package_id": "a25a9a7e9c00afc1fb2e0245519d725b", "mode": "true", "allowed_modes": ["[true,false]"]}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
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
            group_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_waf_rule_group_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_waf_rule_group_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString/groups/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "a25a9a7e9c00afc1fb2e0245519d725b", "name": "Project Honey Pot", "description": "Group designed to protect against IP addresses that are a threat and typically used to launch DDoS attacks", "rules_count": 10, "modified_rules_count": 10, "package_id": "a25a9a7e9c00afc1fb2e0245519d725b", "mode": "true", "allowed_modes": ["[true,false]"]}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
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
            group_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for update_waf_rule_group
#-----------------------------------------------------------------------------
class TestUpdateWafRuleGroup():

    #--------------------------------------------------------
    # update_waf_rule_group()
    #--------------------------------------------------------
    @responses.activate
    def test_update_waf_rule_group_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString/groups/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "a25a9a7e9c00afc1fb2e0245519d725b", "name": "Project Honey Pot", "description": "Group designed to protect against IP addresses that are a threat and typically used to launch DDoS attacks", "rules_count": 10, "modified_rules_count": 10, "package_id": "a25a9a7e9c00afc1fb2e0245519d725b", "mode": "true", "allowed_modes": ["[true,false]"]}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        pkg_id = 'testString'
        group_id = 'testString'
        mode = 'true'

        # Invoke method
        response = service.update_waf_rule_group(
            pkg_id,
            group_id,
            mode=mode,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['mode'] == mode


    #--------------------------------------------------------
    # test_update_waf_rule_group_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_waf_rule_group_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/firewall/waf/packages/testString/groups/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "a25a9a7e9c00afc1fb2e0245519d725b", "name": "Project Honey Pot", "description": "Group designed to protect against IP addresses that are a threat and typically used to launch DDoS attacks", "rules_count": 10, "modified_rules_count": 10, "package_id": "a25a9a7e9c00afc1fb2e0245519d725b", "mode": "true", "allowed_modes": ["[true,false]"]}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}}'
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
            group_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: WAFRuleGroups
##############################################################################

