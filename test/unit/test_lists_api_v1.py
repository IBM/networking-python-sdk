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
Unit Tests for ListsApiV1
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import os
import pytest
import re
import requests
import responses
import urllib
from ibm_cloud_networking_services.lists_api_v1 import *

crn = 'testString'
item_id = 'testString'
list_id = 'testString'
operation_id = 'testString'

_service = ListsApiV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn,
    item_id=item_id,
    list_id=list_id,
    operation_id=operation_id,
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
# Start of Service: Lists
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

        service = ListsApiV1.new_instance(
            crn=crn,
            item_id=item_id,
            list_id=list_id,
            operation_id=operation_id,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, ListsApiV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = ListsApiV1.new_instance(
                crn=crn,
                item_id=item_id,
                list_id=list_id,
                operation_id=operation_id,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = ListsApiV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='crn must be provided'):
            service = ListsApiV1.new_instance(
                crn=None,
                item_id=None,
                list_id=None,
                operation_id=None,
            )


class TestGetManagedLists:
    """
    Test Class for get_managed_lists
    """

    @responses.activate
    def test_get_managed_lists_all_params(self):
        """
        get_managed_lists()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rules/managed_lists')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"name": "cf.malware", "description": "description", "kind": "ip"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_managed_lists()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_managed_lists_all_params_with_retries(self):
        # Enable retries and run test_get_managed_lists_all_params.
        _service.enable_retries()
        self.test_get_managed_lists_all_params()

        # Disable retries and run test_get_managed_lists_all_params.
        _service.disable_retries()
        self.test_get_managed_lists_all_params()

    @responses.activate
    def test_get_managed_lists_value_error(self):
        """
        test_get_managed_lists_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rules/managed_lists')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"name": "cf.malware", "description": "description", "kind": "ip"}]}'
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
                _service.get_managed_lists(**req_copy)

    def test_get_managed_lists_value_error_with_retries(self):
        # Enable retries and run test_get_managed_lists_value_error.
        _service.enable_retries()
        self.test_get_managed_lists_value_error()

        # Disable retries and run test_get_managed_lists_value_error.
        _service.disable_retries()
        self.test_get_managed_lists_value_error()


class TestGetCustomLists:
    """
    Test Class for get_custom_lists
    """

    @responses.activate
    def test_get_custom_lists_all_params(self):
        """
        get_custom_lists()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rules/lists')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"name": "good_ips", "id": "id", "description": "description", "kind": "ip", "num_items": 10, "num_referencing_filters": 5}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_custom_lists()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_custom_lists_all_params_with_retries(self):
        # Enable retries and run test_get_custom_lists_all_params.
        _service.enable_retries()
        self.test_get_custom_lists_all_params()

        # Disable retries and run test_get_custom_lists_all_params.
        _service.disable_retries()
        self.test_get_custom_lists_all_params()

    @responses.activate
    def test_get_custom_lists_value_error(self):
        """
        test_get_custom_lists_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rules/lists')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"name": "good_ips", "id": "id", "description": "description", "kind": "ip", "num_items": 10, "num_referencing_filters": 5}]}'
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
                _service.get_custom_lists(**req_copy)

    def test_get_custom_lists_value_error_with_retries(self):
        # Enable retries and run test_get_custom_lists_value_error.
        _service.enable_retries()
        self.test_get_custom_lists_value_error()

        # Disable retries and run test_get_custom_lists_value_error.
        _service.disable_retries()
        self.test_get_custom_lists_value_error()


class TestCreateCustomLists:
    """
    Test Class for create_custom_lists
    """

    @responses.activate
    def test_create_custom_lists_all_params(self):
        """
        create_custom_lists()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rules/lists')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"name": "good_ips", "id": "id", "description": "description", "kind": "ip", "num_items": 10, "num_referencing_filters": 5}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        kind = 'ip'
        name = 'testString'
        description = 'testString'

        # Invoke method
        response = _service.create_custom_lists(
            kind=kind,
            name=name,
            description=description,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['kind'] == 'ip'
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'

    def test_create_custom_lists_all_params_with_retries(self):
        # Enable retries and run test_create_custom_lists_all_params.
        _service.enable_retries()
        self.test_create_custom_lists_all_params()

        # Disable retries and run test_create_custom_lists_all_params.
        _service.disable_retries()
        self.test_create_custom_lists_all_params()

    @responses.activate
    def test_create_custom_lists_required_params(self):
        """
        test_create_custom_lists_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rules/lists')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"name": "good_ips", "id": "id", "description": "description", "kind": "ip", "num_items": 10, "num_referencing_filters": 5}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.create_custom_lists()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_custom_lists_required_params_with_retries(self):
        # Enable retries and run test_create_custom_lists_required_params.
        _service.enable_retries()
        self.test_create_custom_lists_required_params()

        # Disable retries and run test_create_custom_lists_required_params.
        _service.disable_retries()
        self.test_create_custom_lists_required_params()

    @responses.activate
    def test_create_custom_lists_value_error(self):
        """
        test_create_custom_lists_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rules/lists')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"name": "good_ips", "id": "id", "description": "description", "kind": "ip", "num_items": 10, "num_referencing_filters": 5}}'
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
                _service.create_custom_lists(**req_copy)

    def test_create_custom_lists_value_error_with_retries(self):
        # Enable retries and run test_create_custom_lists_value_error.
        _service.enable_retries()
        self.test_create_custom_lists_value_error()

        # Disable retries and run test_create_custom_lists_value_error.
        _service.disable_retries()
        self.test_create_custom_lists_value_error()


class TestGetCustomList:
    """
    Test Class for get_custom_list
    """

    @responses.activate
    def test_get_custom_list_all_params(self):
        """
        get_custom_list()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rules/lists/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"name": "good_ips", "id": "id", "description": "description", "kind": "ip", "num_items": 10, "num_referencing_filters": 5}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_custom_list()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_custom_list_all_params_with_retries(self):
        # Enable retries and run test_get_custom_list_all_params.
        _service.enable_retries()
        self.test_get_custom_list_all_params()

        # Disable retries and run test_get_custom_list_all_params.
        _service.disable_retries()
        self.test_get_custom_list_all_params()

    @responses.activate
    def test_get_custom_list_value_error(self):
        """
        test_get_custom_list_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rules/lists/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"name": "good_ips", "id": "id", "description": "description", "kind": "ip", "num_items": 10, "num_referencing_filters": 5}}'
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
                _service.get_custom_list(**req_copy)

    def test_get_custom_list_value_error_with_retries(self):
        # Enable retries and run test_get_custom_list_value_error.
        _service.enable_retries()
        self.test_get_custom_list_value_error()

        # Disable retries and run test_get_custom_list_value_error.
        _service.disable_retries()
        self.test_get_custom_list_value_error()


class TestUpdateCustomList:
    """
    Test Class for update_custom_list
    """

    @responses.activate
    def test_update_custom_list_all_params(self):
        """
        update_custom_list()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rules/lists/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"name": "good_ips", "id": "id", "description": "description", "kind": "ip", "num_items": 10, "num_referencing_filters": 5}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        description = 'testString'

        # Invoke method
        response = _service.update_custom_list(
            description=description,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['description'] == 'testString'

    def test_update_custom_list_all_params_with_retries(self):
        # Enable retries and run test_update_custom_list_all_params.
        _service.enable_retries()
        self.test_update_custom_list_all_params()

        # Disable retries and run test_update_custom_list_all_params.
        _service.disable_retries()
        self.test_update_custom_list_all_params()

    @responses.activate
    def test_update_custom_list_required_params(self):
        """
        test_update_custom_list_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rules/lists/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"name": "good_ips", "id": "id", "description": "description", "kind": "ip", "num_items": 10, "num_referencing_filters": 5}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_custom_list()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_custom_list_required_params_with_retries(self):
        # Enable retries and run test_update_custom_list_required_params.
        _service.enable_retries()
        self.test_update_custom_list_required_params()

        # Disable retries and run test_update_custom_list_required_params.
        _service.disable_retries()
        self.test_update_custom_list_required_params()

    @responses.activate
    def test_update_custom_list_value_error(self):
        """
        test_update_custom_list_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rules/lists/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"name": "good_ips", "id": "id", "description": "description", "kind": "ip", "num_items": 10, "num_referencing_filters": 5}}'
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
                _service.update_custom_list(**req_copy)

    def test_update_custom_list_value_error_with_retries(self):
        # Enable retries and run test_update_custom_list_value_error.
        _service.enable_retries()
        self.test_update_custom_list_value_error()

        # Disable retries and run test_update_custom_list_value_error.
        _service.disable_retries()
        self.test_update_custom_list_value_error()


