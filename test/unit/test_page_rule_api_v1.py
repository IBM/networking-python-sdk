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
from ibm_cloud_networking_services.page_rule_api_v1 import *

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

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_page_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_get_page_rule_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/pagerules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "9a7806061c88ada191ed06f989cc3dac", "targets": [{"target": "url", "constraint": {"operator": "matches", "value": "*example.com/images/*"}}], "actions": [{"id": "disable_security", "value": {"anyKey": "anyValue"}}], "priority": 1, "status": "active", "modified_on": "2014-01-01T05:20:00.12345Z", "created_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rule_id = 'testString'

        # Invoke method
        response = service.get_page_rule(
            rule_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_page_rule_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_page_rule_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/pagerules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "9a7806061c88ada191ed06f989cc3dac", "targets": [{"target": "url", "constraint": {"operator": "matches", "value": "*example.com/images/*"}}], "actions": [{"id": "disable_security", "value": {"anyKey": "anyValue"}}], "priority": 1, "status": "active", "modified_on": "2014-01-01T05:20:00.12345Z", "created_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rule_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "rule_id": rule_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_page_rule(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for change_page_rule
#-----------------------------------------------------------------------------
class TestChangePageRule():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # change_page_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_change_page_rule_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/pagerules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "9a7806061c88ada191ed06f989cc3dac", "targets": [{"target": "url", "constraint": {"operator": "matches", "value": "*example.com/images/*"}}], "actions": [{"id": "disable_security", "value": {"anyKey": "anyValue"}}], "priority": 1, "status": "active", "modified_on": "2014-01-01T05:20:00.12345Z", "created_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a TargetsItemConstraint model
        targets_item_constraint_model = {}
        targets_item_constraint_model['operator'] = 'matches'
        targets_item_constraint_model['value'] = '*example.com/images/*'

        # Construct a dict representation of a TargetsItem model
        targets_item_model = {}
        targets_item_model['target'] = 'url'
        targets_item_model['constraint'] = targets_item_constraint_model

        # Construct a dict representation of a PageRulesBodyActionsItem model
        page_rules_body_actions_item_model = {}
        page_rules_body_actions_item_model['id'] = 'disable_security'
        page_rules_body_actions_item_model['value'] = { 'foo': 'bar' }

        # Set up parameter values
        rule_id = 'testString'
        targets = [targets_item_model]
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
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['targets'] == [targets_item_model]
        assert req_body['actions'] == [page_rules_body_actions_item_model]
        assert req_body['priority'] == 1
        assert req_body['status'] == 'active'


    #--------------------------------------------------------
    # test_change_page_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_change_page_rule_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/pagerules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "9a7806061c88ada191ed06f989cc3dac", "targets": [{"target": "url", "constraint": {"operator": "matches", "value": "*example.com/images/*"}}], "actions": [{"id": "disable_security", "value": {"anyKey": "anyValue"}}], "priority": 1, "status": "active", "modified_on": "2014-01-01T05:20:00.12345Z", "created_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rule_id = 'testString'

        # Invoke method
        response = service.change_page_rule(
            rule_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_change_page_rule_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_change_page_rule_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/pagerules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "9a7806061c88ada191ed06f989cc3dac", "targets": [{"target": "url", "constraint": {"operator": "matches", "value": "*example.com/images/*"}}], "actions": [{"id": "disable_security", "value": {"anyKey": "anyValue"}}], "priority": 1, "status": "active", "modified_on": "2014-01-01T05:20:00.12345Z", "created_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rule_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "rule_id": rule_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.change_page_rule(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_page_rule
#-----------------------------------------------------------------------------
class TestUpdatePageRule():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_page_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_update_page_rule_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/pagerules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "9a7806061c88ada191ed06f989cc3dac", "targets": [{"target": "url", "constraint": {"operator": "matches", "value": "*example.com/images/*"}}], "actions": [{"id": "disable_security", "value": {"anyKey": "anyValue"}}], "priority": 1, "status": "active", "modified_on": "2014-01-01T05:20:00.12345Z", "created_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a TargetsItemConstraint model
        targets_item_constraint_model = {}
        targets_item_constraint_model['operator'] = 'matches'
        targets_item_constraint_model['value'] = '*example.com/images/*'

        # Construct a dict representation of a TargetsItem model
        targets_item_model = {}
        targets_item_model['target'] = 'url'
        targets_item_model['constraint'] = targets_item_constraint_model

        # Construct a dict representation of a PageRulesBodyActionsItem model
        page_rules_body_actions_item_model = {}
        page_rules_body_actions_item_model['id'] = 'disable_security'
        page_rules_body_actions_item_model['value'] = { 'foo': 'bar' }

        # Set up parameter values
        rule_id = 'testString'
        targets = [targets_item_model]
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
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['targets'] == [targets_item_model]
        assert req_body['actions'] == [page_rules_body_actions_item_model]
        assert req_body['priority'] == 1
        assert req_body['status'] == 'active'


    #--------------------------------------------------------
    # test_update_page_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_page_rule_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/pagerules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "9a7806061c88ada191ed06f989cc3dac", "targets": [{"target": "url", "constraint": {"operator": "matches", "value": "*example.com/images/*"}}], "actions": [{"id": "disable_security", "value": {"anyKey": "anyValue"}}], "priority": 1, "status": "active", "modified_on": "2014-01-01T05:20:00.12345Z", "created_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rule_id = 'testString'

        # Invoke method
        response = service.update_page_rule(
            rule_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_page_rule_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_page_rule_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/pagerules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "9a7806061c88ada191ed06f989cc3dac", "targets": [{"target": "url", "constraint": {"operator": "matches", "value": "*example.com/images/*"}}], "actions": [{"id": "disable_security", "value": {"anyKey": "anyValue"}}], "priority": 1, "status": "active", "modified_on": "2014-01-01T05:20:00.12345Z", "created_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rule_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "rule_id": rule_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_page_rule(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_page_rule
#-----------------------------------------------------------------------------
class TestDeletePageRule():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # delete_page_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_page_rule_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/pagerules/testString')
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
            rule_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_page_rule_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_page_rule_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/pagerules/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "9a7806061c88ada191ed06f989cc3dac"}}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        rule_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "rule_id": rule_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_page_rule(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for list_page_rules
#-----------------------------------------------------------------------------
class TestListPageRules():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # list_page_rules()
    #--------------------------------------------------------
    @responses.activate
    def test_list_page_rules_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/pagerules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "9a7806061c88ada191ed06f989cc3dac", "targets": [{"target": "url", "constraint": {"operator": "matches", "value": "*example.com/images/*"}}], "actions": [{"id": "disable_security", "value": {"anyKey": "anyValue"}}], "priority": 1, "status": "active", "modified_on": "2014-01-01T05:20:00.12345Z", "created_on": "2014-01-01T05:20:00.12345Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        status = 'active'
        order = 'status'
        direction = 'desc'
        match = 'all'

        # Invoke method
        response = service.list_page_rules(
            status=status,
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
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/pagerules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "9a7806061c88ada191ed06f989cc3dac", "targets": [{"target": "url", "constraint": {"operator": "matches", "value": "*example.com/images/*"}}], "actions": [{"id": "disable_security", "value": {"anyKey": "anyValue"}}], "priority": 1, "status": "active", "modified_on": "2014-01-01T05:20:00.12345Z", "created_on": "2014-01-01T05:20:00.12345Z"}]}'
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


    #--------------------------------------------------------
    # test_list_page_rules_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_page_rules_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/pagerules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "9a7806061c88ada191ed06f989cc3dac", "targets": [{"target": "url", "constraint": {"operator": "matches", "value": "*example.com/images/*"}}], "actions": [{"id": "disable_security", "value": {"anyKey": "anyValue"}}], "priority": 1, "status": "active", "modified_on": "2014-01-01T05:20:00.12345Z", "created_on": "2014-01-01T05:20:00.12345Z"}]}'
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
                service.list_page_rules(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for create_page_rule
#-----------------------------------------------------------------------------
class TestCreatePageRule():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # create_page_rule()
    #--------------------------------------------------------
    @responses.activate
    def test_create_page_rule_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/pagerules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "9a7806061c88ada191ed06f989cc3dac", "targets": [{"target": "url", "constraint": {"operator": "matches", "value": "*example.com/images/*"}}], "actions": [{"id": "disable_security", "value": {"anyKey": "anyValue"}}], "priority": 1, "status": "active", "modified_on": "2014-01-01T05:20:00.12345Z", "created_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a TargetsItemConstraint model
        targets_item_constraint_model = {}
        targets_item_constraint_model['operator'] = 'matches'
        targets_item_constraint_model['value'] = '*example.com/images/*'

        # Construct a dict representation of a TargetsItem model
        targets_item_model = {}
        targets_item_model['target'] = 'url'
        targets_item_model['constraint'] = targets_item_constraint_model

        # Construct a dict representation of a PageRulesBodyActionsItem model
        page_rules_body_actions_item_model = {}
        page_rules_body_actions_item_model['id'] = 'disable_security'
        page_rules_body_actions_item_model['value'] = { 'foo': 'bar' }

        # Set up parameter values
        targets = [targets_item_model]
        actions = [page_rules_body_actions_item_model]
        priority = 1
        status = 'active'

        # Invoke method
        response = service.create_page_rule(
            targets=targets,
            actions=actions,
            priority=priority,
            status=status,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['targets'] == [targets_item_model]
        assert req_body['actions'] == [page_rules_body_actions_item_model]
        assert req_body['priority'] == 1
        assert req_body['status'] == 'active'


    #--------------------------------------------------------
    # test_create_page_rule_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_page_rule_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/pagerules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "9a7806061c88ada191ed06f989cc3dac", "targets": [{"target": "url", "constraint": {"operator": "matches", "value": "*example.com/images/*"}}], "actions": [{"id": "disable_security", "value": {"anyKey": "anyValue"}}], "priority": 1, "status": "active", "modified_on": "2014-01-01T05:20:00.12345Z", "created_on": "2014-01-01T05:20:00.12345Z"}}'
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


    #--------------------------------------------------------
    # test_create_page_rule_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_page_rule_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/pagerules')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "9a7806061c88ada191ed06f989cc3dac", "targets": [{"target": "url", "constraint": {"operator": "matches", "value": "*example.com/images/*"}}], "actions": [{"id": "disable_security", "value": {"anyKey": "anyValue"}}], "priority": 1, "status": "active", "modified_on": "2014-01-01T05:20:00.12345Z", "created_on": "2014-01-01T05:20:00.12345Z"}}'
        responses.add(responses.POST,
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
                service.create_page_rule(**req_copy)



# endregion
##############################################################################
# End of Service: PageRules
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for PageRulesBodyActionsItem
#-----------------------------------------------------------------------------
class TestPageRulesBodyActionsItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for PageRulesBodyActionsItem
    #--------------------------------------------------------
    def test_page_rules_body_actions_item_serialization(self):

        # Construct a json representation of a PageRulesBodyActionsItem model
        page_rules_body_actions_item_model_json = {}
        page_rules_body_actions_item_model_json['id'] = 'disable_security'
        page_rules_body_actions_item_model_json['value'] = { 'foo': 'bar' }

        # Construct a model instance of PageRulesBodyActionsItem by calling from_dict on the json representation
        page_rules_body_actions_item_model = PageRulesBodyActionsItem.from_dict(page_rules_body_actions_item_model_json)
        assert page_rules_body_actions_item_model != False

        # Construct a model instance of PageRulesBodyActionsItem by calling from_dict on the json representation
        page_rules_body_actions_item_model_dict = PageRulesBodyActionsItem.from_dict(page_rules_body_actions_item_model_json).__dict__
        page_rules_body_actions_item_model2 = PageRulesBodyActionsItem(**page_rules_body_actions_item_model_dict)

        # Verify the model instances are equivalent
        assert page_rules_body_actions_item_model == page_rules_body_actions_item_model2

        # Convert model instance back to dict and verify no loss of data
        page_rules_body_actions_item_model_json2 = page_rules_body_actions_item_model.to_dict()
        assert page_rules_body_actions_item_model_json2 == page_rules_body_actions_item_model_json

#-----------------------------------------------------------------------------
# Test Class for PageRulesDeleteResponseResult
#-----------------------------------------------------------------------------
class TestPageRulesDeleteResponseResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for PageRulesDeleteResponseResult
    #--------------------------------------------------------
    def test_page_rules_delete_response_result_serialization(self):

        # Construct a json representation of a PageRulesDeleteResponseResult model
        page_rules_delete_response_result_model_json = {}
        page_rules_delete_response_result_model_json['id'] = '9a7806061c88ada191ed06f989cc3dac'

        # Construct a model instance of PageRulesDeleteResponseResult by calling from_dict on the json representation
        page_rules_delete_response_result_model = PageRulesDeleteResponseResult.from_dict(page_rules_delete_response_result_model_json)
        assert page_rules_delete_response_result_model != False

        # Construct a model instance of PageRulesDeleteResponseResult by calling from_dict on the json representation
        page_rules_delete_response_result_model_dict = PageRulesDeleteResponseResult.from_dict(page_rules_delete_response_result_model_json).__dict__
        page_rules_delete_response_result_model2 = PageRulesDeleteResponseResult(**page_rules_delete_response_result_model_dict)

        # Verify the model instances are equivalent
        assert page_rules_delete_response_result_model == page_rules_delete_response_result_model2

        # Convert model instance back to dict and verify no loss of data
        page_rules_delete_response_result_model_json2 = page_rules_delete_response_result_model.to_dict()
        assert page_rules_delete_response_result_model_json2 == page_rules_delete_response_result_model_json

#-----------------------------------------------------------------------------
# Test Class for TargetsItem
#-----------------------------------------------------------------------------
class TestTargetsItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for TargetsItem
    #--------------------------------------------------------
    def test_targets_item_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        targets_item_constraint_model = {} # TargetsItemConstraint
        targets_item_constraint_model['operator'] = 'matches'
        targets_item_constraint_model['value'] = '*example.com/images/*'

        # Construct a json representation of a TargetsItem model
        targets_item_model_json = {}
        targets_item_model_json['target'] = 'url'
        targets_item_model_json['constraint'] = targets_item_constraint_model

        # Construct a model instance of TargetsItem by calling from_dict on the json representation
        targets_item_model = TargetsItem.from_dict(targets_item_model_json)
        assert targets_item_model != False

        # Construct a model instance of TargetsItem by calling from_dict on the json representation
        targets_item_model_dict = TargetsItem.from_dict(targets_item_model_json).__dict__
        targets_item_model2 = TargetsItem(**targets_item_model_dict)

        # Verify the model instances are equivalent
        assert targets_item_model == targets_item_model2

        # Convert model instance back to dict and verify no loss of data
        targets_item_model_json2 = targets_item_model.to_dict()
        assert targets_item_model_json2 == targets_item_model_json

#-----------------------------------------------------------------------------
# Test Class for TargetsItemConstraint
#-----------------------------------------------------------------------------
class TestTargetsItemConstraint():

    #--------------------------------------------------------
    # Test serialization/deserialization for TargetsItemConstraint
    #--------------------------------------------------------
    def test_targets_item_constraint_serialization(self):

        # Construct a json representation of a TargetsItemConstraint model
        targets_item_constraint_model_json = {}
        targets_item_constraint_model_json['operator'] = 'matches'
        targets_item_constraint_model_json['value'] = '*example.com/images/*'

        # Construct a model instance of TargetsItemConstraint by calling from_dict on the json representation
        targets_item_constraint_model = TargetsItemConstraint.from_dict(targets_item_constraint_model_json)
        assert targets_item_constraint_model != False

        # Construct a model instance of TargetsItemConstraint by calling from_dict on the json representation
        targets_item_constraint_model_dict = TargetsItemConstraint.from_dict(targets_item_constraint_model_json).__dict__
        targets_item_constraint_model2 = TargetsItemConstraint(**targets_item_constraint_model_dict)

        # Verify the model instances are equivalent
        assert targets_item_constraint_model == targets_item_constraint_model2

        # Convert model instance back to dict and verify no loss of data
        targets_item_constraint_model_json2 = targets_item_constraint_model.to_dict()
        assert targets_item_constraint_model_json2 == targets_item_constraint_model_json

#-----------------------------------------------------------------------------
# Test Class for PageRulesDeleteResponse
#-----------------------------------------------------------------------------
class TestPageRulesDeleteResponse():

    #--------------------------------------------------------
    # Test serialization/deserialization for PageRulesDeleteResponse
    #--------------------------------------------------------
    def test_page_rules_delete_response_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        page_rules_delete_response_result_model = {} # PageRulesDeleteResponseResult
        page_rules_delete_response_result_model['id'] = '9a7806061c88ada191ed06f989cc3dac'

        # Construct a json representation of a PageRulesDeleteResponse model
        page_rules_delete_response_model_json = {}
        page_rules_delete_response_model_json['success'] = True
        page_rules_delete_response_model_json['errors'] = [['testString']]
        page_rules_delete_response_model_json['messages'] = [['testString']]
        page_rules_delete_response_model_json['result'] = page_rules_delete_response_result_model

        # Construct a model instance of PageRulesDeleteResponse by calling from_dict on the json representation
        page_rules_delete_response_model = PageRulesDeleteResponse.from_dict(page_rules_delete_response_model_json)
        assert page_rules_delete_response_model != False

        # Construct a model instance of PageRulesDeleteResponse by calling from_dict on the json representation
        page_rules_delete_response_model_dict = PageRulesDeleteResponse.from_dict(page_rules_delete_response_model_json).__dict__
        page_rules_delete_response_model2 = PageRulesDeleteResponse(**page_rules_delete_response_model_dict)

        # Verify the model instances are equivalent
        assert page_rules_delete_response_model == page_rules_delete_response_model2

        # Convert model instance back to dict and verify no loss of data
        page_rules_delete_response_model_json2 = page_rules_delete_response_model.to_dict()
        assert page_rules_delete_response_model_json2 == page_rules_delete_response_model_json

#-----------------------------------------------------------------------------
# Test Class for PageRulesResponseListAll
#-----------------------------------------------------------------------------
class TestPageRulesResponseListAll():

    #--------------------------------------------------------
    # Test serialization/deserialization for PageRulesResponseListAll
    #--------------------------------------------------------
    def test_page_rules_response_list_all_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        targets_item_constraint_model = {} # TargetsItemConstraint
        targets_item_constraint_model['operator'] = 'matches'
        targets_item_constraint_model['value'] = '*example.com/images/*'

        page_rules_body_actions_item_model = {} # PageRulesBodyActionsItem
        page_rules_body_actions_item_model['id'] = 'disable_security'
        page_rules_body_actions_item_model['value'] = { 'foo': 'bar' }

        targets_item_model = {} # TargetsItem
        targets_item_model['target'] = 'url'
        targets_item_model['constraint'] = targets_item_constraint_model

        page_rule_result_model = {} # PageRuleResult
        page_rule_result_model['id'] = '9a7806061c88ada191ed06f989cc3dac'
        page_rule_result_model['targets'] = [targets_item_model]
        page_rule_result_model['actions'] = [page_rules_body_actions_item_model]
        page_rule_result_model['priority'] = 1
        page_rule_result_model['status'] = 'active'
        page_rule_result_model['modified_on'] = '2014-01-01T05:20:00.12345Z'
        page_rule_result_model['created_on'] = '2014-01-01T05:20:00.12345Z'

        # Construct a json representation of a PageRulesResponseListAll model
        page_rules_response_list_all_model_json = {}
        page_rules_response_list_all_model_json['success'] = True
        page_rules_response_list_all_model_json['errors'] = [['testString']]
        page_rules_response_list_all_model_json['messages'] = [['testString']]
        page_rules_response_list_all_model_json['result'] = [page_rule_result_model]

        # Construct a model instance of PageRulesResponseListAll by calling from_dict on the json representation
        page_rules_response_list_all_model = PageRulesResponseListAll.from_dict(page_rules_response_list_all_model_json)
        assert page_rules_response_list_all_model != False

        # Construct a model instance of PageRulesResponseListAll by calling from_dict on the json representation
        page_rules_response_list_all_model_dict = PageRulesResponseListAll.from_dict(page_rules_response_list_all_model_json).__dict__
        page_rules_response_list_all_model2 = PageRulesResponseListAll(**page_rules_response_list_all_model_dict)

        # Verify the model instances are equivalent
        assert page_rules_response_list_all_model == page_rules_response_list_all_model2

        # Convert model instance back to dict and verify no loss of data
        page_rules_response_list_all_model_json2 = page_rules_response_list_all_model.to_dict()
        assert page_rules_response_list_all_model_json2 == page_rules_response_list_all_model_json

#-----------------------------------------------------------------------------
# Test Class for PageRulesResponseWithoutResultInfo
#-----------------------------------------------------------------------------
class TestPageRulesResponseWithoutResultInfo():

    #--------------------------------------------------------
    # Test serialization/deserialization for PageRulesResponseWithoutResultInfo
    #--------------------------------------------------------
    def test_page_rules_response_without_result_info_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        targets_item_constraint_model = {} # TargetsItemConstraint
        targets_item_constraint_model['operator'] = 'matches'
        targets_item_constraint_model['value'] = '*example.com/images/*'

        page_rules_body_actions_item_model = {} # PageRulesBodyActionsItem
        page_rules_body_actions_item_model['id'] = 'disable_security'
        page_rules_body_actions_item_model['value'] = { 'foo': 'bar' }

        targets_item_model = {} # TargetsItem
        targets_item_model['target'] = 'url'
        targets_item_model['constraint'] = targets_item_constraint_model

        page_rule_result_model = {} # PageRuleResult
        page_rule_result_model['id'] = '9a7806061c88ada191ed06f989cc3dac'
        page_rule_result_model['targets'] = [targets_item_model]
        page_rule_result_model['actions'] = [page_rules_body_actions_item_model]
        page_rule_result_model['priority'] = 1
        page_rule_result_model['status'] = 'active'
        page_rule_result_model['modified_on'] = '2014-01-01T05:20:00.12345Z'
        page_rule_result_model['created_on'] = '2014-01-01T05:20:00.12345Z'

        # Construct a json representation of a PageRulesResponseWithoutResultInfo model
        page_rules_response_without_result_info_model_json = {}
        page_rules_response_without_result_info_model_json['success'] = True
        page_rules_response_without_result_info_model_json['errors'] = [['testString']]
        page_rules_response_without_result_info_model_json['messages'] = [['testString']]
        page_rules_response_without_result_info_model_json['result'] = page_rule_result_model

        # Construct a model instance of PageRulesResponseWithoutResultInfo by calling from_dict on the json representation
        page_rules_response_without_result_info_model = PageRulesResponseWithoutResultInfo.from_dict(page_rules_response_without_result_info_model_json)
        assert page_rules_response_without_result_info_model != False

        # Construct a model instance of PageRulesResponseWithoutResultInfo by calling from_dict on the json representation
        page_rules_response_without_result_info_model_dict = PageRulesResponseWithoutResultInfo.from_dict(page_rules_response_without_result_info_model_json).__dict__
        page_rules_response_without_result_info_model2 = PageRulesResponseWithoutResultInfo(**page_rules_response_without_result_info_model_dict)

        # Verify the model instances are equivalent
        assert page_rules_response_without_result_info_model == page_rules_response_without_result_info_model2

        # Convert model instance back to dict and verify no loss of data
        page_rules_response_without_result_info_model_json2 = page_rules_response_without_result_info_model.to_dict()
        assert page_rules_response_without_result_info_model_json2 == page_rules_response_without_result_info_model_json

#-----------------------------------------------------------------------------
# Test Class for PageRuleResult
#-----------------------------------------------------------------------------
class TestPageRuleResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for PageRuleResult
    #--------------------------------------------------------
    def test_page_rule_result_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        targets_item_constraint_model = {} # TargetsItemConstraint
        targets_item_constraint_model['operator'] = 'matches'
        targets_item_constraint_model['value'] = '*example.com/images/*'

        page_rules_body_actions_item_model = {} # PageRulesBodyActionsItem
        page_rules_body_actions_item_model['id'] = 'disable_security'
        page_rules_body_actions_item_model['value'] = { 'foo': 'bar' }

        targets_item_model = {} # TargetsItem
        targets_item_model['target'] = 'url'
        targets_item_model['constraint'] = targets_item_constraint_model

        # Construct a json representation of a PageRuleResult model
        page_rule_result_model_json = {}
        page_rule_result_model_json['id'] = '9a7806061c88ada191ed06f989cc3dac'
        page_rule_result_model_json['targets'] = [targets_item_model]
        page_rule_result_model_json['actions'] = [page_rules_body_actions_item_model]
        page_rule_result_model_json['priority'] = 1
        page_rule_result_model_json['status'] = 'active'
        page_rule_result_model_json['modified_on'] = '2014-01-01T05:20:00.12345Z'
        page_rule_result_model_json['created_on'] = '2014-01-01T05:20:00.12345Z'

        # Construct a model instance of PageRuleResult by calling from_dict on the json representation
        page_rule_result_model = PageRuleResult.from_dict(page_rule_result_model_json)
        assert page_rule_result_model != False

        # Construct a model instance of PageRuleResult by calling from_dict on the json representation
        page_rule_result_model_dict = PageRuleResult.from_dict(page_rule_result_model_json).__dict__
        page_rule_result_model2 = PageRuleResult(**page_rule_result_model_dict)

        # Verify the model instances are equivalent
        assert page_rule_result_model == page_rule_result_model2

        # Convert model instance back to dict and verify no loss of data
        page_rule_result_model_json2 = page_rule_result_model.to_dict()
        assert page_rule_result_model_json2 == page_rule_result_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
