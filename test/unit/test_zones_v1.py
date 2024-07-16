# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2024.
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
Unit Tests for ZonesV1
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
from ibm_cloud_networking_services.zones_v1 import *

crn = 'testString'

_service = ZonesV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn,
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
    return re.compile(request_url.rstrip('/') + '/+')


##############################################################################
# Start of Service: CISZones
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

        service = ZonesV1.new_instance(
            crn=crn,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, ZonesV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = ZonesV1.new_instance(
                crn=crn,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = ZonesV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='crn must be provided'):
            service = ZonesV1.new_instance(
                crn=None,
            )


class TestListZones:
    """
    Test Class for list_zones
    """

    @responses.activate
    def test_list_zones_all_params(self):
        """
        list_zones()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "test-example.com", "original_registrar": "GoDaddy", "original_dnshost": "NameCheap", "status": "active", "paused": false, "original_name_servers": ["ns1.originaldnshost.com"], "name_servers": ["ns001.name.cloud.ibm.com"], "type": "full", "verification_key": "476754457-428595283", "cname_suffix": "cdn.cloudflare.net"}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        page = 1
        per_page = 20

        # Invoke method
        response = _service.list_zones(
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
        assert 'page={}'.format(page) in query_string
        assert 'per_page={}'.format(per_page) in query_string

    def test_list_zones_all_params_with_retries(self):
        # Enable retries and run test_list_zones_all_params.
        _service.enable_retries()
        self.test_list_zones_all_params()

        # Disable retries and run test_list_zones_all_params.
        _service.disable_retries()
        self.test_list_zones_all_params()

    @responses.activate
    def test_list_zones_required_params(self):
        """
        test_list_zones_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "test-example.com", "original_registrar": "GoDaddy", "original_dnshost": "NameCheap", "status": "active", "paused": false, "original_name_servers": ["ns1.originaldnshost.com"], "name_servers": ["ns001.name.cloud.ibm.com"], "type": "full", "verification_key": "476754457-428595283", "cname_suffix": "cdn.cloudflare.net"}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_zones()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_zones_required_params_with_retries(self):
        # Enable retries and run test_list_zones_required_params.
        _service.enable_retries()
        self.test_list_zones_required_params()

        # Disable retries and run test_list_zones_required_params.
        _service.disable_retries()
        self.test_list_zones_required_params()

    @responses.activate
    def test_list_zones_value_error(self):
        """
        test_list_zones_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "test-example.com", "original_registrar": "GoDaddy", "original_dnshost": "NameCheap", "status": "active", "paused": false, "original_name_servers": ["ns1.originaldnshost.com"], "name_servers": ["ns001.name.cloud.ibm.com"], "type": "full", "verification_key": "476754457-428595283", "cname_suffix": "cdn.cloudflare.net"}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
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
                _service.list_zones(**req_copy)

    def test_list_zones_value_error_with_retries(self):
        # Enable retries and run test_list_zones_value_error.
        _service.enable_retries()
        self.test_list_zones_value_error()

        # Disable retries and run test_list_zones_value_error.
        _service.disable_retries()
        self.test_list_zones_value_error()


class TestCreateZone:
    """
    Test Class for create_zone
    """

    @responses.activate
    def test_create_zone_all_params(self):
        """
        create_zone()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "test-example.com", "original_registrar": "GoDaddy", "original_dnshost": "NameCheap", "status": "active", "paused": false, "original_name_servers": ["ns1.originaldnshost.com"], "name_servers": ["ns001.name.cloud.ibm.com"], "type": "full", "verification_key": "476754457-428595283", "cname_suffix": "cdn.cloudflare.net"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        name = 'test-example.com'
        type = 'full'

        # Invoke method
        response = _service.create_zone(
            name=name,
            type=type,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'test-example.com'
        assert req_body['type'] == 'full'

    def test_create_zone_all_params_with_retries(self):
        # Enable retries and run test_create_zone_all_params.
        _service.enable_retries()
        self.test_create_zone_all_params()

        # Disable retries and run test_create_zone_all_params.
        _service.disable_retries()
        self.test_create_zone_all_params()

    @responses.activate
    def test_create_zone_required_params(self):
        """
        test_create_zone_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "test-example.com", "original_registrar": "GoDaddy", "original_dnshost": "NameCheap", "status": "active", "paused": false, "original_name_servers": ["ns1.originaldnshost.com"], "name_servers": ["ns001.name.cloud.ibm.com"], "type": "full", "verification_key": "476754457-428595283", "cname_suffix": "cdn.cloudflare.net"}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.create_zone()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_zone_required_params_with_retries(self):
        # Enable retries and run test_create_zone_required_params.
        _service.enable_retries()
        self.test_create_zone_required_params()

        # Disable retries and run test_create_zone_required_params.
        _service.disable_retries()
        self.test_create_zone_required_params()

    @responses.activate
    def test_create_zone_value_error(self):
        """
        test_create_zone_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "test-example.com", "original_registrar": "GoDaddy", "original_dnshost": "NameCheap", "status": "active", "paused": false, "original_name_servers": ["ns1.originaldnshost.com"], "name_servers": ["ns001.name.cloud.ibm.com"], "type": "full", "verification_key": "476754457-428595283", "cname_suffix": "cdn.cloudflare.net"}}'
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
                _service.create_zone(**req_copy)

    def test_create_zone_value_error_with_retries(self):
        # Enable retries and run test_create_zone_value_error.
        _service.enable_retries()
        self.test_create_zone_value_error()

        # Disable retries and run test_create_zone_value_error.
        _service.disable_retries()
        self.test_create_zone_value_error()