class TestDeleteCustomList:
    """
    Test Class for delete_custom_list
    """

    @responses.activate
    def test_delete_custom_list_all_params(self):
        """
        delete_custom_list()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rules/lists/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "34b12448945f11eaa1b71c4d701ab86e"}}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.delete_custom_list()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_custom_list_all_params_with_retries(self):
        # Enable retries and run test_delete_custom_list_all_params.
        _service.enable_retries()
        self.test_delete_custom_list_all_params()

        # Disable retries and run test_delete_custom_list_all_params.
        _service.disable_retries()
        self.test_delete_custom_list_all_params()

    @responses.activate
    def test_delete_custom_list_value_error(self):
        """
        test_delete_custom_list_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rules/lists/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "34b12448945f11eaa1b71c4d701ab86e"}}'
        responses.add(
            responses.DELETE,
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
                _service.delete_custom_list(**req_copy)

    def test_delete_custom_list_value_error_with_retries(self):
        # Enable retries and run test_delete_custom_list_value_error.
        _service.enable_retries()
        self.test_delete_custom_list_value_error()

        # Disable retries and run test_delete_custom_list_value_error.
        _service.disable_retries()
        self.test_delete_custom_list_value_error()


class TestGetListItems:
    """
    Test Class for get_list_items
    """

    @responses.activate
    def test_get_list_items_all_params(self):
        """
        get_list_items()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rules/lists/testString/items')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "70c2009751b24ffc9ed1ab462ba957b4", "asn": 19604, "comment": "My list of developer IPs.", "hostname": "cloud.ibm.com", "ip": "172.64.0.0/13", "created_on": "2025-03-21T16:19:21Z", "modified_on": "2025-03-21T16:19:37Z"}], "result_info": {"cursors": {"after": "yyy", "before": "xxx"}}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        cursor = 'testString'
        per_page = 1
        search = 'testString'

        # Invoke method
        response = _service.get_list_items(
            cursor=cursor,
            per_page=per_page,
            search=search,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'cursor={}'.format(cursor) in query_string
        assert 'per_page={}'.format(per_page) in query_string
        assert 'search={}'.format(search) in query_string

    def test_get_list_items_all_params_with_retries(self):
        # Enable retries and run test_get_list_items_all_params.
        _service.enable_retries()
        self.test_get_list_items_all_params()

        # Disable retries and run test_get_list_items_all_params.
        _service.disable_retries()
        self.test_get_list_items_all_params()

    @responses.activate
    def test_get_list_items_required_params(self):
        """
        test_get_list_items_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rules/lists/testString/items')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "70c2009751b24ffc9ed1ab462ba957b4", "asn": 19604, "comment": "My list of developer IPs.", "hostname": "cloud.ibm.com", "ip": "172.64.0.0/13", "created_on": "2025-03-21T16:19:21Z", "modified_on": "2025-03-21T16:19:37Z"}], "result_info": {"cursors": {"after": "yyy", "before": "xxx"}}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_list_items()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_list_items_required_params_with_retries(self):
        # Enable retries and run test_get_list_items_required_params.
        _service.enable_retries()
        self.test_get_list_items_required_params()

        # Disable retries and run test_get_list_items_required_params.
        _service.disable_retries()
        self.test_get_list_items_required_params()

    @responses.activate
    def test_get_list_items_value_error(self):
        """
        test_get_list_items_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rules/lists/testString/items')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "70c2009751b24ffc9ed1ab462ba957b4", "asn": 19604, "comment": "My list of developer IPs.", "hostname": "cloud.ibm.com", "ip": "172.64.0.0/13", "created_on": "2025-03-21T16:19:21Z", "modified_on": "2025-03-21T16:19:37Z"}], "result_info": {"cursors": {"after": "yyy", "before": "xxx"}}}'
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
                _service.get_list_items(**req_copy)

    def test_get_list_items_value_error_with_retries(self):
        # Enable retries and run test_get_list_items_value_error.
        _service.enable_retries()
        self.test_get_list_items_value_error()

        # Disable retries and run test_get_list_items_value_error.
        _service.disable_retries()
        self.test_get_list_items_value_error()


class TestCreateListItems:
    """
    Test Class for create_list_items
    """

    @responses.activate
    def test_create_list_items_all_params(self):
        """
        create_list_items()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rules/lists/testString/items')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"operation_id": "53d73a83d33d4e3b8791764a9b9f2412"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a CreateListItemsReqItem model
        create_list_items_req_item_model = {}
        create_list_items_req_item_model['asn'] = 19604
        create_list_items_req_item_model['comment'] = 'My list of developer IPs.'
        create_list_items_req_item_model['hostname'] = 'cloud.ibm.com'
        create_list_items_req_item_model['ip'] = '172.64.0.0/13'

        # Set up parameter values
        create_list_items_req_item = [create_list_items_req_item_model]

        # Invoke method
        response = _service.create_list_items(
            create_list_items_req_item=create_list_items_req_item,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == create_list_items_req_item

    def test_create_list_items_all_params_with_retries(self):
        # Enable retries and run test_create_list_items_all_params.
        _service.enable_retries()
        self.test_create_list_items_all_params()

        # Disable retries and run test_create_list_items_all_params.
        _service.disable_retries()
        self.test_create_list_items_all_params()

    @responses.activate
    def test_create_list_items_required_params(self):
        """
        test_create_list_items_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rules/lists/testString/items')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"operation_id": "53d73a83d33d4e3b8791764a9b9f2412"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.create_list_items()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_list_items_required_params_with_retries(self):
        # Enable retries and run test_create_list_items_required_params.
        _service.enable_retries()
        self.test_create_list_items_required_params()

        # Disable retries and run test_create_list_items_required_params.
        _service.disable_retries()
        self.test_create_list_items_required_params()

    @responses.activate
    def test_create_list_items_value_error(self):
        """
        test_create_list_items_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rules/lists/testString/items')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"operation_id": "53d73a83d33d4e3b8791764a9b9f2412"}}'
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
                _service.create_list_items(**req_copy)

    def test_create_list_items_value_error_with_retries(self):
        # Enable retries and run test_create_list_items_value_error.
        _service.enable_retries()
        self.test_create_list_items_value_error()

        # Disable retries and run test_create_list_items_value_error.
        _service.disable_retries()
        self.test_create_list_items_value_error()


class TestDeleteListItems:
    """
    Test Class for delete_list_items
    """

    @responses.activate
    def test_delete_list_items_all_params(self):
        """
        delete_list_items()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rules/lists/testString/items')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"operation_id": "53d73a83d33d4e3b8791764a9b9f2412"}}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a DeleteListItemsReqItemsItem model
        delete_list_items_req_items_item_model = {}
        delete_list_items_req_items_item_model['id'] = '70c2009751b24ffc9ed1ab462ba957b4'

        # Set up parameter values
        items = [delete_list_items_req_items_item_model]

        # Invoke method
        response = _service.delete_list_items(
            items=items,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['items'] == [delete_list_items_req_items_item_model]

    def test_delete_list_items_all_params_with_retries(self):
        # Enable retries and run test_delete_list_items_all_params.
        _service.enable_retries()
        self.test_delete_list_items_all_params()

        # Disable retries and run test_delete_list_items_all_params.
        _service.disable_retries()
        self.test_delete_list_items_all_params()

    @responses.activate
    def test_delete_list_items_required_params(self):
        """
        test_delete_list_items_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rules/lists/testString/items')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"operation_id": "53d73a83d33d4e3b8791764a9b9f2412"}}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.delete_list_items()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_list_items_required_params_with_retries(self):
        # Enable retries and run test_delete_list_items_required_params.
        _service.enable_retries()
        self.test_delete_list_items_required_params()

        # Disable retries and run test_delete_list_items_required_params.
        _service.disable_retries()
        self.test_delete_list_items_required_params()

    @responses.activate
    def test_delete_list_items_value_error(self):
        """
        test_delete_list_items_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rules/lists/testString/items')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"operation_id": "53d73a83d33d4e3b8791764a9b9f2412"}}'
        responses.add(
            responses.DELETE,
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
                _service.delete_list_items(**req_copy)

    def test_delete_list_items_value_error_with_retries(self):
        # Enable retries and run test_delete_list_items_value_error.
        _service.enable_retries()
        self.test_delete_list_items_value_error()

        # Disable retries and run test_delete_list_items_value_error.
        _service.disable_retries()
        self.test_delete_list_items_value_error()


class TestUpdateListItems:
    """
    Test Class for update_list_items
    """

    @responses.activate
    def test_update_list_items_all_params(self):
        """
        update_list_items()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rules/lists/testString/items')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"operation_id": "53d73a83d33d4e3b8791764a9b9f2412"}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a CreateListItemsReqItem model
        create_list_items_req_item_model = {}
        create_list_items_req_item_model['asn'] = 19604
        create_list_items_req_item_model['comment'] = 'My list of developer IPs.'
        create_list_items_req_item_model['hostname'] = 'cloud.ibm.com'
        create_list_items_req_item_model['ip'] = '172.64.0.0/13'

        # Set up parameter values
        create_list_items_req_item = [create_list_items_req_item_model]

        # Invoke method
        response = _service.update_list_items(
            create_list_items_req_item=create_list_items_req_item,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == create_list_items_req_item

    def test_update_list_items_all_params_with_retries(self):
        # Enable retries and run test_update_list_items_all_params.
        _service.enable_retries()
        self.test_update_list_items_all_params()

        # Disable retries and run test_update_list_items_all_params.
        _service.disable_retries()
        self.test_update_list_items_all_params()

    @responses.activate
    def test_update_list_items_required_params(self):
        """
        test_update_list_items_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rules/lists/testString/items')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"operation_id": "53d73a83d33d4e3b8791764a9b9f2412"}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_list_items()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_list_items_required_params_with_retries(self):
        # Enable retries and run test_update_list_items_required_params.
        _service.enable_retries()
        self.test_update_list_items_required_params()

        # Disable retries and run test_update_list_items_required_params.
        _service.disable_retries()
        self.test_update_list_items_required_params()

    @responses.activate
    def test_update_list_items_value_error(self):
        """
        test_update_list_items_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rules/lists/testString/items')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"operation_id": "53d73a83d33d4e3b8791764a9b9f2412"}}'
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
                _service.update_list_items(**req_copy)

    def test_update_list_items_value_error_with_retries(self):
        # Enable retries and run test_update_list_items_value_error.
        _service.enable_retries()
        self.test_update_list_items_value_error()

        # Disable retries and run test_update_list_items_value_error.
        _service.disable_retries()
        self.test_update_list_items_value_error()


class TestGetListItem:
    """
    Test Class for get_list_item
    """

    @responses.activate
    def test_get_list_item_all_params(self):
        """
        get_list_item()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rules/lists/testString/items/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "70c2009751b24ffc9ed1ab462ba957b4", "asn": 19604, "comment": "My list of developer IPs.", "hostname": "cloud.ibm.com", "ip": "172.64.0.0/13", "created_on": "2025-03-21T16:19:21Z", "modified_on": "2025-03-21T16:19:37Z"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_list_item()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_list_item_all_params_with_retries(self):
        # Enable retries and run test_get_list_item_all_params.
        _service.enable_retries()
        self.test_get_list_item_all_params()

        # Disable retries and run test_get_list_item_all_params.
        _service.disable_retries()
        self.test_get_list_item_all_params()

    @responses.activate
    def test_get_list_item_value_error(self):
        """
        test_get_list_item_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rules/lists/testString/items/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "70c2009751b24ffc9ed1ab462ba957b4", "asn": 19604, "comment": "My list of developer IPs.", "hostname": "cloud.ibm.com", "ip": "172.64.0.0/13", "created_on": "2025-03-21T16:19:21Z", "modified_on": "2025-03-21T16:19:37Z"}}'
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
                _service.get_list_item(**req_copy)

    def test_get_list_item_value_error_with_retries(self):
        # Enable retries and run test_get_list_item_value_error.
        _service.enable_retries()
        self.test_get_list_item_value_error()

        # Disable retries and run test_get_list_item_value_error.
        _service.disable_retries()
        self.test_get_list_item_value_error()


class TestGetOperationStatus:
    """
    Test Class for get_operation_status
    """

    @responses.activate
    def test_get_operation_status_all_params(self):
        """
        get_operation_status()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rules/lists/bulk_operations/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "0147be950d5c42b8b47c07792c5015e3", "status": "completed", "completed": "2025-03-21T16:07:41.782564Z", "error": "error"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_operation_status()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_operation_status_all_params_with_retries(self):
        # Enable retries and run test_get_operation_status_all_params.
        _service.enable_retries()
        self.test_get_operation_status_all_params()

        # Disable retries and run test_get_operation_status_all_params.
        _service.disable_retries()
        self.test_get_operation_status_all_params()

    @responses.activate
    def test_get_operation_status_value_error(self):
        """
        test_get_operation_status_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/rules/lists/bulk_operations/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "0147be950d5c42b8b47c07792c5015e3", "status": "completed", "completed": "2025-03-21T16:07:41.782564Z", "error": "error"}}'
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
                _service.get_operation_status(**req_copy)

    def test_get_operation_status_value_error_with_retries(self):
        # Enable retries and run test_get_operation_status_value_error.
        _service.enable_retries()
        self.test_get_operation_status_value_error()

        # Disable retries and run test_get_operation_status_value_error.
        _service.disable_retries()
        self.test_get_operation_status_value_error()


