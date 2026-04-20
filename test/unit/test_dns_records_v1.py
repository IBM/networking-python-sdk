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
Unit Tests for DnsRecordsV1
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
from ibm_cloud_networking_services.dns_records_v1 import *

crn = 'testString'
zone_identifier = 'testString'

_service = DnsRecordsV1(
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
# Start of Service: DNSRecords
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

        service = DnsRecordsV1.new_instance(
            crn=crn,
            zone_identifier=zone_identifier,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DnsRecordsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DnsRecordsV1.new_instance(
                crn=crn,
                zone_identifier=zone_identifier,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = DnsRecordsV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='crn must be provided'):
            service = DnsRecordsV1.new_instance(
                crn=None,
                zone_identifier=None,
            )


class TestListAllDnsRecords:
    """
    Test Class for list_all_dns_records
    """

    @responses.activate
    def test_list_all_dns_records_all_params(self):
        """
        list_all_dns_records()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/dns_records')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "169.154.10.10", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "zone_name": "test-example.com", "proxiable": true, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        type = 'testString'
        name = 'host1.test-example.com'
        content = '1.2.3.4'
        page = 1
        per_page = 20
        order = 'type'
        direction = 'asc'
        match = 'any'

        # Invoke method
        response = _service.list_all_dns_records(
            type=type,
            name=name,
            content=content,
            page=page,
            per_page=per_page,
            order=order,
            direction=direction,
            match=match,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'type={}'.format(type) in query_string
        assert 'name={}'.format(name) in query_string
        assert 'content={}'.format(content) in query_string
        assert 'page={}'.format(page) in query_string
        assert 'per_page={}'.format(per_page) in query_string
        assert 'order={}'.format(order) in query_string
        assert 'direction={}'.format(direction) in query_string
        assert 'match={}'.format(match) in query_string

    def test_list_all_dns_records_all_params_with_retries(self):
        # Enable retries and run test_list_all_dns_records_all_params.
        _service.enable_retries()
        self.test_list_all_dns_records_all_params()

        # Disable retries and run test_list_all_dns_records_all_params.
        _service.disable_retries()
        self.test_list_all_dns_records_all_params()

    @responses.activate
    def test_list_all_dns_records_required_params(self):
        """
        test_list_all_dns_records_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/dns_records')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "169.154.10.10", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "zone_name": "test-example.com", "proxiable": true, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_all_dns_records()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_all_dns_records_required_params_with_retries(self):
        # Enable retries and run test_list_all_dns_records_required_params.
        _service.enable_retries()
        self.test_list_all_dns_records_required_params()

        # Disable retries and run test_list_all_dns_records_required_params.
        _service.disable_retries()
        self.test_list_all_dns_records_required_params()

    @responses.activate
    def test_list_all_dns_records_value_error(self):
        """
        test_list_all_dns_records_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/dns_records')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "169.154.10.10", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "zone_name": "test-example.com", "proxiable": true, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}}], "result_info": {"page": 1, "per_page": 20, "count": 1, "total_count": 2000}}'
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
                _service.list_all_dns_records(**req_copy)

    def test_list_all_dns_records_value_error_with_retries(self):
        # Enable retries and run test_list_all_dns_records_value_error.
        _service.enable_retries()
        self.test_list_all_dns_records_value_error()

        # Disable retries and run test_list_all_dns_records_value_error.
        _service.disable_retries()
        self.test_list_all_dns_records_value_error()


class TestCreateDnsRecord:
    """
    Test Class for create_dns_record
    """

    @responses.activate
    def test_create_dns_record_all_params(self):
        """
        create_dns_record()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/dns_records')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "169.154.10.10", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "zone_name": "test-example.com", "proxiable": true, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        type = 'A'
        name = 'host-1.test-example.com'
        ttl = 120
        content = '1.2.3.4'
        priority = 5
        proxied = False
        data = {'anyKey': 'anyValue'}

        # Invoke method
        response = _service.create_dns_record(
            type=type,
            name=name,
            ttl=ttl,
            content=content,
            priority=priority,
            proxied=proxied,
            data=data,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'A'
        assert req_body['name'] == 'host-1.test-example.com'
        assert req_body['ttl'] == 120
        assert req_body['content'] == '1.2.3.4'
        assert req_body['priority'] == 5
        assert req_body['proxied'] == False
        assert req_body['data'] == {'anyKey': 'anyValue'}

    def test_create_dns_record_all_params_with_retries(self):
        # Enable retries and run test_create_dns_record_all_params.
        _service.enable_retries()
        self.test_create_dns_record_all_params()

        # Disable retries and run test_create_dns_record_all_params.
        _service.disable_retries()
        self.test_create_dns_record_all_params()

    @responses.activate
    def test_create_dns_record_required_params(self):
        """
        test_create_dns_record_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/dns_records')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "169.154.10.10", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "zone_name": "test-example.com", "proxiable": true, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.create_dns_record()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_create_dns_record_required_params_with_retries(self):
        # Enable retries and run test_create_dns_record_required_params.
        _service.enable_retries()
        self.test_create_dns_record_required_params()

        # Disable retries and run test_create_dns_record_required_params.
        _service.disable_retries()
        self.test_create_dns_record_required_params()

    @responses.activate
    def test_create_dns_record_value_error(self):
        """
        test_create_dns_record_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/dns_records')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "169.154.10.10", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "zone_name": "test-example.com", "proxiable": true, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}}}'
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
                _service.create_dns_record(**req_copy)

    def test_create_dns_record_value_error_with_retries(self):
        # Enable retries and run test_create_dns_record_value_error.
        _service.enable_retries()
        self.test_create_dns_record_value_error()

        # Disable retries and run test_create_dns_record_value_error.
        _service.disable_retries()
        self.test_create_dns_record_value_error()


class TestDeleteDnsRecord:
    """
    Test Class for delete_dns_record
    """

    @responses.activate
    def test_delete_dns_record_all_params(self):
        """
        delete_dns_record()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/dns_records/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc"}}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        dnsrecord_identifier = 'testString'

        # Invoke method
        response = _service.delete_dns_record(
            dnsrecord_identifier,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_dns_record_all_params_with_retries(self):
        # Enable retries and run test_delete_dns_record_all_params.
        _service.enable_retries()
        self.test_delete_dns_record_all_params()

        # Disable retries and run test_delete_dns_record_all_params.
        _service.disable_retries()
        self.test_delete_dns_record_all_params()

    @responses.activate
    def test_delete_dns_record_value_error(self):
        """
        test_delete_dns_record_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/dns_records/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc"}}'
        responses.add(
            responses.DELETE,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        dnsrecord_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "dnsrecord_identifier": dnsrecord_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_dns_record(**req_copy)

    def test_delete_dns_record_value_error_with_retries(self):
        # Enable retries and run test_delete_dns_record_value_error.
        _service.enable_retries()
        self.test_delete_dns_record_value_error()

        # Disable retries and run test_delete_dns_record_value_error.
        _service.disable_retries()
        self.test_delete_dns_record_value_error()


class TestGetDnsRecord:
    """
    Test Class for get_dns_record
    """

    @responses.activate
    def test_get_dns_record_all_params(self):
        """
        get_dns_record()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/dns_records/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "169.154.10.10", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "zone_name": "test-example.com", "proxiable": true, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        dnsrecord_identifier = 'testString'

        # Invoke method
        response = _service.get_dns_record(
            dnsrecord_identifier,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_dns_record_all_params_with_retries(self):
        # Enable retries and run test_get_dns_record_all_params.
        _service.enable_retries()
        self.test_get_dns_record_all_params()

        # Disable retries and run test_get_dns_record_all_params.
        _service.disable_retries()
        self.test_get_dns_record_all_params()

    @responses.activate
    def test_get_dns_record_value_error(self):
        """
        test_get_dns_record_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/dns_records/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "169.154.10.10", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "zone_name": "test-example.com", "proxiable": true, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        dnsrecord_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "dnsrecord_identifier": dnsrecord_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_dns_record(**req_copy)

    def test_get_dns_record_value_error_with_retries(self):
        # Enable retries and run test_get_dns_record_value_error.
        _service.enable_retries()
        self.test_get_dns_record_value_error()

        # Disable retries and run test_get_dns_record_value_error.
        _service.disable_retries()
        self.test_get_dns_record_value_error()


class TestUpdateDnsRecord:
    """
    Test Class for update_dns_record
    """

    @responses.activate
    def test_update_dns_record_all_params(self):
        """
        update_dns_record()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/dns_records/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "169.154.10.10", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "zone_name": "test-example.com", "proxiable": true, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        dnsrecord_identifier = 'testString'
        type = 'A'
        name = 'host-1.test-example.com'
        ttl = 120
        content = '1.2.3.4'
        priority = 5
        proxied = False
        data = {'anyKey': 'anyValue'}

        # Invoke method
        response = _service.update_dns_record(
            dnsrecord_identifier,
            type=type,
            name=name,
            ttl=ttl,
            content=content,
            priority=priority,
            proxied=proxied,
            data=data,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'A'
        assert req_body['name'] == 'host-1.test-example.com'
        assert req_body['ttl'] == 120
        assert req_body['content'] == '1.2.3.4'
        assert req_body['priority'] == 5
        assert req_body['proxied'] == False
        assert req_body['data'] == {'anyKey': 'anyValue'}

    def test_update_dns_record_all_params_with_retries(self):
        # Enable retries and run test_update_dns_record_all_params.
        _service.enable_retries()
        self.test_update_dns_record_all_params()

        # Disable retries and run test_update_dns_record_all_params.
        _service.disable_retries()
        self.test_update_dns_record_all_params()

    @responses.activate
    def test_update_dns_record_required_params(self):
        """
        test_update_dns_record_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/dns_records/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "169.154.10.10", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "zone_name": "test-example.com", "proxiable": true, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        dnsrecord_identifier = 'testString'

        # Invoke method
        response = _service.update_dns_record(
            dnsrecord_identifier,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_dns_record_required_params_with_retries(self):
        # Enable retries and run test_update_dns_record_required_params.
        _service.enable_retries()
        self.test_update_dns_record_required_params()

        # Disable retries and run test_update_dns_record_required_params.
        _service.disable_retries()
        self.test_update_dns_record_required_params()

    @responses.activate
    def test_update_dns_record_value_error(self):
        """
        test_update_dns_record_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/dns_records/testString')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "169.154.10.10", "zone_id": "023e105f4ecef8ad9ca31a8372d0c353", "zone_name": "test-example.com", "proxiable": true, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        dnsrecord_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "dnsrecord_identifier": dnsrecord_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_dns_record(**req_copy)

    def test_update_dns_record_value_error_with_retries(self):
        # Enable retries and run test_update_dns_record_value_error.
        _service.enable_retries()
        self.test_update_dns_record_value_error()

        # Disable retries and run test_update_dns_record_value_error.
        _service.disable_retries()
        self.test_update_dns_record_value_error()


class TestBatchDnsRecords:
    """
    Test Class for batch_dns_records
    """

    @responses.activate
    def test_batch_dns_records_all_params(self):
        """
        batch_dns_records()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/dns_records/batch')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"deletes": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "1.2.3.4", "proxiable": false, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}, "settings": {"anyKey": "anyValue"}, "meta": {"anyKey": "anyValue"}, "comment": "comment", "tags": ["tags"]}], "patches": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "1.2.3.4", "proxiable": false, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}, "settings": {"anyKey": "anyValue"}, "meta": {"anyKey": "anyValue"}, "comment": "comment", "tags": ["tags"]}], "posts": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "1.2.3.4", "proxiable": false, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}, "settings": {"anyKey": "anyValue"}, "meta": {"anyKey": "anyValue"}, "comment": "comment", "tags": ["tags"]}], "puts": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "1.2.3.4", "proxiable": false, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}, "settings": {"anyKey": "anyValue"}, "meta": {"anyKey": "anyValue"}, "comment": "comment", "tags": ["tags"]}]}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a BatchDnsRecordsRequestDeletesItem model
        batch_dns_records_request_deletes_item_model = {}
        batch_dns_records_request_deletes_item_model['id'] = 'testString'

        # Construct a dict representation of a BatchDnsRecordsRequestPatchesItem model
        batch_dns_records_request_patches_item_model = {}
        batch_dns_records_request_patches_item_model['id'] = 'testString'
        batch_dns_records_request_patches_item_model['name'] = 'host-1.test-example.com'
        batch_dns_records_request_patches_item_model['type'] = 'A'
        batch_dns_records_request_patches_item_model['ttl'] = 120
        batch_dns_records_request_patches_item_model['content'] = '1.2.3.4'
        batch_dns_records_request_patches_item_model['priority'] = 5
        batch_dns_records_request_patches_item_model['proxied'] = False
        batch_dns_records_request_patches_item_model['data'] = {'anyKey': 'anyValue'}

        # Construct a dict representation of a DnsrecordInput model
        dnsrecord_input_model = {}
        dnsrecord_input_model['name'] = 'host-1.test-example.com'
        dnsrecord_input_model['type'] = 'A'
        dnsrecord_input_model['ttl'] = 120
        dnsrecord_input_model['content'] = '1.2.3.4'
        dnsrecord_input_model['priority'] = 5
        dnsrecord_input_model['proxied'] = False
        dnsrecord_input_model['data'] = {'anyKey': 'anyValue'}

        # Construct a dict representation of a BatchDnsRecordsRequestPutsItem model
        batch_dns_records_request_puts_item_model = {}
        batch_dns_records_request_puts_item_model['id'] = 'testString'
        batch_dns_records_request_puts_item_model['name'] = 'host-1.test-example.com'
        batch_dns_records_request_puts_item_model['type'] = 'A'
        batch_dns_records_request_puts_item_model['ttl'] = 120
        batch_dns_records_request_puts_item_model['content'] = '1.2.3.4'
        batch_dns_records_request_puts_item_model['priority'] = 5
        batch_dns_records_request_puts_item_model['proxied'] = False
        batch_dns_records_request_puts_item_model['data'] = {'anyKey': 'anyValue'}

        # Set up parameter values
        deletes = [batch_dns_records_request_deletes_item_model]
        patches = [batch_dns_records_request_patches_item_model]
        posts = [dnsrecord_input_model]
        puts = [batch_dns_records_request_puts_item_model]

        # Invoke method
        response = _service.batch_dns_records(
            deletes=deletes,
            patches=patches,
            posts=posts,
            puts=puts,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['deletes'] == [batch_dns_records_request_deletes_item_model]
        assert req_body['patches'] == [batch_dns_records_request_patches_item_model]
        assert req_body['posts'] == [dnsrecord_input_model]
        assert req_body['puts'] == [batch_dns_records_request_puts_item_model]

    def test_batch_dns_records_all_params_with_retries(self):
        # Enable retries and run test_batch_dns_records_all_params.
        _service.enable_retries()
        self.test_batch_dns_records_all_params()

        # Disable retries and run test_batch_dns_records_all_params.
        _service.disable_retries()
        self.test_batch_dns_records_all_params()

    @responses.activate
    def test_batch_dns_records_required_params(self):
        """
        test_batch_dns_records_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/dns_records/batch')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"deletes": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "1.2.3.4", "proxiable": false, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}, "settings": {"anyKey": "anyValue"}, "meta": {"anyKey": "anyValue"}, "comment": "comment", "tags": ["tags"]}], "patches": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "1.2.3.4", "proxiable": false, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}, "settings": {"anyKey": "anyValue"}, "meta": {"anyKey": "anyValue"}, "comment": "comment", "tags": ["tags"]}], "posts": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "1.2.3.4", "proxiable": false, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}, "settings": {"anyKey": "anyValue"}, "meta": {"anyKey": "anyValue"}, "comment": "comment", "tags": ["tags"]}], "puts": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "1.2.3.4", "proxiable": false, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}, "settings": {"anyKey": "anyValue"}, "meta": {"anyKey": "anyValue"}, "comment": "comment", "tags": ["tags"]}]}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.batch_dns_records()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_batch_dns_records_required_params_with_retries(self):
        # Enable retries and run test_batch_dns_records_required_params.
        _service.enable_retries()
        self.test_batch_dns_records_required_params()

        # Disable retries and run test_batch_dns_records_required_params.
        _service.disable_retries()
        self.test_batch_dns_records_required_params()

    @responses.activate
    def test_batch_dns_records_value_error(self):
        """
        test_batch_dns_records_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/dns_records/batch')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"deletes": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "1.2.3.4", "proxiable": false, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}, "settings": {"anyKey": "anyValue"}, "meta": {"anyKey": "anyValue"}, "comment": "comment", "tags": ["tags"]}], "patches": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "1.2.3.4", "proxiable": false, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}, "settings": {"anyKey": "anyValue"}, "meta": {"anyKey": "anyValue"}, "comment": "comment", "tags": ["tags"]}], "posts": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "1.2.3.4", "proxiable": false, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}, "settings": {"anyKey": "anyValue"}, "meta": {"anyKey": "anyValue"}, "comment": "comment", "tags": ["tags"]}], "puts": [{"id": "f1aba936b94213e5b8dca0c0dbf1f9cc", "created_on": "2014-01-01T05:20:00.12345Z", "modified_on": "2014-01-01T05:20:00.12345Z", "name": "host-1.test-example.com", "type": "A", "content": "1.2.3.4", "proxiable": false, "proxied": false, "ttl": 120, "priority": 5, "data": {"anyKey": "anyValue"}, "settings": {"anyKey": "anyValue"}, "meta": {"anyKey": "anyValue"}, "comment": "comment", "tags": ["tags"]}]}}'
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
                _service.batch_dns_records(**req_copy)

    def test_batch_dns_records_value_error_with_retries(self):
        # Enable retries and run test_batch_dns_records_value_error.
        _service.enable_retries()
        self.test_batch_dns_records_value_error()

        # Disable retries and run test_batch_dns_records_value_error.
        _service.disable_retries()
        self.test_batch_dns_records_value_error()


# endregion
##############################################################################
# End of Service: DNSRecords
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_BatchDnsRecordsRequestDeletesItem:
    """
    Test Class for BatchDnsRecordsRequestDeletesItem
    """

    def test_batch_dns_records_request_deletes_item_serialization(self):
        """
        Test serialization/deserialization for BatchDnsRecordsRequestDeletesItem
        """

        # Construct a json representation of a BatchDnsRecordsRequestDeletesItem model
        batch_dns_records_request_deletes_item_model_json = {}
        batch_dns_records_request_deletes_item_model_json['id'] = 'testString'

        # Construct a model instance of BatchDnsRecordsRequestDeletesItem by calling from_dict on the json representation
        batch_dns_records_request_deletes_item_model = BatchDnsRecordsRequestDeletesItem.from_dict(batch_dns_records_request_deletes_item_model_json)
        assert batch_dns_records_request_deletes_item_model != False

        # Construct a model instance of BatchDnsRecordsRequestDeletesItem by calling from_dict on the json representation
        batch_dns_records_request_deletes_item_model_dict = BatchDnsRecordsRequestDeletesItem.from_dict(batch_dns_records_request_deletes_item_model_json).__dict__
        batch_dns_records_request_deletes_item_model2 = BatchDnsRecordsRequestDeletesItem(**batch_dns_records_request_deletes_item_model_dict)

        # Verify the model instances are equivalent
        assert batch_dns_records_request_deletes_item_model == batch_dns_records_request_deletes_item_model2

        # Convert model instance back to dict and verify no loss of data
        batch_dns_records_request_deletes_item_model_json2 = batch_dns_records_request_deletes_item_model.to_dict()
        assert batch_dns_records_request_deletes_item_model_json2 == batch_dns_records_request_deletes_item_model_json


class TestModel_BatchDnsRecordsRequestPatchesItem:
    """
    Test Class for BatchDnsRecordsRequestPatchesItem
    """

    def test_batch_dns_records_request_patches_item_serialization(self):
        """
        Test serialization/deserialization for BatchDnsRecordsRequestPatchesItem
        """

        # Construct a json representation of a BatchDnsRecordsRequestPatchesItem model
        batch_dns_records_request_patches_item_model_json = {}
        batch_dns_records_request_patches_item_model_json['id'] = 'testString'
        batch_dns_records_request_patches_item_model_json['name'] = 'host-1.test-example.com'
        batch_dns_records_request_patches_item_model_json['type'] = 'A'
        batch_dns_records_request_patches_item_model_json['ttl'] = 120
        batch_dns_records_request_patches_item_model_json['content'] = '1.2.3.4'
        batch_dns_records_request_patches_item_model_json['priority'] = 5
        batch_dns_records_request_patches_item_model_json['proxied'] = False
        batch_dns_records_request_patches_item_model_json['data'] = {'anyKey': 'anyValue'}

        # Construct a model instance of BatchDnsRecordsRequestPatchesItem by calling from_dict on the json representation
        batch_dns_records_request_patches_item_model = BatchDnsRecordsRequestPatchesItem.from_dict(batch_dns_records_request_patches_item_model_json)
        assert batch_dns_records_request_patches_item_model != False

        # Construct a model instance of BatchDnsRecordsRequestPatchesItem by calling from_dict on the json representation
        batch_dns_records_request_patches_item_model_dict = BatchDnsRecordsRequestPatchesItem.from_dict(batch_dns_records_request_patches_item_model_json).__dict__
        batch_dns_records_request_patches_item_model2 = BatchDnsRecordsRequestPatchesItem(**batch_dns_records_request_patches_item_model_dict)

        # Verify the model instances are equivalent
        assert batch_dns_records_request_patches_item_model == batch_dns_records_request_patches_item_model2

        # Convert model instance back to dict and verify no loss of data
        batch_dns_records_request_patches_item_model_json2 = batch_dns_records_request_patches_item_model.to_dict()
        assert batch_dns_records_request_patches_item_model_json2 == batch_dns_records_request_patches_item_model_json


class TestModel_BatchDnsRecordsRequestPutsItem:
    """
    Test Class for BatchDnsRecordsRequestPutsItem
    """

    def test_batch_dns_records_request_puts_item_serialization(self):
        """
        Test serialization/deserialization for BatchDnsRecordsRequestPutsItem
        """

        # Construct a json representation of a BatchDnsRecordsRequestPutsItem model
        batch_dns_records_request_puts_item_model_json = {}
        batch_dns_records_request_puts_item_model_json['id'] = 'testString'
        batch_dns_records_request_puts_item_model_json['name'] = 'host-1.test-example.com'
        batch_dns_records_request_puts_item_model_json['type'] = 'A'
        batch_dns_records_request_puts_item_model_json['ttl'] = 120
        batch_dns_records_request_puts_item_model_json['content'] = '1.2.3.4'
        batch_dns_records_request_puts_item_model_json['priority'] = 5
        batch_dns_records_request_puts_item_model_json['proxied'] = False
        batch_dns_records_request_puts_item_model_json['data'] = {'anyKey': 'anyValue'}

        # Construct a model instance of BatchDnsRecordsRequestPutsItem by calling from_dict on the json representation
        batch_dns_records_request_puts_item_model = BatchDnsRecordsRequestPutsItem.from_dict(batch_dns_records_request_puts_item_model_json)
        assert batch_dns_records_request_puts_item_model != False

        # Construct a model instance of BatchDnsRecordsRequestPutsItem by calling from_dict on the json representation
        batch_dns_records_request_puts_item_model_dict = BatchDnsRecordsRequestPutsItem.from_dict(batch_dns_records_request_puts_item_model_json).__dict__
        batch_dns_records_request_puts_item_model2 = BatchDnsRecordsRequestPutsItem(**batch_dns_records_request_puts_item_model_dict)

        # Verify the model instances are equivalent
        assert batch_dns_records_request_puts_item_model == batch_dns_records_request_puts_item_model2

        # Convert model instance back to dict and verify no loss of data
        batch_dns_records_request_puts_item_model_json2 = batch_dns_records_request_puts_item_model.to_dict()
        assert batch_dns_records_request_puts_item_model_json2 == batch_dns_records_request_puts_item_model_json


class TestModel_BatchDnsRecordsResponseResult:
    """
    Test Class for BatchDnsRecordsResponseResult
    """

    def test_batch_dns_records_response_result_serialization(self):
        """
        Test serialization/deserialization for BatchDnsRecordsResponseResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        batch_dns_record_details_model = {}  # BatchDnsRecordDetails
        batch_dns_record_details_model['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        batch_dns_record_details_model['created_on'] = '2014-01-01T05:20:00.12345Z'
        batch_dns_record_details_model['modified_on'] = '2014-01-01T05:20:00.12345Z'
        batch_dns_record_details_model['name'] = 'host-1.test-example.com'
        batch_dns_record_details_model['type'] = 'A'
        batch_dns_record_details_model['content'] = '1.2.3.4'
        batch_dns_record_details_model['proxiable'] = False
        batch_dns_record_details_model['proxied'] = False
        batch_dns_record_details_model['ttl'] = 120
        batch_dns_record_details_model['priority'] = 5
        batch_dns_record_details_model['data'] = {'anyKey': 'anyValue'}
        batch_dns_record_details_model['settings'] = {'anyKey': 'anyValue'}
        batch_dns_record_details_model['meta'] = {'anyKey': 'anyValue'}
        batch_dns_record_details_model['comment'] = 'testString'
        batch_dns_record_details_model['tags'] = ['testString']

        # Construct a json representation of a BatchDnsRecordsResponseResult model
        batch_dns_records_response_result_model_json = {}
        batch_dns_records_response_result_model_json['deletes'] = [batch_dns_record_details_model]
        batch_dns_records_response_result_model_json['patches'] = [batch_dns_record_details_model]
        batch_dns_records_response_result_model_json['posts'] = [batch_dns_record_details_model]
        batch_dns_records_response_result_model_json['puts'] = [batch_dns_record_details_model]

        # Construct a model instance of BatchDnsRecordsResponseResult by calling from_dict on the json representation
        batch_dns_records_response_result_model = BatchDnsRecordsResponseResult.from_dict(batch_dns_records_response_result_model_json)
        assert batch_dns_records_response_result_model != False

        # Construct a model instance of BatchDnsRecordsResponseResult by calling from_dict on the json representation
        batch_dns_records_response_result_model_dict = BatchDnsRecordsResponseResult.from_dict(batch_dns_records_response_result_model_json).__dict__
        batch_dns_records_response_result_model2 = BatchDnsRecordsResponseResult(**batch_dns_records_response_result_model_dict)

        # Verify the model instances are equivalent
        assert batch_dns_records_response_result_model == batch_dns_records_response_result_model2

        # Convert model instance back to dict and verify no loss of data
        batch_dns_records_response_result_model_json2 = batch_dns_records_response_result_model.to_dict()
        assert batch_dns_records_response_result_model_json2 == batch_dns_records_response_result_model_json


class TestModel_DeleteDnsrecordRespResult:
    """
    Test Class for DeleteDnsrecordRespResult
    """

    def test_delete_dnsrecord_resp_result_serialization(self):
        """
        Test serialization/deserialization for DeleteDnsrecordRespResult
        """

        # Construct a json representation of a DeleteDnsrecordRespResult model
        delete_dnsrecord_resp_result_model_json = {}
        delete_dnsrecord_resp_result_model_json['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'

        # Construct a model instance of DeleteDnsrecordRespResult by calling from_dict on the json representation
        delete_dnsrecord_resp_result_model = DeleteDnsrecordRespResult.from_dict(delete_dnsrecord_resp_result_model_json)
        assert delete_dnsrecord_resp_result_model != False

        # Construct a model instance of DeleteDnsrecordRespResult by calling from_dict on the json representation
        delete_dnsrecord_resp_result_model_dict = DeleteDnsrecordRespResult.from_dict(delete_dnsrecord_resp_result_model_json).__dict__
        delete_dnsrecord_resp_result_model2 = DeleteDnsrecordRespResult(**delete_dnsrecord_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert delete_dnsrecord_resp_result_model == delete_dnsrecord_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        delete_dnsrecord_resp_result_model_json2 = delete_dnsrecord_resp_result_model.to_dict()
        assert delete_dnsrecord_resp_result_model_json2 == delete_dnsrecord_resp_result_model_json


class TestModel_BatchDnsRecordDetails:
    """
    Test Class for BatchDnsRecordDetails
    """

    def test_batch_dns_record_details_serialization(self):
        """
        Test serialization/deserialization for BatchDnsRecordDetails
        """

        # Construct a json representation of a BatchDnsRecordDetails model
        batch_dns_record_details_model_json = {}
        batch_dns_record_details_model_json['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        batch_dns_record_details_model_json['created_on'] = '2014-01-01T05:20:00.12345Z'
        batch_dns_record_details_model_json['modified_on'] = '2014-01-01T05:20:00.12345Z'
        batch_dns_record_details_model_json['name'] = 'host-1.test-example.com'
        batch_dns_record_details_model_json['type'] = 'A'
        batch_dns_record_details_model_json['content'] = '1.2.3.4'
        batch_dns_record_details_model_json['proxiable'] = False
        batch_dns_record_details_model_json['proxied'] = False
        batch_dns_record_details_model_json['ttl'] = 120
        batch_dns_record_details_model_json['priority'] = 5
        batch_dns_record_details_model_json['data'] = {'anyKey': 'anyValue'}
        batch_dns_record_details_model_json['settings'] = {'anyKey': 'anyValue'}
        batch_dns_record_details_model_json['meta'] = {'anyKey': 'anyValue'}
        batch_dns_record_details_model_json['comment'] = 'testString'
        batch_dns_record_details_model_json['tags'] = ['testString']

        # Construct a model instance of BatchDnsRecordDetails by calling from_dict on the json representation
        batch_dns_record_details_model = BatchDnsRecordDetails.from_dict(batch_dns_record_details_model_json)
        assert batch_dns_record_details_model != False

        # Construct a model instance of BatchDnsRecordDetails by calling from_dict on the json representation
        batch_dns_record_details_model_dict = BatchDnsRecordDetails.from_dict(batch_dns_record_details_model_json).__dict__
        batch_dns_record_details_model2 = BatchDnsRecordDetails(**batch_dns_record_details_model_dict)

        # Verify the model instances are equivalent
        assert batch_dns_record_details_model == batch_dns_record_details_model2

        # Convert model instance back to dict and verify no loss of data
        batch_dns_record_details_model_json2 = batch_dns_record_details_model.to_dict()
        assert batch_dns_record_details_model_json2 == batch_dns_record_details_model_json


class TestModel_BatchDnsRecordsResponse:
    """
    Test Class for BatchDnsRecordsResponse
    """

    def test_batch_dns_records_response_serialization(self):
        """
        Test serialization/deserialization for BatchDnsRecordsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        batch_dns_record_details_model = {}  # BatchDnsRecordDetails
        batch_dns_record_details_model['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        batch_dns_record_details_model['created_on'] = '2014-01-01T05:20:00.12345Z'
        batch_dns_record_details_model['modified_on'] = '2014-01-01T05:20:00.12345Z'
        batch_dns_record_details_model['name'] = 'host-1.test-example.com'
        batch_dns_record_details_model['type'] = 'A'
        batch_dns_record_details_model['content'] = '1.2.3.4'
        batch_dns_record_details_model['proxiable'] = False
        batch_dns_record_details_model['proxied'] = False
        batch_dns_record_details_model['ttl'] = 120
        batch_dns_record_details_model['priority'] = 5
        batch_dns_record_details_model['data'] = {'anyKey': 'anyValue'}
        batch_dns_record_details_model['settings'] = {'anyKey': 'anyValue'}
        batch_dns_record_details_model['meta'] = {'anyKey': 'anyValue'}
        batch_dns_record_details_model['comment'] = 'testString'
        batch_dns_record_details_model['tags'] = ['testString']

        batch_dns_records_response_result_model = {}  # BatchDnsRecordsResponseResult
        batch_dns_records_response_result_model['deletes'] = [batch_dns_record_details_model]
        batch_dns_records_response_result_model['patches'] = [batch_dns_record_details_model]
        batch_dns_records_response_result_model['posts'] = [batch_dns_record_details_model]
        batch_dns_records_response_result_model['puts'] = [batch_dns_record_details_model]

        # Construct a json representation of a BatchDnsRecordsResponse model
        batch_dns_records_response_model_json = {}
        batch_dns_records_response_model_json['success'] = True
        batch_dns_records_response_model_json['errors'] = [['testString']]
        batch_dns_records_response_model_json['messages'] = [['testString']]
        batch_dns_records_response_model_json['result'] = batch_dns_records_response_result_model

        # Construct a model instance of BatchDnsRecordsResponse by calling from_dict on the json representation
        batch_dns_records_response_model = BatchDnsRecordsResponse.from_dict(batch_dns_records_response_model_json)
        assert batch_dns_records_response_model != False

        # Construct a model instance of BatchDnsRecordsResponse by calling from_dict on the json representation
        batch_dns_records_response_model_dict = BatchDnsRecordsResponse.from_dict(batch_dns_records_response_model_json).__dict__
        batch_dns_records_response_model2 = BatchDnsRecordsResponse(**batch_dns_records_response_model_dict)

        # Verify the model instances are equivalent
        assert batch_dns_records_response_model == batch_dns_records_response_model2

        # Convert model instance back to dict and verify no loss of data
        batch_dns_records_response_model_json2 = batch_dns_records_response_model.to_dict()
        assert batch_dns_records_response_model_json2 == batch_dns_records_response_model_json


class TestModel_DeleteDnsrecordResp:
    """
    Test Class for DeleteDnsrecordResp
    """

    def test_delete_dnsrecord_resp_serialization(self):
        """
        Test serialization/deserialization for DeleteDnsrecordResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        delete_dnsrecord_resp_result_model = {}  # DeleteDnsrecordRespResult
        delete_dnsrecord_resp_result_model['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'

        # Construct a json representation of a DeleteDnsrecordResp model
        delete_dnsrecord_resp_model_json = {}
        delete_dnsrecord_resp_model_json['success'] = True
        delete_dnsrecord_resp_model_json['errors'] = [['testString']]
        delete_dnsrecord_resp_model_json['messages'] = [['testString']]
        delete_dnsrecord_resp_model_json['result'] = delete_dnsrecord_resp_result_model

        # Construct a model instance of DeleteDnsrecordResp by calling from_dict on the json representation
        delete_dnsrecord_resp_model = DeleteDnsrecordResp.from_dict(delete_dnsrecord_resp_model_json)
        assert delete_dnsrecord_resp_model != False

        # Construct a model instance of DeleteDnsrecordResp by calling from_dict on the json representation
        delete_dnsrecord_resp_model_dict = DeleteDnsrecordResp.from_dict(delete_dnsrecord_resp_model_json).__dict__
        delete_dnsrecord_resp_model2 = DeleteDnsrecordResp(**delete_dnsrecord_resp_model_dict)

        # Verify the model instances are equivalent
        assert delete_dnsrecord_resp_model == delete_dnsrecord_resp_model2

        # Convert model instance back to dict and verify no loss of data
        delete_dnsrecord_resp_model_json2 = delete_dnsrecord_resp_model.to_dict()
        assert delete_dnsrecord_resp_model_json2 == delete_dnsrecord_resp_model_json


class TestModel_DnsrecordDetails:
    """
    Test Class for DnsrecordDetails
    """

    def test_dnsrecord_details_serialization(self):
        """
        Test serialization/deserialization for DnsrecordDetails
        """

        # Construct a json representation of a DnsrecordDetails model
        dnsrecord_details_model_json = {}
        dnsrecord_details_model_json['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        dnsrecord_details_model_json['created_on'] = '2014-01-01T05:20:00.12345Z'
        dnsrecord_details_model_json['modified_on'] = '2014-01-01T05:20:00.12345Z'
        dnsrecord_details_model_json['name'] = 'host-1.test-example.com'
        dnsrecord_details_model_json['type'] = 'A'
        dnsrecord_details_model_json['content'] = '169.154.10.10'
        dnsrecord_details_model_json['zone_id'] = '023e105f4ecef8ad9ca31a8372d0c353'
        dnsrecord_details_model_json['zone_name'] = 'test-example.com'
        dnsrecord_details_model_json['proxiable'] = True
        dnsrecord_details_model_json['proxied'] = False
        dnsrecord_details_model_json['ttl'] = 120
        dnsrecord_details_model_json['priority'] = 5
        dnsrecord_details_model_json['data'] = {'anyKey': 'anyValue'}

        # Construct a model instance of DnsrecordDetails by calling from_dict on the json representation
        dnsrecord_details_model = DnsrecordDetails.from_dict(dnsrecord_details_model_json)
        assert dnsrecord_details_model != False

        # Construct a model instance of DnsrecordDetails by calling from_dict on the json representation
        dnsrecord_details_model_dict = DnsrecordDetails.from_dict(dnsrecord_details_model_json).__dict__
        dnsrecord_details_model2 = DnsrecordDetails(**dnsrecord_details_model_dict)

        # Verify the model instances are equivalent
        assert dnsrecord_details_model == dnsrecord_details_model2

        # Convert model instance back to dict and verify no loss of data
        dnsrecord_details_model_json2 = dnsrecord_details_model.to_dict()
        assert dnsrecord_details_model_json2 == dnsrecord_details_model_json


class TestModel_DnsrecordInput:
    """
    Test Class for DnsrecordInput
    """

    def test_dnsrecord_input_serialization(self):
        """
        Test serialization/deserialization for DnsrecordInput
        """

        # Construct a json representation of a DnsrecordInput model
        dnsrecord_input_model_json = {}
        dnsrecord_input_model_json['name'] = 'host-1.test-example.com'
        dnsrecord_input_model_json['type'] = 'A'
        dnsrecord_input_model_json['ttl'] = 120
        dnsrecord_input_model_json['content'] = '1.2.3.4'
        dnsrecord_input_model_json['priority'] = 5
        dnsrecord_input_model_json['proxied'] = False
        dnsrecord_input_model_json['data'] = {'anyKey': 'anyValue'}

        # Construct a model instance of DnsrecordInput by calling from_dict on the json representation
        dnsrecord_input_model = DnsrecordInput.from_dict(dnsrecord_input_model_json)
        assert dnsrecord_input_model != False

        # Construct a model instance of DnsrecordInput by calling from_dict on the json representation
        dnsrecord_input_model_dict = DnsrecordInput.from_dict(dnsrecord_input_model_json).__dict__
        dnsrecord_input_model2 = DnsrecordInput(**dnsrecord_input_model_dict)

        # Verify the model instances are equivalent
        assert dnsrecord_input_model == dnsrecord_input_model2

        # Convert model instance back to dict and verify no loss of data
        dnsrecord_input_model_json2 = dnsrecord_input_model.to_dict()
        assert dnsrecord_input_model_json2 == dnsrecord_input_model_json


class TestModel_DnsrecordResp:
    """
    Test Class for DnsrecordResp
    """

    def test_dnsrecord_resp_serialization(self):
        """
        Test serialization/deserialization for DnsrecordResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        dnsrecord_details_model = {}  # DnsrecordDetails
        dnsrecord_details_model['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        dnsrecord_details_model['created_on'] = '2014-01-01T05:20:00.12345Z'
        dnsrecord_details_model['modified_on'] = '2014-01-01T05:20:00.12345Z'
        dnsrecord_details_model['name'] = 'host-1.test-example.com'
        dnsrecord_details_model['type'] = 'A'
        dnsrecord_details_model['content'] = '169.154.10.10'
        dnsrecord_details_model['zone_id'] = '023e105f4ecef8ad9ca31a8372d0c353'
        dnsrecord_details_model['zone_name'] = 'test-example.com'
        dnsrecord_details_model['proxiable'] = True
        dnsrecord_details_model['proxied'] = False
        dnsrecord_details_model['ttl'] = 120
        dnsrecord_details_model['priority'] = 5
        dnsrecord_details_model['data'] = {'anyKey': 'anyValue'}

        # Construct a json representation of a DnsrecordResp model
        dnsrecord_resp_model_json = {}
        dnsrecord_resp_model_json['success'] = True
        dnsrecord_resp_model_json['errors'] = [['testString']]
        dnsrecord_resp_model_json['messages'] = [['testString']]
        dnsrecord_resp_model_json['result'] = dnsrecord_details_model

        # Construct a model instance of DnsrecordResp by calling from_dict on the json representation
        dnsrecord_resp_model = DnsrecordResp.from_dict(dnsrecord_resp_model_json)
        assert dnsrecord_resp_model != False

        # Construct a model instance of DnsrecordResp by calling from_dict on the json representation
        dnsrecord_resp_model_dict = DnsrecordResp.from_dict(dnsrecord_resp_model_json).__dict__
        dnsrecord_resp_model2 = DnsrecordResp(**dnsrecord_resp_model_dict)

        # Verify the model instances are equivalent
        assert dnsrecord_resp_model == dnsrecord_resp_model2

        # Convert model instance back to dict and verify no loss of data
        dnsrecord_resp_model_json2 = dnsrecord_resp_model.to_dict()
        assert dnsrecord_resp_model_json2 == dnsrecord_resp_model_json


class TestModel_ListDnsrecordsResp:
    """
    Test Class for ListDnsrecordsResp
    """

    def test_list_dnsrecords_resp_serialization(self):
        """
        Test serialization/deserialization for ListDnsrecordsResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        dnsrecord_details_model = {}  # DnsrecordDetails
        dnsrecord_details_model['id'] = 'f1aba936b94213e5b8dca0c0dbf1f9cc'
        dnsrecord_details_model['created_on'] = '2014-01-01T05:20:00.12345Z'
        dnsrecord_details_model['modified_on'] = '2014-01-01T05:20:00.12345Z'
        dnsrecord_details_model['name'] = 'host-1.test-example.com'
        dnsrecord_details_model['type'] = 'A'
        dnsrecord_details_model['content'] = '169.154.10.10'
        dnsrecord_details_model['zone_id'] = '023e105f4ecef8ad9ca31a8372d0c353'
        dnsrecord_details_model['zone_name'] = 'test-example.com'
        dnsrecord_details_model['proxiable'] = True
        dnsrecord_details_model['proxied'] = False
        dnsrecord_details_model['ttl'] = 120
        dnsrecord_details_model['priority'] = 5
        dnsrecord_details_model['data'] = {'anyKey': 'anyValue'}

        result_info_model = {}  # ResultInfo
        result_info_model['page'] = 1
        result_info_model['per_page'] = 20
        result_info_model['count'] = 1
        result_info_model['total_count'] = 2000

        # Construct a json representation of a ListDnsrecordsResp model
        list_dnsrecords_resp_model_json = {}
        list_dnsrecords_resp_model_json['success'] = True
        list_dnsrecords_resp_model_json['errors'] = [['testString']]
        list_dnsrecords_resp_model_json['messages'] = [['testString']]
        list_dnsrecords_resp_model_json['result'] = [dnsrecord_details_model]
        list_dnsrecords_resp_model_json['result_info'] = result_info_model

        # Construct a model instance of ListDnsrecordsResp by calling from_dict on the json representation
        list_dnsrecords_resp_model = ListDnsrecordsResp.from_dict(list_dnsrecords_resp_model_json)
        assert list_dnsrecords_resp_model != False

        # Construct a model instance of ListDnsrecordsResp by calling from_dict on the json representation
        list_dnsrecords_resp_model_dict = ListDnsrecordsResp.from_dict(list_dnsrecords_resp_model_json).__dict__
        list_dnsrecords_resp_model2 = ListDnsrecordsResp(**list_dnsrecords_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_dnsrecords_resp_model == list_dnsrecords_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_dnsrecords_resp_model_json2 = list_dnsrecords_resp_model.to_dict()
        assert list_dnsrecords_resp_model_json2 == list_dnsrecords_resp_model_json


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


# endregion
##############################################################################
# End of Model Tests
##############################################################################
