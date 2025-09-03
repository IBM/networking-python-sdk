# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2025.
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

"""
Unit Tests for RulesetsV1
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import os
import pytest
import re
import responses
import urllib
from ibm_cloud_networking_services.rulesets_v1 import *

crn = 'testString'
zone_identifier = 'testString'

_service = RulesetsV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn,
    zone_identifier=zone_identifier,
)

_base_url = 'https://api.cis.cloud.ibm.com'
_service.set_service_url(_base_url)


def preprocess_url(operation_path: str):
    """
    Returns the request url associated with the specified operation path.
    This will be base_url concatenated with a quoted version of operation_path.
    The returned request URL is used to register the mock response so it needs
    to match the request URL that is formed by the requests library.
    """

    # Form the request URL from the base URL and operation path.
    request_url = _base_url + operation_path

    # If the request url does NOT end with a /, then just return it as-is.
    # Otherwise, return a regular expression that matches one or more trailing /.
    if not request_url.endswith('/'):
        return request_url
    return re.compile(request_url.rstrip('/') + '/+')


##############################################################################
# Start of Service: InstanceRulesets
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = RulesetsV1.new_instance(
            crn=crn,
            zone_identifier=zone_identifier,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, RulesetsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = RulesetsV1.new_instance(
                crn=crn,
                zone_identifier=zone_identifier,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = RulesetsV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='crn must be provided must be provided'):
            service = RulesetsV1.new_instance(
                crn=None,
                zone_identifier=None,
            )


class TestGetInstanceRulesets:
    """
    Test Class for get_instance_rulesets
    """

    @responses.activate
    def test_get_instance_rulesets_all_params(self):
        """
        get_instance_rulesets()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": [{"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_instance_rulesets()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_instance_rulesets_all_params_with_retries(self):
        # Enable retries and run test_get_instance_rulesets_all_params.
        _service.enable_retries()
        self.test_get_instance_rulesets_all_params()

        # Disable retries and run test_get_instance_rulesets_all_params.
        _service.disable_retries()
        self.test_get_instance_rulesets_all_params()

    @responses.activate
    def test_get_instance_rulesets_value_error(self):
        """
        test_get_instance_rulesets_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": [{"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_instance_rulesets(**req_copy)

    def test_get_instance_rulesets_value_error_with_retries(self):
        # Enable retries and run test_get_instance_rulesets_value_error.
        _service.enable_retries()
        self.test_get_instance_rulesets_value_error()

        # Disable retries and run test_get_instance_rulesets_value_error.
        _service.disable_retries()
        self.test_get_instance_rulesets_value_error()


class TestGetInstanceRuleset:
    """
    Test Class for get_instance_ruleset
    """

    @responses.activate
    def test_get_instance_ruleset_all_params(self):
        """
        get_instance_ruleset()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/testString')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_id = 'testString'

        # Invoke method
        response = _service.get_instance_ruleset(
            ruleset_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_instance_ruleset_all_params_with_retries(self):
        # Enable retries and run test_get_instance_ruleset_all_params.
        _service.enable_retries()
        self.test_get_instance_ruleset_all_params()

        # Disable retries and run test_get_instance_ruleset_all_params.
        _service.disable_retries()
        self.test_get_instance_ruleset_all_params()

    @responses.activate
    def test_get_instance_ruleset_value_error(self):
        """
        test_get_instance_ruleset_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/testString')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "ruleset_id": ruleset_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_instance_ruleset(**req_copy)

    def test_get_instance_ruleset_value_error_with_retries(self):
        # Enable retries and run test_get_instance_ruleset_value_error.
        _service.enable_retries()
        self.test_get_instance_ruleset_value_error()

        # Disable retries and run test_get_instance_ruleset_value_error.
        _service.disable_retries()
        self.test_get_instance_ruleset_value_error()


class TestUpdateInstanceRuleset:
    """
    Test Class for update_instance_ruleset
    """

    @responses.activate
    def test_update_instance_ruleset_all_params(self):
        """
        update_instance_ruleset()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/testString')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a RulesOverride model
        rules_override_model = {}
        rules_override_model['id'] = 'testString'
        rules_override_model['enabled'] = True
        rules_override_model['action'] = 'testString'
        rules_override_model['sensitivity_level'] = 'high'
        rules_override_model['score_threshold'] = 60

        # Construct a dict representation of a CategoriesOverride model
        categories_override_model = {}
        categories_override_model['category'] = 'testString'
        categories_override_model['enabled'] = True
        categories_override_model['action'] = 'testString'

        # Construct a dict representation of a Overrides model
        overrides_model = {}
        overrides_model['action'] = 'testString'
        overrides_model['enabled'] = True
        overrides_model['sensitivity_level'] = 'high'
        overrides_model['rules'] = [rules_override_model]
        overrides_model['categories'] = [categories_override_model]

        # Construct a dict representation of a ActionParametersResponse model
        action_parameters_response_model = {}
        action_parameters_response_model['content'] = '{"success": false, "error": "you have been blocked"}'
        action_parameters_response_model['content_type'] = 'application/json'
        action_parameters_response_model['status_code'] = 400

        # Construct a dict representation of a ActionParameters model
        action_parameters_model = {}
        action_parameters_model['id'] = 'testString'
        action_parameters_model['overrides'] = overrides_model
        action_parameters_model['version'] = 'testString'
        action_parameters_model['ruleset'] = 'testString'
        action_parameters_model['rulesets'] = ['testString']
        action_parameters_model['phases'] = ['testString']
        action_parameters_model['products'] = ['testString']
        action_parameters_model['response'] = action_parameters_response_model

        # Construct a dict representation of a Ratelimit model
        ratelimit_model = {}
        ratelimit_model['characteristics'] = ['testString']
        ratelimit_model['counting_expression'] = 'testString'
        ratelimit_model['mitigation_timeout'] = 38
        ratelimit_model['period'] = 38
        ratelimit_model['requests_per_period'] = 38

        # Construct a dict representation of a Logging model
        logging_model = {}
        logging_model['enabled'] = True

        # Construct a dict representation of a Position model
        position_model = {}
        position_model['before'] = 'testString'
        position_model['after'] = 'testString'
        position_model['index'] = 0

        # Construct a dict representation of a RuleCreate model
        rule_create_model = {}
        rule_create_model['action'] = 'testString'
        rule_create_model['action_parameters'] = action_parameters_model
        rule_create_model['ratelimit'] = ratelimit_model
        rule_create_model['description'] = 'testString'
        rule_create_model['enabled'] = True
        rule_create_model['expression'] = 'ip.src ne 1.1.1.1'
        rule_create_model['id'] = 'testString'
        rule_create_model['logging'] = logging_model
        rule_create_model['ref'] = 'my_ref'
        rule_create_model['position'] = position_model

        # Set up parameter values
        ruleset_id = 'testString'
        description = 'Custom instance ruleset'
        kind = 'managed'
        name = 'testString'
        phase = 'ddos_l4'
        rules = [rule_create_model]

        # Invoke method
        response = _service.update_instance_ruleset(
            ruleset_id,
            description=description,
            kind=kind,
            name=name,
            phase=phase,
            rules=rules,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['description'] == 'Custom instance ruleset'
        assert req_body['kind'] == 'managed'
        assert req_body['name'] == 'testString'
        assert req_body['phase'] == 'ddos_l4'
        assert req_body['rules'] == [rule_create_model]

    def test_update_instance_ruleset_all_params_with_retries(self):
        # Enable retries and run test_update_instance_ruleset_all_params.
        _service.enable_retries()
        self.test_update_instance_ruleset_all_params()

        # Disable retries and run test_update_instance_ruleset_all_params.
        _service.disable_retries()
        self.test_update_instance_ruleset_all_params()

    @responses.activate
    def test_update_instance_ruleset_required_params(self):
        """
        test_update_instance_ruleset_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/testString')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_id = 'testString'

        # Invoke method
        response = _service.update_instance_ruleset(
            ruleset_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_instance_ruleset_required_params_with_retries(self):
        # Enable retries and run test_update_instance_ruleset_required_params.
        _service.enable_retries()
        self.test_update_instance_ruleset_required_params()

        # Disable retries and run test_update_instance_ruleset_required_params.
        _service.disable_retries()
        self.test_update_instance_ruleset_required_params()

    @responses.activate
    def test_update_instance_ruleset_value_error(self):
        """
        test_update_instance_ruleset_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/testString')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "ruleset_id": ruleset_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_instance_ruleset(**req_copy)

    def test_update_instance_ruleset_value_error_with_retries(self):
        # Enable retries and run test_update_instance_ruleset_value_error.
        _service.enable_retries()
        self.test_update_instance_ruleset_value_error()

        # Disable retries and run test_update_instance_ruleset_value_error.
        _service.disable_retries()
        self.test_update_instance_ruleset_value_error()


class TestDeleteInstanceRuleset:
    """
    Test Class for delete_instance_ruleset
    """

    @responses.activate
    def test_delete_instance_ruleset_all_params(self):
        """
        delete_instance_ruleset()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        ruleset_id = 'testString'

        # Invoke method
        response = _service.delete_instance_ruleset(
            ruleset_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_instance_ruleset_all_params_with_retries(self):
        # Enable retries and run test_delete_instance_ruleset_all_params.
        _service.enable_retries()
        self.test_delete_instance_ruleset_all_params()

        # Disable retries and run test_delete_instance_ruleset_all_params.
        _service.disable_retries()
        self.test_delete_instance_ruleset_all_params()

    @responses.activate
    def test_delete_instance_ruleset_value_error(self):
        """
        test_delete_instance_ruleset_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        ruleset_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "ruleset_id": ruleset_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_instance_ruleset(**req_copy)

    def test_delete_instance_ruleset_value_error_with_retries(self):
        # Enable retries and run test_delete_instance_ruleset_value_error.
        _service.enable_retries()
        self.test_delete_instance_ruleset_value_error()

        # Disable retries and run test_delete_instance_ruleset_value_error.
        _service.disable_retries()
        self.test_delete_instance_ruleset_value_error()


class TestGetInstanceRulesetVersions:
    """
    Test Class for get_instance_ruleset_versions
    """

    @responses.activate
    def test_get_instance_ruleset_versions_all_params(self):
        """
        get_instance_ruleset_versions()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/testString/versions')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": [{"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_id = 'testString'

        # Invoke method
        response = _service.get_instance_ruleset_versions(
            ruleset_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_instance_ruleset_versions_all_params_with_retries(self):
        # Enable retries and run test_get_instance_ruleset_versions_all_params.
        _service.enable_retries()
        self.test_get_instance_ruleset_versions_all_params()

        # Disable retries and run test_get_instance_ruleset_versions_all_params.
        _service.disable_retries()
        self.test_get_instance_ruleset_versions_all_params()

    @responses.activate
    def test_get_instance_ruleset_versions_value_error(self):
        """
        test_get_instance_ruleset_versions_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/testString/versions')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": [{"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "ruleset_id": ruleset_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_instance_ruleset_versions(**req_copy)

    def test_get_instance_ruleset_versions_value_error_with_retries(self):
        # Enable retries and run test_get_instance_ruleset_versions_value_error.
        _service.enable_retries()
        self.test_get_instance_ruleset_versions_value_error()

        # Disable retries and run test_get_instance_ruleset_versions_value_error.
        _service.disable_retries()
        self.test_get_instance_ruleset_versions_value_error()


class TestGetInstanceRulesetVersion:
    """
    Test Class for get_instance_ruleset_version
    """

    @responses.activate
    def test_get_instance_ruleset_version_all_params(self):
        """
        get_instance_ruleset_version()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/testString/versions/1')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_id = 'testString'
        ruleset_version = '1'

        # Invoke method
        response = _service.get_instance_ruleset_version(
            ruleset_id,
            ruleset_version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_instance_ruleset_version_all_params_with_retries(self):
        # Enable retries and run test_get_instance_ruleset_version_all_params.
        _service.enable_retries()
        self.test_get_instance_ruleset_version_all_params()

        # Disable retries and run test_get_instance_ruleset_version_all_params.
        _service.disable_retries()
        self.test_get_instance_ruleset_version_all_params()

    @responses.activate
    def test_get_instance_ruleset_version_value_error(self):
        """
        test_get_instance_ruleset_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/testString/versions/1')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_id = 'testString'
        ruleset_version = '1'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "ruleset_id": ruleset_id,
            "ruleset_version": ruleset_version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_instance_ruleset_version(**req_copy)

    def test_get_instance_ruleset_version_value_error_with_retries(self):
        # Enable retries and run test_get_instance_ruleset_version_value_error.
        _service.enable_retries()
        self.test_get_instance_ruleset_version_value_error()

        # Disable retries and run test_get_instance_ruleset_version_value_error.
        _service.disable_retries()
        self.test_get_instance_ruleset_version_value_error()


class TestDeleteInstanceRulesetVersion:
    """
    Test Class for delete_instance_ruleset_version
    """

    @responses.activate
    def test_delete_instance_ruleset_version_all_params(self):
        """
        delete_instance_ruleset_version()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/testString/versions/1')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        ruleset_id = 'testString'
        ruleset_version = '1'

        # Invoke method
        response = _service.delete_instance_ruleset_version(
            ruleset_id,
            ruleset_version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_instance_ruleset_version_all_params_with_retries(self):
        # Enable retries and run test_delete_instance_ruleset_version_all_params.
        _service.enable_retries()
        self.test_delete_instance_ruleset_version_all_params()

        # Disable retries and run test_delete_instance_ruleset_version_all_params.
        _service.disable_retries()
        self.test_delete_instance_ruleset_version_all_params()

    @responses.activate
    def test_delete_instance_ruleset_version_value_error(self):
        """
        test_delete_instance_ruleset_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/testString/versions/1')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        ruleset_id = 'testString'
        ruleset_version = '1'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "ruleset_id": ruleset_id,
            "ruleset_version": ruleset_version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_instance_ruleset_version(**req_copy)

    def test_delete_instance_ruleset_version_value_error_with_retries(self):
        # Enable retries and run test_delete_instance_ruleset_version_value_error.
        _service.enable_retries()
        self.test_delete_instance_ruleset_version_value_error()

        # Disable retries and run test_delete_instance_ruleset_version_value_error.
        _service.disable_retries()
        self.test_delete_instance_ruleset_version_value_error()


class TestGetInstanceEntrypointRuleset:
    """
    Test Class for get_instance_entrypoint_ruleset
    """

    @responses.activate
    def test_get_instance_entrypoint_ruleset_all_params(self):
        """
        get_instance_entrypoint_ruleset()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/phases/ddos_l4/entrypoint')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_phase = 'ddos_l4'

        # Invoke method
        response = _service.get_instance_entrypoint_ruleset(
            ruleset_phase,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_instance_entrypoint_ruleset_all_params_with_retries(self):
        # Enable retries and run test_get_instance_entrypoint_ruleset_all_params.
        _service.enable_retries()
        self.test_get_instance_entrypoint_ruleset_all_params()

        # Disable retries and run test_get_instance_entrypoint_ruleset_all_params.
        _service.disable_retries()
        self.test_get_instance_entrypoint_ruleset_all_params()

    @responses.activate
    def test_get_instance_entrypoint_ruleset_value_error(self):
        """
        test_get_instance_entrypoint_ruleset_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/phases/ddos_l4/entrypoint')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_phase = 'ddos_l4'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "ruleset_phase": ruleset_phase,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_instance_entrypoint_ruleset(**req_copy)

    def test_get_instance_entrypoint_ruleset_value_error_with_retries(self):
        # Enable retries and run test_get_instance_entrypoint_ruleset_value_error.
        _service.enable_retries()
        self.test_get_instance_entrypoint_ruleset_value_error()

        # Disable retries and run test_get_instance_entrypoint_ruleset_value_error.
        _service.disable_retries()
        self.test_get_instance_entrypoint_ruleset_value_error()


class TestUpdateInstanceEntrypointRuleset:
    """
    Test Class for update_instance_entrypoint_ruleset
    """

    @responses.activate
    def test_update_instance_entrypoint_ruleset_all_params(self):
        """
        update_instance_entrypoint_ruleset()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/phases/ddos_l4/entrypoint')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a RulesOverride model
        rules_override_model = {}
        rules_override_model['id'] = 'testString'
        rules_override_model['enabled'] = True
        rules_override_model['action'] = 'testString'
        rules_override_model['sensitivity_level'] = 'high'
        rules_override_model['score_threshold'] = 60

        # Construct a dict representation of a CategoriesOverride model
        categories_override_model = {}
        categories_override_model['category'] = 'testString'
        categories_override_model['enabled'] = True
        categories_override_model['action'] = 'testString'

        # Construct a dict representation of a Overrides model
        overrides_model = {}
        overrides_model['action'] = 'testString'
        overrides_model['enabled'] = True
        overrides_model['sensitivity_level'] = 'high'
        overrides_model['rules'] = [rules_override_model]
        overrides_model['categories'] = [categories_override_model]

        # Construct a dict representation of a ActionParametersResponse model
        action_parameters_response_model = {}
        action_parameters_response_model['content'] = '{"success": false, "error": "you have been blocked"}'
        action_parameters_response_model['content_type'] = 'application/json'
        action_parameters_response_model['status_code'] = 400

        # Construct a dict representation of a ActionParameters model
        action_parameters_model = {}
        action_parameters_model['id'] = 'testString'
        action_parameters_model['overrides'] = overrides_model
        action_parameters_model['version'] = 'testString'
        action_parameters_model['ruleset'] = 'testString'
        action_parameters_model['rulesets'] = ['testString']
        action_parameters_model['phases'] = ['testString']
        action_parameters_model['products'] = ['testString']
        action_parameters_model['response'] = action_parameters_response_model

        # Construct a dict representation of a Ratelimit model
        ratelimit_model = {}
        ratelimit_model['characteristics'] = ['testString']
        ratelimit_model['counting_expression'] = 'testString'
        ratelimit_model['mitigation_timeout'] = 38
        ratelimit_model['period'] = 38
        ratelimit_model['requests_per_period'] = 38

        # Construct a dict representation of a Logging model
        logging_model = {}
        logging_model['enabled'] = True

        # Construct a dict representation of a Position model
        position_model = {}
        position_model['before'] = 'testString'
        position_model['after'] = 'testString'
        position_model['index'] = 0

        # Construct a dict representation of a RuleCreate model
        rule_create_model = {}
        rule_create_model['action'] = 'testString'
        rule_create_model['action_parameters'] = action_parameters_model
        rule_create_model['ratelimit'] = ratelimit_model
        rule_create_model['description'] = 'testString'
        rule_create_model['enabled'] = True
        rule_create_model['expression'] = 'ip.src ne 1.1.1.1'
        rule_create_model['id'] = 'testString'
        rule_create_model['logging'] = logging_model
        rule_create_model['ref'] = 'my_ref'
        rule_create_model['position'] = position_model

        # Set up parameter values
        ruleset_phase = 'ddos_l4'
        description = 'Custom instance ruleset'
        kind = 'managed'
        name = 'testString'
        phase = 'ddos_l4'
        rules = [rule_create_model]

        # Invoke method
        response = _service.update_instance_entrypoint_ruleset(
            ruleset_phase,
            description=description,
            kind=kind,
            name=name,
            phase=phase,
            rules=rules,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['description'] == 'Custom instance ruleset'
        assert req_body['kind'] == 'managed'
        assert req_body['name'] == 'testString'
        assert req_body['phase'] == 'ddos_l4'
        assert req_body['rules'] == [rule_create_model]

    def test_update_instance_entrypoint_ruleset_all_params_with_retries(self):
        # Enable retries and run test_update_instance_entrypoint_ruleset_all_params.
        _service.enable_retries()
        self.test_update_instance_entrypoint_ruleset_all_params()

        # Disable retries and run test_update_instance_entrypoint_ruleset_all_params.
        _service.disable_retries()
        self.test_update_instance_entrypoint_ruleset_all_params()

    @responses.activate
    def test_update_instance_entrypoint_ruleset_required_params(self):
        """
        test_update_instance_entrypoint_ruleset_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/phases/ddos_l4/entrypoint')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_phase = 'ddos_l4'

        # Invoke method
        response = _service.update_instance_entrypoint_ruleset(
            ruleset_phase,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_instance_entrypoint_ruleset_required_params_with_retries(self):
        # Enable retries and run test_update_instance_entrypoint_ruleset_required_params.
        _service.enable_retries()
        self.test_update_instance_entrypoint_ruleset_required_params()

        # Disable retries and run test_update_instance_entrypoint_ruleset_required_params.
        _service.disable_retries()
        self.test_update_instance_entrypoint_ruleset_required_params()

    @responses.activate
    def test_update_instance_entrypoint_ruleset_value_error(self):
        """
        test_update_instance_entrypoint_ruleset_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/phases/ddos_l4/entrypoint')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_phase = 'ddos_l4'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "ruleset_phase": ruleset_phase,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_instance_entrypoint_ruleset(**req_copy)

    def test_update_instance_entrypoint_ruleset_value_error_with_retries(self):
        # Enable retries and run test_update_instance_entrypoint_ruleset_value_error.
        _service.enable_retries()
        self.test_update_instance_entrypoint_ruleset_value_error()

        # Disable retries and run test_update_instance_entrypoint_ruleset_value_error.
        _service.disable_retries()
        self.test_update_instance_entrypoint_ruleset_value_error()


class TestGetInstanceEntryPointRulesetVersions:
    """
    Test Class for get_instance_entry_point_ruleset_versions
    """

    @responses.activate
    def test_get_instance_entry_point_ruleset_versions_all_params(self):
        """
        get_instance_entry_point_ruleset_versions()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/phases/ddos_l4/entrypoint/versions')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": [{"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_phase = 'ddos_l4'

        # Invoke method
        response = _service.get_instance_entry_point_ruleset_versions(
            ruleset_phase,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_instance_entry_point_ruleset_versions_all_params_with_retries(self):
        # Enable retries and run test_get_instance_entry_point_ruleset_versions_all_params.
        _service.enable_retries()
        self.test_get_instance_entry_point_ruleset_versions_all_params()

        # Disable retries and run test_get_instance_entry_point_ruleset_versions_all_params.
        _service.disable_retries()
        self.test_get_instance_entry_point_ruleset_versions_all_params()

    @responses.activate
    def test_get_instance_entry_point_ruleset_versions_value_error(self):
        """
        test_get_instance_entry_point_ruleset_versions_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/phases/ddos_l4/entrypoint/versions')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": [{"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_phase = 'ddos_l4'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "ruleset_phase": ruleset_phase,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_instance_entry_point_ruleset_versions(**req_copy)

    def test_get_instance_entry_point_ruleset_versions_value_error_with_retries(self):
        # Enable retries and run test_get_instance_entry_point_ruleset_versions_value_error.
        _service.enable_retries()
        self.test_get_instance_entry_point_ruleset_versions_value_error()

        # Disable retries and run test_get_instance_entry_point_ruleset_versions_value_error.
        _service.disable_retries()
        self.test_get_instance_entry_point_ruleset_versions_value_error()


class TestGetInstanceEntryPointRulesetVersion:
    """
    Test Class for get_instance_entry_point_ruleset_version
    """

    @responses.activate
    def test_get_instance_entry_point_ruleset_version_all_params(self):
        """
        get_instance_entry_point_ruleset_version()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/phases/ddos_l4/entrypoint/versions/1')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_phase = 'ddos_l4'
        ruleset_version = '1'

        # Invoke method
        response = _service.get_instance_entry_point_ruleset_version(
            ruleset_phase,
            ruleset_version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_instance_entry_point_ruleset_version_all_params_with_retries(self):
        # Enable retries and run test_get_instance_entry_point_ruleset_version_all_params.
        _service.enable_retries()
        self.test_get_instance_entry_point_ruleset_version_all_params()

        # Disable retries and run test_get_instance_entry_point_ruleset_version_all_params.
        _service.disable_retries()
        self.test_get_instance_entry_point_ruleset_version_all_params()

    @responses.activate
    def test_get_instance_entry_point_ruleset_version_value_error(self):
        """
        test_get_instance_entry_point_ruleset_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/phases/ddos_l4/entrypoint/versions/1')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_phase = 'ddos_l4'
        ruleset_version = '1'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "ruleset_phase": ruleset_phase,
            "ruleset_version": ruleset_version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_instance_entry_point_ruleset_version(**req_copy)

    def test_get_instance_entry_point_ruleset_version_value_error_with_retries(self):
        # Enable retries and run test_get_instance_entry_point_ruleset_version_value_error.
        _service.enable_retries()
        self.test_get_instance_entry_point_ruleset_version_value_error()

        # Disable retries and run test_get_instance_entry_point_ruleset_version_value_error.
        _service.disable_retries()
        self.test_get_instance_entry_point_ruleset_version_value_error()


class TestCreateInstanceRulesetRule:
    """
    Test Class for create_instance_ruleset_rule
    """

    @responses.activate
    def test_create_instance_ruleset_rule_all_params(self):
        """
        create_instance_ruleset_rule()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/testString/rules')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a RulesOverride model
        rules_override_model = {}
        rules_override_model['id'] = 'testString'
        rules_override_model['enabled'] = True
        rules_override_model['action'] = 'testString'
        rules_override_model['sensitivity_level'] = 'high'
        rules_override_model['score_threshold'] = 60

        # Construct a dict representation of a CategoriesOverride model
        categories_override_model = {}
        categories_override_model['category'] = 'testString'
        categories_override_model['enabled'] = True
        categories_override_model['action'] = 'testString'

        # Construct a dict representation of a Overrides model
        overrides_model = {}
        overrides_model['action'] = 'testString'
        overrides_model['enabled'] = True
        overrides_model['sensitivity_level'] = 'high'
        overrides_model['rules'] = [rules_override_model]
        overrides_model['categories'] = [categories_override_model]

        # Construct a dict representation of a ActionParametersResponse model
        action_parameters_response_model = {}
        action_parameters_response_model['content'] = '{"success": false, "error": "you have been blocked"}'
        action_parameters_response_model['content_type'] = 'application/json'
        action_parameters_response_model['status_code'] = 400

        # Construct a dict representation of a ActionParameters model
        action_parameters_model = {}
        action_parameters_model['id'] = 'testString'
        action_parameters_model['overrides'] = overrides_model
        action_parameters_model['version'] = 'testString'
        action_parameters_model['ruleset'] = 'testString'
        action_parameters_model['rulesets'] = ['testString']
        action_parameters_model['phases'] = ['testString']
        action_parameters_model['products'] = ['testString']
        action_parameters_model['response'] = action_parameters_response_model

        # Construct a dict representation of a Ratelimit model
        ratelimit_model = {}
        ratelimit_model['characteristics'] = ['testString']
        ratelimit_model['counting_expression'] = 'testString'
        ratelimit_model['mitigation_timeout'] = 38
        ratelimit_model['period'] = 38
        ratelimit_model['requests_per_period'] = 38

        # Construct a dict representation of a Logging model
        logging_model = {}
        logging_model['enabled'] = True

        # Construct a dict representation of a Position model
        position_model = {}
        position_model['before'] = 'testString'
        position_model['after'] = 'testString'
        position_model['index'] = 0

        # Set up parameter values
        ruleset_id = 'testString'
        action = 'testString'
        expression = 'ip.src ne 1.1.1.1'
        action_parameters = action_parameters_model
        ratelimit = ratelimit_model
        description = 'testString'
        enabled = True
        id = 'testString'
        logging = logging_model
        ref = 'my_ref'
        position = position_model

        # Invoke method
        response = _service.create_instance_ruleset_rule(
            ruleset_id,
            action=action,
            expression=expression,
            action_parameters=action_parameters,
            ratelimit=ratelimit,
            description=description,
            enabled=enabled,
            id=id,
            logging=logging,
            ref=ref,
            position=position,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['action'] == 'testString'
        assert req_body['expression'] == 'ip.src ne 1.1.1.1'
        assert req_body['action_parameters'] == action_parameters_model
        assert req_body['ratelimit'] == ratelimit_model
        assert req_body['description'] == 'testString'
        assert req_body['enabled'] == True
        assert req_body['id'] == 'testString'
        assert req_body['logging'] == logging_model
        assert req_body['ref'] == 'my_ref'
        assert req_body['position'] == position_model

    def test_create_instance_ruleset_rule_all_params_with_retries(self):
        # Enable retries and run test_create_instance_ruleset_rule_all_params.
        _service.enable_retries()
        self.test_create_instance_ruleset_rule_all_params()

        # Disable retries and run test_create_instance_ruleset_rule_all_params.
        _service.disable_retries()
        self.test_create_instance_ruleset_rule_all_params()

    @responses.activate
    def test_create_instance_ruleset_rule_required_params(self):
        """
        test_create_instance_ruleset_rule_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/testString/rules')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_id = 'testString'

        # Invoke method
        response = _service.create_instance_ruleset_rule(
            ruleset_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_instance_ruleset_rule_required_params_with_retries(self):
        # Enable retries and run test_create_instance_ruleset_rule_required_params.
        _service.enable_retries()
        self.test_create_instance_ruleset_rule_required_params()

        # Disable retries and run test_create_instance_ruleset_rule_required_params.
        _service.disable_retries()
        self.test_create_instance_ruleset_rule_required_params()

    @responses.activate
    def test_create_instance_ruleset_rule_value_error(self):
        """
        test_create_instance_ruleset_rule_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/testString/rules')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "ruleset_id": ruleset_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_instance_ruleset_rule(**req_copy)

    def test_create_instance_ruleset_rule_value_error_with_retries(self):
        # Enable retries and run test_create_instance_ruleset_rule_value_error.
        _service.enable_retries()
        self.test_create_instance_ruleset_rule_value_error()

        # Disable retries and run test_create_instance_ruleset_rule_value_error.
        _service.disable_retries()
        self.test_create_instance_ruleset_rule_value_error()


class TestUpdateInstanceRulesetRule:
    """
    Test Class for update_instance_ruleset_rule
    """

    @responses.activate
    def test_update_instance_ruleset_rule_all_params(self):
        """
        update_instance_ruleset_rule()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/testString/rules/testString')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a RulesOverride model
        rules_override_model = {}
        rules_override_model['id'] = 'testString'
        rules_override_model['enabled'] = True
        rules_override_model['action'] = 'testString'
        rules_override_model['sensitivity_level'] = 'high'
        rules_override_model['score_threshold'] = 60

        # Construct a dict representation of a CategoriesOverride model
        categories_override_model = {}
        categories_override_model['category'] = 'testString'
        categories_override_model['enabled'] = True
        categories_override_model['action'] = 'testString'

        # Construct a dict representation of a Overrides model
        overrides_model = {}
        overrides_model['action'] = 'testString'
        overrides_model['enabled'] = True
        overrides_model['sensitivity_level'] = 'high'
        overrides_model['rules'] = [rules_override_model]
        overrides_model['categories'] = [categories_override_model]

        # Construct a dict representation of a ActionParametersResponse model
        action_parameters_response_model = {}
        action_parameters_response_model['content'] = '{"success": false, "error": "you have been blocked"}'
        action_parameters_response_model['content_type'] = 'application/json'
        action_parameters_response_model['status_code'] = 400

        # Construct a dict representation of a ActionParameters model
        action_parameters_model = {}
        action_parameters_model['id'] = 'testString'
        action_parameters_model['overrides'] = overrides_model
        action_parameters_model['version'] = 'testString'
        action_parameters_model['ruleset'] = 'testString'
        action_parameters_model['rulesets'] = ['testString']
        action_parameters_model['phases'] = ['testString']
        action_parameters_model['products'] = ['testString']
        action_parameters_model['response'] = action_parameters_response_model

        # Construct a dict representation of a Ratelimit model
        ratelimit_model = {}
        ratelimit_model['characteristics'] = ['testString']
        ratelimit_model['counting_expression'] = 'testString'
        ratelimit_model['mitigation_timeout'] = 38
        ratelimit_model['period'] = 38
        ratelimit_model['requests_per_period'] = 38

        # Construct a dict representation of a Logging model
        logging_model = {}
        logging_model['enabled'] = True

        # Construct a dict representation of a Position model
        position_model = {}
        position_model['before'] = 'testString'
        position_model['after'] = 'testString'
        position_model['index'] = 0

        # Set up parameter values
        ruleset_id = 'testString'
        rule_id = 'testString'
        action = 'testString'
        action_parameters = action_parameters_model
        ratelimit = ratelimit_model
        description = 'testString'
        enabled = True
        expression = 'ip.src ne 1.1.1.1'
        id = 'testString'
        logging = logging_model
        ref = 'my_ref'
        position = position_model

        # Invoke method
        response = _service.update_instance_ruleset_rule(
            ruleset_id,
            rule_id,
            action=action,
            action_parameters=action_parameters,
            ratelimit=ratelimit,
            description=description,
            enabled=enabled,
            expression=expression,
            id=id,
            logging=logging,
            ref=ref,
            position=position,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['action'] == 'testString'
        assert req_body['action_parameters'] == action_parameters_model
        assert req_body['ratelimit'] == ratelimit_model
        assert req_body['description'] == 'testString'
        assert req_body['enabled'] == True
        assert req_body['expression'] == 'ip.src ne 1.1.1.1'
        assert req_body['id'] == 'testString'
        assert req_body['logging'] == logging_model
        assert req_body['ref'] == 'my_ref'
        assert req_body['position'] == position_model

    def test_update_instance_ruleset_rule_all_params_with_retries(self):
        # Enable retries and run test_update_instance_ruleset_rule_all_params.
        _service.enable_retries()
        self.test_update_instance_ruleset_rule_all_params()

        # Disable retries and run test_update_instance_ruleset_rule_all_params.
        _service.disable_retries()
        self.test_update_instance_ruleset_rule_all_params()

    @responses.activate
    def test_update_instance_ruleset_rule_required_params(self):
        """
        test_update_instance_ruleset_rule_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/testString/rules/testString')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_id = 'testString'
        rule_id = 'testString'

        # Invoke method
        response = _service.update_instance_ruleset_rule(
            ruleset_id,
            rule_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_instance_ruleset_rule_required_params_with_retries(self):
        # Enable retries and run test_update_instance_ruleset_rule_required_params.
        _service.enable_retries()
        self.test_update_instance_ruleset_rule_required_params()

        # Disable retries and run test_update_instance_ruleset_rule_required_params.
        _service.disable_retries()
        self.test_update_instance_ruleset_rule_required_params()

    @responses.activate
    def test_update_instance_ruleset_rule_value_error(self):
        """
        test_update_instance_ruleset_rule_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/testString/rules/testString')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_id = 'testString'
        rule_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "ruleset_id": ruleset_id,
            "rule_id": rule_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_instance_ruleset_rule(**req_copy)

    def test_update_instance_ruleset_rule_value_error_with_retries(self):
        # Enable retries and run test_update_instance_ruleset_rule_value_error.
        _service.enable_retries()
        self.test_update_instance_ruleset_rule_value_error()

        # Disable retries and run test_update_instance_ruleset_rule_value_error.
        _service.disable_retries()
        self.test_update_instance_ruleset_rule_value_error()


class TestDeleteInstanceRulesetRule:
    """
    Test Class for delete_instance_ruleset_rule
    """

    @responses.activate
    def test_delete_instance_ruleset_rule_all_params(self):
        """
        delete_instance_ruleset_rule()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/testString/rules/testString')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_id = 'testString'
        rule_id = 'testString'

        # Invoke method
        response = _service.delete_instance_ruleset_rule(
            ruleset_id,
            rule_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_instance_ruleset_rule_all_params_with_retries(self):
        # Enable retries and run test_delete_instance_ruleset_rule_all_params.
        _service.enable_retries()
        self.test_delete_instance_ruleset_rule_all_params()

        # Disable retries and run test_delete_instance_ruleset_rule_all_params.
        _service.disable_retries()
        self.test_delete_instance_ruleset_rule_all_params()

    @responses.activate
    def test_delete_instance_ruleset_rule_value_error(self):
        """
        test_delete_instance_ruleset_rule_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/testString/rules/testString')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_id = 'testString'
        rule_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "ruleset_id": ruleset_id,
            "rule_id": rule_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_instance_ruleset_rule(**req_copy)

    def test_delete_instance_ruleset_rule_value_error_with_retries(self):
        # Enable retries and run test_delete_instance_ruleset_rule_value_error.
        _service.enable_retries()
        self.test_delete_instance_ruleset_rule_value_error()

        # Disable retries and run test_delete_instance_ruleset_rule_value_error.
        _service.disable_retries()
        self.test_delete_instance_ruleset_rule_value_error()


class TestGetInstanceRulesetVersionByTag:
    """
    Test Class for get_instance_ruleset_version_by_tag
    """

    @responses.activate
    def test_get_instance_ruleset_version_by_tag_all_params(self):
        """
        get_instance_ruleset_version_by_tag()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/testString/versions/1/by_tag/testString')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_id = 'testString'
        ruleset_version = '1'
        rule_tag = 'testString'

        # Invoke method
        response = _service.get_instance_ruleset_version_by_tag(
            ruleset_id,
            ruleset_version,
            rule_tag,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_instance_ruleset_version_by_tag_all_params_with_retries(self):
        # Enable retries and run test_get_instance_ruleset_version_by_tag_all_params.
        _service.enable_retries()
        self.test_get_instance_ruleset_version_by_tag_all_params()

        # Disable retries and run test_get_instance_ruleset_version_by_tag_all_params.
        _service.disable_retries()
        self.test_get_instance_ruleset_version_by_tag_all_params()

    @responses.activate
    def test_get_instance_ruleset_version_by_tag_value_error(self):
        """
        test_get_instance_ruleset_version_by_tag_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rulesets/testString/versions/1/by_tag/testString')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_id = 'testString'
        ruleset_version = '1'
        rule_tag = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "ruleset_id": ruleset_id,
            "ruleset_version": ruleset_version,
            "rule_tag": rule_tag,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_instance_ruleset_version_by_tag(**req_copy)

    def test_get_instance_ruleset_version_by_tag_value_error_with_retries(self):
        # Enable retries and run test_get_instance_ruleset_version_by_tag_value_error.
        _service.enable_retries()
        self.test_get_instance_ruleset_version_by_tag_value_error()

        # Disable retries and run test_get_instance_ruleset_version_by_tag_value_error.
        _service.disable_retries()
        self.test_get_instance_ruleset_version_by_tag_value_error()


# endregion
##############################################################################
# End of Service: InstanceRulesets
##############################################################################

##############################################################################
# Start of Service: ZoneRulesets
##############################################################################
# region


class TestNewInstance:
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = RulesetsV1.new_instance(
            crn=crn,
            zone_identifier=zone_identifier,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, RulesetsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = RulesetsV1.new_instance(
                crn=crn,
                zone_identifier=zone_identifier,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = RulesetsV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='crn must be provided'):
            service = RulesetsV1.new_instance(
                crn=None,
                zone_identifier=None,
            )


class TestGetZoneRulesets:
    """
    Test Class for get_zone_rulesets
    """

    @responses.activate
    def test_get_zone_rulesets_all_params(self):
        """
        get_zone_rulesets()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": [{"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_zone_rulesets()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_zone_rulesets_all_params_with_retries(self):
        # Enable retries and run test_get_zone_rulesets_all_params.
        _service.enable_retries()
        self.test_get_zone_rulesets_all_params()

        # Disable retries and run test_get_zone_rulesets_all_params.
        _service.disable_retries()
        self.test_get_zone_rulesets_all_params()

    @responses.activate
    def test_get_zone_rulesets_value_error(self):
        """
        test_get_zone_rulesets_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": [{"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_zone_rulesets(**req_copy)

    def test_get_zone_rulesets_value_error_with_retries(self):
        # Enable retries and run test_get_zone_rulesets_value_error.
        _service.enable_retries()
        self.test_get_zone_rulesets_value_error()

        # Disable retries and run test_get_zone_rulesets_value_error.
        _service.disable_retries()
        self.test_get_zone_rulesets_value_error()


class TestGetZoneRuleset:
    """
    Test Class for get_zone_ruleset
    """

    @responses.activate
    def test_get_zone_ruleset_all_params(self):
        """
        get_zone_ruleset()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets/testString')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_id = 'testString'

        # Invoke method
        response = _service.get_zone_ruleset(
            ruleset_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_zone_ruleset_all_params_with_retries(self):
        # Enable retries and run test_get_zone_ruleset_all_params.
        _service.enable_retries()
        self.test_get_zone_ruleset_all_params()

        # Disable retries and run test_get_zone_ruleset_all_params.
        _service.disable_retries()
        self.test_get_zone_ruleset_all_params()

    @responses.activate
    def test_get_zone_ruleset_value_error(self):
        """
        test_get_zone_ruleset_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets/testString')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "ruleset_id": ruleset_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_zone_ruleset(**req_copy)

    def test_get_zone_ruleset_value_error_with_retries(self):
        # Enable retries and run test_get_zone_ruleset_value_error.
        _service.enable_retries()
        self.test_get_zone_ruleset_value_error()

        # Disable retries and run test_get_zone_ruleset_value_error.
        _service.disable_retries()
        self.test_get_zone_ruleset_value_error()


class TestUpdateZoneRuleset:
    """
    Test Class for update_zone_ruleset
    """

    @responses.activate
    def test_update_zone_ruleset_all_params(self):
        """
        update_zone_ruleset()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets/testString')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a RulesOverride model
        rules_override_model = {}
        rules_override_model['id'] = 'testString'
        rules_override_model['enabled'] = True
        rules_override_model['action'] = 'testString'
        rules_override_model['sensitivity_level'] = 'high'
        rules_override_model['score_threshold'] = 60

        # Construct a dict representation of a CategoriesOverride model
        categories_override_model = {}
        categories_override_model['category'] = 'testString'
        categories_override_model['enabled'] = True
        categories_override_model['action'] = 'testString'

        # Construct a dict representation of a Overrides model
        overrides_model = {}
        overrides_model['action'] = 'testString'
        overrides_model['enabled'] = True
        overrides_model['sensitivity_level'] = 'high'
        overrides_model['rules'] = [rules_override_model]
        overrides_model['categories'] = [categories_override_model]

        # Construct a dict representation of a ActionParametersResponse model
        action_parameters_response_model = {}
        action_parameters_response_model['content'] = '{"success": false, "error": "you have been blocked"}'
        action_parameters_response_model['content_type'] = 'application/json'
        action_parameters_response_model['status_code'] = 400

        # Construct a dict representation of a ActionParameters model
        action_parameters_model = {}
        action_parameters_model['id'] = 'testString'
        action_parameters_model['overrides'] = overrides_model
        action_parameters_model['version'] = 'testString'
        action_parameters_model['ruleset'] = 'testString'
        action_parameters_model['rulesets'] = ['testString']
        action_parameters_model['phases'] = ['testString']
        action_parameters_model['products'] = ['testString']
        action_parameters_model['response'] = action_parameters_response_model

        # Construct a dict representation of a Ratelimit model
        ratelimit_model = {}
        ratelimit_model['characteristics'] = ['testString']
        ratelimit_model['counting_expression'] = 'testString'
        ratelimit_model['mitigation_timeout'] = 38
        ratelimit_model['period'] = 38
        ratelimit_model['requests_per_period'] = 38

        # Construct a dict representation of a Logging model
        logging_model = {}
        logging_model['enabled'] = True

        # Construct a dict representation of a Position model
        position_model = {}
        position_model['before'] = 'testString'
        position_model['after'] = 'testString'
        position_model['index'] = 0

        # Construct a dict representation of a RuleCreate model
        rule_create_model = {}
        rule_create_model['action'] = 'testString'
        rule_create_model['action_parameters'] = action_parameters_model
        rule_create_model['ratelimit'] = ratelimit_model
        rule_create_model['description'] = 'testString'
        rule_create_model['enabled'] = True
        rule_create_model['expression'] = 'ip.src ne 1.1.1.1'
        rule_create_model['id'] = 'testString'
        rule_create_model['logging'] = logging_model
        rule_create_model['ref'] = 'my_ref'
        rule_create_model['position'] = position_model

        # Set up parameter values
        ruleset_id = 'testString'
        description = 'Custom instance ruleset'
        kind = 'managed'
        name = 'testString'
        phase = 'ddos_l4'
        rules = [rule_create_model]

        # Invoke method
        response = _service.update_zone_ruleset(
            ruleset_id,
            description=description,
            kind=kind,
            name=name,
            phase=phase,
            rules=rules,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['description'] == 'Custom instance ruleset'
        assert req_body['kind'] == 'managed'
        assert req_body['name'] == 'testString'
        assert req_body['phase'] == 'ddos_l4'
        assert req_body['rules'] == [rule_create_model]

    def test_update_zone_ruleset_all_params_with_retries(self):
        # Enable retries and run test_update_zone_ruleset_all_params.
        _service.enable_retries()
        self.test_update_zone_ruleset_all_params()

        # Disable retries and run test_update_zone_ruleset_all_params.
        _service.disable_retries()
        self.test_update_zone_ruleset_all_params()

    @responses.activate
    def test_update_zone_ruleset_required_params(self):
        """
        test_update_zone_ruleset_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets/testString')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_id = 'testString'

        # Invoke method
        response = _service.update_zone_ruleset(
            ruleset_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_zone_ruleset_required_params_with_retries(self):
        # Enable retries and run test_update_zone_ruleset_required_params.
        _service.enable_retries()
        self.test_update_zone_ruleset_required_params()

        # Disable retries and run test_update_zone_ruleset_required_params.
        _service.disable_retries()
        self.test_update_zone_ruleset_required_params()

    @responses.activate
    def test_update_zone_ruleset_value_error(self):
        """
        test_update_zone_ruleset_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets/testString')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "ruleset_id": ruleset_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_zone_ruleset(**req_copy)

    def test_update_zone_ruleset_value_error_with_retries(self):
        # Enable retries and run test_update_zone_ruleset_value_error.
        _service.enable_retries()
        self.test_update_zone_ruleset_value_error()

        # Disable retries and run test_update_zone_ruleset_value_error.
        _service.disable_retries()
        self.test_update_zone_ruleset_value_error()


class TestDeleteZoneRuleset:
    """
    Test Class for delete_zone_ruleset
    """

    @responses.activate
    def test_delete_zone_ruleset_all_params(self):
        """
        delete_zone_ruleset()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        ruleset_id = 'testString'

        # Invoke method
        response = _service.delete_zone_ruleset(
            ruleset_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_zone_ruleset_all_params_with_retries(self):
        # Enable retries and run test_delete_zone_ruleset_all_params.
        _service.enable_retries()
        self.test_delete_zone_ruleset_all_params()

        # Disable retries and run test_delete_zone_ruleset_all_params.
        _service.disable_retries()
        self.test_delete_zone_ruleset_all_params()

    @responses.activate
    def test_delete_zone_ruleset_value_error(self):
        """
        test_delete_zone_ruleset_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        ruleset_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "ruleset_id": ruleset_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_zone_ruleset(**req_copy)

    def test_delete_zone_ruleset_value_error_with_retries(self):
        # Enable retries and run test_delete_zone_ruleset_value_error.
        _service.enable_retries()
        self.test_delete_zone_ruleset_value_error()

        # Disable retries and run test_delete_zone_ruleset_value_error.
        _service.disable_retries()
        self.test_delete_zone_ruleset_value_error()


class TestGetZoneRulesetVersions:
    """
    Test Class for get_zone_ruleset_versions
    """

    @responses.activate
    def test_get_zone_ruleset_versions_all_params(self):
        """
        get_zone_ruleset_versions()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets/testString/versions')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": [{"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_id = 'testString'

        # Invoke method
        response = _service.get_zone_ruleset_versions(
            ruleset_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_zone_ruleset_versions_all_params_with_retries(self):
        # Enable retries and run test_get_zone_ruleset_versions_all_params.
        _service.enable_retries()
        self.test_get_zone_ruleset_versions_all_params()

        # Disable retries and run test_get_zone_ruleset_versions_all_params.
        _service.disable_retries()
        self.test_get_zone_ruleset_versions_all_params()

    @responses.activate
    def test_get_zone_ruleset_versions_value_error(self):
        """
        test_get_zone_ruleset_versions_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets/testString/versions')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": [{"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "ruleset_id": ruleset_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_zone_ruleset_versions(**req_copy)

    def test_get_zone_ruleset_versions_value_error_with_retries(self):
        # Enable retries and run test_get_zone_ruleset_versions_value_error.
        _service.enable_retries()
        self.test_get_zone_ruleset_versions_value_error()

        # Disable retries and run test_get_zone_ruleset_versions_value_error.
        _service.disable_retries()
        self.test_get_zone_ruleset_versions_value_error()


class TestGetZoneRulesetVersion:
    """
    Test Class for get_zone_ruleset_version
    """

    @responses.activate
    def test_get_zone_ruleset_version_all_params(self):
        """
        get_zone_ruleset_version()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets/testString/versions/1')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_id = 'testString'
        ruleset_version = '1'

        # Invoke method
        response = _service.get_zone_ruleset_version(
            ruleset_id,
            ruleset_version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_zone_ruleset_version_all_params_with_retries(self):
        # Enable retries and run test_get_zone_ruleset_version_all_params.
        _service.enable_retries()
        self.test_get_zone_ruleset_version_all_params()

        # Disable retries and run test_get_zone_ruleset_version_all_params.
        _service.disable_retries()
        self.test_get_zone_ruleset_version_all_params()

    @responses.activate
    def test_get_zone_ruleset_version_value_error(self):
        """
        test_get_zone_ruleset_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets/testString/versions/1')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_id = 'testString'
        ruleset_version = '1'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "ruleset_id": ruleset_id,
            "ruleset_version": ruleset_version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_zone_ruleset_version(**req_copy)

    def test_get_zone_ruleset_version_value_error_with_retries(self):
        # Enable retries and run test_get_zone_ruleset_version_value_error.
        _service.enable_retries()
        self.test_get_zone_ruleset_version_value_error()

        # Disable retries and run test_get_zone_ruleset_version_value_error.
        _service.disable_retries()
        self.test_get_zone_ruleset_version_value_error()


class TestDeleteZoneRulesetVersion:
    """
    Test Class for delete_zone_ruleset_version
    """

    @responses.activate
    def test_delete_zone_ruleset_version_all_params(self):
        """
        delete_zone_ruleset_version()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets/testString/versions/1')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        ruleset_id = 'testString'
        ruleset_version = '1'

        # Invoke method
        response = _service.delete_zone_ruleset_version(
            ruleset_id,
            ruleset_version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_zone_ruleset_version_all_params_with_retries(self):
        # Enable retries and run test_delete_zone_ruleset_version_all_params.
        _service.enable_retries()
        self.test_delete_zone_ruleset_version_all_params()

        # Disable retries and run test_delete_zone_ruleset_version_all_params.
        _service.disable_retries()
        self.test_delete_zone_ruleset_version_all_params()

    @responses.activate
    def test_delete_zone_ruleset_version_value_error(self):
        """
        test_delete_zone_ruleset_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets/testString/versions/1')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        ruleset_id = 'testString'
        ruleset_version = '1'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "ruleset_id": ruleset_id,
            "ruleset_version": ruleset_version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_zone_ruleset_version(**req_copy)

    def test_delete_zone_ruleset_version_value_error_with_retries(self):
        # Enable retries and run test_delete_zone_ruleset_version_value_error.
        _service.enable_retries()
        self.test_delete_zone_ruleset_version_value_error()

        # Disable retries and run test_delete_zone_ruleset_version_value_error.
        _service.disable_retries()
        self.test_delete_zone_ruleset_version_value_error()


class TestGetZoneEntrypointRuleset:
    """
    Test Class for get_zone_entrypoint_ruleset
    """

    @responses.activate
    def test_get_zone_entrypoint_ruleset_all_params(self):
        """
        get_zone_entrypoint_ruleset()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets/phases/ddos_l4/entrypoint')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_phase = 'ddos_l4'

        # Invoke method
        response = _service.get_zone_entrypoint_ruleset(
            ruleset_phase,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_zone_entrypoint_ruleset_all_params_with_retries(self):
        # Enable retries and run test_get_zone_entrypoint_ruleset_all_params.
        _service.enable_retries()
        self.test_get_zone_entrypoint_ruleset_all_params()

        # Disable retries and run test_get_zone_entrypoint_ruleset_all_params.
        _service.disable_retries()
        self.test_get_zone_entrypoint_ruleset_all_params()

    @responses.activate
    def test_get_zone_entrypoint_ruleset_value_error(self):
        """
        test_get_zone_entrypoint_ruleset_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets/phases/ddos_l4/entrypoint')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_phase = 'ddos_l4'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "ruleset_phase": ruleset_phase,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_zone_entrypoint_ruleset(**req_copy)

    def test_get_zone_entrypoint_ruleset_value_error_with_retries(self):
        # Enable retries and run test_get_zone_entrypoint_ruleset_value_error.
        _service.enable_retries()
        self.test_get_zone_entrypoint_ruleset_value_error()

        # Disable retries and run test_get_zone_entrypoint_ruleset_value_error.
        _service.disable_retries()
        self.test_get_zone_entrypoint_ruleset_value_error()


class TestUpdateZoneEntrypointRuleset:
    """
    Test Class for update_zone_entrypoint_ruleset
    """

    @responses.activate
    def test_update_zone_entrypoint_ruleset_all_params(self):
        """
        update_zone_entrypoint_ruleset()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets/phases/ddos_l4/entrypoint')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a RulesOverride model
        rules_override_model = {}
        rules_override_model['id'] = 'testString'
        rules_override_model['enabled'] = True
        rules_override_model['action'] = 'testString'
        rules_override_model['sensitivity_level'] = 'high'
        rules_override_model['score_threshold'] = 60

        # Construct a dict representation of a CategoriesOverride model
        categories_override_model = {}
        categories_override_model['category'] = 'testString'
        categories_override_model['enabled'] = True
        categories_override_model['action'] = 'testString'

        # Construct a dict representation of a Overrides model
        overrides_model = {}
        overrides_model['action'] = 'testString'
        overrides_model['enabled'] = True
        overrides_model['sensitivity_level'] = 'high'
        overrides_model['rules'] = [rules_override_model]
        overrides_model['categories'] = [categories_override_model]

        # Construct a dict representation of a ActionParametersResponse model
        action_parameters_response_model = {}
        action_parameters_response_model['content'] = '{"success": false, "error": "you have been blocked"}'
        action_parameters_response_model['content_type'] = 'application/json'
        action_parameters_response_model['status_code'] = 400

        # Construct a dict representation of a ActionParameters model
        action_parameters_model = {}
        action_parameters_model['id'] = 'testString'
        action_parameters_model['overrides'] = overrides_model
        action_parameters_model['version'] = 'testString'
        action_parameters_model['ruleset'] = 'testString'
        action_parameters_model['rulesets'] = ['testString']
        action_parameters_model['phases'] = ['testString']
        action_parameters_model['products'] = ['testString']
        action_parameters_model['response'] = action_parameters_response_model

        # Construct a dict representation of a Ratelimit model
        ratelimit_model = {}
        ratelimit_model['characteristics'] = ['testString']
        ratelimit_model['counting_expression'] = 'testString'
        ratelimit_model['mitigation_timeout'] = 38
        ratelimit_model['period'] = 38
        ratelimit_model['requests_per_period'] = 38

        # Construct a dict representation of a Logging model
        logging_model = {}
        logging_model['enabled'] = True

        # Construct a dict representation of a Position model
        position_model = {}
        position_model['before'] = 'testString'
        position_model['after'] = 'testString'
        position_model['index'] = 0

        # Construct a dict representation of a RuleCreate model
        rule_create_model = {}
        rule_create_model['action'] = 'testString'
        rule_create_model['action_parameters'] = action_parameters_model
        rule_create_model['ratelimit'] = ratelimit_model
        rule_create_model['description'] = 'testString'
        rule_create_model['enabled'] = True
        rule_create_model['expression'] = 'ip.src ne 1.1.1.1'
        rule_create_model['id'] = 'testString'
        rule_create_model['logging'] = logging_model
        rule_create_model['ref'] = 'my_ref'
        rule_create_model['position'] = position_model

        # Set up parameter values
        ruleset_phase = 'ddos_l4'
        description = 'Custom instance ruleset'
        kind = 'managed'
        name = 'testString'
        phase = 'ddos_l4'
        rules = [rule_create_model]

        # Invoke method
        response = _service.update_zone_entrypoint_ruleset(
            ruleset_phase,
            description=description,
            kind=kind,
            name=name,
            phase=phase,
            rules=rules,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['description'] == 'Custom instance ruleset'
        assert req_body['kind'] == 'managed'
        assert req_body['name'] == 'testString'
        assert req_body['phase'] == 'ddos_l4'
        assert req_body['rules'] == [rule_create_model]

    def test_update_zone_entrypoint_ruleset_all_params_with_retries(self):
        # Enable retries and run test_update_zone_entrypoint_ruleset_all_params.
        _service.enable_retries()
        self.test_update_zone_entrypoint_ruleset_all_params()

        # Disable retries and run test_update_zone_entrypoint_ruleset_all_params.
        _service.disable_retries()
        self.test_update_zone_entrypoint_ruleset_all_params()

    @responses.activate
    def test_update_zone_entrypoint_ruleset_required_params(self):
        """
        test_update_zone_entrypoint_ruleset_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets/phases/ddos_l4/entrypoint')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_phase = 'ddos_l4'

        # Invoke method
        response = _service.update_zone_entrypoint_ruleset(
            ruleset_phase,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_zone_entrypoint_ruleset_required_params_with_retries(self):
        # Enable retries and run test_update_zone_entrypoint_ruleset_required_params.
        _service.enable_retries()
        self.test_update_zone_entrypoint_ruleset_required_params()

        # Disable retries and run test_update_zone_entrypoint_ruleset_required_params.
        _service.disable_retries()
        self.test_update_zone_entrypoint_ruleset_required_params()

    @responses.activate
    def test_update_zone_entrypoint_ruleset_value_error(self):
        """
        test_update_zone_entrypoint_ruleset_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets/phases/ddos_l4/entrypoint')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_phase = 'ddos_l4'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "ruleset_phase": ruleset_phase,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_zone_entrypoint_ruleset(**req_copy)

    def test_update_zone_entrypoint_ruleset_value_error_with_retries(self):
        # Enable retries and run test_update_zone_entrypoint_ruleset_value_error.
        _service.enable_retries()
        self.test_update_zone_entrypoint_ruleset_value_error()

        # Disable retries and run test_update_zone_entrypoint_ruleset_value_error.
        _service.disable_retries()
        self.test_update_zone_entrypoint_ruleset_value_error()


class TestGetZoneEntryPointRulesetVersions:
    """
    Test Class for get_zone_entry_point_ruleset_versions
    """

    @responses.activate
    def test_get_zone_entry_point_ruleset_versions_all_params(self):
        """
        get_zone_entry_point_ruleset_versions()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets/phases/ddos_l4/entrypoint/versions')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": [{"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_phase = 'ddos_l4'

        # Invoke method
        response = _service.get_zone_entry_point_ruleset_versions(
            ruleset_phase,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_zone_entry_point_ruleset_versions_all_params_with_retries(self):
        # Enable retries and run test_get_zone_entry_point_ruleset_versions_all_params.
        _service.enable_retries()
        self.test_get_zone_entry_point_ruleset_versions_all_params()

        # Disable retries and run test_get_zone_entry_point_ruleset_versions_all_params.
        _service.disable_retries()
        self.test_get_zone_entry_point_ruleset_versions_all_params()

    @responses.activate
    def test_get_zone_entry_point_ruleset_versions_value_error(self):
        """
        test_get_zone_entry_point_ruleset_versions_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets/phases/ddos_l4/entrypoint/versions')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": [{"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_phase = 'ddos_l4'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "ruleset_phase": ruleset_phase,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_zone_entry_point_ruleset_versions(**req_copy)

    def test_get_zone_entry_point_ruleset_versions_value_error_with_retries(self):
        # Enable retries and run test_get_zone_entry_point_ruleset_versions_value_error.
        _service.enable_retries()
        self.test_get_zone_entry_point_ruleset_versions_value_error()

        # Disable retries and run test_get_zone_entry_point_ruleset_versions_value_error.
        _service.disable_retries()
        self.test_get_zone_entry_point_ruleset_versions_value_error()


class TestGetZoneEntryPointRulesetVersion:
    """
    Test Class for get_zone_entry_point_ruleset_version
    """

    @responses.activate
    def test_get_zone_entry_point_ruleset_version_all_params(self):
        """
        get_zone_entry_point_ruleset_version()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets/phases/ddos_l4/entrypoint/versions/1')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_phase = 'ddos_l4'
        ruleset_version = '1'

        # Invoke method
        response = _service.get_zone_entry_point_ruleset_version(
            ruleset_phase,
            ruleset_version,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_zone_entry_point_ruleset_version_all_params_with_retries(self):
        # Enable retries and run test_get_zone_entry_point_ruleset_version_all_params.
        _service.enable_retries()
        self.test_get_zone_entry_point_ruleset_version_all_params()

        # Disable retries and run test_get_zone_entry_point_ruleset_version_all_params.
        _service.disable_retries()
        self.test_get_zone_entry_point_ruleset_version_all_params()

    @responses.activate
    def test_get_zone_entry_point_ruleset_version_value_error(self):
        """
        test_get_zone_entry_point_ruleset_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets/phases/ddos_l4/entrypoint/versions/1')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_phase = 'ddos_l4'
        ruleset_version = '1'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "ruleset_phase": ruleset_phase,
            "ruleset_version": ruleset_version,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_zone_entry_point_ruleset_version(**req_copy)

    def test_get_zone_entry_point_ruleset_version_value_error_with_retries(self):
        # Enable retries and run test_get_zone_entry_point_ruleset_version_value_error.
        _service.enable_retries()
        self.test_get_zone_entry_point_ruleset_version_value_error()

        # Disable retries and run test_get_zone_entry_point_ruleset_version_value_error.
        _service.disable_retries()
        self.test_get_zone_entry_point_ruleset_version_value_error()


class TestCreateZoneRulesetRule:
    """
    Test Class for create_zone_ruleset_rule
    """

    @responses.activate
    def test_create_zone_ruleset_rule_all_params(self):
        """
        create_zone_ruleset_rule()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets/testString/rules')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a RulesOverride model
        rules_override_model = {}
        rules_override_model['id'] = 'testString'
        rules_override_model['enabled'] = True
        rules_override_model['action'] = 'testString'
        rules_override_model['sensitivity_level'] = 'high'
        rules_override_model['score_threshold'] = 60

        # Construct a dict representation of a CategoriesOverride model
        categories_override_model = {}
        categories_override_model['category'] = 'testString'
        categories_override_model['enabled'] = True
        categories_override_model['action'] = 'testString'

        # Construct a dict representation of a Overrides model
        overrides_model = {}
        overrides_model['action'] = 'testString'
        overrides_model['enabled'] = True
        overrides_model['sensitivity_level'] = 'high'
        overrides_model['rules'] = [rules_override_model]
        overrides_model['categories'] = [categories_override_model]

        # Construct a dict representation of a ActionParametersResponse model
        action_parameters_response_model = {}
        action_parameters_response_model['content'] = '{"success": false, "error": "you have been blocked"}'
        action_parameters_response_model['content_type'] = 'application/json'
        action_parameters_response_model['status_code'] = 400

        # Construct a dict representation of a ActionParameters model
        action_parameters_model = {}
        action_parameters_model['id'] = 'testString'
        action_parameters_model['overrides'] = overrides_model
        action_parameters_model['version'] = 'testString'
        action_parameters_model['ruleset'] = 'testString'
        action_parameters_model['rulesets'] = ['testString']
        action_parameters_model['phases'] = ['testString']
        action_parameters_model['products'] = ['testString']
        action_parameters_model['response'] = action_parameters_response_model

        # Construct a dict representation of a Ratelimit model
        ratelimit_model = {}
        ratelimit_model['characteristics'] = ['testString']
        ratelimit_model['counting_expression'] = 'testString'
        ratelimit_model['mitigation_timeout'] = 38
        ratelimit_model['period'] = 38
        ratelimit_model['requests_per_period'] = 38

        # Construct a dict representation of a Logging model
        logging_model = {}
        logging_model['enabled'] = True

        # Construct a dict representation of a Position model
        position_model = {}
        position_model['before'] = 'testString'
        position_model['after'] = 'testString'
        position_model['index'] = 0

        # Set up parameter values
        ruleset_id = 'testString'
        action = 'testString'
        expression = 'ip.src ne 1.1.1.1'
        action_parameters = action_parameters_model
        ratelimit = ratelimit_model
        description = 'testString'
        enabled = True
        id = 'testString'
        logging = logging_model
        ref = 'my_ref'
        position = position_model

        # Invoke method
        response = _service.create_zone_ruleset_rule(
            ruleset_id,
            action=action,
            expression=expression,
            action_parameters=action_parameters,
            ratelimit=ratelimit,
            description=description,
            enabled=enabled,
            id=id,
            logging=logging,
            ref=ref,
            position=position,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['action'] == 'testString'
        assert req_body['expression'] == 'ip.src ne 1.1.1.1'
        assert req_body['action_parameters'] == action_parameters_model
        assert req_body['ratelimit'] == ratelimit_model
        assert req_body['description'] == 'testString'
        assert req_body['enabled'] == True
        assert req_body['id'] == 'testString'
        assert req_body['logging'] == logging_model
        assert req_body['ref'] == 'my_ref'
        assert req_body['position'] == position_model

    def test_create_zone_ruleset_rule_all_params_with_retries(self):
        # Enable retries and run test_create_zone_ruleset_rule_all_params.
        _service.enable_retries()
        self.test_create_zone_ruleset_rule_all_params()

        # Disable retries and run test_create_zone_ruleset_rule_all_params.
        _service.disable_retries()
        self.test_create_zone_ruleset_rule_all_params()

    @responses.activate
    def test_create_zone_ruleset_rule_required_params(self):
        """
        test_create_zone_ruleset_rule_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets/testString/rules')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_id = 'testString'

        # Invoke method
        response = _service.create_zone_ruleset_rule(
            ruleset_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_zone_ruleset_rule_required_params_with_retries(self):
        # Enable retries and run test_create_zone_ruleset_rule_required_params.
        _service.enable_retries()
        self.test_create_zone_ruleset_rule_required_params()

        # Disable retries and run test_create_zone_ruleset_rule_required_params.
        _service.disable_retries()
        self.test_create_zone_ruleset_rule_required_params()

    @responses.activate
    def test_create_zone_ruleset_rule_value_error(self):
        """
        test_create_zone_ruleset_rule_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets/testString/rules')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "ruleset_id": ruleset_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_zone_ruleset_rule(**req_copy)

    def test_create_zone_ruleset_rule_value_error_with_retries(self):
        # Enable retries and run test_create_zone_ruleset_rule_value_error.
        _service.enable_retries()
        self.test_create_zone_ruleset_rule_value_error()

        # Disable retries and run test_create_zone_ruleset_rule_value_error.
        _service.disable_retries()
        self.test_create_zone_ruleset_rule_value_error()


class TestUpdateZoneRulesetRule:
    """
    Test Class for update_zone_ruleset_rule
    """

    @responses.activate
    def test_update_zone_ruleset_rule_all_params(self):
        """
        update_zone_ruleset_rule()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets/testString/rules/testString')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a RulesOverride model
        rules_override_model = {}
        rules_override_model['id'] = 'testString'
        rules_override_model['enabled'] = True
        rules_override_model['action'] = 'testString'
        rules_override_model['sensitivity_level'] = 'high'
        rules_override_model['score_threshold'] = 60

        # Construct a dict representation of a CategoriesOverride model
        categories_override_model = {}
        categories_override_model['category'] = 'testString'
        categories_override_model['enabled'] = True
        categories_override_model['action'] = 'testString'

        # Construct a dict representation of a Overrides model
        overrides_model = {}
        overrides_model['action'] = 'testString'
        overrides_model['enabled'] = True
        overrides_model['sensitivity_level'] = 'high'
        overrides_model['rules'] = [rules_override_model]
        overrides_model['categories'] = [categories_override_model]

        # Construct a dict representation of a ActionParametersResponse model
        action_parameters_response_model = {}
        action_parameters_response_model['content'] = '{"success": false, "error": "you have been blocked"}'
        action_parameters_response_model['content_type'] = 'application/json'
        action_parameters_response_model['status_code'] = 400

        # Construct a dict representation of a ActionParameters model
        action_parameters_model = {}
        action_parameters_model['id'] = 'testString'
        action_parameters_model['overrides'] = overrides_model
        action_parameters_model['version'] = 'testString'
        action_parameters_model['ruleset'] = 'testString'
        action_parameters_model['rulesets'] = ['testString']
        action_parameters_model['phases'] = ['testString']
        action_parameters_model['products'] = ['testString']
        action_parameters_model['response'] = action_parameters_response_model

        # Construct a dict representation of a Ratelimit model
        ratelimit_model = {}
        ratelimit_model['characteristics'] = ['testString']
        ratelimit_model['counting_expression'] = 'testString'
        ratelimit_model['mitigation_timeout'] = 38
        ratelimit_model['period'] = 38
        ratelimit_model['requests_per_period'] = 38

        # Construct a dict representation of a Logging model
        logging_model = {}
        logging_model['enabled'] = True

        # Construct a dict representation of a Position model
        position_model = {}
        position_model['before'] = 'testString'
        position_model['after'] = 'testString'
        position_model['index'] = 0

        # Set up parameter values
        ruleset_id = 'testString'
        rule_id = 'testString'
        action = 'testString'
        action_parameters = action_parameters_model
        ratelimit = ratelimit_model
        description = 'testString'
        enabled = True
        expression = 'ip.src ne 1.1.1.1'
        id = 'testString'
        logging = logging_model
        ref = 'my_ref'
        position = position_model

        # Invoke method
        response = _service.update_zone_ruleset_rule(
            ruleset_id,
            rule_id,
            action=action,
            action_parameters=action_parameters,
            ratelimit=ratelimit,
            description=description,
            enabled=enabled,
            expression=expression,
            id=id,
            logging=logging,
            ref=ref,
            position=position,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['action'] == 'testString'
        assert req_body['action_parameters'] == action_parameters_model
        assert req_body['ratelimit'] == ratelimit_model
        assert req_body['description'] == 'testString'
        assert req_body['enabled'] == True
        assert req_body['expression'] == 'ip.src ne 1.1.1.1'
        assert req_body['id'] == 'testString'
        assert req_body['logging'] == logging_model
        assert req_body['ref'] == 'my_ref'
        assert req_body['position'] == position_model

    def test_update_zone_ruleset_rule_all_params_with_retries(self):
        # Enable retries and run test_update_zone_ruleset_rule_all_params.
        _service.enable_retries()
        self.test_update_zone_ruleset_rule_all_params()

        # Disable retries and run test_update_zone_ruleset_rule_all_params.
        _service.disable_retries()
        self.test_update_zone_ruleset_rule_all_params()

    @responses.activate
    def test_update_zone_ruleset_rule_required_params(self):
        """
        test_update_zone_ruleset_rule_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets/testString/rules/testString')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_id = 'testString'
        rule_id = 'testString'

        # Invoke method
        response = _service.update_zone_ruleset_rule(
            ruleset_id,
            rule_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_zone_ruleset_rule_required_params_with_retries(self):
        # Enable retries and run test_update_zone_ruleset_rule_required_params.
        _service.enable_retries()
        self.test_update_zone_ruleset_rule_required_params()

        # Disable retries and run test_update_zone_ruleset_rule_required_params.
        _service.disable_retries()
        self.test_update_zone_ruleset_rule_required_params()

    @responses.activate
    def test_update_zone_ruleset_rule_value_error(self):
        """
        test_update_zone_ruleset_rule_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets/testString/rules/testString')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"description": "Custom instance ruleset", "id": "id", "kind": "managed", "last_updated": "2000-01-01T00:00:00.000000Z", "name": "name", "phase": "ddos_l4", "version": "1", "rules": [{"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}]}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_id = 'testString'
        rule_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "ruleset_id": ruleset_id,
            "rule_id": rule_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_zone_ruleset_rule(**req_copy)

    def test_update_zone_ruleset_rule_value_error_with_retries(self):
        # Enable retries and run test_update_zone_ruleset_rule_value_error.
        _service.enable_retries()
        self.test_update_zone_ruleset_rule_value_error()

        # Disable retries and run test_update_zone_ruleset_rule_value_error.
        _service.disable_retries()
        self.test_update_zone_ruleset_rule_value_error()


class TestDeleteZoneRulesetRule:
    """
    Test Class for delete_zone_ruleset_rule
    """

    @responses.activate
    def test_delete_zone_ruleset_rule_all_params(self):
        """
        delete_zone_ruleset_rule()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets/testString/rules/testString')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_id = 'testString'
        rule_id = 'testString'

        # Invoke method
        response = _service.delete_zone_ruleset_rule(
            ruleset_id,
            rule_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_zone_ruleset_rule_all_params_with_retries(self):
        # Enable retries and run test_delete_zone_ruleset_rule_all_params.
        _service.enable_retries()
        self.test_delete_zone_ruleset_rule_all_params()

        # Disable retries and run test_delete_zone_ruleset_rule_all_params.
        _service.disable_retries()
        self.test_delete_zone_ruleset_rule_all_params()

    @responses.activate
    def test_delete_zone_ruleset_rule_value_error(self):
        """
        test_delete_zone_ruleset_rule_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/rulesets/testString/rules/testString')
        mock_response = '{"success": true, "errors": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "messages": [{"code": 10000, "message": "something failed in the request", "source": {"pointer": "/rules/0/action"}}], "result": {"id": "id", "version": "version", "action": "action", "action_parameters": {"id": "id", "overrides": {"action": "action", "enabled": false, "sensitivity_level": "high", "rules": [{"id": "id", "enabled": false, "action": "action", "sensitivity_level": "high", "score_threshold": 60}], "categories": [{"category": "category", "enabled": false, "action": "action"}]}, "version": "version", "ruleset": "ruleset", "rulesets": ["rulesets"], "phases": ["phases"], "products": ["products"], "response": {"content": "{\\"success\\": false, \\"error\\": \\"you have been blocked\\"}", "content_type": "application/json", "status_code": 400}}, "categories": ["categories"], "enabled": true, "description": "description", "expression": "ip.src ne 1.1.1.1", "ref": "my_ref", "logging": {"enabled": true}, "last_updated": "2000-01-01T00:00:00.000000Z"}}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        ruleset_id = 'testString'
        rule_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "ruleset_id": ruleset_id,
            "rule_id": rule_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_zone_ruleset_rule(**req_copy)

    def test_delete_zone_ruleset_rule_value_error_with_retries(self):
        # Enable retries and run test_delete_zone_ruleset_rule_value_error.
        _service.enable_retries()
        self.test_delete_zone_ruleset_rule_value_error()

        # Disable retries and run test_delete_zone_ruleset_rule_value_error.
        _service.disable_retries()
        self.test_delete_zone_ruleset_rule_value_error()


# endregion
##############################################################################
# End of Service: ZoneRulesets
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_ActionParametersResponse:
    """
    Test Class for ActionParametersResponse
    """

    def test_action_parameters_response_serialization(self):
        """
        Test serialization/deserialization for ActionParametersResponse
        """

        # Construct a json representation of a ActionParametersResponse model
        action_parameters_response_model_json = {}
        action_parameters_response_model_json['content'] = '{"success": false, "error": "you have been blocked"}'
        action_parameters_response_model_json['content_type'] = 'application/json'
        action_parameters_response_model_json['status_code'] = 400

        # Construct a model instance of ActionParametersResponse by calling from_dict on the json representation
        action_parameters_response_model = ActionParametersResponse.from_dict(action_parameters_response_model_json)
        assert action_parameters_response_model != False

        # Construct a model instance of ActionParametersResponse by calling from_dict on the json representation
        action_parameters_response_model_dict = ActionParametersResponse.from_dict(action_parameters_response_model_json).__dict__
        action_parameters_response_model2 = ActionParametersResponse(**action_parameters_response_model_dict)

        # Verify the model instances are equivalent
        assert action_parameters_response_model == action_parameters_response_model2

        # Convert model instance back to dict and verify no loss of data
        action_parameters_response_model_json2 = action_parameters_response_model.to_dict()
        assert action_parameters_response_model_json2 == action_parameters_response_model_json


class TestModel_MessageSource:
    """
    Test Class for MessageSource
    """

    def test_message_source_serialization(self):
        """
        Test serialization/deserialization for MessageSource
        """

        # Construct a json representation of a MessageSource model
        message_source_model_json = {}
        message_source_model_json['pointer'] = '/rules/0/action'

        # Construct a model instance of MessageSource by calling from_dict on the json representation
        message_source_model = MessageSource.from_dict(message_source_model_json)
        assert message_source_model != False

        # Construct a model instance of MessageSource by calling from_dict on the json representation
        message_source_model_dict = MessageSource.from_dict(message_source_model_json).__dict__
        message_source_model2 = MessageSource(**message_source_model_dict)

        # Verify the model instances are equivalent
        assert message_source_model == message_source_model2

        # Convert model instance back to dict and verify no loss of data
        message_source_model_json2 = message_source_model.to_dict()
        assert message_source_model_json2 == message_source_model_json


class TestModel_ActionParameters:
    """
    Test Class for ActionParameters
    """

    def test_action_parameters_serialization(self):
        """
        Test serialization/deserialization for ActionParameters
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rules_override_model = {}  # RulesOverride
        rules_override_model['id'] = 'testString'
        rules_override_model['enabled'] = True
        rules_override_model['action'] = 'testString'
        rules_override_model['sensitivity_level'] = 'high'
        rules_override_model['score_threshold'] = 60

        categories_override_model = {}  # CategoriesOverride
        categories_override_model['category'] = 'testString'
        categories_override_model['enabled'] = True
        categories_override_model['action'] = 'testString'

        overrides_model = {}  # Overrides
        overrides_model['action'] = 'testString'
        overrides_model['enabled'] = True
        overrides_model['sensitivity_level'] = 'high'
        overrides_model['rules'] = [rules_override_model]
        overrides_model['categories'] = [categories_override_model]

        action_parameters_response_model = {}  # ActionParametersResponse
        action_parameters_response_model['content'] = '{"success": false, "error": "you have been blocked"}'
        action_parameters_response_model['content_type'] = 'application/json'
        action_parameters_response_model['status_code'] = 400

        # Construct a json representation of a ActionParameters model
        action_parameters_model_json = {}
        action_parameters_model_json['id'] = 'testString'
        action_parameters_model_json['overrides'] = overrides_model
        action_parameters_model_json['version'] = 'testString'
        action_parameters_model_json['ruleset'] = 'testString'
        action_parameters_model_json['rulesets'] = ['testString']
        action_parameters_model_json['phases'] = ['testString']
        action_parameters_model_json['products'] = ['testString']
        action_parameters_model_json['response'] = action_parameters_response_model

        # Construct a model instance of ActionParameters by calling from_dict on the json representation
        action_parameters_model = ActionParameters.from_dict(action_parameters_model_json)
        assert action_parameters_model != False

        # Construct a model instance of ActionParameters by calling from_dict on the json representation
        action_parameters_model_dict = ActionParameters.from_dict(action_parameters_model_json).__dict__
        action_parameters_model2 = ActionParameters(**action_parameters_model_dict)

        # Verify the model instances are equivalent
        assert action_parameters_model == action_parameters_model2

        # Convert model instance back to dict and verify no loss of data
        action_parameters_model_json2 = action_parameters_model.to_dict()
        assert action_parameters_model_json2 == action_parameters_model_json


class TestModel_CategoriesOverride:
    """
    Test Class for CategoriesOverride
    """

    def test_categories_override_serialization(self):
        """
        Test serialization/deserialization for CategoriesOverride
        """

        # Construct a json representation of a CategoriesOverride model
        categories_override_model_json = {}
        categories_override_model_json['category'] = 'testString'
        categories_override_model_json['enabled'] = True
        categories_override_model_json['action'] = 'testString'

        # Construct a model instance of CategoriesOverride by calling from_dict on the json representation
        categories_override_model = CategoriesOverride.from_dict(categories_override_model_json)
        assert categories_override_model != False

        # Construct a model instance of CategoriesOverride by calling from_dict on the json representation
        categories_override_model_dict = CategoriesOverride.from_dict(categories_override_model_json).__dict__
        categories_override_model2 = CategoriesOverride(**categories_override_model_dict)

        # Verify the model instances are equivalent
        assert categories_override_model == categories_override_model2

        # Convert model instance back to dict and verify no loss of data
        categories_override_model_json2 = categories_override_model.to_dict()
        assert categories_override_model_json2 == categories_override_model_json


class TestModel_ListRulesetsResp:
    """
    Test Class for ListRulesetsResp
    """

    def test_list_rulesets_resp_serialization(self):
        """
        Test serialization/deserialization for ListRulesetsResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        message_source_model = {}  # MessageSource
        message_source_model['pointer'] = '/rules/0/action'

        message_model = {}  # Message
        message_model['code'] = 10000
        message_model['message'] = 'something failed in the request'
        message_model['source'] = message_source_model

        listed_ruleset_model = {}  # ListedRuleset
        listed_ruleset_model['description'] = 'Custom instance ruleset'
        listed_ruleset_model['id'] = 'testString'
        listed_ruleset_model['kind'] = 'managed'
        listed_ruleset_model['last_updated'] = '2000-01-01T00:00:00.000000Z'
        listed_ruleset_model['name'] = 'testString'
        listed_ruleset_model['phase'] = 'ddos_l4'
        listed_ruleset_model['version'] = '1'

        # Construct a json representation of a ListRulesetsResp model
        list_rulesets_resp_model_json = {}
        list_rulesets_resp_model_json['success'] = True
        list_rulesets_resp_model_json['errors'] = [message_model]
        list_rulesets_resp_model_json['messages'] = [message_model]
        list_rulesets_resp_model_json['result'] = [listed_ruleset_model]

        # Construct a model instance of ListRulesetsResp by calling from_dict on the json representation
        list_rulesets_resp_model = ListRulesetsResp.from_dict(list_rulesets_resp_model_json)
        assert list_rulesets_resp_model != False

        # Construct a model instance of ListRulesetsResp by calling from_dict on the json representation
        list_rulesets_resp_model_dict = ListRulesetsResp.from_dict(list_rulesets_resp_model_json).__dict__
        list_rulesets_resp_model2 = ListRulesetsResp(**list_rulesets_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_rulesets_resp_model == list_rulesets_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_rulesets_resp_model_json2 = list_rulesets_resp_model.to_dict()
        assert list_rulesets_resp_model_json2 == list_rulesets_resp_model_json


class TestModel_ListedRuleset:
    """
    Test Class for ListedRuleset
    """

    def test_listed_ruleset_serialization(self):
        """
        Test serialization/deserialization for ListedRuleset
        """

        # Construct a json representation of a ListedRuleset model
        listed_ruleset_model_json = {}
        listed_ruleset_model_json['description'] = 'Custom instance ruleset'
        listed_ruleset_model_json['id'] = 'testString'
        listed_ruleset_model_json['kind'] = 'managed'
        listed_ruleset_model_json['last_updated'] = '2000-01-01T00:00:00.000000Z'
        listed_ruleset_model_json['name'] = 'testString'
        listed_ruleset_model_json['phase'] = 'ddos_l4'
        listed_ruleset_model_json['version'] = '1'

        # Construct a model instance of ListedRuleset by calling from_dict on the json representation
        listed_ruleset_model = ListedRuleset.from_dict(listed_ruleset_model_json)
        assert listed_ruleset_model != False

        # Construct a model instance of ListedRuleset by calling from_dict on the json representation
        listed_ruleset_model_dict = ListedRuleset.from_dict(listed_ruleset_model_json).__dict__
        listed_ruleset_model2 = ListedRuleset(**listed_ruleset_model_dict)

        # Verify the model instances are equivalent
        assert listed_ruleset_model == listed_ruleset_model2

        # Convert model instance back to dict and verify no loss of data
        listed_ruleset_model_json2 = listed_ruleset_model.to_dict()
        assert listed_ruleset_model_json2 == listed_ruleset_model_json


class TestModel_Logging:
    """
    Test Class for Logging
    """

    def test_logging_serialization(self):
        """
        Test serialization/deserialization for Logging
        """

        # Construct a json representation of a Logging model
        logging_model_json = {}
        logging_model_json['enabled'] = True

        # Construct a model instance of Logging by calling from_dict on the json representation
        logging_model = Logging.from_dict(logging_model_json)
        assert logging_model != False

        # Construct a model instance of Logging by calling from_dict on the json representation
        logging_model_dict = Logging.from_dict(logging_model_json).__dict__
        logging_model2 = Logging(**logging_model_dict)

        # Verify the model instances are equivalent
        assert logging_model == logging_model2

        # Convert model instance back to dict and verify no loss of data
        logging_model_json2 = logging_model.to_dict()
        assert logging_model_json2 == logging_model_json


class TestModel_Message:
    """
    Test Class for Message
    """

    def test_message_serialization(self):
        """
        Test serialization/deserialization for Message
        """

        # Construct dict forms of any model objects needed in order to build this model.

        message_source_model = {}  # MessageSource
        message_source_model['pointer'] = '/rules/0/action'

        # Construct a json representation of a Message model
        message_model_json = {}
        message_model_json['code'] = 10000
        message_model_json['message'] = 'something failed in the request'
        message_model_json['source'] = message_source_model

        # Construct a model instance of Message by calling from_dict on the json representation
        message_model = Message.from_dict(message_model_json)
        assert message_model != False

        # Construct a model instance of Message by calling from_dict on the json representation
        message_model_dict = Message.from_dict(message_model_json).__dict__
        message_model2 = Message(**message_model_dict)

        # Verify the model instances are equivalent
        assert message_model == message_model2

        # Convert model instance back to dict and verify no loss of data
        message_model_json2 = message_model.to_dict()
        assert message_model_json2 == message_model_json


class TestModel_Overrides:
    """
    Test Class for Overrides
    """

    def test_overrides_serialization(self):
        """
        Test serialization/deserialization for Overrides
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rules_override_model = {}  # RulesOverride
        rules_override_model['id'] = 'testString'
        rules_override_model['enabled'] = True
        rules_override_model['action'] = 'testString'
        rules_override_model['sensitivity_level'] = 'high'
        rules_override_model['score_threshold'] = 60

        categories_override_model = {}  # CategoriesOverride
        categories_override_model['category'] = 'testString'
        categories_override_model['enabled'] = True
        categories_override_model['action'] = 'testString'

        # Construct a json representation of a Overrides model
        overrides_model_json = {}
        overrides_model_json['action'] = 'testString'
        overrides_model_json['enabled'] = True
        overrides_model_json['sensitivity_level'] = 'high'
        overrides_model_json['rules'] = [rules_override_model]
        overrides_model_json['categories'] = [categories_override_model]

        # Construct a model instance of Overrides by calling from_dict on the json representation
        overrides_model = Overrides.from_dict(overrides_model_json)
        assert overrides_model != False

        # Construct a model instance of Overrides by calling from_dict on the json representation
        overrides_model_dict = Overrides.from_dict(overrides_model_json).__dict__
        overrides_model2 = Overrides(**overrides_model_dict)

        # Verify the model instances are equivalent
        assert overrides_model == overrides_model2

        # Convert model instance back to dict and verify no loss of data
        overrides_model_json2 = overrides_model.to_dict()
        assert overrides_model_json2 == overrides_model_json


class TestModel_Position:
    """
    Test Class for Position
    """

    def test_position_serialization(self):
        """
        Test serialization/deserialization for Position
        """

        # Construct a json representation of a Position model
        position_model_json = {}
        position_model_json['before'] = 'testString'
        position_model_json['after'] = 'testString'
        position_model_json['index'] = 0

        # Construct a model instance of Position by calling from_dict on the json representation
        position_model = Position.from_dict(position_model_json)
        assert position_model != False

        # Construct a model instance of Position by calling from_dict on the json representation
        position_model_dict = Position.from_dict(position_model_json).__dict__
        position_model2 = Position(**position_model_dict)

        # Verify the model instances are equivalent
        assert position_model == position_model2

        # Convert model instance back to dict and verify no loss of data
        position_model_json2 = position_model.to_dict()
        assert position_model_json2 == position_model_json


class TestModel_Ratelimit:
    """
    Test Class for Ratelimit
    """

    def test_ratelimit_serialization(self):
        """
        Test serialization/deserialization for Ratelimit
        """

        # Construct a json representation of a Ratelimit model
        ratelimit_model_json = {}
        ratelimit_model_json['characteristics'] = ['testString']
        ratelimit_model_json['counting_expression'] = 'testString'
        ratelimit_model_json['mitigation_timeout'] = 38
        ratelimit_model_json['period'] = 38
        ratelimit_model_json['requests_per_period'] = 38

        # Construct a model instance of Ratelimit by calling from_dict on the json representation
        ratelimit_model = Ratelimit.from_dict(ratelimit_model_json)
        assert ratelimit_model != False

        # Construct a model instance of Ratelimit by calling from_dict on the json representation
        ratelimit_model_dict = Ratelimit.from_dict(ratelimit_model_json).__dict__
        ratelimit_model2 = Ratelimit(**ratelimit_model_dict)

        # Verify the model instances are equivalent
        assert ratelimit_model == ratelimit_model2

        # Convert model instance back to dict and verify no loss of data
        ratelimit_model_json2 = ratelimit_model.to_dict()
        assert ratelimit_model_json2 == ratelimit_model_json


class TestModel_RuleCreate:
    """
    Test Class for RuleCreate
    """

    def test_rule_create_serialization(self):
        """
        Test serialization/deserialization for RuleCreate
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rules_override_model = {}  # RulesOverride
        rules_override_model['id'] = 'testString'
        rules_override_model['enabled'] = True
        rules_override_model['action'] = 'testString'
        rules_override_model['sensitivity_level'] = 'high'
        rules_override_model['score_threshold'] = 60

        categories_override_model = {}  # CategoriesOverride
        categories_override_model['category'] = 'testString'
        categories_override_model['enabled'] = True
        categories_override_model['action'] = 'testString'

        overrides_model = {}  # Overrides
        overrides_model['action'] = 'testString'
        overrides_model['enabled'] = True
        overrides_model['sensitivity_level'] = 'high'
        overrides_model['rules'] = [rules_override_model]
        overrides_model['categories'] = [categories_override_model]

        action_parameters_response_model = {}  # ActionParametersResponse
        action_parameters_response_model['content'] = '{"success": false, "error": "you have been blocked"}'
        action_parameters_response_model['content_type'] = 'application/json'
        action_parameters_response_model['status_code'] = 400

        action_parameters_model = {}  # ActionParameters
        action_parameters_model['id'] = 'testString'
        action_parameters_model['overrides'] = overrides_model
        action_parameters_model['version'] = 'testString'
        action_parameters_model['ruleset'] = 'testString'
        action_parameters_model['rulesets'] = ['testString']
        action_parameters_model['phases'] = ['testString']
        action_parameters_model['products'] = ['testString']
        action_parameters_model['response'] = action_parameters_response_model

        ratelimit_model = {}  # Ratelimit
        ratelimit_model['characteristics'] = ['testString']
        ratelimit_model['counting_expression'] = 'testString'
        ratelimit_model['mitigation_timeout'] = 38
        ratelimit_model['period'] = 38
        ratelimit_model['requests_per_period'] = 38

        logging_model = {}  # Logging
        logging_model['enabled'] = True

        position_model = {}  # Position
        position_model['before'] = 'testString'
        position_model['after'] = 'testString'
        position_model['index'] = 0

        # Construct a json representation of a RuleCreate model
        rule_create_model_json = {}
        rule_create_model_json['action'] = 'testString'
        rule_create_model_json['action_parameters'] = action_parameters_model
        rule_create_model_json['ratelimit'] = ratelimit_model
        rule_create_model_json['description'] = 'testString'
        rule_create_model_json['enabled'] = True
        rule_create_model_json['expression'] = 'ip.src ne 1.1.1.1'
        rule_create_model_json['id'] = 'testString'
        rule_create_model_json['logging'] = logging_model
        rule_create_model_json['ref'] = 'my_ref'
        rule_create_model_json['position'] = position_model

        # Construct a model instance of RuleCreate by calling from_dict on the json representation
        rule_create_model = RuleCreate.from_dict(rule_create_model_json)
        assert rule_create_model != False

        # Construct a model instance of RuleCreate by calling from_dict on the json representation
        rule_create_model_dict = RuleCreate.from_dict(rule_create_model_json).__dict__
        rule_create_model2 = RuleCreate(**rule_create_model_dict)

        # Verify the model instances are equivalent
        assert rule_create_model == rule_create_model2

        # Convert model instance back to dict and verify no loss of data
        rule_create_model_json2 = rule_create_model.to_dict()
        assert rule_create_model_json2 == rule_create_model_json


class TestModel_RuleDetails:
    """
    Test Class for RuleDetails
    """

    def test_rule_details_serialization(self):
        """
        Test serialization/deserialization for RuleDetails
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rules_override_model = {}  # RulesOverride
        rules_override_model['id'] = 'testString'
        rules_override_model['enabled'] = True
        rules_override_model['action'] = 'testString'
        rules_override_model['sensitivity_level'] = 'high'
        rules_override_model['score_threshold'] = 60

        categories_override_model = {}  # CategoriesOverride
        categories_override_model['category'] = 'testString'
        categories_override_model['enabled'] = True
        categories_override_model['action'] = 'testString'

        overrides_model = {}  # Overrides
        overrides_model['action'] = 'testString'
        overrides_model['enabled'] = True
        overrides_model['sensitivity_level'] = 'high'
        overrides_model['rules'] = [rules_override_model]
        overrides_model['categories'] = [categories_override_model]

        action_parameters_response_model = {}  # ActionParametersResponse
        action_parameters_response_model['content'] = '{"success": false, "error": "you have been blocked"}'
        action_parameters_response_model['content_type'] = 'application/json'
        action_parameters_response_model['status_code'] = 400

        action_parameters_model = {}  # ActionParameters
        action_parameters_model['id'] = 'testString'
        action_parameters_model['overrides'] = overrides_model
        action_parameters_model['version'] = 'testString'
        action_parameters_model['ruleset'] = 'testString'
        action_parameters_model['rulesets'] = ['testString']
        action_parameters_model['phases'] = ['testString']
        action_parameters_model['products'] = ['testString']
        action_parameters_model['response'] = action_parameters_response_model

        logging_model = {}  # Logging
        logging_model['enabled'] = True

        # Construct a json representation of a RuleDetails model
        rule_details_model_json = {}
        rule_details_model_json['id'] = 'testString'
        rule_details_model_json['version'] = 'testString'
        rule_details_model_json['action'] = 'testString'
        rule_details_model_json['action_parameters'] = action_parameters_model
        rule_details_model_json['categories'] = ['testString']
        rule_details_model_json['enabled'] = True
        rule_details_model_json['description'] = 'testString'
        rule_details_model_json['expression'] = 'ip.src ne 1.1.1.1'
        rule_details_model_json['ref'] = 'my_ref'
        rule_details_model_json['logging'] = logging_model
        rule_details_model_json['last_updated'] = '2000-01-01T00:00:00.000000Z'

        # Construct a model instance of RuleDetails by calling from_dict on the json representation
        rule_details_model = RuleDetails.from_dict(rule_details_model_json)
        assert rule_details_model != False

        # Construct a model instance of RuleDetails by calling from_dict on the json representation
        rule_details_model_dict = RuleDetails.from_dict(rule_details_model_json).__dict__
        rule_details_model2 = RuleDetails(**rule_details_model_dict)

        # Verify the model instances are equivalent
        assert rule_details_model == rule_details_model2

        # Convert model instance back to dict and verify no loss of data
        rule_details_model_json2 = rule_details_model.to_dict()
        assert rule_details_model_json2 == rule_details_model_json


class TestModel_RuleResp:
    """
    Test Class for RuleResp
    """

    def test_rule_resp_serialization(self):
        """
        Test serialization/deserialization for RuleResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        message_source_model = {}  # MessageSource
        message_source_model['pointer'] = '/rules/0/action'

        message_model = {}  # Message
        message_model['code'] = 10000
        message_model['message'] = 'something failed in the request'
        message_model['source'] = message_source_model

        rules_override_model = {}  # RulesOverride
        rules_override_model['id'] = 'testString'
        rules_override_model['enabled'] = True
        rules_override_model['action'] = 'testString'
        rules_override_model['sensitivity_level'] = 'high'
        rules_override_model['score_threshold'] = 60

        categories_override_model = {}  # CategoriesOverride
        categories_override_model['category'] = 'testString'
        categories_override_model['enabled'] = True
        categories_override_model['action'] = 'testString'

        overrides_model = {}  # Overrides
        overrides_model['action'] = 'testString'
        overrides_model['enabled'] = True
        overrides_model['sensitivity_level'] = 'high'
        overrides_model['rules'] = [rules_override_model]
        overrides_model['categories'] = [categories_override_model]

        action_parameters_response_model = {}  # ActionParametersResponse
        action_parameters_response_model['content'] = '{"success": false, "error": "you have been blocked"}'
        action_parameters_response_model['content_type'] = 'application/json'
        action_parameters_response_model['status_code'] = 400

        action_parameters_model = {}  # ActionParameters
        action_parameters_model['id'] = 'testString'
        action_parameters_model['overrides'] = overrides_model
        action_parameters_model['version'] = 'testString'
        action_parameters_model['ruleset'] = 'testString'
        action_parameters_model['rulesets'] = ['testString']
        action_parameters_model['phases'] = ['testString']
        action_parameters_model['products'] = ['testString']
        action_parameters_model['response'] = action_parameters_response_model

        logging_model = {}  # Logging
        logging_model['enabled'] = True

        rule_details_model = {}  # RuleDetails
        rule_details_model['id'] = 'testString'
        rule_details_model['version'] = 'testString'
        rule_details_model['action'] = 'testString'
        rule_details_model['action_parameters'] = action_parameters_model
        rule_details_model['categories'] = ['testString']
        rule_details_model['enabled'] = True
        rule_details_model['description'] = 'testString'
        rule_details_model['expression'] = 'ip.src ne 1.1.1.1'
        rule_details_model['ref'] = 'my_ref'
        rule_details_model['logging'] = logging_model
        rule_details_model['last_updated'] = '2000-01-01T00:00:00.000000Z'

        # Construct a json representation of a RuleResp model
        rule_resp_model_json = {}
        rule_resp_model_json['success'] = True
        rule_resp_model_json['errors'] = [message_model]
        rule_resp_model_json['messages'] = [message_model]
        rule_resp_model_json['result'] = rule_details_model

        # Construct a model instance of RuleResp by calling from_dict on the json representation
        rule_resp_model = RuleResp.from_dict(rule_resp_model_json)
        assert rule_resp_model != False

        # Construct a model instance of RuleResp by calling from_dict on the json representation
        rule_resp_model_dict = RuleResp.from_dict(rule_resp_model_json).__dict__
        rule_resp_model2 = RuleResp(**rule_resp_model_dict)

        # Verify the model instances are equivalent
        assert rule_resp_model == rule_resp_model2

        # Convert model instance back to dict and verify no loss of data
        rule_resp_model_json2 = rule_resp_model.to_dict()
        assert rule_resp_model_json2 == rule_resp_model_json


class TestModel_RulesOverride:
    """
    Test Class for RulesOverride
    """

    def test_rules_override_serialization(self):
        """
        Test serialization/deserialization for RulesOverride
        """

        # Construct a json representation of a RulesOverride model
        rules_override_model_json = {}
        rules_override_model_json['id'] = 'testString'
        rules_override_model_json['enabled'] = True
        rules_override_model_json['action'] = 'testString'
        rules_override_model_json['sensitivity_level'] = 'high'
        rules_override_model_json['score_threshold'] = 60

        # Construct a model instance of RulesOverride by calling from_dict on the json representation
        rules_override_model = RulesOverride.from_dict(rules_override_model_json)
        assert rules_override_model != False

        # Construct a model instance of RulesOverride by calling from_dict on the json representation
        rules_override_model_dict = RulesOverride.from_dict(rules_override_model_json).__dict__
        rules_override_model2 = RulesOverride(**rules_override_model_dict)

        # Verify the model instances are equivalent
        assert rules_override_model == rules_override_model2

        # Convert model instance back to dict and verify no loss of data
        rules_override_model_json2 = rules_override_model.to_dict()
        assert rules_override_model_json2 == rules_override_model_json


class TestModel_RulesetDetails:
    """
    Test Class for RulesetDetails
    """

    def test_ruleset_details_serialization(self):
        """
        Test serialization/deserialization for RulesetDetails
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rules_override_model = {}  # RulesOverride
        rules_override_model['id'] = 'testString'
        rules_override_model['enabled'] = True
        rules_override_model['action'] = 'testString'
        rules_override_model['sensitivity_level'] = 'high'
        rules_override_model['score_threshold'] = 60

        categories_override_model = {}  # CategoriesOverride
        categories_override_model['category'] = 'testString'
        categories_override_model['enabled'] = True
        categories_override_model['action'] = 'testString'

        overrides_model = {}  # Overrides
        overrides_model['action'] = 'testString'
        overrides_model['enabled'] = True
        overrides_model['sensitivity_level'] = 'high'
        overrides_model['rules'] = [rules_override_model]
        overrides_model['categories'] = [categories_override_model]

        action_parameters_response_model = {}  # ActionParametersResponse
        action_parameters_response_model['content'] = '{"success": false, "error": "you have been blocked"}'
        action_parameters_response_model['content_type'] = 'application/json'
        action_parameters_response_model['status_code'] = 400

        action_parameters_model = {}  # ActionParameters
        action_parameters_model['id'] = 'testString'
        action_parameters_model['overrides'] = overrides_model
        action_parameters_model['version'] = 'testString'
        action_parameters_model['ruleset'] = 'testString'
        action_parameters_model['rulesets'] = ['testString']
        action_parameters_model['phases'] = ['testString']
        action_parameters_model['products'] = ['testString']
        action_parameters_model['response'] = action_parameters_response_model

        logging_model = {}  # Logging
        logging_model['enabled'] = True

        rule_details_model = {}  # RuleDetails
        rule_details_model['id'] = 'testString'
        rule_details_model['version'] = 'testString'
        rule_details_model['action'] = 'testString'
        rule_details_model['action_parameters'] = action_parameters_model
        rule_details_model['categories'] = ['testString']
        rule_details_model['enabled'] = True
        rule_details_model['description'] = 'testString'
        rule_details_model['expression'] = 'ip.src ne 1.1.1.1'
        rule_details_model['ref'] = 'my_ref'
        rule_details_model['logging'] = logging_model
        rule_details_model['last_updated'] = '2000-01-01T00:00:00.000000Z'

        # Construct a json representation of a RulesetDetails model
        ruleset_details_model_json = {}
        ruleset_details_model_json['description'] = 'Custom instance ruleset'
        ruleset_details_model_json['id'] = 'testString'
        ruleset_details_model_json['kind'] = 'managed'
        ruleset_details_model_json['last_updated'] = '2000-01-01T00:00:00.000000Z'
        ruleset_details_model_json['name'] = 'testString'
        ruleset_details_model_json['phase'] = 'ddos_l4'
        ruleset_details_model_json['version'] = '1'
        ruleset_details_model_json['rules'] = [rule_details_model]

        # Construct a model instance of RulesetDetails by calling from_dict on the json representation
        ruleset_details_model = RulesetDetails.from_dict(ruleset_details_model_json)
        assert ruleset_details_model != False

        # Construct a model instance of RulesetDetails by calling from_dict on the json representation
        ruleset_details_model_dict = RulesetDetails.from_dict(ruleset_details_model_json).__dict__
        ruleset_details_model2 = RulesetDetails(**ruleset_details_model_dict)

        # Verify the model instances are equivalent
        assert ruleset_details_model == ruleset_details_model2

        # Convert model instance back to dict and verify no loss of data
        ruleset_details_model_json2 = ruleset_details_model.to_dict()
        assert ruleset_details_model_json2 == ruleset_details_model_json


class TestModel_RulesetResp:
    """
    Test Class for RulesetResp
    """

    def test_ruleset_resp_serialization(self):
        """
        Test serialization/deserialization for RulesetResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        message_source_model = {}  # MessageSource
        message_source_model['pointer'] = '/rules/0/action'

        message_model = {}  # Message
        message_model['code'] = 10000
        message_model['message'] = 'something failed in the request'
        message_model['source'] = message_source_model

        rules_override_model = {}  # RulesOverride
        rules_override_model['id'] = 'testString'
        rules_override_model['enabled'] = True
        rules_override_model['action'] = 'testString'
        rules_override_model['sensitivity_level'] = 'high'
        rules_override_model['score_threshold'] = 60

        categories_override_model = {}  # CategoriesOverride
        categories_override_model['category'] = 'testString'
        categories_override_model['enabled'] = True
        categories_override_model['action'] = 'testString'

        overrides_model = {}  # Overrides
        overrides_model['action'] = 'testString'
        overrides_model['enabled'] = True
        overrides_model['sensitivity_level'] = 'high'
        overrides_model['rules'] = [rules_override_model]
        overrides_model['categories'] = [categories_override_model]

        action_parameters_response_model = {}  # ActionParametersResponse
        action_parameters_response_model['content'] = '{"success": false, "error": "you have been blocked"}'
        action_parameters_response_model['content_type'] = 'application/json'
        action_parameters_response_model['status_code'] = 400

        action_parameters_model = {}  # ActionParameters
        action_parameters_model['id'] = 'testString'
        action_parameters_model['overrides'] = overrides_model
        action_parameters_model['version'] = 'testString'
        action_parameters_model['ruleset'] = 'testString'
        action_parameters_model['rulesets'] = ['testString']
        action_parameters_model['phases'] = ['testString']
        action_parameters_model['products'] = ['testString']
        action_parameters_model['response'] = action_parameters_response_model

        logging_model = {}  # Logging
        logging_model['enabled'] = True

        rule_details_model = {}  # RuleDetails
        rule_details_model['id'] = 'testString'
        rule_details_model['version'] = 'testString'
        rule_details_model['action'] = 'testString'
        rule_details_model['action_parameters'] = action_parameters_model
        rule_details_model['categories'] = ['testString']
        rule_details_model['enabled'] = True
        rule_details_model['description'] = 'testString'
        rule_details_model['expression'] = 'ip.src ne 1.1.1.1'
        rule_details_model['ref'] = 'my_ref'
        rule_details_model['logging'] = logging_model
        rule_details_model['last_updated'] = '2000-01-01T00:00:00.000000Z'

        ruleset_details_model = {}  # RulesetDetails
        ruleset_details_model['description'] = 'Custom instance ruleset'
        ruleset_details_model['id'] = 'testString'
        ruleset_details_model['kind'] = 'managed'
        ruleset_details_model['last_updated'] = '2000-01-01T00:00:00.000000Z'
        ruleset_details_model['name'] = 'testString'
        ruleset_details_model['phase'] = 'ddos_l4'
        ruleset_details_model['version'] = '1'
        ruleset_details_model['rules'] = [rule_details_model]

        # Construct a json representation of a RulesetResp model
        ruleset_resp_model_json = {}
        ruleset_resp_model_json['success'] = True
        ruleset_resp_model_json['errors'] = [message_model]
        ruleset_resp_model_json['messages'] = [message_model]
        ruleset_resp_model_json['result'] = ruleset_details_model

        # Construct a model instance of RulesetResp by calling from_dict on the json representation
        ruleset_resp_model = RulesetResp.from_dict(ruleset_resp_model_json)
        assert ruleset_resp_model != False

        # Construct a model instance of RulesetResp by calling from_dict on the json representation
        ruleset_resp_model_dict = RulesetResp.from_dict(ruleset_resp_model_json).__dict__
        ruleset_resp_model2 = RulesetResp(**ruleset_resp_model_dict)

        # Verify the model instances are equivalent
        assert ruleset_resp_model == ruleset_resp_model2

        # Convert model instance back to dict and verify no loss of data
        ruleset_resp_model_json2 = ruleset_resp_model.to_dict()
        assert ruleset_resp_model_json2 == ruleset_resp_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################