# endregion
##############################################################################
# End of Service: Lists
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_CreateListItemsReqItem:
    """
    Test Class for CreateListItemsReqItem
    """

    def test_create_list_items_req_item_serialization(self):
        """
        Test serialization/deserialization for CreateListItemsReqItem
        """

        # Construct a json representation of a CreateListItemsReqItem model
        create_list_items_req_item_model_json = {}
        create_list_items_req_item_model_json['asn'] = 19604
        create_list_items_req_item_model_json['comment'] = 'My list of developer IPs.'
        create_list_items_req_item_model_json['hostname'] = 'cloud.ibm.com'
        create_list_items_req_item_model_json['ip'] = '172.64.0.0/13'

        # Construct a model instance of CreateListItemsReqItem by calling from_dict on the json representation
        create_list_items_req_item_model = CreateListItemsReqItem.from_dict(create_list_items_req_item_model_json)
        assert create_list_items_req_item_model != False

        # Construct a model instance of CreateListItemsReqItem by calling from_dict on the json representation
        create_list_items_req_item_model_dict = CreateListItemsReqItem.from_dict(create_list_items_req_item_model_json).__dict__
        create_list_items_req_item_model2 = CreateListItemsReqItem(**create_list_items_req_item_model_dict)

        # Verify the model instances are equivalent
        assert create_list_items_req_item_model == create_list_items_req_item_model2

        # Convert model instance back to dict and verify no loss of data
        create_list_items_req_item_model_json2 = create_list_items_req_item_model.to_dict()
        assert create_list_items_req_item_model_json2 == create_list_items_req_item_model_json


