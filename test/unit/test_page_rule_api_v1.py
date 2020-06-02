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
from ibm_cloud_networking_services import PageRuleApiV1

crn = 'testString'
zone_id = 'testString'

service = PageRuleApiV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn,
    zone_id=zone_id
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: PageRules
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_page_rule
#-----------------------------------------------------------------------------
class TestGetPageRule():

    #--------------------------------------------------------
    # get_page_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_get_page_rule_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/pagerules/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "9a7806061c88ada191ed06f989cc3dac", "targets": [{"target": "url", "constraint": {"operator": "matches", "value": "*example.com/images/*"}}], "actions": [{"value": 5, "id": "disable_security"}], "priority": 1, "status": "active", "modified_on": "2014-01-01T05:20:00.12345Z", "created_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rule_id = 'testString'

        # Invoke method
        response = service.get_page_rule(
            rule_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_page_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_page_rule_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/pagerules/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "9a7806061c88ada191ed06f989cc3dac", "targets": [{"target": "url", "constraint": {"operator": "matches", "value": "*example.com/images/*"}}], "actions": [{"value": 5, "id": "disable_security"}], "priority": 1, "status": "active", "modified_on": "2014-01-01T05:20:00.12345Z", "created_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rule_id = 'testString'

        # Invoke method
        response = service.get_page_rule(
            rule_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for change_page_rule
#-----------------------------------------------------------------------------
class TestChangePageRule():

    #--------------------------------------------------------
    # change_page_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_change_page_rule_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/pagerules/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "9a7806061c88ada191ed06f989cc3dac", "targets": [{"target": "url", "constraint": {"operator": "matches", "value": "*example.com/images/*"}}], "actions": [{"value": 5, "id": "disable_security"}], "priority": 1, "status": "active", "modified_on": "2014-01-01T05:20:00.12345Z", "created_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a PageRulesBodyTargetsItemConstraint model
        page_rules_body_targets_item_constraint_model =  {
            'operator': 'matches',
            'value': '*example.com/images/*'
        }
        # Construct a dict representation of a PageRulesBodyTargetsItem model
        page_rules_body_targets_item_model =  {
            'target': 'url',
            'constraint': page_rules_body_targets_item_constraint_model
        }
        # Construct a dict representation of a PageRulesBodyActionsItemActionsSecurity model
        page_rules_body_actions_item_model =  {
            'value': 38,
            'id': 'disable_security'
        }

        # Set up parameter values
        rule_id = 'testString'
        targets = [page_rules_body_targets_item_model]
        actions = [page_rules_body_actions_item_model]
        priority = 1
        status = 'active'

        # Invoke method
        response = service.change_page_rule(
            rule_id,
            targets=targets,
            actions=actions,
            priority=priority,
            status=status,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['targets'] == targets
        assert req_body['actions'] == actions
        assert req_body['priority'] == priority
        assert req_body['status'] == status


    #--------------------------------------------------------
    # test_change_page_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_change_page_rule_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/pagerules/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "9a7806061c88ada191ed06f989cc3dac", "targets": [{"target": "url", "constraint": {"operator": "matches", "value": "*example.com/images/*"}}], "actions": [{"value": 5, "id": "disable_security"}], "priority": 1, "status": "active", "modified_on": "2014-01-01T05:20:00.12345Z", "created_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rule_id = 'testString'

        # Invoke method
        response = service.change_page_rule(
            rule_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for update_page_rule
#-----------------------------------------------------------------------------
class TestUpdatePageRule():

    #--------------------------------------------------------
    # update_page_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_update_page_rule_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/pagerules/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "9a7806061c88ada191ed06f989cc3dac", "targets": [{"target": "url", "constraint": {"operator": "matches", "value": "*example.com/images/*"}}], "actions": [{"value": 5, "id": "disable_security"}], "priority": 1, "status": "active", "modified_on": "2014-01-01T05:20:00.12345Z", "created_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a PageRulesBodyTargetsItemConstraint model
        page_rules_body_targets_item_constraint_model =  {
            'operator': 'matches',
            'value': '*example.com/images/*'
        }
        # Construct a dict representation of a PageRulesBodyTargetsItem model
        page_rules_body_targets_item_model =  {
            'target': 'url',
            'constraint': page_rules_body_targets_item_constraint_model
        }
        # Construct a dict representation of a PageRulesBodyActionsItemActionsSecurity model
        page_rules_body_actions_item_model =  {
            'value': 38,
            'id': 'disable_security'
        }

        # Set up parameter values
        rule_id = 'testString'
        targets = [page_rules_body_targets_item_model]
        actions = [page_rules_body_actions_item_model]
        priority = 1
        status = 'active'

        # Invoke method
        response = service.update_page_rule(
            rule_id,
            targets=targets,
            actions=actions,
            priority=priority,
            status=status,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['targets'] == targets
        assert req_body['actions'] == actions
        assert req_body['priority'] == priority
        assert req_body['status'] == status


    #--------------------------------------------------------
    # test_update_page_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_page_rule_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/pagerules/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "9a7806061c88ada191ed06f989cc3dac", "targets": [{"target": "url", "constraint": {"operator": "matches", "value": "*example.com/images/*"}}], "actions": [{"value": 5, "id": "disable_security"}], "priority": 1, "status": "active", "modified_on": "2014-01-01T05:20:00.12345Z", "created_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rule_id = 'testString'

        # Invoke method
        response = service.update_page_rule(
            rule_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for delete_page_rule
#-----------------------------------------------------------------------------
class TestDeletePageRule():

    #--------------------------------------------------------
    # delete_page_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_page_rule_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/pagerules/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "9a7806061c88ada191ed06f989cc3dac"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rule_id = 'testString'

        # Invoke method
        response = service.delete_page_rule(
            rule_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_page_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_page_rule_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/pagerules/testString'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "9a7806061c88ada191ed06f989cc3dac"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rule_id = 'testString'

        # Invoke method
        response = service.delete_page_rule(
            rule_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for list_page_rules
#-----------------------------------------------------------------------------
class TestListPageRules():

    #--------------------------------------------------------
    # list_page_rules()
    #--------------------------------------------------------
    @responses.activate
    def test_list_page_rules_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/pagerules'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "9a7806061c88ada191ed06f989cc3dac", "targets": [{"target": "url", "constraint": {"operator": "matches", "value": "*example.com/images/*"}}], "actions": [{"value": 5, "id": "disable_security"}], "priority": 1, "status": "active", "modified_on": "2014-01-01T05:20:00.12345Z", "created_on": "2014-01-01T05:20:00.12345Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        status = 'testString'
        order = 'testString'
        direction = 'testString'
        match = 'testString'

        # Invoke method
        response = service.list_page_rules(
            status=status,
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
        assert 'status={}'.format(status) in query_string
        assert 'order={}'.format(order) in query_string
        assert 'direction={}'.format(direction) in query_string
        assert 'match={}'.format(match) in query_string


    #--------------------------------------------------------
    # test_list_page_rules_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_page_rules_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/pagerules'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "9a7806061c88ada191ed06f989cc3dac", "targets": [{"target": "url", "constraint": {"operator": "matches", "value": "*example.com/images/*"}}], "actions": [{"value": 5, "id": "disable_security"}], "priority": 1, "status": "active", "modified_on": "2014-01-01T05:20:00.12345Z", "created_on": "2014-01-01T05:20:00.12345Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_page_rules()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for create_page_rule
#-----------------------------------------------------------------------------
class TestCreatePageRule():

    #--------------------------------------------------------
    # create_page_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_create_page_rule_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/pagerules'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "9a7806061c88ada191ed06f989cc3dac", "targets": [{"target": "url", "constraint": {"operator": "matches", "value": "*example.com/images/*"}}], "actions": [{"value": 5, "id": "disable_security"}], "priority": 1, "status": "active", "modified_on": "2014-01-01T05:20:00.12345Z", "created_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a PageRulesBodyTargetsItemConstraint model
        page_rules_body_targets_item_constraint_model =  {
            'operator': 'matches',
            'value': '*example.com/images/*'
        }
        # Construct a dict representation of a PageRulesBodyTargetsItem model
        page_rules_body_targets_item_model =  {
            'target': 'url',
            'constraint': page_rules_body_targets_item_constraint_model
        }
        # Construct a dict representation of a PageRulesBodyActionsItemActionsSecurity model
        page_rules_body_actions_item_model =  {
            'value': 38,
            'id': 'disable_security'
        }

        # Set up parameter values
        targets = [page_rules_body_targets_item_model]
        actions = [page_rules_body_actions_item_model]
        priority = 1
        status = 'active'

        # Invoke method
        response = service.create_page_rule(
            targets=targets,
            actions=actions,
            priority=priority,
            status=status,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['targets'] == targets
        assert req_body['actions'] == actions
        assert req_body['priority'] == priority
        assert req_body['status'] == status


    #--------------------------------------------------------
    # test_create_page_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_page_rule_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/pagerules'
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "9a7806061c88ada191ed06f989cc3dac", "targets": [{"target": "url", "constraint": {"operator": "matches", "value": "*example.com/images/*"}}], "actions": [{"value": 5, "id": "disable_security"}], "priority": 1, "status": "active", "modified_on": "2014-01-01T05:20:00.12345Z", "created_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.create_page_rule()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: PageRules
##############################################################################