class TestDeleteZone:
    """
    Test Class for delete_zone
    """

    @responses.activate
    def test_delete_zone_all_params(self):
        """
        delete_zone()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc"}}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_identifier = 'testString'

        # Invoke method
        response = _service.delete_zone(
            zone_identifier,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_zone_all_params_with_retries(self):
        # Enable retries and run test_delete_zone_all_params.
        _service.enable_retries()
        self.test_delete_zone_all_params()

        # Disable retries and run test_delete_zone_all_params.
        _service.disable_retries()
        self.test_delete_zone_all_params()

    @responses.activate
    def test_delete_zone_value_error(self):
        """
        test_delete_zone_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc"}}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "zone_identifier": zone_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_zone(**req_copy)

    def test_delete_zone_value_error_with_retries(self):
        # Enable retries and run test_delete_zone_value_error.
        _service.enable_retries()
        self.test_delete_zone_value_error()

        # Disable retries and run test_delete_zone_value_error.
        _service.disable_retries()
        self.test_delete_zone_value_error()


class TestGetZone:
    """
    Test Class for get_zone
    """

    @responses.activate
    def test_get_zone_all_params(self):
        """
        get_zone()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "test-example.com", "original_registrar": "GoDaddy", "original_dnshost": "NameCheap", "status": "active", "paused": false, "original_name_servers": ["ns1.originaldnshost.com"], "name_servers": ["ns001.name.cloud.ibm.com"], "type": "full", "verification_key": "476754457-428595283", "cname_suffix": "cdn.cloudflare.net"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_identifier = 'testString'

        # Invoke method
        response = _service.get_zone(
            zone_identifier,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_zone_all_params_with_retries(self):
        # Enable retries and run test_get_zone_all_params.
        _service.enable_retries()
        self.test_get_zone_all_params()

        # Disable retries and run test_get_zone_all_params.
        _service.disable_retries()
        self.test_get_zone_all_params()

    @responses.activate
    def test_get_zone_value_error(self):
        """
        test_get_zone_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "test-example.com", "original_registrar": "GoDaddy", "original_dnshost": "NameCheap", "status": "active", "paused": false, "original_name_servers": ["ns1.originaldnshost.com"], "name_servers": ["ns001.name.cloud.ibm.com"], "type": "full", "verification_key": "476754457-428595283", "cname_suffix": "cdn.cloudflare.net"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "zone_identifier": zone_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_zone(**req_copy)

    def test_get_zone_value_error_with_retries(self):
        # Enable retries and run test_get_zone_value_error.
        _service.enable_retries()
        self.test_get_zone_value_error()

        # Disable retries and run test_get_zone_value_error.
        _service.disable_retries()
        self.test_get_zone_value_error()