class TestModel_DeleteListItemsReqItemsItem:
    """
    Test Class for DeleteListItemsReqItemsItem
    """

    def test_delete_list_items_req_items_item_serialization(self):
        """
        Test serialization/deserialization for DeleteListItemsReqItemsItem
        """

        # Construct a json representation of a DeleteListItemsReqItemsItem model
        delete_list_items_req_items_item_model_json = {}
        delete_list_items_req_items_item_model_json['id'] = '70c2009751b24ffc9ed1ab462ba957b4'

        # Construct a model instance of DeleteListItemsReqItemsItem by calling from_dict on the json representation
        delete_list_items_req_items_item_model = DeleteListItemsReqItemsItem.from_dict(delete_list_items_req_items_item_model_json)
        assert delete_list_items_req_items_item_model != False

        # Construct a model instance of DeleteListItemsReqItemsItem by calling from_dict on the json representation
        delete_list_items_req_items_item_model_dict = DeleteListItemsReqItemsItem.from_dict(delete_list_items_req_items_item_model_json).__dict__
        delete_list_items_req_items_item_model2 = DeleteListItemsReqItemsItem(**delete_list_items_req_items_item_model_dict)

        # Verify the model instances are equivalent
        assert delete_list_items_req_items_item_model == delete_list_items_req_items_item_model2

        # Convert model instance back to dict and verify no loss of data
        delete_list_items_req_items_item_model_json2 = delete_list_items_req_items_item_model.to_dict()
        assert delete_list_items_req_items_item_model_json2 == delete_list_items_req_items_item_model_json


