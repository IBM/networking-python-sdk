# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2022.
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
Unit Tests for DnsSvcsV1
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import inspect
import io
import json
import os
import pytest
import re
import requests
import responses
import tempfile
import urllib
# from github.ibm.com/ibmcloud/networking-python-sdk.dns_svcs_v1 import *
from ibm_cloud_networking_services.dns_svcs_v1 import *

_service = DnsSvcsV1(
    authenticator=NoAuthAuthenticator()
)

_base_url = 'https://api.dns-svcs.cloud.ibm.com/v1'
_service.set_service_url(_base_url)


def preprocess_url(operation_path: str):
    """
    Returns the request url associated with the specified operation path.
    This will be base_url concatenated with a quoted version of operation_path.
    The returned request URL is used to register the mock response so it needs
    to match the request URL that is formed by the requests library.
    """
    # First, unquote the path since it might have some quoted/escaped characters in it
    # due to how the generator inserts the operation paths into the unit test code.
    operation_path = urllib.parse.unquote(operation_path)

    # Next, quote the path using urllib so that we approximate what will
    # happen during request processing.
    operation_path = urllib.parse.quote(operation_path, safe='/')

    # Finally, form the request URL from the base URL and operation path.
    request_url = _base_url + operation_path

    # If the request url does NOT end with a /, then just return it as-is.
    # Otherwise, return a regular expression that matches one or more trailing /.
    if re.fullmatch('.*/+', request_url) is None:
        return request_url
    else:
        return re.compile(request_url.rstrip('/') + '/+')