class TestUpdateZone:
    """
    Test Class for update_zone
    """

    @responses.activate
    def test_update_zone_all_params(self):
        """
        update_zone()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "test-example.com", "original_registrar": "GoDaddy", "original_dnshost": "NameCheap", "status": "active", "paused": false, "original_name_servers": ["ns1.originaldnshost.com"], "name_servers": ["ns001.name.cloud.ibm.com"], "type": "full", "verification_key": "476754457-428595283", "cname_suffix": "cdn.cloudflare.net"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_identifier = 'testString'
        paused = False

        # Invoke method
        response = _service.update_zone(
            zone_identifier,
            paused=paused,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['paused'] == False

    def test_update_zone_all_params_with_retries(self):
        # Enable retries and run test_update_zone_all_params.
        _service.enable_retries()
        self.test_update_zone_all_params()

        # Disable retries and run test_update_zone_all_params.
        _service.disable_retries()
        self.test_update_zone_all_params()

    @responses.activate
    def test_update_zone_required_params(self):
        """
        test_update_zone_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "test-example.com", "original_registrar": "GoDaddy", "original_dnshost": "NameCheap", "status": "active", "paused": false, "original_name_servers": ["ns1.originaldnshost.com"], "name_servers": ["ns001.name.cloud.ibm.com"], "type": "full", "verification_key": "476754457-428595283", "cname_suffix": "cdn.cloudflare.net"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_identifier = 'testString'

        # Invoke method
        response = _service.update_zone(
            zone_identifier,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_zone_required_params_with_retries(self):
        # Enable retries and run test_update_zone_required_params.
        _service.enable_retries()
        self.test_update_zone_required_params()

        # Disable retries and run test_update_zone_required_params.
        _service.disable_retries()
        self.test_update_zone_required_params()

    @responses.activate
    def test_update_zone_value_error(self):
        """
        test_update_zone_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "test-example.com", "original_registrar": "GoDaddy", "original_dnshost": "NameCheap", "status": "active", "paused": false, "original_name_servers": ["ns1.originaldnshost.com"], "name_servers": ["ns001.name.cloud.ibm.com"], "type": "full", "verification_key": "476754457-428595283", "cname_suffix": "cdn.cloudflare.net"}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "zone_identifier": zone_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_zone(**req_copy)

    def test_update_zone_value_error_with_retries(self):
        # Enable retries and run test_update_zone_value_error.
        _service.enable_retries()
        self.test_update_zone_value_error()

        # Disable retries and run test_update_zone_value_error.
        _service.disable_retries()
        self.test_update_zone_value_error()


class TestZoneActivationCheck:
    """
    Test Class for zone_activation_check
    """

    @responses.activate
    def test_zone_activation_check_all_params(self):
        """
        zone_activation_check()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/activation_check')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc"}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_identifier = 'testString'

        # Invoke method
        response = _service.zone_activation_check(
            zone_identifier,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_zone_activation_check_all_params_with_retries(self):
        # Enable retries and run test_zone_activation_check_all_params.
        _service.enable_retries()
        self.test_zone_activation_check_all_params()

        # Disable retries and run test_zone_activation_check_all_params.
        _service.disable_retries()
        self.test_zone_activation_check_all_params()

    @responses.activate
    def test_zone_activation_check_value_error(self):
        """
        test_zone_activation_check_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/activation_check')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc"}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        zone_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "zone_identifier": zone_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.zone_activation_check(**req_copy)

    def test_zone_activation_check_value_error_with_retries(self):
        # Enable retries and run test_zone_activation_check_value_error.
        _service.enable_retries()
        self.test_zone_activation_check_value_error()

        # Disable retries and run test_zone_activation_check_value_error.
        _service.disable_retries()
        self.test_zone_activation_check_value_error()


# endregion
##############################################################################
# End of Service: CISZones
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_DeleteZoneRespResult:
    """
    Test Class for DeleteZoneRespResult
    """

    def test_delete_zone_resp_result_serialization(self):
        """
        Test serialization/deserialization for DeleteZoneRespResult
        """

        # Construct a json representation of a DeleteZoneRespResult model
        delete_zone_resp_result_model_json = {}
        delete_zone_resp_result_model_json['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'

        # Construct a model instance of DeleteZoneRespResult by calling from_dict on the json representation
        delete_zone_resp_result_model = DeleteZoneRespResult.from_dict(delete_zone_resp_result_model_json)
        assert delete_zone_resp_result_model != False

        # Construct a model instance of DeleteZoneRespResult by calling from_dict on the json representation
        delete_zone_resp_result_model_dict = DeleteZoneRespResult.from_dict(delete_zone_resp_result_model_json).__dict__
        delete_zone_resp_result_model2 = DeleteZoneRespResult(**delete_zone_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert delete_zone_resp_result_model == delete_zone_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        delete_zone_resp_result_model_json2 = delete_zone_resp_result_model.to_dict()
        assert delete_zone_resp_result_model_json2 == delete_zone_resp_result_model_json


class TestModel_ZoneActivationcheckRespResult:
    """
    Test Class for ZoneActivationcheckRespResult
    """

    def test_zone_activationcheck_resp_result_serialization(self):
        """
        Test serialization/deserialization for ZoneActivationcheckRespResult
        """

        # Construct a json representation of a ZoneActivationcheckRespResult model
        zone_activationcheck_resp_result_model_json = {}
        zone_activationcheck_resp_result_model_json['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'

        # Construct a model instance of ZoneActivationcheckRespResult by calling from_dict on the json representation
        zone_activationcheck_resp_result_model = ZoneActivationcheckRespResult.from_dict(zone_activationcheck_resp_result_model_json)
        assert zone_activationcheck_resp_result_model != False

        # Construct a model instance of ZoneActivationcheckRespResult by calling from_dict on the json representation
        zone_activationcheck_resp_result_model_dict = ZoneActivationcheckRespResult.from_dict(zone_activationcheck_resp_result_model_json).__dict__
        zone_activationcheck_resp_result_model2 = ZoneActivationcheckRespResult(**zone_activationcheck_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert zone_activationcheck_resp_result_model == zone_activationcheck_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        zone_activationcheck_resp_result_model_json2 = zone_activationcheck_resp_result_model.to_dict()
        assert zone_activationcheck_resp_result_model_json2 == zone_activationcheck_resp_result_model_json


class TestModel_DeleteZoneResp:
    """
    Test Class for DeleteZoneResp
    """

    def test_delete_zone_resp_serialization(self):
        """
        Test serialization/deserialization for DeleteZoneResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        delete_zone_resp_result_model = {}  # DeleteZoneRespResult
        delete_zone_resp_result_model['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'

        # Construct a json representation of a DeleteZoneResp model
        delete_zone_resp_model_json = {}
        delete_zone_resp_model_json['success'] = True
        delete_zone_resp_model_json['errors'] = [['testString']]
        delete_zone_resp_model_json['messages'] = [['testString']]
        delete_zone_resp_model_json['result'] = delete_zone_resp_result_model

        # Construct a model instance of DeleteZoneResp by calling from_dict on the json representation
        delete_zone_resp_model = DeleteZoneResp.from_dict(delete_zone_resp_model_json)
        assert delete_zone_resp_model != False

        # Construct a model instance of DeleteZoneResp by calling from_dict on the json representation
        delete_zone_resp_model_dict = DeleteZoneResp.from_dict(delete_zone_resp_model_json).__dict__
        delete_zone_resp_model2 = DeleteZoneResp(**delete_zone_resp_model_dict)

        # Verify the model instances are equivalent
        assert delete_zone_resp_model == delete_zone_resp_model2

        # Convert model instance back to dict and verify no loss of data
        delete_zone_resp_model_json2 = delete_zone_resp_model.to_dict()
        assert delete_zone_resp_model_json2 == delete_zone_resp_model_json


class TestModel_ListZonesResp:
    """
    Test Class for ListZonesResp
    """

    def test_list_zones_resp_serialization(self):
        """
        Test serialization/deserialization for ListZonesResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        zone_details_model = {}  # ZoneDetails
        zone_details_model['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        zone_details_model['created_on'] = '2014-01-01T05:20:00.12345Z'
        zone_details_model['modified_on'] = '2014-01-01T05:20:00.12345Z'
        zone_details_model['name'] = 'test-example.com'
        zone_details_model['original_registrar'] = 'GoDaddy'
        zone_details_model['original_dnshost'] = 'NameCheap'
        zone_details_model['status'] = 'active'
        zone_details_model['paused'] = False
        zone_details_model['original_name_servers'] = ['ns1.originaldnshost.com']
        zone_details_model['name_servers'] = ['ns001.name.cloud.ibm.com']
        zone_details_model['type'] = 'full'
        zone_details_model['verification_key'] = '476754457-428595283'
        zone_details_model['cname_suffix'] = 'cdn.cloudflare.net'

        result_info_model = {}  # ResultInfo
        result_info_model['page'] = 1
        result_info_model['per_page'] = 20
        result_info_model['count'] = 1
        result_info_model['total_count'] = 2000

        # Construct a json representation of a ListZonesResp model
        list_zones_resp_model_json = {}
        list_zones_resp_model_json['success'] = True
        list_zones_resp_model_json['errors'] = [['testString']]
        list_zones_resp_model_json['messages'] = [['testString']]
        list_zones_resp_model_json['result'] = [zone_details_model]
        list_zones_resp_model_json['result_info'] = result_info_model

        # Construct a model instance of ListZonesResp by calling from_dict on the json representation
        list_zones_resp_model = ListZonesResp.from_dict(list_zones_resp_model_json)
        assert list_zones_resp_model != False

        # Construct a model instance of ListZonesResp by calling from_dict on the json representation
        list_zones_resp_model_dict = ListZonesResp.from_dict(list_zones_resp_model_json).__dict__
        list_zones_resp_model2 = ListZonesResp(**list_zones_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_zones_resp_model == list_zones_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_zones_resp_model_json2 = list_zones_resp_model.to_dict()
        assert list_zones_resp_model_json2 == list_zones_resp_model_json


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
        result_info_model_json['page'] = 1
        result_info_model_json['per_page'] = 20
        result_info_model_json['count'] = 1
        result_info_model_json['total_count'] = 2000

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


class TestModel_ZoneActivationcheckResp:
    """
    Test Class for ZoneActivationcheckResp
    """

    def test_zone_activationcheck_resp_serialization(self):
        """
        Test serialization/deserialization for ZoneActivationcheckResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        zone_activationcheck_resp_result_model = {}  # ZoneActivationcheckRespResult
        zone_activationcheck_resp_result_model['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'

        # Construct a json representation of a ZoneActivationcheckResp model
        zone_activationcheck_resp_model_json = {}
        zone_activationcheck_resp_model_json['success'] = True
        zone_activationcheck_resp_model_json['errors'] = [['testString']]
        zone_activationcheck_resp_model_json['messages'] = [['testString']]
        zone_activationcheck_resp_model_json['result'] = zone_activationcheck_resp_result_model

        # Construct a model instance of ZoneActivationcheckResp by calling from_dict on the json representation
        zone_activationcheck_resp_model = ZoneActivationcheckResp.from_dict(zone_activationcheck_resp_model_json)
        assert zone_activationcheck_resp_model != False

        # Construct a model instance of ZoneActivationcheckResp by calling from_dict on the json representation
        zone_activationcheck_resp_model_dict = ZoneActivationcheckResp.from_dict(zone_activationcheck_resp_model_json).__dict__
        zone_activationcheck_resp_model2 = ZoneActivationcheckResp(**zone_activationcheck_resp_model_dict)

        # Verify the model instances are equivalent
        assert zone_activationcheck_resp_model == zone_activationcheck_resp_model2

        # Convert model instance back to dict and verify no loss of data
        zone_activationcheck_resp_model_json2 = zone_activationcheck_resp_model.to_dict()
        assert zone_activationcheck_resp_model_json2 == zone_activationcheck_resp_model_json


class TestModel_ZoneDetails:
    """
    Test Class for ZoneDetails
    """

    def test_zone_details_serialization(self):
        """
        Test serialization/deserialization for ZoneDetails
        """

        # Construct a json representation of a ZoneDetails model
        zone_details_model_json = {}
        zone_details_model_json['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        zone_details_model_json['created_on'] = '2014-01-01T05:20:00.12345Z'
        zone_details_model_json['modified_on'] = '2014-01-01T05:20:00.12345Z'
        zone_details_model_json['name'] = 'test-example.com'
        zone_details_model_json['original_registrar'] = 'GoDaddy'
        zone_details_model_json['original_dnshost'] = 'NameCheap'
        zone_details_model_json['status'] = 'active'
        zone_details_model_json['paused'] = False
        zone_details_model_json['original_name_servers'] = ['ns1.originaldnshost.com']
        zone_details_model_json['name_servers'] = ['ns001.name.cloud.ibm.com']
        zone_details_model_json['type'] = 'full'
        zone_details_model_json['verification_key'] = '476754457-428595283'
        zone_details_model_json['cname_suffix'] = 'cdn.cloudflare.net'

        # Construct a model instance of ZoneDetails by calling from_dict on the json representation
        zone_details_model = ZoneDetails.from_dict(zone_details_model_json)
        assert zone_details_model != False

        # Construct a model instance of ZoneDetails by calling from_dict on the json representation
        zone_details_model_dict = ZoneDetails.from_dict(zone_details_model_json).__dict__
        zone_details_model2 = ZoneDetails(**zone_details_model_dict)

        # Verify the model instances are equivalent
        assert zone_details_model == zone_details_model2

        # Convert model instance back to dict and verify no loss of data
        zone_details_model_json2 = zone_details_model.to_dict()
        assert zone_details_model_json2 == zone_details_model_json


class TestModel_ZoneResp:
    """
    Test Class for ZoneResp
    """

    def test_zone_resp_serialization(self):
        """
        Test serialization/deserialization for ZoneResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        zone_details_model = {}  # ZoneDetails
        zone_details_model['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        zone_details_model['created_on'] = '2014-01-01T05:20:00.12345Z'
        zone_details_model['modified_on'] = '2014-01-01T05:20:00.12345Z'
        zone_details_model['name'] = 'test-example.com'
        zone_details_model['original_registrar'] = 'GoDaddy'
        zone_details_model['original_dnshost'] = 'NameCheap'
        zone_details_model['status'] = 'active'
        zone_details_model['paused'] = False
        zone_details_model['original_name_servers'] = ['ns1.originaldnshost.com']
        zone_details_model['name_servers'] = ['ns001.name.cloud.ibm.com']
        zone_details_model['type'] = 'full'
        zone_details_model['verification_key'] = '476754457-428595283'
        zone_details_model['cname_suffix'] = 'cdn.cloudflare.net'

        # Construct a json representation of a ZoneResp model
        zone_resp_model_json = {}
        zone_resp_model_json['success'] = True
        zone_resp_model_json['errors'] = [['testString']]
        zone_resp_model_json['messages'] = [['testString']]
        zone_resp_model_json['result'] = zone_details_model

        # Construct a model instance of ZoneResp by calling from_dict on the json representation
        zone_resp_model = ZoneResp.from_dict(zone_resp_model_json)
        assert zone_resp_model != False

        # Construct a model instance of ZoneResp by calling from_dict on the json representation
        zone_resp_model_dict = ZoneResp.from_dict(zone_resp_model_json).__dict__
        zone_resp_model2 = ZoneResp(**zone_resp_model_dict)

        # Verify the model instances are equivalent
        assert zone_resp_model == zone_resp_model2

        # Convert model instance back to dict and verify no loss of data
        zone_resp_model_json2 = zone_resp_model.to_dict()
        assert zone_resp_model_json2 == zone_resp_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