class TestModel_DeleteResourceRespResult:
    """
    Test Class for DeleteResourceRespResult
    """

    def test_delete_resource_resp_result_serialization(self):
        """
        Test serialization/deserialization for DeleteResourceRespResult
        """

        # Construct a json representation of a DeleteResourceRespResult model
        delete_resource_resp_result_model_json = {}
        delete_resource_resp_result_model_json['id'] = '34b12448945f11eaa1b71c4d701ab86e'

        # Construct a model instance of DeleteResourceRespResult by calling from_dict on the json representation
        delete_resource_resp_result_model = DeleteResourceRespResult.from_dict(delete_resource_resp_result_model_json)
        assert delete_resource_resp_result_model != False

        # Construct a model instance of DeleteResourceRespResult by calling from_dict on the json representation
        delete_resource_resp_result_model_dict = DeleteResourceRespResult.from_dict(delete_resource_resp_result_model_json).__dict__
        delete_resource_resp_result_model2 = DeleteResourceRespResult(**delete_resource_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert delete_resource_resp_result_model == delete_resource_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        delete_resource_resp_result_model_json2 = delete_resource_resp_result_model.to_dict()
        assert delete_resource_resp_result_model_json2 == delete_resource_resp_result_model_json


class TestModel_ListOperationRespResult:
    """
    Test Class for ListOperationRespResult
    """

    def test_list_operation_resp_result_serialization(self):
        """
        Test serialization/deserialization for ListOperationRespResult
        """

        # Construct a json representation of a ListOperationRespResult model
        list_operation_resp_result_model_json = {}
        list_operation_resp_result_model_json['operation_id'] = '53d73a83d33d4e3b8791764a9b9f2412'

        # Construct a model instance of ListOperationRespResult by calling from_dict on the json representation
        list_operation_resp_result_model = ListOperationRespResult.from_dict(list_operation_resp_result_model_json)
        assert list_operation_resp_result_model != False

        # Construct a model instance of ListOperationRespResult by calling from_dict on the json representation
        list_operation_resp_result_model_dict = ListOperationRespResult.from_dict(list_operation_resp_result_model_json).__dict__
        list_operation_resp_result_model2 = ListOperationRespResult(**list_operation_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert list_operation_resp_result_model == list_operation_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        list_operation_resp_result_model_json2 = list_operation_resp_result_model.to_dict()
        assert list_operation_resp_result_model_json2 == list_operation_resp_result_model_json


class TestModel_ManagedListsResultItem:
    """
    Test Class for ManagedListsResultItem
    """

    def test_managed_lists_result_item_serialization(self):
        """
        Test serialization/deserialization for ManagedListsResultItem
        """

        # Construct a json representation of a ManagedListsResultItem model
        managed_lists_result_item_model_json = {}
        managed_lists_result_item_model_json['name'] = 'cf.malware'
        managed_lists_result_item_model_json['description'] = 'testString'
        managed_lists_result_item_model_json['kind'] = 'ip'

        # Construct a model instance of ManagedListsResultItem by calling from_dict on the json representation
        managed_lists_result_item_model = ManagedListsResultItem.from_dict(managed_lists_result_item_model_json)
        assert managed_lists_result_item_model != False

        # Construct a model instance of ManagedListsResultItem by calling from_dict on the json representation
        managed_lists_result_item_model_dict = ManagedListsResultItem.from_dict(managed_lists_result_item_model_json).__dict__
        managed_lists_result_item_model2 = ManagedListsResultItem(**managed_lists_result_item_model_dict)

        # Verify the model instances are equivalent
        assert managed_lists_result_item_model == managed_lists_result_item_model2

        # Convert model instance back to dict and verify no loss of data
        managed_lists_result_item_model_json2 = managed_lists_result_item_model.to_dict()
        assert managed_lists_result_item_model_json2 == managed_lists_result_item_model_json


class TestModel_OperationStatusRespResult:
    """
    Test Class for OperationStatusRespResult
    """

    def test_operation_status_resp_result_serialization(self):
        """
        Test serialization/deserialization for OperationStatusRespResult
        """

        # Construct a json representation of a OperationStatusRespResult model
        operation_status_resp_result_model_json = {}
        operation_status_resp_result_model_json['id'] = '0147be950d5c42b8b47c07792c5015e3'
        operation_status_resp_result_model_json['status'] = 'completed'
        operation_status_resp_result_model_json['completed'] = '2025-03-21T16:07:41.782564Z'
        operation_status_resp_result_model_json['error'] = 'testString'

        # Construct a model instance of OperationStatusRespResult by calling from_dict on the json representation
        operation_status_resp_result_model = OperationStatusRespResult.from_dict(operation_status_resp_result_model_json)
        assert operation_status_resp_result_model != False

        # Construct a model instance of OperationStatusRespResult by calling from_dict on the json representation
        operation_status_resp_result_model_dict = OperationStatusRespResult.from_dict(operation_status_resp_result_model_json).__dict__
        operation_status_resp_result_model2 = OperationStatusRespResult(**operation_status_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert operation_status_resp_result_model == operation_status_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        operation_status_resp_result_model_json2 = operation_status_resp_result_model.to_dict()
        assert operation_status_resp_result_model_json2 == operation_status_resp_result_model_json


class TestModel_CustomListResp:
    """
    Test Class for CustomListResp
    """

    def test_custom_list_resp_serialization(self):
        """
        Test serialization/deserialization for CustomListResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        custom_list_result_model = {}  # CustomListResult
        custom_list_result_model['name'] = 'good_ips'
        custom_list_result_model['id'] = 'testString'
        custom_list_result_model['description'] = 'testString'
        custom_list_result_model['kind'] = 'ip'
        custom_list_result_model['num_items'] = 10
        custom_list_result_model['num_referencing_filters'] = 5

        # Construct a json representation of a CustomListResp model
        custom_list_resp_model_json = {}
        custom_list_resp_model_json['success'] = True
        custom_list_resp_model_json['errors'] = [['testString']]
        custom_list_resp_model_json['messages'] = [['testString']]
        custom_list_resp_model_json['result'] = custom_list_result_model

        # Construct a model instance of CustomListResp by calling from_dict on the json representation
        custom_list_resp_model = CustomListResp.from_dict(custom_list_resp_model_json)
        assert custom_list_resp_model != False

        # Construct a model instance of CustomListResp by calling from_dict on the json representation
        custom_list_resp_model_dict = CustomListResp.from_dict(custom_list_resp_model_json).__dict__
        custom_list_resp_model2 = CustomListResp(**custom_list_resp_model_dict)

        # Verify the model instances are equivalent
        assert custom_list_resp_model == custom_list_resp_model2

        # Convert model instance back to dict and verify no loss of data
        custom_list_resp_model_json2 = custom_list_resp_model.to_dict()
        assert custom_list_resp_model_json2 == custom_list_resp_model_json


class TestModel_CustomListResult:
    """
    Test Class for CustomListResult
    """

    def test_custom_list_result_serialization(self):
        """
        Test serialization/deserialization for CustomListResult
        """

        # Construct a json representation of a CustomListResult model
        custom_list_result_model_json = {}
        custom_list_result_model_json['name'] = 'good_ips'
        custom_list_result_model_json['id'] = 'testString'
        custom_list_result_model_json['description'] = 'testString'
        custom_list_result_model_json['kind'] = 'ip'
        custom_list_result_model_json['num_items'] = 10
        custom_list_result_model_json['num_referencing_filters'] = 5

        # Construct a model instance of CustomListResult by calling from_dict on the json representation
        custom_list_result_model = CustomListResult.from_dict(custom_list_result_model_json)
        assert custom_list_result_model != False

        # Construct a model instance of CustomListResult by calling from_dict on the json representation
        custom_list_result_model_dict = CustomListResult.from_dict(custom_list_result_model_json).__dict__
        custom_list_result_model2 = CustomListResult(**custom_list_result_model_dict)

        # Verify the model instances are equivalent
        assert custom_list_result_model == custom_list_result_model2

        # Convert model instance back to dict and verify no loss of data
        custom_list_result_model_json2 = custom_list_result_model.to_dict()
        assert custom_list_result_model_json2 == custom_list_result_model_json


class TestModel_CustomListsResp:
    """
    Test Class for CustomListsResp
    """

    def test_custom_lists_resp_serialization(self):
        """
        Test serialization/deserialization for CustomListsResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        custom_list_result_model = {}  # CustomListResult
        custom_list_result_model['name'] = 'good_ips'
        custom_list_result_model['id'] = 'testString'
        custom_list_result_model['description'] = 'testString'
        custom_list_result_model['kind'] = 'ip'
        custom_list_result_model['num_items'] = 10
        custom_list_result_model['num_referencing_filters'] = 5

        # Construct a json representation of a CustomListsResp model
        custom_lists_resp_model_json = {}
        custom_lists_resp_model_json['success'] = True
        custom_lists_resp_model_json['errors'] = [['testString']]
        custom_lists_resp_model_json['messages'] = [['testString']]
        custom_lists_resp_model_json['result'] = [custom_list_result_model]

        # Construct a model instance of CustomListsResp by calling from_dict on the json representation
        custom_lists_resp_model = CustomListsResp.from_dict(custom_lists_resp_model_json)
        assert custom_lists_resp_model != False

        # Construct a model instance of CustomListsResp by calling from_dict on the json representation
        custom_lists_resp_model_dict = CustomListsResp.from_dict(custom_lists_resp_model_json).__dict__
        custom_lists_resp_model2 = CustomListsResp(**custom_lists_resp_model_dict)

        # Verify the model instances are equivalent
        assert custom_lists_resp_model == custom_lists_resp_model2

        # Convert model instance back to dict and verify no loss of data
        custom_lists_resp_model_json2 = custom_lists_resp_model.to_dict()
        assert custom_lists_resp_model_json2 == custom_lists_resp_model_json


class TestModel_DeleteResourceResp:
    """
    Test Class for DeleteResourceResp
    """

    def test_delete_resource_resp_serialization(self):
        """
        Test serialization/deserialization for DeleteResourceResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        delete_resource_resp_result_model = {}  # DeleteResourceRespResult
        delete_resource_resp_result_model['id'] = '34b12448945f11eaa1b71c4d701ab86e'

        # Construct a json representation of a DeleteResourceResp model
        delete_resource_resp_model_json = {}
        delete_resource_resp_model_json['success'] = True
        delete_resource_resp_model_json['errors'] = [['testString']]
        delete_resource_resp_model_json['messages'] = [['testString']]
        delete_resource_resp_model_json['result'] = delete_resource_resp_result_model

        # Construct a model instance of DeleteResourceResp by calling from_dict on the json representation
        delete_resource_resp_model = DeleteResourceResp.from_dict(delete_resource_resp_model_json)
        assert delete_resource_resp_model != False

        # Construct a model instance of DeleteResourceResp by calling from_dict on the json representation
        delete_resource_resp_model_dict = DeleteResourceResp.from_dict(delete_resource_resp_model_json).__dict__
        delete_resource_resp_model2 = DeleteResourceResp(**delete_resource_resp_model_dict)

        # Verify the model instances are equivalent
        assert delete_resource_resp_model == delete_resource_resp_model2

        # Convert model instance back to dict and verify no loss of data
        delete_resource_resp_model_json2 = delete_resource_resp_model.to_dict()
        assert delete_resource_resp_model_json2 == delete_resource_resp_model_json


class TestModel_ListCursor:
    """
    Test Class for ListCursor
    """

    def test_list_cursor_serialization(self):
        """
        Test serialization/deserialization for ListCursor
        """

        # Construct a json representation of a ListCursor model
        list_cursor_model_json = {}
        list_cursor_model_json['after'] = 'yyy'
        list_cursor_model_json['before'] = 'xxx'

        # Construct a model instance of ListCursor by calling from_dict on the json representation
        list_cursor_model = ListCursor.from_dict(list_cursor_model_json)
        assert list_cursor_model != False

        # Construct a model instance of ListCursor by calling from_dict on the json representation
        list_cursor_model_dict = ListCursor.from_dict(list_cursor_model_json).__dict__
        list_cursor_model2 = ListCursor(**list_cursor_model_dict)

        # Verify the model instances are equivalent
        assert list_cursor_model == list_cursor_model2

        # Convert model instance back to dict and verify no loss of data
        list_cursor_model_json2 = list_cursor_model.to_dict()
        assert list_cursor_model_json2 == list_cursor_model_json


class TestModel_ListItem:
    """
    Test Class for ListItem
    """

    def test_list_item_serialization(self):
        """
        Test serialization/deserialization for ListItem
        """

        # Construct a json representation of a ListItem model
        list_item_model_json = {}
        list_item_model_json['id'] = '70c2009751b24ffc9ed1ab462ba957b4'
        list_item_model_json['asn'] = 19604
        list_item_model_json['comment'] = 'My list of developer IPs.'
        list_item_model_json['hostname'] = 'cloud.ibm.com'
        list_item_model_json['ip'] = '172.64.0.0/13'
        list_item_model_json['created_on'] = '2025-03-21T16:19:21Z'
        list_item_model_json['modified_on'] = '2025-03-21T16:19:37Z'

        # Construct a model instance of ListItem by calling from_dict on the json representation
        list_item_model = ListItem.from_dict(list_item_model_json)
        assert list_item_model != False

        # Construct a model instance of ListItem by calling from_dict on the json representation
        list_item_model_dict = ListItem.from_dict(list_item_model_json).__dict__
        list_item_model2 = ListItem(**list_item_model_dict)

        # Verify the model instances are equivalent
        assert list_item_model == list_item_model2

        # Convert model instance back to dict and verify no loss of data
        list_item_model_json2 = list_item_model.to_dict()
        assert list_item_model_json2 == list_item_model_json


class TestModel_ListItemResp:
    """
    Test Class for ListItemResp
    """

    def test_list_item_resp_serialization(self):
        """
        Test serialization/deserialization for ListItemResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        list_item_model = {}  # ListItem
        list_item_model['id'] = '70c2009751b24ffc9ed1ab462ba957b4'
        list_item_model['asn'] = 19604
        list_item_model['comment'] = 'My list of developer IPs.'
        list_item_model['hostname'] = 'cloud.ibm.com'
        list_item_model['ip'] = '172.64.0.0/13'
        list_item_model['created_on'] = '2025-03-21T16:19:21Z'
        list_item_model['modified_on'] = '2025-03-21T16:19:37Z'

        # Construct a json representation of a ListItemResp model
        list_item_resp_model_json = {}
        list_item_resp_model_json['success'] = True
        list_item_resp_model_json['errors'] = [['testString']]
        list_item_resp_model_json['messages'] = [['testString']]
        list_item_resp_model_json['result'] = list_item_model

        # Construct a model instance of ListItemResp by calling from_dict on the json representation
        list_item_resp_model = ListItemResp.from_dict(list_item_resp_model_json)
        assert list_item_resp_model != False

        # Construct a model instance of ListItemResp by calling from_dict on the json representation
        list_item_resp_model_dict = ListItemResp.from_dict(list_item_resp_model_json).__dict__
        list_item_resp_model2 = ListItemResp(**list_item_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_item_resp_model == list_item_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_item_resp_model_json2 = list_item_resp_model.to_dict()
        assert list_item_resp_model_json2 == list_item_resp_model_json


class TestModel_ListItemsResp:
    """
    Test Class for ListItemsResp
    """

    def test_list_items_resp_serialization(self):
        """
        Test serialization/deserialization for ListItemsResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        list_item_model = {}  # ListItem
        list_item_model['id'] = '70c2009751b24ffc9ed1ab462ba957b4'
        list_item_model['asn'] = 19604
        list_item_model['comment'] = 'My list of developer IPs.'
        list_item_model['hostname'] = 'cloud.ibm.com'
        list_item_model['ip'] = '172.64.0.0/13'
        list_item_model['created_on'] = '2025-03-21T16:19:21Z'
        list_item_model['modified_on'] = '2025-03-21T16:19:37Z'

        list_cursor_model = {}  # ListCursor
        list_cursor_model['after'] = 'yyy'
        list_cursor_model['before'] = 'xxx'

        list_items_result_info_model = {}  # ListItemsResultInfo
        list_items_result_info_model['cursors'] = list_cursor_model

        # Construct a json representation of a ListItemsResp model
        list_items_resp_model_json = {}
        list_items_resp_model_json['success'] = True
        list_items_resp_model_json['errors'] = [['testString']]
        list_items_resp_model_json['messages'] = [['testString']]
        list_items_resp_model_json['result'] = [list_item_model]
        list_items_resp_model_json['result_info'] = list_items_result_info_model

        # Construct a model instance of ListItemsResp by calling from_dict on the json representation
        list_items_resp_model = ListItemsResp.from_dict(list_items_resp_model_json)
        assert list_items_resp_model != False

        # Construct a model instance of ListItemsResp by calling from_dict on the json representation
        list_items_resp_model_dict = ListItemsResp.from_dict(list_items_resp_model_json).__dict__
        list_items_resp_model2 = ListItemsResp(**list_items_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_items_resp_model == list_items_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_items_resp_model_json2 = list_items_resp_model.to_dict()
        assert list_items_resp_model_json2 == list_items_resp_model_json


class TestModel_ListItemsResultInfo:
    """
    Test Class for ListItemsResultInfo
    """

    def test_list_items_result_info_serialization(self):
        """
        Test serialization/deserialization for ListItemsResultInfo
        """

        # Construct dict forms of any model objects needed in order to build this model.

        list_cursor_model = {}  # ListCursor
        list_cursor_model['after'] = 'yyy'
        list_cursor_model['before'] = 'xxx'

        # Construct a json representation of a ListItemsResultInfo model
        list_items_result_info_model_json = {}
        list_items_result_info_model_json['cursors'] = list_cursor_model

        # Construct a model instance of ListItemsResultInfo by calling from_dict on the json representation
        list_items_result_info_model = ListItemsResultInfo.from_dict(list_items_result_info_model_json)
        assert list_items_result_info_model != False

        # Construct a model instance of ListItemsResultInfo by calling from_dict on the json representation
        list_items_result_info_model_dict = ListItemsResultInfo.from_dict(list_items_result_info_model_json).__dict__
        list_items_result_info_model2 = ListItemsResultInfo(**list_items_result_info_model_dict)

        # Verify the model instances are equivalent
        assert list_items_result_info_model == list_items_result_info_model2

        # Convert model instance back to dict and verify no loss of data
        list_items_result_info_model_json2 = list_items_result_info_model.to_dict()
        assert list_items_result_info_model_json2 == list_items_result_info_model_json


class TestModel_ListOperationResp:
    """
    Test Class for ListOperationResp
    """

    def test_list_operation_resp_serialization(self):
        """
        Test serialization/deserialization for ListOperationResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        list_operation_resp_result_model = {}  # ListOperationRespResult
        list_operation_resp_result_model['operation_id'] = '53d73a83d33d4e3b8791764a9b9f2412'

        # Construct a json representation of a ListOperationResp model
        list_operation_resp_model_json = {}
        list_operation_resp_model_json['success'] = True
        list_operation_resp_model_json['errors'] = [['testString']]
        list_operation_resp_model_json['messages'] = [['testString']]
        list_operation_resp_model_json['result'] = list_operation_resp_result_model

        # Construct a model instance of ListOperationResp by calling from_dict on the json representation
        list_operation_resp_model = ListOperationResp.from_dict(list_operation_resp_model_json)
        assert list_operation_resp_model != False

        # Construct a model instance of ListOperationResp by calling from_dict on the json representation
        list_operation_resp_model_dict = ListOperationResp.from_dict(list_operation_resp_model_json).__dict__
        list_operation_resp_model2 = ListOperationResp(**list_operation_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_operation_resp_model == list_operation_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_operation_resp_model_json2 = list_operation_resp_model.to_dict()
        assert list_operation_resp_model_json2 == list_operation_resp_model_json


class TestModel_ManagedListsResp:
    """
    Test Class for ManagedListsResp
    """

    def test_managed_lists_resp_serialization(self):
        """
        Test serialization/deserialization for ManagedListsResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        managed_lists_result_item_model = {}  # ManagedListsResultItem
        managed_lists_result_item_model['name'] = 'cf.malware'
        managed_lists_result_item_model['description'] = 'testString'
        managed_lists_result_item_model['kind'] = 'ip'

        # Construct a json representation of a ManagedListsResp model
        managed_lists_resp_model_json = {}
        managed_lists_resp_model_json['success'] = True
        managed_lists_resp_model_json['errors'] = [['testString']]
        managed_lists_resp_model_json['messages'] = [['testString']]
        managed_lists_resp_model_json['result'] = [managed_lists_result_item_model]

        # Construct a model instance of ManagedListsResp by calling from_dict on the json representation
        managed_lists_resp_model = ManagedListsResp.from_dict(managed_lists_resp_model_json)
        assert managed_lists_resp_model != False

        # Construct a model instance of ManagedListsResp by calling from_dict on the json representation
        managed_lists_resp_model_dict = ManagedListsResp.from_dict(managed_lists_resp_model_json).__dict__
        managed_lists_resp_model2 = ManagedListsResp(**managed_lists_resp_model_dict)

        # Verify the model instances are equivalent
        assert managed_lists_resp_model == managed_lists_resp_model2

        # Convert model instance back to dict and verify no loss of data
        managed_lists_resp_model_json2 = managed_lists_resp_model.to_dict()
        assert managed_lists_resp_model_json2 == managed_lists_resp_model_json


class TestModel_OperationStatusResp:
    """
    Test Class for OperationStatusResp
    """

    def test_operation_status_resp_serialization(self):
        """
        Test serialization/deserialization for OperationStatusResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        operation_status_resp_result_model = {}  # OperationStatusRespResult
        operation_status_resp_result_model['id'] = '0147be950d5c42b8b47c07792c5015e3'
        operation_status_resp_result_model['status'] = 'completed'
        operation_status_resp_result_model['completed'] = '2025-03-21T16:07:41.782564Z'
        operation_status_resp_result_model['error'] = 'testString'

        # Construct a json representation of a OperationStatusResp model
        operation_status_resp_model_json = {}
        operation_status_resp_model_json['success'] = True
        operation_status_resp_model_json['errors'] = [['testString']]
        operation_status_resp_model_json['messages'] = [['testString']]
        operation_status_resp_model_json['result'] = operation_status_resp_result_model

        # Construct a model instance of OperationStatusResp by calling from_dict on the json representation
        operation_status_resp_model = OperationStatusResp.from_dict(operation_status_resp_model_json)
        assert operation_status_resp_model != False

        # Construct a model instance of OperationStatusResp by calling from_dict on the json representation
        operation_status_resp_model_dict = OperationStatusResp.from_dict(operation_status_resp_model_json).__dict__
        operation_status_resp_model2 = OperationStatusResp(**operation_status_resp_model_dict)

        # Verify the model instances are equivalent
        assert operation_status_resp_model == operation_status_resp_model2

        # Convert model instance back to dict and verify no loss of data
        operation_status_resp_model_json2 = operation_status_resp_model.to_dict()
        assert operation_status_resp_model_json2 == operation_status_resp_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