##############################################################################
# Start of Service: DNSZones
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = DnsSvcsV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DnsSvcsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DnsSvcsV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestListDnszones():
    """
    Test Class for list_dnszones
    """

    @responses.activate
    def test_list_dnszones_all_params(self):
        """
        list_dnszones()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones')
        mock_response = '{"dnszones": [{"id": "2d0f862b-67cc-41f3-b6a2-59860d0aa90e", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "instance_id": "1407a753-a93f-4bb0-9784-bcfc269ee1b3", "name": "example.com", "description": "The DNS zone is used for VPCs in us-east region", "state": "pending_network_add", "label": "us-east"}], "offset": 0, "limit": 200, "count": 1, "total_count": 1, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "last": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "previous": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        x_correlation_id = 'testString'
        offset = 38
        limit = 200

        # Invoke method
        response = _service.list_dnszones(
            instance_id,
            x_correlation_id=x_correlation_id,
            offset=offset,
            limit=limit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'offset={}'.format(offset) in query_string
        assert 'limit={}'.format(limit) in query_string

    def test_list_dnszones_all_params_with_retries(self):
        # Enable retries and run test_list_dnszones_all_params.
        _service.enable_retries()
        self.test_list_dnszones_all_params()

        # Disable retries and run test_list_dnszones_all_params.
        _service.disable_retries()
        self.test_list_dnszones_all_params()

    @responses.activate
    def test_list_dnszones_required_params(self):
        """
        test_list_dnszones_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones')
        mock_response = '{"dnszones": [{"id": "2d0f862b-67cc-41f3-b6a2-59860d0aa90e", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "instance_id": "1407a753-a93f-4bb0-9784-bcfc269ee1b3", "name": "example.com", "description": "The DNS zone is used for VPCs in us-east region", "state": "pending_network_add", "label": "us-east"}], "offset": 0, "limit": 200, "count": 1, "total_count": 1, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "last": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "previous": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.list_dnszones(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_dnszones_required_params_with_retries(self):
        # Enable retries and run test_list_dnszones_required_params.
        _service.enable_retries()
        self.test_list_dnszones_required_params()

        # Disable retries and run test_list_dnszones_required_params.
        _service.disable_retries()
        self.test_list_dnszones_required_params()

    @responses.activate
    def test_list_dnszones_value_error(self):
        """
        test_list_dnszones_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones')
        mock_response = '{"dnszones": [{"id": "2d0f862b-67cc-41f3-b6a2-59860d0aa90e", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "instance_id": "1407a753-a93f-4bb0-9784-bcfc269ee1b3", "name": "example.com", "description": "The DNS zone is used for VPCs in us-east region", "state": "pending_network_add", "label": "us-east"}], "offset": 0, "limit": 200, "count": 1, "total_count": 1, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "last": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "previous": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_dnszones(**req_copy)


    def test_list_dnszones_value_error_with_retries(self):
        # Enable retries and run test_list_dnszones_value_error.
        _service.enable_retries()
        self.test_list_dnszones_value_error()

        # Disable retries and run test_list_dnszones_value_error.
        _service.disable_retries()
        self.test_list_dnszones_value_error()

class TestCreateDnszone():
    """
    Test Class for create_dnszone
    """

    @responses.activate
    def test_create_dnszone_all_params(self):
        """
        create_dnszone()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones')
        mock_response = '{"id": "2d0f862b-67cc-41f3-b6a2-59860d0aa90e", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "instance_id": "1407a753-a93f-4bb0-9784-bcfc269ee1b3", "name": "example.com", "description": "The DNS zone is used for VPCs in us-east region", "state": "pending_network_add", "label": "us-east"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        name = 'example.com'
        description = 'The DNS zone is used for VPCs in us-east region'
        label = 'us-east'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.create_dnszone(
            instance_id,
            name=name,
            description=description,
            label=label,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'example.com'
        assert req_body['description'] == 'The DNS zone is used for VPCs in us-east region'
        assert req_body['label'] == 'us-east'

    def test_create_dnszone_all_params_with_retries(self):
        # Enable retries and run test_create_dnszone_all_params.
        _service.enable_retries()
        self.test_create_dnszone_all_params()

        # Disable retries and run test_create_dnszone_all_params.
        _service.disable_retries()
        self.test_create_dnszone_all_params()

    @responses.activate
    def test_create_dnszone_required_params(self):
        """
        test_create_dnszone_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones')
        mock_response = '{"id": "2d0f862b-67cc-41f3-b6a2-59860d0aa90e", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "instance_id": "1407a753-a93f-4bb0-9784-bcfc269ee1b3", "name": "example.com", "description": "The DNS zone is used for VPCs in us-east region", "state": "pending_network_add", "label": "us-east"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.create_dnszone(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_dnszone_required_params_with_retries(self):
        # Enable retries and run test_create_dnszone_required_params.
        _service.enable_retries()
        self.test_create_dnszone_required_params()

        # Disable retries and run test_create_dnszone_required_params.
        _service.disable_retries()
        self.test_create_dnszone_required_params()

    @responses.activate
    def test_create_dnszone_value_error(self):
        """
        test_create_dnszone_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones')
        mock_response = '{"id": "2d0f862b-67cc-41f3-b6a2-59860d0aa90e", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "instance_id": "1407a753-a93f-4bb0-9784-bcfc269ee1b3", "name": "example.com", "description": "The DNS zone is used for VPCs in us-east region", "state": "pending_network_add", "label": "us-east"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_dnszone(**req_copy)


    def test_create_dnszone_value_error_with_retries(self):
        # Enable retries and run test_create_dnszone_value_error.
        _service.enable_retries()
        self.test_create_dnszone_value_error()

        # Disable retries and run test_create_dnszone_value_error.
        _service.disable_retries()
        self.test_create_dnszone_value_error()

class TestDeleteDnszone():
    """
    Test Class for delete_dnszone
    """

    @responses.activate
    def test_delete_dnszone_all_params(self):
        """
        delete_dnszone()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.delete_dnszone(
            instance_id,
            dnszone_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_dnszone_all_params_with_retries(self):
        # Enable retries and run test_delete_dnszone_all_params.
        _service.enable_retries()
        self.test_delete_dnszone_all_params()

        # Disable retries and run test_delete_dnszone_all_params.
        _service.disable_retries()
        self.test_delete_dnszone_all_params()

    @responses.activate
    def test_delete_dnszone_required_params(self):
        """
        test_delete_dnszone_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Invoke method
        response = _service.delete_dnszone(
            instance_id,
            dnszone_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_dnszone_required_params_with_retries(self):
        # Enable retries and run test_delete_dnszone_required_params.
        _service.enable_retries()
        self.test_delete_dnszone_required_params()

        # Disable retries and run test_delete_dnszone_required_params.
        _service.disable_retries()
        self.test_delete_dnszone_required_params()

    @responses.activate
    def test_delete_dnszone_value_error(self):
        """
        test_delete_dnszone_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_dnszone(**req_copy)


    def test_delete_dnszone_value_error_with_retries(self):
        # Enable retries and run test_delete_dnszone_value_error.
        _service.enable_retries()
        self.test_delete_dnszone_value_error()

        # Disable retries and run test_delete_dnszone_value_error.
        _service.disable_retries()
        self.test_delete_dnszone_value_error()

class TestGetDnszone():
    """
    Test Class for get_dnszone
    """

    @responses.activate
    def test_get_dnszone_all_params(self):
        """
        get_dnszone()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString')
        mock_response = '{"id": "2d0f862b-67cc-41f3-b6a2-59860d0aa90e", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "instance_id": "1407a753-a93f-4bb0-9784-bcfc269ee1b3", "name": "example.com", "description": "The DNS zone is used for VPCs in us-east region", "state": "pending_network_add", "label": "us-east"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.get_dnszone(
            instance_id,
            dnszone_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_dnszone_all_params_with_retries(self):
        # Enable retries and run test_get_dnszone_all_params.
        _service.enable_retries()
        self.test_get_dnszone_all_params()

        # Disable retries and run test_get_dnszone_all_params.
        _service.disable_retries()
        self.test_get_dnszone_all_params()

    @responses.activate
    def test_get_dnszone_required_params(self):
        """
        test_get_dnszone_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString')
        mock_response = '{"id": "2d0f862b-67cc-41f3-b6a2-59860d0aa90e", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "instance_id": "1407a753-a93f-4bb0-9784-bcfc269ee1b3", "name": "example.com", "description": "The DNS zone is used for VPCs in us-east region", "state": "pending_network_add", "label": "us-east"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Invoke method
        response = _service.get_dnszone(
            instance_id,
            dnszone_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_dnszone_required_params_with_retries(self):
        # Enable retries and run test_get_dnszone_required_params.
        _service.enable_retries()
        self.test_get_dnszone_required_params()

        # Disable retries and run test_get_dnszone_required_params.
        _service.disable_retries()
        self.test_get_dnszone_required_params()

    @responses.activate
    def test_get_dnszone_value_error(self):
        """
        test_get_dnszone_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString')
        mock_response = '{"id": "2d0f862b-67cc-41f3-b6a2-59860d0aa90e", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "instance_id": "1407a753-a93f-4bb0-9784-bcfc269ee1b3", "name": "example.com", "description": "The DNS zone is used for VPCs in us-east region", "state": "pending_network_add", "label": "us-east"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_dnszone(**req_copy)


    def test_get_dnszone_value_error_with_retries(self):
        # Enable retries and run test_get_dnszone_value_error.
        _service.enable_retries()
        self.test_get_dnszone_value_error()

        # Disable retries and run test_get_dnszone_value_error.
        _service.disable_retries()
        self.test_get_dnszone_value_error()

class TestUpdateDnszone():
    """
    Test Class for update_dnszone
    """

    @responses.activate
    def test_update_dnszone_all_params(self):
        """
        update_dnszone()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString')
        mock_response = '{"id": "2d0f862b-67cc-41f3-b6a2-59860d0aa90e", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "instance_id": "1407a753-a93f-4bb0-9784-bcfc269ee1b3", "name": "example.com", "description": "The DNS zone is used for VPCs in us-east region", "state": "pending_network_add", "label": "us-east"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        description = 'The DNS zone is used for VPCs in us-east region'
        label = 'us-east'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.update_dnszone(
            instance_id,
            dnszone_id,
            description=description,
            label=label,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['description'] == 'The DNS zone is used for VPCs in us-east region'
        assert req_body['label'] == 'us-east'

    def test_update_dnszone_all_params_with_retries(self):
        # Enable retries and run test_update_dnszone_all_params.
        _service.enable_retries()
        self.test_update_dnszone_all_params()

        # Disable retries and run test_update_dnszone_all_params.
        _service.disable_retries()
        self.test_update_dnszone_all_params()

    @responses.activate
    def test_update_dnszone_required_params(self):
        """
        test_update_dnszone_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString')
        mock_response = '{"id": "2d0f862b-67cc-41f3-b6a2-59860d0aa90e", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "instance_id": "1407a753-a93f-4bb0-9784-bcfc269ee1b3", "name": "example.com", "description": "The DNS zone is used for VPCs in us-east region", "state": "pending_network_add", "label": "us-east"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Invoke method
        response = _service.update_dnszone(
            instance_id,
            dnszone_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_dnszone_required_params_with_retries(self):
        # Enable retries and run test_update_dnszone_required_params.
        _service.enable_retries()
        self.test_update_dnszone_required_params()

        # Disable retries and run test_update_dnszone_required_params.
        _service.disable_retries()
        self.test_update_dnszone_required_params()

    @responses.activate
    def test_update_dnszone_value_error(self):
        """
        test_update_dnszone_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString')
        mock_response = '{"id": "2d0f862b-67cc-41f3-b6a2-59860d0aa90e", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "instance_id": "1407a753-a93f-4bb0-9784-bcfc269ee1b3", "name": "example.com", "description": "The DNS zone is used for VPCs in us-east region", "state": "pending_network_add", "label": "us-east"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_dnszone(**req_copy)


    def test_update_dnszone_value_error_with_retries(self):
        # Enable retries and run test_update_dnszone_value_error.
        _service.enable_retries()
        self.test_update_dnszone_value_error()

        # Disable retries and run test_update_dnszone_value_error.
        _service.disable_retries()
        self.test_update_dnszone_value_error()

# endregion
##############################################################################
# End of Service: DNSZones
##############################################################################

##############################################################################
# Start of Service: ResourceRecords
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = DnsSvcsV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DnsSvcsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DnsSvcsV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestListResourceRecords():
    """
    Test Class for list_resource_records
    """

    @responses.activate
    def test_list_resource_records_all_params(self):
        """
        list_resource_records()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/resource_records')
        mock_response = '{"resource_records": [{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": {"anyKey": "anyValue"}, "service": "_sip", "protocol": "udp"}], "offset": 0, "limit": 200, "count": 1, "total_count": 1, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "last": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "previous": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        x_correlation_id = 'testString'
        offset = 38
        limit = 200

        # Invoke method
        response = _service.list_resource_records(
            instance_id,
            dnszone_id,
            x_correlation_id=x_correlation_id,
            offset=offset,
            limit=limit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'offset={}'.format(offset) in query_string
        assert 'limit={}'.format(limit) in query_string

    def test_list_resource_records_all_params_with_retries(self):
        # Enable retries and run test_list_resource_records_all_params.
        _service.enable_retries()
        self.test_list_resource_records_all_params()

        # Disable retries and run test_list_resource_records_all_params.
        _service.disable_retries()
        self.test_list_resource_records_all_params()

    @responses.activate
    def test_list_resource_records_required_params(self):
        """
        test_list_resource_records_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/resource_records')
        mock_response = '{"resource_records": [{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": {"anyKey": "anyValue"}, "service": "_sip", "protocol": "udp"}], "offset": 0, "limit": 200, "count": 1, "total_count": 1, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "last": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "previous": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Invoke method
        response = _service.list_resource_records(
            instance_id,
            dnszone_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_resource_records_required_params_with_retries(self):
        # Enable retries and run test_list_resource_records_required_params.
        _service.enable_retries()
        self.test_list_resource_records_required_params()

        # Disable retries and run test_list_resource_records_required_params.
        _service.disable_retries()
        self.test_list_resource_records_required_params()

    @responses.activate
    def test_list_resource_records_value_error(self):
        """
        test_list_resource_records_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/resource_records')
        mock_response = '{"resource_records": [{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": {"anyKey": "anyValue"}, "service": "_sip", "protocol": "udp"}], "offset": 0, "limit": 200, "count": 1, "total_count": 1, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "last": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "previous": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_resource_records(**req_copy)


    def test_list_resource_records_value_error_with_retries(self):
        # Enable retries and run test_list_resource_records_value_error.
        _service.enable_retries()
        self.test_list_resource_records_value_error()

        # Disable retries and run test_list_resource_records_value_error.
        _service.disable_retries()
        self.test_list_resource_records_value_error()

class TestCreateResourceRecord():
    """
    Test Class for create_resource_record
    """

    @responses.activate
    def test_create_resource_record_all_params(self):
        """
        create_resource_record()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/resource_records')
        mock_response = '{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": {"anyKey": "anyValue"}, "service": "_sip", "protocol": "udp"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ResourceRecordInputRdataRdataARecord model
        resource_record_input_rdata_model = {}
        resource_record_input_rdata_model['ip'] = '10.110.201.214'

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        type = 'SRV'
        name = 'test.example.com'
        rdata = resource_record_input_rdata_model
        ttl = 120
        service = '_sip'
        protocol = 'udp'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.create_resource_record(
            instance_id,
            dnszone_id,
            type=type,
            name=name,
            rdata=rdata,
            ttl=ttl,
            service=service,
            protocol=protocol,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'SRV'
        assert req_body['name'] == 'test.example.com'
        assert req_body['rdata'] == resource_record_input_rdata_model
        assert req_body['ttl'] == 120
        assert req_body['service'] == '_sip'
        assert req_body['protocol'] == 'udp'

    def test_create_resource_record_all_params_with_retries(self):
        # Enable retries and run test_create_resource_record_all_params.
        _service.enable_retries()
        self.test_create_resource_record_all_params()

        # Disable retries and run test_create_resource_record_all_params.
        _service.disable_retries()
        self.test_create_resource_record_all_params()

    @responses.activate
    def test_create_resource_record_required_params(self):
        """
        test_create_resource_record_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/resource_records')
        mock_response = '{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": {"anyKey": "anyValue"}, "service": "_sip", "protocol": "udp"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Invoke method
        response = _service.create_resource_record(
            instance_id,
            dnszone_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_resource_record_required_params_with_retries(self):
        # Enable retries and run test_create_resource_record_required_params.
        _service.enable_retries()
        self.test_create_resource_record_required_params()

        # Disable retries and run test_create_resource_record_required_params.
        _service.disable_retries()
        self.test_create_resource_record_required_params()

    @responses.activate
    def test_create_resource_record_value_error(self):
        """
        test_create_resource_record_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/resource_records')
        mock_response = '{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": {"anyKey": "anyValue"}, "service": "_sip", "protocol": "udp"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_resource_record(**req_copy)


    def test_create_resource_record_value_error_with_retries(self):
        # Enable retries and run test_create_resource_record_value_error.
        _service.enable_retries()
        self.test_create_resource_record_value_error()

        # Disable retries and run test_create_resource_record_value_error.
        _service.disable_retries()
        self.test_create_resource_record_value_error()

class TestDeleteResourceRecord():
    """
    Test Class for delete_resource_record
    """

    @responses.activate
    def test_delete_resource_record_all_params(self):
        """
        delete_resource_record()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/resource_records/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        record_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.delete_resource_record(
            instance_id,
            dnszone_id,
            record_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_resource_record_all_params_with_retries(self):
        # Enable retries and run test_delete_resource_record_all_params.
        _service.enable_retries()
        self.test_delete_resource_record_all_params()

        # Disable retries and run test_delete_resource_record_all_params.
        _service.disable_retries()
        self.test_delete_resource_record_all_params()

    @responses.activate
    def test_delete_resource_record_required_params(self):
        """
        test_delete_resource_record_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/resource_records/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        record_id = 'testString'

        # Invoke method
        response = _service.delete_resource_record(
            instance_id,
            dnszone_id,
            record_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_resource_record_required_params_with_retries(self):
        # Enable retries and run test_delete_resource_record_required_params.
        _service.enable_retries()
        self.test_delete_resource_record_required_params()

        # Disable retries and run test_delete_resource_record_required_params.
        _service.disable_retries()
        self.test_delete_resource_record_required_params()

    @responses.activate
    def test_delete_resource_record_value_error(self):
        """
        test_delete_resource_record_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/resource_records/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        record_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
            "record_id": record_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_resource_record(**req_copy)


    def test_delete_resource_record_value_error_with_retries(self):
        # Enable retries and run test_delete_resource_record_value_error.
        _service.enable_retries()
        self.test_delete_resource_record_value_error()

        # Disable retries and run test_delete_resource_record_value_error.
        _service.disable_retries()
        self.test_delete_resource_record_value_error()

class TestGetResourceRecord():
    """
    Test Class for get_resource_record
    """

    @responses.activate
    def test_get_resource_record_all_params(self):
        """
        get_resource_record()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/resource_records/testString')
        mock_response = '{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": {"anyKey": "anyValue"}, "service": "_sip", "protocol": "udp"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        record_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.get_resource_record(
            instance_id,
            dnszone_id,
            record_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_resource_record_all_params_with_retries(self):
        # Enable retries and run test_get_resource_record_all_params.
        _service.enable_retries()
        self.test_get_resource_record_all_params()

        # Disable retries and run test_get_resource_record_all_params.
        _service.disable_retries()
        self.test_get_resource_record_all_params()

    @responses.activate
    def test_get_resource_record_required_params(self):
        """
        test_get_resource_record_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/resource_records/testString')
        mock_response = '{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": {"anyKey": "anyValue"}, "service": "_sip", "protocol": "udp"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        record_id = 'testString'

        # Invoke method
        response = _service.get_resource_record(
            instance_id,
            dnszone_id,
            record_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_resource_record_required_params_with_retries(self):
        # Enable retries and run test_get_resource_record_required_params.
        _service.enable_retries()
        self.test_get_resource_record_required_params()

        # Disable retries and run test_get_resource_record_required_params.
        _service.disable_retries()
        self.test_get_resource_record_required_params()

    @responses.activate
    def test_get_resource_record_value_error(self):
        """
        test_get_resource_record_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/resource_records/testString')
        mock_response = '{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": {"anyKey": "anyValue"}, "service": "_sip", "protocol": "udp"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        record_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
            "record_id": record_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_resource_record(**req_copy)


    def test_get_resource_record_value_error_with_retries(self):
        # Enable retries and run test_get_resource_record_value_error.
        _service.enable_retries()
        self.test_get_resource_record_value_error()

        # Disable retries and run test_get_resource_record_value_error.
        _service.disable_retries()
        self.test_get_resource_record_value_error()

class TestUpdateResourceRecord():
    """
    Test Class for update_resource_record
    """

    @responses.activate
    def test_update_resource_record_all_params(self):
        """
        update_resource_record()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/resource_records/testString')
        mock_response = '{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": {"anyKey": "anyValue"}, "service": "_sip", "protocol": "udp"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ResourceRecordUpdateInputRdataRdataARecord model
        resource_record_update_input_rdata_model = {}
        resource_record_update_input_rdata_model['ip'] = '10.110.201.214'

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        record_id = 'testString'
        name = 'test.example.com'
        rdata = resource_record_update_input_rdata_model
        ttl = 120
        service = '_sip'
        protocol = 'udp'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.update_resource_record(
            instance_id,
            dnszone_id,
            record_id,
            name=name,
            rdata=rdata,
            ttl=ttl,
            service=service,
            protocol=protocol,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'test.example.com'
        assert req_body['rdata'] == resource_record_update_input_rdata_model
        assert req_body['ttl'] == 120
        assert req_body['service'] == '_sip'
        assert req_body['protocol'] == 'udp'

    def test_update_resource_record_all_params_with_retries(self):
        # Enable retries and run test_update_resource_record_all_params.
        _service.enable_retries()
        self.test_update_resource_record_all_params()

        # Disable retries and run test_update_resource_record_all_params.
        _service.disable_retries()
        self.test_update_resource_record_all_params()

    @responses.activate
    def test_update_resource_record_required_params(self):
        """
        test_update_resource_record_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/resource_records/testString')
        mock_response = '{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": {"anyKey": "anyValue"}, "service": "_sip", "protocol": "udp"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        record_id = 'testString'

        # Invoke method
        response = _service.update_resource_record(
            instance_id,
            dnszone_id,
            record_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_resource_record_required_params_with_retries(self):
        # Enable retries and run test_update_resource_record_required_params.
        _service.enable_retries()
        self.test_update_resource_record_required_params()

        # Disable retries and run test_update_resource_record_required_params.
        _service.disable_retries()
        self.test_update_resource_record_required_params()

    @responses.activate
    def test_update_resource_record_value_error(self):
        """
        test_update_resource_record_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/resource_records/testString')
        mock_response = '{"id": "SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "name": "_sip._udp.test.example.com", "type": "SRV", "ttl": 120, "rdata": {"anyKey": "anyValue"}, "service": "_sip", "protocol": "udp"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        record_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
            "record_id": record_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_resource_record(**req_copy)


    def test_update_resource_record_value_error_with_retries(self):
        # Enable retries and run test_update_resource_record_value_error.
        _service.enable_retries()
        self.test_update_resource_record_value_error()

        # Disable retries and run test_update_resource_record_value_error.
        _service.disable_retries()
        self.test_update_resource_record_value_error()

class TestExportResourceRecords():
    """
    Test Class for export_resource_records
    """

    @responses.activate
    def test_export_resource_records_all_params(self):
        """
        export_resource_records()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/export_resource_records')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='text/plain; charset=utf-8',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.export_resource_records(
            instance_id,
            dnszone_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_export_resource_records_all_params_with_retries(self):
        # Enable retries and run test_export_resource_records_all_params.
        _service.enable_retries()
        self.test_export_resource_records_all_params()

        # Disable retries and run test_export_resource_records_all_params.
        _service.disable_retries()
        self.test_export_resource_records_all_params()

    @responses.activate
    def test_export_resource_records_required_params(self):
        """
        test_export_resource_records_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/export_resource_records')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='text/plain; charset=utf-8',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Invoke method
        response = _service.export_resource_records(
            instance_id,
            dnszone_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_export_resource_records_required_params_with_retries(self):
        # Enable retries and run test_export_resource_records_required_params.
        _service.enable_retries()
        self.test_export_resource_records_required_params()

        # Disable retries and run test_export_resource_records_required_params.
        _service.disable_retries()
        self.test_export_resource_records_required_params()

    @responses.activate
    def test_export_resource_records_value_error(self):
        """
        test_export_resource_records_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/export_resource_records')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='text/plain; charset=utf-8',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.export_resource_records(**req_copy)


    def test_export_resource_records_value_error_with_retries(self):
        # Enable retries and run test_export_resource_records_value_error.
        _service.enable_retries()
        self.test_export_resource_records_value_error()

        # Disable retries and run test_export_resource_records_value_error.
        _service.disable_retries()
        self.test_export_resource_records_value_error()

class TestImportResourceRecords():
    """
    Test Class for import_resource_records
    """

    @responses.activate
    def test_import_resource_records_all_params(self):
        """
        import_resource_records()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/import_resource_records')
        mock_response = '{"total_records_parsed": 10, "records_added": 2, "records_failed": 0, "records_added_by_type": {"A": 10, "AAAA": 10, "CNAME": 10, "SRV": 10, "TXT": 10, "MX": 10, "PTR": 10}, "records_failed_by_type": {"A": 10, "AAAA": 10, "CNAME": 10, "SRV": 10, "TXT": 10, "MX": 10, "PTR": 10}, "messages": [{"code": "conflict", "message": "A type record conflict with other records"}], "errors": [{"resource_record": "test.example.com A 1.1.1.1", "error": {"code": "internal_server_error", "message": "An internal error occurred. Try again later."}}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        file = io.BytesIO(b'This is a mock file.').getvalue()
        file_content_type = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.import_resource_records(
            instance_id,
            dnszone_id,
            file=file,
            file_content_type=file_content_type,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_import_resource_records_all_params_with_retries(self):
        # Enable retries and run test_import_resource_records_all_params.
        _service.enable_retries()
        self.test_import_resource_records_all_params()

        # Disable retries and run test_import_resource_records_all_params.
        _service.disable_retries()
        self.test_import_resource_records_all_params()

    @responses.activate
    def test_import_resource_records_required_params(self):
        """
        test_import_resource_records_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/import_resource_records')
        mock_response = '{"total_records_parsed": 10, "records_added": 2, "records_failed": 0, "records_added_by_type": {"A": 10, "AAAA": 10, "CNAME": 10, "SRV": 10, "TXT": 10, "MX": 10, "PTR": 10}, "records_failed_by_type": {"A": 10, "AAAA": 10, "CNAME": 10, "SRV": 10, "TXT": 10, "MX": 10, "PTR": 10}, "messages": [{"code": "conflict", "message": "A type record conflict with other records"}], "errors": [{"resource_record": "test.example.com A 1.1.1.1", "error": {"code": "internal_server_error", "message": "An internal error occurred. Try again later."}}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Invoke method
        response = _service.import_resource_records(
            instance_id,
            dnszone_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_import_resource_records_required_params_with_retries(self):
        # Enable retries and run test_import_resource_records_required_params.
        _service.enable_retries()
        self.test_import_resource_records_required_params()

        # Disable retries and run test_import_resource_records_required_params.
        _service.disable_retries()
        self.test_import_resource_records_required_params()

    @responses.activate
    def test_import_resource_records_value_error(self):
        """
        test_import_resource_records_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/import_resource_records')
        mock_response = '{"total_records_parsed": 10, "records_added": 2, "records_failed": 0, "records_added_by_type": {"A": 10, "AAAA": 10, "CNAME": 10, "SRV": 10, "TXT": 10, "MX": 10, "PTR": 10}, "records_failed_by_type": {"A": 10, "AAAA": 10, "CNAME": 10, "SRV": 10, "TXT": 10, "MX": 10, "PTR": 10}, "messages": [{"code": "conflict", "message": "A type record conflict with other records"}], "errors": [{"resource_record": "test.example.com A 1.1.1.1", "error": {"code": "internal_server_error", "message": "An internal error occurred. Try again later."}}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.import_resource_records(**req_copy)


    def test_import_resource_records_value_error_with_retries(self):
        # Enable retries and run test_import_resource_records_value_error.
        _service.enable_retries()
        self.test_import_resource_records_value_error()

        # Disable retries and run test_import_resource_records_value_error.
        _service.disable_retries()
        self.test_import_resource_records_value_error()

# endregion
##############################################################################
# End of Service: ResourceRecords
##############################################################################

##############################################################################
# Start of Service: PermittedNetwork
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = DnsSvcsV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DnsSvcsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DnsSvcsV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestListPermittedNetworks():
    """
    Test Class for list_permitted_networks
    """

    @responses.activate
    def test_list_permitted_networks_all_params(self):
        """
        list_permitted_networks()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/permitted_networks')
        mock_response = '{"permitted_networks": [{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.list_permitted_networks(
            instance_id,
            dnszone_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_permitted_networks_all_params_with_retries(self):
        # Enable retries and run test_list_permitted_networks_all_params.
        _service.enable_retries()
        self.test_list_permitted_networks_all_params()

        # Disable retries and run test_list_permitted_networks_all_params.
        _service.disable_retries()
        self.test_list_permitted_networks_all_params()

    @responses.activate
    def test_list_permitted_networks_required_params(self):
        """
        test_list_permitted_networks_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/permitted_networks')
        mock_response = '{"permitted_networks": [{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Invoke method
        response = _service.list_permitted_networks(
            instance_id,
            dnszone_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_permitted_networks_required_params_with_retries(self):
        # Enable retries and run test_list_permitted_networks_required_params.
        _service.enable_retries()
        self.test_list_permitted_networks_required_params()

        # Disable retries and run test_list_permitted_networks_required_params.
        _service.disable_retries()
        self.test_list_permitted_networks_required_params()

    @responses.activate
    def test_list_permitted_networks_value_error(self):
        """
        test_list_permitted_networks_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/permitted_networks')
        mock_response = '{"permitted_networks": [{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_permitted_networks(**req_copy)


    def test_list_permitted_networks_value_error_with_retries(self):
        # Enable retries and run test_list_permitted_networks_value_error.
        _service.enable_retries()
        self.test_list_permitted_networks_value_error()

        # Disable retries and run test_list_permitted_networks_value_error.
        _service.disable_retries()
        self.test_list_permitted_networks_value_error()

class TestCreatePermittedNetwork():
    """
    Test Class for create_permitted_network
    """

    @responses.activate
    def test_create_permitted_network_all_params(self):
        """
        create_permitted_network()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/permitted_networks')
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a PermittedNetworkVpc model
        permitted_network_vpc_model = {}
        permitted_network_vpc_model['vpc_crn'] = 'crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6'

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        type = 'vpc'
        permitted_network = permitted_network_vpc_model
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.create_permitted_network(
            instance_id,
            dnszone_id,
            type=type,
            permitted_network=permitted_network,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'vpc'
        assert req_body['permitted_network'] == permitted_network_vpc_model

    def test_create_permitted_network_all_params_with_retries(self):
        # Enable retries and run test_create_permitted_network_all_params.
        _service.enable_retries()
        self.test_create_permitted_network_all_params()

        # Disable retries and run test_create_permitted_network_all_params.
        _service.disable_retries()
        self.test_create_permitted_network_all_params()

    @responses.activate
    def test_create_permitted_network_required_params(self):
        """
        test_create_permitted_network_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/permitted_networks')
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Invoke method
        response = _service.create_permitted_network(
            instance_id,
            dnszone_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_permitted_network_required_params_with_retries(self):
        # Enable retries and run test_create_permitted_network_required_params.
        _service.enable_retries()
        self.test_create_permitted_network_required_params()

        # Disable retries and run test_create_permitted_network_required_params.
        _service.disable_retries()
        self.test_create_permitted_network_required_params()

    @responses.activate
    def test_create_permitted_network_value_error(self):
        """
        test_create_permitted_network_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/permitted_networks')
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_permitted_network(**req_copy)


    def test_create_permitted_network_value_error_with_retries(self):
        # Enable retries and run test_create_permitted_network_value_error.
        _service.enable_retries()
        self.test_create_permitted_network_value_error()

        # Disable retries and run test_create_permitted_network_value_error.
        _service.disable_retries()
        self.test_create_permitted_network_value_error()

class TestDeletePermittedNetwork():
    """
    Test Class for delete_permitted_network
    """

    @responses.activate
    def test_delete_permitted_network_all_params(self):
        """
        delete_permitted_network()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/permitted_networks/testString')
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        permitted_network_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.delete_permitted_network(
            instance_id,
            dnszone_id,
            permitted_network_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_permitted_network_all_params_with_retries(self):
        # Enable retries and run test_delete_permitted_network_all_params.
        _service.enable_retries()
        self.test_delete_permitted_network_all_params()

        # Disable retries and run test_delete_permitted_network_all_params.
        _service.disable_retries()
        self.test_delete_permitted_network_all_params()

    @responses.activate
    def test_delete_permitted_network_required_params(self):
        """
        test_delete_permitted_network_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/permitted_networks/testString')
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        permitted_network_id = 'testString'

        # Invoke method
        response = _service.delete_permitted_network(
            instance_id,
            dnszone_id,
            permitted_network_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_permitted_network_required_params_with_retries(self):
        # Enable retries and run test_delete_permitted_network_required_params.
        _service.enable_retries()
        self.test_delete_permitted_network_required_params()

        # Disable retries and run test_delete_permitted_network_required_params.
        _service.disable_retries()
        self.test_delete_permitted_network_required_params()

    @responses.activate
    def test_delete_permitted_network_value_error(self):
        """
        test_delete_permitted_network_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/permitted_networks/testString')
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        permitted_network_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
            "permitted_network_id": permitted_network_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_permitted_network(**req_copy)


    def test_delete_permitted_network_value_error_with_retries(self):
        # Enable retries and run test_delete_permitted_network_value_error.
        _service.enable_retries()
        self.test_delete_permitted_network_value_error()

        # Disable retries and run test_delete_permitted_network_value_error.
        _service.disable_retries()
        self.test_delete_permitted_network_value_error()

class TestGetPermittedNetwork():
    """
    Test Class for get_permitted_network
    """

    @responses.activate
    def test_get_permitted_network_all_params(self):
        """
        get_permitted_network()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/permitted_networks/testString')
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        permitted_network_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.get_permitted_network(
            instance_id,
            dnszone_id,
            permitted_network_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_permitted_network_all_params_with_retries(self):
        # Enable retries and run test_get_permitted_network_all_params.
        _service.enable_retries()
        self.test_get_permitted_network_all_params()

        # Disable retries and run test_get_permitted_network_all_params.
        _service.disable_retries()
        self.test_get_permitted_network_all_params()

    @responses.activate
    def test_get_permitted_network_required_params(self):
        """
        test_get_permitted_network_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/permitted_networks/testString')
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        permitted_network_id = 'testString'

        # Invoke method
        response = _service.get_permitted_network(
            instance_id,
            dnszone_id,
            permitted_network_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_permitted_network_required_params_with_retries(self):
        # Enable retries and run test_get_permitted_network_required_params.
        _service.enable_retries()
        self.test_get_permitted_network_required_params()

        # Disable retries and run test_get_permitted_network_required_params.
        _service.disable_retries()
        self.test_get_permitted_network_required_params()

    @responses.activate
    def test_get_permitted_network_value_error(self):
        """
        test_get_permitted_network_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/permitted_networks/testString')
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        permitted_network_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
            "permitted_network_id": permitted_network_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_permitted_network(**req_copy)


    def test_get_permitted_network_value_error_with_retries(self):
        # Enable retries and run test_get_permitted_network_value_error.
        _service.enable_retries()
        self.test_get_permitted_network_value_error()

        # Disable retries and run test_get_permitted_network_value_error.
        _service.disable_retries()
        self.test_get_permitted_network_value_error()

# endregion
##############################################################################
# End of Service: PermittedNetwork
##############################################################################

##############################################################################
# Start of Service: GlobalLoadBalancers
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = DnsSvcsV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DnsSvcsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DnsSvcsV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestListLoadBalancers():
    """
    Test Class for list_load_balancers
    """

    @responses.activate
    def test_list_load_balancers_all_params(self):
        """
        list_load_balancers()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/load_balancers')
        mock_response = '{"load_balancers": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "description": "Load balancer for glb.example.com.", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": [{"availability_zone": "us-south-1", "pools": ["0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d"]}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}], "offset": 0, "limit": 200, "count": 1, "total_count": 1, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "last": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "previous": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        x_correlation_id = 'testString'
        offset = 38
        limit = 200

        # Invoke method
        response = _service.list_load_balancers(
            instance_id,
            dnszone_id,
            x_correlation_id=x_correlation_id,
            offset=offset,
            limit=limit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'offset={}'.format(offset) in query_string
        assert 'limit={}'.format(limit) in query_string

    def test_list_load_balancers_all_params_with_retries(self):
        # Enable retries and run test_list_load_balancers_all_params.
        _service.enable_retries()
        self.test_list_load_balancers_all_params()

        # Disable retries and run test_list_load_balancers_all_params.
        _service.disable_retries()
        self.test_list_load_balancers_all_params()

    @responses.activate
    def test_list_load_balancers_required_params(self):
        """
        test_list_load_balancers_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/load_balancers')
        mock_response = '{"load_balancers": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "description": "Load balancer for glb.example.com.", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": [{"availability_zone": "us-south-1", "pools": ["0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d"]}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}], "offset": 0, "limit": 200, "count": 1, "total_count": 1, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "last": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "previous": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Invoke method
        response = _service.list_load_balancers(
            instance_id,
            dnszone_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_load_balancers_required_params_with_retries(self):
        # Enable retries and run test_list_load_balancers_required_params.
        _service.enable_retries()
        self.test_list_load_balancers_required_params()

        # Disable retries and run test_list_load_balancers_required_params.
        _service.disable_retries()
        self.test_list_load_balancers_required_params()

    @responses.activate
    def test_list_load_balancers_value_error(self):
        """
        test_list_load_balancers_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/load_balancers')
        mock_response = '{"load_balancers": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "description": "Load balancer for glb.example.com.", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": [{"availability_zone": "us-south-1", "pools": ["0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d"]}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}], "offset": 0, "limit": 200, "count": 1, "total_count": 1, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "last": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "previous": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_load_balancers(**req_copy)


    def test_list_load_balancers_value_error_with_retries(self):
        # Enable retries and run test_list_load_balancers_value_error.
        _service.enable_retries()
        self.test_list_load_balancers_value_error()

        # Disable retries and run test_list_load_balancers_value_error.
        _service.disable_retries()
        self.test_list_load_balancers_value_error()

class TestCreateLoadBalancer():
    """
    Test Class for create_load_balancer
    """

    @responses.activate
    def test_create_load_balancer_all_params(self):
        """
        create_load_balancer()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/load_balancers')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "description": "Load balancer for glb.example.com.", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": [{"availability_zone": "us-south-1", "pools": ["0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d"]}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a LoadBalancerAzPoolsItem model
        load_balancer_az_pools_item_model = {}
        load_balancer_az_pools_item_model['availability_zone'] = 'us-south-1'
        load_balancer_az_pools_item_model['pools'] = ['0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d']

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        name = 'glb.example.com'
        fallback_pool = '24ccf79a-4ae0-4769-b4c8-17f8f230072e'
        default_pools = ['24ccf79a-4ae0-4769-b4c8-17f8f230072e', '13fa7d9e-aeff-4e14-8300-58021db9ee74']
        description = 'Load balancer for glb.example.com.'
        enabled = True
        ttl = 120
        az_pools = [load_balancer_az_pools_item_model]
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.create_load_balancer(
            instance_id,
            dnszone_id,
            name=name,
            fallback_pool=fallback_pool,
            default_pools=default_pools,
            description=description,
            enabled=enabled,
            ttl=ttl,
            az_pools=az_pools,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'glb.example.com'
        assert req_body['fallback_pool'] == '24ccf79a-4ae0-4769-b4c8-17f8f230072e'
        assert req_body['default_pools'] == ['24ccf79a-4ae0-4769-b4c8-17f8f230072e', '13fa7d9e-aeff-4e14-8300-58021db9ee74']
        assert req_body['description'] == 'Load balancer for glb.example.com.'
        assert req_body['enabled'] == True
        assert req_body['ttl'] == 120
        assert req_body['az_pools'] == [load_balancer_az_pools_item_model]

    def test_create_load_balancer_all_params_with_retries(self):
        # Enable retries and run test_create_load_balancer_all_params.
        _service.enable_retries()
        self.test_create_load_balancer_all_params()

        # Disable retries and run test_create_load_balancer_all_params.
        _service.disable_retries()
        self.test_create_load_balancer_all_params()

    @responses.activate
    def test_create_load_balancer_required_params(self):
        """
        test_create_load_balancer_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/load_balancers')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "description": "Load balancer for glb.example.com.", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": [{"availability_zone": "us-south-1", "pools": ["0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d"]}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Invoke method
        response = _service.create_load_balancer(
            instance_id,
            dnszone_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_load_balancer_required_params_with_retries(self):
        # Enable retries and run test_create_load_balancer_required_params.
        _service.enable_retries()
        self.test_create_load_balancer_required_params()

        # Disable retries and run test_create_load_balancer_required_params.
        _service.disable_retries()
        self.test_create_load_balancer_required_params()

    @responses.activate
    def test_create_load_balancer_value_error(self):
        """
        test_create_load_balancer_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/load_balancers')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "description": "Load balancer for glb.example.com.", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": [{"availability_zone": "us-south-1", "pools": ["0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d"]}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_load_balancer(**req_copy)


    def test_create_load_balancer_value_error_with_retries(self):
        # Enable retries and run test_create_load_balancer_value_error.
        _service.enable_retries()
        self.test_create_load_balancer_value_error()

        # Disable retries and run test_create_load_balancer_value_error.
        _service.disable_retries()
        self.test_create_load_balancer_value_error()

class TestDeleteLoadBalancer():
    """
    Test Class for delete_load_balancer
    """

    @responses.activate
    def test_delete_load_balancer_all_params(self):
        """
        delete_load_balancer()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/load_balancers/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        lb_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.delete_load_balancer(
            instance_id,
            dnszone_id,
            lb_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_load_balancer_all_params_with_retries(self):
        # Enable retries and run test_delete_load_balancer_all_params.
        _service.enable_retries()
        self.test_delete_load_balancer_all_params()

        # Disable retries and run test_delete_load_balancer_all_params.
        _service.disable_retries()
        self.test_delete_load_balancer_all_params()

    @responses.activate
    def test_delete_load_balancer_required_params(self):
        """
        test_delete_load_balancer_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/load_balancers/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        lb_id = 'testString'

        # Invoke method
        response = _service.delete_load_balancer(
            instance_id,
            dnszone_id,
            lb_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_load_balancer_required_params_with_retries(self):
        # Enable retries and run test_delete_load_balancer_required_params.
        _service.enable_retries()
        self.test_delete_load_balancer_required_params()

        # Disable retries and run test_delete_load_balancer_required_params.
        _service.disable_retries()
        self.test_delete_load_balancer_required_params()

    @responses.activate
    def test_delete_load_balancer_value_error(self):
        """
        test_delete_load_balancer_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/load_balancers/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        lb_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
            "lb_id": lb_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_load_balancer(**req_copy)


    def test_delete_load_balancer_value_error_with_retries(self):
        # Enable retries and run test_delete_load_balancer_value_error.
        _service.enable_retries()
        self.test_delete_load_balancer_value_error()

        # Disable retries and run test_delete_load_balancer_value_error.
        _service.disable_retries()
        self.test_delete_load_balancer_value_error()

class TestGetLoadBalancer():
    """
    Test Class for get_load_balancer
    """

    @responses.activate
    def test_get_load_balancer_all_params(self):
        """
        get_load_balancer()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/load_balancers/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "description": "Load balancer for glb.example.com.", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": [{"availability_zone": "us-south-1", "pools": ["0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d"]}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        lb_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.get_load_balancer(
            instance_id,
            dnszone_id,
            lb_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_load_balancer_all_params_with_retries(self):
        # Enable retries and run test_get_load_balancer_all_params.
        _service.enable_retries()
        self.test_get_load_balancer_all_params()

        # Disable retries and run test_get_load_balancer_all_params.
        _service.disable_retries()
        self.test_get_load_balancer_all_params()

    @responses.activate
    def test_get_load_balancer_required_params(self):
        """
        test_get_load_balancer_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/load_balancers/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "description": "Load balancer for glb.example.com.", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": [{"availability_zone": "us-south-1", "pools": ["0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d"]}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        lb_id = 'testString'

        # Invoke method
        response = _service.get_load_balancer(
            instance_id,
            dnszone_id,
            lb_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_load_balancer_required_params_with_retries(self):
        # Enable retries and run test_get_load_balancer_required_params.
        _service.enable_retries()
        self.test_get_load_balancer_required_params()

        # Disable retries and run test_get_load_balancer_required_params.
        _service.disable_retries()
        self.test_get_load_balancer_required_params()

    @responses.activate
    def test_get_load_balancer_value_error(self):
        """
        test_get_load_balancer_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/load_balancers/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "description": "Load balancer for glb.example.com.", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": [{"availability_zone": "us-south-1", "pools": ["0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d"]}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        lb_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
            "lb_id": lb_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_load_balancer(**req_copy)


    def test_get_load_balancer_value_error_with_retries(self):
        # Enable retries and run test_get_load_balancer_value_error.
        _service.enable_retries()
        self.test_get_load_balancer_value_error()

        # Disable retries and run test_get_load_balancer_value_error.
        _service.disable_retries()
        self.test_get_load_balancer_value_error()

class TestUpdateLoadBalancer():
    """
    Test Class for update_load_balancer
    """

    @responses.activate
    def test_update_load_balancer_all_params(self):
        """
        update_load_balancer()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/load_balancers/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "description": "Load balancer for glb.example.com.", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": [{"availability_zone": "us-south-1", "pools": ["0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d"]}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a LoadBalancerAzPoolsItem model
        load_balancer_az_pools_item_model = {}
        load_balancer_az_pools_item_model['availability_zone'] = 'us-south-1'
        load_balancer_az_pools_item_model['pools'] = ['0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d']

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        lb_id = 'testString'
        name = 'glb.example.com'
        description = 'Load balancer for glb.example.com.'
        enabled = True
        ttl = 120
        fallback_pool = '24ccf79a-4ae0-4769-b4c8-17f8f230072e'
        default_pools = ['24ccf79a-4ae0-4769-b4c8-17f8f230072e', '13fa7d9e-aeff-4e14-8300-58021db9ee74']
        az_pools = [load_balancer_az_pools_item_model]
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.update_load_balancer(
            instance_id,
            dnszone_id,
            lb_id,
            name=name,
            description=description,
            enabled=enabled,
            ttl=ttl,
            fallback_pool=fallback_pool,
            default_pools=default_pools,
            az_pools=az_pools,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'glb.example.com'
        assert req_body['description'] == 'Load balancer for glb.example.com.'
        assert req_body['enabled'] == True
        assert req_body['ttl'] == 120
        assert req_body['fallback_pool'] == '24ccf79a-4ae0-4769-b4c8-17f8f230072e'
        assert req_body['default_pools'] == ['24ccf79a-4ae0-4769-b4c8-17f8f230072e', '13fa7d9e-aeff-4e14-8300-58021db9ee74']
        assert req_body['az_pools'] == [load_balancer_az_pools_item_model]

    def test_update_load_balancer_all_params_with_retries(self):
        # Enable retries and run test_update_load_balancer_all_params.
        _service.enable_retries()
        self.test_update_load_balancer_all_params()

        # Disable retries and run test_update_load_balancer_all_params.
        _service.disable_retries()
        self.test_update_load_balancer_all_params()

    @responses.activate
    def test_update_load_balancer_required_params(self):
        """
        test_update_load_balancer_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/load_balancers/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "description": "Load balancer for glb.example.com.", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": [{"availability_zone": "us-south-1", "pools": ["0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d"]}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        lb_id = 'testString'

        # Invoke method
        response = _service.update_load_balancer(
            instance_id,
            dnszone_id,
            lb_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_load_balancer_required_params_with_retries(self):
        # Enable retries and run test_update_load_balancer_required_params.
        _service.enable_retries()
        self.test_update_load_balancer_required_params()

        # Disable retries and run test_update_load_balancer_required_params.
        _service.disable_retries()
        self.test_update_load_balancer_required_params()

    @responses.activate
    def test_update_load_balancer_value_error(self):
        """
        test_update_load_balancer_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/load_balancers/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "glb.example.com", "description": "Load balancer for glb.example.com.", "enabled": true, "ttl": 120, "health": "DEGRADED", "fallback_pool": "24ccf79a-4ae0-4769-b4c8-17f8f230072e", "default_pools": ["default_pools"], "az_pools": [{"availability_zone": "us-south-1", "pools": ["0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d"]}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        lb_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
            "lb_id": lb_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_load_balancer(**req_copy)


    def test_update_load_balancer_value_error_with_retries(self):
        # Enable retries and run test_update_load_balancer_value_error.
        _service.enable_retries()
        self.test_update_load_balancer_value_error()

        # Disable retries and run test_update_load_balancer_value_error.
        _service.disable_retries()
        self.test_update_load_balancer_value_error()

# endregion
##############################################################################
# End of Service: GlobalLoadBalancers
##############################################################################

##############################################################################
# Start of Service: Pools
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = DnsSvcsV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DnsSvcsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DnsSvcsV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestListPools():
    """
    Test Class for list_pools
    """

    @responses.activate
    def test_list_pools_all_params(self):
        """
        list_pools()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/pools')
        mock_response = '{"pools": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "health": true, "health_failure_reason": "health_failure_reason"}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_channel": "https://mywebsite.com/dns/webhook", "health": "HEALTHY", "healthcheck_region": "us-south", "healthcheck_subnets": ["crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04"], "healthcheck_vsis": [{"subnet": "crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "ipv4_address": "10.10.16.8", "ipv4_cidr_block": "10.10.16.0/24", "vpc": "crn:v1:staging:public:is:us-south:a/01652b251c3ae2787110a995d8db0135::vpc:r134-8c426a0a-ec74-4c97-9c02-f6194c224d8a"}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}], "offset": 0, "limit": 200, "count": 1, "total_count": 1, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "last": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "previous": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        x_correlation_id = 'testString'
        offset = 38
        limit = 200

        # Invoke method
        response = _service.list_pools(
            instance_id,
            x_correlation_id=x_correlation_id,
            offset=offset,
            limit=limit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'offset={}'.format(offset) in query_string
        assert 'limit={}'.format(limit) in query_string

    def test_list_pools_all_params_with_retries(self):
        # Enable retries and run test_list_pools_all_params.
        _service.enable_retries()
        self.test_list_pools_all_params()

        # Disable retries and run test_list_pools_all_params.
        _service.disable_retries()
        self.test_list_pools_all_params()

    @responses.activate
    def test_list_pools_required_params(self):
        """
        test_list_pools_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/pools')
        mock_response = '{"pools": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "health": true, "health_failure_reason": "health_failure_reason"}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_channel": "https://mywebsite.com/dns/webhook", "health": "HEALTHY", "healthcheck_region": "us-south", "healthcheck_subnets": ["crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04"], "healthcheck_vsis": [{"subnet": "crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "ipv4_address": "10.10.16.8", "ipv4_cidr_block": "10.10.16.0/24", "vpc": "crn:v1:staging:public:is:us-south:a/01652b251c3ae2787110a995d8db0135::vpc:r134-8c426a0a-ec74-4c97-9c02-f6194c224d8a"}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}], "offset": 0, "limit": 200, "count": 1, "total_count": 1, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "last": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "previous": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.list_pools(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_pools_required_params_with_retries(self):
        # Enable retries and run test_list_pools_required_params.
        _service.enable_retries()
        self.test_list_pools_required_params()

        # Disable retries and run test_list_pools_required_params.
        _service.disable_retries()
        self.test_list_pools_required_params()

    @responses.activate
    def test_list_pools_value_error(self):
        """
        test_list_pools_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/pools')
        mock_response = '{"pools": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "health": true, "health_failure_reason": "health_failure_reason"}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_channel": "https://mywebsite.com/dns/webhook", "health": "HEALTHY", "healthcheck_region": "us-south", "healthcheck_subnets": ["crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04"], "healthcheck_vsis": [{"subnet": "crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "ipv4_address": "10.10.16.8", "ipv4_cidr_block": "10.10.16.0/24", "vpc": "crn:v1:staging:public:is:us-south:a/01652b251c3ae2787110a995d8db0135::vpc:r134-8c426a0a-ec74-4c97-9c02-f6194c224d8a"}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}], "offset": 0, "limit": 200, "count": 1, "total_count": 1, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "last": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "previous": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_pools(**req_copy)


    def test_list_pools_value_error_with_retries(self):
        # Enable retries and run test_list_pools_value_error.
        _service.enable_retries()
        self.test_list_pools_value_error()

        # Disable retries and run test_list_pools_value_error.
        _service.disable_retries()
        self.test_list_pools_value_error()

class TestCreatePool():
    """
    Test Class for create_pool
    """

    @responses.activate
    def test_create_pool_all_params(self):
        """
        create_pool()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/pools')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "health": true, "health_failure_reason": "health_failure_reason"}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_channel": "https://mywebsite.com/dns/webhook", "health": "HEALTHY", "healthcheck_region": "us-south", "healthcheck_subnets": ["crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04"], "healthcheck_vsis": [{"subnet": "crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "ipv4_address": "10.10.16.8", "ipv4_cidr_block": "10.10.16.0/24", "vpc": "crn:v1:staging:public:is:us-south:a/01652b251c3ae2787110a995d8db0135::vpc:r134-8c426a0a-ec74-4c97-9c02-f6194c224d8a"}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a OriginInput model
        origin_input_model = {}
        origin_input_model['name'] = 'app-server-1'
        origin_input_model['description'] = 'description of the origin server'
        origin_input_model['address'] = '10.10.16.8'
        origin_input_model['enabled'] = True

        # Set up parameter values
        instance_id = 'testString'
        name = 'dal10-az-pool'
        origins = [origin_input_model]
        description = 'Load balancer pool for dal10 availability zone.'
        enabled = True
        healthy_origins_threshold = 1
        monitor = '7dd6841c-264e-11ea-88df-062967242a6a'
        notification_channel = 'https://mywebsite.com/dns/webhook'
        healthcheck_region = 'us-south'
        healthcheck_subnets = ['crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04']
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.create_pool(
            instance_id,
            name=name,
            origins=origins,
            description=description,
            enabled=enabled,
            healthy_origins_threshold=healthy_origins_threshold,
            monitor=monitor,
            notification_channel=notification_channel,
            healthcheck_region=healthcheck_region,
            healthcheck_subnets=healthcheck_subnets,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'dal10-az-pool'
        assert req_body['origins'] == [origin_input_model]
        assert req_body['description'] == 'Load balancer pool for dal10 availability zone.'
        assert req_body['enabled'] == True
        assert req_body['healthy_origins_threshold'] == 1
        assert req_body['monitor'] == '7dd6841c-264e-11ea-88df-062967242a6a'
        assert req_body['notification_channel'] == 'https://mywebsite.com/dns/webhook'
        assert req_body['healthcheck_region'] == 'us-south'
        assert req_body['healthcheck_subnets'] == ['crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04']

    def test_create_pool_all_params_with_retries(self):
        # Enable retries and run test_create_pool_all_params.
        _service.enable_retries()
        self.test_create_pool_all_params()

        # Disable retries and run test_create_pool_all_params.
        _service.disable_retries()
        self.test_create_pool_all_params()

    @responses.activate
    def test_create_pool_required_params(self):
        """
        test_create_pool_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/pools')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "health": true, "health_failure_reason": "health_failure_reason"}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_channel": "https://mywebsite.com/dns/webhook", "health": "HEALTHY", "healthcheck_region": "us-south", "healthcheck_subnets": ["crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04"], "healthcheck_vsis": [{"subnet": "crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "ipv4_address": "10.10.16.8", "ipv4_cidr_block": "10.10.16.0/24", "vpc": "crn:v1:staging:public:is:us-south:a/01652b251c3ae2787110a995d8db0135::vpc:r134-8c426a0a-ec74-4c97-9c02-f6194c224d8a"}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.create_pool(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_pool_required_params_with_retries(self):
        # Enable retries and run test_create_pool_required_params.
        _service.enable_retries()
        self.test_create_pool_required_params()

        # Disable retries and run test_create_pool_required_params.
        _service.disable_retries()
        self.test_create_pool_required_params()

    @responses.activate
    def test_create_pool_value_error(self):
        """
        test_create_pool_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/pools')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "health": true, "health_failure_reason": "health_failure_reason"}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_channel": "https://mywebsite.com/dns/webhook", "health": "HEALTHY", "healthcheck_region": "us-south", "healthcheck_subnets": ["crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04"], "healthcheck_vsis": [{"subnet": "crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "ipv4_address": "10.10.16.8", "ipv4_cidr_block": "10.10.16.0/24", "vpc": "crn:v1:staging:public:is:us-south:a/01652b251c3ae2787110a995d8db0135::vpc:r134-8c426a0a-ec74-4c97-9c02-f6194c224d8a"}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_pool(**req_copy)


    def test_create_pool_value_error_with_retries(self):
        # Enable retries and run test_create_pool_value_error.
        _service.enable_retries()
        self.test_create_pool_value_error()

        # Disable retries and run test_create_pool_value_error.
        _service.disable_retries()
        self.test_create_pool_value_error()

class TestDeletePool():
    """
    Test Class for delete_pool
    """

    @responses.activate
    def test_delete_pool_all_params(self):
        """
        delete_pool()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/pools/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        pool_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.delete_pool(
            instance_id,
            pool_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_pool_all_params_with_retries(self):
        # Enable retries and run test_delete_pool_all_params.
        _service.enable_retries()
        self.test_delete_pool_all_params()

        # Disable retries and run test_delete_pool_all_params.
        _service.disable_retries()
        self.test_delete_pool_all_params()

    @responses.activate
    def test_delete_pool_required_params(self):
        """
        test_delete_pool_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/pools/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        pool_id = 'testString'

        # Invoke method
        response = _service.delete_pool(
            instance_id,
            pool_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_pool_required_params_with_retries(self):
        # Enable retries and run test_delete_pool_required_params.
        _service.enable_retries()
        self.test_delete_pool_required_params()

        # Disable retries and run test_delete_pool_required_params.
        _service.disable_retries()
        self.test_delete_pool_required_params()

    @responses.activate
    def test_delete_pool_value_error(self):
        """
        test_delete_pool_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/pools/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        pool_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "pool_id": pool_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_pool(**req_copy)


    def test_delete_pool_value_error_with_retries(self):
        # Enable retries and run test_delete_pool_value_error.
        _service.enable_retries()
        self.test_delete_pool_value_error()

        # Disable retries and run test_delete_pool_value_error.
        _service.disable_retries()
        self.test_delete_pool_value_error()

class TestGetPool():
    """
    Test Class for get_pool
    """

    @responses.activate
    def test_get_pool_all_params(self):
        """
        get_pool()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/pools/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "health": true, "health_failure_reason": "health_failure_reason"}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_channel": "https://mywebsite.com/dns/webhook", "health": "HEALTHY", "healthcheck_region": "us-south", "healthcheck_subnets": ["crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04"], "healthcheck_vsis": [{"subnet": "crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "ipv4_address": "10.10.16.8", "ipv4_cidr_block": "10.10.16.0/24", "vpc": "crn:v1:staging:public:is:us-south:a/01652b251c3ae2787110a995d8db0135::vpc:r134-8c426a0a-ec74-4c97-9c02-f6194c224d8a"}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        pool_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.get_pool(
            instance_id,
            pool_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_pool_all_params_with_retries(self):
        # Enable retries and run test_get_pool_all_params.
        _service.enable_retries()
        self.test_get_pool_all_params()

        # Disable retries and run test_get_pool_all_params.
        _service.disable_retries()
        self.test_get_pool_all_params()

    @responses.activate
    def test_get_pool_required_params(self):
        """
        test_get_pool_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/pools/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "health": true, "health_failure_reason": "health_failure_reason"}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_channel": "https://mywebsite.com/dns/webhook", "health": "HEALTHY", "healthcheck_region": "us-south", "healthcheck_subnets": ["crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04"], "healthcheck_vsis": [{"subnet": "crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "ipv4_address": "10.10.16.8", "ipv4_cidr_block": "10.10.16.0/24", "vpc": "crn:v1:staging:public:is:us-south:a/01652b251c3ae2787110a995d8db0135::vpc:r134-8c426a0a-ec74-4c97-9c02-f6194c224d8a"}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        pool_id = 'testString'

        # Invoke method
        response = _service.get_pool(
            instance_id,
            pool_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_pool_required_params_with_retries(self):
        # Enable retries and run test_get_pool_required_params.
        _service.enable_retries()
        self.test_get_pool_required_params()

        # Disable retries and run test_get_pool_required_params.
        _service.disable_retries()
        self.test_get_pool_required_params()

    @responses.activate
    def test_get_pool_value_error(self):
        """
        test_get_pool_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/pools/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "health": true, "health_failure_reason": "health_failure_reason"}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_channel": "https://mywebsite.com/dns/webhook", "health": "HEALTHY", "healthcheck_region": "us-south", "healthcheck_subnets": ["crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04"], "healthcheck_vsis": [{"subnet": "crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "ipv4_address": "10.10.16.8", "ipv4_cidr_block": "10.10.16.0/24", "vpc": "crn:v1:staging:public:is:us-south:a/01652b251c3ae2787110a995d8db0135::vpc:r134-8c426a0a-ec74-4c97-9c02-f6194c224d8a"}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        pool_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "pool_id": pool_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_pool(**req_copy)


    def test_get_pool_value_error_with_retries(self):
        # Enable retries and run test_get_pool_value_error.
        _service.enable_retries()
        self.test_get_pool_value_error()

        # Disable retries and run test_get_pool_value_error.
        _service.disable_retries()
        self.test_get_pool_value_error()

class TestUpdatePool():
    """
    Test Class for update_pool
    """

    @responses.activate
    def test_update_pool_all_params(self):
        """
        update_pool()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/pools/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "health": true, "health_failure_reason": "health_failure_reason"}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_channel": "https://mywebsite.com/dns/webhook", "health": "HEALTHY", "healthcheck_region": "us-south", "healthcheck_subnets": ["crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04"], "healthcheck_vsis": [{"subnet": "crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "ipv4_address": "10.10.16.8", "ipv4_cidr_block": "10.10.16.0/24", "vpc": "crn:v1:staging:public:is:us-south:a/01652b251c3ae2787110a995d8db0135::vpc:r134-8c426a0a-ec74-4c97-9c02-f6194c224d8a"}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a OriginInput model
        origin_input_model = {}
        origin_input_model['name'] = 'app-server-1'
        origin_input_model['description'] = 'description of the origin server'
        origin_input_model['address'] = '10.10.16.8'
        origin_input_model['enabled'] = True

        # Set up parameter values
        instance_id = 'testString'
        pool_id = 'testString'
        name = 'dal10-az-pool'
        description = 'Load balancer pool for dal10 availability zone.'
        enabled = True
        healthy_origins_threshold = 1
        origins = [origin_input_model]
        monitor = '7dd6841c-264e-11ea-88df-062967242a6a'
        notification_channel = 'https://mywebsite.com/dns/webhook'
        healthcheck_region = 'us-south'
        healthcheck_subnets = ['crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04']
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.update_pool(
            instance_id,
            pool_id,
            name=name,
            description=description,
            enabled=enabled,
            healthy_origins_threshold=healthy_origins_threshold,
            origins=origins,
            monitor=monitor,
            notification_channel=notification_channel,
            healthcheck_region=healthcheck_region,
            healthcheck_subnets=healthcheck_subnets,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'dal10-az-pool'
        assert req_body['description'] == 'Load balancer pool for dal10 availability zone.'
        assert req_body['enabled'] == True
        assert req_body['healthy_origins_threshold'] == 1
        assert req_body['origins'] == [origin_input_model]
        assert req_body['monitor'] == '7dd6841c-264e-11ea-88df-062967242a6a'
        assert req_body['notification_channel'] == 'https://mywebsite.com/dns/webhook'
        assert req_body['healthcheck_region'] == 'us-south'
        assert req_body['healthcheck_subnets'] == ['crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04']

    def test_update_pool_all_params_with_retries(self):
        # Enable retries and run test_update_pool_all_params.
        _service.enable_retries()
        self.test_update_pool_all_params()

        # Disable retries and run test_update_pool_all_params.
        _service.disable_retries()
        self.test_update_pool_all_params()

    @responses.activate
    def test_update_pool_required_params(self):
        """
        test_update_pool_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/pools/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "health": true, "health_failure_reason": "health_failure_reason"}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_channel": "https://mywebsite.com/dns/webhook", "health": "HEALTHY", "healthcheck_region": "us-south", "healthcheck_subnets": ["crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04"], "healthcheck_vsis": [{"subnet": "crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "ipv4_address": "10.10.16.8", "ipv4_cidr_block": "10.10.16.0/24", "vpc": "crn:v1:staging:public:is:us-south:a/01652b251c3ae2787110a995d8db0135::vpc:r134-8c426a0a-ec74-4c97-9c02-f6194c224d8a"}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        pool_id = 'testString'

        # Invoke method
        response = _service.update_pool(
            instance_id,
            pool_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_pool_required_params_with_retries(self):
        # Enable retries and run test_update_pool_required_params.
        _service.enable_retries()
        self.test_update_pool_required_params()

        # Disable retries and run test_update_pool_required_params.
        _service.disable_retries()
        self.test_update_pool_required_params()

    @responses.activate
    def test_update_pool_value_error(self):
        """
        test_update_pool_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/pools/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "dal10-az-pool", "description": "Load balancer pool for dal10 availability zone.", "enabled": true, "healthy_origins_threshold": 1, "origins": [{"name": "app-server-1", "description": "description of the origin server", "address": "10.10.16.8", "enabled": true, "health": true, "health_failure_reason": "health_failure_reason"}], "monitor": "7dd6841c-264e-11ea-88df-062967242a6a", "notification_channel": "https://mywebsite.com/dns/webhook", "health": "HEALTHY", "healthcheck_region": "us-south", "healthcheck_subnets": ["crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04"], "healthcheck_vsis": [{"subnet": "crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "ipv4_address": "10.10.16.8", "ipv4_cidr_block": "10.10.16.0/24", "vpc": "crn:v1:staging:public:is:us-south:a/01652b251c3ae2787110a995d8db0135::vpc:r134-8c426a0a-ec74-4c97-9c02-f6194c224d8a"}], "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        pool_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "pool_id": pool_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_pool(**req_copy)


    def test_update_pool_value_error_with_retries(self):
        # Enable retries and run test_update_pool_value_error.
        _service.enable_retries()
        self.test_update_pool_value_error()

        # Disable retries and run test_update_pool_value_error.
        _service.disable_retries()
        self.test_update_pool_value_error()

# endregion
##############################################################################
# End of Service: Pools
##############################################################################

##############################################################################
# Start of Service: Monitors
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = DnsSvcsV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DnsSvcsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DnsSvcsV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestListMonitors():
    """
    Test Class for list_monitors
    """

    @responses.activate
    def test_list_monitors_all_params(self):
        """
        list_monitors()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/monitors')
        mock_response = '{"monitors": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Load balancer monitor for glb.example.com.", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}], "offset": 0, "limit": 200, "count": 1, "total_count": 1, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "last": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "previous": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        x_correlation_id = 'testString'
        offset = 38
        limit = 200

        # Invoke method
        response = _service.list_monitors(
            instance_id,
            x_correlation_id=x_correlation_id,
            offset=offset,
            limit=limit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'offset={}'.format(offset) in query_string
        assert 'limit={}'.format(limit) in query_string

    def test_list_monitors_all_params_with_retries(self):
        # Enable retries and run test_list_monitors_all_params.
        _service.enable_retries()
        self.test_list_monitors_all_params()

        # Disable retries and run test_list_monitors_all_params.
        _service.disable_retries()
        self.test_list_monitors_all_params()

    @responses.activate
    def test_list_monitors_required_params(self):
        """
        test_list_monitors_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/monitors')
        mock_response = '{"monitors": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Load balancer monitor for glb.example.com.", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}], "offset": 0, "limit": 200, "count": 1, "total_count": 1, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "last": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "previous": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.list_monitors(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_monitors_required_params_with_retries(self):
        # Enable retries and run test_list_monitors_required_params.
        _service.enable_retries()
        self.test_list_monitors_required_params()

        # Disable retries and run test_list_monitors_required_params.
        _service.disable_retries()
        self.test_list_monitors_required_params()

    @responses.activate
    def test_list_monitors_value_error(self):
        """
        test_list_monitors_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/monitors')
        mock_response = '{"monitors": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Load balancer monitor for glb.example.com.", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}], "offset": 0, "limit": 200, "count": 1, "total_count": 1, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "last": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "previous": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_monitors(**req_copy)


    def test_list_monitors_value_error_with_retries(self):
        # Enable retries and run test_list_monitors_value_error.
        _service.enable_retries()
        self.test_list_monitors_value_error()

        # Disable retries and run test_list_monitors_value_error.
        _service.disable_retries()
        self.test_list_monitors_value_error()

class TestCreateMonitor():
    """
    Test Class for create_monitor
    """

    @responses.activate
    def test_create_monitor_all_params(self):
        """
        create_monitor()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/monitors')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Load balancer monitor for glb.example.com.", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a HealthcheckHeader model
        healthcheck_header_model = {}
        healthcheck_header_model['name'] = 'Host'
        healthcheck_header_model['value'] = ['origin.example.com']

        # Set up parameter values
        instance_id = 'testString'
        name = 'healthcheck-monitor'
        type = 'HTTPS'
        description = 'Load balancer monitor for glb.example.com.'
        port = 8080
        interval = 60
        retries = 2
        timeout = 5
        method = 'GET'
        path = '/health'
        headers_ = [healthcheck_header_model]
        allow_insecure = False
        expected_codes = '200'
        expected_body = 'alive'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.create_monitor(
            instance_id,
            name=name,
            type=type,
            description=description,
            port=port,
            interval=interval,
            retries=retries,
            timeout=timeout,
            method=method,
            path=path,
            headers_=headers_,
            allow_insecure=allow_insecure,
            expected_codes=expected_codes,
            expected_body=expected_body,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'healthcheck-monitor'
        assert req_body['type'] == 'HTTPS'
        assert req_body['description'] == 'Load balancer monitor for glb.example.com.'
        assert req_body['port'] == 8080
        assert req_body['interval'] == 60
        assert req_body['retries'] == 2
        assert req_body['timeout'] == 5
        assert req_body['method'] == 'GET'
        assert req_body['path'] == '/health'
        assert req_body['headers'] == [healthcheck_header_model]
        assert req_body['allow_insecure'] == False
        assert req_body['expected_codes'] == '200'
        assert req_body['expected_body'] == 'alive'

    def test_create_monitor_all_params_with_retries(self):
        # Enable retries and run test_create_monitor_all_params.
        _service.enable_retries()
        self.test_create_monitor_all_params()

        # Disable retries and run test_create_monitor_all_params.
        _service.disable_retries()
        self.test_create_monitor_all_params()

    @responses.activate
    def test_create_monitor_required_params(self):
        """
        test_create_monitor_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/monitors')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Load balancer monitor for glb.example.com.", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.create_monitor(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_monitor_required_params_with_retries(self):
        # Enable retries and run test_create_monitor_required_params.
        _service.enable_retries()
        self.test_create_monitor_required_params()

        # Disable retries and run test_create_monitor_required_params.
        _service.disable_retries()
        self.test_create_monitor_required_params()

    @responses.activate
    def test_create_monitor_value_error(self):
        """
        test_create_monitor_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/monitors')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Load balancer monitor for glb.example.com.", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_monitor(**req_copy)


    def test_create_monitor_value_error_with_retries(self):
        # Enable retries and run test_create_monitor_value_error.
        _service.enable_retries()
        self.test_create_monitor_value_error()

        # Disable retries and run test_create_monitor_value_error.
        _service.disable_retries()
        self.test_create_monitor_value_error()

class TestDeleteMonitor():
    """
    Test Class for delete_monitor
    """

    @responses.activate
    def test_delete_monitor_all_params(self):
        """
        delete_monitor()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/monitors/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        monitor_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.delete_monitor(
            instance_id,
            monitor_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_monitor_all_params_with_retries(self):
        # Enable retries and run test_delete_monitor_all_params.
        _service.enable_retries()
        self.test_delete_monitor_all_params()

        # Disable retries and run test_delete_monitor_all_params.
        _service.disable_retries()
        self.test_delete_monitor_all_params()

    @responses.activate
    def test_delete_monitor_required_params(self):
        """
        test_delete_monitor_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/monitors/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        monitor_id = 'testString'

        # Invoke method
        response = _service.delete_monitor(
            instance_id,
            monitor_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_monitor_required_params_with_retries(self):
        # Enable retries and run test_delete_monitor_required_params.
        _service.enable_retries()
        self.test_delete_monitor_required_params()

        # Disable retries and run test_delete_monitor_required_params.
        _service.disable_retries()
        self.test_delete_monitor_required_params()

    @responses.activate
    def test_delete_monitor_value_error(self):
        """
        test_delete_monitor_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/monitors/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        monitor_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "monitor_id": monitor_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_monitor(**req_copy)


    def test_delete_monitor_value_error_with_retries(self):
        # Enable retries and run test_delete_monitor_value_error.
        _service.enable_retries()
        self.test_delete_monitor_value_error()

        # Disable retries and run test_delete_monitor_value_error.
        _service.disable_retries()
        self.test_delete_monitor_value_error()

class TestGetMonitor():
    """
    Test Class for get_monitor
    """

    @responses.activate
    def test_get_monitor_all_params(self):
        """
        get_monitor()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/monitors/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Load balancer monitor for glb.example.com.", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        monitor_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.get_monitor(
            instance_id,
            monitor_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_monitor_all_params_with_retries(self):
        # Enable retries and run test_get_monitor_all_params.
        _service.enable_retries()
        self.test_get_monitor_all_params()

        # Disable retries and run test_get_monitor_all_params.
        _service.disable_retries()
        self.test_get_monitor_all_params()

    @responses.activate
    def test_get_monitor_required_params(self):
        """
        test_get_monitor_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/monitors/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Load balancer monitor for glb.example.com.", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        monitor_id = 'testString'

        # Invoke method
        response = _service.get_monitor(
            instance_id,
            monitor_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_monitor_required_params_with_retries(self):
        # Enable retries and run test_get_monitor_required_params.
        _service.enable_retries()
        self.test_get_monitor_required_params()

        # Disable retries and run test_get_monitor_required_params.
        _service.disable_retries()
        self.test_get_monitor_required_params()

    @responses.activate
    def test_get_monitor_value_error(self):
        """
        test_get_monitor_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/monitors/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Load balancer monitor for glb.example.com.", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        monitor_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "monitor_id": monitor_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_monitor(**req_copy)


    def test_get_monitor_value_error_with_retries(self):
        # Enable retries and run test_get_monitor_value_error.
        _service.enable_retries()
        self.test_get_monitor_value_error()

        # Disable retries and run test_get_monitor_value_error.
        _service.disable_retries()
        self.test_get_monitor_value_error()

class TestUpdateMonitor():
    """
    Test Class for update_monitor
    """

    @responses.activate
    def test_update_monitor_all_params(self):
        """
        update_monitor()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/monitors/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Load balancer monitor for glb.example.com.", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a HealthcheckHeader model
        healthcheck_header_model = {}
        healthcheck_header_model['name'] = 'Host'
        healthcheck_header_model['value'] = ['origin.example.com']

        # Set up parameter values
        instance_id = 'testString'
        monitor_id = 'testString'
        name = 'healthcheck-monitor'
        description = 'Load balancer monitor for glb.example.com.'
        type = 'HTTPS'
        port = 8080
        interval = 60
        retries = 2
        timeout = 5
        method = 'GET'
        path = '/health'
        headers_ = [healthcheck_header_model]
        allow_insecure = False
        expected_codes = '200'
        expected_body = 'alive'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.update_monitor(
            instance_id,
            monitor_id,
            name=name,
            description=description,
            type=type,
            port=port,
            interval=interval,
            retries=retries,
            timeout=timeout,
            method=method,
            path=path,
            headers_=headers_,
            allow_insecure=allow_insecure,
            expected_codes=expected_codes,
            expected_body=expected_body,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'healthcheck-monitor'
        assert req_body['description'] == 'Load balancer monitor for glb.example.com.'
        assert req_body['type'] == 'HTTPS'
        assert req_body['port'] == 8080
        assert req_body['interval'] == 60
        assert req_body['retries'] == 2
        assert req_body['timeout'] == 5
        assert req_body['method'] == 'GET'
        assert req_body['path'] == '/health'
        assert req_body['headers'] == [healthcheck_header_model]
        assert req_body['allow_insecure'] == False
        assert req_body['expected_codes'] == '200'
        assert req_body['expected_body'] == 'alive'

    def test_update_monitor_all_params_with_retries(self):
        # Enable retries and run test_update_monitor_all_params.
        _service.enable_retries()
        self.test_update_monitor_all_params()

        # Disable retries and run test_update_monitor_all_params.
        _service.disable_retries()
        self.test_update_monitor_all_params()

    @responses.activate
    def test_update_monitor_required_params(self):
        """
        test_update_monitor_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/monitors/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Load balancer monitor for glb.example.com.", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        monitor_id = 'testString'

        # Invoke method
        response = _service.update_monitor(
            instance_id,
            monitor_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_monitor_required_params_with_retries(self):
        # Enable retries and run test_update_monitor_required_params.
        _service.enable_retries()
        self.test_update_monitor_required_params()

        # Disable retries and run test_update_monitor_required_params.
        _service.disable_retries()
        self.test_update_monitor_required_params()

    @responses.activate
    def test_update_monitor_value_error(self):
        """
        test_update_monitor_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/monitors/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "healthcheck-monitor", "description": "Load balancer monitor for glb.example.com.", "type": "HTTPS", "port": 8080, "interval": 60, "retries": 2, "timeout": 5, "method": "GET", "path": "/health", "headers": [{"name": "Host", "value": ["origin.example.com"]}], "allow_insecure": false, "expected_codes": "200", "expected_body": "alive", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        monitor_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "monitor_id": monitor_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_monitor(**req_copy)


    def test_update_monitor_value_error_with_retries(self):
        # Enable retries and run test_update_monitor_value_error.
        _service.enable_retries()
        self.test_update_monitor_value_error()

        # Disable retries and run test_update_monitor_value_error.
        _service.disable_retries()
        self.test_update_monitor_value_error()

# endregion
##############################################################################
# End of Service: Monitors
##############################################################################

##############################################################################
# Start of Service: CustomResolvers
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = DnsSvcsV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DnsSvcsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DnsSvcsV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestListCustomResolvers():
    """
    Test Class for list_custom_resolvers
    """

    @responses.activate
    def test_list_custom_resolvers_all_params(self):
        """
        list_custom_resolvers()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers')
        mock_response = '{"custom_resolvers": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "my-resolver", "description": "custom resolver", "enabled": false, "health": "HEALTHY", "locations": [{"id": "9a234ede-c2b6-4c39-bc27-d39ec139ecdb", "subnet_crn": "crn:v1:bluemix:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "enabled": true, "healthy": true, "dns_server_ip": "10.10.16.8"}], "created_on": "2021-04-21T08:18:25.000Z", "modified_on": "2021-04-21T08:18:25.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.list_custom_resolvers(
            instance_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_custom_resolvers_all_params_with_retries(self):
        # Enable retries and run test_list_custom_resolvers_all_params.
        _service.enable_retries()
        self.test_list_custom_resolvers_all_params()

        # Disable retries and run test_list_custom_resolvers_all_params.
        _service.disable_retries()
        self.test_list_custom_resolvers_all_params()

    @responses.activate
    def test_list_custom_resolvers_required_params(self):
        """
        test_list_custom_resolvers_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers')
        mock_response = '{"custom_resolvers": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "my-resolver", "description": "custom resolver", "enabled": false, "health": "HEALTHY", "locations": [{"id": "9a234ede-c2b6-4c39-bc27-d39ec139ecdb", "subnet_crn": "crn:v1:bluemix:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "enabled": true, "healthy": true, "dns_server_ip": "10.10.16.8"}], "created_on": "2021-04-21T08:18:25.000Z", "modified_on": "2021-04-21T08:18:25.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.list_custom_resolvers(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_custom_resolvers_required_params_with_retries(self):
        # Enable retries and run test_list_custom_resolvers_required_params.
        _service.enable_retries()
        self.test_list_custom_resolvers_required_params()

        # Disable retries and run test_list_custom_resolvers_required_params.
        _service.disable_retries()
        self.test_list_custom_resolvers_required_params()

    @responses.activate
    def test_list_custom_resolvers_value_error(self):
        """
        test_list_custom_resolvers_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers')
        mock_response = '{"custom_resolvers": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "my-resolver", "description": "custom resolver", "enabled": false, "health": "HEALTHY", "locations": [{"id": "9a234ede-c2b6-4c39-bc27-d39ec139ecdb", "subnet_crn": "crn:v1:bluemix:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "enabled": true, "healthy": true, "dns_server_ip": "10.10.16.8"}], "created_on": "2021-04-21T08:18:25.000Z", "modified_on": "2021-04-21T08:18:25.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_custom_resolvers(**req_copy)


    def test_list_custom_resolvers_value_error_with_retries(self):
        # Enable retries and run test_list_custom_resolvers_value_error.
        _service.enable_retries()
        self.test_list_custom_resolvers_value_error()

        # Disable retries and run test_list_custom_resolvers_value_error.
        _service.disable_retries()
        self.test_list_custom_resolvers_value_error()

class TestCreateCustomResolver():
    """
    Test Class for create_custom_resolver
    """

    @responses.activate
    def test_create_custom_resolver_all_params(self):
        """
        create_custom_resolver()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "my-resolver", "description": "custom resolver", "enabled": false, "health": "HEALTHY", "locations": [{"id": "9a234ede-c2b6-4c39-bc27-d39ec139ecdb", "subnet_crn": "crn:v1:bluemix:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "enabled": true, "healthy": true, "dns_server_ip": "10.10.16.8"}], "created_on": "2021-04-21T08:18:25.000Z", "modified_on": "2021-04-21T08:18:25.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a LocationInput model
        location_input_model = {}
        location_input_model['subnet_crn'] = 'crn:v1:bluemix:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04'
        location_input_model['enabled'] = False

        # Set up parameter values
        instance_id = 'testString'
        name = 'my-resolver'
        description = 'custom resolver'
        locations = [location_input_model]
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.create_custom_resolver(
            instance_id,
            name=name,
            description=description,
            locations=locations,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'my-resolver'
        assert req_body['description'] == 'custom resolver'
        assert req_body['locations'] == [location_input_model]

    def test_create_custom_resolver_all_params_with_retries(self):
        # Enable retries and run test_create_custom_resolver_all_params.
        _service.enable_retries()
        self.test_create_custom_resolver_all_params()

        # Disable retries and run test_create_custom_resolver_all_params.
        _service.disable_retries()
        self.test_create_custom_resolver_all_params()

    @responses.activate
    def test_create_custom_resolver_required_params(self):
        """
        test_create_custom_resolver_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "my-resolver", "description": "custom resolver", "enabled": false, "health": "HEALTHY", "locations": [{"id": "9a234ede-c2b6-4c39-bc27-d39ec139ecdb", "subnet_crn": "crn:v1:bluemix:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "enabled": true, "healthy": true, "dns_server_ip": "10.10.16.8"}], "created_on": "2021-04-21T08:18:25.000Z", "modified_on": "2021-04-21T08:18:25.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.create_custom_resolver(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_custom_resolver_required_params_with_retries(self):
        # Enable retries and run test_create_custom_resolver_required_params.
        _service.enable_retries()
        self.test_create_custom_resolver_required_params()

        # Disable retries and run test_create_custom_resolver_required_params.
        _service.disable_retries()
        self.test_create_custom_resolver_required_params()

    @responses.activate
    def test_create_custom_resolver_value_error(self):
        """
        test_create_custom_resolver_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "my-resolver", "description": "custom resolver", "enabled": false, "health": "HEALTHY", "locations": [{"id": "9a234ede-c2b6-4c39-bc27-d39ec139ecdb", "subnet_crn": "crn:v1:bluemix:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "enabled": true, "healthy": true, "dns_server_ip": "10.10.16.8"}], "created_on": "2021-04-21T08:18:25.000Z", "modified_on": "2021-04-21T08:18:25.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_custom_resolver(**req_copy)


    def test_create_custom_resolver_value_error_with_retries(self):
        # Enable retries and run test_create_custom_resolver_value_error.
        _service.enable_retries()
        self.test_create_custom_resolver_value_error()

        # Disable retries and run test_create_custom_resolver_value_error.
        _service.disable_retries()
        self.test_create_custom_resolver_value_error()

class TestDeleteCustomResolver():
    """
    Test Class for delete_custom_resolver
    """

    @responses.activate
    def test_delete_custom_resolver_all_params(self):
        """
        delete_custom_resolver()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.delete_custom_resolver(
            instance_id,
            resolver_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_custom_resolver_all_params_with_retries(self):
        # Enable retries and run test_delete_custom_resolver_all_params.
        _service.enable_retries()
        self.test_delete_custom_resolver_all_params()

        # Disable retries and run test_delete_custom_resolver_all_params.
        _service.disable_retries()
        self.test_delete_custom_resolver_all_params()

    @responses.activate
    def test_delete_custom_resolver_required_params(self):
        """
        test_delete_custom_resolver_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'

        # Invoke method
        response = _service.delete_custom_resolver(
            instance_id,
            resolver_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_custom_resolver_required_params_with_retries(self):
        # Enable retries and run test_delete_custom_resolver_required_params.
        _service.enable_retries()
        self.test_delete_custom_resolver_required_params()

        # Disable retries and run test_delete_custom_resolver_required_params.
        _service.disable_retries()
        self.test_delete_custom_resolver_required_params()

    @responses.activate
    def test_delete_custom_resolver_value_error(self):
        """
        test_delete_custom_resolver_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "resolver_id": resolver_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_custom_resolver(**req_copy)


    def test_delete_custom_resolver_value_error_with_retries(self):
        # Enable retries and run test_delete_custom_resolver_value_error.
        _service.enable_retries()
        self.test_delete_custom_resolver_value_error()

        # Disable retries and run test_delete_custom_resolver_value_error.
        _service.disable_retries()
        self.test_delete_custom_resolver_value_error()

class TestGetCustomResolver():
    """
    Test Class for get_custom_resolver
    """

    @responses.activate
    def test_get_custom_resolver_all_params(self):
        """
        get_custom_resolver()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "my-resolver", "description": "custom resolver", "enabled": false, "health": "HEALTHY", "locations": [{"id": "9a234ede-c2b6-4c39-bc27-d39ec139ecdb", "subnet_crn": "crn:v1:bluemix:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "enabled": true, "healthy": true, "dns_server_ip": "10.10.16.8"}], "created_on": "2021-04-21T08:18:25.000Z", "modified_on": "2021-04-21T08:18:25.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.get_custom_resolver(
            instance_id,
            resolver_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_custom_resolver_all_params_with_retries(self):
        # Enable retries and run test_get_custom_resolver_all_params.
        _service.enable_retries()
        self.test_get_custom_resolver_all_params()

        # Disable retries and run test_get_custom_resolver_all_params.
        _service.disable_retries()
        self.test_get_custom_resolver_all_params()

    @responses.activate
    def test_get_custom_resolver_required_params(self):
        """
        test_get_custom_resolver_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "my-resolver", "description": "custom resolver", "enabled": false, "health": "HEALTHY", "locations": [{"id": "9a234ede-c2b6-4c39-bc27-d39ec139ecdb", "subnet_crn": "crn:v1:bluemix:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "enabled": true, "healthy": true, "dns_server_ip": "10.10.16.8"}], "created_on": "2021-04-21T08:18:25.000Z", "modified_on": "2021-04-21T08:18:25.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'

        # Invoke method
        response = _service.get_custom_resolver(
            instance_id,
            resolver_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_custom_resolver_required_params_with_retries(self):
        # Enable retries and run test_get_custom_resolver_required_params.
        _service.enable_retries()
        self.test_get_custom_resolver_required_params()

        # Disable retries and run test_get_custom_resolver_required_params.
        _service.disable_retries()
        self.test_get_custom_resolver_required_params()

    @responses.activate
    def test_get_custom_resolver_value_error(self):
        """
        test_get_custom_resolver_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "my-resolver", "description": "custom resolver", "enabled": false, "health": "HEALTHY", "locations": [{"id": "9a234ede-c2b6-4c39-bc27-d39ec139ecdb", "subnet_crn": "crn:v1:bluemix:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "enabled": true, "healthy": true, "dns_server_ip": "10.10.16.8"}], "created_on": "2021-04-21T08:18:25.000Z", "modified_on": "2021-04-21T08:18:25.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "resolver_id": resolver_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_custom_resolver(**req_copy)


    def test_get_custom_resolver_value_error_with_retries(self):
        # Enable retries and run test_get_custom_resolver_value_error.
        _service.enable_retries()
        self.test_get_custom_resolver_value_error()

        # Disable retries and run test_get_custom_resolver_value_error.
        _service.disable_retries()
        self.test_get_custom_resolver_value_error()

class TestCustomResolver():
    """
    Test Class for update_custom_resolver
    """

    @responses.activate
    def test_update_custom_resolver_all_params(self):
        """
        update_custom_resolver()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "my-resolver", "description": "custom resolver", "enabled": false, "health": "HEALTHY", "locations": [{"id": "9a234ede-c2b6-4c39-bc27-d39ec139ecdb", "subnet_crn": "crn:v1:bluemix:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "enabled": true, "healthy": true, "dns_server_ip": "10.10.16.8"}], "created_on": "2021-04-21T08:18:25.000Z", "modified_on": "2021-04-21T08:18:25.000Z"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        name = 'my-resolver'
        description = 'custom resolver'
        enabled = False
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.update_custom_resolver(
            instance_id,
            resolver_id,
            name=name,
            description=description,
            enabled=enabled,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'my-resolver'
        assert req_body['description'] == 'custom resolver'
        assert req_body['enabled'] == False

    def test_update_custom_resolver_all_params_with_retries(self):
        # Enable retries and run test_update_custom_resolver_all_params.
        _service.enable_retries()
        self.test_update_custom_resolver_all_params()

        # Disable retries and run test_update_custom_resolver_all_params.
        _service.disable_retries()
        self.test_update_custom_resolver_all_params()

    @responses.activate
    def test_update_custom_resolver_required_params(self):
        """
        test_update_custom_resolver_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "my-resolver", "description": "custom resolver", "enabled": false, "health": "HEALTHY", "locations": [{"id": "9a234ede-c2b6-4c39-bc27-d39ec139ecdb", "subnet_crn": "crn:v1:bluemix:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "enabled": true, "healthy": true, "dns_server_ip": "10.10.16.8"}], "created_on": "2021-04-21T08:18:25.000Z", "modified_on": "2021-04-21T08:18:25.000Z"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'

        # Invoke method
        response = _service.update_custom_resolver(
            instance_id,
            resolver_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_custom_resolver_required_params_with_retries(self):
        # Enable retries and run test_update_custom_resolver_required_params.
        _service.enable_retries()
        self.test_update_custom_resolver_required_params()

        # Disable retries and run test_update_custom_resolver_required_params.
        _service.disable_retries()
        self.test_update_custom_resolver_required_params()

    @responses.activate
    def test_update_custom_resolver_value_error(self):
        """
        test_update_custom_resolver_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "my-resolver", "description": "custom resolver", "enabled": false, "health": "HEALTHY", "locations": [{"id": "9a234ede-c2b6-4c39-bc27-d39ec139ecdb", "subnet_crn": "crn:v1:bluemix:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "enabled": true, "healthy": true, "dns_server_ip": "10.10.16.8"}], "created_on": "2021-04-21T08:18:25.000Z", "modified_on": "2021-04-21T08:18:25.000Z"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "resolver_id": resolver_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_custom_resolver(**req_copy)


    def test_update_custom_resolver_value_error_with_retries(self):
        # Enable retries and run test_update_custom_resolver_value_error.
        _service.enable_retries()
        self.test_update_custom_resolver_value_error()

        # Disable retries and run test_update_custom_resolver_value_error.
        _service.disable_retries()
        self.test_update_custom_resolver_value_error()

class TestUpdateCrLocationsOrder():
    """
    Test Class for update_cr_locations_order
    """

    @responses.activate
    def test_update_cr_locations_order_all_params(self):
        """
        update_cr_locations_order()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/locations_order')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "my-resolver", "description": "custom resolver", "enabled": false, "health": "HEALTHY", "locations": [{"id": "9a234ede-c2b6-4c39-bc27-d39ec139ecdb", "subnet_crn": "crn:v1:bluemix:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "enabled": true, "healthy": true, "dns_server_ip": "10.10.16.8"}], "created_on": "2021-04-21T08:18:25.000Z", "modified_on": "2021-04-21T08:18:25.000Z"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        locations = ['9a234ede-c2b6-4c39-bc27-d39ec139ecdb']
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.update_cr_locations_order(
            instance_id,
            resolver_id,
            locations=locations,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['locations'] == ['9a234ede-c2b6-4c39-bc27-d39ec139ecdb']

    def test_update_cr_locations_order_all_params_with_retries(self):
        # Enable retries and run test_update_cr_locations_order_all_params.
        _service.enable_retries()
        self.test_update_cr_locations_order_all_params()

        # Disable retries and run test_update_cr_locations_order_all_params.
        _service.disable_retries()
        self.test_update_cr_locations_order_all_params()

    @responses.activate
    def test_update_cr_locations_order_required_params(self):
        """
        test_update_cr_locations_order_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/locations_order')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "my-resolver", "description": "custom resolver", "enabled": false, "health": "HEALTHY", "locations": [{"id": "9a234ede-c2b6-4c39-bc27-d39ec139ecdb", "subnet_crn": "crn:v1:bluemix:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "enabled": true, "healthy": true, "dns_server_ip": "10.10.16.8"}], "created_on": "2021-04-21T08:18:25.000Z", "modified_on": "2021-04-21T08:18:25.000Z"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'

        # Invoke method
        response = _service.update_cr_locations_order(
            instance_id,
            resolver_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_cr_locations_order_required_params_with_retries(self):
        # Enable retries and run test_update_cr_locations_order_required_params.
        _service.enable_retries()
        self.test_update_cr_locations_order_required_params()

        # Disable retries and run test_update_cr_locations_order_required_params.
        _service.disable_retries()
        self.test_update_cr_locations_order_required_params()

    @responses.activate
    def test_update_cr_locations_order_value_error(self):
        """
        test_update_cr_locations_order_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/locations_order')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "name": "my-resolver", "description": "custom resolver", "enabled": false, "health": "HEALTHY", "locations": [{"id": "9a234ede-c2b6-4c39-bc27-d39ec139ecdb", "subnet_crn": "crn:v1:bluemix:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "enabled": true, "healthy": true, "dns_server_ip": "10.10.16.8"}], "created_on": "2021-04-21T08:18:25.000Z", "modified_on": "2021-04-21T08:18:25.000Z"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "resolver_id": resolver_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_cr_locations_order(**req_copy)


    def test_update_cr_locations_order_value_error_with_retries(self):
        # Enable retries and run test_update_cr_locations_order_value_error.
        _service.enable_retries()
        self.test_update_cr_locations_order_value_error()

        # Disable retries and run test_update_cr_locations_order_value_error.
        _service.disable_retries()
        self.test_update_cr_locations_order_value_error()

# endregion
##############################################################################
# End of Service: CustomResolvers
##############################################################################

##############################################################################
# Start of Service: CustomResolverLocations
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = DnsSvcsV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DnsSvcsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DnsSvcsV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestAddCustomResolverLocation():
    """
    Test Class for add_custom_resolver_location
    """

    @responses.activate
    def test_add_custom_resolver_location_all_params(self):
        """
        add_custom_resolver_location()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/locations')
        mock_response = '{"id": "9a234ede-c2b6-4c39-bc27-d39ec139ecdb", "subnet_crn": "crn:v1:bluemix:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "enabled": true, "healthy": true, "dns_server_ip": "10.10.16.8"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        subnet_crn = 'crn:v1:bluemix:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04'
        enabled = False
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.add_custom_resolver_location(
            instance_id,
            resolver_id,
            subnet_crn=subnet_crn,
            enabled=enabled,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['subnet_crn'] == 'crn:v1:bluemix:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04'
        assert req_body['enabled'] == False

    def test_add_custom_resolver_location_all_params_with_retries(self):
        # Enable retries and run test_add_custom_resolver_location_all_params.
        _service.enable_retries()
        self.test_add_custom_resolver_location_all_params()

        # Disable retries and run test_add_custom_resolver_location_all_params.
        _service.disable_retries()
        self.test_add_custom_resolver_location_all_params()

    @responses.activate
    def test_add_custom_resolver_location_required_params(self):
        """
        test_add_custom_resolver_location_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/locations')
        mock_response = '{"id": "9a234ede-c2b6-4c39-bc27-d39ec139ecdb", "subnet_crn": "crn:v1:bluemix:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "enabled": true, "healthy": true, "dns_server_ip": "10.10.16.8"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'

        # Invoke method
        response = _service.add_custom_resolver_location(
            instance_id,
            resolver_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_add_custom_resolver_location_required_params_with_retries(self):
        # Enable retries and run test_add_custom_resolver_location_required_params.
        _service.enable_retries()
        self.test_add_custom_resolver_location_required_params()

        # Disable retries and run test_add_custom_resolver_location_required_params.
        _service.disable_retries()
        self.test_add_custom_resolver_location_required_params()

    @responses.activate
    def test_add_custom_resolver_location_value_error(self):
        """
        test_add_custom_resolver_location_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/locations')
        mock_response = '{"id": "9a234ede-c2b6-4c39-bc27-d39ec139ecdb", "subnet_crn": "crn:v1:bluemix:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "enabled": true, "healthy": true, "dns_server_ip": "10.10.16.8"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "resolver_id": resolver_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.add_custom_resolver_location(**req_copy)


    def test_add_custom_resolver_location_value_error_with_retries(self):
        # Enable retries and run test_add_custom_resolver_location_value_error.
        _service.enable_retries()
        self.test_add_custom_resolver_location_value_error()

        # Disable retries and run test_add_custom_resolver_location_value_error.
        _service.disable_retries()
        self.test_add_custom_resolver_location_value_error()

class TestUpdateCustomResolverLocation():
    """
    Test Class for update_custom_resolver_location
    """

    @responses.activate
    def test_update_custom_resolver_location_all_params(self):
        """
        update_custom_resolver_location()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/locations/testString')
        mock_response = '{"id": "9a234ede-c2b6-4c39-bc27-d39ec139ecdb", "subnet_crn": "crn:v1:bluemix:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "enabled": true, "healthy": true, "dns_server_ip": "10.10.16.8"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        location_id = 'testString'
        enabled = False
        subnet_crn = 'crn:v1:bluemix:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.update_custom_resolver_location(
            instance_id,
            resolver_id,
            location_id,
            enabled=enabled,
            subnet_crn=subnet_crn,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['enabled'] == False
        assert req_body['subnet_crn'] == 'crn:v1:bluemix:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04'

    def test_update_custom_resolver_location_all_params_with_retries(self):
        # Enable retries and run test_update_custom_resolver_location_all_params.
        _service.enable_retries()
        self.test_update_custom_resolver_location_all_params()

        # Disable retries and run test_update_custom_resolver_location_all_params.
        _service.disable_retries()
        self.test_update_custom_resolver_location_all_params()

    @responses.activate
    def test_update_custom_resolver_location_required_params(self):
        """
        test_update_custom_resolver_location_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/locations/testString')
        mock_response = '{"id": "9a234ede-c2b6-4c39-bc27-d39ec139ecdb", "subnet_crn": "crn:v1:bluemix:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "enabled": true, "healthy": true, "dns_server_ip": "10.10.16.8"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        location_id = 'testString'

        # Invoke method
        response = _service.update_custom_resolver_location(
            instance_id,
            resolver_id,
            location_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_custom_resolver_location_required_params_with_retries(self):
        # Enable retries and run test_update_custom_resolver_location_required_params.
        _service.enable_retries()
        self.test_update_custom_resolver_location_required_params()

        # Disable retries and run test_update_custom_resolver_location_required_params.
        _service.disable_retries()
        self.test_update_custom_resolver_location_required_params()

    @responses.activate
    def test_update_custom_resolver_location_value_error(self):
        """
        test_update_custom_resolver_location_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/locations/testString')
        mock_response = '{"id": "9a234ede-c2b6-4c39-bc27-d39ec139ecdb", "subnet_crn": "crn:v1:bluemix:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04", "enabled": true, "healthy": true, "dns_server_ip": "10.10.16.8"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        location_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "resolver_id": resolver_id,
            "location_id": location_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_custom_resolver_location(**req_copy)


    def test_update_custom_resolver_location_value_error_with_retries(self):
        # Enable retries and run test_update_custom_resolver_location_value_error.
        _service.enable_retries()
        self.test_update_custom_resolver_location_value_error()

        # Disable retries and run test_update_custom_resolver_location_value_error.
        _service.disable_retries()
        self.test_update_custom_resolver_location_value_error()

class TestDeleteCustomResolverLocation():
    """
    Test Class for delete_custom_resolver_location
    """

    @responses.activate
    def test_delete_custom_resolver_location_all_params(self):
        """
        delete_custom_resolver_location()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/locations/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        location_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.delete_custom_resolver_location(
            instance_id,
            resolver_id,
            location_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_custom_resolver_location_all_params_with_retries(self):
        # Enable retries and run test_delete_custom_resolver_location_all_params.
        _service.enable_retries()
        self.test_delete_custom_resolver_location_all_params()

        # Disable retries and run test_delete_custom_resolver_location_all_params.
        _service.disable_retries()
        self.test_delete_custom_resolver_location_all_params()

    @responses.activate
    def test_delete_custom_resolver_location_required_params(self):
        """
        test_delete_custom_resolver_location_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/locations/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        location_id = 'testString'

        # Invoke method
        response = _service.delete_custom_resolver_location(
            instance_id,
            resolver_id,
            location_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_custom_resolver_location_required_params_with_retries(self):
        # Enable retries and run test_delete_custom_resolver_location_required_params.
        _service.enable_retries()
        self.test_delete_custom_resolver_location_required_params()

        # Disable retries and run test_delete_custom_resolver_location_required_params.
        _service.disable_retries()
        self.test_delete_custom_resolver_location_required_params()

    @responses.activate
    def test_delete_custom_resolver_location_value_error(self):
        """
        test_delete_custom_resolver_location_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/locations/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        location_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "resolver_id": resolver_id,
            "location_id": location_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_custom_resolver_location(**req_copy)


    def test_delete_custom_resolver_location_value_error_with_retries(self):
        # Enable retries and run test_delete_custom_resolver_location_value_error.
        _service.enable_retries()
        self.test_delete_custom_resolver_location_value_error()

        # Disable retries and run test_delete_custom_resolver_location_value_error.
        _service.disable_retries()
        self.test_delete_custom_resolver_location_value_error()

# endregion
##############################################################################
# End of Service: CustomResolverLocations
##############################################################################

##############################################################################
# Start of Service: ForwardingRules
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = DnsSvcsV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DnsSvcsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DnsSvcsV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestListForwardingRules():
    """
    Test Class for list_forwarding_rules
    """

    @responses.activate
    def test_list_forwarding_rules_all_params(self):
        """
        list_forwarding_rules()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/forwarding_rules')
        mock_response = '{"forwarding_rules": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "description": "forwarding rule", "type": "zone", "match": "example.com", "forward_to": ["161.26.0.7"], "created_on": "2021-04-21T08:18:25.000Z", "modified_on": "2021-04-21T08:18:25.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.list_forwarding_rules(
            instance_id,
            resolver_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_forwarding_rules_all_params_with_retries(self):
        # Enable retries and run test_list_forwarding_rules_all_params.
        _service.enable_retries()
        self.test_list_forwarding_rules_all_params()

        # Disable retries and run test_list_forwarding_rules_all_params.
        _service.disable_retries()
        self.test_list_forwarding_rules_all_params()

    @responses.activate
    def test_list_forwarding_rules_required_params(self):
        """
        test_list_forwarding_rules_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/forwarding_rules')
        mock_response = '{"forwarding_rules": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "description": "forwarding rule", "type": "zone", "match": "example.com", "forward_to": ["161.26.0.7"], "created_on": "2021-04-21T08:18:25.000Z", "modified_on": "2021-04-21T08:18:25.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'

        # Invoke method
        response = _service.list_forwarding_rules(
            instance_id,
            resolver_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_forwarding_rules_required_params_with_retries(self):
        # Enable retries and run test_list_forwarding_rules_required_params.
        _service.enable_retries()
        self.test_list_forwarding_rules_required_params()

        # Disable retries and run test_list_forwarding_rules_required_params.
        _service.disable_retries()
        self.test_list_forwarding_rules_required_params()

    @responses.activate
    def test_list_forwarding_rules_value_error(self):
        """
        test_list_forwarding_rules_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/forwarding_rules')
        mock_response = '{"forwarding_rules": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "description": "forwarding rule", "type": "zone", "match": "example.com", "forward_to": ["161.26.0.7"], "created_on": "2021-04-21T08:18:25.000Z", "modified_on": "2021-04-21T08:18:25.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "resolver_id": resolver_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_forwarding_rules(**req_copy)


    def test_list_forwarding_rules_value_error_with_retries(self):
        # Enable retries and run test_list_forwarding_rules_value_error.
        _service.enable_retries()
        self.test_list_forwarding_rules_value_error()

        # Disable retries and run test_list_forwarding_rules_value_error.
        _service.disable_retries()
        self.test_list_forwarding_rules_value_error()

class TestCreateForwardingRule():
    """
    Test Class for create_forwarding_rule
    """

    @responses.activate
    def test_create_forwarding_rule_all_params(self):
        """
        create_forwarding_rule()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/forwarding_rules')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "description": "forwarding rule", "type": "zone", "match": "example.com", "forward_to": ["161.26.0.7"], "created_on": "2021-04-21T08:18:25.000Z", "modified_on": "2021-04-21T08:18:25.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        type = 'zone'
        match = 'example.com'
        forward_to = ['161.26.0.7']
        description = 'forwarding rule'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.create_forwarding_rule(
            instance_id,
            resolver_id,
            type=type,
            match=match,
            forward_to=forward_to,
            description=description,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'zone'
        assert req_body['match'] == 'example.com'
        assert req_body['forward_to'] == ['161.26.0.7']
        assert req_body['description'] == 'forwarding rule'

    def test_create_forwarding_rule_all_params_with_retries(self):
        # Enable retries and run test_create_forwarding_rule_all_params.
        _service.enable_retries()
        self.test_create_forwarding_rule_all_params()

        # Disable retries and run test_create_forwarding_rule_all_params.
        _service.disable_retries()
        self.test_create_forwarding_rule_all_params()

    @responses.activate
    def test_create_forwarding_rule_required_params(self):
        """
        test_create_forwarding_rule_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/forwarding_rules')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "description": "forwarding rule", "type": "zone", "match": "example.com", "forward_to": ["161.26.0.7"], "created_on": "2021-04-21T08:18:25.000Z", "modified_on": "2021-04-21T08:18:25.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'

        # Invoke method
        response = _service.create_forwarding_rule(
            instance_id,
            resolver_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_forwarding_rule_required_params_with_retries(self):
        # Enable retries and run test_create_forwarding_rule_required_params.
        _service.enable_retries()
        self.test_create_forwarding_rule_required_params()

        # Disable retries and run test_create_forwarding_rule_required_params.
        _service.disable_retries()
        self.test_create_forwarding_rule_required_params()

    @responses.activate
    def test_create_forwarding_rule_value_error(self):
        """
        test_create_forwarding_rule_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/forwarding_rules')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "description": "forwarding rule", "type": "zone", "match": "example.com", "forward_to": ["161.26.0.7"], "created_on": "2021-04-21T08:18:25.000Z", "modified_on": "2021-04-21T08:18:25.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "resolver_id": resolver_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_forwarding_rule(**req_copy)


    def test_create_forwarding_rule_value_error_with_retries(self):
        # Enable retries and run test_create_forwarding_rule_value_error.
        _service.enable_retries()
        self.test_create_forwarding_rule_value_error()

        # Disable retries and run test_create_forwarding_rule_value_error.
        _service.disable_retries()
        self.test_create_forwarding_rule_value_error()

class TestDeleteForwardingRule():
    """
    Test Class for delete_forwarding_rule
    """

    @responses.activate
    def test_delete_forwarding_rule_all_params(self):
        """
        delete_forwarding_rule()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/forwarding_rules/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        rule_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.delete_forwarding_rule(
            instance_id,
            resolver_id,
            rule_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_forwarding_rule_all_params_with_retries(self):
        # Enable retries and run test_delete_forwarding_rule_all_params.
        _service.enable_retries()
        self.test_delete_forwarding_rule_all_params()

        # Disable retries and run test_delete_forwarding_rule_all_params.
        _service.disable_retries()
        self.test_delete_forwarding_rule_all_params()

    @responses.activate
    def test_delete_forwarding_rule_required_params(self):
        """
        test_delete_forwarding_rule_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/forwarding_rules/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        rule_id = 'testString'

        # Invoke method
        response = _service.delete_forwarding_rule(
            instance_id,
            resolver_id,
            rule_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_forwarding_rule_required_params_with_retries(self):
        # Enable retries and run test_delete_forwarding_rule_required_params.
        _service.enable_retries()
        self.test_delete_forwarding_rule_required_params()

        # Disable retries and run test_delete_forwarding_rule_required_params.
        _service.disable_retries()
        self.test_delete_forwarding_rule_required_params()

    @responses.activate
    def test_delete_forwarding_rule_value_error(self):
        """
        test_delete_forwarding_rule_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/forwarding_rules/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        rule_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "resolver_id": resolver_id,
            "rule_id": rule_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_forwarding_rule(**req_copy)


    def test_delete_forwarding_rule_value_error_with_retries(self):
        # Enable retries and run test_delete_forwarding_rule_value_error.
        _service.enable_retries()
        self.test_delete_forwarding_rule_value_error()

        # Disable retries and run test_delete_forwarding_rule_value_error.
        _service.disable_retries()
        self.test_delete_forwarding_rule_value_error()

class TestGetForwardingRule():
    """
    Test Class for get_forwarding_rule
    """

    @responses.activate
    def test_get_forwarding_rule_all_params(self):
        """
        get_forwarding_rule()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/forwarding_rules/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "description": "forwarding rule", "type": "zone", "match": "example.com", "forward_to": ["161.26.0.7"], "created_on": "2021-04-21T08:18:25.000Z", "modified_on": "2021-04-21T08:18:25.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        rule_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.get_forwarding_rule(
            instance_id,
            resolver_id,
            rule_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_forwarding_rule_all_params_with_retries(self):
        # Enable retries and run test_get_forwarding_rule_all_params.
        _service.enable_retries()
        self.test_get_forwarding_rule_all_params()

        # Disable retries and run test_get_forwarding_rule_all_params.
        _service.disable_retries()
        self.test_get_forwarding_rule_all_params()

    @responses.activate
    def test_get_forwarding_rule_required_params(self):
        """
        test_get_forwarding_rule_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/forwarding_rules/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "description": "forwarding rule", "type": "zone", "match": "example.com", "forward_to": ["161.26.0.7"], "created_on": "2021-04-21T08:18:25.000Z", "modified_on": "2021-04-21T08:18:25.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        rule_id = 'testString'

        # Invoke method
        response = _service.get_forwarding_rule(
            instance_id,
            resolver_id,
            rule_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_forwarding_rule_required_params_with_retries(self):
        # Enable retries and run test_get_forwarding_rule_required_params.
        _service.enable_retries()
        self.test_get_forwarding_rule_required_params()

        # Disable retries and run test_get_forwarding_rule_required_params.
        _service.disable_retries()
        self.test_get_forwarding_rule_required_params()

    @responses.activate
    def test_get_forwarding_rule_value_error(self):
        """
        test_get_forwarding_rule_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/forwarding_rules/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "description": "forwarding rule", "type": "zone", "match": "example.com", "forward_to": ["161.26.0.7"], "created_on": "2021-04-21T08:18:25.000Z", "modified_on": "2021-04-21T08:18:25.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        rule_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "resolver_id": resolver_id,
            "rule_id": rule_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_forwarding_rule(**req_copy)


    def test_get_forwarding_rule_value_error_with_retries(self):
        # Enable retries and run test_get_forwarding_rule_value_error.
        _service.enable_retries()
        self.test_get_forwarding_rule_value_error()

        # Disable retries and run test_get_forwarding_rule_value_error.
        _service.disable_retries()
        self.test_get_forwarding_rule_value_error()

class TestUpdateForwardingRule():
    """
    Test Class for update_forwarding_rule
    """

    @responses.activate
    def test_update_forwarding_rule_all_params(self):
        """
        update_forwarding_rule()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/forwarding_rules/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "description": "forwarding rule", "type": "zone", "match": "example.com", "forward_to": ["161.26.0.7"], "created_on": "2021-04-21T08:18:25.000Z", "modified_on": "2021-04-21T08:18:25.000Z"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        rule_id = 'testString'
        description = 'forwarding rule'
        match = 'example.com'
        forward_to = ['161.26.0.7']
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.update_forwarding_rule(
            instance_id,
            resolver_id,
            rule_id,
            description=description,
            match=match,
            forward_to=forward_to,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['description'] == 'forwarding rule'
        assert req_body['match'] == 'example.com'
        assert req_body['forward_to'] == ['161.26.0.7']

    def test_update_forwarding_rule_all_params_with_retries(self):
        # Enable retries and run test_update_forwarding_rule_all_params.
        _service.enable_retries()
        self.test_update_forwarding_rule_all_params()

        # Disable retries and run test_update_forwarding_rule_all_params.
        _service.disable_retries()
        self.test_update_forwarding_rule_all_params()

    @responses.activate
    def test_update_forwarding_rule_required_params(self):
        """
        test_update_forwarding_rule_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/forwarding_rules/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "description": "forwarding rule", "type": "zone", "match": "example.com", "forward_to": ["161.26.0.7"], "created_on": "2021-04-21T08:18:25.000Z", "modified_on": "2021-04-21T08:18:25.000Z"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        rule_id = 'testString'

        # Invoke method
        response = _service.update_forwarding_rule(
            instance_id,
            resolver_id,
            rule_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_forwarding_rule_required_params_with_retries(self):
        # Enable retries and run test_update_forwarding_rule_required_params.
        _service.enable_retries()
        self.test_update_forwarding_rule_required_params()

        # Disable retries and run test_update_forwarding_rule_required_params.
        _service.disable_retries()
        self.test_update_forwarding_rule_required_params()

    @responses.activate
    def test_update_forwarding_rule_value_error(self):
        """
        test_update_forwarding_rule_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/forwarding_rules/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "description": "forwarding rule", "type": "zone", "match": "example.com", "forward_to": ["161.26.0.7"], "created_on": "2021-04-21T08:18:25.000Z", "modified_on": "2021-04-21T08:18:25.000Z"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        rule_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "resolver_id": resolver_id,
            "rule_id": rule_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_forwarding_rule(**req_copy)


    def test_update_forwarding_rule_value_error_with_retries(self):
        # Enable retries and run test_update_forwarding_rule_value_error.
        _service.enable_retries()
        self.test_update_forwarding_rule_value_error()

        # Disable retries and run test_update_forwarding_rule_value_error.
        _service.disable_retries()
        self.test_update_forwarding_rule_value_error()

# endregion
##############################################################################
# End of Service: ForwardingRules
##############################################################################

##############################################################################
# Start of Service: SecondaryZones
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = DnsSvcsV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DnsSvcsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DnsSvcsV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestCreateSecondaryZone():
    """
    Test Class for create_secondary_zone
    """

    @responses.activate
    def test_create_secondary_zone_all_params(self):
        """
        create_secondary_zone()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/secondary_zones')
        mock_response = '{"id": "f97ef698-d5fa-4f91-bc5a-33f17d143b7d", "description": "secondary zone", "zone": "example.com", "enabled": false, "transfer_from": [{"address": "10.0.0.7", "port": 53}], "created_on": "2022-03-16T08:18:25Z", "modified_on": "2022-03-16T08:18:25Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a SecondaryZoneSourceInputItem model
        secondary_zone_source_input_item_model = {}
        secondary_zone_source_input_item_model['address'] = '10.0.0.7'

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        zone = 'example.com'
        transfer_from = [secondary_zone_source_input_item_model]
        description = 'secondary zone'
        enabled = False
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.create_secondary_zone(
            instance_id,
            resolver_id,
            zone=zone,
            transfer_from=transfer_from,
            description=description,
            enabled=enabled,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['zone'] == 'example.com'
        assert req_body['transfer_from'] == [secondary_zone_source_input_item_model]
        assert req_body['description'] == 'secondary zone'
        assert req_body['enabled'] == False

    def test_create_secondary_zone_all_params_with_retries(self):
        # Enable retries and run test_create_secondary_zone_all_params.
        _service.enable_retries()
        self.test_create_secondary_zone_all_params()

        # Disable retries and run test_create_secondary_zone_all_params.
        _service.disable_retries()
        self.test_create_secondary_zone_all_params()

    @responses.activate
    def test_create_secondary_zone_required_params(self):
        """
        test_create_secondary_zone_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/secondary_zones')
        mock_response = '{"id": "f97ef698-d5fa-4f91-bc5a-33f17d143b7d", "description": "secondary zone", "zone": "example.com", "enabled": false, "transfer_from": [{"address": "10.0.0.7", "port": 53}], "created_on": "2022-03-16T08:18:25Z", "modified_on": "2022-03-16T08:18:25Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'

        # Invoke method
        response = _service.create_secondary_zone(
            instance_id,
            resolver_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_secondary_zone_required_params_with_retries(self):
        # Enable retries and run test_create_secondary_zone_required_params.
        _service.enable_retries()
        self.test_create_secondary_zone_required_params()

        # Disable retries and run test_create_secondary_zone_required_params.
        _service.disable_retries()
        self.test_create_secondary_zone_required_params()

    @responses.activate
    def test_create_secondary_zone_value_error(self):
        """
        test_create_secondary_zone_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/secondary_zones')
        mock_response = '{"id": "f97ef698-d5fa-4f91-bc5a-33f17d143b7d", "description": "secondary zone", "zone": "example.com", "enabled": false, "transfer_from": [{"address": "10.0.0.7", "port": 53}], "created_on": "2022-03-16T08:18:25Z", "modified_on": "2022-03-16T08:18:25Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "resolver_id": resolver_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_secondary_zone(**req_copy)


    def test_create_secondary_zone_value_error_with_retries(self):
        # Enable retries and run test_create_secondary_zone_value_error.
        _service.enable_retries()
        self.test_create_secondary_zone_value_error()

        # Disable retries and run test_create_secondary_zone_value_error.
        _service.disable_retries()
        self.test_create_secondary_zone_value_error()

class TestListSecondaryZones():
    """
    Test Class for list_secondary_zones
    """

    @responses.activate
    def test_list_secondary_zones_all_params(self):
        """
        list_secondary_zones()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/secondary_zones')
        mock_response = '{"secondary_zones": [{"id": "f97ef698-d5fa-4f91-bc5a-33f17d143b7d", "description": "secondary zone", "zone": "example.com", "enabled": false, "transfer_from": [{"address": "10.0.0.7", "port": 53}], "created_on": "2022-03-16T08:18:25Z", "modified_on": "2022-03-16T08:18:25Z"}], "offset": 0, "limit": 200, "count": 1, "total_count": 1, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "last": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "previous": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        x_correlation_id = 'testString'
        offset = 38
        limit = 200

        # Invoke method
        response = _service.list_secondary_zones(
            instance_id,
            resolver_id,
            x_correlation_id=x_correlation_id,
            offset=offset,
            limit=limit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'offset={}'.format(offset) in query_string
        assert 'limit={}'.format(limit) in query_string

    def test_list_secondary_zones_all_params_with_retries(self):
        # Enable retries and run test_list_secondary_zones_all_params.
        _service.enable_retries()
        self.test_list_secondary_zones_all_params()

        # Disable retries and run test_list_secondary_zones_all_params.
        _service.disable_retries()
        self.test_list_secondary_zones_all_params()

    @responses.activate
    def test_list_secondary_zones_required_params(self):
        """
        test_list_secondary_zones_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/secondary_zones')
        mock_response = '{"secondary_zones": [{"id": "f97ef698-d5fa-4f91-bc5a-33f17d143b7d", "description": "secondary zone", "zone": "example.com", "enabled": false, "transfer_from": [{"address": "10.0.0.7", "port": 53}], "created_on": "2022-03-16T08:18:25Z", "modified_on": "2022-03-16T08:18:25Z"}], "offset": 0, "limit": 200, "count": 1, "total_count": 1, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "last": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "previous": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'

        # Invoke method
        response = _service.list_secondary_zones(
            instance_id,
            resolver_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_secondary_zones_required_params_with_retries(self):
        # Enable retries and run test_list_secondary_zones_required_params.
        _service.enable_retries()
        self.test_list_secondary_zones_required_params()

        # Disable retries and run test_list_secondary_zones_required_params.
        _service.disable_retries()
        self.test_list_secondary_zones_required_params()

    @responses.activate
    def test_list_secondary_zones_value_error(self):
        """
        test_list_secondary_zones_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/secondary_zones')
        mock_response = '{"secondary_zones": [{"id": "f97ef698-d5fa-4f91-bc5a-33f17d143b7d", "description": "secondary zone", "zone": "example.com", "enabled": false, "transfer_from": [{"address": "10.0.0.7", "port": 53}], "created_on": "2022-03-16T08:18:25Z", "modified_on": "2022-03-16T08:18:25Z"}], "offset": 0, "limit": 200, "count": 1, "total_count": 1, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "last": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "previous": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "resolver_id": resolver_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_secondary_zones(**req_copy)


    def test_list_secondary_zones_value_error_with_retries(self):
        # Enable retries and run test_list_secondary_zones_value_error.
        _service.enable_retries()
        self.test_list_secondary_zones_value_error()

        # Disable retries and run test_list_secondary_zones_value_error.
        _service.disable_retries()
        self.test_list_secondary_zones_value_error()

class TestGetSecondaryZone():
    """
    Test Class for get_secondary_zone
    """

    @responses.activate
    def test_get_secondary_zone_all_params(self):
        """
        get_secondary_zone()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/secondary_zones/testString')
        mock_response = '{"id": "f97ef698-d5fa-4f91-bc5a-33f17d143b7d", "description": "secondary zone", "zone": "example.com", "enabled": false, "transfer_from": [{"address": "10.0.0.7", "port": 53}], "created_on": "2022-03-16T08:18:25Z", "modified_on": "2022-03-16T08:18:25Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        sz_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.get_secondary_zone(
            instance_id,
            resolver_id,
            sz_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_secondary_zone_all_params_with_retries(self):
        # Enable retries and run test_get_secondary_zone_all_params.
        _service.enable_retries()
        self.test_get_secondary_zone_all_params()

        # Disable retries and run test_get_secondary_zone_all_params.
        _service.disable_retries()
        self.test_get_secondary_zone_all_params()

    @responses.activate
    def test_get_secondary_zone_required_params(self):
        """
        test_get_secondary_zone_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/secondary_zones/testString')
        mock_response = '{"id": "f97ef698-d5fa-4f91-bc5a-33f17d143b7d", "description": "secondary zone", "zone": "example.com", "enabled": false, "transfer_from": [{"address": "10.0.0.7", "port": 53}], "created_on": "2022-03-16T08:18:25Z", "modified_on": "2022-03-16T08:18:25Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        sz_id = 'testString'

        # Invoke method
        response = _service.get_secondary_zone(
            instance_id,
            resolver_id,
            sz_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_secondary_zone_required_params_with_retries(self):
        # Enable retries and run test_get_secondary_zone_required_params.
        _service.enable_retries()
        self.test_get_secondary_zone_required_params()

        # Disable retries and run test_get_secondary_zone_required_params.
        _service.disable_retries()
        self.test_get_secondary_zone_required_params()

    @responses.activate
    def test_get_secondary_zone_value_error(self):
        """
        test_get_secondary_zone_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/secondary_zones/testString')
        mock_response = '{"id": "f97ef698-d5fa-4f91-bc5a-33f17d143b7d", "description": "secondary zone", "zone": "example.com", "enabled": false, "transfer_from": [{"address": "10.0.0.7", "port": 53}], "created_on": "2022-03-16T08:18:25Z", "modified_on": "2022-03-16T08:18:25Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        sz_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "resolver_id": resolver_id,
            "sz_id": sz_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_secondary_zone(**req_copy)


    def test_get_secondary_zone_value_error_with_retries(self):
        # Enable retries and run test_get_secondary_zone_value_error.
        _service.enable_retries()
        self.test_get_secondary_zone_value_error()

        # Disable retries and run test_get_secondary_zone_value_error.
        _service.disable_retries()
        self.test_get_secondary_zone_value_error()

class TestUpdateSecondaryZone():
    """
    Test Class for update_secondary_zone
    """

    @responses.activate
    def test_update_secondary_zone_all_params(self):
        """
        update_secondary_zone()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/secondary_zones/testString')
        mock_response = '{"id": "f97ef698-d5fa-4f91-bc5a-33f17d143b7d", "description": "secondary zone", "zone": "example.com", "enabled": false, "transfer_from": [{"address": "10.0.0.7", "port": 53}], "created_on": "2022-03-16T08:18:25Z", "modified_on": "2022-03-16T08:18:25Z"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a SecondaryZoneSourceInputItem model
        secondary_zone_source_input_item_model = {}
        secondary_zone_source_input_item_model['address'] = '10.0.0.7'

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        sz_id = 'testString'
        description = 'secondary zone'
        enabled = False
        transfer_from = [secondary_zone_source_input_item_model]
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.update_secondary_zone(
            instance_id,
            resolver_id,
            sz_id,
            description=description,
            enabled=enabled,
            transfer_from=transfer_from,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['description'] == 'secondary zone'
        assert req_body['enabled'] == False
        assert req_body['transfer_from'] == [secondary_zone_source_input_item_model]

    def test_update_secondary_zone_all_params_with_retries(self):
        # Enable retries and run test_update_secondary_zone_all_params.
        _service.enable_retries()
        self.test_update_secondary_zone_all_params()

        # Disable retries and run test_update_secondary_zone_all_params.
        _service.disable_retries()
        self.test_update_secondary_zone_all_params()

    @responses.activate
    def test_update_secondary_zone_required_params(self):
        """
        test_update_secondary_zone_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/secondary_zones/testString')
        mock_response = '{"id": "f97ef698-d5fa-4f91-bc5a-33f17d143b7d", "description": "secondary zone", "zone": "example.com", "enabled": false, "transfer_from": [{"address": "10.0.0.7", "port": 53}], "created_on": "2022-03-16T08:18:25Z", "modified_on": "2022-03-16T08:18:25Z"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        sz_id = 'testString'

        # Invoke method
        response = _service.update_secondary_zone(
            instance_id,
            resolver_id,
            sz_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_secondary_zone_required_params_with_retries(self):
        # Enable retries and run test_update_secondary_zone_required_params.
        _service.enable_retries()
        self.test_update_secondary_zone_required_params()

        # Disable retries and run test_update_secondary_zone_required_params.
        _service.disable_retries()
        self.test_update_secondary_zone_required_params()

    @responses.activate
    def test_update_secondary_zone_value_error(self):
        """
        test_update_secondary_zone_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/secondary_zones/testString')
        mock_response = '{"id": "f97ef698-d5fa-4f91-bc5a-33f17d143b7d", "description": "secondary zone", "zone": "example.com", "enabled": false, "transfer_from": [{"address": "10.0.0.7", "port": 53}], "created_on": "2022-03-16T08:18:25Z", "modified_on": "2022-03-16T08:18:25Z"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        sz_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "resolver_id": resolver_id,
            "sz_id": sz_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_secondary_zone(**req_copy)


    def test_update_secondary_zone_value_error_with_retries(self):
        # Enable retries and run test_update_secondary_zone_value_error.
        _service.enable_retries()
        self.test_update_secondary_zone_value_error()

        # Disable retries and run test_update_secondary_zone_value_error.
        _service.disable_retries()
        self.test_update_secondary_zone_value_error()

class TestDeleteSecondaryZone():
    """
    Test Class for delete_secondary_zone
    """

    @responses.activate
    def test_delete_secondary_zone_all_params(self):
        """
        delete_secondary_zone()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/secondary_zones/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        sz_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.delete_secondary_zone(
            instance_id,
            resolver_id,
            sz_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_secondary_zone_all_params_with_retries(self):
        # Enable retries and run test_delete_secondary_zone_all_params.
        _service.enable_retries()
        self.test_delete_secondary_zone_all_params()

        # Disable retries and run test_delete_secondary_zone_all_params.
        _service.disable_retries()
        self.test_delete_secondary_zone_all_params()

    @responses.activate
    def test_delete_secondary_zone_required_params(self):
        """
        test_delete_secondary_zone_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/secondary_zones/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        sz_id = 'testString'

        # Invoke method
        response = _service.delete_secondary_zone(
            instance_id,
            resolver_id,
            sz_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_secondary_zone_required_params_with_retries(self):
        # Enable retries and run test_delete_secondary_zone_required_params.
        _service.enable_retries()
        self.test_delete_secondary_zone_required_params()

        # Disable retries and run test_delete_secondary_zone_required_params.
        _service.disable_retries()
        self.test_delete_secondary_zone_required_params()

    @responses.activate
    def test_delete_secondary_zone_value_error(self):
        """
        test_delete_secondary_zone_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/custom_resolvers/testString/secondary_zones/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        resolver_id = 'testString'
        sz_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "resolver_id": resolver_id,
            "sz_id": sz_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_secondary_zone(**req_copy)


    def test_delete_secondary_zone_value_error_with_retries(self):
        # Enable retries and run test_delete_secondary_zone_value_error.
        _service.enable_retries()
        self.test_delete_secondary_zone_value_error()

        # Disable retries and run test_delete_secondary_zone_value_error.
        _service.disable_retries()
        self.test_delete_secondary_zone_value_error()

# endregion
##############################################################################
# End of Service: SecondaryZones
##############################################################################

##############################################################################
# Start of Service: LinkedZones
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = DnsSvcsV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DnsSvcsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DnsSvcsV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestListLinkedZones():
    """
    Test Class for list_linked_zones
    """

    @responses.activate
    def test_list_linked_zones_all_params(self):
        """
        list_linked_zones()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/linked_dnszones')
        mock_response = '{"linked_dnszones": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "instance_id": "5cbc3c1b-021c-4ad7-b9e4-a5dfefdecf85", "name": "example.com", "description": "linked zone example", "linked_to": {"instance_crn": "crn:v1:staging:public:pdnsdev:global:a/01652b251c3ae2787110a995d8db0135:abe30019-1c08-42dc-9ad9-a0682af70054::", "zone_id": "05855abe-3908-4cdc-bf0d-063e0b1c296d"}, "state": "APPROVAL_PENDING", "label": "dev", "approval_required_before": "2022-03-16T07:23:25Z", "created_on": "2022-03-09T07:23:25Z", "modified_on": "2022-03-09T07:23:25Z"}], "offset": 0, "limit": 200, "count": 1, "total_count": 1, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "last": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "previous": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        x_correlation_id = 'testString'
        offset = 38
        limit = 200

        # Invoke method
        response = _service.list_linked_zones(
            instance_id,
            x_correlation_id=x_correlation_id,
            offset=offset,
            limit=limit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'offset={}'.format(offset) in query_string
        assert 'limit={}'.format(limit) in query_string

    def test_list_linked_zones_all_params_with_retries(self):
        # Enable retries and run test_list_linked_zones_all_params.
        _service.enable_retries()
        self.test_list_linked_zones_all_params()

        # Disable retries and run test_list_linked_zones_all_params.
        _service.disable_retries()
        self.test_list_linked_zones_all_params()

    @responses.activate
    def test_list_linked_zones_required_params(self):
        """
        test_list_linked_zones_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/linked_dnszones')
        mock_response = '{"linked_dnszones": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "instance_id": "5cbc3c1b-021c-4ad7-b9e4-a5dfefdecf85", "name": "example.com", "description": "linked zone example", "linked_to": {"instance_crn": "crn:v1:staging:public:pdnsdev:global:a/01652b251c3ae2787110a995d8db0135:abe30019-1c08-42dc-9ad9-a0682af70054::", "zone_id": "05855abe-3908-4cdc-bf0d-063e0b1c296d"}, "state": "APPROVAL_PENDING", "label": "dev", "approval_required_before": "2022-03-16T07:23:25Z", "created_on": "2022-03-09T07:23:25Z", "modified_on": "2022-03-09T07:23:25Z"}], "offset": 0, "limit": 200, "count": 1, "total_count": 1, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "last": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "previous": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.list_linked_zones(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_linked_zones_required_params_with_retries(self):
        # Enable retries and run test_list_linked_zones_required_params.
        _service.enable_retries()
        self.test_list_linked_zones_required_params()

        # Disable retries and run test_list_linked_zones_required_params.
        _service.disable_retries()
        self.test_list_linked_zones_required_params()

    @responses.activate
    def test_list_linked_zones_value_error(self):
        """
        test_list_linked_zones_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/linked_dnszones')
        mock_response = '{"linked_dnszones": [{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "instance_id": "5cbc3c1b-021c-4ad7-b9e4-a5dfefdecf85", "name": "example.com", "description": "linked zone example", "linked_to": {"instance_crn": "crn:v1:staging:public:pdnsdev:global:a/01652b251c3ae2787110a995d8db0135:abe30019-1c08-42dc-9ad9-a0682af70054::", "zone_id": "05855abe-3908-4cdc-bf0d-063e0b1c296d"}, "state": "APPROVAL_PENDING", "label": "dev", "approval_required_before": "2022-03-16T07:23:25Z", "created_on": "2022-03-09T07:23:25Z", "modified_on": "2022-03-09T07:23:25Z"}], "offset": 0, "limit": 200, "count": 1, "total_count": 1, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "last": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "previous": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_linked_zones(**req_copy)


    def test_list_linked_zones_value_error_with_retries(self):
        # Enable retries and run test_list_linked_zones_value_error.
        _service.enable_retries()
        self.test_list_linked_zones_value_error()

        # Disable retries and run test_list_linked_zones_value_error.
        _service.disable_retries()
        self.test_list_linked_zones_value_error()

class TestCreateLinkedZone():
    """
    Test Class for create_linked_zone
    """

    @responses.activate
    def test_create_linked_zone_all_params(self):
        """
        create_linked_zone()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/linked_dnszones')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "instance_id": "5cbc3c1b-021c-4ad7-b9e4-a5dfefdecf85", "name": "example.com", "description": "linked zone example", "linked_to": {"instance_crn": "crn:v1:staging:public:pdnsdev:global:a/01652b251c3ae2787110a995d8db0135:abe30019-1c08-42dc-9ad9-a0682af70054::", "zone_id": "05855abe-3908-4cdc-bf0d-063e0b1c296d"}, "state": "APPROVAL_PENDING", "label": "dev", "approval_required_before": "2022-03-16T07:23:25Z", "created_on": "2022-03-09T07:23:25Z", "modified_on": "2022-03-09T07:23:25Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        owner_instance_id = 'abe30019-1c08-42dc-9ad9-a0682af70054'
        owner_zone_id = '05855abe-3908-4cdc-bf0d-063e0b1c296d'
        description = 'linked zone example'
        label = 'dev'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.create_linked_zone(
            instance_id,
            owner_instance_id=owner_instance_id,
            owner_zone_id=owner_zone_id,
            description=description,
            label=label,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['owner_instance_id'] == 'abe30019-1c08-42dc-9ad9-a0682af70054'
        assert req_body['owner_zone_id'] == '05855abe-3908-4cdc-bf0d-063e0b1c296d'
        assert req_body['description'] == 'linked zone example'
        assert req_body['label'] == 'dev'

    def test_create_linked_zone_all_params_with_retries(self):
        # Enable retries and run test_create_linked_zone_all_params.
        _service.enable_retries()
        self.test_create_linked_zone_all_params()

        # Disable retries and run test_create_linked_zone_all_params.
        _service.disable_retries()
        self.test_create_linked_zone_all_params()

    @responses.activate
    def test_create_linked_zone_required_params(self):
        """
        test_create_linked_zone_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/linked_dnszones')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "instance_id": "5cbc3c1b-021c-4ad7-b9e4-a5dfefdecf85", "name": "example.com", "description": "linked zone example", "linked_to": {"instance_crn": "crn:v1:staging:public:pdnsdev:global:a/01652b251c3ae2787110a995d8db0135:abe30019-1c08-42dc-9ad9-a0682af70054::", "zone_id": "05855abe-3908-4cdc-bf0d-063e0b1c296d"}, "state": "APPROVAL_PENDING", "label": "dev", "approval_required_before": "2022-03-16T07:23:25Z", "created_on": "2022-03-09T07:23:25Z", "modified_on": "2022-03-09T07:23:25Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.create_linked_zone(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_linked_zone_required_params_with_retries(self):
        # Enable retries and run test_create_linked_zone_required_params.
        _service.enable_retries()
        self.test_create_linked_zone_required_params()

        # Disable retries and run test_create_linked_zone_required_params.
        _service.disable_retries()
        self.test_create_linked_zone_required_params()

    @responses.activate
    def test_create_linked_zone_value_error(self):
        """
        test_create_linked_zone_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/linked_dnszones')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "instance_id": "5cbc3c1b-021c-4ad7-b9e4-a5dfefdecf85", "name": "example.com", "description": "linked zone example", "linked_to": {"instance_crn": "crn:v1:staging:public:pdnsdev:global:a/01652b251c3ae2787110a995d8db0135:abe30019-1c08-42dc-9ad9-a0682af70054::", "zone_id": "05855abe-3908-4cdc-bf0d-063e0b1c296d"}, "state": "APPROVAL_PENDING", "label": "dev", "approval_required_before": "2022-03-16T07:23:25Z", "created_on": "2022-03-09T07:23:25Z", "modified_on": "2022-03-09T07:23:25Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_linked_zone(**req_copy)


    def test_create_linked_zone_value_error_with_retries(self):
        # Enable retries and run test_create_linked_zone_value_error.
        _service.enable_retries()
        self.test_create_linked_zone_value_error()

        # Disable retries and run test_create_linked_zone_value_error.
        _service.disable_retries()
        self.test_create_linked_zone_value_error()

class TestGetLinkedZone():
    """
    Test Class for get_linked_zone
    """

    @responses.activate
    def test_get_linked_zone_all_params(self):
        """
        get_linked_zone()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/linked_dnszones/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "instance_id": "5cbc3c1b-021c-4ad7-b9e4-a5dfefdecf85", "name": "example.com", "description": "linked zone example", "linked_to": {"instance_crn": "crn:v1:staging:public:pdnsdev:global:a/01652b251c3ae2787110a995d8db0135:abe30019-1c08-42dc-9ad9-a0682af70054::", "zone_id": "05855abe-3908-4cdc-bf0d-063e0b1c296d"}, "state": "APPROVAL_PENDING", "label": "dev", "approval_required_before": "2022-03-16T07:23:25Z", "created_on": "2022-03-09T07:23:25Z", "modified_on": "2022-03-09T07:23:25Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        lz_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.get_linked_zone(
            instance_id,
            lz_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_linked_zone_all_params_with_retries(self):
        # Enable retries and run test_get_linked_zone_all_params.
        _service.enable_retries()
        self.test_get_linked_zone_all_params()

        # Disable retries and run test_get_linked_zone_all_params.
        _service.disable_retries()
        self.test_get_linked_zone_all_params()

    @responses.activate
    def test_get_linked_zone_required_params(self):
        """
        test_get_linked_zone_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/linked_dnszones/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "instance_id": "5cbc3c1b-021c-4ad7-b9e4-a5dfefdecf85", "name": "example.com", "description": "linked zone example", "linked_to": {"instance_crn": "crn:v1:staging:public:pdnsdev:global:a/01652b251c3ae2787110a995d8db0135:abe30019-1c08-42dc-9ad9-a0682af70054::", "zone_id": "05855abe-3908-4cdc-bf0d-063e0b1c296d"}, "state": "APPROVAL_PENDING", "label": "dev", "approval_required_before": "2022-03-16T07:23:25Z", "created_on": "2022-03-09T07:23:25Z", "modified_on": "2022-03-09T07:23:25Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        lz_id = 'testString'

        # Invoke method
        response = _service.get_linked_zone(
            instance_id,
            lz_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_linked_zone_required_params_with_retries(self):
        # Enable retries and run test_get_linked_zone_required_params.
        _service.enable_retries()
        self.test_get_linked_zone_required_params()

        # Disable retries and run test_get_linked_zone_required_params.
        _service.disable_retries()
        self.test_get_linked_zone_required_params()

    @responses.activate
    def test_get_linked_zone_value_error(self):
        """
        test_get_linked_zone_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/linked_dnszones/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "instance_id": "5cbc3c1b-021c-4ad7-b9e4-a5dfefdecf85", "name": "example.com", "description": "linked zone example", "linked_to": {"instance_crn": "crn:v1:staging:public:pdnsdev:global:a/01652b251c3ae2787110a995d8db0135:abe30019-1c08-42dc-9ad9-a0682af70054::", "zone_id": "05855abe-3908-4cdc-bf0d-063e0b1c296d"}, "state": "APPROVAL_PENDING", "label": "dev", "approval_required_before": "2022-03-16T07:23:25Z", "created_on": "2022-03-09T07:23:25Z", "modified_on": "2022-03-09T07:23:25Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        lz_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "lz_id": lz_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_linked_zone(**req_copy)


    def test_get_linked_zone_value_error_with_retries(self):
        # Enable retries and run test_get_linked_zone_value_error.
        _service.enable_retries()
        self.test_get_linked_zone_value_error()

        # Disable retries and run test_get_linked_zone_value_error.
        _service.disable_retries()
        self.test_get_linked_zone_value_error()

class TestUpdateLinkedZone():
    """
    Test Class for update_linked_zone
    """

    @responses.activate
    def test_update_linked_zone_all_params(self):
        """
        update_linked_zone()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/linked_dnszones/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "instance_id": "5cbc3c1b-021c-4ad7-b9e4-a5dfefdecf85", "name": "example.com", "description": "linked zone example", "linked_to": {"instance_crn": "crn:v1:staging:public:pdnsdev:global:a/01652b251c3ae2787110a995d8db0135:abe30019-1c08-42dc-9ad9-a0682af70054::", "zone_id": "05855abe-3908-4cdc-bf0d-063e0b1c296d"}, "state": "APPROVAL_PENDING", "label": "dev", "approval_required_before": "2022-03-16T07:23:25Z", "created_on": "2022-03-09T07:23:25Z", "modified_on": "2022-03-09T07:23:25Z"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        lz_id = 'testString'
        description = 'linked zone example'
        label = 'dev'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.update_linked_zone(
            instance_id,
            lz_id,
            description=description,
            label=label,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['description'] == 'linked zone example'
        assert req_body['label'] == 'dev'

    def test_update_linked_zone_all_params_with_retries(self):
        # Enable retries and run test_update_linked_zone_all_params.
        _service.enable_retries()
        self.test_update_linked_zone_all_params()

        # Disable retries and run test_update_linked_zone_all_params.
        _service.disable_retries()
        self.test_update_linked_zone_all_params()

    @responses.activate
    def test_update_linked_zone_required_params(self):
        """
        test_update_linked_zone_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/linked_dnszones/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "instance_id": "5cbc3c1b-021c-4ad7-b9e4-a5dfefdecf85", "name": "example.com", "description": "linked zone example", "linked_to": {"instance_crn": "crn:v1:staging:public:pdnsdev:global:a/01652b251c3ae2787110a995d8db0135:abe30019-1c08-42dc-9ad9-a0682af70054::", "zone_id": "05855abe-3908-4cdc-bf0d-063e0b1c296d"}, "state": "APPROVAL_PENDING", "label": "dev", "approval_required_before": "2022-03-16T07:23:25Z", "created_on": "2022-03-09T07:23:25Z", "modified_on": "2022-03-09T07:23:25Z"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        lz_id = 'testString'

        # Invoke method
        response = _service.update_linked_zone(
            instance_id,
            lz_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_linked_zone_required_params_with_retries(self):
        # Enable retries and run test_update_linked_zone_required_params.
        _service.enable_retries()
        self.test_update_linked_zone_required_params()

        # Disable retries and run test_update_linked_zone_required_params.
        _service.disable_retries()
        self.test_update_linked_zone_required_params()

    @responses.activate
    def test_update_linked_zone_value_error(self):
        """
        test_update_linked_zone_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/linked_dnszones/testString')
        mock_response = '{"id": "5365b73c-ce6f-4d6f-ad9f-d9c131b26370", "instance_id": "5cbc3c1b-021c-4ad7-b9e4-a5dfefdecf85", "name": "example.com", "description": "linked zone example", "linked_to": {"instance_crn": "crn:v1:staging:public:pdnsdev:global:a/01652b251c3ae2787110a995d8db0135:abe30019-1c08-42dc-9ad9-a0682af70054::", "zone_id": "05855abe-3908-4cdc-bf0d-063e0b1c296d"}, "state": "APPROVAL_PENDING", "label": "dev", "approval_required_before": "2022-03-16T07:23:25Z", "created_on": "2022-03-09T07:23:25Z", "modified_on": "2022-03-09T07:23:25Z"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        lz_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "lz_id": lz_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_linked_zone(**req_copy)


    def test_update_linked_zone_value_error_with_retries(self):
        # Enable retries and run test_update_linked_zone_value_error.
        _service.enable_retries()
        self.test_update_linked_zone_value_error()

        # Disable retries and run test_update_linked_zone_value_error.
        _service.disable_retries()
        self.test_update_linked_zone_value_error()

class TestDeleteLinkedZone():
    """
    Test Class for delete_linked_zone
    """

    @responses.activate
    def test_delete_linked_zone_all_params(self):
        """
        delete_linked_zone()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/linked_dnszones/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        lz_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.delete_linked_zone(
            instance_id,
            lz_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_linked_zone_all_params_with_retries(self):
        # Enable retries and run test_delete_linked_zone_all_params.
        _service.enable_retries()
        self.test_delete_linked_zone_all_params()

        # Disable retries and run test_delete_linked_zone_all_params.
        _service.disable_retries()
        self.test_delete_linked_zone_all_params()

    @responses.activate
    def test_delete_linked_zone_required_params(self):
        """
        test_delete_linked_zone_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/linked_dnszones/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        lz_id = 'testString'

        # Invoke method
        response = _service.delete_linked_zone(
            instance_id,
            lz_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_linked_zone_required_params_with_retries(self):
        # Enable retries and run test_delete_linked_zone_required_params.
        _service.enable_retries()
        self.test_delete_linked_zone_required_params()

        # Disable retries and run test_delete_linked_zone_required_params.
        _service.disable_retries()
        self.test_delete_linked_zone_required_params()

    @responses.activate
    def test_delete_linked_zone_value_error(self):
        """
        test_delete_linked_zone_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/linked_dnszones/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        lz_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "lz_id": lz_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_linked_zone(**req_copy)


    def test_delete_linked_zone_value_error_with_retries(self):
        # Enable retries and run test_delete_linked_zone_value_error.
        _service.enable_retries()
        self.test_delete_linked_zone_value_error()

        # Disable retries and run test_delete_linked_zone_value_error.
        _service.disable_retries()
        self.test_delete_linked_zone_value_error()

# endregion
##############################################################################
# End of Service: LinkedZones
##############################################################################

##############################################################################
# Start of Service: AccessRequests
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = DnsSvcsV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DnsSvcsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DnsSvcsV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestListDnszoneAccessRequests():
    """
    Test Class for list_dnszone_access_requests
    """

    @responses.activate
    def test_list_dnszone_access_requests_all_params(self):
        """
        list_dnszone_access_requests()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/access_requests')
        mock_response = '{"access_requests": [{"id": "9a234ede-c2b6-4c39-bc27-d39ec139ecdb", "requestor": {"account": "01652b251c3ae2787110a995d8db0135"}, "zone_id": "05855abe-3908-4cdc-bf0d-063e0b1c296d", "zone_name": "example.com", "state": "PENDING", "expires_at": "2022-03-16T07:23:25Z", "created_on": "2022-03-09T07:23:25Z", "modified_on": "2022-03-09T07:23:25Z"}], "offset": 0, "limit": 200, "count": 1, "total_count": 1, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "last": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "previous": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        x_correlation_id = 'testString'
        offset = 38
        limit = 200

        # Invoke method
        response = _service.list_dnszone_access_requests(
            instance_id,
            dnszone_id,
            x_correlation_id=x_correlation_id,
            offset=offset,
            limit=limit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'offset={}'.format(offset) in query_string
        assert 'limit={}'.format(limit) in query_string

    def test_list_dnszone_access_requests_all_params_with_retries(self):
        # Enable retries and run test_list_dnszone_access_requests_all_params.
        _service.enable_retries()
        self.test_list_dnszone_access_requests_all_params()

        # Disable retries and run test_list_dnszone_access_requests_all_params.
        _service.disable_retries()
        self.test_list_dnszone_access_requests_all_params()

    @responses.activate
    def test_list_dnszone_access_requests_required_params(self):
        """
        test_list_dnszone_access_requests_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/access_requests')
        mock_response = '{"access_requests": [{"id": "9a234ede-c2b6-4c39-bc27-d39ec139ecdb", "requestor": {"account": "01652b251c3ae2787110a995d8db0135"}, "zone_id": "05855abe-3908-4cdc-bf0d-063e0b1c296d", "zone_name": "example.com", "state": "PENDING", "expires_at": "2022-03-16T07:23:25Z", "created_on": "2022-03-09T07:23:25Z", "modified_on": "2022-03-09T07:23:25Z"}], "offset": 0, "limit": 200, "count": 1, "total_count": 1, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "last": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "previous": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Invoke method
        response = _service.list_dnszone_access_requests(
            instance_id,
            dnszone_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_dnszone_access_requests_required_params_with_retries(self):
        # Enable retries and run test_list_dnszone_access_requests_required_params.
        _service.enable_retries()
        self.test_list_dnszone_access_requests_required_params()

        # Disable retries and run test_list_dnszone_access_requests_required_params.
        _service.disable_retries()
        self.test_list_dnszone_access_requests_required_params()

    @responses.activate
    def test_list_dnszone_access_requests_value_error(self):
        """
        test_list_dnszone_access_requests_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/access_requests')
        mock_response = '{"access_requests": [{"id": "9a234ede-c2b6-4c39-bc27-d39ec139ecdb", "requestor": {"account": "01652b251c3ae2787110a995d8db0135"}, "zone_id": "05855abe-3908-4cdc-bf0d-063e0b1c296d", "zone_name": "example.com", "state": "PENDING", "expires_at": "2022-03-16T07:23:25Z", "created_on": "2022-03-09T07:23:25Z", "modified_on": "2022-03-09T07:23:25Z"}], "offset": 0, "limit": 200, "count": 1, "total_count": 1, "first": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "last": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "previous": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}, "next": {"href": "https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_dnszone_access_requests(**req_copy)


    def test_list_dnszone_access_requests_value_error_with_retries(self):
        # Enable retries and run test_list_dnszone_access_requests_value_error.
        _service.enable_retries()
        self.test_list_dnszone_access_requests_value_error()

        # Disable retries and run test_list_dnszone_access_requests_value_error.
        _service.disable_retries()
        self.test_list_dnszone_access_requests_value_error()

class TestGetDnszoneAccessRequest():
    """
    Test Class for get_dnszone_access_request
    """

    @responses.activate
    def test_get_dnszone_access_request_all_params(self):
        """
        get_dnszone_access_request()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/access_requests/testString')
        mock_response = '{"id": "9a234ede-c2b6-4c39-bc27-d39ec139ecdb", "requestor": {"account": "01652b251c3ae2787110a995d8db0135"}, "zone_id": "05855abe-3908-4cdc-bf0d-063e0b1c296d", "zone_name": "example.com", "state": "PENDING", "expires_at": "2022-03-16T07:23:25Z", "created_on": "2022-03-09T07:23:25Z", "modified_on": "2022-03-09T07:23:25Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        request_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.get_dnszone_access_request(
            instance_id,
            dnszone_id,
            request_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_dnszone_access_request_all_params_with_retries(self):
        # Enable retries and run test_get_dnszone_access_request_all_params.
        _service.enable_retries()
        self.test_get_dnszone_access_request_all_params()

        # Disable retries and run test_get_dnszone_access_request_all_params.
        _service.disable_retries()
        self.test_get_dnszone_access_request_all_params()

    @responses.activate
    def test_get_dnszone_access_request_required_params(self):
        """
        test_get_dnszone_access_request_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/access_requests/testString')
        mock_response = '{"id": "9a234ede-c2b6-4c39-bc27-d39ec139ecdb", "requestor": {"account": "01652b251c3ae2787110a995d8db0135"}, "zone_id": "05855abe-3908-4cdc-bf0d-063e0b1c296d", "zone_name": "example.com", "state": "PENDING", "expires_at": "2022-03-16T07:23:25Z", "created_on": "2022-03-09T07:23:25Z", "modified_on": "2022-03-09T07:23:25Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        request_id = 'testString'

        # Invoke method
        response = _service.get_dnszone_access_request(
            instance_id,
            dnszone_id,
            request_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_dnszone_access_request_required_params_with_retries(self):
        # Enable retries and run test_get_dnszone_access_request_required_params.
        _service.enable_retries()
        self.test_get_dnszone_access_request_required_params()

        # Disable retries and run test_get_dnszone_access_request_required_params.
        _service.disable_retries()
        self.test_get_dnszone_access_request_required_params()

    @responses.activate
    def test_get_dnszone_access_request_value_error(self):
        """
        test_get_dnszone_access_request_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/access_requests/testString')
        mock_response = '{"id": "9a234ede-c2b6-4c39-bc27-d39ec139ecdb", "requestor": {"account": "01652b251c3ae2787110a995d8db0135"}, "zone_id": "05855abe-3908-4cdc-bf0d-063e0b1c296d", "zone_name": "example.com", "state": "PENDING", "expires_at": "2022-03-16T07:23:25Z", "created_on": "2022-03-09T07:23:25Z", "modified_on": "2022-03-09T07:23:25Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        request_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
            "request_id": request_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_dnszone_access_request(**req_copy)


    def test_get_dnszone_access_request_value_error_with_retries(self):
        # Enable retries and run test_get_dnszone_access_request_value_error.
        _service.enable_retries()
        self.test_get_dnszone_access_request_value_error()

        # Disable retries and run test_get_dnszone_access_request_value_error.
        _service.disable_retries()
        self.test_get_dnszone_access_request_value_error()

class TestUpdateDnszoneAccessRequest():
    """
    Test Class for update_dnszone_access_request
    """

    @responses.activate
    def test_update_dnszone_access_request_all_params(self):
        """
        update_dnszone_access_request()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/access_requests/testString')
        mock_response = '{"id": "9a234ede-c2b6-4c39-bc27-d39ec139ecdb", "requestor": {"account": "01652b251c3ae2787110a995d8db0135"}, "zone_id": "05855abe-3908-4cdc-bf0d-063e0b1c296d", "zone_name": "example.com", "state": "PENDING", "expires_at": "2022-03-16T07:23:25Z", "created_on": "2022-03-09T07:23:25Z", "modified_on": "2022-03-09T07:23:25Z"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        request_id = 'testString'
        action = 'APPROVE'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.update_dnszone_access_request(
            instance_id,
            dnszone_id,
            request_id,
            action=action,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['action'] == 'APPROVE'

    def test_update_dnszone_access_request_all_params_with_retries(self):
        # Enable retries and run test_update_dnszone_access_request_all_params.
        _service.enable_retries()
        self.test_update_dnszone_access_request_all_params()

        # Disable retries and run test_update_dnszone_access_request_all_params.
        _service.disable_retries()
        self.test_update_dnszone_access_request_all_params()

    @responses.activate
    def test_update_dnszone_access_request_required_params(self):
        """
        test_update_dnszone_access_request_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/access_requests/testString')
        mock_response = '{"id": "9a234ede-c2b6-4c39-bc27-d39ec139ecdb", "requestor": {"account": "01652b251c3ae2787110a995d8db0135"}, "zone_id": "05855abe-3908-4cdc-bf0d-063e0b1c296d", "zone_name": "example.com", "state": "PENDING", "expires_at": "2022-03-16T07:23:25Z", "created_on": "2022-03-09T07:23:25Z", "modified_on": "2022-03-09T07:23:25Z"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        request_id = 'testString'

        # Invoke method
        response = _service.update_dnszone_access_request(
            instance_id,
            dnszone_id,
            request_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_dnszone_access_request_required_params_with_retries(self):
        # Enable retries and run test_update_dnszone_access_request_required_params.
        _service.enable_retries()
        self.test_update_dnszone_access_request_required_params()

        # Disable retries and run test_update_dnszone_access_request_required_params.
        _service.disable_retries()
        self.test_update_dnszone_access_request_required_params()

    @responses.activate
    def test_update_dnszone_access_request_value_error(self):
        """
        test_update_dnszone_access_request_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/dnszones/testString/access_requests/testString')
        mock_response = '{"id": "9a234ede-c2b6-4c39-bc27-d39ec139ecdb", "requestor": {"account": "01652b251c3ae2787110a995d8db0135"}, "zone_id": "05855abe-3908-4cdc-bf0d-063e0b1c296d", "zone_name": "example.com", "state": "PENDING", "expires_at": "2022-03-16T07:23:25Z", "created_on": "2022-03-09T07:23:25Z", "modified_on": "2022-03-09T07:23:25Z"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        dnszone_id = 'testString'
        request_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "dnszone_id": dnszone_id,
            "request_id": request_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_dnszone_access_request(**req_copy)


    def test_update_dnszone_access_request_value_error_with_retries(self):
        # Enable retries and run test_update_dnszone_access_request_value_error.
        _service.enable_retries()
        self.test_update_dnszone_access_request_value_error()

        # Disable retries and run test_update_dnszone_access_request_value_error.
        _service.disable_retries()
        self.test_update_dnszone_access_request_value_error()

# endregion
##############################################################################
# End of Service: AccessRequests
##############################################################################

##############################################################################
# Start of Service: PermittedNetworkForLinkedZone
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = DnsSvcsV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DnsSvcsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DnsSvcsV1.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestListLinkedPermittedNetworks():
    """
    Test Class for list_linked_permitted_networks
    """

    @responses.activate
    def test_list_linked_permitted_networks_all_params(self):
        """
        list_linked_permitted_networks()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/linked_dnszones/testString/permitted_networks')
        mock_response = '{"permitted_networks": [{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        lz_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.list_linked_permitted_networks(
            instance_id,
            lz_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_linked_permitted_networks_all_params_with_retries(self):
        # Enable retries and run test_list_linked_permitted_networks_all_params.
        _service.enable_retries()
        self.test_list_linked_permitted_networks_all_params()

        # Disable retries and run test_list_linked_permitted_networks_all_params.
        _service.disable_retries()
        self.test_list_linked_permitted_networks_all_params()

    @responses.activate
    def test_list_linked_permitted_networks_required_params(self):
        """
        test_list_linked_permitted_networks_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/linked_dnszones/testString/permitted_networks')
        mock_response = '{"permitted_networks": [{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        lz_id = 'testString'

        # Invoke method
        response = _service.list_linked_permitted_networks(
            instance_id,
            lz_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_linked_permitted_networks_required_params_with_retries(self):
        # Enable retries and run test_list_linked_permitted_networks_required_params.
        _service.enable_retries()
        self.test_list_linked_permitted_networks_required_params()

        # Disable retries and run test_list_linked_permitted_networks_required_params.
        _service.disable_retries()
        self.test_list_linked_permitted_networks_required_params()

    @responses.activate
    def test_list_linked_permitted_networks_value_error(self):
        """
        test_list_linked_permitted_networks_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/linked_dnszones/testString/permitted_networks')
        mock_response = '{"permitted_networks": [{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        lz_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "lz_id": lz_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_linked_permitted_networks(**req_copy)


    def test_list_linked_permitted_networks_value_error_with_retries(self):
        # Enable retries and run test_list_linked_permitted_networks_value_error.
        _service.enable_retries()
        self.test_list_linked_permitted_networks_value_error()

        # Disable retries and run test_list_linked_permitted_networks_value_error.
        _service.disable_retries()
        self.test_list_linked_permitted_networks_value_error()

class TestCreateLzPermittedNetwork():
    """
    Test Class for create_lz_permitted_network
    """

    @responses.activate
    def test_create_lz_permitted_network_all_params(self):
        """
        create_lz_permitted_network()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/linked_dnszones/testString/permitted_networks')
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a PermittedNetworkVpc model
        permitted_network_vpc_model = {}
        permitted_network_vpc_model['vpc_crn'] = 'crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6'

        # Set up parameter values
        instance_id = 'testString'
        lz_id = 'testString'
        type = 'vpc'
        permitted_network = permitted_network_vpc_model
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.create_lz_permitted_network(
            instance_id,
            lz_id,
            type=type,
            permitted_network=permitted_network,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'vpc'
        assert req_body['permitted_network'] == permitted_network_vpc_model

    def test_create_lz_permitted_network_all_params_with_retries(self):
        # Enable retries and run test_create_lz_permitted_network_all_params.
        _service.enable_retries()
        self.test_create_lz_permitted_network_all_params()

        # Disable retries and run test_create_lz_permitted_network_all_params.
        _service.disable_retries()
        self.test_create_lz_permitted_network_all_params()

    @responses.activate
    def test_create_lz_permitted_network_required_params(self):
        """
        test_create_lz_permitted_network_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/linked_dnszones/testString/permitted_networks')
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        lz_id = 'testString'

        # Invoke method
        response = _service.create_lz_permitted_network(
            instance_id,
            lz_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_lz_permitted_network_required_params_with_retries(self):
        # Enable retries and run test_create_lz_permitted_network_required_params.
        _service.enable_retries()
        self.test_create_lz_permitted_network_required_params()

        # Disable retries and run test_create_lz_permitted_network_required_params.
        _service.disable_retries()
        self.test_create_lz_permitted_network_required_params()

    @responses.activate
    def test_create_lz_permitted_network_value_error(self):
        """
        test_create_lz_permitted_network_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/linked_dnszones/testString/permitted_networks')
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        lz_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "lz_id": lz_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_lz_permitted_network(**req_copy)


    def test_create_lz_permitted_network_value_error_with_retries(self):
        # Enable retries and run test_create_lz_permitted_network_value_error.
        _service.enable_retries()
        self.test_create_lz_permitted_network_value_error()

        # Disable retries and run test_create_lz_permitted_network_value_error.
        _service.disable_retries()
        self.test_create_lz_permitted_network_value_error()

class TestDeleteLzPermittedNetwork():
    """
    Test Class for delete_lz_permitted_network
    """

    @responses.activate
    def test_delete_lz_permitted_network_all_params(self):
        """
        delete_lz_permitted_network()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/linked_dnszones/testString/permitted_networks/testString')
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        instance_id = 'testString'
        lz_id = 'testString'
        permitted_network_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.delete_lz_permitted_network(
            instance_id,
            lz_id,
            permitted_network_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_lz_permitted_network_all_params_with_retries(self):
        # Enable retries and run test_delete_lz_permitted_network_all_params.
        _service.enable_retries()
        self.test_delete_lz_permitted_network_all_params()

        # Disable retries and run test_delete_lz_permitted_network_all_params.
        _service.disable_retries()
        self.test_delete_lz_permitted_network_all_params()

    @responses.activate
    def test_delete_lz_permitted_network_required_params(self):
        """
        test_delete_lz_permitted_network_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/linked_dnszones/testString/permitted_networks/testString')
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        instance_id = 'testString'
        lz_id = 'testString'
        permitted_network_id = 'testString'

        # Invoke method
        response = _service.delete_lz_permitted_network(
            instance_id,
            lz_id,
            permitted_network_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_lz_permitted_network_required_params_with_retries(self):
        # Enable retries and run test_delete_lz_permitted_network_required_params.
        _service.enable_retries()
        self.test_delete_lz_permitted_network_required_params()

        # Disable retries and run test_delete_lz_permitted_network_required_params.
        _service.disable_retries()
        self.test_delete_lz_permitted_network_required_params()

    @responses.activate
    def test_delete_lz_permitted_network_value_error(self):
        """
        test_delete_lz_permitted_network_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/linked_dnszones/testString/permitted_networks/testString')
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        instance_id = 'testString'
        lz_id = 'testString'
        permitted_network_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "lz_id": lz_id,
            "permitted_network_id": permitted_network_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_lz_permitted_network(**req_copy)


    def test_delete_lz_permitted_network_value_error_with_retries(self):
        # Enable retries and run test_delete_lz_permitted_network_value_error.
        _service.enable_retries()
        self.test_delete_lz_permitted_network_value_error()

        # Disable retries and run test_delete_lz_permitted_network_value_error.
        _service.disable_retries()
        self.test_delete_lz_permitted_network_value_error()

class TestGetLinkedPermittedNetwork():
    """
    Test Class for get_linked_permitted_network
    """

    @responses.activate
    def test_get_linked_permitted_network_all_params(self):
        """
        get_linked_permitted_network()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/linked_dnszones/testString/permitted_networks/testString')
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        lz_id = 'testString'
        permitted_network_id = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.get_linked_permitted_network(
            instance_id,
            lz_id,
            permitted_network_id,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_linked_permitted_network_all_params_with_retries(self):
        # Enable retries and run test_get_linked_permitted_network_all_params.
        _service.enable_retries()
        self.test_get_linked_permitted_network_all_params()

        # Disable retries and run test_get_linked_permitted_network_all_params.
        _service.disable_retries()
        self.test_get_linked_permitted_network_all_params()

    @responses.activate
    def test_get_linked_permitted_network_required_params(self):
        """
        test_get_linked_permitted_network_required_params()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/linked_dnszones/testString/permitted_networks/testString')
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        lz_id = 'testString'
        permitted_network_id = 'testString'

        # Invoke method
        response = _service.get_linked_permitted_network(
            instance_id,
            lz_id,
            permitted_network_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_linked_permitted_network_required_params_with_retries(self):
        # Enable retries and run test_get_linked_permitted_network_required_params.
        _service.enable_retries()
        self.test_get_linked_permitted_network_required_params()

        # Disable retries and run test_get_linked_permitted_network_required_params.
        _service.disable_retries()
        self.test_get_linked_permitted_network_required_params()

    @responses.activate
    def test_get_linked_permitted_network_value_error(self):
        """
        test_get_linked_permitted_network_value_error()
        """
        # Set up mock
        url = preprocess_url('/instances/testString/linked_dnszones/testString/permitted_networks/testString')
        mock_response = '{"id": "fecd0173-3919-456b-b202-3029dfa1b0f7", "created_on": "2019-01-01T05:20:00.12345Z", "modified_on": "2019-01-01T05:20:00.12345Z", "permitted_network": {"vpc_crn": "crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6"}, "type": "vpc", "state": "ACTIVE"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        lz_id = 'testString'
        permitted_network_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "lz_id": lz_id,
            "permitted_network_id": permitted_network_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_linked_permitted_network(**req_copy)


    def test_get_linked_permitted_network_value_error_with_retries(self):
        # Enable retries and run test_get_linked_permitted_network_value_error.
        _service.enable_retries()
        self.test_get_linked_permitted_network_value_error()

        # Disable retries and run test_get_linked_permitted_network_value_error.
        _service.disable_retries()
        self.test_get_linked_permitted_network_value_error()

# endregion
##############################################################################
# End of Service: PermittedNetworkForLinkedZone
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_AccessRequestRequestor():
    """
    Test Class for AccessRequestRequestor
    """

    def test_access_request_requestor_serialization(self):
        """
        Test serialization/deserialization for AccessRequestRequestor
        """

        # Construct a json representation of a AccessRequestRequestor model
        access_request_requestor_model_json = {}
        access_request_requestor_model_json['account'] = '01652b251c3ae2787110a995d8db0135'

        # Construct a model instance of AccessRequestRequestor by calling from_dict on the json representation
        access_request_requestor_model = AccessRequestRequestor.from_dict(access_request_requestor_model_json)
        assert access_request_requestor_model != False

        # Construct a model instance of AccessRequestRequestor by calling from_dict on the json representation
        access_request_requestor_model_dict = AccessRequestRequestor.from_dict(access_request_requestor_model_json).__dict__
        access_request_requestor_model2 = AccessRequestRequestor(**access_request_requestor_model_dict)

        # Verify the model instances are equivalent
        assert access_request_requestor_model == access_request_requestor_model2

        # Convert model instance back to dict and verify no loss of data
        access_request_requestor_model_json2 = access_request_requestor_model.to_dict()
        assert access_request_requestor_model_json2 == access_request_requestor_model_json

class TestModel_LinkedZoneLinkedTo():
    """
    Test Class for LinkedZoneLinkedTo
    """

    def test_linked_zone_linked_to_serialization(self):
        """
        Test serialization/deserialization for LinkedZoneLinkedTo
        """

        # Construct a json representation of a LinkedZoneLinkedTo model
        linked_zone_linked_to_model_json = {}
        linked_zone_linked_to_model_json['instance_crn'] = 'crn:v1:staging:public:pdnsdev:global:a/01652b251c3ae2787110a995d8db0135:abe30019-1c08-42dc-9ad9-a0682af70054::'
        linked_zone_linked_to_model_json['zone_id'] = '05855abe-3908-4cdc-bf0d-063e0b1c296d'

        # Construct a model instance of LinkedZoneLinkedTo by calling from_dict on the json representation
        linked_zone_linked_to_model = LinkedZoneLinkedTo.from_dict(linked_zone_linked_to_model_json)
        assert linked_zone_linked_to_model != False

        # Construct a model instance of LinkedZoneLinkedTo by calling from_dict on the json representation
        linked_zone_linked_to_model_dict = LinkedZoneLinkedTo.from_dict(linked_zone_linked_to_model_json).__dict__
        linked_zone_linked_to_model2 = LinkedZoneLinkedTo(**linked_zone_linked_to_model_dict)

        # Verify the model instances are equivalent
        assert linked_zone_linked_to_model == linked_zone_linked_to_model2

        # Convert model instance back to dict and verify no loss of data
        linked_zone_linked_to_model_json2 = linked_zone_linked_to_model.to_dict()
        assert linked_zone_linked_to_model_json2 == linked_zone_linked_to_model_json

class TestModel_LoadBalancerAzPoolsItem():
    """
    Test Class for LoadBalancerAzPoolsItem
    """

    def test_load_balancer_az_pools_item_serialization(self):
        """
        Test serialization/deserialization for LoadBalancerAzPoolsItem
        """

        # Construct a json representation of a LoadBalancerAzPoolsItem model
        load_balancer_az_pools_item_model_json = {}
        load_balancer_az_pools_item_model_json['availability_zone'] = 'us-south-1'
        load_balancer_az_pools_item_model_json['pools'] = ['0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d']

        # Construct a model instance of LoadBalancerAzPoolsItem by calling from_dict on the json representation
        load_balancer_az_pools_item_model = LoadBalancerAzPoolsItem.from_dict(load_balancer_az_pools_item_model_json)
        assert load_balancer_az_pools_item_model != False

        # Construct a model instance of LoadBalancerAzPoolsItem by calling from_dict on the json representation
        load_balancer_az_pools_item_model_dict = LoadBalancerAzPoolsItem.from_dict(load_balancer_az_pools_item_model_json).__dict__
        load_balancer_az_pools_item_model2 = LoadBalancerAzPoolsItem(**load_balancer_az_pools_item_model_dict)

        # Verify the model instances are equivalent
        assert load_balancer_az_pools_item_model == load_balancer_az_pools_item_model2

        # Convert model instance back to dict and verify no loss of data
        load_balancer_az_pools_item_model_json2 = load_balancer_az_pools_item_model.to_dict()
        assert load_balancer_az_pools_item_model_json2 == load_balancer_az_pools_item_model_json

class TestModel_PoolHealthcheckVsisItem():
    """
    Test Class for PoolHealthcheckVsisItem
    """

    def test_pool_healthcheck_vsis_item_serialization(self):
        """
        Test serialization/deserialization for PoolHealthcheckVsisItem
        """

        # Construct a json representation of a PoolHealthcheckVsisItem model
        pool_healthcheck_vsis_item_model_json = {}
        pool_healthcheck_vsis_item_model_json['subnet'] = 'crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04'
        pool_healthcheck_vsis_item_model_json['ipv4_address'] = '10.10.16.8'
        pool_healthcheck_vsis_item_model_json['ipv4_cidr_block'] = '10.10.16.0/24'
        pool_healthcheck_vsis_item_model_json['vpc'] = 'crn:v1:staging:public:is:us-south:a/01652b251c3ae2787110a995d8db0135::vpc:r134-8c426a0a-ec74-4c97-9c02-f6194c224d8a'

        # Construct a model instance of PoolHealthcheckVsisItem by calling from_dict on the json representation
        pool_healthcheck_vsis_item_model = PoolHealthcheckVsisItem.from_dict(pool_healthcheck_vsis_item_model_json)
        assert pool_healthcheck_vsis_item_model != False

        # Construct a model instance of PoolHealthcheckVsisItem by calling from_dict on the json representation
        pool_healthcheck_vsis_item_model_dict = PoolHealthcheckVsisItem.from_dict(pool_healthcheck_vsis_item_model_json).__dict__
        pool_healthcheck_vsis_item_model2 = PoolHealthcheckVsisItem(**pool_healthcheck_vsis_item_model_dict)

        # Verify the model instances are equivalent
        assert pool_healthcheck_vsis_item_model == pool_healthcheck_vsis_item_model2

        # Convert model instance back to dict and verify no loss of data
        pool_healthcheck_vsis_item_model_json2 = pool_healthcheck_vsis_item_model.to_dict()
        assert pool_healthcheck_vsis_item_model_json2 == pool_healthcheck_vsis_item_model_json

class TestModel_RecordsImportErrorModelError():
    """
    Test Class for RecordsImportErrorModelError
    """

    def test_records_import_error_model_error_serialization(self):
        """
        Test serialization/deserialization for RecordsImportErrorModelError
        """

        # Construct a json representation of a RecordsImportErrorModelError model
        records_import_error_model_error_model_json = {}
        records_import_error_model_error_model_json['code'] = 'internal_server_error'
        records_import_error_model_error_model_json['message'] = 'An internal error occurred. Try again later.'

        # Construct a model instance of RecordsImportErrorModelError by calling from_dict on the json representation
        records_import_error_model_error_model = RecordsImportErrorModelError.from_dict(records_import_error_model_error_model_json)
        assert records_import_error_model_error_model != False

        # Construct a model instance of RecordsImportErrorModelError by calling from_dict on the json representation
        records_import_error_model_error_model_dict = RecordsImportErrorModelError.from_dict(records_import_error_model_error_model_json).__dict__
        records_import_error_model_error_model2 = RecordsImportErrorModelError(**records_import_error_model_error_model_dict)

        # Verify the model instances are equivalent
        assert records_import_error_model_error_model == records_import_error_model_error_model2

        # Convert model instance back to dict and verify no loss of data
        records_import_error_model_error_model_json2 = records_import_error_model_error_model.to_dict()
        assert records_import_error_model_error_model_json2 == records_import_error_model_error_model_json

class TestModel_SecondaryZoneSourceInputItem():
    """
    Test Class for SecondaryZoneSourceInputItem
    """

    def test_secondary_zone_source_input_item_serialization(self):
        """
        Test serialization/deserialization for SecondaryZoneSourceInputItem
        """

        # Construct a json representation of a SecondaryZoneSourceInputItem model
        secondary_zone_source_input_item_model_json = {}
        secondary_zone_source_input_item_model_json['address'] = '10.0.0.7'

        # Construct a model instance of SecondaryZoneSourceInputItem by calling from_dict on the json representation
        secondary_zone_source_input_item_model = SecondaryZoneSourceInputItem.from_dict(secondary_zone_source_input_item_model_json)
        assert secondary_zone_source_input_item_model != False

        # Construct a model instance of SecondaryZoneSourceInputItem by calling from_dict on the json representation
        secondary_zone_source_input_item_model_dict = SecondaryZoneSourceInputItem.from_dict(secondary_zone_source_input_item_model_json).__dict__
        secondary_zone_source_input_item_model2 = SecondaryZoneSourceInputItem(**secondary_zone_source_input_item_model_dict)

        # Verify the model instances are equivalent
        assert secondary_zone_source_input_item_model == secondary_zone_source_input_item_model2

        # Convert model instance back to dict and verify no loss of data
        secondary_zone_source_input_item_model_json2 = secondary_zone_source_input_item_model.to_dict()
        assert secondary_zone_source_input_item_model_json2 == secondary_zone_source_input_item_model_json

class TestModel_SecondaryZoneTransferFromItem():
    """
    Test Class for SecondaryZoneTransferFromItem
    """

    def test_secondary_zone_transfer_from_item_serialization(self):
        """
        Test serialization/deserialization for SecondaryZoneTransferFromItem
        """

        # Construct a json representation of a SecondaryZoneTransferFromItem model
        secondary_zone_transfer_from_item_model_json = {}
        secondary_zone_transfer_from_item_model_json['address'] = '10.0.0.7'
        secondary_zone_transfer_from_item_model_json['port'] = 53

        # Construct a model instance of SecondaryZoneTransferFromItem by calling from_dict on the json representation
        secondary_zone_transfer_from_item_model = SecondaryZoneTransferFromItem.from_dict(secondary_zone_transfer_from_item_model_json)
        assert secondary_zone_transfer_from_item_model != False

        # Construct a model instance of SecondaryZoneTransferFromItem by calling from_dict on the json representation
        secondary_zone_transfer_from_item_model_dict = SecondaryZoneTransferFromItem.from_dict(secondary_zone_transfer_from_item_model_json).__dict__
        secondary_zone_transfer_from_item_model2 = SecondaryZoneTransferFromItem(**secondary_zone_transfer_from_item_model_dict)

        # Verify the model instances are equivalent
        assert secondary_zone_transfer_from_item_model == secondary_zone_transfer_from_item_model2

        # Convert model instance back to dict and verify no loss of data
        secondary_zone_transfer_from_item_model_json2 = secondary_zone_transfer_from_item_model.to_dict()
        assert secondary_zone_transfer_from_item_model_json2 == secondary_zone_transfer_from_item_model_json

class TestModel_AccessRequest():
    """
    Test Class for AccessRequest
    """

    def test_access_request_serialization(self):
        """
        Test serialization/deserialization for AccessRequest
        """

        # Construct dict forms of any model objects needed in order to build this model.

        access_request_requestor_model = {} # AccessRequestRequestor
        access_request_requestor_model['account'] = '01652b251c3ae2787110a995d8db0135'

        # Construct a json representation of a AccessRequest model
        access_request_model_json = {}
        access_request_model_json['id'] = '9a234ede-c2b6-4c39-bc27-d39ec139ecdb'
        access_request_model_json['requestor'] = access_request_requestor_model
        access_request_model_json['zone_id'] = '05855abe-3908-4cdc-bf0d-063e0b1c296d'
        access_request_model_json['zone_name'] = 'example.com'
        access_request_model_json['state'] = 'PENDING'
        access_request_model_json['expires_at'] = '2022-03-16T07:23:25Z'
        access_request_model_json['created_on'] = '2022-03-09T07:23:25Z'
        access_request_model_json['modified_on'] = '2022-03-09T07:23:25Z'

        # Construct a model instance of AccessRequest by calling from_dict on the json representation
        access_request_model = AccessRequest.from_dict(access_request_model_json)
        assert access_request_model != False

        # Construct a model instance of AccessRequest by calling from_dict on the json representation
        access_request_model_dict = AccessRequest.from_dict(access_request_model_json).__dict__
        access_request_model2 = AccessRequest(**access_request_model_dict)

        # Verify the model instances are equivalent
        assert access_request_model == access_request_model2

        # Convert model instance back to dict and verify no loss of data
        access_request_model_json2 = access_request_model.to_dict()
        assert access_request_model_json2 == access_request_model_json

class TestModel_AccessRequestsList():
    """
    Test Class for AccessRequestsList
    """

    def test_access_requests_list_serialization(self):
        """
        Test serialization/deserialization for AccessRequestsList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        access_request_requestor_model = {} # AccessRequestRequestor
        access_request_requestor_model['account'] = '01652b251c3ae2787110a995d8db0135'

        access_request_model = {} # AccessRequest
        access_request_model['id'] = '9a234ede-c2b6-4c39-bc27-d39ec139ecdb'
        access_request_model['requestor'] = access_request_requestor_model
        access_request_model['zone_id'] = '05855abe-3908-4cdc-bf0d-063e0b1c296d'
        access_request_model['zone_name'] = 'example.com'
        access_request_model['state'] = 'PENDING'
        access_request_model['expires_at'] = '2022-03-16T07:23:25Z'
        access_request_model['created_on'] = '2022-03-09T07:23:25Z'
        access_request_model['modified_on'] = '2022-03-09T07:23:25Z'

        pagination_ref_model = {} # PaginationRef
        pagination_ref_model['href'] = 'https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200'

        # Construct a json representation of a AccessRequestsList model
        access_requests_list_model_json = {}
        access_requests_list_model_json['access_requests'] = [access_request_model]
        access_requests_list_model_json['offset'] = 0
        access_requests_list_model_json['limit'] = 200
        access_requests_list_model_json['count'] = 1
        access_requests_list_model_json['total_count'] = 1
        access_requests_list_model_json['first'] = pagination_ref_model
        access_requests_list_model_json['last'] = pagination_ref_model
        access_requests_list_model_json['previous'] = pagination_ref_model
        access_requests_list_model_json['next'] = pagination_ref_model

        # Construct a model instance of AccessRequestsList by calling from_dict on the json representation
        access_requests_list_model = AccessRequestsList.from_dict(access_requests_list_model_json)
        assert access_requests_list_model != False

        # Construct a model instance of AccessRequestsList by calling from_dict on the json representation
        access_requests_list_model_dict = AccessRequestsList.from_dict(access_requests_list_model_json).__dict__
        access_requests_list_model2 = AccessRequestsList(**access_requests_list_model_dict)

        # Verify the model instances are equivalent
        assert access_requests_list_model == access_requests_list_model2

        # Convert model instance back to dict and verify no loss of data
        access_requests_list_model_json2 = access_requests_list_model.to_dict()
        assert access_requests_list_model_json2 == access_requests_list_model_json

class TestModel_CustomResolver():
    """
    Test Class for CustomResolver
    """

    def test_custom_resolver_serialization(self):
        """
        Test serialization/deserialization for CustomResolver
        """

        # Construct dict forms of any model objects needed in order to build this model.

        location_model = {} # Location
        location_model['id'] = '9a234ede-c2b6-4c39-bc27-d39ec139ecdb'
        location_model['subnet_crn'] = 'crn:v1:bluemix:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04'
        location_model['enabled'] = True
        location_model['healthy'] = True
        location_model['dns_server_ip'] = '10.10.16.8'

        # Construct a json representation of a CustomResolver model
        custom_resolver_model_json = {}
        custom_resolver_model_json['id'] = '5365b73c-ce6f-4d6f-ad9f-d9c131b26370'
        custom_resolver_model_json['name'] = 'my-resolver'
        custom_resolver_model_json['description'] = 'custom resolver'
        custom_resolver_model_json['enabled'] = False
        custom_resolver_model_json['health'] = 'HEALTHY'
        custom_resolver_model_json['locations'] = [location_model]
        custom_resolver_model_json['created_on'] = '2021-04-21T08:18:25Z'
        custom_resolver_model_json['modified_on'] = '2021-04-21T08:18:25Z'

        # Construct a model instance of CustomResolver by calling from_dict on the json representation
        custom_resolver_model = CustomResolver.from_dict(custom_resolver_model_json)
        assert custom_resolver_model != False

        # Construct a model instance of CustomResolver by calling from_dict on the json representation
        custom_resolver_model_dict = CustomResolver.from_dict(custom_resolver_model_json).__dict__
        custom_resolver_model2 = CustomResolver(**custom_resolver_model_dict)

        # Verify the model instances are equivalent
        assert custom_resolver_model == custom_resolver_model2

        # Convert model instance back to dict and verify no loss of data
        custom_resolver_model_json2 = custom_resolver_model.to_dict()
        assert custom_resolver_model_json2 == custom_resolver_model_json

class TestModel_CustomResolverList():
    """
    Test Class for CustomResolverList
    """

    def test_custom_resolver_list_serialization(self):
        """
        Test serialization/deserialization for CustomResolverList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        location_model = {} # Location
        location_model['id'] = '9a234ede-c2b6-4c39-bc27-d39ec139ecdb'
        location_model['subnet_crn'] = 'crn:v1:bluemix:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04'
        location_model['enabled'] = True
        location_model['healthy'] = True
        location_model['dns_server_ip'] = '10.10.16.8'

        custom_resolver_model = {} # CustomResolver
        custom_resolver_model['id'] = '5365b73c-ce6f-4d6f-ad9f-d9c131b26370'
        custom_resolver_model['name'] = 'my-resolver'
        custom_resolver_model['description'] = 'custom resolver'
        custom_resolver_model['enabled'] = False
        custom_resolver_model['health'] = 'HEALTHY'
        custom_resolver_model['locations'] = [location_model]
        custom_resolver_model['created_on'] = '2021-04-21T08:18:25Z'
        custom_resolver_model['modified_on'] = '2021-04-21T08:18:25Z'

        # Construct a json representation of a CustomResolverList model
        custom_resolver_list_model_json = {}
        custom_resolver_list_model_json['custom_resolvers'] = [custom_resolver_model]

        # Construct a model instance of CustomResolverList by calling from_dict on the json representation
        custom_resolver_list_model = CustomResolverList.from_dict(custom_resolver_list_model_json)
        assert custom_resolver_list_model != False

        # Construct a model instance of CustomResolverList by calling from_dict on the json representation
        custom_resolver_list_model_dict = CustomResolverList.from_dict(custom_resolver_list_model_json).__dict__
        custom_resolver_list_model2 = CustomResolverList(**custom_resolver_list_model_dict)

        # Verify the model instances are equivalent
        assert custom_resolver_list_model == custom_resolver_list_model2

        # Convert model instance back to dict and verify no loss of data
        custom_resolver_list_model_json2 = custom_resolver_list_model.to_dict()
        assert custom_resolver_list_model_json2 == custom_resolver_list_model_json

class TestModel_Dnszone():
    """
    Test Class for Dnszone
    """

    def test_dnszone_serialization(self):
        """
        Test serialization/deserialization for Dnszone
        """

        # Construct a json representation of a Dnszone model
        dnszone_model_json = {}
        dnszone_model_json['id'] = '2d0f862b-67cc-41f3-b6a2-59860d0aa90e'
        dnszone_model_json['created_on'] = '2019-01-01T05:20:00.12345Z'
        dnszone_model_json['modified_on'] = '2019-01-01T05:20:00.12345Z'
        dnszone_model_json['instance_id'] = '1407a753-a93f-4bb0-9784-bcfc269ee1b3'
        dnszone_model_json['name'] = 'example.com'
        dnszone_model_json['description'] = 'The DNS zone is used for VPCs in us-east region'
        dnszone_model_json['state'] = 'pending_network_add'
        dnszone_model_json['label'] = 'us-east'

        # Construct a model instance of Dnszone by calling from_dict on the json representation
        dnszone_model = Dnszone.from_dict(dnszone_model_json)
        assert dnszone_model != False

        # Construct a model instance of Dnszone by calling from_dict on the json representation
        dnszone_model_dict = Dnszone.from_dict(dnszone_model_json).__dict__
        dnszone_model2 = Dnszone(**dnszone_model_dict)

        # Verify the model instances are equivalent
        assert dnszone_model == dnszone_model2

        # Convert model instance back to dict and verify no loss of data
        dnszone_model_json2 = dnszone_model.to_dict()
        assert dnszone_model_json2 == dnszone_model_json

class TestModel_ForwardingRule():
    """
    Test Class for ForwardingRule
    """

    def test_forwarding_rule_serialization(self):
        """
        Test serialization/deserialization for ForwardingRule
        """

        # Construct a json representation of a ForwardingRule model
        forwarding_rule_model_json = {}
        forwarding_rule_model_json['id'] = '5365b73c-ce6f-4d6f-ad9f-d9c131b26370'
        forwarding_rule_model_json['description'] = 'forwarding rule'
        forwarding_rule_model_json['type'] = 'zone'
        forwarding_rule_model_json['match'] = 'example.com'
        forwarding_rule_model_json['forward_to'] = ['161.26.0.7']
        forwarding_rule_model_json['created_on'] = '2021-04-21T08:18:25Z'
        forwarding_rule_model_json['modified_on'] = '2021-04-21T08:18:25Z'

        # Construct a model instance of ForwardingRule by calling from_dict on the json representation
        forwarding_rule_model = ForwardingRule.from_dict(forwarding_rule_model_json)
        assert forwarding_rule_model != False

        # Construct a model instance of ForwardingRule by calling from_dict on the json representation
        forwarding_rule_model_dict = ForwardingRule.from_dict(forwarding_rule_model_json).__dict__
        forwarding_rule_model2 = ForwardingRule(**forwarding_rule_model_dict)

        # Verify the model instances are equivalent
        assert forwarding_rule_model == forwarding_rule_model2

        # Convert model instance back to dict and verify no loss of data
        forwarding_rule_model_json2 = forwarding_rule_model.to_dict()
        assert forwarding_rule_model_json2 == forwarding_rule_model_json

class TestModel_ForwardingRuleList():
    """
    Test Class for ForwardingRuleList
    """

    def test_forwarding_rule_list_serialization(self):
        """
        Test serialization/deserialization for ForwardingRuleList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        forwarding_rule_model = {} # ForwardingRule
        forwarding_rule_model['id'] = '5365b73c-ce6f-4d6f-ad9f-d9c131b26370'
        forwarding_rule_model['description'] = 'forwarding rule'
        forwarding_rule_model['type'] = 'zone'
        forwarding_rule_model['match'] = 'example.com'
        forwarding_rule_model['forward_to'] = ['161.26.0.7']
        forwarding_rule_model['created_on'] = '2021-04-21T08:18:25Z'
        forwarding_rule_model['modified_on'] = '2021-04-21T08:18:25Z'

        # Construct a json representation of a ForwardingRuleList model
        forwarding_rule_list_model_json = {}
        forwarding_rule_list_model_json['forwarding_rules'] = [forwarding_rule_model]

        # Construct a model instance of ForwardingRuleList by calling from_dict on the json representation
        forwarding_rule_list_model = ForwardingRuleList.from_dict(forwarding_rule_list_model_json)
        assert forwarding_rule_list_model != False

        # Construct a model instance of ForwardingRuleList by calling from_dict on the json representation
        forwarding_rule_list_model_dict = ForwardingRuleList.from_dict(forwarding_rule_list_model_json).__dict__
        forwarding_rule_list_model2 = ForwardingRuleList(**forwarding_rule_list_model_dict)

        # Verify the model instances are equivalent
        assert forwarding_rule_list_model == forwarding_rule_list_model2

        # Convert model instance back to dict and verify no loss of data
        forwarding_rule_list_model_json2 = forwarding_rule_list_model.to_dict()
        assert forwarding_rule_list_model_json2 == forwarding_rule_list_model_json

class TestModel_HealthcheckHeader():
    """
    Test Class for HealthcheckHeader
    """

    def test_healthcheck_header_serialization(self):
        """
        Test serialization/deserialization for HealthcheckHeader
        """

        # Construct a json representation of a HealthcheckHeader model
        healthcheck_header_model_json = {}
        healthcheck_header_model_json['name'] = 'Host'
        healthcheck_header_model_json['value'] = ['origin.example.com']

        # Construct a model instance of HealthcheckHeader by calling from_dict on the json representation
        healthcheck_header_model = HealthcheckHeader.from_dict(healthcheck_header_model_json)
        assert healthcheck_header_model != False

        # Construct a model instance of HealthcheckHeader by calling from_dict on the json representation
        healthcheck_header_model_dict = HealthcheckHeader.from_dict(healthcheck_header_model_json).__dict__
        healthcheck_header_model2 = HealthcheckHeader(**healthcheck_header_model_dict)

        # Verify the model instances are equivalent
        assert healthcheck_header_model == healthcheck_header_model2

        # Convert model instance back to dict and verify no loss of data
        healthcheck_header_model_json2 = healthcheck_header_model.to_dict()
        assert healthcheck_header_model_json2 == healthcheck_header_model_json

class TestModel_ImportResourceRecordsResp():
    """
    Test Class for ImportResourceRecordsResp
    """

    def test_import_resource_records_resp_serialization(self):
        """
        Test serialization/deserialization for ImportResourceRecordsResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        record_stats_by_type_model = {} # RecordStatsByType
        record_stats_by_type_model['A'] = 10
        record_stats_by_type_model['AAAA'] = 10
        record_stats_by_type_model['CNAME'] = 10
        record_stats_by_type_model['SRV'] = 10
        record_stats_by_type_model['TXT'] = 10
        record_stats_by_type_model['MX'] = 10
        record_stats_by_type_model['PTR'] = 10

        records_import_message_model_model = {} # RecordsImportMessageModel
        records_import_message_model_model['code'] = 'conflict'
        records_import_message_model_model['message'] = 'A type record conflict with other records'

        records_import_error_model_error_model = {} # RecordsImportErrorModelError
        records_import_error_model_error_model['code'] = 'internal_server_error'
        records_import_error_model_error_model['message'] = 'An internal error occurred. Try again later.'

        records_import_error_model_model = {} # RecordsImportErrorModel
        records_import_error_model_model['resource_record'] = 'test.example.com A 1.1.1.1'
        records_import_error_model_model['error'] = records_import_error_model_error_model

        # Construct a json representation of a ImportResourceRecordsResp model
        import_resource_records_resp_model_json = {}
        import_resource_records_resp_model_json['total_records_parsed'] = 10
        import_resource_records_resp_model_json['records_added'] = 2
        import_resource_records_resp_model_json['records_failed'] = 0
        import_resource_records_resp_model_json['records_added_by_type'] = record_stats_by_type_model
        import_resource_records_resp_model_json['records_failed_by_type'] = record_stats_by_type_model
        import_resource_records_resp_model_json['messages'] = [records_import_message_model_model]
        import_resource_records_resp_model_json['errors'] = [records_import_error_model_model]

        # Construct a model instance of ImportResourceRecordsResp by calling from_dict on the json representation
        import_resource_records_resp_model = ImportResourceRecordsResp.from_dict(import_resource_records_resp_model_json)
        assert import_resource_records_resp_model != False

        # Construct a model instance of ImportResourceRecordsResp by calling from_dict on the json representation
        import_resource_records_resp_model_dict = ImportResourceRecordsResp.from_dict(import_resource_records_resp_model_json).__dict__
        import_resource_records_resp_model2 = ImportResourceRecordsResp(**import_resource_records_resp_model_dict)

        # Verify the model instances are equivalent
        assert import_resource_records_resp_model == import_resource_records_resp_model2

        # Convert model instance back to dict and verify no loss of data
        import_resource_records_resp_model_json2 = import_resource_records_resp_model.to_dict()
        assert import_resource_records_resp_model_json2 == import_resource_records_resp_model_json

class TestModel_LinkedZone():
    """
    Test Class for LinkedZone
    """

    def test_linked_zone_serialization(self):
        """
        Test serialization/deserialization for LinkedZone
        """

        # Construct dict forms of any model objects needed in order to build this model.

        linked_zone_linked_to_model = {} # LinkedZoneLinkedTo
        linked_zone_linked_to_model['instance_crn'] = 'crn:v1:staging:public:pdnsdev:global:a/01652b251c3ae2787110a995d8db0135:abe30019-1c08-42dc-9ad9-a0682af70054::'
        linked_zone_linked_to_model['zone_id'] = '05855abe-3908-4cdc-bf0d-063e0b1c296d'

        # Construct a json representation of a LinkedZone model
        linked_zone_model_json = {}
        linked_zone_model_json['id'] = '5365b73c-ce6f-4d6f-ad9f-d9c131b26370'
        linked_zone_model_json['instance_id'] = '5cbc3c1b-021c-4ad7-b9e4-a5dfefdecf85'
        linked_zone_model_json['name'] = 'example.com'
        linked_zone_model_json['description'] = 'linked zone example'
        linked_zone_model_json['linked_to'] = linked_zone_linked_to_model
        linked_zone_model_json['state'] = 'APPROVAL_PENDING'
        linked_zone_model_json['label'] = 'dev'
        linked_zone_model_json['approval_required_before'] = '2022-03-16T07:23:25Z'
        linked_zone_model_json['created_on'] = '2022-03-09T07:23:25Z'
        linked_zone_model_json['modified_on'] = '2022-03-09T07:23:25Z'

        # Construct a model instance of LinkedZone by calling from_dict on the json representation
        linked_zone_model = LinkedZone.from_dict(linked_zone_model_json)
        assert linked_zone_model != False

        # Construct a model instance of LinkedZone by calling from_dict on the json representation
        linked_zone_model_dict = LinkedZone.from_dict(linked_zone_model_json).__dict__
        linked_zone_model2 = LinkedZone(**linked_zone_model_dict)

        # Verify the model instances are equivalent
        assert linked_zone_model == linked_zone_model2

        # Convert model instance back to dict and verify no loss of data
        linked_zone_model_json2 = linked_zone_model.to_dict()
        assert linked_zone_model_json2 == linked_zone_model_json

class TestModel_LinkedZonesList():
    """
    Test Class for LinkedZonesList
    """

    def test_linked_zones_list_serialization(self):
        """
        Test serialization/deserialization for LinkedZonesList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        linked_zone_linked_to_model = {} # LinkedZoneLinkedTo
        linked_zone_linked_to_model['instance_crn'] = 'crn:v1:staging:public:pdnsdev:global:a/01652b251c3ae2787110a995d8db0135:abe30019-1c08-42dc-9ad9-a0682af70054::'
        linked_zone_linked_to_model['zone_id'] = '05855abe-3908-4cdc-bf0d-063e0b1c296d'

        linked_zone_model = {} # LinkedZone
        linked_zone_model['id'] = '5365b73c-ce6f-4d6f-ad9f-d9c131b26370'
        linked_zone_model['instance_id'] = '5cbc3c1b-021c-4ad7-b9e4-a5dfefdecf85'
        linked_zone_model['name'] = 'example.com'
        linked_zone_model['description'] = 'linked zone example'
        linked_zone_model['linked_to'] = linked_zone_linked_to_model
        linked_zone_model['state'] = 'APPROVAL_PENDING'
        linked_zone_model['label'] = 'dev'
        linked_zone_model['approval_required_before'] = '2022-03-16T07:23:25Z'
        linked_zone_model['created_on'] = '2022-03-09T07:23:25Z'
        linked_zone_model['modified_on'] = '2022-03-09T07:23:25Z'

        pagination_ref_model = {} # PaginationRef
        pagination_ref_model['href'] = 'https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200'

        # Construct a json representation of a LinkedZonesList model
        linked_zones_list_model_json = {}
        linked_zones_list_model_json['linked_dnszones'] = [linked_zone_model]
        linked_zones_list_model_json['offset'] = 0
        linked_zones_list_model_json['limit'] = 200
        linked_zones_list_model_json['count'] = 1
        linked_zones_list_model_json['total_count'] = 1
        linked_zones_list_model_json['first'] = pagination_ref_model
        linked_zones_list_model_json['last'] = pagination_ref_model
        linked_zones_list_model_json['previous'] = pagination_ref_model
        linked_zones_list_model_json['next'] = pagination_ref_model

        # Construct a model instance of LinkedZonesList by calling from_dict on the json representation
        linked_zones_list_model = LinkedZonesList.from_dict(linked_zones_list_model_json)
        assert linked_zones_list_model != False

        # Construct a model instance of LinkedZonesList by calling from_dict on the json representation
        linked_zones_list_model_dict = LinkedZonesList.from_dict(linked_zones_list_model_json).__dict__
        linked_zones_list_model2 = LinkedZonesList(**linked_zones_list_model_dict)

        # Verify the model instances are equivalent
        assert linked_zones_list_model == linked_zones_list_model2

        # Convert model instance back to dict and verify no loss of data
        linked_zones_list_model_json2 = linked_zones_list_model.to_dict()
        assert linked_zones_list_model_json2 == linked_zones_list_model_json

class TestModel_ListDnszones():
    """
    Test Class for ListDnszones
    """

    def test_list_dnszones_serialization(self):
        """
        Test serialization/deserialization for ListDnszones
        """

        # Construct dict forms of any model objects needed in order to build this model.

        dnszone_model = {} # Dnszone
        dnszone_model['id'] = '2d0f862b-67cc-41f3-b6a2-59860d0aa90e'
        dnszone_model['created_on'] = '2019-01-01T05:20:00.12345Z'
        dnszone_model['modified_on'] = '2019-01-01T05:20:00.12345Z'
        dnszone_model['instance_id'] = '1407a753-a93f-4bb0-9784-bcfc269ee1b3'
        dnszone_model['name'] = 'example.com'
        dnszone_model['description'] = 'The DNS zone is used for VPCs in us-east region'
        dnszone_model['state'] = 'pending_network_add'
        dnszone_model['label'] = 'us-east'

        pagination_ref_model = {} # PaginationRef
        pagination_ref_model['href'] = 'https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200'

        # Construct a json representation of a ListDnszones model
        list_dnszones_model_json = {}
        list_dnszones_model_json['dnszones'] = [dnszone_model]
        list_dnszones_model_json['offset'] = 0
        list_dnszones_model_json['limit'] = 200
        list_dnszones_model_json['count'] = 1
        list_dnszones_model_json['total_count'] = 1
        list_dnszones_model_json['first'] = pagination_ref_model
        list_dnszones_model_json['last'] = pagination_ref_model
        list_dnszones_model_json['previous'] = pagination_ref_model
        list_dnszones_model_json['next'] = pagination_ref_model

        # Construct a model instance of ListDnszones by calling from_dict on the json representation
        list_dnszones_model = ListDnszones.from_dict(list_dnszones_model_json)
        assert list_dnszones_model != False

        # Construct a model instance of ListDnszones by calling from_dict on the json representation
        list_dnszones_model_dict = ListDnszones.from_dict(list_dnszones_model_json).__dict__
        list_dnszones_model2 = ListDnszones(**list_dnszones_model_dict)

        # Verify the model instances are equivalent
        assert list_dnszones_model == list_dnszones_model2

        # Convert model instance back to dict and verify no loss of data
        list_dnszones_model_json2 = list_dnszones_model.to_dict()
        assert list_dnszones_model_json2 == list_dnszones_model_json

class TestModel_ListLoadBalancers():
    """
    Test Class for ListLoadBalancers
    """

    def test_list_load_balancers_serialization(self):
        """
        Test serialization/deserialization for ListLoadBalancers
        """

        # Construct dict forms of any model objects needed in order to build this model.

        load_balancer_az_pools_item_model = {} # LoadBalancerAzPoolsItem
        load_balancer_az_pools_item_model['availability_zone'] = 'us-south-1'
        load_balancer_az_pools_item_model['pools'] = ['0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d']

        load_balancer_model = {} # LoadBalancer
        load_balancer_model['id'] = '5365b73c-ce6f-4d6f-ad9f-d9c131b26370'
        load_balancer_model['name'] = 'glb.example.com'
        load_balancer_model['description'] = 'Load balancer for glb.example.com.'
        load_balancer_model['enabled'] = True
        load_balancer_model['ttl'] = 120
        load_balancer_model['health'] = 'DEGRADED'
        load_balancer_model['fallback_pool'] = '24ccf79a-4ae0-4769-b4c8-17f8f230072e'
        load_balancer_model['default_pools'] = ['24ccf79a-4ae0-4769-b4c8-17f8f230072e', '13fa7d9e-aeff-4e14-8300-58021db9ee74']
        load_balancer_model['az_pools'] = [load_balancer_az_pools_item_model]
        load_balancer_model['created_on'] = '2019-01-01T05:20:00.12345Z'
        load_balancer_model['modified_on'] = '2019-01-01T05:20:00.12345Z'

        pagination_ref_model = {} # PaginationRef
        pagination_ref_model['href'] = 'https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200'

        # Construct a json representation of a ListLoadBalancers model
        list_load_balancers_model_json = {}
        list_load_balancers_model_json['load_balancers'] = [load_balancer_model]
        list_load_balancers_model_json['offset'] = 0
        list_load_balancers_model_json['limit'] = 200
        list_load_balancers_model_json['count'] = 1
        list_load_balancers_model_json['total_count'] = 1
        list_load_balancers_model_json['first'] = pagination_ref_model
        list_load_balancers_model_json['last'] = pagination_ref_model
        list_load_balancers_model_json['previous'] = pagination_ref_model
        list_load_balancers_model_json['next'] = pagination_ref_model

        # Construct a model instance of ListLoadBalancers by calling from_dict on the json representation
        list_load_balancers_model = ListLoadBalancers.from_dict(list_load_balancers_model_json)
        assert list_load_balancers_model != False

        # Construct a model instance of ListLoadBalancers by calling from_dict on the json representation
        list_load_balancers_model_dict = ListLoadBalancers.from_dict(list_load_balancers_model_json).__dict__
        list_load_balancers_model2 = ListLoadBalancers(**list_load_balancers_model_dict)

        # Verify the model instances are equivalent
        assert list_load_balancers_model == list_load_balancers_model2

        # Convert model instance back to dict and verify no loss of data
        list_load_balancers_model_json2 = list_load_balancers_model.to_dict()
        assert list_load_balancers_model_json2 == list_load_balancers_model_json

class TestModel_ListMonitors():
    """
    Test Class for ListMonitors
    """

    def test_list_monitors_serialization(self):
        """
        Test serialization/deserialization for ListMonitors
        """

        # Construct dict forms of any model objects needed in order to build this model.

        healthcheck_header_model = {} # HealthcheckHeader
        healthcheck_header_model['name'] = 'Host'
        healthcheck_header_model['value'] = ['origin.example.com']

        monitor_model = {} # Monitor
        monitor_model['id'] = '5365b73c-ce6f-4d6f-ad9f-d9c131b26370'
        monitor_model['name'] = 'healthcheck-monitor'
        monitor_model['description'] = 'Load balancer monitor for glb.example.com.'
        monitor_model['type'] = 'HTTPS'
        monitor_model['port'] = 8080
        monitor_model['interval'] = 60
        monitor_model['retries'] = 2
        monitor_model['timeout'] = 5
        monitor_model['method'] = 'GET'
        monitor_model['path'] = '/health'
        monitor_model['headers'] = [healthcheck_header_model]
        monitor_model['allow_insecure'] = False
        monitor_model['expected_codes'] = '200'
        monitor_model['expected_body'] = 'alive'
        monitor_model['created_on'] = '2019-01-01T05:20:00.12345Z'
        monitor_model['modified_on'] = '2019-01-01T05:20:00.12345Z'

        pagination_ref_model = {} # PaginationRef
        pagination_ref_model['href'] = 'https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200'

        # Construct a json representation of a ListMonitors model
        list_monitors_model_json = {}
        list_monitors_model_json['monitors'] = [monitor_model]
        list_monitors_model_json['offset'] = 0
        list_monitors_model_json['limit'] = 200
        list_monitors_model_json['count'] = 1
        list_monitors_model_json['total_count'] = 1
        list_monitors_model_json['first'] = pagination_ref_model
        list_monitors_model_json['last'] = pagination_ref_model
        list_monitors_model_json['previous'] = pagination_ref_model
        list_monitors_model_json['next'] = pagination_ref_model

        # Construct a model instance of ListMonitors by calling from_dict on the json representation
        list_monitors_model = ListMonitors.from_dict(list_monitors_model_json)
        assert list_monitors_model != False

        # Construct a model instance of ListMonitors by calling from_dict on the json representation
        list_monitors_model_dict = ListMonitors.from_dict(list_monitors_model_json).__dict__
        list_monitors_model2 = ListMonitors(**list_monitors_model_dict)

        # Verify the model instances are equivalent
        assert list_monitors_model == list_monitors_model2

        # Convert model instance back to dict and verify no loss of data
        list_monitors_model_json2 = list_monitors_model.to_dict()
        assert list_monitors_model_json2 == list_monitors_model_json

class TestModel_ListPermittedNetworks():
    """
    Test Class for ListPermittedNetworks
    """

    def test_list_permitted_networks_serialization(self):
        """
        Test serialization/deserialization for ListPermittedNetworks
        """

        # Construct dict forms of any model objects needed in order to build this model.

        permitted_network_vpc_model = {} # PermittedNetworkVpc
        permitted_network_vpc_model['vpc_crn'] = 'crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6'

        permitted_network_model = {} # PermittedNetwork
        permitted_network_model['id'] = 'fecd0173-3919-456b-b202-3029dfa1b0f7'
        permitted_network_model['created_on'] = '2019-01-01T05:20:00.12345Z'
        permitted_network_model['modified_on'] = '2019-01-01T05:20:00.12345Z'
        permitted_network_model['permitted_network'] = permitted_network_vpc_model
        permitted_network_model['type'] = 'vpc'
        permitted_network_model['state'] = 'ACTIVE'

        # Construct a json representation of a ListPermittedNetworks model
        list_permitted_networks_model_json = {}
        list_permitted_networks_model_json['permitted_networks'] = [permitted_network_model]

        # Construct a model instance of ListPermittedNetworks by calling from_dict on the json representation
        list_permitted_networks_model = ListPermittedNetworks.from_dict(list_permitted_networks_model_json)
        assert list_permitted_networks_model != False

        # Construct a model instance of ListPermittedNetworks by calling from_dict on the json representation
        list_permitted_networks_model_dict = ListPermittedNetworks.from_dict(list_permitted_networks_model_json).__dict__
        list_permitted_networks_model2 = ListPermittedNetworks(**list_permitted_networks_model_dict)

        # Verify the model instances are equivalent
        assert list_permitted_networks_model == list_permitted_networks_model2

        # Convert model instance back to dict and verify no loss of data
        list_permitted_networks_model_json2 = list_permitted_networks_model.to_dict()
        assert list_permitted_networks_model_json2 == list_permitted_networks_model_json

class TestModel_ListPools():
    """
    Test Class for ListPools
    """

    def test_list_pools_serialization(self):
        """
        Test serialization/deserialization for ListPools
        """

        # Construct dict forms of any model objects needed in order to build this model.

        origin_model = {} # Origin
        origin_model['name'] = 'app-server-1'
        origin_model['description'] = 'description of the origin server'
        origin_model['address'] = '10.10.16.8'
        origin_model['enabled'] = True
        origin_model['health'] = True
        origin_model['health_failure_reason'] = 'testString'

        pool_healthcheck_vsis_item_model = {} # PoolHealthcheckVsisItem
        pool_healthcheck_vsis_item_model['subnet'] = 'crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04'
        pool_healthcheck_vsis_item_model['ipv4_address'] = '10.10.16.8'
        pool_healthcheck_vsis_item_model['ipv4_cidr_block'] = '10.10.16.0/24'
        pool_healthcheck_vsis_item_model['vpc'] = 'crn:v1:staging:public:is:us-south:a/01652b251c3ae2787110a995d8db0135::vpc:r134-8c426a0a-ec74-4c97-9c02-f6194c224d8a'

        pool_model = {} # Pool
        pool_model['id'] = '5365b73c-ce6f-4d6f-ad9f-d9c131b26370'
        pool_model['name'] = 'dal10-az-pool'
        pool_model['description'] = 'Load balancer pool for dal10 availability zone.'
        pool_model['enabled'] = True
        pool_model['healthy_origins_threshold'] = 1
        pool_model['origins'] = [origin_model]
        pool_model['monitor'] = '7dd6841c-264e-11ea-88df-062967242a6a'
        pool_model['notification_channel'] = 'https://mywebsite.com/dns/webhook'
        pool_model['health'] = 'HEALTHY'
        pool_model['healthcheck_region'] = 'us-south'
        pool_model['healthcheck_subnets'] = ['crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04']
        pool_model['healthcheck_vsis'] = [pool_healthcheck_vsis_item_model]
        pool_model['created_on'] = '2019-01-01T05:20:00.12345Z'
        pool_model['modified_on'] = '2019-01-01T05:20:00.12345Z'

        pagination_ref_model = {} # PaginationRef
        pagination_ref_model['href'] = 'https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200'

        # Construct a json representation of a ListPools model
        list_pools_model_json = {}
        list_pools_model_json['pools'] = [pool_model]
        list_pools_model_json['offset'] = 0
        list_pools_model_json['limit'] = 200
        list_pools_model_json['count'] = 1
        list_pools_model_json['total_count'] = 1
        list_pools_model_json['first'] = pagination_ref_model
        list_pools_model_json['last'] = pagination_ref_model
        list_pools_model_json['previous'] = pagination_ref_model
        list_pools_model_json['next'] = pagination_ref_model

        # Construct a model instance of ListPools by calling from_dict on the json representation
        list_pools_model = ListPools.from_dict(list_pools_model_json)
        assert list_pools_model != False

        # Construct a model instance of ListPools by calling from_dict on the json representation
        list_pools_model_dict = ListPools.from_dict(list_pools_model_json).__dict__
        list_pools_model2 = ListPools(**list_pools_model_dict)

        # Verify the model instances are equivalent
        assert list_pools_model == list_pools_model2

        # Convert model instance back to dict and verify no loss of data
        list_pools_model_json2 = list_pools_model.to_dict()
        assert list_pools_model_json2 == list_pools_model_json

class TestModel_ListResourceRecords():
    """
    Test Class for ListResourceRecords
    """

    def test_list_resource_records_serialization(self):
        """
        Test serialization/deserialization for ListResourceRecords
        """

        # Construct dict forms of any model objects needed in order to build this model.

        resource_record_model = {} # ResourceRecord
        resource_record_model['id'] = 'SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370'
        resource_record_model['created_on'] = '2019-01-01T05:20:00.12345Z'
        resource_record_model['modified_on'] = '2019-01-01T05:20:00.12345Z'
        resource_record_model['name'] = '_sip._udp.test.example.com'
        resource_record_model['type'] = 'SRV'
        resource_record_model['ttl'] = 120
        resource_record_model['rdata'] = {'foo': 'bar'}
        resource_record_model['service'] = '_sip'
        resource_record_model['protocol'] = 'udp'

        pagination_ref_model = {} # PaginationRef
        pagination_ref_model['href'] = 'https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200'

        # Construct a json representation of a ListResourceRecords model
        list_resource_records_model_json = {}
        list_resource_records_model_json['resource_records'] = [resource_record_model]
        list_resource_records_model_json['offset'] = 0
        list_resource_records_model_json['limit'] = 200
        list_resource_records_model_json['count'] = 1
        list_resource_records_model_json['total_count'] = 1
        list_resource_records_model_json['first'] = pagination_ref_model
        list_resource_records_model_json['last'] = pagination_ref_model
        list_resource_records_model_json['previous'] = pagination_ref_model
        list_resource_records_model_json['next'] = pagination_ref_model

        # Construct a model instance of ListResourceRecords by calling from_dict on the json representation
        list_resource_records_model = ListResourceRecords.from_dict(list_resource_records_model_json)
        assert list_resource_records_model != False

        # Construct a model instance of ListResourceRecords by calling from_dict on the json representation
        list_resource_records_model_dict = ListResourceRecords.from_dict(list_resource_records_model_json).__dict__
        list_resource_records_model2 = ListResourceRecords(**list_resource_records_model_dict)

        # Verify the model instances are equivalent
        assert list_resource_records_model == list_resource_records_model2

        # Convert model instance back to dict and verify no loss of data
        list_resource_records_model_json2 = list_resource_records_model.to_dict()
        assert list_resource_records_model_json2 == list_resource_records_model_json

class TestModel_LoadBalancer():
    """
    Test Class for LoadBalancer
    """

    def test_load_balancer_serialization(self):
        """
        Test serialization/deserialization for LoadBalancer
        """

        # Construct dict forms of any model objects needed in order to build this model.

        load_balancer_az_pools_item_model = {} # LoadBalancerAzPoolsItem
        load_balancer_az_pools_item_model['availability_zone'] = 'us-south-1'
        load_balancer_az_pools_item_model['pools'] = ['0fc0bb7c-2fab-476e-8b9b-40fa14bf8e3d']

        # Construct a json representation of a LoadBalancer model
        load_balancer_model_json = {}
        load_balancer_model_json['id'] = '5365b73c-ce6f-4d6f-ad9f-d9c131b26370'
        load_balancer_model_json['name'] = 'glb.example.com'
        load_balancer_model_json['description'] = 'Load balancer for glb.example.com.'
        load_balancer_model_json['enabled'] = True
        load_balancer_model_json['ttl'] = 120
        load_balancer_model_json['health'] = 'DEGRADED'
        load_balancer_model_json['fallback_pool'] = '24ccf79a-4ae0-4769-b4c8-17f8f230072e'
        load_balancer_model_json['default_pools'] = ['24ccf79a-4ae0-4769-b4c8-17f8f230072e', '13fa7d9e-aeff-4e14-8300-58021db9ee74']
        load_balancer_model_json['az_pools'] = [load_balancer_az_pools_item_model]
        load_balancer_model_json['created_on'] = '2019-01-01T05:20:00.12345Z'
        load_balancer_model_json['modified_on'] = '2019-01-01T05:20:00.12345Z'

        # Construct a model instance of LoadBalancer by calling from_dict on the json representation
        load_balancer_model = LoadBalancer.from_dict(load_balancer_model_json)
        assert load_balancer_model != False

        # Construct a model instance of LoadBalancer by calling from_dict on the json representation
        load_balancer_model_dict = LoadBalancer.from_dict(load_balancer_model_json).__dict__
        load_balancer_model2 = LoadBalancer(**load_balancer_model_dict)

        # Verify the model instances are equivalent
        assert load_balancer_model == load_balancer_model2

        # Convert model instance back to dict and verify no loss of data
        load_balancer_model_json2 = load_balancer_model.to_dict()
        assert load_balancer_model_json2 == load_balancer_model_json

class TestModel_Location():
    """
    Test Class for Location
    """

    def test_location_serialization(self):
        """
        Test serialization/deserialization for Location
        """

        # Construct a json representation of a Location model
        location_model_json = {}
        location_model_json['id'] = '9a234ede-c2b6-4c39-bc27-d39ec139ecdb'
        location_model_json['subnet_crn'] = 'crn:v1:bluemix:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04'
        location_model_json['enabled'] = True
        location_model_json['healthy'] = True
        location_model_json['dns_server_ip'] = '10.10.16.8'

        # Construct a model instance of Location by calling from_dict on the json representation
        location_model = Location.from_dict(location_model_json)
        assert location_model != False

        # Construct a model instance of Location by calling from_dict on the json representation
        location_model_dict = Location.from_dict(location_model_json).__dict__
        location_model2 = Location(**location_model_dict)

        # Verify the model instances are equivalent
        assert location_model == location_model2

        # Convert model instance back to dict and verify no loss of data
        location_model_json2 = location_model.to_dict()
        assert location_model_json2 == location_model_json

class TestModel_LocationInput():
    """
    Test Class for LocationInput
    """

    def test_location_input_serialization(self):
        """
        Test serialization/deserialization for LocationInput
        """

        # Construct a json representation of a LocationInput model
        location_input_model_json = {}
        location_input_model_json['subnet_crn'] = 'crn:v1:bluemix:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04'
        location_input_model_json['enabled'] = False

        # Construct a model instance of LocationInput by calling from_dict on the json representation
        location_input_model = LocationInput.from_dict(location_input_model_json)
        assert location_input_model != False

        # Construct a model instance of LocationInput by calling from_dict on the json representation
        location_input_model_dict = LocationInput.from_dict(location_input_model_json).__dict__
        location_input_model2 = LocationInput(**location_input_model_dict)

        # Verify the model instances are equivalent
        assert location_input_model == location_input_model2

        # Convert model instance back to dict and verify no loss of data
        location_input_model_json2 = location_input_model.to_dict()
        assert location_input_model_json2 == location_input_model_json

class TestModel_Monitor():
    """
    Test Class for Monitor
    """

    def test_monitor_serialization(self):
        """
        Test serialization/deserialization for Monitor
        """

        # Construct dict forms of any model objects needed in order to build this model.

        healthcheck_header_model = {} # HealthcheckHeader
        healthcheck_header_model['name'] = 'Host'
        healthcheck_header_model['value'] = ['origin.example.com']

        # Construct a json representation of a Monitor model
        monitor_model_json = {}
        monitor_model_json['id'] = '5365b73c-ce6f-4d6f-ad9f-d9c131b26370'
        monitor_model_json['name'] = 'healthcheck-monitor'
        monitor_model_json['description'] = 'Load balancer monitor for glb.example.com.'
        monitor_model_json['type'] = 'HTTPS'
        monitor_model_json['port'] = 8080
        monitor_model_json['interval'] = 60
        monitor_model_json['retries'] = 2
        monitor_model_json['timeout'] = 5
        monitor_model_json['method'] = 'GET'
        monitor_model_json['path'] = '/health'
        monitor_model_json['headers'] = [healthcheck_header_model]
        monitor_model_json['allow_insecure'] = False
        monitor_model_json['expected_codes'] = '200'
        monitor_model_json['expected_body'] = 'alive'
        monitor_model_json['created_on'] = '2019-01-01T05:20:00.12345Z'
        monitor_model_json['modified_on'] = '2019-01-01T05:20:00.12345Z'

        # Construct a model instance of Monitor by calling from_dict on the json representation
        monitor_model = Monitor.from_dict(monitor_model_json)
        assert monitor_model != False

        # Construct a model instance of Monitor by calling from_dict on the json representation
        monitor_model_dict = Monitor.from_dict(monitor_model_json).__dict__
        monitor_model2 = Monitor(**monitor_model_dict)

        # Verify the model instances are equivalent
        assert monitor_model == monitor_model2

        # Convert model instance back to dict and verify no loss of data
        monitor_model_json2 = monitor_model.to_dict()
        assert monitor_model_json2 == monitor_model_json

class TestModel_Origin():
    """
    Test Class for Origin
    """

    def test_origin_serialization(self):
        """
        Test serialization/deserialization for Origin
        """

        # Construct a json representation of a Origin model
        origin_model_json = {}
        origin_model_json['name'] = 'app-server-1'
        origin_model_json['description'] = 'description of the origin server'
        origin_model_json['address'] = '10.10.16.8'
        origin_model_json['enabled'] = True
        origin_model_json['health'] = True
        origin_model_json['health_failure_reason'] = 'testString'

        # Construct a model instance of Origin by calling from_dict on the json representation
        origin_model = Origin.from_dict(origin_model_json)
        assert origin_model != False

        # Construct a model instance of Origin by calling from_dict on the json representation
        origin_model_dict = Origin.from_dict(origin_model_json).__dict__
        origin_model2 = Origin(**origin_model_dict)

        # Verify the model instances are equivalent
        assert origin_model == origin_model2

        # Convert model instance back to dict and verify no loss of data
        origin_model_json2 = origin_model.to_dict()
        assert origin_model_json2 == origin_model_json

class TestModel_OriginInput():
    """
    Test Class for OriginInput
    """

    def test_origin_input_serialization(self):
        """
        Test serialization/deserialization for OriginInput
        """

        # Construct a json representation of a OriginInput model
        origin_input_model_json = {}
        origin_input_model_json['name'] = 'app-server-1'
        origin_input_model_json['description'] = 'description of the origin server'
        origin_input_model_json['address'] = '10.10.16.8'
        origin_input_model_json['enabled'] = True

        # Construct a model instance of OriginInput by calling from_dict on the json representation
        origin_input_model = OriginInput.from_dict(origin_input_model_json)
        assert origin_input_model != False

        # Construct a model instance of OriginInput by calling from_dict on the json representation
        origin_input_model_dict = OriginInput.from_dict(origin_input_model_json).__dict__
        origin_input_model2 = OriginInput(**origin_input_model_dict)

        # Verify the model instances are equivalent
        assert origin_input_model == origin_input_model2

        # Convert model instance back to dict and verify no loss of data
        origin_input_model_json2 = origin_input_model.to_dict()
        assert origin_input_model_json2 == origin_input_model_json

class TestModel_PaginationRef():
    """
    Test Class for PaginationRef
    """

    def test_pagination_ref_serialization(self):
        """
        Test serialization/deserialization for PaginationRef
        """

        # Construct a json representation of a PaginationRef model
        pagination_ref_model_json = {}
        pagination_ref_model_json['href'] = 'https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200'

        # Construct a model instance of PaginationRef by calling from_dict on the json representation
        pagination_ref_model = PaginationRef.from_dict(pagination_ref_model_json)
        assert pagination_ref_model != False

        # Construct a model instance of PaginationRef by calling from_dict on the json representation
        pagination_ref_model_dict = PaginationRef.from_dict(pagination_ref_model_json).__dict__
        pagination_ref_model2 = PaginationRef(**pagination_ref_model_dict)

        # Verify the model instances are equivalent
        assert pagination_ref_model == pagination_ref_model2

        # Convert model instance back to dict and verify no loss of data
        pagination_ref_model_json2 = pagination_ref_model.to_dict()
        assert pagination_ref_model_json2 == pagination_ref_model_json

class TestModel_PermittedNetwork():
    """
    Test Class for PermittedNetwork
    """

    def test_permitted_network_serialization(self):
        """
        Test serialization/deserialization for PermittedNetwork
        """

        # Construct dict forms of any model objects needed in order to build this model.

        permitted_network_vpc_model = {} # PermittedNetworkVpc
        permitted_network_vpc_model['vpc_crn'] = 'crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6'

        # Construct a json representation of a PermittedNetwork model
        permitted_network_model_json = {}
        permitted_network_model_json['id'] = 'fecd0173-3919-456b-b202-3029dfa1b0f7'
        permitted_network_model_json['created_on'] = '2019-01-01T05:20:00.12345Z'
        permitted_network_model_json['modified_on'] = '2019-01-01T05:20:00.12345Z'
        permitted_network_model_json['permitted_network'] = permitted_network_vpc_model
        permitted_network_model_json['type'] = 'vpc'
        permitted_network_model_json['state'] = 'ACTIVE'

        # Construct a model instance of PermittedNetwork by calling from_dict on the json representation
        permitted_network_model = PermittedNetwork.from_dict(permitted_network_model_json)
        assert permitted_network_model != False

        # Construct a model instance of PermittedNetwork by calling from_dict on the json representation
        permitted_network_model_dict = PermittedNetwork.from_dict(permitted_network_model_json).__dict__
        permitted_network_model2 = PermittedNetwork(**permitted_network_model_dict)

        # Verify the model instances are equivalent
        assert permitted_network_model == permitted_network_model2

        # Convert model instance back to dict and verify no loss of data
        permitted_network_model_json2 = permitted_network_model.to_dict()
        assert permitted_network_model_json2 == permitted_network_model_json

class TestModel_PermittedNetworkVpc():
    """
    Test Class for PermittedNetworkVpc
    """

    def test_permitted_network_vpc_serialization(self):
        """
        Test serialization/deserialization for PermittedNetworkVpc
        """

        # Construct a json representation of a PermittedNetworkVpc model
        permitted_network_vpc_model_json = {}
        permitted_network_vpc_model_json['vpc_crn'] = 'crn:v1:bluemix:public:is:eu-de:a/bcf1865e99742d38d2d5fc3fb80a5496::vpc:6e6cc326-04d1-4c99-a289-efb3ae4193d6'

        # Construct a model instance of PermittedNetworkVpc by calling from_dict on the json representation
        permitted_network_vpc_model = PermittedNetworkVpc.from_dict(permitted_network_vpc_model_json)
        assert permitted_network_vpc_model != False

        # Construct a model instance of PermittedNetworkVpc by calling from_dict on the json representation
        permitted_network_vpc_model_dict = PermittedNetworkVpc.from_dict(permitted_network_vpc_model_json).__dict__
        permitted_network_vpc_model2 = PermittedNetworkVpc(**permitted_network_vpc_model_dict)

        # Verify the model instances are equivalent
        assert permitted_network_vpc_model == permitted_network_vpc_model2

        # Convert model instance back to dict and verify no loss of data
        permitted_network_vpc_model_json2 = permitted_network_vpc_model.to_dict()
        assert permitted_network_vpc_model_json2 == permitted_network_vpc_model_json

class TestModel_Pool():
    """
    Test Class for Pool
    """

    def test_pool_serialization(self):
        """
        Test serialization/deserialization for Pool
        """

        # Construct dict forms of any model objects needed in order to build this model.

        origin_model = {} # Origin
        origin_model['name'] = 'app-server-1'
        origin_model['description'] = 'description of the origin server'
        origin_model['address'] = '10.10.16.8'
        origin_model['enabled'] = True
        origin_model['health'] = True
        origin_model['health_failure_reason'] = 'testString'

        pool_healthcheck_vsis_item_model = {} # PoolHealthcheckVsisItem
        pool_healthcheck_vsis_item_model['subnet'] = 'crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04'
        pool_healthcheck_vsis_item_model['ipv4_address'] = '10.10.16.8'
        pool_healthcheck_vsis_item_model['ipv4_cidr_block'] = '10.10.16.0/24'
        pool_healthcheck_vsis_item_model['vpc'] = 'crn:v1:staging:public:is:us-south:a/01652b251c3ae2787110a995d8db0135::vpc:r134-8c426a0a-ec74-4c97-9c02-f6194c224d8a'

        # Construct a json representation of a Pool model
        pool_model_json = {}
        pool_model_json['id'] = '5365b73c-ce6f-4d6f-ad9f-d9c131b26370'
        pool_model_json['name'] = 'dal10-az-pool'
        pool_model_json['description'] = 'Load balancer pool for dal10 availability zone.'
        pool_model_json['enabled'] = True
        pool_model_json['healthy_origins_threshold'] = 1
        pool_model_json['origins'] = [origin_model]
        pool_model_json['monitor'] = '7dd6841c-264e-11ea-88df-062967242a6a'
        pool_model_json['notification_channel'] = 'https://mywebsite.com/dns/webhook'
        pool_model_json['health'] = 'HEALTHY'
        pool_model_json['healthcheck_region'] = 'us-south'
        pool_model_json['healthcheck_subnets'] = ['crn:v1:staging:public:is:us-south-1:a/01652b251c3ae2787110a995d8db0135::subnet:0716-b49ef064-0f89-4fb1-8212-135b12568f04']
        pool_model_json['healthcheck_vsis'] = [pool_healthcheck_vsis_item_model]
        pool_model_json['created_on'] = '2019-01-01T05:20:00.12345Z'
        pool_model_json['modified_on'] = '2019-01-01T05:20:00.12345Z'

        # Construct a model instance of Pool by calling from_dict on the json representation
        pool_model = Pool.from_dict(pool_model_json)
        assert pool_model != False

        # Construct a model instance of Pool by calling from_dict on the json representation
        pool_model_dict = Pool.from_dict(pool_model_json).__dict__
        pool_model2 = Pool(**pool_model_dict)

        # Verify the model instances are equivalent
        assert pool_model == pool_model2

        # Convert model instance back to dict and verify no loss of data
        pool_model_json2 = pool_model.to_dict()
        assert pool_model_json2 == pool_model_json

class TestModel_RecordStatsByType():
    """
    Test Class for RecordStatsByType
    """

    def test_record_stats_by_type_serialization(self):
        """
        Test serialization/deserialization for RecordStatsByType
        """

        # Construct a json representation of a RecordStatsByType model
        record_stats_by_type_model_json = {}
        record_stats_by_type_model_json['A'] = 10
        record_stats_by_type_model_json['AAAA'] = 10
        record_stats_by_type_model_json['CNAME'] = 10
        record_stats_by_type_model_json['SRV'] = 10
        record_stats_by_type_model_json['TXT'] = 10
        record_stats_by_type_model_json['MX'] = 10
        record_stats_by_type_model_json['PTR'] = 10

        # Construct a model instance of RecordStatsByType by calling from_dict on the json representation
        record_stats_by_type_model = RecordStatsByType.from_dict(record_stats_by_type_model_json)
        assert record_stats_by_type_model != False

        # Construct a model instance of RecordStatsByType by calling from_dict on the json representation
        record_stats_by_type_model_dict = RecordStatsByType.from_dict(record_stats_by_type_model_json).__dict__
        record_stats_by_type_model2 = RecordStatsByType(**record_stats_by_type_model_dict)

        # Verify the model instances are equivalent
        assert record_stats_by_type_model == record_stats_by_type_model2

        # Convert model instance back to dict and verify no loss of data
        record_stats_by_type_model_json2 = record_stats_by_type_model.to_dict()
        assert record_stats_by_type_model_json2 == record_stats_by_type_model_json

class TestModel_RecordsImportErrorModel():
    """
    Test Class for RecordsImportErrorModel
    """

    def test_records_import_error_model_serialization(self):
        """
        Test serialization/deserialization for RecordsImportErrorModel
        """

        # Construct dict forms of any model objects needed in order to build this model.

        records_import_error_model_error_model = {} # RecordsImportErrorModelError
        records_import_error_model_error_model['code'] = 'internal_server_error'
        records_import_error_model_error_model['message'] = 'An internal error occurred. Try again later.'

        # Construct a json representation of a RecordsImportErrorModel model
        records_import_error_model_model_json = {}
        records_import_error_model_model_json['resource_record'] = 'test.example.com A 1.1.1.1'
        records_import_error_model_model_json['error'] = records_import_error_model_error_model

        # Construct a model instance of RecordsImportErrorModel by calling from_dict on the json representation
        records_import_error_model_model = RecordsImportErrorModel.from_dict(records_import_error_model_model_json)
        assert records_import_error_model_model != False

        # Construct a model instance of RecordsImportErrorModel by calling from_dict on the json representation
        records_import_error_model_model_dict = RecordsImportErrorModel.from_dict(records_import_error_model_model_json).__dict__
        records_import_error_model_model2 = RecordsImportErrorModel(**records_import_error_model_model_dict)

        # Verify the model instances are equivalent
        assert records_import_error_model_model == records_import_error_model_model2

        # Convert model instance back to dict and verify no loss of data
        records_import_error_model_model_json2 = records_import_error_model_model.to_dict()
        assert records_import_error_model_model_json2 == records_import_error_model_model_json

class TestModel_RecordsImportMessageModel():
    """
    Test Class for RecordsImportMessageModel
    """

    def test_records_import_message_model_serialization(self):
        """
        Test serialization/deserialization for RecordsImportMessageModel
        """

        # Construct a json representation of a RecordsImportMessageModel model
        records_import_message_model_model_json = {}
        records_import_message_model_model_json['code'] = 'conflict'
        records_import_message_model_model_json['message'] = 'A type record conflict with other records'

        # Construct a model instance of RecordsImportMessageModel by calling from_dict on the json representation
        records_import_message_model_model = RecordsImportMessageModel.from_dict(records_import_message_model_model_json)
        assert records_import_message_model_model != False

        # Construct a model instance of RecordsImportMessageModel by calling from_dict on the json representation
        records_import_message_model_model_dict = RecordsImportMessageModel.from_dict(records_import_message_model_model_json).__dict__
        records_import_message_model_model2 = RecordsImportMessageModel(**records_import_message_model_model_dict)

        # Verify the model instances are equivalent
        assert records_import_message_model_model == records_import_message_model_model2

        # Convert model instance back to dict and verify no loss of data
        records_import_message_model_model_json2 = records_import_message_model_model.to_dict()
        assert records_import_message_model_model_json2 == records_import_message_model_model_json

class TestModel_ResourceRecord():
    """
    Test Class for ResourceRecord
    """

    def test_resource_record_serialization(self):
        """
        Test serialization/deserialization for ResourceRecord
        """

        # Construct a json representation of a ResourceRecord model
        resource_record_model_json = {}
        resource_record_model_json['id'] = 'SRV:5365b73c-ce6f-4d6f-ad9f-d9c131b26370'
        resource_record_model_json['created_on'] = '2019-01-01T05:20:00.12345Z'
        resource_record_model_json['modified_on'] = '2019-01-01T05:20:00.12345Z'
        resource_record_model_json['name'] = '_sip._udp.test.example.com'
        resource_record_model_json['type'] = 'SRV'
        resource_record_model_json['ttl'] = 120
        resource_record_model_json['rdata'] = {'foo': 'bar'}
        resource_record_model_json['service'] = '_sip'
        resource_record_model_json['protocol'] = 'udp'

        # Construct a model instance of ResourceRecord by calling from_dict on the json representation
        resource_record_model = ResourceRecord.from_dict(resource_record_model_json)
        assert resource_record_model != False

        # Construct a model instance of ResourceRecord by calling from_dict on the json representation
        resource_record_model_dict = ResourceRecord.from_dict(resource_record_model_json).__dict__
        resource_record_model2 = ResourceRecord(**resource_record_model_dict)

        # Verify the model instances are equivalent
        assert resource_record_model == resource_record_model2

        # Convert model instance back to dict and verify no loss of data
        resource_record_model_json2 = resource_record_model.to_dict()
        assert resource_record_model_json2 == resource_record_model_json

class TestModel_SecondaryZone():
    """
    Test Class for SecondaryZone
    """

    def test_secondary_zone_serialization(self):
        """
        Test serialization/deserialization for SecondaryZone
        """

        # Construct dict forms of any model objects needed in order to build this model.

        secondary_zone_transfer_from_item_model = {} # SecondaryZoneTransferFromItem
        secondary_zone_transfer_from_item_model['address'] = '10.0.0.7'
        secondary_zone_transfer_from_item_model['port'] = 53

        # Construct a json representation of a SecondaryZone model
        secondary_zone_model_json = {}
        secondary_zone_model_json['id'] = 'f97ef698-d5fa-4f91-bc5a-33f17d143b7d'
        secondary_zone_model_json['description'] = 'secondary zone'
        secondary_zone_model_json['zone'] = 'example.com'
        secondary_zone_model_json['enabled'] = False
        secondary_zone_model_json['transfer_from'] = [secondary_zone_transfer_from_item_model]
        secondary_zone_model_json['created_on'] = '2022-03-16T08:18:25Z'
        secondary_zone_model_json['modified_on'] = '2022-03-16T08:18:25Z'

        # Construct a model instance of SecondaryZone by calling from_dict on the json representation
        secondary_zone_model = SecondaryZone.from_dict(secondary_zone_model_json)
        assert secondary_zone_model != False

        # Construct a model instance of SecondaryZone by calling from_dict on the json representation
        secondary_zone_model_dict = SecondaryZone.from_dict(secondary_zone_model_json).__dict__
        secondary_zone_model2 = SecondaryZone(**secondary_zone_model_dict)

        # Verify the model instances are equivalent
        assert secondary_zone_model == secondary_zone_model2

        # Convert model instance back to dict and verify no loss of data
        secondary_zone_model_json2 = secondary_zone_model.to_dict()
        assert secondary_zone_model_json2 == secondary_zone_model_json

class TestModel_SecondaryZoneList():
    """
    Test Class for SecondaryZoneList
    """

    def test_secondary_zone_list_serialization(self):
        """
        Test serialization/deserialization for SecondaryZoneList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        secondary_zone_transfer_from_item_model = {} # SecondaryZoneTransferFromItem
        secondary_zone_transfer_from_item_model['address'] = '10.0.0.7'
        secondary_zone_transfer_from_item_model['port'] = 53

        secondary_zone_model = {} # SecondaryZone
        secondary_zone_model['id'] = 'f97ef698-d5fa-4f91-bc5a-33f17d143b7d'
        secondary_zone_model['description'] = 'secondary zone'
        secondary_zone_model['zone'] = 'example.com'
        secondary_zone_model['enabled'] = False
        secondary_zone_model['transfer_from'] = [secondary_zone_transfer_from_item_model]
        secondary_zone_model['created_on'] = '2022-03-16T08:18:25Z'
        secondary_zone_model['modified_on'] = '2022-03-16T08:18:25Z'

        pagination_ref_model = {} # PaginationRef
        pagination_ref_model['href'] = 'https://api.dns-svcs.cloud.ibm.com/v1/instances/434f6c3e-6014-4124-a61d-2e910bca19b1/dnszones?offset=0&limit=200'

        # Construct a json representation of a SecondaryZoneList model
        secondary_zone_list_model_json = {}
        secondary_zone_list_model_json['secondary_zones'] = [secondary_zone_model]
        secondary_zone_list_model_json['offset'] = 0
        secondary_zone_list_model_json['limit'] = 200
        secondary_zone_list_model_json['count'] = 1
        secondary_zone_list_model_json['total_count'] = 1
        secondary_zone_list_model_json['first'] = pagination_ref_model
        secondary_zone_list_model_json['last'] = pagination_ref_model
        secondary_zone_list_model_json['previous'] = pagination_ref_model
        secondary_zone_list_model_json['next'] = pagination_ref_model

        # Construct a model instance of SecondaryZoneList by calling from_dict on the json representation
        secondary_zone_list_model = SecondaryZoneList.from_dict(secondary_zone_list_model_json)
        assert secondary_zone_list_model != False

        # Construct a model instance of SecondaryZoneList by calling from_dict on the json representation
        secondary_zone_list_model_dict = SecondaryZoneList.from_dict(secondary_zone_list_model_json).__dict__
        secondary_zone_list_model2 = SecondaryZoneList(**secondary_zone_list_model_dict)

        # Verify the model instances are equivalent
        assert secondary_zone_list_model == secondary_zone_list_model2

        # Convert model instance back to dict and verify no loss of data
        secondary_zone_list_model_json2 = secondary_zone_list_model.to_dict()
        assert secondary_zone_list_model_json2 == secondary_zone_list_model_json

class TestModel_ResourceRecordInputRdataRdataARecord():
    """
    Test Class for ResourceRecordInputRdataRdataARecord
    """

    def test_resource_record_input_rdata_rdata_a_record_serialization(self):
        """
        Test serialization/deserialization for ResourceRecordInputRdataRdataARecord
        """

        # Construct a json representation of a ResourceRecordInputRdataRdataARecord model
        resource_record_input_rdata_rdata_a_record_model_json = {}
        resource_record_input_rdata_rdata_a_record_model_json['ip'] = '10.110.201.214'

        # Construct a model instance of ResourceRecordInputRdataRdataARecord by calling from_dict on the json representation
        resource_record_input_rdata_rdata_a_record_model = ResourceRecordInputRdataRdataARecord.from_dict(resource_record_input_rdata_rdata_a_record_model_json)
        assert resource_record_input_rdata_rdata_a_record_model != False

        # Construct a model instance of ResourceRecordInputRdataRdataARecord by calling from_dict on the json representation
        resource_record_input_rdata_rdata_a_record_model_dict = ResourceRecordInputRdataRdataARecord.from_dict(resource_record_input_rdata_rdata_a_record_model_json).__dict__
        resource_record_input_rdata_rdata_a_record_model2 = ResourceRecordInputRdataRdataARecord(**resource_record_input_rdata_rdata_a_record_model_dict)

        # Verify the model instances are equivalent
        assert resource_record_input_rdata_rdata_a_record_model == resource_record_input_rdata_rdata_a_record_model2

        # Convert model instance back to dict and verify no loss of data
        resource_record_input_rdata_rdata_a_record_model_json2 = resource_record_input_rdata_rdata_a_record_model.to_dict()
        assert resource_record_input_rdata_rdata_a_record_model_json2 == resource_record_input_rdata_rdata_a_record_model_json

class TestModel_ResourceRecordInputRdataRdataAaaaRecord():
    """
    Test Class for ResourceRecordInputRdataRdataAaaaRecord
    """

    def test_resource_record_input_rdata_rdata_aaaa_record_serialization(self):
        """
        Test serialization/deserialization for ResourceRecordInputRdataRdataAaaaRecord
        """

        # Construct a json representation of a ResourceRecordInputRdataRdataAaaaRecord model
        resource_record_input_rdata_rdata_aaaa_record_model_json = {}
        resource_record_input_rdata_rdata_aaaa_record_model_json['ip'] = '2019::2019'

        # Construct a model instance of ResourceRecordInputRdataRdataAaaaRecord by calling from_dict on the json representation
        resource_record_input_rdata_rdata_aaaa_record_model = ResourceRecordInputRdataRdataAaaaRecord.from_dict(resource_record_input_rdata_rdata_aaaa_record_model_json)
        assert resource_record_input_rdata_rdata_aaaa_record_model != False

        # Construct a model instance of ResourceRecordInputRdataRdataAaaaRecord by calling from_dict on the json representation
        resource_record_input_rdata_rdata_aaaa_record_model_dict = ResourceRecordInputRdataRdataAaaaRecord.from_dict(resource_record_input_rdata_rdata_aaaa_record_model_json).__dict__
        resource_record_input_rdata_rdata_aaaa_record_model2 = ResourceRecordInputRdataRdataAaaaRecord(**resource_record_input_rdata_rdata_aaaa_record_model_dict)

        # Verify the model instances are equivalent
        assert resource_record_input_rdata_rdata_aaaa_record_model == resource_record_input_rdata_rdata_aaaa_record_model2

        # Convert model instance back to dict and verify no loss of data
        resource_record_input_rdata_rdata_aaaa_record_model_json2 = resource_record_input_rdata_rdata_aaaa_record_model.to_dict()
        assert resource_record_input_rdata_rdata_aaaa_record_model_json2 == resource_record_input_rdata_rdata_aaaa_record_model_json

class TestModel_ResourceRecordInputRdataRdataCnameRecord():
    """
    Test Class for ResourceRecordInputRdataRdataCnameRecord
    """

    def test_resource_record_input_rdata_rdata_cname_record_serialization(self):
        """
        Test serialization/deserialization for ResourceRecordInputRdataRdataCnameRecord
        """

        # Construct a json representation of a ResourceRecordInputRdataRdataCnameRecord model
        resource_record_input_rdata_rdata_cname_record_model_json = {}
        resource_record_input_rdata_rdata_cname_record_model_json['cname'] = 'www.example.com'

        # Construct a model instance of ResourceRecordInputRdataRdataCnameRecord by calling from_dict on the json representation
        resource_record_input_rdata_rdata_cname_record_model = ResourceRecordInputRdataRdataCnameRecord.from_dict(resource_record_input_rdata_rdata_cname_record_model_json)
        assert resource_record_input_rdata_rdata_cname_record_model != False

        # Construct a model instance of ResourceRecordInputRdataRdataCnameRecord by calling from_dict on the json representation
        resource_record_input_rdata_rdata_cname_record_model_dict = ResourceRecordInputRdataRdataCnameRecord.from_dict(resource_record_input_rdata_rdata_cname_record_model_json).__dict__
        resource_record_input_rdata_rdata_cname_record_model2 = ResourceRecordInputRdataRdataCnameRecord(**resource_record_input_rdata_rdata_cname_record_model_dict)

        # Verify the model instances are equivalent
        assert resource_record_input_rdata_rdata_cname_record_model == resource_record_input_rdata_rdata_cname_record_model2

        # Convert model instance back to dict and verify no loss of data
        resource_record_input_rdata_rdata_cname_record_model_json2 = resource_record_input_rdata_rdata_cname_record_model.to_dict()
        assert resource_record_input_rdata_rdata_cname_record_model_json2 == resource_record_input_rdata_rdata_cname_record_model_json

class TestModel_ResourceRecordInputRdataRdataMxRecord():
    """
    Test Class for ResourceRecordInputRdataRdataMxRecord
    """

    def test_resource_record_input_rdata_rdata_mx_record_serialization(self):
        """
        Test serialization/deserialization for ResourceRecordInputRdataRdataMxRecord
        """

        # Construct a json representation of a ResourceRecordInputRdataRdataMxRecord model
        resource_record_input_rdata_rdata_mx_record_model_json = {}
        resource_record_input_rdata_rdata_mx_record_model_json['exchange'] = 'mail.example.com'
        resource_record_input_rdata_rdata_mx_record_model_json['preference'] = 10

        # Construct a model instance of ResourceRecordInputRdataRdataMxRecord by calling from_dict on the json representation
        resource_record_input_rdata_rdata_mx_record_model = ResourceRecordInputRdataRdataMxRecord.from_dict(resource_record_input_rdata_rdata_mx_record_model_json)
        assert resource_record_input_rdata_rdata_mx_record_model != False

        # Construct a model instance of ResourceRecordInputRdataRdataMxRecord by calling from_dict on the json representation
        resource_record_input_rdata_rdata_mx_record_model_dict = ResourceRecordInputRdataRdataMxRecord.from_dict(resource_record_input_rdata_rdata_mx_record_model_json).__dict__
        resource_record_input_rdata_rdata_mx_record_model2 = ResourceRecordInputRdataRdataMxRecord(**resource_record_input_rdata_rdata_mx_record_model_dict)

        # Verify the model instances are equivalent
        assert resource_record_input_rdata_rdata_mx_record_model == resource_record_input_rdata_rdata_mx_record_model2

        # Convert model instance back to dict and verify no loss of data
        resource_record_input_rdata_rdata_mx_record_model_json2 = resource_record_input_rdata_rdata_mx_record_model.to_dict()
        assert resource_record_input_rdata_rdata_mx_record_model_json2 == resource_record_input_rdata_rdata_mx_record_model_json

class TestModel_ResourceRecordInputRdataRdataPtrRecord():
    """
    Test Class for ResourceRecordInputRdataRdataPtrRecord
    """

    def test_resource_record_input_rdata_rdata_ptr_record_serialization(self):
        """
        Test serialization/deserialization for ResourceRecordInputRdataRdataPtrRecord
        """

        # Construct a json representation of a ResourceRecordInputRdataRdataPtrRecord model
        resource_record_input_rdata_rdata_ptr_record_model_json = {}
        resource_record_input_rdata_rdata_ptr_record_model_json['ptrdname'] = 'www.example.com'

        # Construct a model instance of ResourceRecordInputRdataRdataPtrRecord by calling from_dict on the json representation
        resource_record_input_rdata_rdata_ptr_record_model = ResourceRecordInputRdataRdataPtrRecord.from_dict(resource_record_input_rdata_rdata_ptr_record_model_json)
        assert resource_record_input_rdata_rdata_ptr_record_model != False

        # Construct a model instance of ResourceRecordInputRdataRdataPtrRecord by calling from_dict on the json representation
        resource_record_input_rdata_rdata_ptr_record_model_dict = ResourceRecordInputRdataRdataPtrRecord.from_dict(resource_record_input_rdata_rdata_ptr_record_model_json).__dict__
        resource_record_input_rdata_rdata_ptr_record_model2 = ResourceRecordInputRdataRdataPtrRecord(**resource_record_input_rdata_rdata_ptr_record_model_dict)

        # Verify the model instances are equivalent
        assert resource_record_input_rdata_rdata_ptr_record_model == resource_record_input_rdata_rdata_ptr_record_model2

        # Convert model instance back to dict and verify no loss of data
        resource_record_input_rdata_rdata_ptr_record_model_json2 = resource_record_input_rdata_rdata_ptr_record_model.to_dict()
        assert resource_record_input_rdata_rdata_ptr_record_model_json2 == resource_record_input_rdata_rdata_ptr_record_model_json

class TestModel_ResourceRecordInputRdataRdataSrvRecord():
    """
    Test Class for ResourceRecordInputRdataRdataSrvRecord
    """

    def test_resource_record_input_rdata_rdata_srv_record_serialization(self):
        """
        Test serialization/deserialization for ResourceRecordInputRdataRdataSrvRecord
        """

        # Construct a json representation of a ResourceRecordInputRdataRdataSrvRecord model
        resource_record_input_rdata_rdata_srv_record_model_json = {}
        resource_record_input_rdata_rdata_srv_record_model_json['port'] = 80
        resource_record_input_rdata_rdata_srv_record_model_json['priority'] = 10
        resource_record_input_rdata_rdata_srv_record_model_json['target'] = 'www.example.com'
        resource_record_input_rdata_rdata_srv_record_model_json['weight'] = 10

        # Construct a model instance of ResourceRecordInputRdataRdataSrvRecord by calling from_dict on the json representation
        resource_record_input_rdata_rdata_srv_record_model = ResourceRecordInputRdataRdataSrvRecord.from_dict(resource_record_input_rdata_rdata_srv_record_model_json)
        assert resource_record_input_rdata_rdata_srv_record_model != False

        # Construct a model instance of ResourceRecordInputRdataRdataSrvRecord by calling from_dict on the json representation
        resource_record_input_rdata_rdata_srv_record_model_dict = ResourceRecordInputRdataRdataSrvRecord.from_dict(resource_record_input_rdata_rdata_srv_record_model_json).__dict__
        resource_record_input_rdata_rdata_srv_record_model2 = ResourceRecordInputRdataRdataSrvRecord(**resource_record_input_rdata_rdata_srv_record_model_dict)

        # Verify the model instances are equivalent
        assert resource_record_input_rdata_rdata_srv_record_model == resource_record_input_rdata_rdata_srv_record_model2

        # Convert model instance back to dict and verify no loss of data
        resource_record_input_rdata_rdata_srv_record_model_json2 = resource_record_input_rdata_rdata_srv_record_model.to_dict()
        assert resource_record_input_rdata_rdata_srv_record_model_json2 == resource_record_input_rdata_rdata_srv_record_model_json

class TestModel_ResourceRecordInputRdataRdataTxtRecord():
    """
    Test Class for ResourceRecordInputRdataRdataTxtRecord
    """

    def test_resource_record_input_rdata_rdata_txt_record_serialization(self):
        """
        Test serialization/deserialization for ResourceRecordInputRdataRdataTxtRecord
        """

        # Construct a json representation of a ResourceRecordInputRdataRdataTxtRecord model
        resource_record_input_rdata_rdata_txt_record_model_json = {}
        resource_record_input_rdata_rdata_txt_record_model_json['text'] = 'This is a text record'

        # Construct a model instance of ResourceRecordInputRdataRdataTxtRecord by calling from_dict on the json representation
        resource_record_input_rdata_rdata_txt_record_model = ResourceRecordInputRdataRdataTxtRecord.from_dict(resource_record_input_rdata_rdata_txt_record_model_json)
        assert resource_record_input_rdata_rdata_txt_record_model != False

        # Construct a model instance of ResourceRecordInputRdataRdataTxtRecord by calling from_dict on the json representation
        resource_record_input_rdata_rdata_txt_record_model_dict = ResourceRecordInputRdataRdataTxtRecord.from_dict(resource_record_input_rdata_rdata_txt_record_model_json).__dict__
        resource_record_input_rdata_rdata_txt_record_model2 = ResourceRecordInputRdataRdataTxtRecord(**resource_record_input_rdata_rdata_txt_record_model_dict)

        # Verify the model instances are equivalent
        assert resource_record_input_rdata_rdata_txt_record_model == resource_record_input_rdata_rdata_txt_record_model2

        # Convert model instance back to dict and verify no loss of data
        resource_record_input_rdata_rdata_txt_record_model_json2 = resource_record_input_rdata_rdata_txt_record_model.to_dict()
        assert resource_record_input_rdata_rdata_txt_record_model_json2 == resource_record_input_rdata_rdata_txt_record_model_json

class TestModel_ResourceRecordUpdateInputRdataRdataARecord():
    """
    Test Class for ResourceRecordUpdateInputRdataRdataARecord
    """

    def test_resource_record_update_input_rdata_rdata_a_record_serialization(self):
        """
        Test serialization/deserialization for ResourceRecordUpdateInputRdataRdataARecord
        """

        # Construct a json representation of a ResourceRecordUpdateInputRdataRdataARecord model
        resource_record_update_input_rdata_rdata_a_record_model_json = {}
        resource_record_update_input_rdata_rdata_a_record_model_json['ip'] = '10.110.201.214'

        # Construct a model instance of ResourceRecordUpdateInputRdataRdataARecord by calling from_dict on the json representation
        resource_record_update_input_rdata_rdata_a_record_model = ResourceRecordUpdateInputRdataRdataARecord.from_dict(resource_record_update_input_rdata_rdata_a_record_model_json)
        assert resource_record_update_input_rdata_rdata_a_record_model != False

        # Construct a model instance of ResourceRecordUpdateInputRdataRdataARecord by calling from_dict on the json representation
        resource_record_update_input_rdata_rdata_a_record_model_dict = ResourceRecordUpdateInputRdataRdataARecord.from_dict(resource_record_update_input_rdata_rdata_a_record_model_json).__dict__
        resource_record_update_input_rdata_rdata_a_record_model2 = ResourceRecordUpdateInputRdataRdataARecord(**resource_record_update_input_rdata_rdata_a_record_model_dict)

        # Verify the model instances are equivalent
        assert resource_record_update_input_rdata_rdata_a_record_model == resource_record_update_input_rdata_rdata_a_record_model2

        # Convert model instance back to dict and verify no loss of data
        resource_record_update_input_rdata_rdata_a_record_model_json2 = resource_record_update_input_rdata_rdata_a_record_model.to_dict()
        assert resource_record_update_input_rdata_rdata_a_record_model_json2 == resource_record_update_input_rdata_rdata_a_record_model_json

class TestModel_ResourceRecordUpdateInputRdataRdataAaaaRecord():
    """
    Test Class for ResourceRecordUpdateInputRdataRdataAaaaRecord
    """

    def test_resource_record_update_input_rdata_rdata_aaaa_record_serialization(self):
        """
        Test serialization/deserialization for ResourceRecordUpdateInputRdataRdataAaaaRecord
        """

        # Construct a json representation of a ResourceRecordUpdateInputRdataRdataAaaaRecord model
        resource_record_update_input_rdata_rdata_aaaa_record_model_json = {}
        resource_record_update_input_rdata_rdata_aaaa_record_model_json['ip'] = '2019::2019'

        # Construct a model instance of ResourceRecordUpdateInputRdataRdataAaaaRecord by calling from_dict on the json representation
        resource_record_update_input_rdata_rdata_aaaa_record_model = ResourceRecordUpdateInputRdataRdataAaaaRecord.from_dict(resource_record_update_input_rdata_rdata_aaaa_record_model_json)
        assert resource_record_update_input_rdata_rdata_aaaa_record_model != False

        # Construct a model instance of ResourceRecordUpdateInputRdataRdataAaaaRecord by calling from_dict on the json representation
        resource_record_update_input_rdata_rdata_aaaa_record_model_dict = ResourceRecordUpdateInputRdataRdataAaaaRecord.from_dict(resource_record_update_input_rdata_rdata_aaaa_record_model_json).__dict__
        resource_record_update_input_rdata_rdata_aaaa_record_model2 = ResourceRecordUpdateInputRdataRdataAaaaRecord(**resource_record_update_input_rdata_rdata_aaaa_record_model_dict)

        # Verify the model instances are equivalent
        assert resource_record_update_input_rdata_rdata_aaaa_record_model == resource_record_update_input_rdata_rdata_aaaa_record_model2

        # Convert model instance back to dict and verify no loss of data
        resource_record_update_input_rdata_rdata_aaaa_record_model_json2 = resource_record_update_input_rdata_rdata_aaaa_record_model.to_dict()
        assert resource_record_update_input_rdata_rdata_aaaa_record_model_json2 == resource_record_update_input_rdata_rdata_aaaa_record_model_json

class TestModel_ResourceRecordUpdateInputRdataRdataCnameRecord():
    """
    Test Class for ResourceRecordUpdateInputRdataRdataCnameRecord
    """

    def test_resource_record_update_input_rdata_rdata_cname_record_serialization(self):
        """
        Test serialization/deserialization for ResourceRecordUpdateInputRdataRdataCnameRecord
        """

        # Construct a json representation of a ResourceRecordUpdateInputRdataRdataCnameRecord model
        resource_record_update_input_rdata_rdata_cname_record_model_json = {}
        resource_record_update_input_rdata_rdata_cname_record_model_json['cname'] = 'www.example.com'

        # Construct a model instance of ResourceRecordUpdateInputRdataRdataCnameRecord by calling from_dict on the json representation
        resource_record_update_input_rdata_rdata_cname_record_model = ResourceRecordUpdateInputRdataRdataCnameRecord.from_dict(resource_record_update_input_rdata_rdata_cname_record_model_json)
        assert resource_record_update_input_rdata_rdata_cname_record_model != False

        # Construct a model instance of ResourceRecordUpdateInputRdataRdataCnameRecord by calling from_dict on the json representation
        resource_record_update_input_rdata_rdata_cname_record_model_dict = ResourceRecordUpdateInputRdataRdataCnameRecord.from_dict(resource_record_update_input_rdata_rdata_cname_record_model_json).__dict__
        resource_record_update_input_rdata_rdata_cname_record_model2 = ResourceRecordUpdateInputRdataRdataCnameRecord(**resource_record_update_input_rdata_rdata_cname_record_model_dict)

        # Verify the model instances are equivalent
        assert resource_record_update_input_rdata_rdata_cname_record_model == resource_record_update_input_rdata_rdata_cname_record_model2

        # Convert model instance back to dict and verify no loss of data
        resource_record_update_input_rdata_rdata_cname_record_model_json2 = resource_record_update_input_rdata_rdata_cname_record_model.to_dict()
        assert resource_record_update_input_rdata_rdata_cname_record_model_json2 == resource_record_update_input_rdata_rdata_cname_record_model_json

class TestModel_ResourceRecordUpdateInputRdataRdataMxRecord():
    """
    Test Class for ResourceRecordUpdateInputRdataRdataMxRecord
    """

    def test_resource_record_update_input_rdata_rdata_mx_record_serialization(self):
        """
        Test serialization/deserialization for ResourceRecordUpdateInputRdataRdataMxRecord
        """

        # Construct a json representation of a ResourceRecordUpdateInputRdataRdataMxRecord model
        resource_record_update_input_rdata_rdata_mx_record_model_json = {}
        resource_record_update_input_rdata_rdata_mx_record_model_json['exchange'] = 'mail.example.com'
        resource_record_update_input_rdata_rdata_mx_record_model_json['preference'] = 10

        # Construct a model instance of ResourceRecordUpdateInputRdataRdataMxRecord by calling from_dict on the json representation
        resource_record_update_input_rdata_rdata_mx_record_model = ResourceRecordUpdateInputRdataRdataMxRecord.from_dict(resource_record_update_input_rdata_rdata_mx_record_model_json)
        assert resource_record_update_input_rdata_rdata_mx_record_model != False

        # Construct a model instance of ResourceRecordUpdateInputRdataRdataMxRecord by calling from_dict on the json representation
        resource_record_update_input_rdata_rdata_mx_record_model_dict = ResourceRecordUpdateInputRdataRdataMxRecord.from_dict(resource_record_update_input_rdata_rdata_mx_record_model_json).__dict__
        resource_record_update_input_rdata_rdata_mx_record_model2 = ResourceRecordUpdateInputRdataRdataMxRecord(**resource_record_update_input_rdata_rdata_mx_record_model_dict)

        # Verify the model instances are equivalent
        assert resource_record_update_input_rdata_rdata_mx_record_model == resource_record_update_input_rdata_rdata_mx_record_model2

        # Convert model instance back to dict and verify no loss of data
        resource_record_update_input_rdata_rdata_mx_record_model_json2 = resource_record_update_input_rdata_rdata_mx_record_model.to_dict()
        assert resource_record_update_input_rdata_rdata_mx_record_model_json2 == resource_record_update_input_rdata_rdata_mx_record_model_json

class TestModel_ResourceRecordUpdateInputRdataRdataPtrRecord():
    """
    Test Class for ResourceRecordUpdateInputRdataRdataPtrRecord
    """

    def test_resource_record_update_input_rdata_rdata_ptr_record_serialization(self):
        """
        Test serialization/deserialization for ResourceRecordUpdateInputRdataRdataPtrRecord
        """

        # Construct a json representation of a ResourceRecordUpdateInputRdataRdataPtrRecord model
        resource_record_update_input_rdata_rdata_ptr_record_model_json = {}
        resource_record_update_input_rdata_rdata_ptr_record_model_json['ptrdname'] = 'www.example.com'

        # Construct a model instance of ResourceRecordUpdateInputRdataRdataPtrRecord by calling from_dict on the json representation
        resource_record_update_input_rdata_rdata_ptr_record_model = ResourceRecordUpdateInputRdataRdataPtrRecord.from_dict(resource_record_update_input_rdata_rdata_ptr_record_model_json)
        assert resource_record_update_input_rdata_rdata_ptr_record_model != False

        # Construct a model instance of ResourceRecordUpdateInputRdataRdataPtrRecord by calling from_dict on the json representation
        resource_record_update_input_rdata_rdata_ptr_record_model_dict = ResourceRecordUpdateInputRdataRdataPtrRecord.from_dict(resource_record_update_input_rdata_rdata_ptr_record_model_json).__dict__
        resource_record_update_input_rdata_rdata_ptr_record_model2 = ResourceRecordUpdateInputRdataRdataPtrRecord(**resource_record_update_input_rdata_rdata_ptr_record_model_dict)

        # Verify the model instances are equivalent
        assert resource_record_update_input_rdata_rdata_ptr_record_model == resource_record_update_input_rdata_rdata_ptr_record_model2

        # Convert model instance back to dict and verify no loss of data
        resource_record_update_input_rdata_rdata_ptr_record_model_json2 = resource_record_update_input_rdata_rdata_ptr_record_model.to_dict()
        assert resource_record_update_input_rdata_rdata_ptr_record_model_json2 == resource_record_update_input_rdata_rdata_ptr_record_model_json

class TestModel_ResourceRecordUpdateInputRdataRdataSrvRecord():
    """
    Test Class for ResourceRecordUpdateInputRdataRdataSrvRecord
    """

    def test_resource_record_update_input_rdata_rdata_srv_record_serialization(self):
        """
        Test serialization/deserialization for ResourceRecordUpdateInputRdataRdataSrvRecord
        """

        # Construct a json representation of a ResourceRecordUpdateInputRdataRdataSrvRecord model
        resource_record_update_input_rdata_rdata_srv_record_model_json = {}
        resource_record_update_input_rdata_rdata_srv_record_model_json['port'] = 80
        resource_record_update_input_rdata_rdata_srv_record_model_json['priority'] = 10
        resource_record_update_input_rdata_rdata_srv_record_model_json['target'] = 'www.example.com'
        resource_record_update_input_rdata_rdata_srv_record_model_json['weight'] = 10

        # Construct a model instance of ResourceRecordUpdateInputRdataRdataSrvRecord by calling from_dict on the json representation
        resource_record_update_input_rdata_rdata_srv_record_model = ResourceRecordUpdateInputRdataRdataSrvRecord.from_dict(resource_record_update_input_rdata_rdata_srv_record_model_json)
        assert resource_record_update_input_rdata_rdata_srv_record_model != False

        # Construct a model instance of ResourceRecordUpdateInputRdataRdataSrvRecord by calling from_dict on the json representation
        resource_record_update_input_rdata_rdata_srv_record_model_dict = ResourceRecordUpdateInputRdataRdataSrvRecord.from_dict(resource_record_update_input_rdata_rdata_srv_record_model_json).__dict__
        resource_record_update_input_rdata_rdata_srv_record_model2 = ResourceRecordUpdateInputRdataRdataSrvRecord(**resource_record_update_input_rdata_rdata_srv_record_model_dict)

        # Verify the model instances are equivalent
        assert resource_record_update_input_rdata_rdata_srv_record_model == resource_record_update_input_rdata_rdata_srv_record_model2

        # Convert model instance back to dict and verify no loss of data
        resource_record_update_input_rdata_rdata_srv_record_model_json2 = resource_record_update_input_rdata_rdata_srv_record_model.to_dict()
        assert resource_record_update_input_rdata_rdata_srv_record_model_json2 == resource_record_update_input_rdata_rdata_srv_record_model_json

class TestModel_ResourceRecordUpdateInputRdataRdataTxtRecord():
    """
    Test Class for ResourceRecordUpdateInputRdataRdataTxtRecord
    """

    def test_resource_record_update_input_rdata_rdata_txt_record_serialization(self):
        """
        Test serialization/deserialization for ResourceRecordUpdateInputRdataRdataTxtRecord
        """

        # Construct a json representation of a ResourceRecordUpdateInputRdataRdataTxtRecord model
        resource_record_update_input_rdata_rdata_txt_record_model_json = {}
        resource_record_update_input_rdata_rdata_txt_record_model_json['text'] = 'This is a text record'

        # Construct a model instance of ResourceRecordUpdateInputRdataRdataTxtRecord by calling from_dict on the json representation
        resource_record_update_input_rdata_rdata_txt_record_model = ResourceRecordUpdateInputRdataRdataTxtRecord.from_dict(resource_record_update_input_rdata_rdata_txt_record_model_json)
        assert resource_record_update_input_rdata_rdata_txt_record_model != False

        # Construct a model instance of ResourceRecordUpdateInputRdataRdataTxtRecord by calling from_dict on the json representation
        resource_record_update_input_rdata_rdata_txt_record_model_dict = ResourceRecordUpdateInputRdataRdataTxtRecord.from_dict(resource_record_update_input_rdata_rdata_txt_record_model_json).__dict__
        resource_record_update_input_rdata_rdata_txt_record_model2 = ResourceRecordUpdateInputRdataRdataTxtRecord(**resource_record_update_input_rdata_rdata_txt_record_model_dict)

        # Verify the model instances are equivalent
        assert resource_record_update_input_rdata_rdata_txt_record_model == resource_record_update_input_rdata_rdata_txt_record_model2

        # Convert model instance back to dict and verify no loss of data
        resource_record_update_input_rdata_rdata_txt_record_model_json2 = resource_record_update_input_rdata_rdata_txt_record_model.to_dict()
        assert resource_record_update_input_rdata_rdata_txt_record_model_json2 == resource_record_update_input_rdata_rdata_txt_record_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
