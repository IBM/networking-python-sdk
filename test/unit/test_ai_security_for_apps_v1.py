# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2026.
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
Unit Tests for AiSecurityForAppsV1
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import inspect
import json
import os
import pytest
import re
import requests
import responses
import urllib
from ibm_cloud_networking_services.ai_security_for_apps_v1 import *

crn = 'testString'
zone_identifier = 'testString'

_service = AiSecurityForAppsV1(
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
# Start of Service: AISecuritySettings
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

        service = AiSecurityForAppsV1.new_instance(
            crn=crn,
            zone_identifier=zone_identifier,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, AiSecurityForAppsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = AiSecurityForAppsV1.new_instance(
                crn=crn,
                zone_identifier=zone_identifier,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = AiSecurityForAppsV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='crn must be provided'):
            service = AiSecurityForAppsV1.new_instance(
                crn=None,
                zone_identifier=None,
            )


class TestGetAiSecuritySettings:
    """
    Test Class for get_ai_security_settings
    """

    @responses.activate
    def test_get_ai_security_settings_all_params(self):
        """
        get_ai_security_settings()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/ai_security/settings')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"enabled": false}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_ai_security_settings()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_ai_security_settings_all_params_with_retries(self):
        # Enable retries and run test_get_ai_security_settings_all_params.
        _service.enable_retries()
        self.test_get_ai_security_settings_all_params()

        # Disable retries and run test_get_ai_security_settings_all_params.
        _service.disable_retries()
        self.test_get_ai_security_settings_all_params()

    @responses.activate
    def test_get_ai_security_settings_value_error(self):
        """
        test_get_ai_security_settings_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/ai_security/settings')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"enabled": false}}'
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
                _service.get_ai_security_settings(**req_copy)

    def test_get_ai_security_settings_value_error_with_retries(self):
        # Enable retries and run test_get_ai_security_settings_value_error.
        _service.enable_retries()
        self.test_get_ai_security_settings_value_error()

        # Disable retries and run test_get_ai_security_settings_value_error.
        _service.disable_retries()
        self.test_get_ai_security_settings_value_error()


class TestReplaceZoneAiSecuritySettings:
    """
    Test Class for replace_zone_ai_security_settings
    """

    @responses.activate
    def test_replace_zone_ai_security_settings_all_params(self):
        """
        replace_zone_ai_security_settings()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/ai_security/settings')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"enabled": false}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        enabled = True

        # Invoke method
        response = _service.replace_zone_ai_security_settings(
            enabled=enabled,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['enabled'] == True

    def test_replace_zone_ai_security_settings_all_params_with_retries(self):
        # Enable retries and run test_replace_zone_ai_security_settings_all_params.
        _service.enable_retries()
        self.test_replace_zone_ai_security_settings_all_params()

        # Disable retries and run test_replace_zone_ai_security_settings_all_params.
        _service.disable_retries()
        self.test_replace_zone_ai_security_settings_all_params()

    @responses.activate
    def test_replace_zone_ai_security_settings_required_params(self):
        """
        test_replace_zone_ai_security_settings_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/ai_security/settings')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"enabled": false}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.replace_zone_ai_security_settings()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_replace_zone_ai_security_settings_required_params_with_retries(self):
        # Enable retries and run test_replace_zone_ai_security_settings_required_params.
        _service.enable_retries()
        self.test_replace_zone_ai_security_settings_required_params()

        # Disable retries and run test_replace_zone_ai_security_settings_required_params.
        _service.disable_retries()
        self.test_replace_zone_ai_security_settings_required_params()

    @responses.activate
    def test_replace_zone_ai_security_settings_value_error(self):
        """
        test_replace_zone_ai_security_settings_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/ai_security/settings')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"enabled": false}}'
        responses.add(
            responses.PUT,
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
                _service.replace_zone_ai_security_settings(**req_copy)

    def test_replace_zone_ai_security_settings_value_error_with_retries(self):
        # Enable retries and run test_replace_zone_ai_security_settings_value_error.
        _service.enable_retries()
        self.test_replace_zone_ai_security_settings_value_error()

        # Disable retries and run test_replace_zone_ai_security_settings_value_error.
        _service.disable_retries()
        self.test_replace_zone_ai_security_settings_value_error()


# endregion
##############################################################################
# End of Service: AISecuritySettings
##############################################################################

##############################################################################
# Start of Service: APIGatewayDiscovery
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

        service = AiSecurityForAppsV1.new_instance(
            crn=crn,
            zone_identifier=zone_identifier,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, AiSecurityForAppsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = AiSecurityForAppsV1.new_instance(
                crn=crn,
                zone_identifier=zone_identifier,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = AiSecurityForAppsV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='crn must be provided'):
            service = AiSecurityForAppsV1.new_instance(
                crn=None,
                zone_identifier=None,
            )


class TestGetApiGatewayDiscovery:
    """
    Test Class for get_api_gateway_discovery
    """

    @responses.activate
    def test_get_api_gateway_discovery_all_params(self):
        """
        get_api_gateway_discovery()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/discovery')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"anyKey": "anyValue"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_api_gateway_discovery()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_api_gateway_discovery_all_params_with_retries(self):
        # Enable retries and run test_get_api_gateway_discovery_all_params.
        _service.enable_retries()
        self.test_get_api_gateway_discovery_all_params()

        # Disable retries and run test_get_api_gateway_discovery_all_params.
        _service.disable_retries()
        self.test_get_api_gateway_discovery_all_params()

    @responses.activate
    def test_get_api_gateway_discovery_value_error(self):
        """
        test_get_api_gateway_discovery_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/discovery')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"anyKey": "anyValue"}}'
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
                _service.get_api_gateway_discovery(**req_copy)

    def test_get_api_gateway_discovery_value_error_with_retries(self):
        # Enable retries and run test_get_api_gateway_discovery_value_error.
        _service.enable_retries()
        self.test_get_api_gateway_discovery_value_error()

        # Disable retries and run test_get_api_gateway_discovery_value_error.
        _service.disable_retries()
        self.test_get_api_gateway_discovery_value_error()


# endregion
##############################################################################
# End of Service: APIGatewayDiscovery
##############################################################################

##############################################################################
# Start of Service: APIGatewayDiscoveryOperations
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

        service = AiSecurityForAppsV1.new_instance(
            crn=crn,
            zone_identifier=zone_identifier,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, AiSecurityForAppsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = AiSecurityForAppsV1.new_instance(
                crn=crn,
                zone_identifier=zone_identifier,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = AiSecurityForAppsV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='crn must be provided'):
            service = AiSecurityForAppsV1.new_instance(
                crn=None,
                zone_identifier=None,
            )


class TestListApiGatewayDiscoveryOperations:
    """
    Test Class for list_api_gateway_discovery_operations
    """

    @responses.activate
    def test_list_api_gateway_discovery_operations_all_params(self):
        """
        list_api_gateway_discovery_operations()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/discovery/operations')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415", "endpoint": "/v1/messages", "host": "api.example.com", "method": "POST", "last_updated": "2024-01-01T00:00:00.000Z", "origin": ["ML"], "state": "review", "features": {"traffic_stats": {"last_updated": "2019-01-01T12:00:00.000Z", "period_seconds": 14, "requests": 8}}}], "result_info": {"count": 5, "page": 4, "per_page": 8, "total_count": 11}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        diff = True
        direction = 'asc'
        endpoint = 'testString'
        host = ['testString']
        method = ['testString']
        order = 'host'
        origin = 'ML'
        state = 'review'
        page = 1
        per_page = 5

        # Invoke method
        response = _service.list_api_gateway_discovery_operations(
            diff=diff,
            direction=direction,
            endpoint=endpoint,
            host=host,
            method=method,
            order=order,
            origin=origin,
            state=state,
            page=page,
            per_page=per_page,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'diff={}'.format('true' if diff else 'false') in query_string
        assert 'direction={}'.format(direction) in query_string
        assert 'endpoint={}'.format(endpoint) in query_string
        assert 'host={}'.format(','.join(host)) in query_string
        assert 'method={}'.format(','.join(method)) in query_string
        assert 'order={}'.format(order) in query_string
        assert 'origin={}'.format(origin) in query_string
        assert 'state={}'.format(state) in query_string
        assert 'page={}'.format(page) in query_string
        assert 'per_page={}'.format(per_page) in query_string

    def test_list_api_gateway_discovery_operations_all_params_with_retries(self):
        # Enable retries and run test_list_api_gateway_discovery_operations_all_params.
        _service.enable_retries()
        self.test_list_api_gateway_discovery_operations_all_params()

        # Disable retries and run test_list_api_gateway_discovery_operations_all_params.
        _service.disable_retries()
        self.test_list_api_gateway_discovery_operations_all_params()

    @responses.activate
    def test_list_api_gateway_discovery_operations_required_params(self):
        """
        test_list_api_gateway_discovery_operations_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/discovery/operations')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415", "endpoint": "/v1/messages", "host": "api.example.com", "method": "POST", "last_updated": "2024-01-01T00:00:00.000Z", "origin": ["ML"], "state": "review", "features": {"traffic_stats": {"last_updated": "2019-01-01T12:00:00.000Z", "period_seconds": 14, "requests": 8}}}], "result_info": {"count": 5, "page": 4, "per_page": 8, "total_count": 11}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_api_gateway_discovery_operations()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_api_gateway_discovery_operations_required_params_with_retries(self):
        # Enable retries and run test_list_api_gateway_discovery_operations_required_params.
        _service.enable_retries()
        self.test_list_api_gateway_discovery_operations_required_params()

        # Disable retries and run test_list_api_gateway_discovery_operations_required_params.
        _service.disable_retries()
        self.test_list_api_gateway_discovery_operations_required_params()

    @responses.activate
    def test_list_api_gateway_discovery_operations_value_error(self):
        """
        test_list_api_gateway_discovery_operations_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/discovery/operations')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415", "endpoint": "/v1/messages", "host": "api.example.com", "method": "POST", "last_updated": "2024-01-01T00:00:00.000Z", "origin": ["ML"], "state": "review", "features": {"traffic_stats": {"last_updated": "2019-01-01T12:00:00.000Z", "period_seconds": 14, "requests": 8}}}], "result_info": {"count": 5, "page": 4, "per_page": 8, "total_count": 11}}'
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
                _service.list_api_gateway_discovery_operations(**req_copy)

    def test_list_api_gateway_discovery_operations_value_error_with_retries(self):
        # Enable retries and run test_list_api_gateway_discovery_operations_value_error.
        _service.enable_retries()
        self.test_list_api_gateway_discovery_operations_value_error()

        # Disable retries and run test_list_api_gateway_discovery_operations_value_error.
        _service.disable_retries()
        self.test_list_api_gateway_discovery_operations_value_error()


class TestUpdateZoneApiGatewayDiscoveryOperation:
    """
    Test Class for update_zone_api_gateway_discovery_operation
    """

    @responses.activate
    def test_update_zone_api_gateway_discovery_operation_all_params(self):
        """
        update_zone_api_gateway_discovery_operation()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/discovery/operations')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415", "endpoint": "/v1/messages", "host": "api.example.com", "method": "POST", "last_updated": "2024-01-01T00:00:00.000Z", "origin": ["ML"], "state": "review", "features": {"traffic_stats": {"last_updated": "2019-01-01T12:00:00.000Z", "period_seconds": 14, "requests": 8}}}]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        request_body = {'key1': 'testString'}

        # Invoke method
        response = _service.update_zone_api_gateway_discovery_operation(
            request_body=request_body,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == request_body

    def test_update_zone_api_gateway_discovery_operation_all_params_with_retries(self):
        # Enable retries and run test_update_zone_api_gateway_discovery_operation_all_params.
        _service.enable_retries()
        self.test_update_zone_api_gateway_discovery_operation_all_params()

        # Disable retries and run test_update_zone_api_gateway_discovery_operation_all_params.
        _service.disable_retries()
        self.test_update_zone_api_gateway_discovery_operation_all_params()

    @responses.activate
    def test_update_zone_api_gateway_discovery_operation_required_params(self):
        """
        test_update_zone_api_gateway_discovery_operation_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/discovery/operations')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415", "endpoint": "/v1/messages", "host": "api.example.com", "method": "POST", "last_updated": "2024-01-01T00:00:00.000Z", "origin": ["ML"], "state": "review", "features": {"traffic_stats": {"last_updated": "2019-01-01T12:00:00.000Z", "period_seconds": 14, "requests": 8}}}]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_zone_api_gateway_discovery_operation()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_zone_api_gateway_discovery_operation_required_params_with_retries(self):
        # Enable retries and run test_update_zone_api_gateway_discovery_operation_required_params.
        _service.enable_retries()
        self.test_update_zone_api_gateway_discovery_operation_required_params()

        # Disable retries and run test_update_zone_api_gateway_discovery_operation_required_params.
        _service.disable_retries()
        self.test_update_zone_api_gateway_discovery_operation_required_params()

    @responses.activate
    def test_update_zone_api_gateway_discovery_operation_value_error(self):
        """
        test_update_zone_api_gateway_discovery_operation_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/discovery/operations')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415", "endpoint": "/v1/messages", "host": "api.example.com", "method": "POST", "last_updated": "2024-01-01T00:00:00.000Z", "origin": ["ML"], "state": "review", "features": {"traffic_stats": {"last_updated": "2019-01-01T12:00:00.000Z", "period_seconds": 14, "requests": 8}}}]}'
        responses.add(
            responses.PATCH,
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
                _service.update_zone_api_gateway_discovery_operation(**req_copy)

    def test_update_zone_api_gateway_discovery_operation_value_error_with_retries(self):
        # Enable retries and run test_update_zone_api_gateway_discovery_operation_value_error.
        _service.enable_retries()
        self.test_update_zone_api_gateway_discovery_operation_value_error()

        # Disable retries and run test_update_zone_api_gateway_discovery_operation_value_error.
        _service.disable_retries()
        self.test_update_zone_api_gateway_discovery_operation_value_error()


# endregion
##############################################################################
# End of Service: APIGatewayDiscoveryOperations
##############################################################################

##############################################################################
# Start of Service: APIGatewayOperations
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

        service = AiSecurityForAppsV1.new_instance(
            crn=crn,
            zone_identifier=zone_identifier,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, AiSecurityForAppsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = AiSecurityForAppsV1.new_instance(
                crn=crn,
                zone_identifier=zone_identifier,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = AiSecurityForAppsV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='crn must be provided'):
            service = AiSecurityForAppsV1.new_instance(
                crn=None,
                zone_identifier=None,
            )


class TestDeleteZoneApiGatewayOperations:
    """
    Test Class for delete_zone_api_gateway_operations
    """

    @responses.activate
    def test_delete_zone_api_gateway_operations_all_params(self):
        """
        delete_zone_api_gateway_operations()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/operations')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": "anyValue"}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ApiGatewayOperationsDeleteInputItem model
        api_gateway_operations_delete_input_item_model = {}
        api_gateway_operations_delete_input_item_model['operation_id'] = 'f174e90a-fafe-4643-bbbc-4a0ed4fc8415'

        # Set up parameter values
        api_gateway_operations_delete_input_item = [api_gateway_operations_delete_input_item_model]

        # Invoke method
        response = _service.delete_zone_api_gateway_operations(
            api_gateway_operations_delete_input_item,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == api_gateway_operations_delete_input_item

    def test_delete_zone_api_gateway_operations_all_params_with_retries(self):
        # Enable retries and run test_delete_zone_api_gateway_operations_all_params.
        _service.enable_retries()
        self.test_delete_zone_api_gateway_operations_all_params()

        # Disable retries and run test_delete_zone_api_gateway_operations_all_params.
        _service.disable_retries()
        self.test_delete_zone_api_gateway_operations_all_params()

    @responses.activate
    def test_delete_zone_api_gateway_operations_value_error(self):
        """
        test_delete_zone_api_gateway_operations_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/operations')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": "anyValue"}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ApiGatewayOperationsDeleteInputItem model
        api_gateway_operations_delete_input_item_model = {}
        api_gateway_operations_delete_input_item_model['operation_id'] = 'f174e90a-fafe-4643-bbbc-4a0ed4fc8415'

        # Set up parameter values
        api_gateway_operations_delete_input_item = [api_gateway_operations_delete_input_item_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "api_gateway_operations_delete_input_item": api_gateway_operations_delete_input_item,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_zone_api_gateway_operations(**req_copy)

    def test_delete_zone_api_gateway_operations_value_error_with_retries(self):
        # Enable retries and run test_delete_zone_api_gateway_operations_value_error.
        _service.enable_retries()
        self.test_delete_zone_api_gateway_operations_value_error()

        # Disable retries and run test_delete_zone_api_gateway_operations_value_error.
        _service.disable_retries()
        self.test_delete_zone_api_gateway_operations_value_error()


class TestListZoneApiGatewayOperations:
    """
    Test Class for list_zone_api_gateway_operations
    """

    @responses.activate
    def test_list_zone_api_gateway_operations_all_params(self):
        """
        list_zone_api_gateway_operations()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/operations')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"operation_id": "test-fafe-4643-bbbc-example", "method": "POST", "host": "api.example.com", "endpoint": "/v1/messages", "last_updated": "2024-01-01T00:00:00.000Z"}], "result_info": {"count": 5, "page": 4, "per_page": 8, "total_count": 11}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        host = ['testString']
        method = ['GET']
        endpoint = 'testString'
        labels = ['testString']
        direction = 'asc'
        order = 'host'
        page = 1
        per_page = 1

        # Invoke method
        response = _service.list_zone_api_gateway_operations(
            host=host,
            method=method,
            endpoint=endpoint,
            labels=labels,
            direction=direction,
            order=order,
            page=page,
            per_page=per_page,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'host={}'.format(','.join(host)) in query_string
        assert 'method={}'.format(','.join(method)) in query_string
        assert 'endpoint={}'.format(endpoint) in query_string
        assert 'labels={}'.format(','.join(labels)) in query_string
        assert 'direction={}'.format(direction) in query_string
        assert 'order={}'.format(order) in query_string
        assert 'page={}'.format(page) in query_string
        assert 'per_page={}'.format(per_page) in query_string

    def test_list_zone_api_gateway_operations_all_params_with_retries(self):
        # Enable retries and run test_list_zone_api_gateway_operations_all_params.
        _service.enable_retries()
        self.test_list_zone_api_gateway_operations_all_params()

        # Disable retries and run test_list_zone_api_gateway_operations_all_params.
        _service.disable_retries()
        self.test_list_zone_api_gateway_operations_all_params()

    @responses.activate
    def test_list_zone_api_gateway_operations_required_params(self):
        """
        test_list_zone_api_gateway_operations_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/operations')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"operation_id": "test-fafe-4643-bbbc-example", "method": "POST", "host": "api.example.com", "endpoint": "/v1/messages", "last_updated": "2024-01-01T00:00:00.000Z"}], "result_info": {"count": 5, "page": 4, "per_page": 8, "total_count": 11}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_zone_api_gateway_operations()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_zone_api_gateway_operations_required_params_with_retries(self):
        # Enable retries and run test_list_zone_api_gateway_operations_required_params.
        _service.enable_retries()
        self.test_list_zone_api_gateway_operations_required_params()

        # Disable retries and run test_list_zone_api_gateway_operations_required_params.
        _service.disable_retries()
        self.test_list_zone_api_gateway_operations_required_params()

    @responses.activate
    def test_list_zone_api_gateway_operations_value_error(self):
        """
        test_list_zone_api_gateway_operations_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/operations')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"operation_id": "test-fafe-4643-bbbc-example", "method": "POST", "host": "api.example.com", "endpoint": "/v1/messages", "last_updated": "2024-01-01T00:00:00.000Z"}], "result_info": {"count": 5, "page": 4, "per_page": 8, "total_count": 11}}'
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
                _service.list_zone_api_gateway_operations(**req_copy)

    def test_list_zone_api_gateway_operations_value_error_with_retries(self):
        # Enable retries and run test_list_zone_api_gateway_operations_value_error.
        _service.enable_retries()
        self.test_list_zone_api_gateway_operations_value_error()

        # Disable retries and run test_list_zone_api_gateway_operations_value_error.
        _service.disable_retries()
        self.test_list_zone_api_gateway_operations_value_error()


class TestCreateZoneApiGatewayOperation:
    """
    Test Class for create_zone_api_gateway_operation
    """

    @responses.activate
    def test_create_zone_api_gateway_operation_all_params(self):
        """
        create_zone_api_gateway_operation()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/operations')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"operation_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415", "method": "POST", "host": "api.example.com", "endpoint": "/v1/messages"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ApiGatewayOperation model
        api_gateway_operation_model = {}
        api_gateway_operation_model['method'] = 'POST'
        api_gateway_operation_model['host'] = 'api.example.com'
        api_gateway_operation_model['endpoint'] = '/v1/messages'

        # Set up parameter values
        api_gateway_operation = [api_gateway_operation_model]

        # Invoke method
        response = _service.create_zone_api_gateway_operation(
            api_gateway_operation=api_gateway_operation,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == api_gateway_operation

    def test_create_zone_api_gateway_operation_all_params_with_retries(self):
        # Enable retries and run test_create_zone_api_gateway_operation_all_params.
        _service.enable_retries()
        self.test_create_zone_api_gateway_operation_all_params()

        # Disable retries and run test_create_zone_api_gateway_operation_all_params.
        _service.disable_retries()
        self.test_create_zone_api_gateway_operation_all_params()

    @responses.activate
    def test_create_zone_api_gateway_operation_required_params(self):
        """
        test_create_zone_api_gateway_operation_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/operations')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"operation_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415", "method": "POST", "host": "api.example.com", "endpoint": "/v1/messages"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.create_zone_api_gateway_operation()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_zone_api_gateway_operation_required_params_with_retries(self):
        # Enable retries and run test_create_zone_api_gateway_operation_required_params.
        _service.enable_retries()
        self.test_create_zone_api_gateway_operation_required_params()

        # Disable retries and run test_create_zone_api_gateway_operation_required_params.
        _service.disable_retries()
        self.test_create_zone_api_gateway_operation_required_params()

    @responses.activate
    def test_create_zone_api_gateway_operation_value_error(self):
        """
        test_create_zone_api_gateway_operation_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/operations')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"operation_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415", "method": "POST", "host": "api.example.com", "endpoint": "/v1/messages"}]}'
        responses.add(
            responses.POST,
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
                _service.create_zone_api_gateway_operation(**req_copy)

    def test_create_zone_api_gateway_operation_value_error_with_retries(self):
        # Enable retries and run test_create_zone_api_gateway_operation_value_error.
        _service.enable_retries()
        self.test_create_zone_api_gateway_operation_value_error()

        # Disable retries and run test_create_zone_api_gateway_operation_value_error.
        _service.disable_retries()
        self.test_create_zone_api_gateway_operation_value_error()


class TestCreateApiGatewayOperationItem:
    """
    Test Class for create_api_gateway_operation_item
    """

    @responses.activate
    def test_create_api_gateway_operation_item_all_params(self):
        """
        create_api_gateway_operation_item()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/operations/item')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"operation_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415", "method": "POST", "host": "api.example.com", "endpoint": "/v1/messages"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        method = 'POST'
        host = 'api.example.com'
        endpoint = '/v1/messages'

        # Invoke method
        response = _service.create_api_gateway_operation_item(
            method=method,
            host=host,
            endpoint=endpoint,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['method'] == 'POST'
        assert req_body['host'] == 'api.example.com'
        assert req_body['endpoint'] == '/v1/messages'

    def test_create_api_gateway_operation_item_all_params_with_retries(self):
        # Enable retries and run test_create_api_gateway_operation_item_all_params.
        _service.enable_retries()
        self.test_create_api_gateway_operation_item_all_params()

        # Disable retries and run test_create_api_gateway_operation_item_all_params.
        _service.disable_retries()
        self.test_create_api_gateway_operation_item_all_params()

    @responses.activate
    def test_create_api_gateway_operation_item_required_params(self):
        """
        test_create_api_gateway_operation_item_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/operations/item')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"operation_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415", "method": "POST", "host": "api.example.com", "endpoint": "/v1/messages"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.create_api_gateway_operation_item()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_api_gateway_operation_item_required_params_with_retries(self):
        # Enable retries and run test_create_api_gateway_operation_item_required_params.
        _service.enable_retries()
        self.test_create_api_gateway_operation_item_required_params()

        # Disable retries and run test_create_api_gateway_operation_item_required_params.
        _service.disable_retries()
        self.test_create_api_gateway_operation_item_required_params()

    @responses.activate
    def test_create_api_gateway_operation_item_value_error(self):
        """
        test_create_api_gateway_operation_item_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/operations/item')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"operation_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415", "method": "POST", "host": "api.example.com", "endpoint": "/v1/messages"}}'
        responses.add(
            responses.POST,
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
                _service.create_api_gateway_operation_item(**req_copy)

    def test_create_api_gateway_operation_item_value_error_with_retries(self):
        # Enable retries and run test_create_api_gateway_operation_item_value_error.
        _service.enable_retries()
        self.test_create_api_gateway_operation_item_value_error()

        # Disable retries and run test_create_api_gateway_operation_item_value_error.
        _service.disable_retries()
        self.test_create_api_gateway_operation_item_value_error()


class TestReplaceZoneApiGatewayOperationLabels:
    """
    Test Class for replace_zone_api_gateway_operation_labels
    """

    @responses.activate
    def test_replace_zone_api_gateway_operation_labels_all_params(self):
        """
        replace_zone_api_gateway_operation_labels()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/operations/labels')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"operation_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415", "labels": [{"name": "cf-llm", "source": "managed"}]}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ApiGatewayOperationsLabelsBulkInputSelectorInclude model
        api_gateway_operations_labels_bulk_input_selector_include_model = {}
        api_gateway_operations_labels_bulk_input_selector_include_model['operation_ids'] = ['f174e90a-fafe-4643-bbbc-4a0ed4fc8415']

        # Construct a dict representation of a ApiGatewayOperationsLabelsBulkInputSelector model
        api_gateway_operations_labels_bulk_input_selector_model = {}
        api_gateway_operations_labels_bulk_input_selector_model['include'] = api_gateway_operations_labels_bulk_input_selector_include_model

        # Construct a dict representation of a ApiGatewayOperationsLabelsBulkInputUser model
        api_gateway_operations_labels_bulk_input_user_model = {}
        api_gateway_operations_labels_bulk_input_user_model['labels'] = ['testString']

        # Construct a dict representation of a ApiGatewayOperationsLabelsBulkInputManaged model
        api_gateway_operations_labels_bulk_input_managed_model = {}
        api_gateway_operations_labels_bulk_input_managed_model['labels'] = ['testString']

        # Set up parameter values
        selector = api_gateway_operations_labels_bulk_input_selector_model
        user = api_gateway_operations_labels_bulk_input_user_model
        managed = api_gateway_operations_labels_bulk_input_managed_model

        # Invoke method
        response = _service.replace_zone_api_gateway_operation_labels(
            selector=selector,
            user=user,
            managed=managed,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['selector'] == api_gateway_operations_labels_bulk_input_selector_model
        assert req_body['user'] == api_gateway_operations_labels_bulk_input_user_model
        assert req_body['managed'] == api_gateway_operations_labels_bulk_input_managed_model

    def test_replace_zone_api_gateway_operation_labels_all_params_with_retries(self):
        # Enable retries and run test_replace_zone_api_gateway_operation_labels_all_params.
        _service.enable_retries()
        self.test_replace_zone_api_gateway_operation_labels_all_params()

        # Disable retries and run test_replace_zone_api_gateway_operation_labels_all_params.
        _service.disable_retries()
        self.test_replace_zone_api_gateway_operation_labels_all_params()

    @responses.activate
    def test_replace_zone_api_gateway_operation_labels_required_params(self):
        """
        test_replace_zone_api_gateway_operation_labels_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/operations/labels')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"operation_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415", "labels": [{"name": "cf-llm", "source": "managed"}]}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.replace_zone_api_gateway_operation_labels()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_replace_zone_api_gateway_operation_labels_required_params_with_retries(self):
        # Enable retries and run test_replace_zone_api_gateway_operation_labels_required_params.
        _service.enable_retries()
        self.test_replace_zone_api_gateway_operation_labels_required_params()

        # Disable retries and run test_replace_zone_api_gateway_operation_labels_required_params.
        _service.disable_retries()
        self.test_replace_zone_api_gateway_operation_labels_required_params()

    @responses.activate
    def test_replace_zone_api_gateway_operation_labels_value_error(self):
        """
        test_replace_zone_api_gateway_operation_labels_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/operations/labels')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"operation_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415", "labels": [{"name": "cf-llm", "source": "managed"}]}]}'
        responses.add(
            responses.PUT,
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
                _service.replace_zone_api_gateway_operation_labels(**req_copy)

    def test_replace_zone_api_gateway_operation_labels_value_error_with_retries(self):
        # Enable retries and run test_replace_zone_api_gateway_operation_labels_value_error.
        _service.enable_retries()
        self.test_replace_zone_api_gateway_operation_labels_value_error()

        # Disable retries and run test_replace_zone_api_gateway_operation_labels_value_error.
        _service.disable_retries()
        self.test_replace_zone_api_gateway_operation_labels_value_error()


class TestDeleteZoneApiGatewayOperationLabels:
    """
    Test Class for delete_zone_api_gateway_operation_labels
    """

    @responses.activate
    def test_delete_zone_api_gateway_operation_labels_all_params(self):
        """
        delete_zone_api_gateway_operation_labels()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/operations/labels')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": "anyValue"}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ApiGatewayOperationsLabelsBulkDeleteInputSelectorInclude model
        api_gateway_operations_labels_bulk_delete_input_selector_include_model = {}
        api_gateway_operations_labels_bulk_delete_input_selector_include_model['operation_ids'] = ['f174e90a-fafe-4643-bbbc-4a0ed4fc8415']

        # Construct a dict representation of a ApiGatewayOperationsLabelsBulkDeleteInputSelector model
        api_gateway_operations_labels_bulk_delete_input_selector_model = {}
        api_gateway_operations_labels_bulk_delete_input_selector_model['include'] = api_gateway_operations_labels_bulk_delete_input_selector_include_model

        # Construct a dict representation of a ApiGatewayOperationsLabelsBulkDeleteInputUser model
        api_gateway_operations_labels_bulk_delete_input_user_model = {}
        api_gateway_operations_labels_bulk_delete_input_user_model['labels'] = ['testString']

        # Construct a dict representation of a ApiGatewayOperationsLabelsBulkDeleteInputManaged model
        api_gateway_operations_labels_bulk_delete_input_managed_model = {}
        api_gateway_operations_labels_bulk_delete_input_managed_model['labels'] = ['testString']

        # Set up parameter values
        selector = api_gateway_operations_labels_bulk_delete_input_selector_model
        user = api_gateway_operations_labels_bulk_delete_input_user_model
        managed = api_gateway_operations_labels_bulk_delete_input_managed_model

        # Invoke method
        response = _service.delete_zone_api_gateway_operation_labels(
            selector,
            user=user,
            managed=managed,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['selector'] == api_gateway_operations_labels_bulk_delete_input_selector_model
        assert req_body['user'] == api_gateway_operations_labels_bulk_delete_input_user_model
        assert req_body['managed'] == api_gateway_operations_labels_bulk_delete_input_managed_model

    def test_delete_zone_api_gateway_operation_labels_all_params_with_retries(self):
        # Enable retries and run test_delete_zone_api_gateway_operation_labels_all_params.
        _service.enable_retries()
        self.test_delete_zone_api_gateway_operation_labels_all_params()

        # Disable retries and run test_delete_zone_api_gateway_operation_labels_all_params.
        _service.disable_retries()
        self.test_delete_zone_api_gateway_operation_labels_all_params()

    @responses.activate
    def test_delete_zone_api_gateway_operation_labels_value_error(self):
        """
        test_delete_zone_api_gateway_operation_labels_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/operations/labels')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": "anyValue"}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ApiGatewayOperationsLabelsBulkDeleteInputSelectorInclude model
        api_gateway_operations_labels_bulk_delete_input_selector_include_model = {}
        api_gateway_operations_labels_bulk_delete_input_selector_include_model['operation_ids'] = ['f174e90a-fafe-4643-bbbc-4a0ed4fc8415']

        # Construct a dict representation of a ApiGatewayOperationsLabelsBulkDeleteInputSelector model
        api_gateway_operations_labels_bulk_delete_input_selector_model = {}
        api_gateway_operations_labels_bulk_delete_input_selector_model['include'] = api_gateway_operations_labels_bulk_delete_input_selector_include_model

        # Construct a dict representation of a ApiGatewayOperationsLabelsBulkDeleteInputUser model
        api_gateway_operations_labels_bulk_delete_input_user_model = {}
        api_gateway_operations_labels_bulk_delete_input_user_model['labels'] = ['testString']

        # Construct a dict representation of a ApiGatewayOperationsLabelsBulkDeleteInputManaged model
        api_gateway_operations_labels_bulk_delete_input_managed_model = {}
        api_gateway_operations_labels_bulk_delete_input_managed_model['labels'] = ['testString']

        # Set up parameter values
        selector = api_gateway_operations_labels_bulk_delete_input_selector_model
        user = api_gateway_operations_labels_bulk_delete_input_user_model
        managed = api_gateway_operations_labels_bulk_delete_input_managed_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "selector": selector,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_zone_api_gateway_operation_labels(**req_copy)

    def test_delete_zone_api_gateway_operation_labels_value_error_with_retries(self):
        # Enable retries and run test_delete_zone_api_gateway_operation_labels_value_error.
        _service.enable_retries()
        self.test_delete_zone_api_gateway_operation_labels_value_error()

        # Disable retries and run test_delete_zone_api_gateway_operation_labels_value_error.
        _service.disable_retries()
        self.test_delete_zone_api_gateway_operation_labels_value_error()


class TestUpdateApiGatewayOperationLabels:
    """
    Test Class for update_api_gateway_operation_labels
    """

    @responses.activate
    def test_update_api_gateway_operation_labels_all_params(self):
        """
        update_api_gateway_operation_labels()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/operations/labels')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"operation_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415", "labels": [{"name": "cf-llm", "source": "managed"}]}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a ApiGatewayOperationsLabelsBulkInputSelectorInclude model
        api_gateway_operations_labels_bulk_input_selector_include_model = {}
        api_gateway_operations_labels_bulk_input_selector_include_model['operation_ids'] = ['f174e90a-fafe-4643-bbbc-4a0ed4fc8415']

        # Construct a dict representation of a ApiGatewayOperationsLabelsBulkInputSelector model
        api_gateway_operations_labels_bulk_input_selector_model = {}
        api_gateway_operations_labels_bulk_input_selector_model['include'] = api_gateway_operations_labels_bulk_input_selector_include_model

        # Construct a dict representation of a ApiGatewayOperationsLabelsBulkInputUser model
        api_gateway_operations_labels_bulk_input_user_model = {}
        api_gateway_operations_labels_bulk_input_user_model['labels'] = ['testString']

        # Construct a dict representation of a ApiGatewayOperationsLabelsBulkInputManaged model
        api_gateway_operations_labels_bulk_input_managed_model = {}
        api_gateway_operations_labels_bulk_input_managed_model['labels'] = ['testString']

        # Set up parameter values
        selector = api_gateway_operations_labels_bulk_input_selector_model
        user = api_gateway_operations_labels_bulk_input_user_model
        managed = api_gateway_operations_labels_bulk_input_managed_model

        # Invoke method
        response = _service.update_api_gateway_operation_labels(
            selector=selector,
            user=user,
            managed=managed,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['selector'] == api_gateway_operations_labels_bulk_input_selector_model
        assert req_body['user'] == api_gateway_operations_labels_bulk_input_user_model
        assert req_body['managed'] == api_gateway_operations_labels_bulk_input_managed_model

    def test_update_api_gateway_operation_labels_all_params_with_retries(self):
        # Enable retries and run test_update_api_gateway_operation_labels_all_params.
        _service.enable_retries()
        self.test_update_api_gateway_operation_labels_all_params()

        # Disable retries and run test_update_api_gateway_operation_labels_all_params.
        _service.disable_retries()
        self.test_update_api_gateway_operation_labels_all_params()

    @responses.activate
    def test_update_api_gateway_operation_labels_required_params(self):
        """
        test_update_api_gateway_operation_labels_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/operations/labels')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"operation_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415", "labels": [{"name": "cf-llm", "source": "managed"}]}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_api_gateway_operation_labels()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_api_gateway_operation_labels_required_params_with_retries(self):
        # Enable retries and run test_update_api_gateway_operation_labels_required_params.
        _service.enable_retries()
        self.test_update_api_gateway_operation_labels_required_params()

        # Disable retries and run test_update_api_gateway_operation_labels_required_params.
        _service.disable_retries()
        self.test_update_api_gateway_operation_labels_required_params()

    @responses.activate
    def test_update_api_gateway_operation_labels_value_error(self):
        """
        test_update_api_gateway_operation_labels_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/operations/labels')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"operation_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415", "labels": [{"name": "cf-llm", "source": "managed"}]}]}'
        responses.add(
            responses.POST,
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
                _service.update_api_gateway_operation_labels(**req_copy)

    def test_update_api_gateway_operation_labels_value_error_with_retries(self):
        # Enable retries and run test_update_api_gateway_operation_labels_value_error.
        _service.enable_retries()
        self.test_update_api_gateway_operation_labels_value_error()

        # Disable retries and run test_update_api_gateway_operation_labels_value_error.
        _service.disable_retries()
        self.test_update_api_gateway_operation_labels_value_error()


class TestCreateApiGatewayOperationLabels:
    """
    Test Class for create_api_gateway_operation_labels
    """

    @responses.activate
    def test_create_api_gateway_operation_labels_all_params(self):
        """
        create_api_gateway_operation_labels()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/operations/testString/labels')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"operation_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415", "labels": [{"name": "cf-llm", "source": "managed"}]}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        operation_id = 'testString'
        user = []
        managed = ['cf-llm']

        # Invoke method
        response = _service.create_api_gateway_operation_labels(
            operation_id,
            user=user,
            managed=managed,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['user'] == []
        assert req_body['managed'] == ['cf-llm']

    def test_create_api_gateway_operation_labels_all_params_with_retries(self):
        # Enable retries and run test_create_api_gateway_operation_labels_all_params.
        _service.enable_retries()
        self.test_create_api_gateway_operation_labels_all_params()

        # Disable retries and run test_create_api_gateway_operation_labels_all_params.
        _service.disable_retries()
        self.test_create_api_gateway_operation_labels_all_params()

    @responses.activate
    def test_create_api_gateway_operation_labels_required_params(self):
        """
        test_create_api_gateway_operation_labels_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/operations/testString/labels')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"operation_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415", "labels": [{"name": "cf-llm", "source": "managed"}]}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        operation_id = 'testString'

        # Invoke method
        response = _service.create_api_gateway_operation_labels(
            operation_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_api_gateway_operation_labels_required_params_with_retries(self):
        # Enable retries and run test_create_api_gateway_operation_labels_required_params.
        _service.enable_retries()
        self.test_create_api_gateway_operation_labels_required_params()

        # Disable retries and run test_create_api_gateway_operation_labels_required_params.
        _service.disable_retries()
        self.test_create_api_gateway_operation_labels_required_params()

    @responses.activate
    def test_create_api_gateway_operation_labels_value_error(self):
        """
        test_create_api_gateway_operation_labels_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/operations/testString/labels')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"operation_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415", "labels": [{"name": "cf-llm", "source": "managed"}]}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        operation_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "operation_id": operation_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_api_gateway_operation_labels(**req_copy)

    def test_create_api_gateway_operation_labels_value_error_with_retries(self):
        # Enable retries and run test_create_api_gateway_operation_labels_value_error.
        _service.enable_retries()
        self.test_create_api_gateway_operation_labels_value_error()

        # Disable retries and run test_create_api_gateway_operation_labels_value_error.
        _service.disable_retries()
        self.test_create_api_gateway_operation_labels_value_error()


class TestSetZoneApiGatewayOperationLabels:
    """
    Test Class for set_zone_api_gateway_operation_labels
    """

    @responses.activate
    def test_set_zone_api_gateway_operation_labels_all_params(self):
        """
        set_zone_api_gateway_operation_labels()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/operations/testString/labels')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"operation_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415", "labels": [{"name": "cf-llm", "source": "managed"}]}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        operation_id = 'testString'
        user = []
        managed = ['cf-llm']

        # Invoke method
        response = _service.set_zone_api_gateway_operation_labels(
            operation_id,
            user=user,
            managed=managed,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['user'] == []
        assert req_body['managed'] == ['cf-llm']

    def test_set_zone_api_gateway_operation_labels_all_params_with_retries(self):
        # Enable retries and run test_set_zone_api_gateway_operation_labels_all_params.
        _service.enable_retries()
        self.test_set_zone_api_gateway_operation_labels_all_params()

        # Disable retries and run test_set_zone_api_gateway_operation_labels_all_params.
        _service.disable_retries()
        self.test_set_zone_api_gateway_operation_labels_all_params()

    @responses.activate
    def test_set_zone_api_gateway_operation_labels_required_params(self):
        """
        test_set_zone_api_gateway_operation_labels_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/operations/testString/labels')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"operation_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415", "labels": [{"name": "cf-llm", "source": "managed"}]}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        operation_id = 'testString'

        # Invoke method
        response = _service.set_zone_api_gateway_operation_labels(
            operation_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_set_zone_api_gateway_operation_labels_required_params_with_retries(self):
        # Enable retries and run test_set_zone_api_gateway_operation_labels_required_params.
        _service.enable_retries()
        self.test_set_zone_api_gateway_operation_labels_required_params()

        # Disable retries and run test_set_zone_api_gateway_operation_labels_required_params.
        _service.disable_retries()
        self.test_set_zone_api_gateway_operation_labels_required_params()

    @responses.activate
    def test_set_zone_api_gateway_operation_labels_value_error(self):
        """
        test_set_zone_api_gateway_operation_labels_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/operations/testString/labels')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"operation_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415", "labels": [{"name": "cf-llm", "source": "managed"}]}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        operation_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "operation_id": operation_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.set_zone_api_gateway_operation_labels(**req_copy)

    def test_set_zone_api_gateway_operation_labels_value_error_with_retries(self):
        # Enable retries and run test_set_zone_api_gateway_operation_labels_value_error.
        _service.enable_retries()
        self.test_set_zone_api_gateway_operation_labels_value_error()

        # Disable retries and run test_set_zone_api_gateway_operation_labels_value_error.
        _service.disable_retries()
        self.test_set_zone_api_gateway_operation_labels_value_error()


class TestUnsetZoneApiGatewayOperationLabels:
    """
    Test Class for unset_zone_api_gateway_operation_labels
    """

    @responses.activate
    def test_unset_zone_api_gateway_operation_labels_all_params(self):
        """
        unset_zone_api_gateway_operation_labels()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/operations/testString/labels')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": "anyValue"}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        operation_id = 'testString'
        user = ['testString']
        managed = ['testString']

        # Invoke method
        response = _service.unset_zone_api_gateway_operation_labels(
            operation_id,
            user=user,
            managed=managed,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['user'] == ['testString']
        assert req_body['managed'] == ['testString']

    def test_unset_zone_api_gateway_operation_labels_all_params_with_retries(self):
        # Enable retries and run test_unset_zone_api_gateway_operation_labels_all_params.
        _service.enable_retries()
        self.test_unset_zone_api_gateway_operation_labels_all_params()

        # Disable retries and run test_unset_zone_api_gateway_operation_labels_all_params.
        _service.disable_retries()
        self.test_unset_zone_api_gateway_operation_labels_all_params()

    @responses.activate
    def test_unset_zone_api_gateway_operation_labels_value_error(self):
        """
        test_unset_zone_api_gateway_operation_labels_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/operations/testString/labels')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": "anyValue"}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        operation_id = 'testString'
        user = ['testString']
        managed = ['testString']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "operation_id": operation_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.unset_zone_api_gateway_operation_labels(**req_copy)

    def test_unset_zone_api_gateway_operation_labels_value_error_with_retries(self):
        # Enable retries and run test_unset_zone_api_gateway_operation_labels_value_error.
        _service.enable_retries()
        self.test_unset_zone_api_gateway_operation_labels_value_error()

        # Disable retries and run test_unset_zone_api_gateway_operation_labels_value_error.
        _service.disable_retries()
        self.test_unset_zone_api_gateway_operation_labels_value_error()


class TestGetZoneApiGatewayOperation:
    """
    Test Class for get_zone_api_gateway_operation
    """

    @responses.activate
    def test_get_zone_api_gateway_operation_all_params(self):
        """
        get_zone_api_gateway_operation()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/operations/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"operation_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415", "method": "POST", "host": "api.example.com", "endpoint": "/v1/messages"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        operation_id = 'testString'

        # Invoke method
        response = _service.get_zone_api_gateway_operation(
            operation_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_zone_api_gateway_operation_all_params_with_retries(self):
        # Enable retries and run test_get_zone_api_gateway_operation_all_params.
        _service.enable_retries()
        self.test_get_zone_api_gateway_operation_all_params()

        # Disable retries and run test_get_zone_api_gateway_operation_all_params.
        _service.disable_retries()
        self.test_get_zone_api_gateway_operation_all_params()

    @responses.activate
    def test_get_zone_api_gateway_operation_value_error(self):
        """
        test_get_zone_api_gateway_operation_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/operations/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"operation_id": "f174e90a-fafe-4643-bbbc-4a0ed4fc8415", "method": "POST", "host": "api.example.com", "endpoint": "/v1/messages"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        operation_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "operation_id": operation_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_zone_api_gateway_operation(**req_copy)

    def test_get_zone_api_gateway_operation_value_error_with_retries(self):
        # Enable retries and run test_get_zone_api_gateway_operation_value_error.
        _service.enable_retries()
        self.test_get_zone_api_gateway_operation_value_error()

        # Disable retries and run test_get_zone_api_gateway_operation_value_error.
        _service.disable_retries()
        self.test_get_zone_api_gateway_operation_value_error()


class TestDeleteZoneApiGatewayOperation:
    """
    Test Class for delete_zone_api_gateway_operation
    """

    @responses.activate
    def test_delete_zone_api_gateway_operation_all_params(self):
        """
        delete_zone_api_gateway_operation()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/operations/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        operation_id = 'testString'

        # Invoke method
        response = _service.delete_zone_api_gateway_operation(
            operation_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_zone_api_gateway_operation_all_params_with_retries(self):
        # Enable retries and run test_delete_zone_api_gateway_operation_all_params.
        _service.enable_retries()
        self.test_delete_zone_api_gateway_operation_all_params()

        # Disable retries and run test_delete_zone_api_gateway_operation_all_params.
        _service.disable_retries()
        self.test_delete_zone_api_gateway_operation_all_params()

    @responses.activate
    def test_delete_zone_api_gateway_operation_value_error(self):
        """
        test_delete_zone_api_gateway_operation_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/operations/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        operation_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "operation_id": operation_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_zone_api_gateway_operation(**req_copy)

    def test_delete_zone_api_gateway_operation_value_error_with_retries(self):
        # Enable retries and run test_delete_zone_api_gateway_operation_value_error.
        _service.enable_retries()
        self.test_delete_zone_api_gateway_operation_value_error()

        # Disable retries and run test_delete_zone_api_gateway_operation_value_error.
        _service.disable_retries()
        self.test_delete_zone_api_gateway_operation_value_error()


# endregion
##############################################################################
# End of Service: APIGatewayOperations
##############################################################################

##############################################################################
# Start of Service: APIGatewaySchemas
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

        service = AiSecurityForAppsV1.new_instance(
            crn=crn,
            zone_identifier=zone_identifier,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, AiSecurityForAppsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = AiSecurityForAppsV1.new_instance(
                crn=crn,
                zone_identifier=zone_identifier,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = AiSecurityForAppsV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='crn must be provided'):
            service = AiSecurityForAppsV1.new_instance(
                crn=None,
                zone_identifier=None,
            )


class TestGetApiGatewaySchemas:
    """
    Test Class for get_api_gateway_schemas
    """

    @responses.activate
    def test_get_api_gateway_schemas_all_params(self):
        """
        get_api_gateway_schemas()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/schemas')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"anyKey": "anyValue"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_api_gateway_schemas()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_api_gateway_schemas_all_params_with_retries(self):
        # Enable retries and run test_get_api_gateway_schemas_all_params.
        _service.enable_retries()
        self.test_get_api_gateway_schemas_all_params()

        # Disable retries and run test_get_api_gateway_schemas_all_params.
        _service.disable_retries()
        self.test_get_api_gateway_schemas_all_params()

    @responses.activate
    def test_get_api_gateway_schemas_value_error(self):
        """
        test_get_api_gateway_schemas_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/api_gateway/schemas')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"anyKey": "anyValue"}}'
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
                _service.get_api_gateway_schemas(**req_copy)

    def test_get_api_gateway_schemas_value_error_with_retries(self):
        # Enable retries and run test_get_api_gateway_schemas_value_error.
        _service.enable_retries()
        self.test_get_api_gateway_schemas_value_error()

        # Disable retries and run test_get_api_gateway_schemas_value_error.
        _service.disable_retries()
        self.test_get_api_gateway_schemas_value_error()


# endregion
##############################################################################
# End of Service: APIGatewaySchemas
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_AiSecuritySettingsRespResult:
    """
    Test Class for AiSecuritySettingsRespResult
    """

    def test_ai_security_settings_resp_result_serialization(self):
        """
        Test serialization/deserialization for AiSecuritySettingsRespResult
        """

        # Construct a json representation of a AiSecuritySettingsRespResult model
        ai_security_settings_resp_result_model_json = {}
        ai_security_settings_resp_result_model_json['enabled'] = False

        # Construct a model instance of AiSecuritySettingsRespResult by calling from_dict on the json representation
        ai_security_settings_resp_result_model = AiSecuritySettingsRespResult.from_dict(ai_security_settings_resp_result_model_json)
        assert ai_security_settings_resp_result_model != False

        # Construct a model instance of AiSecuritySettingsRespResult by calling from_dict on the json representation
        ai_security_settings_resp_result_model_dict = AiSecuritySettingsRespResult.from_dict(ai_security_settings_resp_result_model_json).__dict__
        ai_security_settings_resp_result_model2 = AiSecuritySettingsRespResult(**ai_security_settings_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert ai_security_settings_resp_result_model == ai_security_settings_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        ai_security_settings_resp_result_model_json2 = ai_security_settings_resp_result_model.to_dict()
        assert ai_security_settings_resp_result_model_json2 == ai_security_settings_resp_result_model_json


class TestModel_ApiGatewayOperationItemRespResult:
    """
    Test Class for ApiGatewayOperationItemRespResult
    """

    def test_api_gateway_operation_item_resp_result_serialization(self):
        """
        Test serialization/deserialization for ApiGatewayOperationItemRespResult
        """

        # Construct a json representation of a ApiGatewayOperationItemRespResult model
        api_gateway_operation_item_resp_result_model_json = {}
        api_gateway_operation_item_resp_result_model_json['operation_id'] = 'f174e90a-fafe-4643-bbbc-4a0ed4fc8415'
        api_gateway_operation_item_resp_result_model_json['method'] = 'POST'
        api_gateway_operation_item_resp_result_model_json['host'] = 'api.example.com'
        api_gateway_operation_item_resp_result_model_json['endpoint'] = '/v1/messages'

        # Construct a model instance of ApiGatewayOperationItemRespResult by calling from_dict on the json representation
        api_gateway_operation_item_resp_result_model = ApiGatewayOperationItemRespResult.from_dict(api_gateway_operation_item_resp_result_model_json)
        assert api_gateway_operation_item_resp_result_model != False

        # Construct a model instance of ApiGatewayOperationItemRespResult by calling from_dict on the json representation
        api_gateway_operation_item_resp_result_model_dict = ApiGatewayOperationItemRespResult.from_dict(api_gateway_operation_item_resp_result_model_json).__dict__
        api_gateway_operation_item_resp_result_model2 = ApiGatewayOperationItemRespResult(**api_gateway_operation_item_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert api_gateway_operation_item_resp_result_model == api_gateway_operation_item_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        api_gateway_operation_item_resp_result_model_json2 = api_gateway_operation_item_resp_result_model.to_dict()
        assert api_gateway_operation_item_resp_result_model_json2 == api_gateway_operation_item_resp_result_model_json


class TestModel_ApiGatewayOperationLabelRespResult:
    """
    Test Class for ApiGatewayOperationLabelRespResult
    """

    def test_api_gateway_operation_label_resp_result_serialization(self):
        """
        Test serialization/deserialization for ApiGatewayOperationLabelRespResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        api_gateway_operation_label_resp_result_labels_item_model = {}  # ApiGatewayOperationLabelRespResultLabelsItem
        api_gateway_operation_label_resp_result_labels_item_model['name'] = 'cf-llm'
        api_gateway_operation_label_resp_result_labels_item_model['source'] = 'managed'

        # Construct a json representation of a ApiGatewayOperationLabelRespResult model
        api_gateway_operation_label_resp_result_model_json = {}
        api_gateway_operation_label_resp_result_model_json['operation_id'] = 'f174e90a-fafe-4643-bbbc-4a0ed4fc8415'
        api_gateway_operation_label_resp_result_model_json['labels'] = [api_gateway_operation_label_resp_result_labels_item_model]

        # Construct a model instance of ApiGatewayOperationLabelRespResult by calling from_dict on the json representation
        api_gateway_operation_label_resp_result_model = ApiGatewayOperationLabelRespResult.from_dict(api_gateway_operation_label_resp_result_model_json)
        assert api_gateway_operation_label_resp_result_model != False

        # Construct a model instance of ApiGatewayOperationLabelRespResult by calling from_dict on the json representation
        api_gateway_operation_label_resp_result_model_dict = ApiGatewayOperationLabelRespResult.from_dict(api_gateway_operation_label_resp_result_model_json).__dict__
        api_gateway_operation_label_resp_result_model2 = ApiGatewayOperationLabelRespResult(**api_gateway_operation_label_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert api_gateway_operation_label_resp_result_model == api_gateway_operation_label_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        api_gateway_operation_label_resp_result_model_json2 = api_gateway_operation_label_resp_result_model.to_dict()
        assert api_gateway_operation_label_resp_result_model_json2 == api_gateway_operation_label_resp_result_model_json


class TestModel_ApiGatewayOperationLabelRespResultLabelsItem:
    """
    Test Class for ApiGatewayOperationLabelRespResultLabelsItem
    """

    def test_api_gateway_operation_label_resp_result_labels_item_serialization(self):
        """
        Test serialization/deserialization for ApiGatewayOperationLabelRespResultLabelsItem
        """

        # Construct a json representation of a ApiGatewayOperationLabelRespResultLabelsItem model
        api_gateway_operation_label_resp_result_labels_item_model_json = {}
        api_gateway_operation_label_resp_result_labels_item_model_json['name'] = 'cf-llm'
        api_gateway_operation_label_resp_result_labels_item_model_json['source'] = 'managed'

        # Construct a model instance of ApiGatewayOperationLabelRespResultLabelsItem by calling from_dict on the json representation
        api_gateway_operation_label_resp_result_labels_item_model = ApiGatewayOperationLabelRespResultLabelsItem.from_dict(api_gateway_operation_label_resp_result_labels_item_model_json)
        assert api_gateway_operation_label_resp_result_labels_item_model != False

        # Construct a model instance of ApiGatewayOperationLabelRespResultLabelsItem by calling from_dict on the json representation
        api_gateway_operation_label_resp_result_labels_item_model_dict = ApiGatewayOperationLabelRespResultLabelsItem.from_dict(api_gateway_operation_label_resp_result_labels_item_model_json).__dict__
        api_gateway_operation_label_resp_result_labels_item_model2 = ApiGatewayOperationLabelRespResultLabelsItem(**api_gateway_operation_label_resp_result_labels_item_model_dict)

        # Verify the model instances are equivalent
        assert api_gateway_operation_label_resp_result_labels_item_model == api_gateway_operation_label_resp_result_labels_item_model2

        # Convert model instance back to dict and verify no loss of data
        api_gateway_operation_label_resp_result_labels_item_model_json2 = api_gateway_operation_label_resp_result_labels_item_model.to_dict()
        assert api_gateway_operation_label_resp_result_labels_item_model_json2 == api_gateway_operation_label_resp_result_labels_item_model_json


class TestModel_ApiGatewayOperationsDeleteInputItem:
    """
    Test Class for ApiGatewayOperationsDeleteInputItem
    """

    def test_api_gateway_operations_delete_input_item_serialization(self):
        """
        Test serialization/deserialization for ApiGatewayOperationsDeleteInputItem
        """

        # Construct a json representation of a ApiGatewayOperationsDeleteInputItem model
        api_gateway_operations_delete_input_item_model_json = {}
        api_gateway_operations_delete_input_item_model_json['operation_id'] = 'f174e90a-fafe-4643-bbbc-4a0ed4fc8415'

        # Construct a model instance of ApiGatewayOperationsDeleteInputItem by calling from_dict on the json representation
        api_gateway_operations_delete_input_item_model = ApiGatewayOperationsDeleteInputItem.from_dict(api_gateway_operations_delete_input_item_model_json)
        assert api_gateway_operations_delete_input_item_model != False

        # Construct a model instance of ApiGatewayOperationsDeleteInputItem by calling from_dict on the json representation
        api_gateway_operations_delete_input_item_model_dict = ApiGatewayOperationsDeleteInputItem.from_dict(api_gateway_operations_delete_input_item_model_json).__dict__
        api_gateway_operations_delete_input_item_model2 = ApiGatewayOperationsDeleteInputItem(**api_gateway_operations_delete_input_item_model_dict)

        # Verify the model instances are equivalent
        assert api_gateway_operations_delete_input_item_model == api_gateway_operations_delete_input_item_model2

        # Convert model instance back to dict and verify no loss of data
        api_gateway_operations_delete_input_item_model_json2 = api_gateway_operations_delete_input_item_model.to_dict()
        assert api_gateway_operations_delete_input_item_model_json2 == api_gateway_operations_delete_input_item_model_json


class TestModel_ApiGatewayOperationsLabelsBulkDeleteInputManaged:
    """
    Test Class for ApiGatewayOperationsLabelsBulkDeleteInputManaged
    """

    def test_api_gateway_operations_labels_bulk_delete_input_managed_serialization(self):
        """
        Test serialization/deserialization for ApiGatewayOperationsLabelsBulkDeleteInputManaged
        """

        # Construct a json representation of a ApiGatewayOperationsLabelsBulkDeleteInputManaged model
        api_gateway_operations_labels_bulk_delete_input_managed_model_json = {}
        api_gateway_operations_labels_bulk_delete_input_managed_model_json['labels'] = ['testString']

        # Construct a model instance of ApiGatewayOperationsLabelsBulkDeleteInputManaged by calling from_dict on the json representation
        api_gateway_operations_labels_bulk_delete_input_managed_model = ApiGatewayOperationsLabelsBulkDeleteInputManaged.from_dict(api_gateway_operations_labels_bulk_delete_input_managed_model_json)
        assert api_gateway_operations_labels_bulk_delete_input_managed_model != False

        # Construct a model instance of ApiGatewayOperationsLabelsBulkDeleteInputManaged by calling from_dict on the json representation
        api_gateway_operations_labels_bulk_delete_input_managed_model_dict = ApiGatewayOperationsLabelsBulkDeleteInputManaged.from_dict(api_gateway_operations_labels_bulk_delete_input_managed_model_json).__dict__
        api_gateway_operations_labels_bulk_delete_input_managed_model2 = ApiGatewayOperationsLabelsBulkDeleteInputManaged(**api_gateway_operations_labels_bulk_delete_input_managed_model_dict)

        # Verify the model instances are equivalent
        assert api_gateway_operations_labels_bulk_delete_input_managed_model == api_gateway_operations_labels_bulk_delete_input_managed_model2

        # Convert model instance back to dict and verify no loss of data
        api_gateway_operations_labels_bulk_delete_input_managed_model_json2 = api_gateway_operations_labels_bulk_delete_input_managed_model.to_dict()
        assert api_gateway_operations_labels_bulk_delete_input_managed_model_json2 == api_gateway_operations_labels_bulk_delete_input_managed_model_json


class TestModel_ApiGatewayOperationsLabelsBulkDeleteInputSelector:
    """
    Test Class for ApiGatewayOperationsLabelsBulkDeleteInputSelector
    """

    def test_api_gateway_operations_labels_bulk_delete_input_selector_serialization(self):
        """
        Test serialization/deserialization for ApiGatewayOperationsLabelsBulkDeleteInputSelector
        """

        # Construct dict forms of any model objects needed in order to build this model.

        api_gateway_operations_labels_bulk_delete_input_selector_include_model = {}  # ApiGatewayOperationsLabelsBulkDeleteInputSelectorInclude
        api_gateway_operations_labels_bulk_delete_input_selector_include_model['operation_ids'] = ['f174e90a-fafe-4643-bbbc-4a0ed4fc8415']

        # Construct a json representation of a ApiGatewayOperationsLabelsBulkDeleteInputSelector model
        api_gateway_operations_labels_bulk_delete_input_selector_model_json = {}
        api_gateway_operations_labels_bulk_delete_input_selector_model_json['include'] = api_gateway_operations_labels_bulk_delete_input_selector_include_model

        # Construct a model instance of ApiGatewayOperationsLabelsBulkDeleteInputSelector by calling from_dict on the json representation
        api_gateway_operations_labels_bulk_delete_input_selector_model = ApiGatewayOperationsLabelsBulkDeleteInputSelector.from_dict(api_gateway_operations_labels_bulk_delete_input_selector_model_json)
        assert api_gateway_operations_labels_bulk_delete_input_selector_model != False

        # Construct a model instance of ApiGatewayOperationsLabelsBulkDeleteInputSelector by calling from_dict on the json representation
        api_gateway_operations_labels_bulk_delete_input_selector_model_dict = ApiGatewayOperationsLabelsBulkDeleteInputSelector.from_dict(api_gateway_operations_labels_bulk_delete_input_selector_model_json).__dict__
        api_gateway_operations_labels_bulk_delete_input_selector_model2 = ApiGatewayOperationsLabelsBulkDeleteInputSelector(**api_gateway_operations_labels_bulk_delete_input_selector_model_dict)

        # Verify the model instances are equivalent
        assert api_gateway_operations_labels_bulk_delete_input_selector_model == api_gateway_operations_labels_bulk_delete_input_selector_model2

        # Convert model instance back to dict and verify no loss of data
        api_gateway_operations_labels_bulk_delete_input_selector_model_json2 = api_gateway_operations_labels_bulk_delete_input_selector_model.to_dict()
        assert api_gateway_operations_labels_bulk_delete_input_selector_model_json2 == api_gateway_operations_labels_bulk_delete_input_selector_model_json


class TestModel_ApiGatewayOperationsLabelsBulkDeleteInputSelectorInclude:
    """
    Test Class for ApiGatewayOperationsLabelsBulkDeleteInputSelectorInclude
    """

    def test_api_gateway_operations_labels_bulk_delete_input_selector_include_serialization(self):
        """
        Test serialization/deserialization for ApiGatewayOperationsLabelsBulkDeleteInputSelectorInclude
        """

        # Construct a json representation of a ApiGatewayOperationsLabelsBulkDeleteInputSelectorInclude model
        api_gateway_operations_labels_bulk_delete_input_selector_include_model_json = {}
        api_gateway_operations_labels_bulk_delete_input_selector_include_model_json['operation_ids'] = ['f174e90a-fafe-4643-bbbc-4a0ed4fc8415']

        # Construct a model instance of ApiGatewayOperationsLabelsBulkDeleteInputSelectorInclude by calling from_dict on the json representation
        api_gateway_operations_labels_bulk_delete_input_selector_include_model = ApiGatewayOperationsLabelsBulkDeleteInputSelectorInclude.from_dict(api_gateway_operations_labels_bulk_delete_input_selector_include_model_json)
        assert api_gateway_operations_labels_bulk_delete_input_selector_include_model != False

        # Construct a model instance of ApiGatewayOperationsLabelsBulkDeleteInputSelectorInclude by calling from_dict on the json representation
        api_gateway_operations_labels_bulk_delete_input_selector_include_model_dict = ApiGatewayOperationsLabelsBulkDeleteInputSelectorInclude.from_dict(api_gateway_operations_labels_bulk_delete_input_selector_include_model_json).__dict__
        api_gateway_operations_labels_bulk_delete_input_selector_include_model2 = ApiGatewayOperationsLabelsBulkDeleteInputSelectorInclude(**api_gateway_operations_labels_bulk_delete_input_selector_include_model_dict)

        # Verify the model instances are equivalent
        assert api_gateway_operations_labels_bulk_delete_input_selector_include_model == api_gateway_operations_labels_bulk_delete_input_selector_include_model2

        # Convert model instance back to dict and verify no loss of data
        api_gateway_operations_labels_bulk_delete_input_selector_include_model_json2 = api_gateway_operations_labels_bulk_delete_input_selector_include_model.to_dict()
        assert api_gateway_operations_labels_bulk_delete_input_selector_include_model_json2 == api_gateway_operations_labels_bulk_delete_input_selector_include_model_json


class TestModel_ApiGatewayOperationsLabelsBulkDeleteInputUser:
    """
    Test Class for ApiGatewayOperationsLabelsBulkDeleteInputUser
    """

    def test_api_gateway_operations_labels_bulk_delete_input_user_serialization(self):
        """
        Test serialization/deserialization for ApiGatewayOperationsLabelsBulkDeleteInputUser
        """

        # Construct a json representation of a ApiGatewayOperationsLabelsBulkDeleteInputUser model
        api_gateway_operations_labels_bulk_delete_input_user_model_json = {}
        api_gateway_operations_labels_bulk_delete_input_user_model_json['labels'] = ['testString']

        # Construct a model instance of ApiGatewayOperationsLabelsBulkDeleteInputUser by calling from_dict on the json representation
        api_gateway_operations_labels_bulk_delete_input_user_model = ApiGatewayOperationsLabelsBulkDeleteInputUser.from_dict(api_gateway_operations_labels_bulk_delete_input_user_model_json)
        assert api_gateway_operations_labels_bulk_delete_input_user_model != False

        # Construct a model instance of ApiGatewayOperationsLabelsBulkDeleteInputUser by calling from_dict on the json representation
        api_gateway_operations_labels_bulk_delete_input_user_model_dict = ApiGatewayOperationsLabelsBulkDeleteInputUser.from_dict(api_gateway_operations_labels_bulk_delete_input_user_model_json).__dict__
        api_gateway_operations_labels_bulk_delete_input_user_model2 = ApiGatewayOperationsLabelsBulkDeleteInputUser(**api_gateway_operations_labels_bulk_delete_input_user_model_dict)

        # Verify the model instances are equivalent
        assert api_gateway_operations_labels_bulk_delete_input_user_model == api_gateway_operations_labels_bulk_delete_input_user_model2

        # Convert model instance back to dict and verify no loss of data
        api_gateway_operations_labels_bulk_delete_input_user_model_json2 = api_gateway_operations_labels_bulk_delete_input_user_model.to_dict()
        assert api_gateway_operations_labels_bulk_delete_input_user_model_json2 == api_gateway_operations_labels_bulk_delete_input_user_model_json


class TestModel_ApiGatewayOperationsLabelsBulkInputManaged:
    """
    Test Class for ApiGatewayOperationsLabelsBulkInputManaged
    """

    def test_api_gateway_operations_labels_bulk_input_managed_serialization(self):
        """
        Test serialization/deserialization for ApiGatewayOperationsLabelsBulkInputManaged
        """

        # Construct a json representation of a ApiGatewayOperationsLabelsBulkInputManaged model
        api_gateway_operations_labels_bulk_input_managed_model_json = {}
        api_gateway_operations_labels_bulk_input_managed_model_json['labels'] = ['testString']

        # Construct a model instance of ApiGatewayOperationsLabelsBulkInputManaged by calling from_dict on the json representation
        api_gateway_operations_labels_bulk_input_managed_model = ApiGatewayOperationsLabelsBulkInputManaged.from_dict(api_gateway_operations_labels_bulk_input_managed_model_json)
        assert api_gateway_operations_labels_bulk_input_managed_model != False

        # Construct a model instance of ApiGatewayOperationsLabelsBulkInputManaged by calling from_dict on the json representation
        api_gateway_operations_labels_bulk_input_managed_model_dict = ApiGatewayOperationsLabelsBulkInputManaged.from_dict(api_gateway_operations_labels_bulk_input_managed_model_json).__dict__
        api_gateway_operations_labels_bulk_input_managed_model2 = ApiGatewayOperationsLabelsBulkInputManaged(**api_gateway_operations_labels_bulk_input_managed_model_dict)

        # Verify the model instances are equivalent
        assert api_gateway_operations_labels_bulk_input_managed_model == api_gateway_operations_labels_bulk_input_managed_model2

        # Convert model instance back to dict and verify no loss of data
        api_gateway_operations_labels_bulk_input_managed_model_json2 = api_gateway_operations_labels_bulk_input_managed_model.to_dict()
        assert api_gateway_operations_labels_bulk_input_managed_model_json2 == api_gateway_operations_labels_bulk_input_managed_model_json


class TestModel_ApiGatewayOperationsLabelsBulkInputSelector:
    """
    Test Class for ApiGatewayOperationsLabelsBulkInputSelector
    """

    def test_api_gateway_operations_labels_bulk_input_selector_serialization(self):
        """
        Test serialization/deserialization for ApiGatewayOperationsLabelsBulkInputSelector
        """

        # Construct dict forms of any model objects needed in order to build this model.

        api_gateway_operations_labels_bulk_input_selector_include_model = {}  # ApiGatewayOperationsLabelsBulkInputSelectorInclude
        api_gateway_operations_labels_bulk_input_selector_include_model['operation_ids'] = ['f174e90a-fafe-4643-bbbc-4a0ed4fc8415']

        # Construct a json representation of a ApiGatewayOperationsLabelsBulkInputSelector model
        api_gateway_operations_labels_bulk_input_selector_model_json = {}
        api_gateway_operations_labels_bulk_input_selector_model_json['include'] = api_gateway_operations_labels_bulk_input_selector_include_model

        # Construct a model instance of ApiGatewayOperationsLabelsBulkInputSelector by calling from_dict on the json representation
        api_gateway_operations_labels_bulk_input_selector_model = ApiGatewayOperationsLabelsBulkInputSelector.from_dict(api_gateway_operations_labels_bulk_input_selector_model_json)
        assert api_gateway_operations_labels_bulk_input_selector_model != False

        # Construct a model instance of ApiGatewayOperationsLabelsBulkInputSelector by calling from_dict on the json representation
        api_gateway_operations_labels_bulk_input_selector_model_dict = ApiGatewayOperationsLabelsBulkInputSelector.from_dict(api_gateway_operations_labels_bulk_input_selector_model_json).__dict__
        api_gateway_operations_labels_bulk_input_selector_model2 = ApiGatewayOperationsLabelsBulkInputSelector(**api_gateway_operations_labels_bulk_input_selector_model_dict)

        # Verify the model instances are equivalent
        assert api_gateway_operations_labels_bulk_input_selector_model == api_gateway_operations_labels_bulk_input_selector_model2

        # Convert model instance back to dict and verify no loss of data
        api_gateway_operations_labels_bulk_input_selector_model_json2 = api_gateway_operations_labels_bulk_input_selector_model.to_dict()
        assert api_gateway_operations_labels_bulk_input_selector_model_json2 == api_gateway_operations_labels_bulk_input_selector_model_json


class TestModel_ApiGatewayOperationsLabelsBulkInputSelectorInclude:
    """
    Test Class for ApiGatewayOperationsLabelsBulkInputSelectorInclude
    """

    def test_api_gateway_operations_labels_bulk_input_selector_include_serialization(self):
        """
        Test serialization/deserialization for ApiGatewayOperationsLabelsBulkInputSelectorInclude
        """

        # Construct a json representation of a ApiGatewayOperationsLabelsBulkInputSelectorInclude model
        api_gateway_operations_labels_bulk_input_selector_include_model_json = {}
        api_gateway_operations_labels_bulk_input_selector_include_model_json['operation_ids'] = ['f174e90a-fafe-4643-bbbc-4a0ed4fc8415']

        # Construct a model instance of ApiGatewayOperationsLabelsBulkInputSelectorInclude by calling from_dict on the json representation
        api_gateway_operations_labels_bulk_input_selector_include_model = ApiGatewayOperationsLabelsBulkInputSelectorInclude.from_dict(api_gateway_operations_labels_bulk_input_selector_include_model_json)
        assert api_gateway_operations_labels_bulk_input_selector_include_model != False

        # Construct a model instance of ApiGatewayOperationsLabelsBulkInputSelectorInclude by calling from_dict on the json representation
        api_gateway_operations_labels_bulk_input_selector_include_model_dict = ApiGatewayOperationsLabelsBulkInputSelectorInclude.from_dict(api_gateway_operations_labels_bulk_input_selector_include_model_json).__dict__
        api_gateway_operations_labels_bulk_input_selector_include_model2 = ApiGatewayOperationsLabelsBulkInputSelectorInclude(**api_gateway_operations_labels_bulk_input_selector_include_model_dict)

        # Verify the model instances are equivalent
        assert api_gateway_operations_labels_bulk_input_selector_include_model == api_gateway_operations_labels_bulk_input_selector_include_model2

        # Convert model instance back to dict and verify no loss of data
        api_gateway_operations_labels_bulk_input_selector_include_model_json2 = api_gateway_operations_labels_bulk_input_selector_include_model.to_dict()
        assert api_gateway_operations_labels_bulk_input_selector_include_model_json2 == api_gateway_operations_labels_bulk_input_selector_include_model_json


class TestModel_ApiGatewayOperationsLabelsBulkInputUser:
    """
    Test Class for ApiGatewayOperationsLabelsBulkInputUser
    """

    def test_api_gateway_operations_labels_bulk_input_user_serialization(self):
        """
        Test serialization/deserialization for ApiGatewayOperationsLabelsBulkInputUser
        """

        # Construct a json representation of a ApiGatewayOperationsLabelsBulkInputUser model
        api_gateway_operations_labels_bulk_input_user_model_json = {}
        api_gateway_operations_labels_bulk_input_user_model_json['labels'] = ['testString']

        # Construct a model instance of ApiGatewayOperationsLabelsBulkInputUser by calling from_dict on the json representation
        api_gateway_operations_labels_bulk_input_user_model = ApiGatewayOperationsLabelsBulkInputUser.from_dict(api_gateway_operations_labels_bulk_input_user_model_json)
        assert api_gateway_operations_labels_bulk_input_user_model != False

        # Construct a model instance of ApiGatewayOperationsLabelsBulkInputUser by calling from_dict on the json representation
        api_gateway_operations_labels_bulk_input_user_model_dict = ApiGatewayOperationsLabelsBulkInputUser.from_dict(api_gateway_operations_labels_bulk_input_user_model_json).__dict__
        api_gateway_operations_labels_bulk_input_user_model2 = ApiGatewayOperationsLabelsBulkInputUser(**api_gateway_operations_labels_bulk_input_user_model_dict)

        # Verify the model instances are equivalent
        assert api_gateway_operations_labels_bulk_input_user_model == api_gateway_operations_labels_bulk_input_user_model2

        # Convert model instance back to dict and verify no loss of data
        api_gateway_operations_labels_bulk_input_user_model_json2 = api_gateway_operations_labels_bulk_input_user_model.to_dict()
        assert api_gateway_operations_labels_bulk_input_user_model_json2 == api_gateway_operations_labels_bulk_input_user_model_json


class TestModel_ApiGatewayOperationsLabelsRespResultItem:
    """
    Test Class for ApiGatewayOperationsLabelsRespResultItem
    """

    def test_api_gateway_operations_labels_resp_result_item_serialization(self):
        """
        Test serialization/deserialization for ApiGatewayOperationsLabelsRespResultItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        api_gateway_operations_labels_resp_result_item_labels_item_model = {}  # ApiGatewayOperationsLabelsRespResultItemLabelsItem
        api_gateway_operations_labels_resp_result_item_labels_item_model['name'] = 'cf-llm'
        api_gateway_operations_labels_resp_result_item_labels_item_model['source'] = 'managed'

        # Construct a json representation of a ApiGatewayOperationsLabelsRespResultItem model
        api_gateway_operations_labels_resp_result_item_model_json = {}
        api_gateway_operations_labels_resp_result_item_model_json['operation_id'] = 'f174e90a-fafe-4643-bbbc-4a0ed4fc8415'
        api_gateway_operations_labels_resp_result_item_model_json['labels'] = [api_gateway_operations_labels_resp_result_item_labels_item_model]

        # Construct a model instance of ApiGatewayOperationsLabelsRespResultItem by calling from_dict on the json representation
        api_gateway_operations_labels_resp_result_item_model = ApiGatewayOperationsLabelsRespResultItem.from_dict(api_gateway_operations_labels_resp_result_item_model_json)
        assert api_gateway_operations_labels_resp_result_item_model != False

        # Construct a model instance of ApiGatewayOperationsLabelsRespResultItem by calling from_dict on the json representation
        api_gateway_operations_labels_resp_result_item_model_dict = ApiGatewayOperationsLabelsRespResultItem.from_dict(api_gateway_operations_labels_resp_result_item_model_json).__dict__
        api_gateway_operations_labels_resp_result_item_model2 = ApiGatewayOperationsLabelsRespResultItem(**api_gateway_operations_labels_resp_result_item_model_dict)

        # Verify the model instances are equivalent
        assert api_gateway_operations_labels_resp_result_item_model == api_gateway_operations_labels_resp_result_item_model2

        # Convert model instance back to dict and verify no loss of data
        api_gateway_operations_labels_resp_result_item_model_json2 = api_gateway_operations_labels_resp_result_item_model.to_dict()
        assert api_gateway_operations_labels_resp_result_item_model_json2 == api_gateway_operations_labels_resp_result_item_model_json


class TestModel_ApiGatewayOperationsLabelsRespResultItemLabelsItem:
    """
    Test Class for ApiGatewayOperationsLabelsRespResultItemLabelsItem
    """

    def test_api_gateway_operations_labels_resp_result_item_labels_item_serialization(self):
        """
        Test serialization/deserialization for ApiGatewayOperationsLabelsRespResultItemLabelsItem
        """

        # Construct a json representation of a ApiGatewayOperationsLabelsRespResultItemLabelsItem model
        api_gateway_operations_labels_resp_result_item_labels_item_model_json = {}
        api_gateway_operations_labels_resp_result_item_labels_item_model_json['name'] = 'cf-llm'
        api_gateway_operations_labels_resp_result_item_labels_item_model_json['source'] = 'managed'

        # Construct a model instance of ApiGatewayOperationsLabelsRespResultItemLabelsItem by calling from_dict on the json representation
        api_gateway_operations_labels_resp_result_item_labels_item_model = ApiGatewayOperationsLabelsRespResultItemLabelsItem.from_dict(api_gateway_operations_labels_resp_result_item_labels_item_model_json)
        assert api_gateway_operations_labels_resp_result_item_labels_item_model != False

        # Construct a model instance of ApiGatewayOperationsLabelsRespResultItemLabelsItem by calling from_dict on the json representation
        api_gateway_operations_labels_resp_result_item_labels_item_model_dict = ApiGatewayOperationsLabelsRespResultItemLabelsItem.from_dict(api_gateway_operations_labels_resp_result_item_labels_item_model_json).__dict__
        api_gateway_operations_labels_resp_result_item_labels_item_model2 = ApiGatewayOperationsLabelsRespResultItemLabelsItem(**api_gateway_operations_labels_resp_result_item_labels_item_model_dict)

        # Verify the model instances are equivalent
        assert api_gateway_operations_labels_resp_result_item_labels_item_model == api_gateway_operations_labels_resp_result_item_labels_item_model2

        # Convert model instance back to dict and verify no loss of data
        api_gateway_operations_labels_resp_result_item_labels_item_model_json2 = api_gateway_operations_labels_resp_result_item_labels_item_model.to_dict()
        assert api_gateway_operations_labels_resp_result_item_labels_item_model_json2 == api_gateway_operations_labels_resp_result_item_labels_item_model_json


class TestModel_ApiGatewayOperationsListRespResultItem:
    """
    Test Class for ApiGatewayOperationsListRespResultItem
    """

    def test_api_gateway_operations_list_resp_result_item_serialization(self):
        """
        Test serialization/deserialization for ApiGatewayOperationsListRespResultItem
        """

        # Construct a json representation of a ApiGatewayOperationsListRespResultItem model
        api_gateway_operations_list_resp_result_item_model_json = {}
        api_gateway_operations_list_resp_result_item_model_json['operation_id'] = 'test-fafe-4643-bbbc-example'
        api_gateway_operations_list_resp_result_item_model_json['method'] = 'POST'
        api_gateway_operations_list_resp_result_item_model_json['host'] = 'api.example.com'
        api_gateway_operations_list_resp_result_item_model_json['endpoint'] = '/v1/messages'
        api_gateway_operations_list_resp_result_item_model_json['last_updated'] = '2024-01-01T00:00:00Z'

        # Construct a model instance of ApiGatewayOperationsListRespResultItem by calling from_dict on the json representation
        api_gateway_operations_list_resp_result_item_model = ApiGatewayOperationsListRespResultItem.from_dict(api_gateway_operations_list_resp_result_item_model_json)
        assert api_gateway_operations_list_resp_result_item_model != False

        # Construct a model instance of ApiGatewayOperationsListRespResultItem by calling from_dict on the json representation
        api_gateway_operations_list_resp_result_item_model_dict = ApiGatewayOperationsListRespResultItem.from_dict(api_gateway_operations_list_resp_result_item_model_json).__dict__
        api_gateway_operations_list_resp_result_item_model2 = ApiGatewayOperationsListRespResultItem(**api_gateway_operations_list_resp_result_item_model_dict)

        # Verify the model instances are equivalent
        assert api_gateway_operations_list_resp_result_item_model == api_gateway_operations_list_resp_result_item_model2

        # Convert model instance back to dict and verify no loss of data
        api_gateway_operations_list_resp_result_item_model_json2 = api_gateway_operations_list_resp_result_item_model.to_dict()
        assert api_gateway_operations_list_resp_result_item_model_json2 == api_gateway_operations_list_resp_result_item_model_json


class TestModel_ApiGatewayOperationsRespResultItem:
    """
    Test Class for ApiGatewayOperationsRespResultItem
    """

    def test_api_gateway_operations_resp_result_item_serialization(self):
        """
        Test serialization/deserialization for ApiGatewayOperationsRespResultItem
        """

        # Construct a json representation of a ApiGatewayOperationsRespResultItem model
        api_gateway_operations_resp_result_item_model_json = {}
        api_gateway_operations_resp_result_item_model_json['operation_id'] = 'f174e90a-fafe-4643-bbbc-4a0ed4fc8415'
        api_gateway_operations_resp_result_item_model_json['method'] = 'POST'
        api_gateway_operations_resp_result_item_model_json['host'] = 'api.example.com'
        api_gateway_operations_resp_result_item_model_json['endpoint'] = '/v1/messages'

        # Construct a model instance of ApiGatewayOperationsRespResultItem by calling from_dict on the json representation
        api_gateway_operations_resp_result_item_model = ApiGatewayOperationsRespResultItem.from_dict(api_gateway_operations_resp_result_item_model_json)
        assert api_gateway_operations_resp_result_item_model != False

        # Construct a model instance of ApiGatewayOperationsRespResultItem by calling from_dict on the json representation
        api_gateway_operations_resp_result_item_model_dict = ApiGatewayOperationsRespResultItem.from_dict(api_gateway_operations_resp_result_item_model_json).__dict__
        api_gateway_operations_resp_result_item_model2 = ApiGatewayOperationsRespResultItem(**api_gateway_operations_resp_result_item_model_dict)

        # Verify the model instances are equivalent
        assert api_gateway_operations_resp_result_item_model == api_gateway_operations_resp_result_item_model2

        # Convert model instance back to dict and verify no loss of data
        api_gateway_operations_resp_result_item_model_json2 = api_gateway_operations_resp_result_item_model.to_dict()
        assert api_gateway_operations_resp_result_item_model_json2 == api_gateway_operations_resp_result_item_model_json


class TestModel_DiscoveryOperationFeatures:
    """
    Test Class for DiscoveryOperationFeatures
    """

    def test_discovery_operation_features_serialization(self):
        """
        Test serialization/deserialization for DiscoveryOperationFeatures
        """

        # Construct dict forms of any model objects needed in order to build this model.

        discovery_operation_features_traffic_stats_model = {}  # DiscoveryOperationFeaturesTrafficStats
        discovery_operation_features_traffic_stats_model['last_updated'] = '2019-01-01T12:00:00Z'
        discovery_operation_features_traffic_stats_model['period_seconds'] = 38
        discovery_operation_features_traffic_stats_model['requests'] = 72.5

        # Construct a json representation of a DiscoveryOperationFeatures model
        discovery_operation_features_model_json = {}
        discovery_operation_features_model_json['traffic_stats'] = discovery_operation_features_traffic_stats_model

        # Construct a model instance of DiscoveryOperationFeatures by calling from_dict on the json representation
        discovery_operation_features_model = DiscoveryOperationFeatures.from_dict(discovery_operation_features_model_json)
        assert discovery_operation_features_model != False

        # Construct a model instance of DiscoveryOperationFeatures by calling from_dict on the json representation
        discovery_operation_features_model_dict = DiscoveryOperationFeatures.from_dict(discovery_operation_features_model_json).__dict__
        discovery_operation_features_model2 = DiscoveryOperationFeatures(**discovery_operation_features_model_dict)

        # Verify the model instances are equivalent
        assert discovery_operation_features_model == discovery_operation_features_model2

        # Convert model instance back to dict and verify no loss of data
        discovery_operation_features_model_json2 = discovery_operation_features_model.to_dict()
        assert discovery_operation_features_model_json2 == discovery_operation_features_model_json


class TestModel_DiscoveryOperationFeaturesTrafficStats:
    """
    Test Class for DiscoveryOperationFeaturesTrafficStats
    """

    def test_discovery_operation_features_traffic_stats_serialization(self):
        """
        Test serialization/deserialization for DiscoveryOperationFeaturesTrafficStats
        """

        # Construct a json representation of a DiscoveryOperationFeaturesTrafficStats model
        discovery_operation_features_traffic_stats_model_json = {}
        discovery_operation_features_traffic_stats_model_json['last_updated'] = '2019-01-01T12:00:00Z'
        discovery_operation_features_traffic_stats_model_json['period_seconds'] = 38
        discovery_operation_features_traffic_stats_model_json['requests'] = 72.5

        # Construct a model instance of DiscoveryOperationFeaturesTrafficStats by calling from_dict on the json representation
        discovery_operation_features_traffic_stats_model = DiscoveryOperationFeaturesTrafficStats.from_dict(discovery_operation_features_traffic_stats_model_json)
        assert discovery_operation_features_traffic_stats_model != False

        # Construct a model instance of DiscoveryOperationFeaturesTrafficStats by calling from_dict on the json representation
        discovery_operation_features_traffic_stats_model_dict = DiscoveryOperationFeaturesTrafficStats.from_dict(discovery_operation_features_traffic_stats_model_json).__dict__
        discovery_operation_features_traffic_stats_model2 = DiscoveryOperationFeaturesTrafficStats(**discovery_operation_features_traffic_stats_model_dict)

        # Verify the model instances are equivalent
        assert discovery_operation_features_traffic_stats_model == discovery_operation_features_traffic_stats_model2

        # Convert model instance back to dict and verify no loss of data
        discovery_operation_features_traffic_stats_model_json2 = discovery_operation_features_traffic_stats_model.to_dict()
        assert discovery_operation_features_traffic_stats_model_json2 == discovery_operation_features_traffic_stats_model_json


class TestModel_AiSecuritySettingsResp:
    """
    Test Class for AiSecuritySettingsResp
    """

    def test_ai_security_settings_resp_serialization(self):
        """
        Test serialization/deserialization for AiSecuritySettingsResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        ai_security_settings_resp_result_model = {}  # AiSecuritySettingsRespResult
        ai_security_settings_resp_result_model['enabled'] = False

        # Construct a json representation of a AiSecuritySettingsResp model
        ai_security_settings_resp_model_json = {}
        ai_security_settings_resp_model_json['success'] = True
        ai_security_settings_resp_model_json['errors'] = [['testString']]
        ai_security_settings_resp_model_json['messages'] = [['testString']]
        ai_security_settings_resp_model_json['result'] = ai_security_settings_resp_result_model

        # Construct a model instance of AiSecuritySettingsResp by calling from_dict on the json representation
        ai_security_settings_resp_model = AiSecuritySettingsResp.from_dict(ai_security_settings_resp_model_json)
        assert ai_security_settings_resp_model != False

        # Construct a model instance of AiSecuritySettingsResp by calling from_dict on the json representation
        ai_security_settings_resp_model_dict = AiSecuritySettingsResp.from_dict(ai_security_settings_resp_model_json).__dict__
        ai_security_settings_resp_model2 = AiSecuritySettingsResp(**ai_security_settings_resp_model_dict)

        # Verify the model instances are equivalent
        assert ai_security_settings_resp_model == ai_security_settings_resp_model2

        # Convert model instance back to dict and verify no loss of data
        ai_security_settings_resp_model_json2 = ai_security_settings_resp_model.to_dict()
        assert ai_security_settings_resp_model_json2 == ai_security_settings_resp_model_json


class TestModel_ApiGatewayDiscoveryResp:
    """
    Test Class for ApiGatewayDiscoveryResp
    """

    def test_api_gateway_discovery_resp_serialization(self):
        """
        Test serialization/deserialization for ApiGatewayDiscoveryResp
        """

        # Construct a json representation of a ApiGatewayDiscoveryResp model
        api_gateway_discovery_resp_model_json = {}
        api_gateway_discovery_resp_model_json['success'] = True
        api_gateway_discovery_resp_model_json['errors'] = [['testString']]
        api_gateway_discovery_resp_model_json['messages'] = [['testString']]
        api_gateway_discovery_resp_model_json['result'] = {'anyKey': 'anyValue'}

        # Construct a model instance of ApiGatewayDiscoveryResp by calling from_dict on the json representation
        api_gateway_discovery_resp_model = ApiGatewayDiscoveryResp.from_dict(api_gateway_discovery_resp_model_json)
        assert api_gateway_discovery_resp_model != False

        # Construct a model instance of ApiGatewayDiscoveryResp by calling from_dict on the json representation
        api_gateway_discovery_resp_model_dict = ApiGatewayDiscoveryResp.from_dict(api_gateway_discovery_resp_model_json).__dict__
        api_gateway_discovery_resp_model2 = ApiGatewayDiscoveryResp(**api_gateway_discovery_resp_model_dict)

        # Verify the model instances are equivalent
        assert api_gateway_discovery_resp_model == api_gateway_discovery_resp_model2

        # Convert model instance back to dict and verify no loss of data
        api_gateway_discovery_resp_model_json2 = api_gateway_discovery_resp_model.to_dict()
        assert api_gateway_discovery_resp_model_json2 == api_gateway_discovery_resp_model_json


class TestModel_ApiGatewayNullResultResp:
    """
    Test Class for ApiGatewayNullResultResp
    """

    def test_api_gateway_null_result_resp_serialization(self):
        """
        Test serialization/deserialization for ApiGatewayNullResultResp
        """

        # Construct a json representation of a ApiGatewayNullResultResp model
        api_gateway_null_result_resp_model_json = {}
        api_gateway_null_result_resp_model_json['success'] = True
        api_gateway_null_result_resp_model_json['errors'] = [['testString']]
        api_gateway_null_result_resp_model_json['messages'] = [['testString']]
        api_gateway_null_result_resp_model_json['result'] = 'testString'

        # Construct a model instance of ApiGatewayNullResultResp by calling from_dict on the json representation
        api_gateway_null_result_resp_model = ApiGatewayNullResultResp.from_dict(api_gateway_null_result_resp_model_json)
        assert api_gateway_null_result_resp_model != False

        # Construct a model instance of ApiGatewayNullResultResp by calling from_dict on the json representation
        api_gateway_null_result_resp_model_dict = ApiGatewayNullResultResp.from_dict(api_gateway_null_result_resp_model_json).__dict__
        api_gateway_null_result_resp_model2 = ApiGatewayNullResultResp(**api_gateway_null_result_resp_model_dict)

        # Verify the model instances are equivalent
        assert api_gateway_null_result_resp_model == api_gateway_null_result_resp_model2

        # Convert model instance back to dict and verify no loss of data
        api_gateway_null_result_resp_model_json2 = api_gateway_null_result_resp_model.to_dict()
        assert api_gateway_null_result_resp_model_json2 == api_gateway_null_result_resp_model_json


class TestModel_ApiGatewayOperation:
    """
    Test Class for ApiGatewayOperation
    """

    def test_api_gateway_operation_serialization(self):
        """
        Test serialization/deserialization for ApiGatewayOperation
        """

        # Construct a json representation of a ApiGatewayOperation model
        api_gateway_operation_model_json = {}
        api_gateway_operation_model_json['method'] = 'POST'
        api_gateway_operation_model_json['host'] = 'api.example.com'
        api_gateway_operation_model_json['endpoint'] = '/v1/messages'

        # Construct a model instance of ApiGatewayOperation by calling from_dict on the json representation
        api_gateway_operation_model = ApiGatewayOperation.from_dict(api_gateway_operation_model_json)
        assert api_gateway_operation_model != False

        # Construct a model instance of ApiGatewayOperation by calling from_dict on the json representation
        api_gateway_operation_model_dict = ApiGatewayOperation.from_dict(api_gateway_operation_model_json).__dict__
        api_gateway_operation_model2 = ApiGatewayOperation(**api_gateway_operation_model_dict)

        # Verify the model instances are equivalent
        assert api_gateway_operation_model == api_gateway_operation_model2

        # Convert model instance back to dict and verify no loss of data
        api_gateway_operation_model_json2 = api_gateway_operation_model.to_dict()
        assert api_gateway_operation_model_json2 == api_gateway_operation_model_json


class TestModel_ApiGatewayOperationItemResp:
    """
    Test Class for ApiGatewayOperationItemResp
    """

    def test_api_gateway_operation_item_resp_serialization(self):
        """
        Test serialization/deserialization for ApiGatewayOperationItemResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        api_gateway_operation_item_resp_result_model = {}  # ApiGatewayOperationItemRespResult
        api_gateway_operation_item_resp_result_model['operation_id'] = 'f174e90a-fafe-4643-bbbc-4a0ed4fc8415'
        api_gateway_operation_item_resp_result_model['method'] = 'POST'
        api_gateway_operation_item_resp_result_model['host'] = 'api.example.com'
        api_gateway_operation_item_resp_result_model['endpoint'] = '/v1/messages'

        # Construct a json representation of a ApiGatewayOperationItemResp model
        api_gateway_operation_item_resp_model_json = {}
        api_gateway_operation_item_resp_model_json['success'] = True
        api_gateway_operation_item_resp_model_json['errors'] = [['testString']]
        api_gateway_operation_item_resp_model_json['messages'] = [['testString']]
        api_gateway_operation_item_resp_model_json['result'] = api_gateway_operation_item_resp_result_model

        # Construct a model instance of ApiGatewayOperationItemResp by calling from_dict on the json representation
        api_gateway_operation_item_resp_model = ApiGatewayOperationItemResp.from_dict(api_gateway_operation_item_resp_model_json)
        assert api_gateway_operation_item_resp_model != False

        # Construct a model instance of ApiGatewayOperationItemResp by calling from_dict on the json representation
        api_gateway_operation_item_resp_model_dict = ApiGatewayOperationItemResp.from_dict(api_gateway_operation_item_resp_model_json).__dict__
        api_gateway_operation_item_resp_model2 = ApiGatewayOperationItemResp(**api_gateway_operation_item_resp_model_dict)

        # Verify the model instances are equivalent
        assert api_gateway_operation_item_resp_model == api_gateway_operation_item_resp_model2

        # Convert model instance back to dict and verify no loss of data
        api_gateway_operation_item_resp_model_json2 = api_gateway_operation_item_resp_model.to_dict()
        assert api_gateway_operation_item_resp_model_json2 == api_gateway_operation_item_resp_model_json


class TestModel_ApiGatewayOperationLabelResp:
    """
    Test Class for ApiGatewayOperationLabelResp
    """

    def test_api_gateway_operation_label_resp_serialization(self):
        """
        Test serialization/deserialization for ApiGatewayOperationLabelResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        api_gateway_operation_label_resp_result_labels_item_model = {}  # ApiGatewayOperationLabelRespResultLabelsItem
        api_gateway_operation_label_resp_result_labels_item_model['name'] = 'cf-llm'
        api_gateway_operation_label_resp_result_labels_item_model['source'] = 'managed'

        api_gateway_operation_label_resp_result_model = {}  # ApiGatewayOperationLabelRespResult
        api_gateway_operation_label_resp_result_model['operation_id'] = 'f174e90a-fafe-4643-bbbc-4a0ed4fc8415'
        api_gateway_operation_label_resp_result_model['labels'] = [api_gateway_operation_label_resp_result_labels_item_model]

        # Construct a json representation of a ApiGatewayOperationLabelResp model
        api_gateway_operation_label_resp_model_json = {}
        api_gateway_operation_label_resp_model_json['success'] = True
        api_gateway_operation_label_resp_model_json['errors'] = [['testString']]
        api_gateway_operation_label_resp_model_json['messages'] = [['testString']]
        api_gateway_operation_label_resp_model_json['result'] = api_gateway_operation_label_resp_result_model

        # Construct a model instance of ApiGatewayOperationLabelResp by calling from_dict on the json representation
        api_gateway_operation_label_resp_model = ApiGatewayOperationLabelResp.from_dict(api_gateway_operation_label_resp_model_json)
        assert api_gateway_operation_label_resp_model != False

        # Construct a model instance of ApiGatewayOperationLabelResp by calling from_dict on the json representation
        api_gateway_operation_label_resp_model_dict = ApiGatewayOperationLabelResp.from_dict(api_gateway_operation_label_resp_model_json).__dict__
        api_gateway_operation_label_resp_model2 = ApiGatewayOperationLabelResp(**api_gateway_operation_label_resp_model_dict)

        # Verify the model instances are equivalent
        assert api_gateway_operation_label_resp_model == api_gateway_operation_label_resp_model2

        # Convert model instance back to dict and verify no loss of data
        api_gateway_operation_label_resp_model_json2 = api_gateway_operation_label_resp_model.to_dict()
        assert api_gateway_operation_label_resp_model_json2 == api_gateway_operation_label_resp_model_json


class TestModel_ApiGatewayOperationsLabelsResp:
    """
    Test Class for ApiGatewayOperationsLabelsResp
    """

    def test_api_gateway_operations_labels_resp_serialization(self):
        """
        Test serialization/deserialization for ApiGatewayOperationsLabelsResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        api_gateway_operations_labels_resp_result_item_labels_item_model = {}  # ApiGatewayOperationsLabelsRespResultItemLabelsItem
        api_gateway_operations_labels_resp_result_item_labels_item_model['name'] = 'cf-llm'
        api_gateway_operations_labels_resp_result_item_labels_item_model['source'] = 'managed'

        api_gateway_operations_labels_resp_result_item_model = {}  # ApiGatewayOperationsLabelsRespResultItem
        api_gateway_operations_labels_resp_result_item_model['operation_id'] = 'f174e90a-fafe-4643-bbbc-4a0ed4fc8415'
        api_gateway_operations_labels_resp_result_item_model['labels'] = [api_gateway_operations_labels_resp_result_item_labels_item_model]

        # Construct a json representation of a ApiGatewayOperationsLabelsResp model
        api_gateway_operations_labels_resp_model_json = {}
        api_gateway_operations_labels_resp_model_json['success'] = True
        api_gateway_operations_labels_resp_model_json['errors'] = [['testString']]
        api_gateway_operations_labels_resp_model_json['messages'] = [['testString']]
        api_gateway_operations_labels_resp_model_json['result'] = [api_gateway_operations_labels_resp_result_item_model]

        # Construct a model instance of ApiGatewayOperationsLabelsResp by calling from_dict on the json representation
        api_gateway_operations_labels_resp_model = ApiGatewayOperationsLabelsResp.from_dict(api_gateway_operations_labels_resp_model_json)
        assert api_gateway_operations_labels_resp_model != False

        # Construct a model instance of ApiGatewayOperationsLabelsResp by calling from_dict on the json representation
        api_gateway_operations_labels_resp_model_dict = ApiGatewayOperationsLabelsResp.from_dict(api_gateway_operations_labels_resp_model_json).__dict__
        api_gateway_operations_labels_resp_model2 = ApiGatewayOperationsLabelsResp(**api_gateway_operations_labels_resp_model_dict)

        # Verify the model instances are equivalent
        assert api_gateway_operations_labels_resp_model == api_gateway_operations_labels_resp_model2

        # Convert model instance back to dict and verify no loss of data
        api_gateway_operations_labels_resp_model_json2 = api_gateway_operations_labels_resp_model.to_dict()
        assert api_gateway_operations_labels_resp_model_json2 == api_gateway_operations_labels_resp_model_json


class TestModel_ApiGatewayOperationsListResp:
    """
    Test Class for ApiGatewayOperationsListResp
    """

    def test_api_gateway_operations_list_resp_serialization(self):
        """
        Test serialization/deserialization for ApiGatewayOperationsListResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        api_gateway_operations_list_resp_result_item_model = {}  # ApiGatewayOperationsListRespResultItem
        api_gateway_operations_list_resp_result_item_model['operation_id'] = 'test-fafe-4643-bbbc-example'
        api_gateway_operations_list_resp_result_item_model['method'] = 'POST'
        api_gateway_operations_list_resp_result_item_model['host'] = 'api.example.com'
        api_gateway_operations_list_resp_result_item_model['endpoint'] = '/v1/messages'
        api_gateway_operations_list_resp_result_item_model['last_updated'] = '2024-01-01T00:00:00Z'

        result_info_model = {}  # ResultInfo
        result_info_model['count'] = 38
        result_info_model['page'] = 38
        result_info_model['per_page'] = 38
        result_info_model['total_count'] = 38

        # Construct a json representation of a ApiGatewayOperationsListResp model
        api_gateway_operations_list_resp_model_json = {}
        api_gateway_operations_list_resp_model_json['success'] = True
        api_gateway_operations_list_resp_model_json['errors'] = [['testString']]
        api_gateway_operations_list_resp_model_json['messages'] = [['testString']]
        api_gateway_operations_list_resp_model_json['result'] = [api_gateway_operations_list_resp_result_item_model]
        api_gateway_operations_list_resp_model_json['result_info'] = result_info_model

        # Construct a model instance of ApiGatewayOperationsListResp by calling from_dict on the json representation
        api_gateway_operations_list_resp_model = ApiGatewayOperationsListResp.from_dict(api_gateway_operations_list_resp_model_json)
        assert api_gateway_operations_list_resp_model != False

        # Construct a model instance of ApiGatewayOperationsListResp by calling from_dict on the json representation
        api_gateway_operations_list_resp_model_dict = ApiGatewayOperationsListResp.from_dict(api_gateway_operations_list_resp_model_json).__dict__
        api_gateway_operations_list_resp_model2 = ApiGatewayOperationsListResp(**api_gateway_operations_list_resp_model_dict)

        # Verify the model instances are equivalent
        assert api_gateway_operations_list_resp_model == api_gateway_operations_list_resp_model2

        # Convert model instance back to dict and verify no loss of data
        api_gateway_operations_list_resp_model_json2 = api_gateway_operations_list_resp_model.to_dict()
        assert api_gateway_operations_list_resp_model_json2 == api_gateway_operations_list_resp_model_json


class TestModel_ApiGatewayOperationsResp:
    """
    Test Class for ApiGatewayOperationsResp
    """

    def test_api_gateway_operations_resp_serialization(self):
        """
        Test serialization/deserialization for ApiGatewayOperationsResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        api_gateway_operations_resp_result_item_model = {}  # ApiGatewayOperationsRespResultItem
        api_gateway_operations_resp_result_item_model['operation_id'] = 'f174e90a-fafe-4643-bbbc-4a0ed4fc8415'
        api_gateway_operations_resp_result_item_model['method'] = 'POST'
        api_gateway_operations_resp_result_item_model['host'] = 'api.example.com'
        api_gateway_operations_resp_result_item_model['endpoint'] = '/v1/messages'

        # Construct a json representation of a ApiGatewayOperationsResp model
        api_gateway_operations_resp_model_json = {}
        api_gateway_operations_resp_model_json['success'] = True
        api_gateway_operations_resp_model_json['errors'] = [['testString']]
        api_gateway_operations_resp_model_json['messages'] = [['testString']]
        api_gateway_operations_resp_model_json['result'] = [api_gateway_operations_resp_result_item_model]

        # Construct a model instance of ApiGatewayOperationsResp by calling from_dict on the json representation
        api_gateway_operations_resp_model = ApiGatewayOperationsResp.from_dict(api_gateway_operations_resp_model_json)
        assert api_gateway_operations_resp_model != False

        # Construct a model instance of ApiGatewayOperationsResp by calling from_dict on the json representation
        api_gateway_operations_resp_model_dict = ApiGatewayOperationsResp.from_dict(api_gateway_operations_resp_model_json).__dict__
        api_gateway_operations_resp_model2 = ApiGatewayOperationsResp(**api_gateway_operations_resp_model_dict)

        # Verify the model instances are equivalent
        assert api_gateway_operations_resp_model == api_gateway_operations_resp_model2

        # Convert model instance back to dict and verify no loss of data
        api_gateway_operations_resp_model_json2 = api_gateway_operations_resp_model.to_dict()
        assert api_gateway_operations_resp_model_json2 == api_gateway_operations_resp_model_json


class TestModel_ApiGatewaySchemasResp:
    """
    Test Class for ApiGatewaySchemasResp
    """

    def test_api_gateway_schemas_resp_serialization(self):
        """
        Test serialization/deserialization for ApiGatewaySchemasResp
        """

        # Construct a json representation of a ApiGatewaySchemasResp model
        api_gateway_schemas_resp_model_json = {}
        api_gateway_schemas_resp_model_json['success'] = True
        api_gateway_schemas_resp_model_json['errors'] = [['testString']]
        api_gateway_schemas_resp_model_json['messages'] = [['testString']]
        api_gateway_schemas_resp_model_json['result'] = {'anyKey': 'anyValue'}

        # Construct a model instance of ApiGatewaySchemasResp by calling from_dict on the json representation
        api_gateway_schemas_resp_model = ApiGatewaySchemasResp.from_dict(api_gateway_schemas_resp_model_json)
        assert api_gateway_schemas_resp_model != False

        # Construct a model instance of ApiGatewaySchemasResp by calling from_dict on the json representation
        api_gateway_schemas_resp_model_dict = ApiGatewaySchemasResp.from_dict(api_gateway_schemas_resp_model_json).__dict__
        api_gateway_schemas_resp_model2 = ApiGatewaySchemasResp(**api_gateway_schemas_resp_model_dict)

        # Verify the model instances are equivalent
        assert api_gateway_schemas_resp_model == api_gateway_schemas_resp_model2

        # Convert model instance back to dict and verify no loss of data
        api_gateway_schemas_resp_model_json2 = api_gateway_schemas_resp_model.to_dict()
        assert api_gateway_schemas_resp_model_json2 == api_gateway_schemas_resp_model_json


class TestModel_DiscoveryOperation:
    """
    Test Class for DiscoveryOperation
    """

    def test_discovery_operation_serialization(self):
        """
        Test serialization/deserialization for DiscoveryOperation
        """

        # Construct dict forms of any model objects needed in order to build this model.

        discovery_operation_features_traffic_stats_model = {}  # DiscoveryOperationFeaturesTrafficStats
        discovery_operation_features_traffic_stats_model['last_updated'] = '2019-01-01T12:00:00Z'
        discovery_operation_features_traffic_stats_model['period_seconds'] = 38
        discovery_operation_features_traffic_stats_model['requests'] = 72.5

        discovery_operation_features_model = {}  # DiscoveryOperationFeatures
        discovery_operation_features_model['traffic_stats'] = discovery_operation_features_traffic_stats_model

        # Construct a json representation of a DiscoveryOperation model
        discovery_operation_model_json = {}
        discovery_operation_model_json['id'] = 'f174e90a-fafe-4643-bbbc-4a0ed4fc8415'
        discovery_operation_model_json['endpoint'] = '/v1/messages'
        discovery_operation_model_json['host'] = 'api.example.com'
        discovery_operation_model_json['method'] = 'POST'
        discovery_operation_model_json['last_updated'] = '2024-01-01T00:00:00Z'
        discovery_operation_model_json['origin'] = ['ML']
        discovery_operation_model_json['state'] = 'review'
        discovery_operation_model_json['features'] = discovery_operation_features_model

        # Construct a model instance of DiscoveryOperation by calling from_dict on the json representation
        discovery_operation_model = DiscoveryOperation.from_dict(discovery_operation_model_json)
        assert discovery_operation_model != False

        # Construct a model instance of DiscoveryOperation by calling from_dict on the json representation
        discovery_operation_model_dict = DiscoveryOperation.from_dict(discovery_operation_model_json).__dict__
        discovery_operation_model2 = DiscoveryOperation(**discovery_operation_model_dict)

        # Verify the model instances are equivalent
        assert discovery_operation_model == discovery_operation_model2

        # Convert model instance back to dict and verify no loss of data
        discovery_operation_model_json2 = discovery_operation_model.to_dict()
        assert discovery_operation_model_json2 == discovery_operation_model_json


class TestModel_DiscoveryOperationsListResp:
    """
    Test Class for DiscoveryOperationsListResp
    """

    def test_discovery_operations_list_resp_serialization(self):
        """
        Test serialization/deserialization for DiscoveryOperationsListResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        discovery_operation_features_traffic_stats_model = {}  # DiscoveryOperationFeaturesTrafficStats
        discovery_operation_features_traffic_stats_model['last_updated'] = '2019-01-01T12:00:00Z'
        discovery_operation_features_traffic_stats_model['period_seconds'] = 38
        discovery_operation_features_traffic_stats_model['requests'] = 72.5

        discovery_operation_features_model = {}  # DiscoveryOperationFeatures
        discovery_operation_features_model['traffic_stats'] = discovery_operation_features_traffic_stats_model

        discovery_operation_model = {}  # DiscoveryOperation
        discovery_operation_model['id'] = 'f174e90a-fafe-4643-bbbc-4a0ed4fc8415'
        discovery_operation_model['endpoint'] = '/v1/messages'
        discovery_operation_model['host'] = 'api.example.com'
        discovery_operation_model['method'] = 'POST'
        discovery_operation_model['last_updated'] = '2024-01-01T00:00:00Z'
        discovery_operation_model['origin'] = ['ML']
        discovery_operation_model['state'] = 'review'
        discovery_operation_model['features'] = discovery_operation_features_model

        result_info_model = {}  # ResultInfo
        result_info_model['count'] = 38
        result_info_model['page'] = 38
        result_info_model['per_page'] = 38
        result_info_model['total_count'] = 38

        # Construct a json representation of a DiscoveryOperationsListResp model
        discovery_operations_list_resp_model_json = {}
        discovery_operations_list_resp_model_json['success'] = True
        discovery_operations_list_resp_model_json['errors'] = [['testString']]
        discovery_operations_list_resp_model_json['messages'] = [['testString']]
        discovery_operations_list_resp_model_json['result'] = [discovery_operation_model]
        discovery_operations_list_resp_model_json['result_info'] = result_info_model

        # Construct a model instance of DiscoveryOperationsListResp by calling from_dict on the json representation
        discovery_operations_list_resp_model = DiscoveryOperationsListResp.from_dict(discovery_operations_list_resp_model_json)
        assert discovery_operations_list_resp_model != False

        # Construct a model instance of DiscoveryOperationsListResp by calling from_dict on the json representation
        discovery_operations_list_resp_model_dict = DiscoveryOperationsListResp.from_dict(discovery_operations_list_resp_model_json).__dict__
        discovery_operations_list_resp_model2 = DiscoveryOperationsListResp(**discovery_operations_list_resp_model_dict)

        # Verify the model instances are equivalent
        assert discovery_operations_list_resp_model == discovery_operations_list_resp_model2

        # Convert model instance back to dict and verify no loss of data
        discovery_operations_list_resp_model_json2 = discovery_operations_list_resp_model.to_dict()
        assert discovery_operations_list_resp_model_json2 == discovery_operations_list_resp_model_json


class TestModel_DiscoveryOperationsPatchResp:
    """
    Test Class for DiscoveryOperationsPatchResp
    """

    def test_discovery_operations_patch_resp_serialization(self):
        """
        Test serialization/deserialization for DiscoveryOperationsPatchResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        discovery_operation_features_traffic_stats_model = {}  # DiscoveryOperationFeaturesTrafficStats
        discovery_operation_features_traffic_stats_model['last_updated'] = '2019-01-01T12:00:00Z'
        discovery_operation_features_traffic_stats_model['period_seconds'] = 38
        discovery_operation_features_traffic_stats_model['requests'] = 72.5

        discovery_operation_features_model = {}  # DiscoveryOperationFeatures
        discovery_operation_features_model['traffic_stats'] = discovery_operation_features_traffic_stats_model

        discovery_operation_model = {}  # DiscoveryOperation
        discovery_operation_model['id'] = 'f174e90a-fafe-4643-bbbc-4a0ed4fc8415'
        discovery_operation_model['endpoint'] = '/v1/messages'
        discovery_operation_model['host'] = 'api.example.com'
        discovery_operation_model['method'] = 'POST'
        discovery_operation_model['last_updated'] = '2024-01-01T00:00:00Z'
        discovery_operation_model['origin'] = ['ML']
        discovery_operation_model['state'] = 'review'
        discovery_operation_model['features'] = discovery_operation_features_model

        # Construct a json representation of a DiscoveryOperationsPatchResp model
        discovery_operations_patch_resp_model_json = {}
        discovery_operations_patch_resp_model_json['success'] = True
        discovery_operations_patch_resp_model_json['errors'] = [['testString']]
        discovery_operations_patch_resp_model_json['messages'] = [['testString']]
        discovery_operations_patch_resp_model_json['result'] = [discovery_operation_model]

        # Construct a model instance of DiscoveryOperationsPatchResp by calling from_dict on the json representation
        discovery_operations_patch_resp_model = DiscoveryOperationsPatchResp.from_dict(discovery_operations_patch_resp_model_json)
        assert discovery_operations_patch_resp_model != False

        # Construct a model instance of DiscoveryOperationsPatchResp by calling from_dict on the json representation
        discovery_operations_patch_resp_model_dict = DiscoveryOperationsPatchResp.from_dict(discovery_operations_patch_resp_model_json).__dict__
        discovery_operations_patch_resp_model2 = DiscoveryOperationsPatchResp(**discovery_operations_patch_resp_model_dict)

        # Verify the model instances are equivalent
        assert discovery_operations_patch_resp_model == discovery_operations_patch_resp_model2

        # Convert model instance back to dict and verify no loss of data
        discovery_operations_patch_resp_model_json2 = discovery_operations_patch_resp_model.to_dict()
        assert discovery_operations_patch_resp_model_json2 == discovery_operations_patch_resp_model_json


class TestModel_ResultInfo:
    """
    Test Class for ResultInfo
    """

    def test_result_info_serialization(self):
        """
        Test serialization/deserialization for ResultInfo
        """

        # Construct a json representation of a ResultInfo model
        result_info_model_json = {}
        result_info_model_json['count'] = 38
        result_info_model_json['page'] = 38
        result_info_model_json['per_page'] = 38
        result_info_model_json['total_count'] = 38

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


# endregion
##############################################################################
# End of Model Tests
##############################################################################
