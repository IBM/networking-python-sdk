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
Unit Tests for ZonesSettingsV1
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import inspect
import json
import os
import pytest
import re
import responses
import urllib
from ibm_cloud_networking_services.zones_settings_v1 import *

crn = 'testString'
zone_identifier = 'testString'

_service = ZonesSettingsV1(
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
# Start of Service: ZonesSettings
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

        service = ZonesSettingsV1.new_instance(
            crn=crn,
            zone_identifier=zone_identifier,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, ZonesSettingsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = ZonesSettingsV1.new_instance(
                crn=crn,
                zone_identifier=zone_identifier,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = ZonesSettingsV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='crn must be provided'):
            service = ZonesSettingsV1.new_instance(
                crn=None,
                zone_identifier=None,
            )


class TestGetZoneDnssec:
    """
    Test Class for get_zone_dnssec
    """

    @responses.activate
    def test_get_zone_dnssec_all_params(self):
        """
        get_zone_dnssec()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/dnssec')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"status": "active", "flags": 257, "algorithm": "13", "key_type": "ECDSAP256SHA256", "digest_type": "2", "digest_algorithm": "SHA256", "digest": "48E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "ds": "example.com. 3600 IN DS 16953 13 2 248E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "key_tag": 42, "public_key": "oXiGYrSTO+LSCJ3mohc8EP+CzF9KxBj8/ydXJ22pKuZP3VAC3/Md/k7xZfz470CoRyZJ6gV6vml07IC3d8xqhA=="}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_zone_dnssec()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_zone_dnssec_all_params_with_retries(self):
        # Enable retries and run test_get_zone_dnssec_all_params.
        _service.enable_retries()
        self.test_get_zone_dnssec_all_params()

        # Disable retries and run test_get_zone_dnssec_all_params.
        _service.disable_retries()
        self.test_get_zone_dnssec_all_params()

    @responses.activate
    def test_get_zone_dnssec_value_error(self):
        """
        test_get_zone_dnssec_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/dnssec')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"status": "active", "flags": 257, "algorithm": "13", "key_type": "ECDSAP256SHA256", "digest_type": "2", "digest_algorithm": "SHA256", "digest": "48E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "ds": "example.com. 3600 IN DS 16953 13 2 248E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "key_tag": 42, "public_key": "oXiGYrSTO+LSCJ3mohc8EP+CzF9KxBj8/ydXJ22pKuZP3VAC3/Md/k7xZfz470CoRyZJ6gV6vml07IC3d8xqhA=="}}'
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
                _service.get_zone_dnssec(**req_copy)

    def test_get_zone_dnssec_value_error_with_retries(self):
        # Enable retries and run test_get_zone_dnssec_value_error.
        _service.enable_retries()
        self.test_get_zone_dnssec_value_error()

        # Disable retries and run test_get_zone_dnssec_value_error.
        _service.disable_retries()
        self.test_get_zone_dnssec_value_error()


class TestUpdateZoneDnssec:
    """
    Test Class for update_zone_dnssec
    """

    @responses.activate
    def test_update_zone_dnssec_all_params(self):
        """
        update_zone_dnssec()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/dnssec')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"status": "active", "flags": 257, "algorithm": "13", "key_type": "ECDSAP256SHA256", "digest_type": "2", "digest_algorithm": "SHA256", "digest": "48E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "ds": "example.com. 3600 IN DS 16953 13 2 248E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "key_tag": 42, "public_key": "oXiGYrSTO+LSCJ3mohc8EP+CzF9KxBj8/ydXJ22pKuZP3VAC3/Md/k7xZfz470CoRyZJ6gV6vml07IC3d8xqhA=="}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        status = 'active'

        # Invoke method
        response = _service.update_zone_dnssec(
            status=status,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['status'] == 'active'

    def test_update_zone_dnssec_all_params_with_retries(self):
        # Enable retries and run test_update_zone_dnssec_all_params.
        _service.enable_retries()
        self.test_update_zone_dnssec_all_params()

        # Disable retries and run test_update_zone_dnssec_all_params.
        _service.disable_retries()
        self.test_update_zone_dnssec_all_params()

    @responses.activate
    def test_update_zone_dnssec_required_params(self):
        """
        test_update_zone_dnssec_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/dnssec')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"status": "active", "flags": 257, "algorithm": "13", "key_type": "ECDSAP256SHA256", "digest_type": "2", "digest_algorithm": "SHA256", "digest": "48E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "ds": "example.com. 3600 IN DS 16953 13 2 248E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "key_tag": 42, "public_key": "oXiGYrSTO+LSCJ3mohc8EP+CzF9KxBj8/ydXJ22pKuZP3VAC3/Md/k7xZfz470CoRyZJ6gV6vml07IC3d8xqhA=="}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_zone_dnssec()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_zone_dnssec_required_params_with_retries(self):
        # Enable retries and run test_update_zone_dnssec_required_params.
        _service.enable_retries()
        self.test_update_zone_dnssec_required_params()

        # Disable retries and run test_update_zone_dnssec_required_params.
        _service.disable_retries()
        self.test_update_zone_dnssec_required_params()

    @responses.activate
    def test_update_zone_dnssec_value_error(self):
        """
        test_update_zone_dnssec_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/dnssec')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"status": "active", "flags": 257, "algorithm": "13", "key_type": "ECDSAP256SHA256", "digest_type": "2", "digest_algorithm": "SHA256", "digest": "48E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "ds": "example.com. 3600 IN DS 16953 13 2 248E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45", "key_tag": 42, "public_key": "oXiGYrSTO+LSCJ3mohc8EP+CzF9KxBj8/ydXJ22pKuZP3VAC3/Md/k7xZfz470CoRyZJ6gV6vml07IC3d8xqhA=="}}'
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
                _service.update_zone_dnssec(**req_copy)

    def test_update_zone_dnssec_value_error_with_retries(self):
        # Enable retries and run test_update_zone_dnssec_value_error.
        _service.enable_retries()
        self.test_update_zone_dnssec_value_error()

        # Disable retries and run test_update_zone_dnssec_value_error.
        _service.disable_retries()
        self.test_update_zone_dnssec_value_error()


class TestGetZoneCnameFlattening:
    """
    Test Class for get_zone_cname_flattening
    """

    @responses.activate
    def test_get_zone_cname_flattening_all_params(self):
        """
        get_zone_cname_flattening()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/cname_flattening')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "cname_flattening", "value": "flatten_all", "modified_on": "2014-01-01T05:20:00.123Z", "editable": true}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_zone_cname_flattening()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_zone_cname_flattening_all_params_with_retries(self):
        # Enable retries and run test_get_zone_cname_flattening_all_params.
        _service.enable_retries()
        self.test_get_zone_cname_flattening_all_params()

        # Disable retries and run test_get_zone_cname_flattening_all_params.
        _service.disable_retries()
        self.test_get_zone_cname_flattening_all_params()

    @responses.activate
    def test_get_zone_cname_flattening_value_error(self):
        """
        test_get_zone_cname_flattening_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/cname_flattening')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "cname_flattening", "value": "flatten_all", "modified_on": "2014-01-01T05:20:00.123Z", "editable": true}}'
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
                _service.get_zone_cname_flattening(**req_copy)

    def test_get_zone_cname_flattening_value_error_with_retries(self):
        # Enable retries and run test_get_zone_cname_flattening_value_error.
        _service.enable_retries()
        self.test_get_zone_cname_flattening_value_error()

        # Disable retries and run test_get_zone_cname_flattening_value_error.
        _service.disable_retries()
        self.test_get_zone_cname_flattening_value_error()


class TestUpdateZoneCnameFlattening:
    """
    Test Class for update_zone_cname_flattening
    """

    @responses.activate
    def test_update_zone_cname_flattening_all_params(self):
        """
        update_zone_cname_flattening()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/cname_flattening')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "cname_flattening", "value": "flatten_all", "modified_on": "2014-01-01T05:20:00.123Z", "editable": true}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 'flatten_all'

        # Invoke method
        response = _service.update_zone_cname_flattening(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'flatten_all'

    def test_update_zone_cname_flattening_all_params_with_retries(self):
        # Enable retries and run test_update_zone_cname_flattening_all_params.
        _service.enable_retries()
        self.test_update_zone_cname_flattening_all_params()

        # Disable retries and run test_update_zone_cname_flattening_all_params.
        _service.disable_retries()
        self.test_update_zone_cname_flattening_all_params()

    @responses.activate
    def test_update_zone_cname_flattening_required_params(self):
        """
        test_update_zone_cname_flattening_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/cname_flattening')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "cname_flattening", "value": "flatten_all", "modified_on": "2014-01-01T05:20:00.123Z", "editable": true}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_zone_cname_flattening()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_zone_cname_flattening_required_params_with_retries(self):
        # Enable retries and run test_update_zone_cname_flattening_required_params.
        _service.enable_retries()
        self.test_update_zone_cname_flattening_required_params()

        # Disable retries and run test_update_zone_cname_flattening_required_params.
        _service.disable_retries()
        self.test_update_zone_cname_flattening_required_params()

    @responses.activate
    def test_update_zone_cname_flattening_value_error(self):
        """
        test_update_zone_cname_flattening_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/cname_flattening')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"id": "cname_flattening", "value": "flatten_all", "modified_on": "2014-01-01T05:20:00.123Z", "editable": true}}'
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
                _service.update_zone_cname_flattening(**req_copy)

    def test_update_zone_cname_flattening_value_error_with_retries(self):
        # Enable retries and run test_update_zone_cname_flattening_value_error.
        _service.enable_retries()
        self.test_update_zone_cname_flattening_value_error()

        # Disable retries and run test_update_zone_cname_flattening_value_error.
        _service.disable_retries()
        self.test_update_zone_cname_flattening_value_error()


class TestGetOpportunisticEncryption:
    """
    Test Class for get_opportunistic_encryption
    """

    @responses.activate
    def test_get_opportunistic_encryption_all_params(self):
        """
        get_opportunistic_encryption()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/opportunistic_encryption')
        mock_response = '{"result": {"id": "opportunistic_encryption", "value": "off", "editable": true, "modified_on": "2017-01-01T05:20:00.123Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_opportunistic_encryption()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_opportunistic_encryption_all_params_with_retries(self):
        # Enable retries and run test_get_opportunistic_encryption_all_params.
        _service.enable_retries()
        self.test_get_opportunistic_encryption_all_params()

        # Disable retries and run test_get_opportunistic_encryption_all_params.
        _service.disable_retries()
        self.test_get_opportunistic_encryption_all_params()

    @responses.activate
    def test_get_opportunistic_encryption_value_error(self):
        """
        test_get_opportunistic_encryption_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/opportunistic_encryption')
        mock_response = '{"result": {"id": "opportunistic_encryption", "value": "off", "editable": true, "modified_on": "2017-01-01T05:20:00.123Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_opportunistic_encryption(**req_copy)

    def test_get_opportunistic_encryption_value_error_with_retries(self):
        # Enable retries and run test_get_opportunistic_encryption_value_error.
        _service.enable_retries()
        self.test_get_opportunistic_encryption_value_error()

        # Disable retries and run test_get_opportunistic_encryption_value_error.
        _service.disable_retries()
        self.test_get_opportunistic_encryption_value_error()


class TestUpdateOpportunisticEncryption:
    """
    Test Class for update_opportunistic_encryption
    """

    @responses.activate
    def test_update_opportunistic_encryption_all_params(self):
        """
        update_opportunistic_encryption()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/opportunistic_encryption')
        mock_response = '{"result": {"id": "opportunistic_encryption", "value": "off", "editable": true, "modified_on": "2017-01-01T05:20:00.123Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 'off'

        # Invoke method
        response = _service.update_opportunistic_encryption(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'off'

    def test_update_opportunistic_encryption_all_params_with_retries(self):
        # Enable retries and run test_update_opportunistic_encryption_all_params.
        _service.enable_retries()
        self.test_update_opportunistic_encryption_all_params()

        # Disable retries and run test_update_opportunistic_encryption_all_params.
        _service.disable_retries()
        self.test_update_opportunistic_encryption_all_params()

    @responses.activate
    def test_update_opportunistic_encryption_required_params(self):
        """
        test_update_opportunistic_encryption_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/opportunistic_encryption')
        mock_response = '{"result": {"id": "opportunistic_encryption", "value": "off", "editable": true, "modified_on": "2017-01-01T05:20:00.123Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_opportunistic_encryption()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_opportunistic_encryption_required_params_with_retries(self):
        # Enable retries and run test_update_opportunistic_encryption_required_params.
        _service.enable_retries()
        self.test_update_opportunistic_encryption_required_params()

        # Disable retries and run test_update_opportunistic_encryption_required_params.
        _service.disable_retries()
        self.test_update_opportunistic_encryption_required_params()

    @responses.activate
    def test_update_opportunistic_encryption_value_error(self):
        """
        test_update_opportunistic_encryption_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/opportunistic_encryption')
        mock_response = '{"result": {"id": "opportunistic_encryption", "value": "off", "editable": true, "modified_on": "2017-01-01T05:20:00.123Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_opportunistic_encryption(**req_copy)

    def test_update_opportunistic_encryption_value_error_with_retries(self):
        # Enable retries and run test_update_opportunistic_encryption_value_error.
        _service.enable_retries()
        self.test_update_opportunistic_encryption_value_error()

        # Disable retries and run test_update_opportunistic_encryption_value_error.
        _service.disable_retries()
        self.test_update_opportunistic_encryption_value_error()


class TestGetOpportunisticOnion:
    """
    Test Class for get_opportunistic_onion
    """

    @responses.activate
    def test_get_opportunistic_onion_all_params(self):
        """
        get_opportunistic_onion()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/opportunistic_onion')
        mock_response = '{"result": {"id": "opportunistic_onion", "value": "off", "editable": true, "modified_on": "2017-01-01T05:20:00.123Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_opportunistic_onion()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_opportunistic_onion_all_params_with_retries(self):
        # Enable retries and run test_get_opportunistic_onion_all_params.
        _service.enable_retries()
        self.test_get_opportunistic_onion_all_params()

        # Disable retries and run test_get_opportunistic_onion_all_params.
        _service.disable_retries()
        self.test_get_opportunistic_onion_all_params()

    @responses.activate
    def test_get_opportunistic_onion_value_error(self):
        """
        test_get_opportunistic_onion_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/opportunistic_onion')
        mock_response = '{"result": {"id": "opportunistic_onion", "value": "off", "editable": true, "modified_on": "2017-01-01T05:20:00.123Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_opportunistic_onion(**req_copy)

    def test_get_opportunistic_onion_value_error_with_retries(self):
        # Enable retries and run test_get_opportunistic_onion_value_error.
        _service.enable_retries()
        self.test_get_opportunistic_onion_value_error()

        # Disable retries and run test_get_opportunistic_onion_value_error.
        _service.disable_retries()
        self.test_get_opportunistic_onion_value_error()


class TestUpdateOpportunisticOnion:
    """
    Test Class for update_opportunistic_onion
    """

    @responses.activate
    def test_update_opportunistic_onion_all_params(self):
        """
        update_opportunistic_onion()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/opportunistic_onion')
        mock_response = '{"result": {"id": "opportunistic_onion", "value": "off", "editable": true, "modified_on": "2017-01-01T05:20:00.123Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 'off'

        # Invoke method
        response = _service.update_opportunistic_onion(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'off'

    def test_update_opportunistic_onion_all_params_with_retries(self):
        # Enable retries and run test_update_opportunistic_onion_all_params.
        _service.enable_retries()
        self.test_update_opportunistic_onion_all_params()

        # Disable retries and run test_update_opportunistic_onion_all_params.
        _service.disable_retries()
        self.test_update_opportunistic_onion_all_params()

    @responses.activate
    def test_update_opportunistic_onion_required_params(self):
        """
        test_update_opportunistic_onion_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/opportunistic_onion')
        mock_response = '{"result": {"id": "opportunistic_onion", "value": "off", "editable": true, "modified_on": "2017-01-01T05:20:00.123Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_opportunistic_onion()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_opportunistic_onion_required_params_with_retries(self):
        # Enable retries and run test_update_opportunistic_onion_required_params.
        _service.enable_retries()
        self.test_update_opportunistic_onion_required_params()

        # Disable retries and run test_update_opportunistic_onion_required_params.
        _service.disable_retries()
        self.test_update_opportunistic_onion_required_params()

    @responses.activate
    def test_update_opportunistic_onion_value_error(self):
        """
        test_update_opportunistic_onion_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/opportunistic_onion')
        mock_response = '{"result": {"id": "opportunistic_onion", "value": "off", "editable": true, "modified_on": "2017-01-01T05:20:00.123Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_opportunistic_onion(**req_copy)

    def test_update_opportunistic_onion_value_error_with_retries(self):
        # Enable retries and run test_update_opportunistic_onion_value_error.
        _service.enable_retries()
        self.test_update_opportunistic_onion_value_error()

        # Disable retries and run test_update_opportunistic_onion_value_error.
        _service.disable_retries()
        self.test_update_opportunistic_onion_value_error()


class TestGetChallengeTtl:
    """
    Test Class for get_challenge_ttl
    """

    @responses.activate
    def test_get_challenge_ttl_all_params(self):
        """
        get_challenge_ttl()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/challenge_ttl')
        mock_response = '{"result": {"id": "challenge_ttl", "value": 1800, "editable": true, "modified_on": "2018-09-17T07:21:39.844Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_challenge_ttl()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_challenge_ttl_all_params_with_retries(self):
        # Enable retries and run test_get_challenge_ttl_all_params.
        _service.enable_retries()
        self.test_get_challenge_ttl_all_params()

        # Disable retries and run test_get_challenge_ttl_all_params.
        _service.disable_retries()
        self.test_get_challenge_ttl_all_params()

    @responses.activate
    def test_get_challenge_ttl_value_error(self):
        """
        test_get_challenge_ttl_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/challenge_ttl')
        mock_response = '{"result": {"id": "challenge_ttl", "value": 1800, "editable": true, "modified_on": "2018-09-17T07:21:39.844Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_challenge_ttl(**req_copy)

    def test_get_challenge_ttl_value_error_with_retries(self):
        # Enable retries and run test_get_challenge_ttl_value_error.
        _service.enable_retries()
        self.test_get_challenge_ttl_value_error()

        # Disable retries and run test_get_challenge_ttl_value_error.
        _service.disable_retries()
        self.test_get_challenge_ttl_value_error()


class TestUpdateChallengeTtl:
    """
    Test Class for update_challenge_ttl
    """

    @responses.activate
    def test_update_challenge_ttl_all_params(self):
        """
        update_challenge_ttl()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/challenge_ttl')
        mock_response = '{"result": {"id": "challenge_ttl", "value": 1800, "editable": true, "modified_on": "2018-09-17T07:21:39.844Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 1800

        # Invoke method
        response = _service.update_challenge_ttl(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 1800

    def test_update_challenge_ttl_all_params_with_retries(self):
        # Enable retries and run test_update_challenge_ttl_all_params.
        _service.enable_retries()
        self.test_update_challenge_ttl_all_params()

        # Disable retries and run test_update_challenge_ttl_all_params.
        _service.disable_retries()
        self.test_update_challenge_ttl_all_params()

    @responses.activate
    def test_update_challenge_ttl_required_params(self):
        """
        test_update_challenge_ttl_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/challenge_ttl')
        mock_response = '{"result": {"id": "challenge_ttl", "value": 1800, "editable": true, "modified_on": "2018-09-17T07:21:39.844Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_challenge_ttl()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_challenge_ttl_required_params_with_retries(self):
        # Enable retries and run test_update_challenge_ttl_required_params.
        _service.enable_retries()
        self.test_update_challenge_ttl_required_params()

        # Disable retries and run test_update_challenge_ttl_required_params.
        _service.disable_retries()
        self.test_update_challenge_ttl_required_params()

    @responses.activate
    def test_update_challenge_ttl_value_error(self):
        """
        test_update_challenge_ttl_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/challenge_ttl')
        mock_response = '{"result": {"id": "challenge_ttl", "value": 1800, "editable": true, "modified_on": "2018-09-17T07:21:39.844Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_challenge_ttl(**req_copy)

    def test_update_challenge_ttl_value_error_with_retries(self):
        # Enable retries and run test_update_challenge_ttl_value_error.
        _service.enable_retries()
        self.test_update_challenge_ttl_value_error()

        # Disable retries and run test_update_challenge_ttl_value_error.
        _service.disable_retries()
        self.test_update_challenge_ttl_value_error()


class TestGetAutomaticHttpsRewrites:
    """
    Test Class for get_automatic_https_rewrites
    """

    @responses.activate
    def test_get_automatic_https_rewrites_all_params(self):
        """
        get_automatic_https_rewrites()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/automatic_https_rewrites')
        mock_response = '{"result": {"id": "automatic_https_rewrites", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_automatic_https_rewrites()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_automatic_https_rewrites_all_params_with_retries(self):
        # Enable retries and run test_get_automatic_https_rewrites_all_params.
        _service.enable_retries()
        self.test_get_automatic_https_rewrites_all_params()

        # Disable retries and run test_get_automatic_https_rewrites_all_params.
        _service.disable_retries()
        self.test_get_automatic_https_rewrites_all_params()

    @responses.activate
    def test_get_automatic_https_rewrites_value_error(self):
        """
        test_get_automatic_https_rewrites_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/automatic_https_rewrites')
        mock_response = '{"result": {"id": "automatic_https_rewrites", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_automatic_https_rewrites(**req_copy)

    def test_get_automatic_https_rewrites_value_error_with_retries(self):
        # Enable retries and run test_get_automatic_https_rewrites_value_error.
        _service.enable_retries()
        self.test_get_automatic_https_rewrites_value_error()

        # Disable retries and run test_get_automatic_https_rewrites_value_error.
        _service.disable_retries()
        self.test_get_automatic_https_rewrites_value_error()


class TestUpdateAutomaticHttpsRewrites:
    """
    Test Class for update_automatic_https_rewrites
    """

    @responses.activate
    def test_update_automatic_https_rewrites_all_params(self):
        """
        update_automatic_https_rewrites()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/automatic_https_rewrites')
        mock_response = '{"result": {"id": "automatic_https_rewrites", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 'off'

        # Invoke method
        response = _service.update_automatic_https_rewrites(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'off'

    def test_update_automatic_https_rewrites_all_params_with_retries(self):
        # Enable retries and run test_update_automatic_https_rewrites_all_params.
        _service.enable_retries()
        self.test_update_automatic_https_rewrites_all_params()

        # Disable retries and run test_update_automatic_https_rewrites_all_params.
        _service.disable_retries()
        self.test_update_automatic_https_rewrites_all_params()

    @responses.activate
    def test_update_automatic_https_rewrites_required_params(self):
        """
        test_update_automatic_https_rewrites_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/automatic_https_rewrites')
        mock_response = '{"result": {"id": "automatic_https_rewrites", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_automatic_https_rewrites()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_automatic_https_rewrites_required_params_with_retries(self):
        # Enable retries and run test_update_automatic_https_rewrites_required_params.
        _service.enable_retries()
        self.test_update_automatic_https_rewrites_required_params()

        # Disable retries and run test_update_automatic_https_rewrites_required_params.
        _service.disable_retries()
        self.test_update_automatic_https_rewrites_required_params()

    @responses.activate
    def test_update_automatic_https_rewrites_value_error(self):
        """
        test_update_automatic_https_rewrites_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/automatic_https_rewrites')
        mock_response = '{"result": {"id": "automatic_https_rewrites", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_automatic_https_rewrites(**req_copy)

    def test_update_automatic_https_rewrites_value_error_with_retries(self):
        # Enable retries and run test_update_automatic_https_rewrites_value_error.
        _service.enable_retries()
        self.test_update_automatic_https_rewrites_value_error()

        # Disable retries and run test_update_automatic_https_rewrites_value_error.
        _service.disable_retries()
        self.test_update_automatic_https_rewrites_value_error()


class TestGetTrueClientIp:
    """
    Test Class for get_true_client_ip
    """

    @responses.activate
    def test_get_true_client_ip_all_params(self):
        """
        get_true_client_ip()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/true_client_ip_header')
        mock_response = '{"result": {"id": "true_client_ip_header", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_true_client_ip()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_true_client_ip_all_params_with_retries(self):
        # Enable retries and run test_get_true_client_ip_all_params.
        _service.enable_retries()
        self.test_get_true_client_ip_all_params()

        # Disable retries and run test_get_true_client_ip_all_params.
        _service.disable_retries()
        self.test_get_true_client_ip_all_params()

    @responses.activate
    def test_get_true_client_ip_value_error(self):
        """
        test_get_true_client_ip_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/true_client_ip_header')
        mock_response = '{"result": {"id": "true_client_ip_header", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_true_client_ip(**req_copy)

    def test_get_true_client_ip_value_error_with_retries(self):
        # Enable retries and run test_get_true_client_ip_value_error.
        _service.enable_retries()
        self.test_get_true_client_ip_value_error()

        # Disable retries and run test_get_true_client_ip_value_error.
        _service.disable_retries()
        self.test_get_true_client_ip_value_error()


class TestUpdateTrueClientIp:
    """
    Test Class for update_true_client_ip
    """

    @responses.activate
    def test_update_true_client_ip_all_params(self):
        """
        update_true_client_ip()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/true_client_ip_header')
        mock_response = '{"result": {"id": "true_client_ip_header", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 'on'

        # Invoke method
        response = _service.update_true_client_ip(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'on'

    def test_update_true_client_ip_all_params_with_retries(self):
        # Enable retries and run test_update_true_client_ip_all_params.
        _service.enable_retries()
        self.test_update_true_client_ip_all_params()

        # Disable retries and run test_update_true_client_ip_all_params.
        _service.disable_retries()
        self.test_update_true_client_ip_all_params()

    @responses.activate
    def test_update_true_client_ip_required_params(self):
        """
        test_update_true_client_ip_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/true_client_ip_header')
        mock_response = '{"result": {"id": "true_client_ip_header", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_true_client_ip()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_true_client_ip_required_params_with_retries(self):
        # Enable retries and run test_update_true_client_ip_required_params.
        _service.enable_retries()
        self.test_update_true_client_ip_required_params()

        # Disable retries and run test_update_true_client_ip_required_params.
        _service.disable_retries()
        self.test_update_true_client_ip_required_params()

    @responses.activate
    def test_update_true_client_ip_value_error(self):
        """
        test_update_true_client_ip_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/true_client_ip_header')
        mock_response = '{"result": {"id": "true_client_ip_header", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_true_client_ip(**req_copy)

    def test_update_true_client_ip_value_error_with_retries(self):
        # Enable retries and run test_update_true_client_ip_value_error.
        _service.enable_retries()
        self.test_update_true_client_ip_value_error()

        # Disable retries and run test_update_true_client_ip_value_error.
        _service.disable_retries()
        self.test_update_true_client_ip_value_error()


class TestGetAlwaysUseHttps:
    """
    Test Class for get_always_use_https
    """

    @responses.activate
    def test_get_always_use_https_all_params(self):
        """
        get_always_use_https()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/always_use_https')
        mock_response = '{"result": {"id": "always_use_https", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_always_use_https()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_always_use_https_all_params_with_retries(self):
        # Enable retries and run test_get_always_use_https_all_params.
        _service.enable_retries()
        self.test_get_always_use_https_all_params()

        # Disable retries and run test_get_always_use_https_all_params.
        _service.disable_retries()
        self.test_get_always_use_https_all_params()

    @responses.activate
    def test_get_always_use_https_value_error(self):
        """
        test_get_always_use_https_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/always_use_https')
        mock_response = '{"result": {"id": "always_use_https", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_always_use_https(**req_copy)

    def test_get_always_use_https_value_error_with_retries(self):
        # Enable retries and run test_get_always_use_https_value_error.
        _service.enable_retries()
        self.test_get_always_use_https_value_error()

        # Disable retries and run test_get_always_use_https_value_error.
        _service.disable_retries()
        self.test_get_always_use_https_value_error()


class TestUpdateAlwaysUseHttps:
    """
    Test Class for update_always_use_https
    """

    @responses.activate
    def test_update_always_use_https_all_params(self):
        """
        update_always_use_https()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/always_use_https')
        mock_response = '{"result": {"id": "always_use_https", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 'on'

        # Invoke method
        response = _service.update_always_use_https(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'on'

    def test_update_always_use_https_all_params_with_retries(self):
        # Enable retries and run test_update_always_use_https_all_params.
        _service.enable_retries()
        self.test_update_always_use_https_all_params()

        # Disable retries and run test_update_always_use_https_all_params.
        _service.disable_retries()
        self.test_update_always_use_https_all_params()

    @responses.activate
    def test_update_always_use_https_required_params(self):
        """
        test_update_always_use_https_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/always_use_https')
        mock_response = '{"result": {"id": "always_use_https", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_always_use_https()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_always_use_https_required_params_with_retries(self):
        # Enable retries and run test_update_always_use_https_required_params.
        _service.enable_retries()
        self.test_update_always_use_https_required_params()

        # Disable retries and run test_update_always_use_https_required_params.
        _service.disable_retries()
        self.test_update_always_use_https_required_params()

    @responses.activate
    def test_update_always_use_https_value_error(self):
        """
        test_update_always_use_https_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/always_use_https')
        mock_response = '{"result": {"id": "always_use_https", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_always_use_https(**req_copy)

    def test_update_always_use_https_value_error_with_retries(self):
        # Enable retries and run test_update_always_use_https_value_error.
        _service.enable_retries()
        self.test_update_always_use_https_value_error()

        # Disable retries and run test_update_always_use_https_value_error.
        _service.disable_retries()
        self.test_update_always_use_https_value_error()


class TestGetImageSizeOptimization:
    """
    Test Class for get_image_size_optimization
    """

    @responses.activate
    def test_get_image_size_optimization_all_params(self):
        """
        get_image_size_optimization()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/image_size_optimization')
        mock_response = '{"result": {"id": "image_size_optimization", "value": "lossless", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_image_size_optimization()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_image_size_optimization_all_params_with_retries(self):
        # Enable retries and run test_get_image_size_optimization_all_params.
        _service.enable_retries()
        self.test_get_image_size_optimization_all_params()

        # Disable retries and run test_get_image_size_optimization_all_params.
        _service.disable_retries()
        self.test_get_image_size_optimization_all_params()

    @responses.activate
    def test_get_image_size_optimization_value_error(self):
        """
        test_get_image_size_optimization_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/image_size_optimization')
        mock_response = '{"result": {"id": "image_size_optimization", "value": "lossless", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_image_size_optimization(**req_copy)

    def test_get_image_size_optimization_value_error_with_retries(self):
        # Enable retries and run test_get_image_size_optimization_value_error.
        _service.enable_retries()
        self.test_get_image_size_optimization_value_error()

        # Disable retries and run test_get_image_size_optimization_value_error.
        _service.disable_retries()
        self.test_get_image_size_optimization_value_error()


class TestUpdateImageSizeOptimization:
    """
    Test Class for update_image_size_optimization
    """

    @responses.activate
    def test_update_image_size_optimization_all_params(self):
        """
        update_image_size_optimization()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/image_size_optimization')
        mock_response = '{"result": {"id": "image_size_optimization", "value": "lossless", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 'lossless'

        # Invoke method
        response = _service.update_image_size_optimization(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'lossless'

    def test_update_image_size_optimization_all_params_with_retries(self):
        # Enable retries and run test_update_image_size_optimization_all_params.
        _service.enable_retries()
        self.test_update_image_size_optimization_all_params()

        # Disable retries and run test_update_image_size_optimization_all_params.
        _service.disable_retries()
        self.test_update_image_size_optimization_all_params()

    @responses.activate
    def test_update_image_size_optimization_required_params(self):
        """
        test_update_image_size_optimization_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/image_size_optimization')
        mock_response = '{"result": {"id": "image_size_optimization", "value": "lossless", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_image_size_optimization()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_image_size_optimization_required_params_with_retries(self):
        # Enable retries and run test_update_image_size_optimization_required_params.
        _service.enable_retries()
        self.test_update_image_size_optimization_required_params()

        # Disable retries and run test_update_image_size_optimization_required_params.
        _service.disable_retries()
        self.test_update_image_size_optimization_required_params()

    @responses.activate
    def test_update_image_size_optimization_value_error(self):
        """
        test_update_image_size_optimization_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/image_size_optimization')
        mock_response = '{"result": {"id": "image_size_optimization", "value": "lossless", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_image_size_optimization(**req_copy)

    def test_update_image_size_optimization_value_error_with_retries(self):
        # Enable retries and run test_update_image_size_optimization_value_error.
        _service.enable_retries()
        self.test_update_image_size_optimization_value_error()

        # Disable retries and run test_update_image_size_optimization_value_error.
        _service.disable_retries()
        self.test_update_image_size_optimization_value_error()


class TestGetScriptLoadOptimization:
    """
    Test Class for get_script_load_optimization
    """

    @responses.activate
    def test_get_script_load_optimization_all_params(self):
        """
        get_script_load_optimization()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/script_load_optimization')
        mock_response = '{"result": {"id": "script_load_optimization", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_script_load_optimization()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_script_load_optimization_all_params_with_retries(self):
        # Enable retries and run test_get_script_load_optimization_all_params.
        _service.enable_retries()
        self.test_get_script_load_optimization_all_params()

        # Disable retries and run test_get_script_load_optimization_all_params.
        _service.disable_retries()
        self.test_get_script_load_optimization_all_params()

    @responses.activate
    def test_get_script_load_optimization_value_error(self):
        """
        test_get_script_load_optimization_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/script_load_optimization')
        mock_response = '{"result": {"id": "script_load_optimization", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_script_load_optimization(**req_copy)

    def test_get_script_load_optimization_value_error_with_retries(self):
        # Enable retries and run test_get_script_load_optimization_value_error.
        _service.enable_retries()
        self.test_get_script_load_optimization_value_error()

        # Disable retries and run test_get_script_load_optimization_value_error.
        _service.disable_retries()
        self.test_get_script_load_optimization_value_error()


class TestUpdateScriptLoadOptimization:
    """
    Test Class for update_script_load_optimization
    """

    @responses.activate
    def test_update_script_load_optimization_all_params(self):
        """
        update_script_load_optimization()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/script_load_optimization')
        mock_response = '{"result": {"id": "script_load_optimization", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 'on'

        # Invoke method
        response = _service.update_script_load_optimization(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'on'

    def test_update_script_load_optimization_all_params_with_retries(self):
        # Enable retries and run test_update_script_load_optimization_all_params.
        _service.enable_retries()
        self.test_update_script_load_optimization_all_params()

        # Disable retries and run test_update_script_load_optimization_all_params.
        _service.disable_retries()
        self.test_update_script_load_optimization_all_params()

    @responses.activate
    def test_update_script_load_optimization_required_params(self):
        """
        test_update_script_load_optimization_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/script_load_optimization')
        mock_response = '{"result": {"id": "script_load_optimization", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_script_load_optimization()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_script_load_optimization_required_params_with_retries(self):
        # Enable retries and run test_update_script_load_optimization_required_params.
        _service.enable_retries()
        self.test_update_script_load_optimization_required_params()

        # Disable retries and run test_update_script_load_optimization_required_params.
        _service.disable_retries()
        self.test_update_script_load_optimization_required_params()

    @responses.activate
    def test_update_script_load_optimization_value_error(self):
        """
        test_update_script_load_optimization_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/script_load_optimization')
        mock_response = '{"result": {"id": "script_load_optimization", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_script_load_optimization(**req_copy)

    def test_update_script_load_optimization_value_error_with_retries(self):
        # Enable retries and run test_update_script_load_optimization_value_error.
        _service.enable_retries()
        self.test_update_script_load_optimization_value_error()

        # Disable retries and run test_update_script_load_optimization_value_error.
        _service.disable_retries()
        self.test_update_script_load_optimization_value_error()


class TestGetImageLoadOptimization:
    """
    Test Class for get_image_load_optimization
    """

    @responses.activate
    def test_get_image_load_optimization_all_params(self):
        """
        get_image_load_optimization()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/image_load_optimization')
        mock_response = '{"result": {"id": "image_load_optimization", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_image_load_optimization()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_image_load_optimization_all_params_with_retries(self):
        # Enable retries and run test_get_image_load_optimization_all_params.
        _service.enable_retries()
        self.test_get_image_load_optimization_all_params()

        # Disable retries and run test_get_image_load_optimization_all_params.
        _service.disable_retries()
        self.test_get_image_load_optimization_all_params()

    @responses.activate
    def test_get_image_load_optimization_value_error(self):
        """
        test_get_image_load_optimization_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/image_load_optimization')
        mock_response = '{"result": {"id": "image_load_optimization", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_image_load_optimization(**req_copy)

    def test_get_image_load_optimization_value_error_with_retries(self):
        # Enable retries and run test_get_image_load_optimization_value_error.
        _service.enable_retries()
        self.test_get_image_load_optimization_value_error()

        # Disable retries and run test_get_image_load_optimization_value_error.
        _service.disable_retries()
        self.test_get_image_load_optimization_value_error()


class TestUpdateImageLoadOptimization:
    """
    Test Class for update_image_load_optimization
    """

    @responses.activate
    def test_update_image_load_optimization_all_params(self):
        """
        update_image_load_optimization()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/image_load_optimization')
        mock_response = '{"result": {"id": "image_load_optimization", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 'on'

        # Invoke method
        response = _service.update_image_load_optimization(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'on'

    def test_update_image_load_optimization_all_params_with_retries(self):
        # Enable retries and run test_update_image_load_optimization_all_params.
        _service.enable_retries()
        self.test_update_image_load_optimization_all_params()

        # Disable retries and run test_update_image_load_optimization_all_params.
        _service.disable_retries()
        self.test_update_image_load_optimization_all_params()

    @responses.activate
    def test_update_image_load_optimization_required_params(self):
        """
        test_update_image_load_optimization_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/image_load_optimization')
        mock_response = '{"result": {"id": "image_load_optimization", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_image_load_optimization()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_image_load_optimization_required_params_with_retries(self):
        # Enable retries and run test_update_image_load_optimization_required_params.
        _service.enable_retries()
        self.test_update_image_load_optimization_required_params()

        # Disable retries and run test_update_image_load_optimization_required_params.
        _service.disable_retries()
        self.test_update_image_load_optimization_required_params()

    @responses.activate
    def test_update_image_load_optimization_value_error(self):
        """
        test_update_image_load_optimization_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/image_load_optimization')
        mock_response = '{"result": {"id": "image_load_optimization", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_image_load_optimization(**req_copy)

    def test_update_image_load_optimization_value_error_with_retries(self):
        # Enable retries and run test_update_image_load_optimization_value_error.
        _service.enable_retries()
        self.test_update_image_load_optimization_value_error()

        # Disable retries and run test_update_image_load_optimization_value_error.
        _service.disable_retries()
        self.test_update_image_load_optimization_value_error()


class TestGetMinify:
    """
    Test Class for get_minify
    """

    @responses.activate
    def test_get_minify_all_params(self):
        """
        get_minify()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/minify')
        mock_response = '{"result": {"id": "minify", "value": {"css": "on", "html": "on", "js": "on"}, "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_minify()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_minify_all_params_with_retries(self):
        # Enable retries and run test_get_minify_all_params.
        _service.enable_retries()
        self.test_get_minify_all_params()

        # Disable retries and run test_get_minify_all_params.
        _service.disable_retries()
        self.test_get_minify_all_params()

    @responses.activate
    def test_get_minify_value_error(self):
        """
        test_get_minify_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/minify')
        mock_response = '{"result": {"id": "minify", "value": {"css": "on", "html": "on", "js": "on"}, "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_minify(**req_copy)

    def test_get_minify_value_error_with_retries(self):
        # Enable retries and run test_get_minify_value_error.
        _service.enable_retries()
        self.test_get_minify_value_error()

        # Disable retries and run test_get_minify_value_error.
        _service.disable_retries()
        self.test_get_minify_value_error()


class TestUpdateMinify:
    """
    Test Class for update_minify
    """

    @responses.activate
    def test_update_minify_all_params(self):
        """
        update_minify()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/minify')
        mock_response = '{"result": {"id": "minify", "value": {"css": "on", "html": "on", "js": "on"}, "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a MinifySettingValue model
        minify_setting_value_model = {}
        minify_setting_value_model['css'] = 'off'
        minify_setting_value_model['html'] = 'off'
        minify_setting_value_model['js'] = 'off'

        # Set up parameter values
        value = minify_setting_value_model

        # Invoke method
        response = _service.update_minify(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == minify_setting_value_model

    def test_update_minify_all_params_with_retries(self):
        # Enable retries and run test_update_minify_all_params.
        _service.enable_retries()
        self.test_update_minify_all_params()

        # Disable retries and run test_update_minify_all_params.
        _service.disable_retries()
        self.test_update_minify_all_params()

    @responses.activate
    def test_update_minify_required_params(self):
        """
        test_update_minify_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/minify')
        mock_response = '{"result": {"id": "minify", "value": {"css": "on", "html": "on", "js": "on"}, "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_minify()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_minify_required_params_with_retries(self):
        # Enable retries and run test_update_minify_required_params.
        _service.enable_retries()
        self.test_update_minify_required_params()

        # Disable retries and run test_update_minify_required_params.
        _service.disable_retries()
        self.test_update_minify_required_params()

    @responses.activate
    def test_update_minify_value_error(self):
        """
        test_update_minify_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/minify')
        mock_response = '{"result": {"id": "minify", "value": {"css": "on", "html": "on", "js": "on"}, "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_minify(**req_copy)

    def test_update_minify_value_error_with_retries(self):
        # Enable retries and run test_update_minify_value_error.
        _service.enable_retries()
        self.test_update_minify_value_error()

        # Disable retries and run test_update_minify_value_error.
        _service.disable_retries()
        self.test_update_minify_value_error()


class TestGetMinTlsVersion:
    """
    Test Class for get_min_tls_version
    """

    @responses.activate
    def test_get_min_tls_version_all_params(self):
        """
        get_min_tls_version()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/min_tls_version')
        mock_response = '{"result": {"id": "min_tls_version", "value": "1.2", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_min_tls_version()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_min_tls_version_all_params_with_retries(self):
        # Enable retries and run test_get_min_tls_version_all_params.
        _service.enable_retries()
        self.test_get_min_tls_version_all_params()

        # Disable retries and run test_get_min_tls_version_all_params.
        _service.disable_retries()
        self.test_get_min_tls_version_all_params()

    @responses.activate
    def test_get_min_tls_version_value_error(self):
        """
        test_get_min_tls_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/min_tls_version')
        mock_response = '{"result": {"id": "min_tls_version", "value": "1.2", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_min_tls_version(**req_copy)

    def test_get_min_tls_version_value_error_with_retries(self):
        # Enable retries and run test_get_min_tls_version_value_error.
        _service.enable_retries()
        self.test_get_min_tls_version_value_error()

        # Disable retries and run test_get_min_tls_version_value_error.
        _service.disable_retries()
        self.test_get_min_tls_version_value_error()


class TestUpdateMinTlsVersion:
    """
    Test Class for update_min_tls_version
    """

    @responses.activate
    def test_update_min_tls_version_all_params(self):
        """
        update_min_tls_version()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/min_tls_version')
        mock_response = '{"result": {"id": "min_tls_version", "value": "1.2", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = '1.2'

        # Invoke method
        response = _service.update_min_tls_version(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == '1.2'

    def test_update_min_tls_version_all_params_with_retries(self):
        # Enable retries and run test_update_min_tls_version_all_params.
        _service.enable_retries()
        self.test_update_min_tls_version_all_params()

        # Disable retries and run test_update_min_tls_version_all_params.
        _service.disable_retries()
        self.test_update_min_tls_version_all_params()

    @responses.activate
    def test_update_min_tls_version_required_params(self):
        """
        test_update_min_tls_version_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/min_tls_version')
        mock_response = '{"result": {"id": "min_tls_version", "value": "1.2", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_min_tls_version()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_min_tls_version_required_params_with_retries(self):
        # Enable retries and run test_update_min_tls_version_required_params.
        _service.enable_retries()
        self.test_update_min_tls_version_required_params()

        # Disable retries and run test_update_min_tls_version_required_params.
        _service.disable_retries()
        self.test_update_min_tls_version_required_params()

    @responses.activate
    def test_update_min_tls_version_value_error(self):
        """
        test_update_min_tls_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/min_tls_version')
        mock_response = '{"result": {"id": "min_tls_version", "value": "1.2", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_min_tls_version(**req_copy)

    def test_update_min_tls_version_value_error_with_retries(self):
        # Enable retries and run test_update_min_tls_version_value_error.
        _service.enable_retries()
        self.test_update_min_tls_version_value_error()

        # Disable retries and run test_update_min_tls_version_value_error.
        _service.disable_retries()
        self.test_update_min_tls_version_value_error()


class TestGetIpGeolocation:
    """
    Test Class for get_ip_geolocation
    """

    @responses.activate
    def test_get_ip_geolocation_all_params(self):
        """
        get_ip_geolocation()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/ip_geolocation')
        mock_response = '{"result": {"id": "ip_geolocation", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_ip_geolocation()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_ip_geolocation_all_params_with_retries(self):
        # Enable retries and run test_get_ip_geolocation_all_params.
        _service.enable_retries()
        self.test_get_ip_geolocation_all_params()

        # Disable retries and run test_get_ip_geolocation_all_params.
        _service.disable_retries()
        self.test_get_ip_geolocation_all_params()

    @responses.activate
    def test_get_ip_geolocation_value_error(self):
        """
        test_get_ip_geolocation_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/ip_geolocation')
        mock_response = '{"result": {"id": "ip_geolocation", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_ip_geolocation(**req_copy)

    def test_get_ip_geolocation_value_error_with_retries(self):
        # Enable retries and run test_get_ip_geolocation_value_error.
        _service.enable_retries()
        self.test_get_ip_geolocation_value_error()

        # Disable retries and run test_get_ip_geolocation_value_error.
        _service.disable_retries()
        self.test_get_ip_geolocation_value_error()


class TestUpdateIpGeolocation:
    """
    Test Class for update_ip_geolocation
    """

    @responses.activate
    def test_update_ip_geolocation_all_params(self):
        """
        update_ip_geolocation()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/ip_geolocation')
        mock_response = '{"result": {"id": "ip_geolocation", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 'on'

        # Invoke method
        response = _service.update_ip_geolocation(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'on'

    def test_update_ip_geolocation_all_params_with_retries(self):
        # Enable retries and run test_update_ip_geolocation_all_params.
        _service.enable_retries()
        self.test_update_ip_geolocation_all_params()

        # Disable retries and run test_update_ip_geolocation_all_params.
        _service.disable_retries()
        self.test_update_ip_geolocation_all_params()

    @responses.activate
    def test_update_ip_geolocation_required_params(self):
        """
        test_update_ip_geolocation_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/ip_geolocation')
        mock_response = '{"result": {"id": "ip_geolocation", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_ip_geolocation()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_ip_geolocation_required_params_with_retries(self):
        # Enable retries and run test_update_ip_geolocation_required_params.
        _service.enable_retries()
        self.test_update_ip_geolocation_required_params()

        # Disable retries and run test_update_ip_geolocation_required_params.
        _service.disable_retries()
        self.test_update_ip_geolocation_required_params()

    @responses.activate
    def test_update_ip_geolocation_value_error(self):
        """
        test_update_ip_geolocation_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/ip_geolocation')
        mock_response = '{"result": {"id": "ip_geolocation", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_ip_geolocation(**req_copy)

    def test_update_ip_geolocation_value_error_with_retries(self):
        # Enable retries and run test_update_ip_geolocation_value_error.
        _service.enable_retries()
        self.test_update_ip_geolocation_value_error()

        # Disable retries and run test_update_ip_geolocation_value_error.
        _service.disable_retries()
        self.test_update_ip_geolocation_value_error()


class TestGetServerSideExclude:
    """
    Test Class for get_server_side_exclude
    """

    @responses.activate
    def test_get_server_side_exclude_all_params(self):
        """
        get_server_side_exclude()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/server_side_exclude')
        mock_response = '{"result": {"id": "server_side_exclude", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_server_side_exclude()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_server_side_exclude_all_params_with_retries(self):
        # Enable retries and run test_get_server_side_exclude_all_params.
        _service.enable_retries()
        self.test_get_server_side_exclude_all_params()

        # Disable retries and run test_get_server_side_exclude_all_params.
        _service.disable_retries()
        self.test_get_server_side_exclude_all_params()

    @responses.activate
    def test_get_server_side_exclude_value_error(self):
        """
        test_get_server_side_exclude_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/server_side_exclude')
        mock_response = '{"result": {"id": "server_side_exclude", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_server_side_exclude(**req_copy)

    def test_get_server_side_exclude_value_error_with_retries(self):
        # Enable retries and run test_get_server_side_exclude_value_error.
        _service.enable_retries()
        self.test_get_server_side_exclude_value_error()

        # Disable retries and run test_get_server_side_exclude_value_error.
        _service.disable_retries()
        self.test_get_server_side_exclude_value_error()


class TestUpdateServerSideExclude:
    """
    Test Class for update_server_side_exclude
    """

    @responses.activate
    def test_update_server_side_exclude_all_params(self):
        """
        update_server_side_exclude()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/server_side_exclude')
        mock_response = '{"result": {"id": "server_side_exclude", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 'on'

        # Invoke method
        response = _service.update_server_side_exclude(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'on'

    def test_update_server_side_exclude_all_params_with_retries(self):
        # Enable retries and run test_update_server_side_exclude_all_params.
        _service.enable_retries()
        self.test_update_server_side_exclude_all_params()

        # Disable retries and run test_update_server_side_exclude_all_params.
        _service.disable_retries()
        self.test_update_server_side_exclude_all_params()

    @responses.activate
    def test_update_server_side_exclude_required_params(self):
        """
        test_update_server_side_exclude_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/server_side_exclude')
        mock_response = '{"result": {"id": "server_side_exclude", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_server_side_exclude()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_server_side_exclude_required_params_with_retries(self):
        # Enable retries and run test_update_server_side_exclude_required_params.
        _service.enable_retries()
        self.test_update_server_side_exclude_required_params()

        # Disable retries and run test_update_server_side_exclude_required_params.
        _service.disable_retries()
        self.test_update_server_side_exclude_required_params()

    @responses.activate
    def test_update_server_side_exclude_value_error(self):
        """
        test_update_server_side_exclude_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/server_side_exclude')
        mock_response = '{"result": {"id": "server_side_exclude", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_server_side_exclude(**req_copy)

    def test_update_server_side_exclude_value_error_with_retries(self):
        # Enable retries and run test_update_server_side_exclude_value_error.
        _service.enable_retries()
        self.test_update_server_side_exclude_value_error()

        # Disable retries and run test_update_server_side_exclude_value_error.
        _service.disable_retries()
        self.test_update_server_side_exclude_value_error()


class TestGetSecurityHeader:
    """
    Test Class for get_security_header
    """

    @responses.activate
    def test_get_security_header_all_params(self):
        """
        get_security_header()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/security_header')
        mock_response = '{"result": {"id": "security_header", "value": {"strict_transport_security": {"enabled": true, "max_age": 86400, "include_subdomains": true, "preload": true, "nosniff": true}}, "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_security_header()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_security_header_all_params_with_retries(self):
        # Enable retries and run test_get_security_header_all_params.
        _service.enable_retries()
        self.test_get_security_header_all_params()

        # Disable retries and run test_get_security_header_all_params.
        _service.disable_retries()
        self.test_get_security_header_all_params()

    @responses.activate
    def test_get_security_header_value_error(self):
        """
        test_get_security_header_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/security_header')
        mock_response = '{"result": {"id": "security_header", "value": {"strict_transport_security": {"enabled": true, "max_age": 86400, "include_subdomains": true, "preload": true, "nosniff": true}}, "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_security_header(**req_copy)

    def test_get_security_header_value_error_with_retries(self):
        # Enable retries and run test_get_security_header_value_error.
        _service.enable_retries()
        self.test_get_security_header_value_error()

        # Disable retries and run test_get_security_header_value_error.
        _service.disable_retries()
        self.test_get_security_header_value_error()


class TestUpdateSecurityHeader:
    """
    Test Class for update_security_header
    """

    @responses.activate
    def test_update_security_header_all_params(self):
        """
        update_security_header()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/security_header')
        mock_response = '{"result": {"id": "security_header", "value": {"strict_transport_security": {"enabled": true, "max_age": 86400, "include_subdomains": true, "preload": true, "nosniff": true}}, "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a SecurityHeaderSettingValueStrictTransportSecurity model
        security_header_setting_value_strict_transport_security_model = {}
        security_header_setting_value_strict_transport_security_model['enabled'] = True
        security_header_setting_value_strict_transport_security_model['max_age'] = 86400
        security_header_setting_value_strict_transport_security_model['include_subdomains'] = True
        security_header_setting_value_strict_transport_security_model['preload'] = True
        security_header_setting_value_strict_transport_security_model['nosniff'] = True

        # Construct a dict representation of a SecurityHeaderSettingValue model
        security_header_setting_value_model = {}
        security_header_setting_value_model['strict_transport_security'] = security_header_setting_value_strict_transport_security_model

        # Set up parameter values
        value = security_header_setting_value_model

        # Invoke method
        response = _service.update_security_header(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == security_header_setting_value_model

    def test_update_security_header_all_params_with_retries(self):
        # Enable retries and run test_update_security_header_all_params.
        _service.enable_retries()
        self.test_update_security_header_all_params()

        # Disable retries and run test_update_security_header_all_params.
        _service.disable_retries()
        self.test_update_security_header_all_params()

    @responses.activate
    def test_update_security_header_required_params(self):
        """
        test_update_security_header_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/security_header')
        mock_response = '{"result": {"id": "security_header", "value": {"strict_transport_security": {"enabled": true, "max_age": 86400, "include_subdomains": true, "preload": true, "nosniff": true}}, "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_security_header()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_security_header_required_params_with_retries(self):
        # Enable retries and run test_update_security_header_required_params.
        _service.enable_retries()
        self.test_update_security_header_required_params()

        # Disable retries and run test_update_security_header_required_params.
        _service.disable_retries()
        self.test_update_security_header_required_params()

    @responses.activate
    def test_update_security_header_value_error(self):
        """
        test_update_security_header_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/security_header')
        mock_response = '{"result": {"id": "security_header", "value": {"strict_transport_security": {"enabled": true, "max_age": 86400, "include_subdomains": true, "preload": true, "nosniff": true}}, "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_security_header(**req_copy)

    def test_update_security_header_value_error_with_retries(self):
        # Enable retries and run test_update_security_header_value_error.
        _service.enable_retries()
        self.test_update_security_header_value_error()

        # Disable retries and run test_update_security_header_value_error.
        _service.disable_retries()
        self.test_update_security_header_value_error()


class TestGetMobileRedirect:
    """
    Test Class for get_mobile_redirect
    """

    @responses.activate
    def test_get_mobile_redirect_all_params(self):
        """
        get_mobile_redirect()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/mobile_redirect')
        mock_response = '{"result": {"id": "mobile_redirect", "value": {"status": "on", "mobile_subdomain": "m", "strip_uri": false}, "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_mobile_redirect()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_mobile_redirect_all_params_with_retries(self):
        # Enable retries and run test_get_mobile_redirect_all_params.
        _service.enable_retries()
        self.test_get_mobile_redirect_all_params()

        # Disable retries and run test_get_mobile_redirect_all_params.
        _service.disable_retries()
        self.test_get_mobile_redirect_all_params()

    @responses.activate
    def test_get_mobile_redirect_value_error(self):
        """
        test_get_mobile_redirect_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/mobile_redirect')
        mock_response = '{"result": {"id": "mobile_redirect", "value": {"status": "on", "mobile_subdomain": "m", "strip_uri": false}, "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_mobile_redirect(**req_copy)

    def test_get_mobile_redirect_value_error_with_retries(self):
        # Enable retries and run test_get_mobile_redirect_value_error.
        _service.enable_retries()
        self.test_get_mobile_redirect_value_error()

        # Disable retries and run test_get_mobile_redirect_value_error.
        _service.disable_retries()
        self.test_get_mobile_redirect_value_error()


class TestUpdateMobileRedirect:
    """
    Test Class for update_mobile_redirect
    """

    @responses.activate
    def test_update_mobile_redirect_all_params(self):
        """
        update_mobile_redirect()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/mobile_redirect')
        mock_response = '{"result": {"id": "mobile_redirect", "value": {"status": "on", "mobile_subdomain": "m", "strip_uri": false}, "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a MobileRedirecSettingValue model
        mobile_redirec_setting_value_model = {}
        mobile_redirec_setting_value_model['status'] = 'on'
        mobile_redirec_setting_value_model['mobile_subdomain'] = 'm'
        mobile_redirec_setting_value_model['strip_uri'] = False

        # Set up parameter values
        value = mobile_redirec_setting_value_model

        # Invoke method
        response = _service.update_mobile_redirect(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == mobile_redirec_setting_value_model

    def test_update_mobile_redirect_all_params_with_retries(self):
        # Enable retries and run test_update_mobile_redirect_all_params.
        _service.enable_retries()
        self.test_update_mobile_redirect_all_params()

        # Disable retries and run test_update_mobile_redirect_all_params.
        _service.disable_retries()
        self.test_update_mobile_redirect_all_params()

    @responses.activate
    def test_update_mobile_redirect_required_params(self):
        """
        test_update_mobile_redirect_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/mobile_redirect')
        mock_response = '{"result": {"id": "mobile_redirect", "value": {"status": "on", "mobile_subdomain": "m", "strip_uri": false}, "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_mobile_redirect()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_mobile_redirect_required_params_with_retries(self):
        # Enable retries and run test_update_mobile_redirect_required_params.
        _service.enable_retries()
        self.test_update_mobile_redirect_required_params()

        # Disable retries and run test_update_mobile_redirect_required_params.
        _service.disable_retries()
        self.test_update_mobile_redirect_required_params()

    @responses.activate
    def test_update_mobile_redirect_value_error(self):
        """
        test_update_mobile_redirect_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/mobile_redirect')
        mock_response = '{"result": {"id": "mobile_redirect", "value": {"status": "on", "mobile_subdomain": "m", "strip_uri": false}, "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_mobile_redirect(**req_copy)

    def test_update_mobile_redirect_value_error_with_retries(self):
        # Enable retries and run test_update_mobile_redirect_value_error.
        _service.enable_retries()
        self.test_update_mobile_redirect_value_error()

        # Disable retries and run test_update_mobile_redirect_value_error.
        _service.disable_retries()
        self.test_update_mobile_redirect_value_error()


class TestGetPrefetchPreload:
    """
    Test Class for get_prefetch_preload
    """

    @responses.activate
    def test_get_prefetch_preload_all_params(self):
        """
        get_prefetch_preload()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/prefetch_preload')
        mock_response = '{"result": {"id": "prefetch_preload", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_prefetch_preload()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_prefetch_preload_all_params_with_retries(self):
        # Enable retries and run test_get_prefetch_preload_all_params.
        _service.enable_retries()
        self.test_get_prefetch_preload_all_params()

        # Disable retries and run test_get_prefetch_preload_all_params.
        _service.disable_retries()
        self.test_get_prefetch_preload_all_params()

    @responses.activate
    def test_get_prefetch_preload_value_error(self):
        """
        test_get_prefetch_preload_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/prefetch_preload')
        mock_response = '{"result": {"id": "prefetch_preload", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_prefetch_preload(**req_copy)

    def test_get_prefetch_preload_value_error_with_retries(self):
        # Enable retries and run test_get_prefetch_preload_value_error.
        _service.enable_retries()
        self.test_get_prefetch_preload_value_error()

        # Disable retries and run test_get_prefetch_preload_value_error.
        _service.disable_retries()
        self.test_get_prefetch_preload_value_error()


class TestUpdatePrefetchPreload:
    """
    Test Class for update_prefetch_preload
    """

    @responses.activate
    def test_update_prefetch_preload_all_params(self):
        """
        update_prefetch_preload()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/prefetch_preload')
        mock_response = '{"result": {"id": "prefetch_preload", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 'on'

        # Invoke method
        response = _service.update_prefetch_preload(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'on'

    def test_update_prefetch_preload_all_params_with_retries(self):
        # Enable retries and run test_update_prefetch_preload_all_params.
        _service.enable_retries()
        self.test_update_prefetch_preload_all_params()

        # Disable retries and run test_update_prefetch_preload_all_params.
        _service.disable_retries()
        self.test_update_prefetch_preload_all_params()

    @responses.activate
    def test_update_prefetch_preload_required_params(self):
        """
        test_update_prefetch_preload_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/prefetch_preload')
        mock_response = '{"result": {"id": "prefetch_preload", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_prefetch_preload()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_prefetch_preload_required_params_with_retries(self):
        # Enable retries and run test_update_prefetch_preload_required_params.
        _service.enable_retries()
        self.test_update_prefetch_preload_required_params()

        # Disable retries and run test_update_prefetch_preload_required_params.
        _service.disable_retries()
        self.test_update_prefetch_preload_required_params()

    @responses.activate
    def test_update_prefetch_preload_value_error(self):
        """
        test_update_prefetch_preload_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/prefetch_preload')
        mock_response = '{"result": {"id": "prefetch_preload", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_prefetch_preload(**req_copy)

    def test_update_prefetch_preload_value_error_with_retries(self):
        # Enable retries and run test_update_prefetch_preload_value_error.
        _service.enable_retries()
        self.test_update_prefetch_preload_value_error()

        # Disable retries and run test_update_prefetch_preload_value_error.
        _service.disable_retries()
        self.test_update_prefetch_preload_value_error()


class TestGetHttp2:
    """
    Test Class for get_http2
    """

    @responses.activate
    def test_get_http2_all_params(self):
        """
        get_http2()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/http2')
        mock_response = '{"result": {"id": "http2", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_http2()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_http2_all_params_with_retries(self):
        # Enable retries and run test_get_http2_all_params.
        _service.enable_retries()
        self.test_get_http2_all_params()

        # Disable retries and run test_get_http2_all_params.
        _service.disable_retries()
        self.test_get_http2_all_params()

    @responses.activate
    def test_get_http2_value_error(self):
        """
        test_get_http2_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/http2')
        mock_response = '{"result": {"id": "http2", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_http2(**req_copy)

    def test_get_http2_value_error_with_retries(self):
        # Enable retries and run test_get_http2_value_error.
        _service.enable_retries()
        self.test_get_http2_value_error()

        # Disable retries and run test_get_http2_value_error.
        _service.disable_retries()
        self.test_get_http2_value_error()


class TestUpdateHttp2:
    """
    Test Class for update_http2
    """

    @responses.activate
    def test_update_http2_all_params(self):
        """
        update_http2()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/http2')
        mock_response = '{"result": {"id": "http2", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 'on'

        # Invoke method
        response = _service.update_http2(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'on'

    def test_update_http2_all_params_with_retries(self):
        # Enable retries and run test_update_http2_all_params.
        _service.enable_retries()
        self.test_update_http2_all_params()

        # Disable retries and run test_update_http2_all_params.
        _service.disable_retries()
        self.test_update_http2_all_params()

    @responses.activate
    def test_update_http2_required_params(self):
        """
        test_update_http2_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/http2')
        mock_response = '{"result": {"id": "http2", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_http2()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_http2_required_params_with_retries(self):
        # Enable retries and run test_update_http2_required_params.
        _service.enable_retries()
        self.test_update_http2_required_params()

        # Disable retries and run test_update_http2_required_params.
        _service.disable_retries()
        self.test_update_http2_required_params()

    @responses.activate
    def test_update_http2_value_error(self):
        """
        test_update_http2_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/http2')
        mock_response = '{"result": {"id": "http2", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_http2(**req_copy)

    def test_update_http2_value_error_with_retries(self):
        # Enable retries and run test_update_http2_value_error.
        _service.enable_retries()
        self.test_update_http2_value_error()

        # Disable retries and run test_update_http2_value_error.
        _service.disable_retries()
        self.test_update_http2_value_error()


class TestGetHttp3:
    """
    Test Class for get_http3
    """

    @responses.activate
    def test_get_http3_all_params(self):
        """
        get_http3()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/http3')
        mock_response = '{"result": {"id": "http3", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_http3()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_http3_all_params_with_retries(self):
        # Enable retries and run test_get_http3_all_params.
        _service.enable_retries()
        self.test_get_http3_all_params()

        # Disable retries and run test_get_http3_all_params.
        _service.disable_retries()
        self.test_get_http3_all_params()

    @responses.activate
    def test_get_http3_value_error(self):
        """
        test_get_http3_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/http3')
        mock_response = '{"result": {"id": "http3", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_http3(**req_copy)

    def test_get_http3_value_error_with_retries(self):
        # Enable retries and run test_get_http3_value_error.
        _service.enable_retries()
        self.test_get_http3_value_error()

        # Disable retries and run test_get_http3_value_error.
        _service.disable_retries()
        self.test_get_http3_value_error()


class TestUpdateHttp3:
    """
    Test Class for update_http3
    """

    @responses.activate
    def test_update_http3_all_params(self):
        """
        update_http3()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/http3')
        mock_response = '{"result": {"id": "http3", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 'on'

        # Invoke method
        response = _service.update_http3(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'on'

    def test_update_http3_all_params_with_retries(self):
        # Enable retries and run test_update_http3_all_params.
        _service.enable_retries()
        self.test_update_http3_all_params()

        # Disable retries and run test_update_http3_all_params.
        _service.disable_retries()
        self.test_update_http3_all_params()

    @responses.activate
    def test_update_http3_required_params(self):
        """
        test_update_http3_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/http3')
        mock_response = '{"result": {"id": "http3", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_http3()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_http3_required_params_with_retries(self):
        # Enable retries and run test_update_http3_required_params.
        _service.enable_retries()
        self.test_update_http3_required_params()

        # Disable retries and run test_update_http3_required_params.
        _service.disable_retries()
        self.test_update_http3_required_params()

    @responses.activate
    def test_update_http3_value_error(self):
        """
        test_update_http3_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/http3')
        mock_response = '{"result": {"id": "http3", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_http3(**req_copy)

    def test_update_http3_value_error_with_retries(self):
        # Enable retries and run test_update_http3_value_error.
        _service.enable_retries()
        self.test_update_http3_value_error()

        # Disable retries and run test_update_http3_value_error.
        _service.disable_retries()
        self.test_update_http3_value_error()


class TestGetIpv6:
    """
    Test Class for get_ipv6
    """

    @responses.activate
    def test_get_ipv6_all_params(self):
        """
        get_ipv6()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/ipv6')
        mock_response = '{"result": {"id": "ipv6", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_ipv6()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_ipv6_all_params_with_retries(self):
        # Enable retries and run test_get_ipv6_all_params.
        _service.enable_retries()
        self.test_get_ipv6_all_params()

        # Disable retries and run test_get_ipv6_all_params.
        _service.disable_retries()
        self.test_get_ipv6_all_params()

    @responses.activate
    def test_get_ipv6_value_error(self):
        """
        test_get_ipv6_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/ipv6')
        mock_response = '{"result": {"id": "ipv6", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_ipv6(**req_copy)

    def test_get_ipv6_value_error_with_retries(self):
        # Enable retries and run test_get_ipv6_value_error.
        _service.enable_retries()
        self.test_get_ipv6_value_error()

        # Disable retries and run test_get_ipv6_value_error.
        _service.disable_retries()
        self.test_get_ipv6_value_error()


class TestUpdateIpv6:
    """
    Test Class for update_ipv6
    """

    @responses.activate
    def test_update_ipv6_all_params(self):
        """
        update_ipv6()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/ipv6')
        mock_response = '{"result": {"id": "ipv6", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 'on'

        # Invoke method
        response = _service.update_ipv6(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'on'

    def test_update_ipv6_all_params_with_retries(self):
        # Enable retries and run test_update_ipv6_all_params.
        _service.enable_retries()
        self.test_update_ipv6_all_params()

        # Disable retries and run test_update_ipv6_all_params.
        _service.disable_retries()
        self.test_update_ipv6_all_params()

    @responses.activate
    def test_update_ipv6_required_params(self):
        """
        test_update_ipv6_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/ipv6')
        mock_response = '{"result": {"id": "ipv6", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_ipv6()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_ipv6_required_params_with_retries(self):
        # Enable retries and run test_update_ipv6_required_params.
        _service.enable_retries()
        self.test_update_ipv6_required_params()

        # Disable retries and run test_update_ipv6_required_params.
        _service.disable_retries()
        self.test_update_ipv6_required_params()

    @responses.activate
    def test_update_ipv6_value_error(self):
        """
        test_update_ipv6_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/ipv6')
        mock_response = '{"result": {"id": "ipv6", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_ipv6(**req_copy)

    def test_update_ipv6_value_error_with_retries(self):
        # Enable retries and run test_update_ipv6_value_error.
        _service.enable_retries()
        self.test_update_ipv6_value_error()

        # Disable retries and run test_update_ipv6_value_error.
        _service.disable_retries()
        self.test_update_ipv6_value_error()


class TestGetWebSockets:
    """
    Test Class for get_web_sockets
    """

    @responses.activate
    def test_get_web_sockets_all_params(self):
        """
        get_web_sockets()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/websockets')
        mock_response = '{"result": {"id": "websockets", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_web_sockets()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_web_sockets_all_params_with_retries(self):
        # Enable retries and run test_get_web_sockets_all_params.
        _service.enable_retries()
        self.test_get_web_sockets_all_params()

        # Disable retries and run test_get_web_sockets_all_params.
        _service.disable_retries()
        self.test_get_web_sockets_all_params()

    @responses.activate
    def test_get_web_sockets_value_error(self):
        """
        test_get_web_sockets_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/websockets')
        mock_response = '{"result": {"id": "websockets", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_web_sockets(**req_copy)

    def test_get_web_sockets_value_error_with_retries(self):
        # Enable retries and run test_get_web_sockets_value_error.
        _service.enable_retries()
        self.test_get_web_sockets_value_error()

        # Disable retries and run test_get_web_sockets_value_error.
        _service.disable_retries()
        self.test_get_web_sockets_value_error()


class TestUpdateWebSockets:
    """
    Test Class for update_web_sockets
    """

    @responses.activate
    def test_update_web_sockets_all_params(self):
        """
        update_web_sockets()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/websockets')
        mock_response = '{"result": {"id": "websockets", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 'on'

        # Invoke method
        response = _service.update_web_sockets(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'on'

    def test_update_web_sockets_all_params_with_retries(self):
        # Enable retries and run test_update_web_sockets_all_params.
        _service.enable_retries()
        self.test_update_web_sockets_all_params()

        # Disable retries and run test_update_web_sockets_all_params.
        _service.disable_retries()
        self.test_update_web_sockets_all_params()

    @responses.activate
    def test_update_web_sockets_required_params(self):
        """
        test_update_web_sockets_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/websockets')
        mock_response = '{"result": {"id": "websockets", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_web_sockets()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_web_sockets_required_params_with_retries(self):
        # Enable retries and run test_update_web_sockets_required_params.
        _service.enable_retries()
        self.test_update_web_sockets_required_params()

        # Disable retries and run test_update_web_sockets_required_params.
        _service.disable_retries()
        self.test_update_web_sockets_required_params()

    @responses.activate
    def test_update_web_sockets_value_error(self):
        """
        test_update_web_sockets_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/websockets')
        mock_response = '{"result": {"id": "websockets", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_web_sockets(**req_copy)

    def test_update_web_sockets_value_error_with_retries(self):
        # Enable retries and run test_update_web_sockets_value_error.
        _service.enable_retries()
        self.test_update_web_sockets_value_error()

        # Disable retries and run test_update_web_sockets_value_error.
        _service.disable_retries()
        self.test_update_web_sockets_value_error()


class TestGetPseudoIpv4:
    """
    Test Class for get_pseudo_ipv4
    """

    @responses.activate
    def test_get_pseudo_ipv4_all_params(self):
        """
        get_pseudo_ipv4()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/pseudo_ipv4')
        mock_response = '{"result": {"id": "pseudo_ipv4", "value": "add_header", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_pseudo_ipv4()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_pseudo_ipv4_all_params_with_retries(self):
        # Enable retries and run test_get_pseudo_ipv4_all_params.
        _service.enable_retries()
        self.test_get_pseudo_ipv4_all_params()

        # Disable retries and run test_get_pseudo_ipv4_all_params.
        _service.disable_retries()
        self.test_get_pseudo_ipv4_all_params()

    @responses.activate
    def test_get_pseudo_ipv4_value_error(self):
        """
        test_get_pseudo_ipv4_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/pseudo_ipv4')
        mock_response = '{"result": {"id": "pseudo_ipv4", "value": "add_header", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_pseudo_ipv4(**req_copy)

    def test_get_pseudo_ipv4_value_error_with_retries(self):
        # Enable retries and run test_get_pseudo_ipv4_value_error.
        _service.enable_retries()
        self.test_get_pseudo_ipv4_value_error()

        # Disable retries and run test_get_pseudo_ipv4_value_error.
        _service.disable_retries()
        self.test_get_pseudo_ipv4_value_error()


class TestUpdatePseudoIpv4:
    """
    Test Class for update_pseudo_ipv4
    """

    @responses.activate
    def test_update_pseudo_ipv4_all_params(self):
        """
        update_pseudo_ipv4()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/pseudo_ipv4')
        mock_response = '{"result": {"id": "pseudo_ipv4", "value": "add_header", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 'add_header'

        # Invoke method
        response = _service.update_pseudo_ipv4(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'add_header'

    def test_update_pseudo_ipv4_all_params_with_retries(self):
        # Enable retries and run test_update_pseudo_ipv4_all_params.
        _service.enable_retries()
        self.test_update_pseudo_ipv4_all_params()

        # Disable retries and run test_update_pseudo_ipv4_all_params.
        _service.disable_retries()
        self.test_update_pseudo_ipv4_all_params()

    @responses.activate
    def test_update_pseudo_ipv4_required_params(self):
        """
        test_update_pseudo_ipv4_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/pseudo_ipv4')
        mock_response = '{"result": {"id": "pseudo_ipv4", "value": "add_header", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_pseudo_ipv4()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_pseudo_ipv4_required_params_with_retries(self):
        # Enable retries and run test_update_pseudo_ipv4_required_params.
        _service.enable_retries()
        self.test_update_pseudo_ipv4_required_params()

        # Disable retries and run test_update_pseudo_ipv4_required_params.
        _service.disable_retries()
        self.test_update_pseudo_ipv4_required_params()

    @responses.activate
    def test_update_pseudo_ipv4_value_error(self):
        """
        test_update_pseudo_ipv4_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/pseudo_ipv4')
        mock_response = '{"result": {"id": "pseudo_ipv4", "value": "add_header", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_pseudo_ipv4(**req_copy)

    def test_update_pseudo_ipv4_value_error_with_retries(self):
        # Enable retries and run test_update_pseudo_ipv4_value_error.
        _service.enable_retries()
        self.test_update_pseudo_ipv4_value_error()

        # Disable retries and run test_update_pseudo_ipv4_value_error.
        _service.disable_retries()
        self.test_update_pseudo_ipv4_value_error()


class TestGetResponseBuffering:
    """
    Test Class for get_response_buffering
    """

    @responses.activate
    def test_get_response_buffering_all_params(self):
        """
        get_response_buffering()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/response_buffering')
        mock_response = '{"result": {"id": "response_buffering", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_response_buffering()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_response_buffering_all_params_with_retries(self):
        # Enable retries and run test_get_response_buffering_all_params.
        _service.enable_retries()
        self.test_get_response_buffering_all_params()

        # Disable retries and run test_get_response_buffering_all_params.
        _service.disable_retries()
        self.test_get_response_buffering_all_params()

    @responses.activate
    def test_get_response_buffering_value_error(self):
        """
        test_get_response_buffering_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/response_buffering')
        mock_response = '{"result": {"id": "response_buffering", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_response_buffering(**req_copy)

    def test_get_response_buffering_value_error_with_retries(self):
        # Enable retries and run test_get_response_buffering_value_error.
        _service.enable_retries()
        self.test_get_response_buffering_value_error()

        # Disable retries and run test_get_response_buffering_value_error.
        _service.disable_retries()
        self.test_get_response_buffering_value_error()


class TestUpdateResponseBuffering:
    """
    Test Class for update_response_buffering
    """

    @responses.activate
    def test_update_response_buffering_all_params(self):
        """
        update_response_buffering()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/response_buffering')
        mock_response = '{"result": {"id": "response_buffering", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 'on'

        # Invoke method
        response = _service.update_response_buffering(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'on'

    def test_update_response_buffering_all_params_with_retries(self):
        # Enable retries and run test_update_response_buffering_all_params.
        _service.enable_retries()
        self.test_update_response_buffering_all_params()

        # Disable retries and run test_update_response_buffering_all_params.
        _service.disable_retries()
        self.test_update_response_buffering_all_params()

    @responses.activate
    def test_update_response_buffering_required_params(self):
        """
        test_update_response_buffering_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/response_buffering')
        mock_response = '{"result": {"id": "response_buffering", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_response_buffering()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_response_buffering_required_params_with_retries(self):
        # Enable retries and run test_update_response_buffering_required_params.
        _service.enable_retries()
        self.test_update_response_buffering_required_params()

        # Disable retries and run test_update_response_buffering_required_params.
        _service.disable_retries()
        self.test_update_response_buffering_required_params()

    @responses.activate
    def test_update_response_buffering_value_error(self):
        """
        test_update_response_buffering_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/response_buffering')
        mock_response = '{"result": {"id": "response_buffering", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_response_buffering(**req_copy)

    def test_update_response_buffering_value_error_with_retries(self):
        # Enable retries and run test_update_response_buffering_value_error.
        _service.enable_retries()
        self.test_update_response_buffering_value_error()

        # Disable retries and run test_update_response_buffering_value_error.
        _service.disable_retries()
        self.test_update_response_buffering_value_error()


class TestGetHotlinkProtection:
    """
    Test Class for get_hotlink_protection
    """

    @responses.activate
    def test_get_hotlink_protection_all_params(self):
        """
        get_hotlink_protection()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/hotlink_protection')
        mock_response = '{"result": {"id": "hotlink_protection", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_hotlink_protection()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_hotlink_protection_all_params_with_retries(self):
        # Enable retries and run test_get_hotlink_protection_all_params.
        _service.enable_retries()
        self.test_get_hotlink_protection_all_params()

        # Disable retries and run test_get_hotlink_protection_all_params.
        _service.disable_retries()
        self.test_get_hotlink_protection_all_params()

    @responses.activate
    def test_get_hotlink_protection_value_error(self):
        """
        test_get_hotlink_protection_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/hotlink_protection')
        mock_response = '{"result": {"id": "hotlink_protection", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_hotlink_protection(**req_copy)

    def test_get_hotlink_protection_value_error_with_retries(self):
        # Enable retries and run test_get_hotlink_protection_value_error.
        _service.enable_retries()
        self.test_get_hotlink_protection_value_error()

        # Disable retries and run test_get_hotlink_protection_value_error.
        _service.disable_retries()
        self.test_get_hotlink_protection_value_error()


class TestUpdateHotlinkProtection:
    """
    Test Class for update_hotlink_protection
    """

    @responses.activate
    def test_update_hotlink_protection_all_params(self):
        """
        update_hotlink_protection()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/hotlink_protection')
        mock_response = '{"result": {"id": "hotlink_protection", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 'on'

        # Invoke method
        response = _service.update_hotlink_protection(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'on'

    def test_update_hotlink_protection_all_params_with_retries(self):
        # Enable retries and run test_update_hotlink_protection_all_params.
        _service.enable_retries()
        self.test_update_hotlink_protection_all_params()

        # Disable retries and run test_update_hotlink_protection_all_params.
        _service.disable_retries()
        self.test_update_hotlink_protection_all_params()

    @responses.activate
    def test_update_hotlink_protection_required_params(self):
        """
        test_update_hotlink_protection_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/hotlink_protection')
        mock_response = '{"result": {"id": "hotlink_protection", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_hotlink_protection()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_hotlink_protection_required_params_with_retries(self):
        # Enable retries and run test_update_hotlink_protection_required_params.
        _service.enable_retries()
        self.test_update_hotlink_protection_required_params()

        # Disable retries and run test_update_hotlink_protection_required_params.
        _service.disable_retries()
        self.test_update_hotlink_protection_required_params()

    @responses.activate
    def test_update_hotlink_protection_value_error(self):
        """
        test_update_hotlink_protection_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/hotlink_protection')
        mock_response = '{"result": {"id": "hotlink_protection", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_hotlink_protection(**req_copy)

    def test_update_hotlink_protection_value_error_with_retries(self):
        # Enable retries and run test_update_hotlink_protection_value_error.
        _service.enable_retries()
        self.test_update_hotlink_protection_value_error()

        # Disable retries and run test_update_hotlink_protection_value_error.
        _service.disable_retries()
        self.test_update_hotlink_protection_value_error()


class TestGetMaxUpload:
    """
    Test Class for get_max_upload
    """

    @responses.activate
    def test_get_max_upload_all_params(self):
        """
        get_max_upload()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/max_upload')
        mock_response = '{"result": {"id": "max_upload", "value": 300, "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_max_upload()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_max_upload_all_params_with_retries(self):
        # Enable retries and run test_get_max_upload_all_params.
        _service.enable_retries()
        self.test_get_max_upload_all_params()

        # Disable retries and run test_get_max_upload_all_params.
        _service.disable_retries()
        self.test_get_max_upload_all_params()

    @responses.activate
    def test_get_max_upload_value_error(self):
        """
        test_get_max_upload_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/max_upload')
        mock_response = '{"result": {"id": "max_upload", "value": 300, "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_max_upload(**req_copy)

    def test_get_max_upload_value_error_with_retries(self):
        # Enable retries and run test_get_max_upload_value_error.
        _service.enable_retries()
        self.test_get_max_upload_value_error()

        # Disable retries and run test_get_max_upload_value_error.
        _service.disable_retries()
        self.test_get_max_upload_value_error()


class TestUpdateMaxUpload:
    """
    Test Class for update_max_upload
    """

    @responses.activate
    def test_update_max_upload_all_params(self):
        """
        update_max_upload()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/max_upload')
        mock_response = '{"result": {"id": "max_upload", "value": 300, "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 300

        # Invoke method
        response = _service.update_max_upload(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 300

    def test_update_max_upload_all_params_with_retries(self):
        # Enable retries and run test_update_max_upload_all_params.
        _service.enable_retries()
        self.test_update_max_upload_all_params()

        # Disable retries and run test_update_max_upload_all_params.
        _service.disable_retries()
        self.test_update_max_upload_all_params()

    @responses.activate
    def test_update_max_upload_required_params(self):
        """
        test_update_max_upload_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/max_upload')
        mock_response = '{"result": {"id": "max_upload", "value": 300, "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_max_upload()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_max_upload_required_params_with_retries(self):
        # Enable retries and run test_update_max_upload_required_params.
        _service.enable_retries()
        self.test_update_max_upload_required_params()

        # Disable retries and run test_update_max_upload_required_params.
        _service.disable_retries()
        self.test_update_max_upload_required_params()

    @responses.activate
    def test_update_max_upload_value_error(self):
        """
        test_update_max_upload_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/max_upload')
        mock_response = '{"result": {"id": "max_upload", "value": 300, "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_max_upload(**req_copy)

    def test_update_max_upload_value_error_with_retries(self):
        # Enable retries and run test_update_max_upload_value_error.
        _service.enable_retries()
        self.test_update_max_upload_value_error()

        # Disable retries and run test_update_max_upload_value_error.
        _service.disable_retries()
        self.test_update_max_upload_value_error()


class TestGetTlsClientAuth:
    """
    Test Class for get_tls_client_auth
    """

    @responses.activate
    def test_get_tls_client_auth_all_params(self):
        """
        get_tls_client_auth()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/tls_client_auth')
        mock_response = '{"result": {"id": "tls_client_auth", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_tls_client_auth()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_tls_client_auth_all_params_with_retries(self):
        # Enable retries and run test_get_tls_client_auth_all_params.
        _service.enable_retries()
        self.test_get_tls_client_auth_all_params()

        # Disable retries and run test_get_tls_client_auth_all_params.
        _service.disable_retries()
        self.test_get_tls_client_auth_all_params()

    @responses.activate
    def test_get_tls_client_auth_value_error(self):
        """
        test_get_tls_client_auth_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/tls_client_auth')
        mock_response = '{"result": {"id": "tls_client_auth", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_tls_client_auth(**req_copy)

    def test_get_tls_client_auth_value_error_with_retries(self):
        # Enable retries and run test_get_tls_client_auth_value_error.
        _service.enable_retries()
        self.test_get_tls_client_auth_value_error()

        # Disable retries and run test_get_tls_client_auth_value_error.
        _service.disable_retries()
        self.test_get_tls_client_auth_value_error()


class TestUpdateTlsClientAuth:
    """
    Test Class for update_tls_client_auth
    """

    @responses.activate
    def test_update_tls_client_auth_all_params(self):
        """
        update_tls_client_auth()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/tls_client_auth')
        mock_response = '{"result": {"id": "tls_client_auth", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 'on'

        # Invoke method
        response = _service.update_tls_client_auth(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'on'

    def test_update_tls_client_auth_all_params_with_retries(self):
        # Enable retries and run test_update_tls_client_auth_all_params.
        _service.enable_retries()
        self.test_update_tls_client_auth_all_params()

        # Disable retries and run test_update_tls_client_auth_all_params.
        _service.disable_retries()
        self.test_update_tls_client_auth_all_params()

    @responses.activate
    def test_update_tls_client_auth_required_params(self):
        """
        test_update_tls_client_auth_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/tls_client_auth')
        mock_response = '{"result": {"id": "tls_client_auth", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_tls_client_auth()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_tls_client_auth_required_params_with_retries(self):
        # Enable retries and run test_update_tls_client_auth_required_params.
        _service.enable_retries()
        self.test_update_tls_client_auth_required_params()

        # Disable retries and run test_update_tls_client_auth_required_params.
        _service.disable_retries()
        self.test_update_tls_client_auth_required_params()

    @responses.activate
    def test_update_tls_client_auth_value_error(self):
        """
        test_update_tls_client_auth_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/tls_client_auth')
        mock_response = '{"result": {"id": "tls_client_auth", "value": "off", "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_tls_client_auth(**req_copy)

    def test_update_tls_client_auth_value_error_with_retries(self):
        # Enable retries and run test_update_tls_client_auth_value_error.
        _service.enable_retries()
        self.test_update_tls_client_auth_value_error()

        # Disable retries and run test_update_tls_client_auth_value_error.
        _service.disable_retries()
        self.test_update_tls_client_auth_value_error()


class TestGetBrotli:
    """
    Test Class for get_brotli
    """

    @responses.activate
    def test_get_brotli_all_params(self):
        """
        get_brotli()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/brotli')
        mock_response = '{"result": {"id": "brotli", "value": "off", "editable": true, "modified_on": "2018-12-08T18:57:52.826Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_brotli()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_brotli_all_params_with_retries(self):
        # Enable retries and run test_get_brotli_all_params.
        _service.enable_retries()
        self.test_get_brotli_all_params()

        # Disable retries and run test_get_brotli_all_params.
        _service.disable_retries()
        self.test_get_brotli_all_params()

    @responses.activate
    def test_get_brotli_value_error(self):
        """
        test_get_brotli_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/brotli')
        mock_response = '{"result": {"id": "brotli", "value": "off", "editable": true, "modified_on": "2018-12-08T18:57:52.826Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_brotli(**req_copy)

    def test_get_brotli_value_error_with_retries(self):
        # Enable retries and run test_get_brotli_value_error.
        _service.enable_retries()
        self.test_get_brotli_value_error()

        # Disable retries and run test_get_brotli_value_error.
        _service.disable_retries()
        self.test_get_brotli_value_error()


class TestUpdateBrotli:
    """
    Test Class for update_brotli
    """

    @responses.activate
    def test_update_brotli_all_params(self):
        """
        update_brotli()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/brotli')
        mock_response = '{"result": {"id": "brotli", "value": "off", "editable": true, "modified_on": "2018-12-08T18:57:52.826Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 'on'

        # Invoke method
        response = _service.update_brotli(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'on'

    def test_update_brotli_all_params_with_retries(self):
        # Enable retries and run test_update_brotli_all_params.
        _service.enable_retries()
        self.test_update_brotli_all_params()

        # Disable retries and run test_update_brotli_all_params.
        _service.disable_retries()
        self.test_update_brotli_all_params()

    @responses.activate
    def test_update_brotli_required_params(self):
        """
        test_update_brotli_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/brotli')
        mock_response = '{"result": {"id": "brotli", "value": "off", "editable": true, "modified_on": "2018-12-08T18:57:52.826Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_brotli()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_brotli_required_params_with_retries(self):
        # Enable retries and run test_update_brotli_required_params.
        _service.enable_retries()
        self.test_update_brotli_required_params()

        # Disable retries and run test_update_brotli_required_params.
        _service.disable_retries()
        self.test_update_brotli_required_params()

    @responses.activate
    def test_update_brotli_value_error(self):
        """
        test_update_brotli_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/brotli')
        mock_response = '{"result": {"id": "brotli", "value": "off", "editable": true, "modified_on": "2018-12-08T18:57:52.826Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_brotli(**req_copy)

    def test_update_brotli_value_error_with_retries(self):
        # Enable retries and run test_update_brotli_value_error.
        _service.enable_retries()
        self.test_update_brotli_value_error()

        # Disable retries and run test_update_brotli_value_error.
        _service.disable_retries()
        self.test_update_brotli_value_error()


class TestGetProxyReadTimeout:
    """
    Test Class for get_proxy_read_timeout
    """

    @responses.activate
    def test_get_proxy_read_timeout_all_params(self):
        """
        get_proxy_read_timeout()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/proxy_read_timeout')
        mock_response = '{"result": {"id": "proxy_read_timeout", "value": 100, "editable": true, "modified_on": "2018-12-08T18:57:52.826Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_proxy_read_timeout()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_proxy_read_timeout_all_params_with_retries(self):
        # Enable retries and run test_get_proxy_read_timeout_all_params.
        _service.enable_retries()
        self.test_get_proxy_read_timeout_all_params()

        # Disable retries and run test_get_proxy_read_timeout_all_params.
        _service.disable_retries()
        self.test_get_proxy_read_timeout_all_params()

    @responses.activate
    def test_get_proxy_read_timeout_value_error(self):
        """
        test_get_proxy_read_timeout_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/proxy_read_timeout')
        mock_response = '{"result": {"id": "proxy_read_timeout", "value": 100, "editable": true, "modified_on": "2018-12-08T18:57:52.826Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_proxy_read_timeout(**req_copy)

    def test_get_proxy_read_timeout_value_error_with_retries(self):
        # Enable retries and run test_get_proxy_read_timeout_value_error.
        _service.enable_retries()
        self.test_get_proxy_read_timeout_value_error()

        # Disable retries and run test_get_proxy_read_timeout_value_error.
        _service.disable_retries()
        self.test_get_proxy_read_timeout_value_error()


class TestUpdateProxyReadTimeout:
    """
    Test Class for update_proxy_read_timeout
    """

    @responses.activate
    def test_update_proxy_read_timeout_all_params(self):
        """
        update_proxy_read_timeout()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/proxy_read_timeout')
        mock_response = '{"result": {"id": "proxy_read_timeout", "value": 100, "editable": true, "modified_on": "2018-12-08T18:57:52.826Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 600

        # Invoke method
        response = _service.update_proxy_read_timeout(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 600

    def test_update_proxy_read_timeout_all_params_with_retries(self):
        # Enable retries and run test_update_proxy_read_timeout_all_params.
        _service.enable_retries()
        self.test_update_proxy_read_timeout_all_params()

        # Disable retries and run test_update_proxy_read_timeout_all_params.
        _service.disable_retries()
        self.test_update_proxy_read_timeout_all_params()

    @responses.activate
    def test_update_proxy_read_timeout_required_params(self):
        """
        test_update_proxy_read_timeout_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/proxy_read_timeout')
        mock_response = '{"result": {"id": "proxy_read_timeout", "value": 100, "editable": true, "modified_on": "2018-12-08T18:57:52.826Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_proxy_read_timeout()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_proxy_read_timeout_required_params_with_retries(self):
        # Enable retries and run test_update_proxy_read_timeout_required_params.
        _service.enable_retries()
        self.test_update_proxy_read_timeout_required_params()

        # Disable retries and run test_update_proxy_read_timeout_required_params.
        _service.disable_retries()
        self.test_update_proxy_read_timeout_required_params()

    @responses.activate
    def test_update_proxy_read_timeout_value_error(self):
        """
        test_update_proxy_read_timeout_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/proxy_read_timeout')
        mock_response = '{"result": {"id": "proxy_read_timeout", "value": 100, "editable": true, "modified_on": "2018-12-08T18:57:52.826Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_proxy_read_timeout(**req_copy)

    def test_update_proxy_read_timeout_value_error_with_retries(self):
        # Enable retries and run test_update_proxy_read_timeout_value_error.
        _service.enable_retries()
        self.test_update_proxy_read_timeout_value_error()

        # Disable retries and run test_update_proxy_read_timeout_value_error.
        _service.disable_retries()
        self.test_update_proxy_read_timeout_value_error()


class TestGetBrowserCheck:
    """
    Test Class for get_browser_check
    """

    @responses.activate
    def test_get_browser_check_all_params(self):
        """
        get_browser_check()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/browser_check')
        mock_response = '{"result": {"id": "browser_check", "value": "off", "editable": true, "modified_on": "2018-12-08T18:57:14.506Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_browser_check()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_browser_check_all_params_with_retries(self):
        # Enable retries and run test_get_browser_check_all_params.
        _service.enable_retries()
        self.test_get_browser_check_all_params()

        # Disable retries and run test_get_browser_check_all_params.
        _service.disable_retries()
        self.test_get_browser_check_all_params()

    @responses.activate
    def test_get_browser_check_value_error(self):
        """
        test_get_browser_check_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/browser_check')
        mock_response = '{"result": {"id": "browser_check", "value": "off", "editable": true, "modified_on": "2018-12-08T18:57:14.506Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_browser_check(**req_copy)

    def test_get_browser_check_value_error_with_retries(self):
        # Enable retries and run test_get_browser_check_value_error.
        _service.enable_retries()
        self.test_get_browser_check_value_error()

        # Disable retries and run test_get_browser_check_value_error.
        _service.disable_retries()
        self.test_get_browser_check_value_error()


class TestUpdateBrowserCheck:
    """
    Test Class for update_browser_check
    """

    @responses.activate
    def test_update_browser_check_all_params(self):
        """
        update_browser_check()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/browser_check')
        mock_response = '{"result": {"id": "browser_check", "value": "off", "editable": true, "modified_on": "2018-12-08T18:57:14.506Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 'on'

        # Invoke method
        response = _service.update_browser_check(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'on'

    def test_update_browser_check_all_params_with_retries(self):
        # Enable retries and run test_update_browser_check_all_params.
        _service.enable_retries()
        self.test_update_browser_check_all_params()

        # Disable retries and run test_update_browser_check_all_params.
        _service.disable_retries()
        self.test_update_browser_check_all_params()

    @responses.activate
    def test_update_browser_check_required_params(self):
        """
        test_update_browser_check_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/browser_check')
        mock_response = '{"result": {"id": "browser_check", "value": "off", "editable": true, "modified_on": "2018-12-08T18:57:14.506Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_browser_check()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_browser_check_required_params_with_retries(self):
        # Enable retries and run test_update_browser_check_required_params.
        _service.enable_retries()
        self.test_update_browser_check_required_params()

        # Disable retries and run test_update_browser_check_required_params.
        _service.disable_retries()
        self.test_update_browser_check_required_params()

    @responses.activate
    def test_update_browser_check_value_error(self):
        """
        test_update_browser_check_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/browser_check')
        mock_response = '{"result": {"id": "browser_check", "value": "off", "editable": true, "modified_on": "2018-12-08T18:57:14.506Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_browser_check(**req_copy)

    def test_update_browser_check_value_error_with_retries(self):
        # Enable retries and run test_update_browser_check_value_error.
        _service.enable_retries()
        self.test_update_browser_check_value_error()

        # Disable retries and run test_update_browser_check_value_error.
        _service.disable_retries()
        self.test_update_browser_check_value_error()


class TestGetEnableErrorPagesOn:
    """
    Test Class for get_enable_error_pages_on
    """

    @responses.activate
    def test_get_enable_error_pages_on_all_params(self):
        """
        get_enable_error_pages_on()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/origin_error_page_pass_thru')
        mock_response = '{"result": {"id": "origin_error_page_pass_thru", "value": "off", "editable": true, "modified_on": "2018-12-08T18:57:52.826Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_enable_error_pages_on()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_enable_error_pages_on_all_params_with_retries(self):
        # Enable retries and run test_get_enable_error_pages_on_all_params.
        _service.enable_retries()
        self.test_get_enable_error_pages_on_all_params()

        # Disable retries and run test_get_enable_error_pages_on_all_params.
        _service.disable_retries()
        self.test_get_enable_error_pages_on_all_params()

    @responses.activate
    def test_get_enable_error_pages_on_value_error(self):
        """
        test_get_enable_error_pages_on_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/origin_error_page_pass_thru')
        mock_response = '{"result": {"id": "origin_error_page_pass_thru", "value": "off", "editable": true, "modified_on": "2018-12-08T18:57:52.826Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_enable_error_pages_on(**req_copy)

    def test_get_enable_error_pages_on_value_error_with_retries(self):
        # Enable retries and run test_get_enable_error_pages_on_value_error.
        _service.enable_retries()
        self.test_get_enable_error_pages_on_value_error()

        # Disable retries and run test_get_enable_error_pages_on_value_error.
        _service.disable_retries()
        self.test_get_enable_error_pages_on_value_error()


class TestUpdateEnableErrorPagesOn:
    """
    Test Class for update_enable_error_pages_on
    """

    @responses.activate
    def test_update_enable_error_pages_on_all_params(self):
        """
        update_enable_error_pages_on()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/origin_error_page_pass_thru')
        mock_response = '{"result": {"id": "origin_error_page_pass_thru", "value": "off", "editable": true, "modified_on": "2018-12-08T18:57:52.826Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 'on'

        # Invoke method
        response = _service.update_enable_error_pages_on(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'on'

    def test_update_enable_error_pages_on_all_params_with_retries(self):
        # Enable retries and run test_update_enable_error_pages_on_all_params.
        _service.enable_retries()
        self.test_update_enable_error_pages_on_all_params()

        # Disable retries and run test_update_enable_error_pages_on_all_params.
        _service.disable_retries()
        self.test_update_enable_error_pages_on_all_params()

    @responses.activate
    def test_update_enable_error_pages_on_required_params(self):
        """
        test_update_enable_error_pages_on_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/origin_error_page_pass_thru')
        mock_response = '{"result": {"id": "origin_error_page_pass_thru", "value": "off", "editable": true, "modified_on": "2018-12-08T18:57:52.826Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_enable_error_pages_on()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_enable_error_pages_on_required_params_with_retries(self):
        # Enable retries and run test_update_enable_error_pages_on_required_params.
        _service.enable_retries()
        self.test_update_enable_error_pages_on_required_params()

        # Disable retries and run test_update_enable_error_pages_on_required_params.
        _service.disable_retries()
        self.test_update_enable_error_pages_on_required_params()

    @responses.activate
    def test_update_enable_error_pages_on_value_error(self):
        """
        test_update_enable_error_pages_on_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/origin_error_page_pass_thru')
        mock_response = '{"result": {"id": "origin_error_page_pass_thru", "value": "off", "editable": true, "modified_on": "2018-12-08T18:57:52.826Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_enable_error_pages_on(**req_copy)

    def test_update_enable_error_pages_on_value_error_with_retries(self):
        # Enable retries and run test_update_enable_error_pages_on_value_error.
        _service.enable_retries()
        self.test_update_enable_error_pages_on_value_error()

        # Disable retries and run test_update_enable_error_pages_on_value_error.
        _service.disable_retries()
        self.test_update_enable_error_pages_on_value_error()


class TestGetWebApplicationFirewall:
    """
    Test Class for get_web_application_firewall
    """

    @responses.activate
    def test_get_web_application_firewall_all_params(self):
        """
        get_web_application_firewall()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/waf')
        mock_response = '{"result": {"id": "waf", "value": "off", "editable": true, "modified_on": "2018-12-08T18:57:43.889Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_web_application_firewall()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_web_application_firewall_all_params_with_retries(self):
        # Enable retries and run test_get_web_application_firewall_all_params.
        _service.enable_retries()
        self.test_get_web_application_firewall_all_params()

        # Disable retries and run test_get_web_application_firewall_all_params.
        _service.disable_retries()
        self.test_get_web_application_firewall_all_params()

    @responses.activate
    def test_get_web_application_firewall_value_error(self):
        """
        test_get_web_application_firewall_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/waf')
        mock_response = '{"result": {"id": "waf", "value": "off", "editable": true, "modified_on": "2018-12-08T18:57:43.889Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_web_application_firewall(**req_copy)

    def test_get_web_application_firewall_value_error_with_retries(self):
        # Enable retries and run test_get_web_application_firewall_value_error.
        _service.enable_retries()
        self.test_get_web_application_firewall_value_error()

        # Disable retries and run test_get_web_application_firewall_value_error.
        _service.disable_retries()
        self.test_get_web_application_firewall_value_error()


class TestUpdateWebApplicationFirewall:
    """
    Test Class for update_web_application_firewall
    """

    @responses.activate
    def test_update_web_application_firewall_all_params(self):
        """
        update_web_application_firewall()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/waf')
        mock_response = '{"result": {"id": "waf", "value": "off", "editable": true, "modified_on": "2018-12-08T18:57:43.889Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 'on'

        # Invoke method
        response = _service.update_web_application_firewall(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'on'

    def test_update_web_application_firewall_all_params_with_retries(self):
        # Enable retries and run test_update_web_application_firewall_all_params.
        _service.enable_retries()
        self.test_update_web_application_firewall_all_params()

        # Disable retries and run test_update_web_application_firewall_all_params.
        _service.disable_retries()
        self.test_update_web_application_firewall_all_params()

    @responses.activate
    def test_update_web_application_firewall_required_params(self):
        """
        test_update_web_application_firewall_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/waf')
        mock_response = '{"result": {"id": "waf", "value": "off", "editable": true, "modified_on": "2018-12-08T18:57:43.889Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_web_application_firewall()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_web_application_firewall_required_params_with_retries(self):
        # Enable retries and run test_update_web_application_firewall_required_params.
        _service.enable_retries()
        self.test_update_web_application_firewall_required_params()

        # Disable retries and run test_update_web_application_firewall_required_params.
        _service.disable_retries()
        self.test_update_web_application_firewall_required_params()

    @responses.activate
    def test_update_web_application_firewall_value_error(self):
        """
        test_update_web_application_firewall_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/waf')
        mock_response = '{"result": {"id": "waf", "value": "off", "editable": true, "modified_on": "2018-12-08T18:57:43.889Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_web_application_firewall(**req_copy)

    def test_update_web_application_firewall_value_error_with_retries(self):
        # Enable retries and run test_update_web_application_firewall_value_error.
        _service.enable_retries()
        self.test_update_web_application_firewall_value_error()

        # Disable retries and run test_update_web_application_firewall_value_error.
        _service.disable_retries()
        self.test_update_web_application_firewall_value_error()


class TestGetCiphers:
    """
    Test Class for get_ciphers
    """

    @responses.activate
    def test_get_ciphers_all_params(self):
        """
        get_ciphers()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/ciphers')
        mock_response = '{"result": {"id": "ciphers", "value": ["value"], "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_ciphers()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_ciphers_all_params_with_retries(self):
        # Enable retries and run test_get_ciphers_all_params.
        _service.enable_retries()
        self.test_get_ciphers_all_params()

        # Disable retries and run test_get_ciphers_all_params.
        _service.disable_retries()
        self.test_get_ciphers_all_params()

    @responses.activate
    def test_get_ciphers_value_error(self):
        """
        test_get_ciphers_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/ciphers')
        mock_response = '{"result": {"id": "ciphers", "value": ["value"], "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_ciphers(**req_copy)

    def test_get_ciphers_value_error_with_retries(self):
        # Enable retries and run test_get_ciphers_value_error.
        _service.enable_retries()
        self.test_get_ciphers_value_error()

        # Disable retries and run test_get_ciphers_value_error.
        _service.disable_retries()
        self.test_get_ciphers_value_error()


class TestUpdateCiphers:
    """
    Test Class for update_ciphers
    """

    @responses.activate
    def test_update_ciphers_all_params(self):
        """
        update_ciphers()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/ciphers')
        mock_response = '{"result": {"id": "ciphers", "value": ["value"], "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = ['AES256-GCM-SHA384', 'AES256-SHA256']

        # Invoke method
        response = _service.update_ciphers(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == ['AES256-GCM-SHA384', 'AES256-SHA256']

    def test_update_ciphers_all_params_with_retries(self):
        # Enable retries and run test_update_ciphers_all_params.
        _service.enable_retries()
        self.test_update_ciphers_all_params()

        # Disable retries and run test_update_ciphers_all_params.
        _service.disable_retries()
        self.test_update_ciphers_all_params()

    @responses.activate
    def test_update_ciphers_required_params(self):
        """
        test_update_ciphers_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/ciphers')
        mock_response = '{"result": {"id": "ciphers", "value": ["value"], "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_ciphers()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_ciphers_required_params_with_retries(self):
        # Enable retries and run test_update_ciphers_required_params.
        _service.enable_retries()
        self.test_update_ciphers_required_params()

        # Disable retries and run test_update_ciphers_required_params.
        _service.disable_retries()
        self.test_update_ciphers_required_params()

    @responses.activate
    def test_update_ciphers_value_error(self):
        """
        test_update_ciphers_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/ciphers')
        mock_response = '{"result": {"id": "ciphers", "value": ["value"], "editable": true, "modified_on": "2018-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_ciphers(**req_copy)

    def test_update_ciphers_value_error_with_retries(self):
        # Enable retries and run test_update_ciphers_value_error.
        _service.enable_retries()
        self.test_update_ciphers_value_error()

        # Disable retries and run test_update_ciphers_value_error.
        _service.disable_retries()
        self.test_update_ciphers_value_error()


class TestGetOriginMaxHttpVersion:
    """
    Test Class for get_origin_max_http_version
    """

    @responses.activate
    def test_get_origin_max_http_version_all_params(self):
        """
        get_origin_max_http_version()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/origin_max_http_version')
        mock_response = '{"result": {"id": "origin_max_http_version", "value": "1", "editable": true, "modified_on": "2023-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_origin_max_http_version()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_origin_max_http_version_all_params_with_retries(self):
        # Enable retries and run test_get_origin_max_http_version_all_params.
        _service.enable_retries()
        self.test_get_origin_max_http_version_all_params()

        # Disable retries and run test_get_origin_max_http_version_all_params.
        _service.disable_retries()
        self.test_get_origin_max_http_version_all_params()

    @responses.activate
    def test_get_origin_max_http_version_value_error(self):
        """
        test_get_origin_max_http_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/origin_max_http_version')
        mock_response = '{"result": {"id": "origin_max_http_version", "value": "1", "editable": true, "modified_on": "2023-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_origin_max_http_version(**req_copy)

    def test_get_origin_max_http_version_value_error_with_retries(self):
        # Enable retries and run test_get_origin_max_http_version_value_error.
        _service.enable_retries()
        self.test_get_origin_max_http_version_value_error()

        # Disable retries and run test_get_origin_max_http_version_value_error.
        _service.disable_retries()
        self.test_get_origin_max_http_version_value_error()


class TestUpdateOriginMaxHttpVersion:
    """
    Test Class for update_origin_max_http_version
    """

    @responses.activate
    def test_update_origin_max_http_version_all_params(self):
        """
        update_origin_max_http_version()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/origin_max_http_version')
        mock_response = '{"result": {"id": "origin_max_http_version", "value": "1", "editable": true, "modified_on": "2023-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = '1'

        # Invoke method
        response = _service.update_origin_max_http_version(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == '1'

    def test_update_origin_max_http_version_all_params_with_retries(self):
        # Enable retries and run test_update_origin_max_http_version_all_params.
        _service.enable_retries()
        self.test_update_origin_max_http_version_all_params()

        # Disable retries and run test_update_origin_max_http_version_all_params.
        _service.disable_retries()
        self.test_update_origin_max_http_version_all_params()

    @responses.activate
    def test_update_origin_max_http_version_required_params(self):
        """
        test_update_origin_max_http_version_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/origin_max_http_version')
        mock_response = '{"result": {"id": "origin_max_http_version", "value": "1", "editable": true, "modified_on": "2023-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_origin_max_http_version()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_origin_max_http_version_required_params_with_retries(self):
        # Enable retries and run test_update_origin_max_http_version_required_params.
        _service.enable_retries()
        self.test_update_origin_max_http_version_required_params()

        # Disable retries and run test_update_origin_max_http_version_required_params.
        _service.disable_retries()
        self.test_update_origin_max_http_version_required_params()

    @responses.activate
    def test_update_origin_max_http_version_value_error(self):
        """
        test_update_origin_max_http_version_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/origin_max_http_version')
        mock_response = '{"result": {"id": "origin_max_http_version", "value": "1", "editable": true, "modified_on": "2023-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_origin_max_http_version(**req_copy)

    def test_update_origin_max_http_version_value_error_with_retries(self):
        # Enable retries and run test_update_origin_max_http_version_value_error.
        _service.enable_retries()
        self.test_update_origin_max_http_version_value_error()

        # Disable retries and run test_update_origin_max_http_version_value_error.
        _service.disable_retries()
        self.test_update_origin_max_http_version_value_error()


class TestGetOriginPostQuantumEncryption:
    """
    Test Class for get_origin_post_quantum_encryption
    """

    @responses.activate
    def test_get_origin_post_quantum_encryption_all_params(self):
        """
        get_origin_post_quantum_encryption()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/cache/origin_post_quantum_encryption')
        mock_response = '{"result": {"id": "origin_pqe", "value": "off", "editable": true, "modified_on": "2023-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_origin_post_quantum_encryption()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_origin_post_quantum_encryption_all_params_with_retries(self):
        # Enable retries and run test_get_origin_post_quantum_encryption_all_params.
        _service.enable_retries()
        self.test_get_origin_post_quantum_encryption_all_params()

        # Disable retries and run test_get_origin_post_quantum_encryption_all_params.
        _service.disable_retries()
        self.test_get_origin_post_quantum_encryption_all_params()

    @responses.activate
    def test_get_origin_post_quantum_encryption_value_error(self):
        """
        test_get_origin_post_quantum_encryption_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/cache/origin_post_quantum_encryption')
        mock_response = '{"result": {"id": "origin_pqe", "value": "off", "editable": true, "modified_on": "2023-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_origin_post_quantum_encryption(**req_copy)

    def test_get_origin_post_quantum_encryption_value_error_with_retries(self):
        # Enable retries and run test_get_origin_post_quantum_encryption_value_error.
        _service.enable_retries()
        self.test_get_origin_post_quantum_encryption_value_error()

        # Disable retries and run test_get_origin_post_quantum_encryption_value_error.
        _service.disable_retries()
        self.test_get_origin_post_quantum_encryption_value_error()


class TestUpdateOriginPostQuantumEncryption:
    """
    Test Class for update_origin_post_quantum_encryption
    """

    @responses.activate
    def test_update_origin_post_quantum_encryption_all_params(self):
        """
        update_origin_post_quantum_encryption()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/cache/origin_post_quantum_encryption')
        mock_response = '{"result": {"id": "origin_pqe", "value": "off", "editable": true, "modified_on": "2023-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 'preferred'

        # Invoke method
        response = _service.update_origin_post_quantum_encryption(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'preferred'

    def test_update_origin_post_quantum_encryption_all_params_with_retries(self):
        # Enable retries and run test_update_origin_post_quantum_encryption_all_params.
        _service.enable_retries()
        self.test_update_origin_post_quantum_encryption_all_params()

        # Disable retries and run test_update_origin_post_quantum_encryption_all_params.
        _service.disable_retries()
        self.test_update_origin_post_quantum_encryption_all_params()

    @responses.activate
    def test_update_origin_post_quantum_encryption_required_params(self):
        """
        test_update_origin_post_quantum_encryption_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/cache/origin_post_quantum_encryption')
        mock_response = '{"result": {"id": "origin_pqe", "value": "off", "editable": true, "modified_on": "2023-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_origin_post_quantum_encryption()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_origin_post_quantum_encryption_required_params_with_retries(self):
        # Enable retries and run test_update_origin_post_quantum_encryption_required_params.
        _service.enable_retries()
        self.test_update_origin_post_quantum_encryption_required_params()

        # Disable retries and run test_update_origin_post_quantum_encryption_required_params.
        _service.disable_retries()
        self.test_update_origin_post_quantum_encryption_required_params()

    @responses.activate
    def test_update_origin_post_quantum_encryption_value_error(self):
        """
        test_update_origin_post_quantum_encryption_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/cache/origin_post_quantum_encryption')
        mock_response = '{"result": {"id": "origin_pqe", "value": "off", "editable": true, "modified_on": "2023-09-14T09:49:19.524Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_origin_post_quantum_encryption(**req_copy)

    def test_update_origin_post_quantum_encryption_value_error_with_retries(self):
        # Enable retries and run test_update_origin_post_quantum_encryption_value_error.
        _service.enable_retries()
        self.test_update_origin_post_quantum_encryption_value_error()

        # Disable retries and run test_update_origin_post_quantum_encryption_value_error.
        _service.disable_retries()
        self.test_update_origin_post_quantum_encryption_value_error()


class TestGetLogRetention:
    """
    Test Class for get_log_retention
    """

    @responses.activate
    def test_get_log_retention_all_params(self):
        """
        get_log_retention()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/logs/retention')
        mock_response = '{"success": true, "result": {"flag": true}, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        crn = 'testString'
        zone_identifier = 'testString'

        # Invoke method
        response = _service.get_log_retention(
            crn,
            zone_identifier,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_log_retention_all_params_with_retries(self):
        # Enable retries and run test_get_log_retention_all_params.
        _service.enable_retries()
        self.test_get_log_retention_all_params()

        # Disable retries and run test_get_log_retention_all_params.
        _service.disable_retries()
        self.test_get_log_retention_all_params()

    @responses.activate
    def test_get_log_retention_value_error(self):
        """
        test_get_log_retention_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/logs/retention')
        mock_response = '{"success": true, "result": {"flag": true}, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        crn = 'testString'
        zone_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "crn": crn,
            "zone_identifier": zone_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_log_retention(**req_copy)

    def test_get_log_retention_value_error_with_retries(self):
        # Enable retries and run test_get_log_retention_value_error.
        _service.enable_retries()
        self.test_get_log_retention_value_error()

        # Disable retries and run test_get_log_retention_value_error.
        _service.disable_retries()
        self.test_get_log_retention_value_error()


class TestUpdateLogRetention:
    """
    Test Class for update_log_retention
    """

    @responses.activate
    def test_update_log_retention_all_params(self):
        """
        update_log_retention()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/logs/retention')
        mock_response = '{"success": true, "result": {"flag": true}, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        crn = 'testString'
        zone_identifier = 'testString'
        flag = True

        # Invoke method
        response = _service.update_log_retention(
            crn,
            zone_identifier,
            flag=flag,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['flag'] == True

    def test_update_log_retention_all_params_with_retries(self):
        # Enable retries and run test_update_log_retention_all_params.
        _service.enable_retries()
        self.test_update_log_retention_all_params()

        # Disable retries and run test_update_log_retention_all_params.
        _service.disable_retries()
        self.test_update_log_retention_all_params()

    @responses.activate
    def test_update_log_retention_required_params(self):
        """
        test_update_log_retention_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/logs/retention')
        mock_response = '{"success": true, "result": {"flag": true}, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        crn = 'testString'
        zone_identifier = 'testString'

        # Invoke method
        response = _service.update_log_retention(
            crn,
            zone_identifier,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_log_retention_required_params_with_retries(self):
        # Enable retries and run test_update_log_retention_required_params.
        _service.enable_retries()
        self.test_update_log_retention_required_params()

        # Disable retries and run test_update_log_retention_required_params.
        _service.disable_retries()
        self.test_update_log_retention_required_params()

    @responses.activate
    def test_update_log_retention_value_error(self):
        """
        test_update_log_retention_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/logs/retention')
        mock_response = '{"success": true, "result": {"flag": true}, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        crn = 'testString'
        zone_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "crn": crn,
            "zone_identifier": zone_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_log_retention(**req_copy)

    def test_update_log_retention_value_error_with_retries(self):
        # Enable retries and run test_update_log_retention_value_error.
        _service.enable_retries()
        self.test_update_log_retention_value_error()

        # Disable retries and run test_update_log_retention_value_error.
        _service.disable_retries()
        self.test_update_log_retention_value_error()


class TestGetBotManagement:
    """
    Test Class for get_bot_management
    """

    @responses.activate
    def test_get_bot_management_all_params(self):
        """
        get_bot_management()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/bot_management')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"session_score": false, "enable_js": false, "use_latest_model": false, "ai_bots_protection": "block"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_bot_management()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_bot_management_all_params_with_retries(self):
        # Enable retries and run test_get_bot_management_all_params.
        _service.enable_retries()
        self.test_get_bot_management_all_params()

        # Disable retries and run test_get_bot_management_all_params.
        _service.disable_retries()
        self.test_get_bot_management_all_params()

    @responses.activate
    def test_get_bot_management_value_error(self):
        """
        test_get_bot_management_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/bot_management')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"session_score": false, "enable_js": false, "use_latest_model": false, "ai_bots_protection": "block"}}'
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
                _service.get_bot_management(**req_copy)

    def test_get_bot_management_value_error_with_retries(self):
        # Enable retries and run test_get_bot_management_value_error.
        _service.enable_retries()
        self.test_get_bot_management_value_error()

        # Disable retries and run test_get_bot_management_value_error.
        _service.disable_retries()
        self.test_get_bot_management_value_error()


class TestUpdateBotManagement:
    """
    Test Class for update_bot_management
    """

    @responses.activate
    def test_update_bot_management_all_params(self):
        """
        update_bot_management()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/bot_management')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"session_score": false, "enable_js": false, "use_latest_model": false, "ai_bots_protection": "block"}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        session_score = False
        enable_js = False
        use_latest_model = False
        ai_bots_protection = 'block'

        # Invoke method
        response = _service.update_bot_management(
            session_score=session_score,
            enable_js=enable_js,
            use_latest_model=use_latest_model,
            ai_bots_protection=ai_bots_protection,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['session_score'] == False
        assert req_body['enable_js'] == False
        assert req_body['use_latest_model'] == False
        assert req_body['ai_bots_protection'] == 'block'

    def test_update_bot_management_all_params_with_retries(self):
        # Enable retries and run test_update_bot_management_all_params.
        _service.enable_retries()
        self.test_update_bot_management_all_params()

        # Disable retries and run test_update_bot_management_all_params.
        _service.disable_retries()
        self.test_update_bot_management_all_params()

    @responses.activate
    def test_update_bot_management_required_params(self):
        """
        test_update_bot_management_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/bot_management')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"session_score": false, "enable_js": false, "use_latest_model": false, "ai_bots_protection": "block"}}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_bot_management()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_bot_management_required_params_with_retries(self):
        # Enable retries and run test_update_bot_management_required_params.
        _service.enable_retries()
        self.test_update_bot_management_required_params()

        # Disable retries and run test_update_bot_management_required_params.
        _service.disable_retries()
        self.test_update_bot_management_required_params()

    @responses.activate
    def test_update_bot_management_value_error(self):
        """
        test_update_bot_management_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/bot_management')
        mock_response = '{"success": true, "errors": [["errors"]], "messages": [["messages"]], "result": {"session_score": false, "enable_js": false, "use_latest_model": false, "ai_bots_protection": "block"}}'
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
                _service.update_bot_management(**req_copy)

    def test_update_bot_management_value_error_with_retries(self):
        # Enable retries and run test_update_bot_management_value_error.
        _service.enable_retries()
        self.test_update_bot_management_value_error()

        # Disable retries and run test_update_bot_management_value_error.
        _service.disable_retries()
        self.test_update_bot_management_value_error()


class TestGetReplaceInsecureJs:
    """
    Test Class for get_replace_insecure_js
    """

    @responses.activate
    def test_get_replace_insecure_js_all_params(self):
        """
        get_replace_insecure_js()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/replace_insecure_js')
        mock_response = '{"result": {"id": "replace_insecure_js", "value": "off", "editable": true, "modified_on": "2017-01-01T05:20:00.123Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_replace_insecure_js()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_replace_insecure_js_all_params_with_retries(self):
        # Enable retries and run test_get_replace_insecure_js_all_params.
        _service.enable_retries()
        self.test_get_replace_insecure_js_all_params()

        # Disable retries and run test_get_replace_insecure_js_all_params.
        _service.disable_retries()
        self.test_get_replace_insecure_js_all_params()

    @responses.activate
    def test_get_replace_insecure_js_value_error(self):
        """
        test_get_replace_insecure_js_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/replace_insecure_js')
        mock_response = '{"result": {"id": "replace_insecure_js", "value": "off", "editable": true, "modified_on": "2017-01-01T05:20:00.123Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_replace_insecure_js(**req_copy)

    def test_get_replace_insecure_js_value_error_with_retries(self):
        # Enable retries and run test_get_replace_insecure_js_value_error.
        _service.enable_retries()
        self.test_get_replace_insecure_js_value_error()

        # Disable retries and run test_get_replace_insecure_js_value_error.
        _service.disable_retries()
        self.test_get_replace_insecure_js_value_error()


class TestUpdateReplaceInsecureJs:
    """
    Test Class for update_replace_insecure_js
    """

    @responses.activate
    def test_update_replace_insecure_js_all_params(self):
        """
        update_replace_insecure_js()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/replace_insecure_js')
        mock_response = '{"result": {"id": "replace_insecure_js", "value": "off", "editable": true, "modified_on": "2017-01-01T05:20:00.123Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 'off'

        # Invoke method
        response = _service.update_replace_insecure_js(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'off'

    def test_update_replace_insecure_js_all_params_with_retries(self):
        # Enable retries and run test_update_replace_insecure_js_all_params.
        _service.enable_retries()
        self.test_update_replace_insecure_js_all_params()

        # Disable retries and run test_update_replace_insecure_js_all_params.
        _service.disable_retries()
        self.test_update_replace_insecure_js_all_params()

    @responses.activate
    def test_update_replace_insecure_js_required_params(self):
        """
        test_update_replace_insecure_js_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/replace_insecure_js')
        mock_response = '{"result": {"id": "replace_insecure_js", "value": "off", "editable": true, "modified_on": "2017-01-01T05:20:00.123Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_replace_insecure_js()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_replace_insecure_js_required_params_with_retries(self):
        # Enable retries and run test_update_replace_insecure_js_required_params.
        _service.enable_retries()
        self.test_update_replace_insecure_js_required_params()

        # Disable retries and run test_update_replace_insecure_js_required_params.
        _service.disable_retries()
        self.test_update_replace_insecure_js_required_params()

    @responses.activate
    def test_update_replace_insecure_js_value_error(self):
        """
        test_update_replace_insecure_js_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/replace_insecure_js')
        mock_response = '{"result": {"id": "replace_insecure_js", "value": "off", "editable": true, "modified_on": "2017-01-01T05:20:00.123Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_replace_insecure_js(**req_copy)

    def test_update_replace_insecure_js_value_error_with_retries(self):
        # Enable retries and run test_update_replace_insecure_js_value_error.
        _service.enable_retries()
        self.test_update_replace_insecure_js_value_error()

        # Disable retries and run test_update_replace_insecure_js_value_error.
        _service.disable_retries()
        self.test_update_replace_insecure_js_value_error()


class TestGetEmailObfuscation:
    """
    Test Class for get_email_obfuscation
    """

    @responses.activate
    def test_get_email_obfuscation_all_params(self):
        """
        get_email_obfuscation()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/email_obfuscation')
        mock_response = '{"result": {"id": "email_obfuscation", "value": "off", "editable": true, "modified_on": "2017-01-01T05:20:00.123Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.get_email_obfuscation()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_email_obfuscation_all_params_with_retries(self):
        # Enable retries and run test_get_email_obfuscation_all_params.
        _service.enable_retries()
        self.test_get_email_obfuscation_all_params()

        # Disable retries and run test_get_email_obfuscation_all_params.
        _service.disable_retries()
        self.test_get_email_obfuscation_all_params()

    @responses.activate
    def test_get_email_obfuscation_value_error(self):
        """
        test_get_email_obfuscation_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/email_obfuscation')
        mock_response = '{"result": {"id": "email_obfuscation", "value": "off", "editable": true, "modified_on": "2017-01-01T05:20:00.123Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.get_email_obfuscation(**req_copy)

    def test_get_email_obfuscation_value_error_with_retries(self):
        # Enable retries and run test_get_email_obfuscation_value_error.
        _service.enable_retries()
        self.test_get_email_obfuscation_value_error()

        # Disable retries and run test_get_email_obfuscation_value_error.
        _service.disable_retries()
        self.test_get_email_obfuscation_value_error()


class TestUpdateEmailObfuscation:
    """
    Test Class for update_email_obfuscation
    """

    @responses.activate
    def test_update_email_obfuscation_all_params(self):
        """
        update_email_obfuscation()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/email_obfuscation')
        mock_response = '{"result": {"id": "email_obfuscation", "value": "off", "editable": true, "modified_on": "2017-01-01T05:20:00.123Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        value = 'off'

        # Invoke method
        response = _service.update_email_obfuscation(
            value=value,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'off'

    def test_update_email_obfuscation_all_params_with_retries(self):
        # Enable retries and run test_update_email_obfuscation_all_params.
        _service.enable_retries()
        self.test_update_email_obfuscation_all_params()

        # Disable retries and run test_update_email_obfuscation_all_params.
        _service.disable_retries()
        self.test_update_email_obfuscation_all_params()

    @responses.activate
    def test_update_email_obfuscation_required_params(self):
        """
        test_update_email_obfuscation_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/email_obfuscation')
        mock_response = '{"result": {"id": "email_obfuscation", "value": "off", "editable": true, "modified_on": "2017-01-01T05:20:00.123Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.update_email_obfuscation()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_email_obfuscation_required_params_with_retries(self):
        # Enable retries and run test_update_email_obfuscation_required_params.
        _service.enable_retries()
        self.test_update_email_obfuscation_required_params()

        # Disable retries and run test_update_email_obfuscation_required_params.
        _service.disable_retries()
        self.test_update_email_obfuscation_required_params()

    @responses.activate
    def test_update_email_obfuscation_value_error(self):
        """
        test_update_email_obfuscation_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/settings/email_obfuscation')
        mock_response = '{"result": {"id": "email_obfuscation", "value": "off", "editable": true, "modified_on": "2017-01-01T05:20:00.123Z"}, "success": true, "errors": [["errors"]], "messages": [["messages"]]}'
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
                _service.update_email_obfuscation(**req_copy)

    def test_update_email_obfuscation_value_error_with_retries(self):
        # Enable retries and run test_update_email_obfuscation_value_error.
        _service.enable_retries()
        self.test_update_email_obfuscation_value_error()

        # Disable retries and run test_update_email_obfuscation_value_error.
        _service.disable_retries()
        self.test_update_email_obfuscation_value_error()


# endregion
##############################################################################
# End of Service: ZonesSettings
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_AlwaysUseHttpsRespResult:
    """
    Test Class for AlwaysUseHttpsRespResult
    """

    def test_always_use_https_resp_result_serialization(self):
        """
        Test serialization/deserialization for AlwaysUseHttpsRespResult
        """

        # Construct a json representation of a AlwaysUseHttpsRespResult model
        always_use_https_resp_result_model_json = {}
        always_use_https_resp_result_model_json['id'] = 'always_use_https'
        always_use_https_resp_result_model_json['value'] = 'off'
        always_use_https_resp_result_model_json['editable'] = True
        always_use_https_resp_result_model_json['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a model instance of AlwaysUseHttpsRespResult by calling from_dict on the json representation
        always_use_https_resp_result_model = AlwaysUseHttpsRespResult.from_dict(always_use_https_resp_result_model_json)
        assert always_use_https_resp_result_model != False

        # Construct a model instance of AlwaysUseHttpsRespResult by calling from_dict on the json representation
        always_use_https_resp_result_model_dict = AlwaysUseHttpsRespResult.from_dict(always_use_https_resp_result_model_json).__dict__
        always_use_https_resp_result_model2 = AlwaysUseHttpsRespResult(**always_use_https_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert always_use_https_resp_result_model == always_use_https_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        always_use_https_resp_result_model_json2 = always_use_https_resp_result_model.to_dict()
        assert always_use_https_resp_result_model_json2 == always_use_https_resp_result_model_json


class TestModel_AutomaticHttpsRewritesRespResult:
    """
    Test Class for AutomaticHttpsRewritesRespResult
    """

    def test_automatic_https_rewrites_resp_result_serialization(self):
        """
        Test serialization/deserialization for AutomaticHttpsRewritesRespResult
        """

        # Construct a json representation of a AutomaticHttpsRewritesRespResult model
        automatic_https_rewrites_resp_result_model_json = {}
        automatic_https_rewrites_resp_result_model_json['id'] = 'automatic_https_rewrites'
        automatic_https_rewrites_resp_result_model_json['value'] = 'off'
        automatic_https_rewrites_resp_result_model_json['editable'] = True
        automatic_https_rewrites_resp_result_model_json['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a model instance of AutomaticHttpsRewritesRespResult by calling from_dict on the json representation
        automatic_https_rewrites_resp_result_model = AutomaticHttpsRewritesRespResult.from_dict(automatic_https_rewrites_resp_result_model_json)
        assert automatic_https_rewrites_resp_result_model != False

        # Construct a model instance of AutomaticHttpsRewritesRespResult by calling from_dict on the json representation
        automatic_https_rewrites_resp_result_model_dict = AutomaticHttpsRewritesRespResult.from_dict(automatic_https_rewrites_resp_result_model_json).__dict__
        automatic_https_rewrites_resp_result_model2 = AutomaticHttpsRewritesRespResult(**automatic_https_rewrites_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert automatic_https_rewrites_resp_result_model == automatic_https_rewrites_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        automatic_https_rewrites_resp_result_model_json2 = automatic_https_rewrites_resp_result_model.to_dict()
        assert automatic_https_rewrites_resp_result_model_json2 == automatic_https_rewrites_resp_result_model_json


class TestModel_BrotliRespResult:
    """
    Test Class for BrotliRespResult
    """

    def test_brotli_resp_result_serialization(self):
        """
        Test serialization/deserialization for BrotliRespResult
        """

        # Construct a json representation of a BrotliRespResult model
        brotli_resp_result_model_json = {}
        brotli_resp_result_model_json['id'] = 'brotli'
        brotli_resp_result_model_json['value'] = 'off'
        brotli_resp_result_model_json['editable'] = True
        brotli_resp_result_model_json['modified_on'] = '2018-12-08T18:57:52.826000Z'

        # Construct a model instance of BrotliRespResult by calling from_dict on the json representation
        brotli_resp_result_model = BrotliRespResult.from_dict(brotli_resp_result_model_json)
        assert brotli_resp_result_model != False

        # Construct a model instance of BrotliRespResult by calling from_dict on the json representation
        brotli_resp_result_model_dict = BrotliRespResult.from_dict(brotli_resp_result_model_json).__dict__
        brotli_resp_result_model2 = BrotliRespResult(**brotli_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert brotli_resp_result_model == brotli_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        brotli_resp_result_model_json2 = brotli_resp_result_model.to_dict()
        assert brotli_resp_result_model_json2 == brotli_resp_result_model_json


class TestModel_BrowserCheckRespResult:
    """
    Test Class for BrowserCheckRespResult
    """

    def test_browser_check_resp_result_serialization(self):
        """
        Test serialization/deserialization for BrowserCheckRespResult
        """

        # Construct a json representation of a BrowserCheckRespResult model
        browser_check_resp_result_model_json = {}
        browser_check_resp_result_model_json['id'] = 'browser_check'
        browser_check_resp_result_model_json['value'] = 'off'
        browser_check_resp_result_model_json['editable'] = True
        browser_check_resp_result_model_json['modified_on'] = '2018-12-08T18:57:14.506000Z'

        # Construct a model instance of BrowserCheckRespResult by calling from_dict on the json representation
        browser_check_resp_result_model = BrowserCheckRespResult.from_dict(browser_check_resp_result_model_json)
        assert browser_check_resp_result_model != False

        # Construct a model instance of BrowserCheckRespResult by calling from_dict on the json representation
        browser_check_resp_result_model_dict = BrowserCheckRespResult.from_dict(browser_check_resp_result_model_json).__dict__
        browser_check_resp_result_model2 = BrowserCheckRespResult(**browser_check_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert browser_check_resp_result_model == browser_check_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        browser_check_resp_result_model_json2 = browser_check_resp_result_model.to_dict()
        assert browser_check_resp_result_model_json2 == browser_check_resp_result_model_json


class TestModel_ChallengeTtlRespResult:
    """
    Test Class for ChallengeTtlRespResult
    """

    def test_challenge_ttl_resp_result_serialization(self):
        """
        Test serialization/deserialization for ChallengeTtlRespResult
        """

        # Construct a json representation of a ChallengeTtlRespResult model
        challenge_ttl_resp_result_model_json = {}
        challenge_ttl_resp_result_model_json['id'] = 'challenge_ttl'
        challenge_ttl_resp_result_model_json['value'] = 1800
        challenge_ttl_resp_result_model_json['editable'] = True
        challenge_ttl_resp_result_model_json['modified_on'] = '2018-09-17T07:21:39.844000Z'

        # Construct a model instance of ChallengeTtlRespResult by calling from_dict on the json representation
        challenge_ttl_resp_result_model = ChallengeTtlRespResult.from_dict(challenge_ttl_resp_result_model_json)
        assert challenge_ttl_resp_result_model != False

        # Construct a model instance of ChallengeTtlRespResult by calling from_dict on the json representation
        challenge_ttl_resp_result_model_dict = ChallengeTtlRespResult.from_dict(challenge_ttl_resp_result_model_json).__dict__
        challenge_ttl_resp_result_model2 = ChallengeTtlRespResult(**challenge_ttl_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert challenge_ttl_resp_result_model == challenge_ttl_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        challenge_ttl_resp_result_model_json2 = challenge_ttl_resp_result_model.to_dict()
        assert challenge_ttl_resp_result_model_json2 == challenge_ttl_resp_result_model_json


class TestModel_CiphersRespResult:
    """
    Test Class for CiphersRespResult
    """

    def test_ciphers_resp_result_serialization(self):
        """
        Test serialization/deserialization for CiphersRespResult
        """

        # Construct a json representation of a CiphersRespResult model
        ciphers_resp_result_model_json = {}
        ciphers_resp_result_model_json['id'] = 'ciphers'
        ciphers_resp_result_model_json['value'] = ['AES256-GCM-SHA384', 'AES256-SHA256']
        ciphers_resp_result_model_json['editable'] = True
        ciphers_resp_result_model_json['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a model instance of CiphersRespResult by calling from_dict on the json representation
        ciphers_resp_result_model = CiphersRespResult.from_dict(ciphers_resp_result_model_json)
        assert ciphers_resp_result_model != False

        # Construct a model instance of CiphersRespResult by calling from_dict on the json representation
        ciphers_resp_result_model_dict = CiphersRespResult.from_dict(ciphers_resp_result_model_json).__dict__
        ciphers_resp_result_model2 = CiphersRespResult(**ciphers_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert ciphers_resp_result_model == ciphers_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        ciphers_resp_result_model_json2 = ciphers_resp_result_model.to_dict()
        assert ciphers_resp_result_model_json2 == ciphers_resp_result_model_json


class TestModel_EmailObfuscationRespResult:
    """
    Test Class for EmailObfuscationRespResult
    """

    def test_email_obfuscation_resp_result_serialization(self):
        """
        Test serialization/deserialization for EmailObfuscationRespResult
        """

        # Construct a json representation of a EmailObfuscationRespResult model
        email_obfuscation_resp_result_model_json = {}
        email_obfuscation_resp_result_model_json['id'] = 'email_obfuscation'
        email_obfuscation_resp_result_model_json['value'] = 'off'
        email_obfuscation_resp_result_model_json['editable'] = True
        email_obfuscation_resp_result_model_json['modified_on'] = '2017-01-01T05:20:00.123000Z'

        # Construct a model instance of EmailObfuscationRespResult by calling from_dict on the json representation
        email_obfuscation_resp_result_model = EmailObfuscationRespResult.from_dict(email_obfuscation_resp_result_model_json)
        assert email_obfuscation_resp_result_model != False

        # Construct a model instance of EmailObfuscationRespResult by calling from_dict on the json representation
        email_obfuscation_resp_result_model_dict = EmailObfuscationRespResult.from_dict(email_obfuscation_resp_result_model_json).__dict__
        email_obfuscation_resp_result_model2 = EmailObfuscationRespResult(**email_obfuscation_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert email_obfuscation_resp_result_model == email_obfuscation_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        email_obfuscation_resp_result_model_json2 = email_obfuscation_resp_result_model.to_dict()
        assert email_obfuscation_resp_result_model_json2 == email_obfuscation_resp_result_model_json


class TestModel_HotlinkProtectionRespResult:
    """
    Test Class for HotlinkProtectionRespResult
    """

    def test_hotlink_protection_resp_result_serialization(self):
        """
        Test serialization/deserialization for HotlinkProtectionRespResult
        """

        # Construct a json representation of a HotlinkProtectionRespResult model
        hotlink_protection_resp_result_model_json = {}
        hotlink_protection_resp_result_model_json['id'] = 'hotlink_protection'
        hotlink_protection_resp_result_model_json['value'] = 'off'
        hotlink_protection_resp_result_model_json['editable'] = True
        hotlink_protection_resp_result_model_json['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a model instance of HotlinkProtectionRespResult by calling from_dict on the json representation
        hotlink_protection_resp_result_model = HotlinkProtectionRespResult.from_dict(hotlink_protection_resp_result_model_json)
        assert hotlink_protection_resp_result_model != False

        # Construct a model instance of HotlinkProtectionRespResult by calling from_dict on the json representation
        hotlink_protection_resp_result_model_dict = HotlinkProtectionRespResult.from_dict(hotlink_protection_resp_result_model_json).__dict__
        hotlink_protection_resp_result_model2 = HotlinkProtectionRespResult(**hotlink_protection_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert hotlink_protection_resp_result_model == hotlink_protection_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        hotlink_protection_resp_result_model_json2 = hotlink_protection_resp_result_model.to_dict()
        assert hotlink_protection_resp_result_model_json2 == hotlink_protection_resp_result_model_json


class TestModel_Http2RespResult:
    """
    Test Class for Http2RespResult
    """

    def test_http2_resp_result_serialization(self):
        """
        Test serialization/deserialization for Http2RespResult
        """

        # Construct a json representation of a Http2RespResult model
        http2_resp_result_model_json = {}
        http2_resp_result_model_json['id'] = 'http2'
        http2_resp_result_model_json['value'] = 'off'
        http2_resp_result_model_json['editable'] = True
        http2_resp_result_model_json['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a model instance of Http2RespResult by calling from_dict on the json representation
        http2_resp_result_model = Http2RespResult.from_dict(http2_resp_result_model_json)
        assert http2_resp_result_model != False

        # Construct a model instance of Http2RespResult by calling from_dict on the json representation
        http2_resp_result_model_dict = Http2RespResult.from_dict(http2_resp_result_model_json).__dict__
        http2_resp_result_model2 = Http2RespResult(**http2_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert http2_resp_result_model == http2_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        http2_resp_result_model_json2 = http2_resp_result_model.to_dict()
        assert http2_resp_result_model_json2 == http2_resp_result_model_json


class TestModel_Http3RespResult:
    """
    Test Class for Http3RespResult
    """

    def test_http3_resp_result_serialization(self):
        """
        Test serialization/deserialization for Http3RespResult
        """

        # Construct a json representation of a Http3RespResult model
        http3_resp_result_model_json = {}
        http3_resp_result_model_json['id'] = 'http3'
        http3_resp_result_model_json['value'] = 'off'
        http3_resp_result_model_json['editable'] = True
        http3_resp_result_model_json['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a model instance of Http3RespResult by calling from_dict on the json representation
        http3_resp_result_model = Http3RespResult.from_dict(http3_resp_result_model_json)
        assert http3_resp_result_model != False

        # Construct a model instance of Http3RespResult by calling from_dict on the json representation
        http3_resp_result_model_dict = Http3RespResult.from_dict(http3_resp_result_model_json).__dict__
        http3_resp_result_model2 = Http3RespResult(**http3_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert http3_resp_result_model == http3_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        http3_resp_result_model_json2 = http3_resp_result_model.to_dict()
        assert http3_resp_result_model_json2 == http3_resp_result_model_json


class TestModel_ImageLoadOptimizationRespResult:
    """
    Test Class for ImageLoadOptimizationRespResult
    """

    def test_image_load_optimization_resp_result_serialization(self):
        """
        Test serialization/deserialization for ImageLoadOptimizationRespResult
        """

        # Construct a json representation of a ImageLoadOptimizationRespResult model
        image_load_optimization_resp_result_model_json = {}
        image_load_optimization_resp_result_model_json['id'] = 'image_load_optimization'
        image_load_optimization_resp_result_model_json['value'] = 'off'
        image_load_optimization_resp_result_model_json['editable'] = True
        image_load_optimization_resp_result_model_json['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a model instance of ImageLoadOptimizationRespResult by calling from_dict on the json representation
        image_load_optimization_resp_result_model = ImageLoadOptimizationRespResult.from_dict(image_load_optimization_resp_result_model_json)
        assert image_load_optimization_resp_result_model != False

        # Construct a model instance of ImageLoadOptimizationRespResult by calling from_dict on the json representation
        image_load_optimization_resp_result_model_dict = ImageLoadOptimizationRespResult.from_dict(image_load_optimization_resp_result_model_json).__dict__
        image_load_optimization_resp_result_model2 = ImageLoadOptimizationRespResult(**image_load_optimization_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert image_load_optimization_resp_result_model == image_load_optimization_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        image_load_optimization_resp_result_model_json2 = image_load_optimization_resp_result_model.to_dict()
        assert image_load_optimization_resp_result_model_json2 == image_load_optimization_resp_result_model_json


class TestModel_ImageSizeOptimizationRespResult:
    """
    Test Class for ImageSizeOptimizationRespResult
    """

    def test_image_size_optimization_resp_result_serialization(self):
        """
        Test serialization/deserialization for ImageSizeOptimizationRespResult
        """

        # Construct a json representation of a ImageSizeOptimizationRespResult model
        image_size_optimization_resp_result_model_json = {}
        image_size_optimization_resp_result_model_json['id'] = 'image_size_optimization'
        image_size_optimization_resp_result_model_json['value'] = 'lossless'
        image_size_optimization_resp_result_model_json['editable'] = True
        image_size_optimization_resp_result_model_json['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a model instance of ImageSizeOptimizationRespResult by calling from_dict on the json representation
        image_size_optimization_resp_result_model = ImageSizeOptimizationRespResult.from_dict(image_size_optimization_resp_result_model_json)
        assert image_size_optimization_resp_result_model != False

        # Construct a model instance of ImageSizeOptimizationRespResult by calling from_dict on the json representation
        image_size_optimization_resp_result_model_dict = ImageSizeOptimizationRespResult.from_dict(image_size_optimization_resp_result_model_json).__dict__
        image_size_optimization_resp_result_model2 = ImageSizeOptimizationRespResult(**image_size_optimization_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert image_size_optimization_resp_result_model == image_size_optimization_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        image_size_optimization_resp_result_model_json2 = image_size_optimization_resp_result_model.to_dict()
        assert image_size_optimization_resp_result_model_json2 == image_size_optimization_resp_result_model_json


class TestModel_IpGeolocationRespResult:
    """
    Test Class for IpGeolocationRespResult
    """

    def test_ip_geolocation_resp_result_serialization(self):
        """
        Test serialization/deserialization for IpGeolocationRespResult
        """

        # Construct a json representation of a IpGeolocationRespResult model
        ip_geolocation_resp_result_model_json = {}
        ip_geolocation_resp_result_model_json['id'] = 'ip_geolocation'
        ip_geolocation_resp_result_model_json['value'] = 'off'
        ip_geolocation_resp_result_model_json['editable'] = True
        ip_geolocation_resp_result_model_json['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a model instance of IpGeolocationRespResult by calling from_dict on the json representation
        ip_geolocation_resp_result_model = IpGeolocationRespResult.from_dict(ip_geolocation_resp_result_model_json)
        assert ip_geolocation_resp_result_model != False

        # Construct a model instance of IpGeolocationRespResult by calling from_dict on the json representation
        ip_geolocation_resp_result_model_dict = IpGeolocationRespResult.from_dict(ip_geolocation_resp_result_model_json).__dict__
        ip_geolocation_resp_result_model2 = IpGeolocationRespResult(**ip_geolocation_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert ip_geolocation_resp_result_model == ip_geolocation_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        ip_geolocation_resp_result_model_json2 = ip_geolocation_resp_result_model.to_dict()
        assert ip_geolocation_resp_result_model_json2 == ip_geolocation_resp_result_model_json


class TestModel_Ipv6RespResult:
    """
    Test Class for Ipv6RespResult
    """

    def test_ipv6_resp_result_serialization(self):
        """
        Test serialization/deserialization for Ipv6RespResult
        """

        # Construct a json representation of a Ipv6RespResult model
        ipv6_resp_result_model_json = {}
        ipv6_resp_result_model_json['id'] = 'ipv6'
        ipv6_resp_result_model_json['value'] = 'off'
        ipv6_resp_result_model_json['editable'] = True
        ipv6_resp_result_model_json['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a model instance of Ipv6RespResult by calling from_dict on the json representation
        ipv6_resp_result_model = Ipv6RespResult.from_dict(ipv6_resp_result_model_json)
        assert ipv6_resp_result_model != False

        # Construct a model instance of Ipv6RespResult by calling from_dict on the json representation
        ipv6_resp_result_model_dict = Ipv6RespResult.from_dict(ipv6_resp_result_model_json).__dict__
        ipv6_resp_result_model2 = Ipv6RespResult(**ipv6_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert ipv6_resp_result_model == ipv6_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        ipv6_resp_result_model_json2 = ipv6_resp_result_model.to_dict()
        assert ipv6_resp_result_model_json2 == ipv6_resp_result_model_json


class TestModel_LogRetentionRespResult:
    """
    Test Class for LogRetentionRespResult
    """

    def test_log_retention_resp_result_serialization(self):
        """
        Test serialization/deserialization for LogRetentionRespResult
        """

        # Construct a json representation of a LogRetentionRespResult model
        log_retention_resp_result_model_json = {}
        log_retention_resp_result_model_json['flag'] = True

        # Construct a model instance of LogRetentionRespResult by calling from_dict on the json representation
        log_retention_resp_result_model = LogRetentionRespResult.from_dict(log_retention_resp_result_model_json)
        assert log_retention_resp_result_model != False

        # Construct a model instance of LogRetentionRespResult by calling from_dict on the json representation
        log_retention_resp_result_model_dict = LogRetentionRespResult.from_dict(log_retention_resp_result_model_json).__dict__
        log_retention_resp_result_model2 = LogRetentionRespResult(**log_retention_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert log_retention_resp_result_model == log_retention_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        log_retention_resp_result_model_json2 = log_retention_resp_result_model.to_dict()
        assert log_retention_resp_result_model_json2 == log_retention_resp_result_model_json


class TestModel_MaxUploadRespResult:
    """
    Test Class for MaxUploadRespResult
    """

    def test_max_upload_resp_result_serialization(self):
        """
        Test serialization/deserialization for MaxUploadRespResult
        """

        # Construct a json representation of a MaxUploadRespResult model
        max_upload_resp_result_model_json = {}
        max_upload_resp_result_model_json['id'] = 'max_upload'
        max_upload_resp_result_model_json['value'] = 300
        max_upload_resp_result_model_json['editable'] = True
        max_upload_resp_result_model_json['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a model instance of MaxUploadRespResult by calling from_dict on the json representation
        max_upload_resp_result_model = MaxUploadRespResult.from_dict(max_upload_resp_result_model_json)
        assert max_upload_resp_result_model != False

        # Construct a model instance of MaxUploadRespResult by calling from_dict on the json representation
        max_upload_resp_result_model_dict = MaxUploadRespResult.from_dict(max_upload_resp_result_model_json).__dict__
        max_upload_resp_result_model2 = MaxUploadRespResult(**max_upload_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert max_upload_resp_result_model == max_upload_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        max_upload_resp_result_model_json2 = max_upload_resp_result_model.to_dict()
        assert max_upload_resp_result_model_json2 == max_upload_resp_result_model_json


class TestModel_MinTlsVersionRespResult:
    """
    Test Class for MinTlsVersionRespResult
    """

    def test_min_tls_version_resp_result_serialization(self):
        """
        Test serialization/deserialization for MinTlsVersionRespResult
        """

        # Construct a json representation of a MinTlsVersionRespResult model
        min_tls_version_resp_result_model_json = {}
        min_tls_version_resp_result_model_json['id'] = 'min_tls_version'
        min_tls_version_resp_result_model_json['value'] = '1.2'
        min_tls_version_resp_result_model_json['editable'] = True
        min_tls_version_resp_result_model_json['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a model instance of MinTlsVersionRespResult by calling from_dict on the json representation
        min_tls_version_resp_result_model = MinTlsVersionRespResult.from_dict(min_tls_version_resp_result_model_json)
        assert min_tls_version_resp_result_model != False

        # Construct a model instance of MinTlsVersionRespResult by calling from_dict on the json representation
        min_tls_version_resp_result_model_dict = MinTlsVersionRespResult.from_dict(min_tls_version_resp_result_model_json).__dict__
        min_tls_version_resp_result_model2 = MinTlsVersionRespResult(**min_tls_version_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert min_tls_version_resp_result_model == min_tls_version_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        min_tls_version_resp_result_model_json2 = min_tls_version_resp_result_model.to_dict()
        assert min_tls_version_resp_result_model_json2 == min_tls_version_resp_result_model_json


class TestModel_MinifyRespResult:
    """
    Test Class for MinifyRespResult
    """

    def test_minify_resp_result_serialization(self):
        """
        Test serialization/deserialization for MinifyRespResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        minify_resp_result_value_model = {}  # MinifyRespResultValue
        minify_resp_result_value_model['css'] = 'on'
        minify_resp_result_value_model['html'] = 'on'
        minify_resp_result_value_model['js'] = 'on'

        # Construct a json representation of a MinifyRespResult model
        minify_resp_result_model_json = {}
        minify_resp_result_model_json['id'] = 'minify'
        minify_resp_result_model_json['value'] = minify_resp_result_value_model
        minify_resp_result_model_json['editable'] = True
        minify_resp_result_model_json['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a model instance of MinifyRespResult by calling from_dict on the json representation
        minify_resp_result_model = MinifyRespResult.from_dict(minify_resp_result_model_json)
        assert minify_resp_result_model != False

        # Construct a model instance of MinifyRespResult by calling from_dict on the json representation
        minify_resp_result_model_dict = MinifyRespResult.from_dict(minify_resp_result_model_json).__dict__
        minify_resp_result_model2 = MinifyRespResult(**minify_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert minify_resp_result_model == minify_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        minify_resp_result_model_json2 = minify_resp_result_model.to_dict()
        assert minify_resp_result_model_json2 == minify_resp_result_model_json


class TestModel_MinifyRespResultValue:
    """
    Test Class for MinifyRespResultValue
    """

    def test_minify_resp_result_value_serialization(self):
        """
        Test serialization/deserialization for MinifyRespResultValue
        """

        # Construct a json representation of a MinifyRespResultValue model
        minify_resp_result_value_model_json = {}
        minify_resp_result_value_model_json['css'] = 'on'
        minify_resp_result_value_model_json['html'] = 'on'
        minify_resp_result_value_model_json['js'] = 'on'

        # Construct a model instance of MinifyRespResultValue by calling from_dict on the json representation
        minify_resp_result_value_model = MinifyRespResultValue.from_dict(minify_resp_result_value_model_json)
        assert minify_resp_result_value_model != False

        # Construct a model instance of MinifyRespResultValue by calling from_dict on the json representation
        minify_resp_result_value_model_dict = MinifyRespResultValue.from_dict(minify_resp_result_value_model_json).__dict__
        minify_resp_result_value_model2 = MinifyRespResultValue(**minify_resp_result_value_model_dict)

        # Verify the model instances are equivalent
        assert minify_resp_result_value_model == minify_resp_result_value_model2

        # Convert model instance back to dict and verify no loss of data
        minify_resp_result_value_model_json2 = minify_resp_result_value_model.to_dict()
        assert minify_resp_result_value_model_json2 == minify_resp_result_value_model_json


class TestModel_MinifySettingValue:
    """
    Test Class for MinifySettingValue
    """

    def test_minify_setting_value_serialization(self):
        """
        Test serialization/deserialization for MinifySettingValue
        """

        # Construct a json representation of a MinifySettingValue model
        minify_setting_value_model_json = {}
        minify_setting_value_model_json['css'] = 'off'
        minify_setting_value_model_json['html'] = 'off'
        minify_setting_value_model_json['js'] = 'off'

        # Construct a model instance of MinifySettingValue by calling from_dict on the json representation
        minify_setting_value_model = MinifySettingValue.from_dict(minify_setting_value_model_json)
        assert minify_setting_value_model != False

        # Construct a model instance of MinifySettingValue by calling from_dict on the json representation
        minify_setting_value_model_dict = MinifySettingValue.from_dict(minify_setting_value_model_json).__dict__
        minify_setting_value_model2 = MinifySettingValue(**minify_setting_value_model_dict)

        # Verify the model instances are equivalent
        assert minify_setting_value_model == minify_setting_value_model2

        # Convert model instance back to dict and verify no loss of data
        minify_setting_value_model_json2 = minify_setting_value_model.to_dict()
        assert minify_setting_value_model_json2 == minify_setting_value_model_json


class TestModel_MobileRedirecSettingValue:
    """
    Test Class for MobileRedirecSettingValue
    """

    def test_mobile_redirec_setting_value_serialization(self):
        """
        Test serialization/deserialization for MobileRedirecSettingValue
        """

        # Construct a json representation of a MobileRedirecSettingValue model
        mobile_redirec_setting_value_model_json = {}
        mobile_redirec_setting_value_model_json['status'] = 'on'
        mobile_redirec_setting_value_model_json['mobile_subdomain'] = 'm'
        mobile_redirec_setting_value_model_json['strip_uri'] = False

        # Construct a model instance of MobileRedirecSettingValue by calling from_dict on the json representation
        mobile_redirec_setting_value_model = MobileRedirecSettingValue.from_dict(mobile_redirec_setting_value_model_json)
        assert mobile_redirec_setting_value_model != False

        # Construct a model instance of MobileRedirecSettingValue by calling from_dict on the json representation
        mobile_redirec_setting_value_model_dict = MobileRedirecSettingValue.from_dict(mobile_redirec_setting_value_model_json).__dict__
        mobile_redirec_setting_value_model2 = MobileRedirecSettingValue(**mobile_redirec_setting_value_model_dict)

        # Verify the model instances are equivalent
        assert mobile_redirec_setting_value_model == mobile_redirec_setting_value_model2

        # Convert model instance back to dict and verify no loss of data
        mobile_redirec_setting_value_model_json2 = mobile_redirec_setting_value_model.to_dict()
        assert mobile_redirec_setting_value_model_json2 == mobile_redirec_setting_value_model_json


class TestModel_MobileRedirectRespResult:
    """
    Test Class for MobileRedirectRespResult
    """

    def test_mobile_redirect_resp_result_serialization(self):
        """
        Test serialization/deserialization for MobileRedirectRespResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        mobile_redirect_resp_result_value_model = {}  # MobileRedirectRespResultValue
        mobile_redirect_resp_result_value_model['status'] = 'on'
        mobile_redirect_resp_result_value_model['mobile_subdomain'] = 'm'
        mobile_redirect_resp_result_value_model['strip_uri'] = False

        # Construct a json representation of a MobileRedirectRespResult model
        mobile_redirect_resp_result_model_json = {}
        mobile_redirect_resp_result_model_json['id'] = 'mobile_redirect'
        mobile_redirect_resp_result_model_json['value'] = mobile_redirect_resp_result_value_model
        mobile_redirect_resp_result_model_json['editable'] = True
        mobile_redirect_resp_result_model_json['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a model instance of MobileRedirectRespResult by calling from_dict on the json representation
        mobile_redirect_resp_result_model = MobileRedirectRespResult.from_dict(mobile_redirect_resp_result_model_json)
        assert mobile_redirect_resp_result_model != False

        # Construct a model instance of MobileRedirectRespResult by calling from_dict on the json representation
        mobile_redirect_resp_result_model_dict = MobileRedirectRespResult.from_dict(mobile_redirect_resp_result_model_json).__dict__
        mobile_redirect_resp_result_model2 = MobileRedirectRespResult(**mobile_redirect_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert mobile_redirect_resp_result_model == mobile_redirect_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        mobile_redirect_resp_result_model_json2 = mobile_redirect_resp_result_model.to_dict()
        assert mobile_redirect_resp_result_model_json2 == mobile_redirect_resp_result_model_json


class TestModel_MobileRedirectRespResultValue:
    """
    Test Class for MobileRedirectRespResultValue
    """

    def test_mobile_redirect_resp_result_value_serialization(self):
        """
        Test serialization/deserialization for MobileRedirectRespResultValue
        """

        # Construct a json representation of a MobileRedirectRespResultValue model
        mobile_redirect_resp_result_value_model_json = {}
        mobile_redirect_resp_result_value_model_json['status'] = 'on'
        mobile_redirect_resp_result_value_model_json['mobile_subdomain'] = 'm'
        mobile_redirect_resp_result_value_model_json['strip_uri'] = False

        # Construct a model instance of MobileRedirectRespResultValue by calling from_dict on the json representation
        mobile_redirect_resp_result_value_model = MobileRedirectRespResultValue.from_dict(mobile_redirect_resp_result_value_model_json)
        assert mobile_redirect_resp_result_value_model != False

        # Construct a model instance of MobileRedirectRespResultValue by calling from_dict on the json representation
        mobile_redirect_resp_result_value_model_dict = MobileRedirectRespResultValue.from_dict(mobile_redirect_resp_result_value_model_json).__dict__
        mobile_redirect_resp_result_value_model2 = MobileRedirectRespResultValue(**mobile_redirect_resp_result_value_model_dict)

        # Verify the model instances are equivalent
        assert mobile_redirect_resp_result_value_model == mobile_redirect_resp_result_value_model2

        # Convert model instance back to dict and verify no loss of data
        mobile_redirect_resp_result_value_model_json2 = mobile_redirect_resp_result_value_model.to_dict()
        assert mobile_redirect_resp_result_value_model_json2 == mobile_redirect_resp_result_value_model_json


class TestModel_OpportunisticEncryptionRespResult:
    """
    Test Class for OpportunisticEncryptionRespResult
    """

    def test_opportunistic_encryption_resp_result_serialization(self):
        """
        Test serialization/deserialization for OpportunisticEncryptionRespResult
        """

        # Construct a json representation of a OpportunisticEncryptionRespResult model
        opportunistic_encryption_resp_result_model_json = {}
        opportunistic_encryption_resp_result_model_json['id'] = 'opportunistic_encryption'
        opportunistic_encryption_resp_result_model_json['value'] = 'off'
        opportunistic_encryption_resp_result_model_json['editable'] = True
        opportunistic_encryption_resp_result_model_json['modified_on'] = '2017-01-01T05:20:00.123000Z'

        # Construct a model instance of OpportunisticEncryptionRespResult by calling from_dict on the json representation
        opportunistic_encryption_resp_result_model = OpportunisticEncryptionRespResult.from_dict(opportunistic_encryption_resp_result_model_json)
        assert opportunistic_encryption_resp_result_model != False

        # Construct a model instance of OpportunisticEncryptionRespResult by calling from_dict on the json representation
        opportunistic_encryption_resp_result_model_dict = OpportunisticEncryptionRespResult.from_dict(opportunistic_encryption_resp_result_model_json).__dict__
        opportunistic_encryption_resp_result_model2 = OpportunisticEncryptionRespResult(**opportunistic_encryption_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert opportunistic_encryption_resp_result_model == opportunistic_encryption_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        opportunistic_encryption_resp_result_model_json2 = opportunistic_encryption_resp_result_model.to_dict()
        assert opportunistic_encryption_resp_result_model_json2 == opportunistic_encryption_resp_result_model_json


class TestModel_OpportunisticOnionRespResult:
    """
    Test Class for OpportunisticOnionRespResult
    """

    def test_opportunistic_onion_resp_result_serialization(self):
        """
        Test serialization/deserialization for OpportunisticOnionRespResult
        """

        # Construct a json representation of a OpportunisticOnionRespResult model
        opportunistic_onion_resp_result_model_json = {}
        opportunistic_onion_resp_result_model_json['id'] = 'opportunistic_onion'
        opportunistic_onion_resp_result_model_json['value'] = 'off'
        opportunistic_onion_resp_result_model_json['editable'] = True
        opportunistic_onion_resp_result_model_json['modified_on'] = '2017-01-01T05:20:00.123000Z'

        # Construct a model instance of OpportunisticOnionRespResult by calling from_dict on the json representation
        opportunistic_onion_resp_result_model = OpportunisticOnionRespResult.from_dict(opportunistic_onion_resp_result_model_json)
        assert opportunistic_onion_resp_result_model != False

        # Construct a model instance of OpportunisticOnionRespResult by calling from_dict on the json representation
        opportunistic_onion_resp_result_model_dict = OpportunisticOnionRespResult.from_dict(opportunistic_onion_resp_result_model_json).__dict__
        opportunistic_onion_resp_result_model2 = OpportunisticOnionRespResult(**opportunistic_onion_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert opportunistic_onion_resp_result_model == opportunistic_onion_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        opportunistic_onion_resp_result_model_json2 = opportunistic_onion_resp_result_model.to_dict()
        assert opportunistic_onion_resp_result_model_json2 == opportunistic_onion_resp_result_model_json


class TestModel_OriginErrorPagePassThruRespResult:
    """
    Test Class for OriginErrorPagePassThruRespResult
    """

    def test_origin_error_page_pass_thru_resp_result_serialization(self):
        """
        Test serialization/deserialization for OriginErrorPagePassThruRespResult
        """

        # Construct a json representation of a OriginErrorPagePassThruRespResult model
        origin_error_page_pass_thru_resp_result_model_json = {}
        origin_error_page_pass_thru_resp_result_model_json['id'] = 'origin_error_page_pass_thru'
        origin_error_page_pass_thru_resp_result_model_json['value'] = 'off'
        origin_error_page_pass_thru_resp_result_model_json['editable'] = True
        origin_error_page_pass_thru_resp_result_model_json['modified_on'] = '2018-12-08T18:57:52.826000Z'

        # Construct a model instance of OriginErrorPagePassThruRespResult by calling from_dict on the json representation
        origin_error_page_pass_thru_resp_result_model = OriginErrorPagePassThruRespResult.from_dict(origin_error_page_pass_thru_resp_result_model_json)
        assert origin_error_page_pass_thru_resp_result_model != False

        # Construct a model instance of OriginErrorPagePassThruRespResult by calling from_dict on the json representation
        origin_error_page_pass_thru_resp_result_model_dict = OriginErrorPagePassThruRespResult.from_dict(origin_error_page_pass_thru_resp_result_model_json).__dict__
        origin_error_page_pass_thru_resp_result_model2 = OriginErrorPagePassThruRespResult(**origin_error_page_pass_thru_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert origin_error_page_pass_thru_resp_result_model == origin_error_page_pass_thru_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        origin_error_page_pass_thru_resp_result_model_json2 = origin_error_page_pass_thru_resp_result_model.to_dict()
        assert origin_error_page_pass_thru_resp_result_model_json2 == origin_error_page_pass_thru_resp_result_model_json


class TestModel_OriginMaxHttpVersionRespResult:
    """
    Test Class for OriginMaxHttpVersionRespResult
    """

    def test_origin_max_http_version_resp_result_serialization(self):
        """
        Test serialization/deserialization for OriginMaxHttpVersionRespResult
        """

        # Construct a json representation of a OriginMaxHttpVersionRespResult model
        origin_max_http_version_resp_result_model_json = {}
        origin_max_http_version_resp_result_model_json['id'] = 'origin_max_http_version'
        origin_max_http_version_resp_result_model_json['value'] = '1'
        origin_max_http_version_resp_result_model_json['editable'] = True
        origin_max_http_version_resp_result_model_json['modified_on'] = '2023-09-14T09:49:19.524000Z'

        # Construct a model instance of OriginMaxHttpVersionRespResult by calling from_dict on the json representation
        origin_max_http_version_resp_result_model = OriginMaxHttpVersionRespResult.from_dict(origin_max_http_version_resp_result_model_json)
        assert origin_max_http_version_resp_result_model != False

        # Construct a model instance of OriginMaxHttpVersionRespResult by calling from_dict on the json representation
        origin_max_http_version_resp_result_model_dict = OriginMaxHttpVersionRespResult.from_dict(origin_max_http_version_resp_result_model_json).__dict__
        origin_max_http_version_resp_result_model2 = OriginMaxHttpVersionRespResult(**origin_max_http_version_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert origin_max_http_version_resp_result_model == origin_max_http_version_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        origin_max_http_version_resp_result_model_json2 = origin_max_http_version_resp_result_model.to_dict()
        assert origin_max_http_version_resp_result_model_json2 == origin_max_http_version_resp_result_model_json


class TestModel_OriginPostQuantumEncryptionRespResult:
    """
    Test Class for OriginPostQuantumEncryptionRespResult
    """

    def test_origin_post_quantum_encryption_resp_result_serialization(self):
        """
        Test serialization/deserialization for OriginPostQuantumEncryptionRespResult
        """

        # Construct a json representation of a OriginPostQuantumEncryptionRespResult model
        origin_post_quantum_encryption_resp_result_model_json = {}
        origin_post_quantum_encryption_resp_result_model_json['id'] = 'origin_pqe'
        origin_post_quantum_encryption_resp_result_model_json['value'] = 'off'
        origin_post_quantum_encryption_resp_result_model_json['editable'] = True
        origin_post_quantum_encryption_resp_result_model_json['modified_on'] = '2023-09-14T09:49:19.524000Z'

        # Construct a model instance of OriginPostQuantumEncryptionRespResult by calling from_dict on the json representation
        origin_post_quantum_encryption_resp_result_model = OriginPostQuantumEncryptionRespResult.from_dict(origin_post_quantum_encryption_resp_result_model_json)
        assert origin_post_quantum_encryption_resp_result_model != False

        # Construct a model instance of OriginPostQuantumEncryptionRespResult by calling from_dict on the json representation
        origin_post_quantum_encryption_resp_result_model_dict = OriginPostQuantumEncryptionRespResult.from_dict(origin_post_quantum_encryption_resp_result_model_json).__dict__
        origin_post_quantum_encryption_resp_result_model2 = OriginPostQuantumEncryptionRespResult(**origin_post_quantum_encryption_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert origin_post_quantum_encryption_resp_result_model == origin_post_quantum_encryption_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        origin_post_quantum_encryption_resp_result_model_json2 = origin_post_quantum_encryption_resp_result_model.to_dict()
        assert origin_post_quantum_encryption_resp_result_model_json2 == origin_post_quantum_encryption_resp_result_model_json


class TestModel_PrefetchPreloadRespResult:
    """
    Test Class for PrefetchPreloadRespResult
    """

    def test_prefetch_preload_resp_result_serialization(self):
        """
        Test serialization/deserialization for PrefetchPreloadRespResult
        """

        # Construct a json representation of a PrefetchPreloadRespResult model
        prefetch_preload_resp_result_model_json = {}
        prefetch_preload_resp_result_model_json['id'] = 'prefetch_preload'
        prefetch_preload_resp_result_model_json['value'] = 'off'
        prefetch_preload_resp_result_model_json['editable'] = True
        prefetch_preload_resp_result_model_json['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a model instance of PrefetchPreloadRespResult by calling from_dict on the json representation
        prefetch_preload_resp_result_model = PrefetchPreloadRespResult.from_dict(prefetch_preload_resp_result_model_json)
        assert prefetch_preload_resp_result_model != False

        # Construct a model instance of PrefetchPreloadRespResult by calling from_dict on the json representation
        prefetch_preload_resp_result_model_dict = PrefetchPreloadRespResult.from_dict(prefetch_preload_resp_result_model_json).__dict__
        prefetch_preload_resp_result_model2 = PrefetchPreloadRespResult(**prefetch_preload_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert prefetch_preload_resp_result_model == prefetch_preload_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        prefetch_preload_resp_result_model_json2 = prefetch_preload_resp_result_model.to_dict()
        assert prefetch_preload_resp_result_model_json2 == prefetch_preload_resp_result_model_json


class TestModel_ProxyReadTimeoutRespResult:
    """
    Test Class for ProxyReadTimeoutRespResult
    """

    def test_proxy_read_timeout_resp_result_serialization(self):
        """
        Test serialization/deserialization for ProxyReadTimeoutRespResult
        """

        # Construct a json representation of a ProxyReadTimeoutRespResult model
        proxy_read_timeout_resp_result_model_json = {}
        proxy_read_timeout_resp_result_model_json['id'] = 'proxy_read_timeout'
        proxy_read_timeout_resp_result_model_json['value'] = 100
        proxy_read_timeout_resp_result_model_json['editable'] = True
        proxy_read_timeout_resp_result_model_json['modified_on'] = '2018-12-08T18:57:52.826000Z'

        # Construct a model instance of ProxyReadTimeoutRespResult by calling from_dict on the json representation
        proxy_read_timeout_resp_result_model = ProxyReadTimeoutRespResult.from_dict(proxy_read_timeout_resp_result_model_json)
        assert proxy_read_timeout_resp_result_model != False

        # Construct a model instance of ProxyReadTimeoutRespResult by calling from_dict on the json representation
        proxy_read_timeout_resp_result_model_dict = ProxyReadTimeoutRespResult.from_dict(proxy_read_timeout_resp_result_model_json).__dict__
        proxy_read_timeout_resp_result_model2 = ProxyReadTimeoutRespResult(**proxy_read_timeout_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert proxy_read_timeout_resp_result_model == proxy_read_timeout_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        proxy_read_timeout_resp_result_model_json2 = proxy_read_timeout_resp_result_model.to_dict()
        assert proxy_read_timeout_resp_result_model_json2 == proxy_read_timeout_resp_result_model_json


class TestModel_PseudoIpv4RespResult:
    """
    Test Class for PseudoIpv4RespResult
    """

    def test_pseudo_ipv4_resp_result_serialization(self):
        """
        Test serialization/deserialization for PseudoIpv4RespResult
        """

        # Construct a json representation of a PseudoIpv4RespResult model
        pseudo_ipv4_resp_result_model_json = {}
        pseudo_ipv4_resp_result_model_json['id'] = 'pseudo_ipv4'
        pseudo_ipv4_resp_result_model_json['value'] = 'add_header'
        pseudo_ipv4_resp_result_model_json['editable'] = True
        pseudo_ipv4_resp_result_model_json['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a model instance of PseudoIpv4RespResult by calling from_dict on the json representation
        pseudo_ipv4_resp_result_model = PseudoIpv4RespResult.from_dict(pseudo_ipv4_resp_result_model_json)
        assert pseudo_ipv4_resp_result_model != False

        # Construct a model instance of PseudoIpv4RespResult by calling from_dict on the json representation
        pseudo_ipv4_resp_result_model_dict = PseudoIpv4RespResult.from_dict(pseudo_ipv4_resp_result_model_json).__dict__
        pseudo_ipv4_resp_result_model2 = PseudoIpv4RespResult(**pseudo_ipv4_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert pseudo_ipv4_resp_result_model == pseudo_ipv4_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        pseudo_ipv4_resp_result_model_json2 = pseudo_ipv4_resp_result_model.to_dict()
        assert pseudo_ipv4_resp_result_model_json2 == pseudo_ipv4_resp_result_model_json


class TestModel_ReplaceInsecureJsRespResult:
    """
    Test Class for ReplaceInsecureJsRespResult
    """

    def test_replace_insecure_js_resp_result_serialization(self):
        """
        Test serialization/deserialization for ReplaceInsecureJsRespResult
        """

        # Construct a json representation of a ReplaceInsecureJsRespResult model
        replace_insecure_js_resp_result_model_json = {}
        replace_insecure_js_resp_result_model_json['id'] = 'replace_insecure_js'
        replace_insecure_js_resp_result_model_json['value'] = 'off'
        replace_insecure_js_resp_result_model_json['editable'] = True
        replace_insecure_js_resp_result_model_json['modified_on'] = '2017-01-01T05:20:00.123000Z'

        # Construct a model instance of ReplaceInsecureJsRespResult by calling from_dict on the json representation
        replace_insecure_js_resp_result_model = ReplaceInsecureJsRespResult.from_dict(replace_insecure_js_resp_result_model_json)
        assert replace_insecure_js_resp_result_model != False

        # Construct a model instance of ReplaceInsecureJsRespResult by calling from_dict on the json representation
        replace_insecure_js_resp_result_model_dict = ReplaceInsecureJsRespResult.from_dict(replace_insecure_js_resp_result_model_json).__dict__
        replace_insecure_js_resp_result_model2 = ReplaceInsecureJsRespResult(**replace_insecure_js_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert replace_insecure_js_resp_result_model == replace_insecure_js_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        replace_insecure_js_resp_result_model_json2 = replace_insecure_js_resp_result_model.to_dict()
        assert replace_insecure_js_resp_result_model_json2 == replace_insecure_js_resp_result_model_json


class TestModel_ResponseBufferingRespResult:
    """
    Test Class for ResponseBufferingRespResult
    """

    def test_response_buffering_resp_result_serialization(self):
        """
        Test serialization/deserialization for ResponseBufferingRespResult
        """

        # Construct a json representation of a ResponseBufferingRespResult model
        response_buffering_resp_result_model_json = {}
        response_buffering_resp_result_model_json['id'] = 'response_buffering'
        response_buffering_resp_result_model_json['value'] = 'off'
        response_buffering_resp_result_model_json['editable'] = True
        response_buffering_resp_result_model_json['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a model instance of ResponseBufferingRespResult by calling from_dict on the json representation
        response_buffering_resp_result_model = ResponseBufferingRespResult.from_dict(response_buffering_resp_result_model_json)
        assert response_buffering_resp_result_model != False

        # Construct a model instance of ResponseBufferingRespResult by calling from_dict on the json representation
        response_buffering_resp_result_model_dict = ResponseBufferingRespResult.from_dict(response_buffering_resp_result_model_json).__dict__
        response_buffering_resp_result_model2 = ResponseBufferingRespResult(**response_buffering_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert response_buffering_resp_result_model == response_buffering_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        response_buffering_resp_result_model_json2 = response_buffering_resp_result_model.to_dict()
        assert response_buffering_resp_result_model_json2 == response_buffering_resp_result_model_json


class TestModel_ScriptLoadOptimizationRespResult:
    """
    Test Class for ScriptLoadOptimizationRespResult
    """

    def test_script_load_optimization_resp_result_serialization(self):
        """
        Test serialization/deserialization for ScriptLoadOptimizationRespResult
        """

        # Construct a json representation of a ScriptLoadOptimizationRespResult model
        script_load_optimization_resp_result_model_json = {}
        script_load_optimization_resp_result_model_json['id'] = 'script_load_optimization'
        script_load_optimization_resp_result_model_json['value'] = 'off'
        script_load_optimization_resp_result_model_json['editable'] = True
        script_load_optimization_resp_result_model_json['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a model instance of ScriptLoadOptimizationRespResult by calling from_dict on the json representation
        script_load_optimization_resp_result_model = ScriptLoadOptimizationRespResult.from_dict(script_load_optimization_resp_result_model_json)
        assert script_load_optimization_resp_result_model != False

        # Construct a model instance of ScriptLoadOptimizationRespResult by calling from_dict on the json representation
        script_load_optimization_resp_result_model_dict = ScriptLoadOptimizationRespResult.from_dict(script_load_optimization_resp_result_model_json).__dict__
        script_load_optimization_resp_result_model2 = ScriptLoadOptimizationRespResult(**script_load_optimization_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert script_load_optimization_resp_result_model == script_load_optimization_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        script_load_optimization_resp_result_model_json2 = script_load_optimization_resp_result_model.to_dict()
        assert script_load_optimization_resp_result_model_json2 == script_load_optimization_resp_result_model_json


class TestModel_SecurityHeaderRespResult:
    """
    Test Class for SecurityHeaderRespResult
    """

    def test_security_header_resp_result_serialization(self):
        """
        Test serialization/deserialization for SecurityHeaderRespResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        security_header_resp_result_value_strict_transport_security_model = {}  # SecurityHeaderRespResultValueStrictTransportSecurity
        security_header_resp_result_value_strict_transport_security_model['enabled'] = True
        security_header_resp_result_value_strict_transport_security_model['max_age'] = 86400
        security_header_resp_result_value_strict_transport_security_model['include_subdomains'] = True
        security_header_resp_result_value_strict_transport_security_model['preload'] = True
        security_header_resp_result_value_strict_transport_security_model['nosniff'] = True

        security_header_resp_result_value_model = {}  # SecurityHeaderRespResultValue
        security_header_resp_result_value_model['strict_transport_security'] = security_header_resp_result_value_strict_transport_security_model

        # Construct a json representation of a SecurityHeaderRespResult model
        security_header_resp_result_model_json = {}
        security_header_resp_result_model_json['id'] = 'security_header'
        security_header_resp_result_model_json['value'] = security_header_resp_result_value_model
        security_header_resp_result_model_json['editable'] = True
        security_header_resp_result_model_json['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a model instance of SecurityHeaderRespResult by calling from_dict on the json representation
        security_header_resp_result_model = SecurityHeaderRespResult.from_dict(security_header_resp_result_model_json)
        assert security_header_resp_result_model != False

        # Construct a model instance of SecurityHeaderRespResult by calling from_dict on the json representation
        security_header_resp_result_model_dict = SecurityHeaderRespResult.from_dict(security_header_resp_result_model_json).__dict__
        security_header_resp_result_model2 = SecurityHeaderRespResult(**security_header_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert security_header_resp_result_model == security_header_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        security_header_resp_result_model_json2 = security_header_resp_result_model.to_dict()
        assert security_header_resp_result_model_json2 == security_header_resp_result_model_json


class TestModel_SecurityHeaderRespResultValue:
    """
    Test Class for SecurityHeaderRespResultValue
    """

    def test_security_header_resp_result_value_serialization(self):
        """
        Test serialization/deserialization for SecurityHeaderRespResultValue
        """

        # Construct dict forms of any model objects needed in order to build this model.

        security_header_resp_result_value_strict_transport_security_model = {}  # SecurityHeaderRespResultValueStrictTransportSecurity
        security_header_resp_result_value_strict_transport_security_model['enabled'] = True
        security_header_resp_result_value_strict_transport_security_model['max_age'] = 86400
        security_header_resp_result_value_strict_transport_security_model['include_subdomains'] = True
        security_header_resp_result_value_strict_transport_security_model['preload'] = True
        security_header_resp_result_value_strict_transport_security_model['nosniff'] = True

        # Construct a json representation of a SecurityHeaderRespResultValue model
        security_header_resp_result_value_model_json = {}
        security_header_resp_result_value_model_json['strict_transport_security'] = security_header_resp_result_value_strict_transport_security_model

        # Construct a model instance of SecurityHeaderRespResultValue by calling from_dict on the json representation
        security_header_resp_result_value_model = SecurityHeaderRespResultValue.from_dict(security_header_resp_result_value_model_json)
        assert security_header_resp_result_value_model != False

        # Construct a model instance of SecurityHeaderRespResultValue by calling from_dict on the json representation
        security_header_resp_result_value_model_dict = SecurityHeaderRespResultValue.from_dict(security_header_resp_result_value_model_json).__dict__
        security_header_resp_result_value_model2 = SecurityHeaderRespResultValue(**security_header_resp_result_value_model_dict)

        # Verify the model instances are equivalent
        assert security_header_resp_result_value_model == security_header_resp_result_value_model2

        # Convert model instance back to dict and verify no loss of data
        security_header_resp_result_value_model_json2 = security_header_resp_result_value_model.to_dict()
        assert security_header_resp_result_value_model_json2 == security_header_resp_result_value_model_json


class TestModel_SecurityHeaderRespResultValueStrictTransportSecurity:
    """
    Test Class for SecurityHeaderRespResultValueStrictTransportSecurity
    """

    def test_security_header_resp_result_value_strict_transport_security_serialization(self):
        """
        Test serialization/deserialization for SecurityHeaderRespResultValueStrictTransportSecurity
        """

        # Construct a json representation of a SecurityHeaderRespResultValueStrictTransportSecurity model
        security_header_resp_result_value_strict_transport_security_model_json = {}
        security_header_resp_result_value_strict_transport_security_model_json['enabled'] = True
        security_header_resp_result_value_strict_transport_security_model_json['max_age'] = 86400
        security_header_resp_result_value_strict_transport_security_model_json['include_subdomains'] = True
        security_header_resp_result_value_strict_transport_security_model_json['preload'] = True
        security_header_resp_result_value_strict_transport_security_model_json['nosniff'] = True

        # Construct a model instance of SecurityHeaderRespResultValueStrictTransportSecurity by calling from_dict on the json representation
        security_header_resp_result_value_strict_transport_security_model = SecurityHeaderRespResultValueStrictTransportSecurity.from_dict(security_header_resp_result_value_strict_transport_security_model_json)
        assert security_header_resp_result_value_strict_transport_security_model != False

        # Construct a model instance of SecurityHeaderRespResultValueStrictTransportSecurity by calling from_dict on the json representation
        security_header_resp_result_value_strict_transport_security_model_dict = SecurityHeaderRespResultValueStrictTransportSecurity.from_dict(security_header_resp_result_value_strict_transport_security_model_json).__dict__
        security_header_resp_result_value_strict_transport_security_model2 = SecurityHeaderRespResultValueStrictTransportSecurity(**security_header_resp_result_value_strict_transport_security_model_dict)

        # Verify the model instances are equivalent
        assert security_header_resp_result_value_strict_transport_security_model == security_header_resp_result_value_strict_transport_security_model2

        # Convert model instance back to dict and verify no loss of data
        security_header_resp_result_value_strict_transport_security_model_json2 = security_header_resp_result_value_strict_transport_security_model.to_dict()
        assert security_header_resp_result_value_strict_transport_security_model_json2 == security_header_resp_result_value_strict_transport_security_model_json


class TestModel_SecurityHeaderSettingValue:
    """
    Test Class for SecurityHeaderSettingValue
    """

    def test_security_header_setting_value_serialization(self):
        """
        Test serialization/deserialization for SecurityHeaderSettingValue
        """

        # Construct dict forms of any model objects needed in order to build this model.

        security_header_setting_value_strict_transport_security_model = {}  # SecurityHeaderSettingValueStrictTransportSecurity
        security_header_setting_value_strict_transport_security_model['enabled'] = True
        security_header_setting_value_strict_transport_security_model['max_age'] = 86400
        security_header_setting_value_strict_transport_security_model['include_subdomains'] = True
        security_header_setting_value_strict_transport_security_model['preload'] = True
        security_header_setting_value_strict_transport_security_model['nosniff'] = True

        # Construct a json representation of a SecurityHeaderSettingValue model
        security_header_setting_value_model_json = {}
        security_header_setting_value_model_json['strict_transport_security'] = security_header_setting_value_strict_transport_security_model

        # Construct a model instance of SecurityHeaderSettingValue by calling from_dict on the json representation
        security_header_setting_value_model = SecurityHeaderSettingValue.from_dict(security_header_setting_value_model_json)
        assert security_header_setting_value_model != False

        # Construct a model instance of SecurityHeaderSettingValue by calling from_dict on the json representation
        security_header_setting_value_model_dict = SecurityHeaderSettingValue.from_dict(security_header_setting_value_model_json).__dict__
        security_header_setting_value_model2 = SecurityHeaderSettingValue(**security_header_setting_value_model_dict)

        # Verify the model instances are equivalent
        assert security_header_setting_value_model == security_header_setting_value_model2

        # Convert model instance back to dict and verify no loss of data
        security_header_setting_value_model_json2 = security_header_setting_value_model.to_dict()
        assert security_header_setting_value_model_json2 == security_header_setting_value_model_json


class TestModel_SecurityHeaderSettingValueStrictTransportSecurity:
    """
    Test Class for SecurityHeaderSettingValueStrictTransportSecurity
    """

    def test_security_header_setting_value_strict_transport_security_serialization(self):
        """
        Test serialization/deserialization for SecurityHeaderSettingValueStrictTransportSecurity
        """

        # Construct a json representation of a SecurityHeaderSettingValueStrictTransportSecurity model
        security_header_setting_value_strict_transport_security_model_json = {}
        security_header_setting_value_strict_transport_security_model_json['enabled'] = True
        security_header_setting_value_strict_transport_security_model_json['max_age'] = 86400
        security_header_setting_value_strict_transport_security_model_json['include_subdomains'] = True
        security_header_setting_value_strict_transport_security_model_json['preload'] = True
        security_header_setting_value_strict_transport_security_model_json['nosniff'] = True

        # Construct a model instance of SecurityHeaderSettingValueStrictTransportSecurity by calling from_dict on the json representation
        security_header_setting_value_strict_transport_security_model = SecurityHeaderSettingValueStrictTransportSecurity.from_dict(security_header_setting_value_strict_transport_security_model_json)
        assert security_header_setting_value_strict_transport_security_model != False

        # Construct a model instance of SecurityHeaderSettingValueStrictTransportSecurity by calling from_dict on the json representation
        security_header_setting_value_strict_transport_security_model_dict = SecurityHeaderSettingValueStrictTransportSecurity.from_dict(security_header_setting_value_strict_transport_security_model_json).__dict__
        security_header_setting_value_strict_transport_security_model2 = SecurityHeaderSettingValueStrictTransportSecurity(**security_header_setting_value_strict_transport_security_model_dict)

        # Verify the model instances are equivalent
        assert security_header_setting_value_strict_transport_security_model == security_header_setting_value_strict_transport_security_model2

        # Convert model instance back to dict and verify no loss of data
        security_header_setting_value_strict_transport_security_model_json2 = security_header_setting_value_strict_transport_security_model.to_dict()
        assert security_header_setting_value_strict_transport_security_model_json2 == security_header_setting_value_strict_transport_security_model_json


class TestModel_ServerSideExcludeRespResult:
    """
    Test Class for ServerSideExcludeRespResult
    """

    def test_server_side_exclude_resp_result_serialization(self):
        """
        Test serialization/deserialization for ServerSideExcludeRespResult
        """

        # Construct a json representation of a ServerSideExcludeRespResult model
        server_side_exclude_resp_result_model_json = {}
        server_side_exclude_resp_result_model_json['id'] = 'server_side_exclude'
        server_side_exclude_resp_result_model_json['value'] = 'off'
        server_side_exclude_resp_result_model_json['editable'] = True
        server_side_exclude_resp_result_model_json['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a model instance of ServerSideExcludeRespResult by calling from_dict on the json representation
        server_side_exclude_resp_result_model = ServerSideExcludeRespResult.from_dict(server_side_exclude_resp_result_model_json)
        assert server_side_exclude_resp_result_model != False

        # Construct a model instance of ServerSideExcludeRespResult by calling from_dict on the json representation
        server_side_exclude_resp_result_model_dict = ServerSideExcludeRespResult.from_dict(server_side_exclude_resp_result_model_json).__dict__
        server_side_exclude_resp_result_model2 = ServerSideExcludeRespResult(**server_side_exclude_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert server_side_exclude_resp_result_model == server_side_exclude_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        server_side_exclude_resp_result_model_json2 = server_side_exclude_resp_result_model.to_dict()
        assert server_side_exclude_resp_result_model_json2 == server_side_exclude_resp_result_model_json


class TestModel_TlsClientAuthRespResult:
    """
    Test Class for TlsClientAuthRespResult
    """

    def test_tls_client_auth_resp_result_serialization(self):
        """
        Test serialization/deserialization for TlsClientAuthRespResult
        """

        # Construct a json representation of a TlsClientAuthRespResult model
        tls_client_auth_resp_result_model_json = {}
        tls_client_auth_resp_result_model_json['id'] = 'tls_client_auth'
        tls_client_auth_resp_result_model_json['value'] = 'off'
        tls_client_auth_resp_result_model_json['editable'] = True
        tls_client_auth_resp_result_model_json['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a model instance of TlsClientAuthRespResult by calling from_dict on the json representation
        tls_client_auth_resp_result_model = TlsClientAuthRespResult.from_dict(tls_client_auth_resp_result_model_json)
        assert tls_client_auth_resp_result_model != False

        # Construct a model instance of TlsClientAuthRespResult by calling from_dict on the json representation
        tls_client_auth_resp_result_model_dict = TlsClientAuthRespResult.from_dict(tls_client_auth_resp_result_model_json).__dict__
        tls_client_auth_resp_result_model2 = TlsClientAuthRespResult(**tls_client_auth_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert tls_client_auth_resp_result_model == tls_client_auth_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        tls_client_auth_resp_result_model_json2 = tls_client_auth_resp_result_model.to_dict()
        assert tls_client_auth_resp_result_model_json2 == tls_client_auth_resp_result_model_json


class TestModel_TrueClientIpRespResult:
    """
    Test Class for TrueClientIpRespResult
    """

    def test_true_client_ip_resp_result_serialization(self):
        """
        Test serialization/deserialization for TrueClientIpRespResult
        """

        # Construct a json representation of a TrueClientIpRespResult model
        true_client_ip_resp_result_model_json = {}
        true_client_ip_resp_result_model_json['id'] = 'true_client_ip_header'
        true_client_ip_resp_result_model_json['value'] = 'off'
        true_client_ip_resp_result_model_json['editable'] = True
        true_client_ip_resp_result_model_json['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a model instance of TrueClientIpRespResult by calling from_dict on the json representation
        true_client_ip_resp_result_model = TrueClientIpRespResult.from_dict(true_client_ip_resp_result_model_json)
        assert true_client_ip_resp_result_model != False

        # Construct a model instance of TrueClientIpRespResult by calling from_dict on the json representation
        true_client_ip_resp_result_model_dict = TrueClientIpRespResult.from_dict(true_client_ip_resp_result_model_json).__dict__
        true_client_ip_resp_result_model2 = TrueClientIpRespResult(**true_client_ip_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert true_client_ip_resp_result_model == true_client_ip_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        true_client_ip_resp_result_model_json2 = true_client_ip_resp_result_model.to_dict()
        assert true_client_ip_resp_result_model_json2 == true_client_ip_resp_result_model_json


class TestModel_WafRespResult:
    """
    Test Class for WafRespResult
    """

    def test_waf_resp_result_serialization(self):
        """
        Test serialization/deserialization for WafRespResult
        """

        # Construct a json representation of a WafRespResult model
        waf_resp_result_model_json = {}
        waf_resp_result_model_json['id'] = 'waf'
        waf_resp_result_model_json['value'] = 'off'
        waf_resp_result_model_json['editable'] = True
        waf_resp_result_model_json['modified_on'] = '2018-12-08T18:57:43.889000Z'

        # Construct a model instance of WafRespResult by calling from_dict on the json representation
        waf_resp_result_model = WafRespResult.from_dict(waf_resp_result_model_json)
        assert waf_resp_result_model != False

        # Construct a model instance of WafRespResult by calling from_dict on the json representation
        waf_resp_result_model_dict = WafRespResult.from_dict(waf_resp_result_model_json).__dict__
        waf_resp_result_model2 = WafRespResult(**waf_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert waf_resp_result_model == waf_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        waf_resp_result_model_json2 = waf_resp_result_model.to_dict()
        assert waf_resp_result_model_json2 == waf_resp_result_model_json


class TestModel_WebsocketsRespResult:
    """
    Test Class for WebsocketsRespResult
    """

    def test_websockets_resp_result_serialization(self):
        """
        Test serialization/deserialization for WebsocketsRespResult
        """

        # Construct a json representation of a WebsocketsRespResult model
        websockets_resp_result_model_json = {}
        websockets_resp_result_model_json['id'] = 'websockets'
        websockets_resp_result_model_json['value'] = 'off'
        websockets_resp_result_model_json['editable'] = True
        websockets_resp_result_model_json['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a model instance of WebsocketsRespResult by calling from_dict on the json representation
        websockets_resp_result_model = WebsocketsRespResult.from_dict(websockets_resp_result_model_json)
        assert websockets_resp_result_model != False

        # Construct a model instance of WebsocketsRespResult by calling from_dict on the json representation
        websockets_resp_result_model_dict = WebsocketsRespResult.from_dict(websockets_resp_result_model_json).__dict__
        websockets_resp_result_model2 = WebsocketsRespResult(**websockets_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert websockets_resp_result_model == websockets_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        websockets_resp_result_model_json2 = websockets_resp_result_model.to_dict()
        assert websockets_resp_result_model_json2 == websockets_resp_result_model_json


class TestModel_ZonesDnssecRespResult:
    """
    Test Class for ZonesDnssecRespResult
    """

    def test_zones_dnssec_resp_result_serialization(self):
        """
        Test serialization/deserialization for ZonesDnssecRespResult
        """

        # Construct a json representation of a ZonesDnssecRespResult model
        zones_dnssec_resp_result_model_json = {}
        zones_dnssec_resp_result_model_json['status'] = 'active'
        zones_dnssec_resp_result_model_json['flags'] = 257
        zones_dnssec_resp_result_model_json['algorithm'] = '13'
        zones_dnssec_resp_result_model_json['key_type'] = 'ECDSAP256SHA256'
        zones_dnssec_resp_result_model_json['digest_type'] = '2'
        zones_dnssec_resp_result_model_json['digest_algorithm'] = 'SHA256'
        zones_dnssec_resp_result_model_json['digest'] = '48E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45'
        zones_dnssec_resp_result_model_json['ds'] = 'example.com. 3600 IN DS 16953 13 2 248E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45'
        zones_dnssec_resp_result_model_json['key_tag'] = 42
        zones_dnssec_resp_result_model_json['public_key'] = 'oXiGYrSTO+LSCJ3mohc8EP+CzF9KxBj8/ydXJ22pKuZP3VAC3/Md/k7xZfz470CoRyZJ6gV6vml07IC3d8xqhA=='

        # Construct a model instance of ZonesDnssecRespResult by calling from_dict on the json representation
        zones_dnssec_resp_result_model = ZonesDnssecRespResult.from_dict(zones_dnssec_resp_result_model_json)
        assert zones_dnssec_resp_result_model != False

        # Construct a model instance of ZonesDnssecRespResult by calling from_dict on the json representation
        zones_dnssec_resp_result_model_dict = ZonesDnssecRespResult.from_dict(zones_dnssec_resp_result_model_json).__dict__
        zones_dnssec_resp_result_model2 = ZonesDnssecRespResult(**zones_dnssec_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert zones_dnssec_resp_result_model == zones_dnssec_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        zones_dnssec_resp_result_model_json2 = zones_dnssec_resp_result_model.to_dict()
        assert zones_dnssec_resp_result_model_json2 == zones_dnssec_resp_result_model_json


class TestModel_AlwaysUseHttpsResp:
    """
    Test Class for AlwaysUseHttpsResp
    """

    def test_always_use_https_resp_serialization(self):
        """
        Test serialization/deserialization for AlwaysUseHttpsResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        always_use_https_resp_result_model = {}  # AlwaysUseHttpsRespResult
        always_use_https_resp_result_model['id'] = 'always_use_https'
        always_use_https_resp_result_model['value'] = 'off'
        always_use_https_resp_result_model['editable'] = True
        always_use_https_resp_result_model['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a json representation of a AlwaysUseHttpsResp model
        always_use_https_resp_model_json = {}
        always_use_https_resp_model_json['result'] = always_use_https_resp_result_model
        always_use_https_resp_model_json['success'] = True
        always_use_https_resp_model_json['errors'] = [['testString']]
        always_use_https_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of AlwaysUseHttpsResp by calling from_dict on the json representation
        always_use_https_resp_model = AlwaysUseHttpsResp.from_dict(always_use_https_resp_model_json)
        assert always_use_https_resp_model != False

        # Construct a model instance of AlwaysUseHttpsResp by calling from_dict on the json representation
        always_use_https_resp_model_dict = AlwaysUseHttpsResp.from_dict(always_use_https_resp_model_json).__dict__
        always_use_https_resp_model2 = AlwaysUseHttpsResp(**always_use_https_resp_model_dict)

        # Verify the model instances are equivalent
        assert always_use_https_resp_model == always_use_https_resp_model2

        # Convert model instance back to dict and verify no loss of data
        always_use_https_resp_model_json2 = always_use_https_resp_model.to_dict()
        assert always_use_https_resp_model_json2 == always_use_https_resp_model_json


class TestModel_AutomaticHttpsRewritesResp:
    """
    Test Class for AutomaticHttpsRewritesResp
    """

    def test_automatic_https_rewrites_resp_serialization(self):
        """
        Test serialization/deserialization for AutomaticHttpsRewritesResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        automatic_https_rewrites_resp_result_model = {}  # AutomaticHttpsRewritesRespResult
        automatic_https_rewrites_resp_result_model['id'] = 'automatic_https_rewrites'
        automatic_https_rewrites_resp_result_model['value'] = 'off'
        automatic_https_rewrites_resp_result_model['editable'] = True
        automatic_https_rewrites_resp_result_model['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a json representation of a AutomaticHttpsRewritesResp model
        automatic_https_rewrites_resp_model_json = {}
        automatic_https_rewrites_resp_model_json['result'] = automatic_https_rewrites_resp_result_model
        automatic_https_rewrites_resp_model_json['success'] = True
        automatic_https_rewrites_resp_model_json['errors'] = [['testString']]
        automatic_https_rewrites_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of AutomaticHttpsRewritesResp by calling from_dict on the json representation
        automatic_https_rewrites_resp_model = AutomaticHttpsRewritesResp.from_dict(automatic_https_rewrites_resp_model_json)
        assert automatic_https_rewrites_resp_model != False

        # Construct a model instance of AutomaticHttpsRewritesResp by calling from_dict on the json representation
        automatic_https_rewrites_resp_model_dict = AutomaticHttpsRewritesResp.from_dict(automatic_https_rewrites_resp_model_json).__dict__
        automatic_https_rewrites_resp_model2 = AutomaticHttpsRewritesResp(**automatic_https_rewrites_resp_model_dict)

        # Verify the model instances are equivalent
        assert automatic_https_rewrites_resp_model == automatic_https_rewrites_resp_model2

        # Convert model instance back to dict and verify no loss of data
        automatic_https_rewrites_resp_model_json2 = automatic_https_rewrites_resp_model.to_dict()
        assert automatic_https_rewrites_resp_model_json2 == automatic_https_rewrites_resp_model_json


class TestModel_BotMgtResp:
    """
    Test Class for BotMgtResp
    """

    def test_bot_mgt_resp_serialization(self):
        """
        Test serialization/deserialization for BotMgtResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        bot_mgt_settings_model = {}  # BotMgtSettings
        bot_mgt_settings_model['session_score'] = False
        bot_mgt_settings_model['enable_js'] = False
        bot_mgt_settings_model['use_latest_model'] = False
        bot_mgt_settings_model['ai_bots_protection'] = 'block'

        # Construct a json representation of a BotMgtResp model
        bot_mgt_resp_model_json = {}
        bot_mgt_resp_model_json['success'] = True
        bot_mgt_resp_model_json['errors'] = [['testString']]
        bot_mgt_resp_model_json['messages'] = [['testString']]
        bot_mgt_resp_model_json['result'] = bot_mgt_settings_model

        # Construct a model instance of BotMgtResp by calling from_dict on the json representation
        bot_mgt_resp_model = BotMgtResp.from_dict(bot_mgt_resp_model_json)
        assert bot_mgt_resp_model != False

        # Construct a model instance of BotMgtResp by calling from_dict on the json representation
        bot_mgt_resp_model_dict = BotMgtResp.from_dict(bot_mgt_resp_model_json).__dict__
        bot_mgt_resp_model2 = BotMgtResp(**bot_mgt_resp_model_dict)

        # Verify the model instances are equivalent
        assert bot_mgt_resp_model == bot_mgt_resp_model2

        # Convert model instance back to dict and verify no loss of data
        bot_mgt_resp_model_json2 = bot_mgt_resp_model.to_dict()
        assert bot_mgt_resp_model_json2 == bot_mgt_resp_model_json


class TestModel_BotMgtSettings:
    """
    Test Class for BotMgtSettings
    """

    def test_bot_mgt_settings_serialization(self):
        """
        Test serialization/deserialization for BotMgtSettings
        """

        # Construct a json representation of a BotMgtSettings model
        bot_mgt_settings_model_json = {}
        bot_mgt_settings_model_json['session_score'] = False
        bot_mgt_settings_model_json['enable_js'] = False
        bot_mgt_settings_model_json['use_latest_model'] = False
        bot_mgt_settings_model_json['ai_bots_protection'] = 'block'

        # Construct a model instance of BotMgtSettings by calling from_dict on the json representation
        bot_mgt_settings_model = BotMgtSettings.from_dict(bot_mgt_settings_model_json)
        assert bot_mgt_settings_model != False

        # Construct a model instance of BotMgtSettings by calling from_dict on the json representation
        bot_mgt_settings_model_dict = BotMgtSettings.from_dict(bot_mgt_settings_model_json).__dict__
        bot_mgt_settings_model2 = BotMgtSettings(**bot_mgt_settings_model_dict)

        # Verify the model instances are equivalent
        assert bot_mgt_settings_model == bot_mgt_settings_model2

        # Convert model instance back to dict and verify no loss of data
        bot_mgt_settings_model_json2 = bot_mgt_settings_model.to_dict()
        assert bot_mgt_settings_model_json2 == bot_mgt_settings_model_json


class TestModel_BrotliResp:
    """
    Test Class for BrotliResp
    """

    def test_brotli_resp_serialization(self):
        """
        Test serialization/deserialization for BrotliResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        brotli_resp_result_model = {}  # BrotliRespResult
        brotli_resp_result_model['id'] = 'brotli'
        brotli_resp_result_model['value'] = 'off'
        brotli_resp_result_model['editable'] = True
        brotli_resp_result_model['modified_on'] = '2018-12-08T18:57:52.826000Z'

        # Construct a json representation of a BrotliResp model
        brotli_resp_model_json = {}
        brotli_resp_model_json['result'] = brotli_resp_result_model
        brotli_resp_model_json['success'] = True
        brotli_resp_model_json['errors'] = [['testString']]
        brotli_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of BrotliResp by calling from_dict on the json representation
        brotli_resp_model = BrotliResp.from_dict(brotli_resp_model_json)
        assert brotli_resp_model != False

        # Construct a model instance of BrotliResp by calling from_dict on the json representation
        brotli_resp_model_dict = BrotliResp.from_dict(brotli_resp_model_json).__dict__
        brotli_resp_model2 = BrotliResp(**brotli_resp_model_dict)

        # Verify the model instances are equivalent
        assert brotli_resp_model == brotli_resp_model2

        # Convert model instance back to dict and verify no loss of data
        brotli_resp_model_json2 = brotli_resp_model.to_dict()
        assert brotli_resp_model_json2 == brotli_resp_model_json


class TestModel_BrowserCheckResp:
    """
    Test Class for BrowserCheckResp
    """

    def test_browser_check_resp_serialization(self):
        """
        Test serialization/deserialization for BrowserCheckResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        browser_check_resp_result_model = {}  # BrowserCheckRespResult
        browser_check_resp_result_model['id'] = 'browser_check'
        browser_check_resp_result_model['value'] = 'off'
        browser_check_resp_result_model['editable'] = True
        browser_check_resp_result_model['modified_on'] = '2018-12-08T18:57:14.506000Z'

        # Construct a json representation of a BrowserCheckResp model
        browser_check_resp_model_json = {}
        browser_check_resp_model_json['result'] = browser_check_resp_result_model
        browser_check_resp_model_json['success'] = True
        browser_check_resp_model_json['errors'] = [['testString']]
        browser_check_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of BrowserCheckResp by calling from_dict on the json representation
        browser_check_resp_model = BrowserCheckResp.from_dict(browser_check_resp_model_json)
        assert browser_check_resp_model != False

        # Construct a model instance of BrowserCheckResp by calling from_dict on the json representation
        browser_check_resp_model_dict = BrowserCheckResp.from_dict(browser_check_resp_model_json).__dict__
        browser_check_resp_model2 = BrowserCheckResp(**browser_check_resp_model_dict)

        # Verify the model instances are equivalent
        assert browser_check_resp_model == browser_check_resp_model2

        # Convert model instance back to dict and verify no loss of data
        browser_check_resp_model_json2 = browser_check_resp_model.to_dict()
        assert browser_check_resp_model_json2 == browser_check_resp_model_json


class TestModel_ChallengeTtlResp:
    """
    Test Class for ChallengeTtlResp
    """

    def test_challenge_ttl_resp_serialization(self):
        """
        Test serialization/deserialization for ChallengeTtlResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        challenge_ttl_resp_result_model = {}  # ChallengeTtlRespResult
        challenge_ttl_resp_result_model['id'] = 'challenge_ttl'
        challenge_ttl_resp_result_model['value'] = 1800
        challenge_ttl_resp_result_model['editable'] = True
        challenge_ttl_resp_result_model['modified_on'] = '2018-09-17T07:21:39.844000Z'

        # Construct a json representation of a ChallengeTtlResp model
        challenge_ttl_resp_model_json = {}
        challenge_ttl_resp_model_json['result'] = challenge_ttl_resp_result_model
        challenge_ttl_resp_model_json['success'] = True
        challenge_ttl_resp_model_json['errors'] = [['testString']]
        challenge_ttl_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of ChallengeTtlResp by calling from_dict on the json representation
        challenge_ttl_resp_model = ChallengeTtlResp.from_dict(challenge_ttl_resp_model_json)
        assert challenge_ttl_resp_model != False

        # Construct a model instance of ChallengeTtlResp by calling from_dict on the json representation
        challenge_ttl_resp_model_dict = ChallengeTtlResp.from_dict(challenge_ttl_resp_model_json).__dict__
        challenge_ttl_resp_model2 = ChallengeTtlResp(**challenge_ttl_resp_model_dict)

        # Verify the model instances are equivalent
        assert challenge_ttl_resp_model == challenge_ttl_resp_model2

        # Convert model instance back to dict and verify no loss of data
        challenge_ttl_resp_model_json2 = challenge_ttl_resp_model.to_dict()
        assert challenge_ttl_resp_model_json2 == challenge_ttl_resp_model_json


class TestModel_CiphersResp:
    """
    Test Class for CiphersResp
    """

    def test_ciphers_resp_serialization(self):
        """
        Test serialization/deserialization for CiphersResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        ciphers_resp_result_model = {}  # CiphersRespResult
        ciphers_resp_result_model['id'] = 'ciphers'
        ciphers_resp_result_model['value'] = ['AES256-GCM-SHA384', 'AES256-SHA256']
        ciphers_resp_result_model['editable'] = True
        ciphers_resp_result_model['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a json representation of a CiphersResp model
        ciphers_resp_model_json = {}
        ciphers_resp_model_json['result'] = ciphers_resp_result_model
        ciphers_resp_model_json['success'] = True
        ciphers_resp_model_json['errors'] = [['testString']]
        ciphers_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of CiphersResp by calling from_dict on the json representation
        ciphers_resp_model = CiphersResp.from_dict(ciphers_resp_model_json)
        assert ciphers_resp_model != False

        # Construct a model instance of CiphersResp by calling from_dict on the json representation
        ciphers_resp_model_dict = CiphersResp.from_dict(ciphers_resp_model_json).__dict__
        ciphers_resp_model2 = CiphersResp(**ciphers_resp_model_dict)

        # Verify the model instances are equivalent
        assert ciphers_resp_model == ciphers_resp_model2

        # Convert model instance back to dict and verify no loss of data
        ciphers_resp_model_json2 = ciphers_resp_model.to_dict()
        assert ciphers_resp_model_json2 == ciphers_resp_model_json


class TestModel_CnameFlatteningResponse:
    """
    Test Class for CnameFlatteningResponse
    """

    def test_cname_flattening_response_serialization(self):
        """
        Test serialization/deserialization for CnameFlatteningResponse
        """

        # Construct a json representation of a CnameFlatteningResponse model
        cname_flattening_response_model_json = {}
        cname_flattening_response_model_json['id'] = 'cname_flattening'
        cname_flattening_response_model_json['value'] = 'flatten_all'
        cname_flattening_response_model_json['modified_on'] = '2014-01-01T05:20:00.123000Z'
        cname_flattening_response_model_json['editable'] = True

        # Construct a model instance of CnameFlatteningResponse by calling from_dict on the json representation
        cname_flattening_response_model = CnameFlatteningResponse.from_dict(cname_flattening_response_model_json)
        assert cname_flattening_response_model != False

        # Construct a model instance of CnameFlatteningResponse by calling from_dict on the json representation
        cname_flattening_response_model_dict = CnameFlatteningResponse.from_dict(cname_flattening_response_model_json).__dict__
        cname_flattening_response_model2 = CnameFlatteningResponse(**cname_flattening_response_model_dict)

        # Verify the model instances are equivalent
        assert cname_flattening_response_model == cname_flattening_response_model2

        # Convert model instance back to dict and verify no loss of data
        cname_flattening_response_model_json2 = cname_flattening_response_model.to_dict()
        assert cname_flattening_response_model_json2 == cname_flattening_response_model_json


class TestModel_EmailObfuscationResp:
    """
    Test Class for EmailObfuscationResp
    """

    def test_email_obfuscation_resp_serialization(self):
        """
        Test serialization/deserialization for EmailObfuscationResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        email_obfuscation_resp_result_model = {}  # EmailObfuscationRespResult
        email_obfuscation_resp_result_model['id'] = 'email_obfuscation'
        email_obfuscation_resp_result_model['value'] = 'off'
        email_obfuscation_resp_result_model['editable'] = True
        email_obfuscation_resp_result_model['modified_on'] = '2017-01-01T05:20:00.123000Z'

        # Construct a json representation of a EmailObfuscationResp model
        email_obfuscation_resp_model_json = {}
        email_obfuscation_resp_model_json['result'] = email_obfuscation_resp_result_model
        email_obfuscation_resp_model_json['success'] = True
        email_obfuscation_resp_model_json['errors'] = [['testString']]
        email_obfuscation_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of EmailObfuscationResp by calling from_dict on the json representation
        email_obfuscation_resp_model = EmailObfuscationResp.from_dict(email_obfuscation_resp_model_json)
        assert email_obfuscation_resp_model != False

        # Construct a model instance of EmailObfuscationResp by calling from_dict on the json representation
        email_obfuscation_resp_model_dict = EmailObfuscationResp.from_dict(email_obfuscation_resp_model_json).__dict__
        email_obfuscation_resp_model2 = EmailObfuscationResp(**email_obfuscation_resp_model_dict)

        # Verify the model instances are equivalent
        assert email_obfuscation_resp_model == email_obfuscation_resp_model2

        # Convert model instance back to dict and verify no loss of data
        email_obfuscation_resp_model_json2 = email_obfuscation_resp_model.to_dict()
        assert email_obfuscation_resp_model_json2 == email_obfuscation_resp_model_json


class TestModel_HotlinkProtectionResp:
    """
    Test Class for HotlinkProtectionResp
    """

    def test_hotlink_protection_resp_serialization(self):
        """
        Test serialization/deserialization for HotlinkProtectionResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        hotlink_protection_resp_result_model = {}  # HotlinkProtectionRespResult
        hotlink_protection_resp_result_model['id'] = 'hotlink_protection'
        hotlink_protection_resp_result_model['value'] = 'off'
        hotlink_protection_resp_result_model['editable'] = True
        hotlink_protection_resp_result_model['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a json representation of a HotlinkProtectionResp model
        hotlink_protection_resp_model_json = {}
        hotlink_protection_resp_model_json['result'] = hotlink_protection_resp_result_model
        hotlink_protection_resp_model_json['success'] = True
        hotlink_protection_resp_model_json['errors'] = [['testString']]
        hotlink_protection_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of HotlinkProtectionResp by calling from_dict on the json representation
        hotlink_protection_resp_model = HotlinkProtectionResp.from_dict(hotlink_protection_resp_model_json)
        assert hotlink_protection_resp_model != False

        # Construct a model instance of HotlinkProtectionResp by calling from_dict on the json representation
        hotlink_protection_resp_model_dict = HotlinkProtectionResp.from_dict(hotlink_protection_resp_model_json).__dict__
        hotlink_protection_resp_model2 = HotlinkProtectionResp(**hotlink_protection_resp_model_dict)

        # Verify the model instances are equivalent
        assert hotlink_protection_resp_model == hotlink_protection_resp_model2

        # Convert model instance back to dict and verify no loss of data
        hotlink_protection_resp_model_json2 = hotlink_protection_resp_model.to_dict()
        assert hotlink_protection_resp_model_json2 == hotlink_protection_resp_model_json


class TestModel_Http2Resp:
    """
    Test Class for Http2Resp
    """

    def test_http2_resp_serialization(self):
        """
        Test serialization/deserialization for Http2Resp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        http2_resp_result_model = {}  # Http2RespResult
        http2_resp_result_model['id'] = 'http2'
        http2_resp_result_model['value'] = 'off'
        http2_resp_result_model['editable'] = True
        http2_resp_result_model['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a json representation of a Http2Resp model
        http2_resp_model_json = {}
        http2_resp_model_json['result'] = http2_resp_result_model
        http2_resp_model_json['success'] = True
        http2_resp_model_json['errors'] = [['testString']]
        http2_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of Http2Resp by calling from_dict on the json representation
        http2_resp_model = Http2Resp.from_dict(http2_resp_model_json)
        assert http2_resp_model != False

        # Construct a model instance of Http2Resp by calling from_dict on the json representation
        http2_resp_model_dict = Http2Resp.from_dict(http2_resp_model_json).__dict__
        http2_resp_model2 = Http2Resp(**http2_resp_model_dict)

        # Verify the model instances are equivalent
        assert http2_resp_model == http2_resp_model2

        # Convert model instance back to dict and verify no loss of data
        http2_resp_model_json2 = http2_resp_model.to_dict()
        assert http2_resp_model_json2 == http2_resp_model_json


class TestModel_Http3Resp:
    """
    Test Class for Http3Resp
    """

    def test_http3_resp_serialization(self):
        """
        Test serialization/deserialization for Http3Resp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        http3_resp_result_model = {}  # Http3RespResult
        http3_resp_result_model['id'] = 'http3'
        http3_resp_result_model['value'] = 'off'
        http3_resp_result_model['editable'] = True
        http3_resp_result_model['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a json representation of a Http3Resp model
        http3_resp_model_json = {}
        http3_resp_model_json['result'] = http3_resp_result_model
        http3_resp_model_json['success'] = True
        http3_resp_model_json['errors'] = [['testString']]
        http3_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of Http3Resp by calling from_dict on the json representation
        http3_resp_model = Http3Resp.from_dict(http3_resp_model_json)
        assert http3_resp_model != False

        # Construct a model instance of Http3Resp by calling from_dict on the json representation
        http3_resp_model_dict = Http3Resp.from_dict(http3_resp_model_json).__dict__
        http3_resp_model2 = Http3Resp(**http3_resp_model_dict)

        # Verify the model instances are equivalent
        assert http3_resp_model == http3_resp_model2

        # Convert model instance back to dict and verify no loss of data
        http3_resp_model_json2 = http3_resp_model.to_dict()
        assert http3_resp_model_json2 == http3_resp_model_json


class TestModel_ImageLoadOptimizationResp:
    """
    Test Class for ImageLoadOptimizationResp
    """

    def test_image_load_optimization_resp_serialization(self):
        """
        Test serialization/deserialization for ImageLoadOptimizationResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        image_load_optimization_resp_result_model = {}  # ImageLoadOptimizationRespResult
        image_load_optimization_resp_result_model['id'] = 'image_load_optimization'
        image_load_optimization_resp_result_model['value'] = 'off'
        image_load_optimization_resp_result_model['editable'] = True
        image_load_optimization_resp_result_model['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a json representation of a ImageLoadOptimizationResp model
        image_load_optimization_resp_model_json = {}
        image_load_optimization_resp_model_json['result'] = image_load_optimization_resp_result_model
        image_load_optimization_resp_model_json['success'] = True
        image_load_optimization_resp_model_json['errors'] = [['testString']]
        image_load_optimization_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of ImageLoadOptimizationResp by calling from_dict on the json representation
        image_load_optimization_resp_model = ImageLoadOptimizationResp.from_dict(image_load_optimization_resp_model_json)
        assert image_load_optimization_resp_model != False

        # Construct a model instance of ImageLoadOptimizationResp by calling from_dict on the json representation
        image_load_optimization_resp_model_dict = ImageLoadOptimizationResp.from_dict(image_load_optimization_resp_model_json).__dict__
        image_load_optimization_resp_model2 = ImageLoadOptimizationResp(**image_load_optimization_resp_model_dict)

        # Verify the model instances are equivalent
        assert image_load_optimization_resp_model == image_load_optimization_resp_model2

        # Convert model instance back to dict and verify no loss of data
        image_load_optimization_resp_model_json2 = image_load_optimization_resp_model.to_dict()
        assert image_load_optimization_resp_model_json2 == image_load_optimization_resp_model_json


class TestModel_ImageSizeOptimizationResp:
    """
    Test Class for ImageSizeOptimizationResp
    """

    def test_image_size_optimization_resp_serialization(self):
        """
        Test serialization/deserialization for ImageSizeOptimizationResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        image_size_optimization_resp_result_model = {}  # ImageSizeOptimizationRespResult
        image_size_optimization_resp_result_model['id'] = 'image_size_optimization'
        image_size_optimization_resp_result_model['value'] = 'lossless'
        image_size_optimization_resp_result_model['editable'] = True
        image_size_optimization_resp_result_model['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a json representation of a ImageSizeOptimizationResp model
        image_size_optimization_resp_model_json = {}
        image_size_optimization_resp_model_json['result'] = image_size_optimization_resp_result_model
        image_size_optimization_resp_model_json['success'] = True
        image_size_optimization_resp_model_json['errors'] = [['testString']]
        image_size_optimization_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of ImageSizeOptimizationResp by calling from_dict on the json representation
        image_size_optimization_resp_model = ImageSizeOptimizationResp.from_dict(image_size_optimization_resp_model_json)
        assert image_size_optimization_resp_model != False

        # Construct a model instance of ImageSizeOptimizationResp by calling from_dict on the json representation
        image_size_optimization_resp_model_dict = ImageSizeOptimizationResp.from_dict(image_size_optimization_resp_model_json).__dict__
        image_size_optimization_resp_model2 = ImageSizeOptimizationResp(**image_size_optimization_resp_model_dict)

        # Verify the model instances are equivalent
        assert image_size_optimization_resp_model == image_size_optimization_resp_model2

        # Convert model instance back to dict and verify no loss of data
        image_size_optimization_resp_model_json2 = image_size_optimization_resp_model.to_dict()
        assert image_size_optimization_resp_model_json2 == image_size_optimization_resp_model_json


class TestModel_IpGeolocationResp:
    """
    Test Class for IpGeolocationResp
    """

    def test_ip_geolocation_resp_serialization(self):
        """
        Test serialization/deserialization for IpGeolocationResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        ip_geolocation_resp_result_model = {}  # IpGeolocationRespResult
        ip_geolocation_resp_result_model['id'] = 'ip_geolocation'
        ip_geolocation_resp_result_model['value'] = 'off'
        ip_geolocation_resp_result_model['editable'] = True
        ip_geolocation_resp_result_model['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a json representation of a IpGeolocationResp model
        ip_geolocation_resp_model_json = {}
        ip_geolocation_resp_model_json['result'] = ip_geolocation_resp_result_model
        ip_geolocation_resp_model_json['success'] = True
        ip_geolocation_resp_model_json['errors'] = [['testString']]
        ip_geolocation_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of IpGeolocationResp by calling from_dict on the json representation
        ip_geolocation_resp_model = IpGeolocationResp.from_dict(ip_geolocation_resp_model_json)
        assert ip_geolocation_resp_model != False

        # Construct a model instance of IpGeolocationResp by calling from_dict on the json representation
        ip_geolocation_resp_model_dict = IpGeolocationResp.from_dict(ip_geolocation_resp_model_json).__dict__
        ip_geolocation_resp_model2 = IpGeolocationResp(**ip_geolocation_resp_model_dict)

        # Verify the model instances are equivalent
        assert ip_geolocation_resp_model == ip_geolocation_resp_model2

        # Convert model instance back to dict and verify no loss of data
        ip_geolocation_resp_model_json2 = ip_geolocation_resp_model.to_dict()
        assert ip_geolocation_resp_model_json2 == ip_geolocation_resp_model_json


class TestModel_Ipv6Resp:
    """
    Test Class for Ipv6Resp
    """

    def test_ipv6_resp_serialization(self):
        """
        Test serialization/deserialization for Ipv6Resp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        ipv6_resp_result_model = {}  # Ipv6RespResult
        ipv6_resp_result_model['id'] = 'ipv6'
        ipv6_resp_result_model['value'] = 'off'
        ipv6_resp_result_model['editable'] = True
        ipv6_resp_result_model['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a json representation of a Ipv6Resp model
        ipv6_resp_model_json = {}
        ipv6_resp_model_json['result'] = ipv6_resp_result_model
        ipv6_resp_model_json['success'] = True
        ipv6_resp_model_json['errors'] = [['testString']]
        ipv6_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of Ipv6Resp by calling from_dict on the json representation
        ipv6_resp_model = Ipv6Resp.from_dict(ipv6_resp_model_json)
        assert ipv6_resp_model != False

        # Construct a model instance of Ipv6Resp by calling from_dict on the json representation
        ipv6_resp_model_dict = Ipv6Resp.from_dict(ipv6_resp_model_json).__dict__
        ipv6_resp_model2 = Ipv6Resp(**ipv6_resp_model_dict)

        # Verify the model instances are equivalent
        assert ipv6_resp_model == ipv6_resp_model2

        # Convert model instance back to dict and verify no loss of data
        ipv6_resp_model_json2 = ipv6_resp_model.to_dict()
        assert ipv6_resp_model_json2 == ipv6_resp_model_json


class TestModel_LogRetentionResp:
    """
    Test Class for LogRetentionResp
    """

    def test_log_retention_resp_serialization(self):
        """
        Test serialization/deserialization for LogRetentionResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        log_retention_resp_result_model = {}  # LogRetentionRespResult
        log_retention_resp_result_model['flag'] = True

        # Construct a json representation of a LogRetentionResp model
        log_retention_resp_model_json = {}
        log_retention_resp_model_json['success'] = True
        log_retention_resp_model_json['result'] = log_retention_resp_result_model
        log_retention_resp_model_json['errors'] = ['testString']
        log_retention_resp_model_json['messages'] = ['testString']

        # Construct a model instance of LogRetentionResp by calling from_dict on the json representation
        log_retention_resp_model = LogRetentionResp.from_dict(log_retention_resp_model_json)
        assert log_retention_resp_model != False

        # Construct a model instance of LogRetentionResp by calling from_dict on the json representation
        log_retention_resp_model_dict = LogRetentionResp.from_dict(log_retention_resp_model_json).__dict__
        log_retention_resp_model2 = LogRetentionResp(**log_retention_resp_model_dict)

        # Verify the model instances are equivalent
        assert log_retention_resp_model == log_retention_resp_model2

        # Convert model instance back to dict and verify no loss of data
        log_retention_resp_model_json2 = log_retention_resp_model.to_dict()
        assert log_retention_resp_model_json2 == log_retention_resp_model_json


class TestModel_MaxUploadResp:
    """
    Test Class for MaxUploadResp
    """

    def test_max_upload_resp_serialization(self):
        """
        Test serialization/deserialization for MaxUploadResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        max_upload_resp_result_model = {}  # MaxUploadRespResult
        max_upload_resp_result_model['id'] = 'max_upload'
        max_upload_resp_result_model['value'] = 300
        max_upload_resp_result_model['editable'] = True
        max_upload_resp_result_model['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a json representation of a MaxUploadResp model
        max_upload_resp_model_json = {}
        max_upload_resp_model_json['result'] = max_upload_resp_result_model
        max_upload_resp_model_json['success'] = True
        max_upload_resp_model_json['errors'] = [['testString']]
        max_upload_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of MaxUploadResp by calling from_dict on the json representation
        max_upload_resp_model = MaxUploadResp.from_dict(max_upload_resp_model_json)
        assert max_upload_resp_model != False

        # Construct a model instance of MaxUploadResp by calling from_dict on the json representation
        max_upload_resp_model_dict = MaxUploadResp.from_dict(max_upload_resp_model_json).__dict__
        max_upload_resp_model2 = MaxUploadResp(**max_upload_resp_model_dict)

        # Verify the model instances are equivalent
        assert max_upload_resp_model == max_upload_resp_model2

        # Convert model instance back to dict and verify no loss of data
        max_upload_resp_model_json2 = max_upload_resp_model.to_dict()
        assert max_upload_resp_model_json2 == max_upload_resp_model_json


class TestModel_MinTlsVersionResp:
    """
    Test Class for MinTlsVersionResp
    """

    def test_min_tls_version_resp_serialization(self):
        """
        Test serialization/deserialization for MinTlsVersionResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        min_tls_version_resp_result_model = {}  # MinTlsVersionRespResult
        min_tls_version_resp_result_model['id'] = 'min_tls_version'
        min_tls_version_resp_result_model['value'] = '1.2'
        min_tls_version_resp_result_model['editable'] = True
        min_tls_version_resp_result_model['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a json representation of a MinTlsVersionResp model
        min_tls_version_resp_model_json = {}
        min_tls_version_resp_model_json['result'] = min_tls_version_resp_result_model
        min_tls_version_resp_model_json['success'] = True
        min_tls_version_resp_model_json['errors'] = [['testString']]
        min_tls_version_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of MinTlsVersionResp by calling from_dict on the json representation
        min_tls_version_resp_model = MinTlsVersionResp.from_dict(min_tls_version_resp_model_json)
        assert min_tls_version_resp_model != False

        # Construct a model instance of MinTlsVersionResp by calling from_dict on the json representation
        min_tls_version_resp_model_dict = MinTlsVersionResp.from_dict(min_tls_version_resp_model_json).__dict__
        min_tls_version_resp_model2 = MinTlsVersionResp(**min_tls_version_resp_model_dict)

        # Verify the model instances are equivalent
        assert min_tls_version_resp_model == min_tls_version_resp_model2

        # Convert model instance back to dict and verify no loss of data
        min_tls_version_resp_model_json2 = min_tls_version_resp_model.to_dict()
        assert min_tls_version_resp_model_json2 == min_tls_version_resp_model_json


class TestModel_MinifyResp:
    """
    Test Class for MinifyResp
    """

    def test_minify_resp_serialization(self):
        """
        Test serialization/deserialization for MinifyResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        minify_resp_result_value_model = {}  # MinifyRespResultValue
        minify_resp_result_value_model['css'] = 'on'
        minify_resp_result_value_model['html'] = 'on'
        minify_resp_result_value_model['js'] = 'on'

        minify_resp_result_model = {}  # MinifyRespResult
        minify_resp_result_model['id'] = 'minify'
        minify_resp_result_model['value'] = minify_resp_result_value_model
        minify_resp_result_model['editable'] = True
        minify_resp_result_model['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a json representation of a MinifyResp model
        minify_resp_model_json = {}
        minify_resp_model_json['result'] = minify_resp_result_model
        minify_resp_model_json['success'] = True
        minify_resp_model_json['errors'] = [['testString']]
        minify_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of MinifyResp by calling from_dict on the json representation
        minify_resp_model = MinifyResp.from_dict(minify_resp_model_json)
        assert minify_resp_model != False

        # Construct a model instance of MinifyResp by calling from_dict on the json representation
        minify_resp_model_dict = MinifyResp.from_dict(minify_resp_model_json).__dict__
        minify_resp_model2 = MinifyResp(**minify_resp_model_dict)

        # Verify the model instances are equivalent
        assert minify_resp_model == minify_resp_model2

        # Convert model instance back to dict and verify no loss of data
        minify_resp_model_json2 = minify_resp_model.to_dict()
        assert minify_resp_model_json2 == minify_resp_model_json


class TestModel_MobileRedirectResp:
    """
    Test Class for MobileRedirectResp
    """

    def test_mobile_redirect_resp_serialization(self):
        """
        Test serialization/deserialization for MobileRedirectResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        mobile_redirect_resp_result_value_model = {}  # MobileRedirectRespResultValue
        mobile_redirect_resp_result_value_model['status'] = 'on'
        mobile_redirect_resp_result_value_model['mobile_subdomain'] = 'm'
        mobile_redirect_resp_result_value_model['strip_uri'] = False

        mobile_redirect_resp_result_model = {}  # MobileRedirectRespResult
        mobile_redirect_resp_result_model['id'] = 'mobile_redirect'
        mobile_redirect_resp_result_model['value'] = mobile_redirect_resp_result_value_model
        mobile_redirect_resp_result_model['editable'] = True
        mobile_redirect_resp_result_model['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a json representation of a MobileRedirectResp model
        mobile_redirect_resp_model_json = {}
        mobile_redirect_resp_model_json['result'] = mobile_redirect_resp_result_model
        mobile_redirect_resp_model_json['success'] = True
        mobile_redirect_resp_model_json['errors'] = [['testString']]
        mobile_redirect_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of MobileRedirectResp by calling from_dict on the json representation
        mobile_redirect_resp_model = MobileRedirectResp.from_dict(mobile_redirect_resp_model_json)
        assert mobile_redirect_resp_model != False

        # Construct a model instance of MobileRedirectResp by calling from_dict on the json representation
        mobile_redirect_resp_model_dict = MobileRedirectResp.from_dict(mobile_redirect_resp_model_json).__dict__
        mobile_redirect_resp_model2 = MobileRedirectResp(**mobile_redirect_resp_model_dict)

        # Verify the model instances are equivalent
        assert mobile_redirect_resp_model == mobile_redirect_resp_model2

        # Convert model instance back to dict and verify no loss of data
        mobile_redirect_resp_model_json2 = mobile_redirect_resp_model.to_dict()
        assert mobile_redirect_resp_model_json2 == mobile_redirect_resp_model_json


class TestModel_OpportunisticEncryptionResp:
    """
    Test Class for OpportunisticEncryptionResp
    """

    def test_opportunistic_encryption_resp_serialization(self):
        """
        Test serialization/deserialization for OpportunisticEncryptionResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        opportunistic_encryption_resp_result_model = {}  # OpportunisticEncryptionRespResult
        opportunistic_encryption_resp_result_model['id'] = 'opportunistic_encryption'
        opportunistic_encryption_resp_result_model['value'] = 'off'
        opportunistic_encryption_resp_result_model['editable'] = True
        opportunistic_encryption_resp_result_model['modified_on'] = '2017-01-01T05:20:00.123000Z'

        # Construct a json representation of a OpportunisticEncryptionResp model
        opportunistic_encryption_resp_model_json = {}
        opportunistic_encryption_resp_model_json['result'] = opportunistic_encryption_resp_result_model
        opportunistic_encryption_resp_model_json['success'] = True
        opportunistic_encryption_resp_model_json['errors'] = [['testString']]
        opportunistic_encryption_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of OpportunisticEncryptionResp by calling from_dict on the json representation
        opportunistic_encryption_resp_model = OpportunisticEncryptionResp.from_dict(opportunistic_encryption_resp_model_json)
        assert opportunistic_encryption_resp_model != False

        # Construct a model instance of OpportunisticEncryptionResp by calling from_dict on the json representation
        opportunistic_encryption_resp_model_dict = OpportunisticEncryptionResp.from_dict(opportunistic_encryption_resp_model_json).__dict__
        opportunistic_encryption_resp_model2 = OpportunisticEncryptionResp(**opportunistic_encryption_resp_model_dict)

        # Verify the model instances are equivalent
        assert opportunistic_encryption_resp_model == opportunistic_encryption_resp_model2

        # Convert model instance back to dict and verify no loss of data
        opportunistic_encryption_resp_model_json2 = opportunistic_encryption_resp_model.to_dict()
        assert opportunistic_encryption_resp_model_json2 == opportunistic_encryption_resp_model_json


class TestModel_OpportunisticOnionResp:
    """
    Test Class for OpportunisticOnionResp
    """

    def test_opportunistic_onion_resp_serialization(self):
        """
        Test serialization/deserialization for OpportunisticOnionResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        opportunistic_onion_resp_result_model = {}  # OpportunisticOnionRespResult
        opportunistic_onion_resp_result_model['id'] = 'opportunistic_onion'
        opportunistic_onion_resp_result_model['value'] = 'off'
        opportunistic_onion_resp_result_model['editable'] = True
        opportunistic_onion_resp_result_model['modified_on'] = '2017-01-01T05:20:00.123000Z'

        # Construct a json representation of a OpportunisticOnionResp model
        opportunistic_onion_resp_model_json = {}
        opportunistic_onion_resp_model_json['result'] = opportunistic_onion_resp_result_model
        opportunistic_onion_resp_model_json['success'] = True
        opportunistic_onion_resp_model_json['errors'] = [['testString']]
        opportunistic_onion_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of OpportunisticOnionResp by calling from_dict on the json representation
        opportunistic_onion_resp_model = OpportunisticOnionResp.from_dict(opportunistic_onion_resp_model_json)
        assert opportunistic_onion_resp_model != False

        # Construct a model instance of OpportunisticOnionResp by calling from_dict on the json representation
        opportunistic_onion_resp_model_dict = OpportunisticOnionResp.from_dict(opportunistic_onion_resp_model_json).__dict__
        opportunistic_onion_resp_model2 = OpportunisticOnionResp(**opportunistic_onion_resp_model_dict)

        # Verify the model instances are equivalent
        assert opportunistic_onion_resp_model == opportunistic_onion_resp_model2

        # Convert model instance back to dict and verify no loss of data
        opportunistic_onion_resp_model_json2 = opportunistic_onion_resp_model.to_dict()
        assert opportunistic_onion_resp_model_json2 == opportunistic_onion_resp_model_json


class TestModel_OriginErrorPagePassThruResp:
    """
    Test Class for OriginErrorPagePassThruResp
    """

    def test_origin_error_page_pass_thru_resp_serialization(self):
        """
        Test serialization/deserialization for OriginErrorPagePassThruResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        origin_error_page_pass_thru_resp_result_model = {}  # OriginErrorPagePassThruRespResult
        origin_error_page_pass_thru_resp_result_model['id'] = 'origin_error_page_pass_thru'
        origin_error_page_pass_thru_resp_result_model['value'] = 'off'
        origin_error_page_pass_thru_resp_result_model['editable'] = True
        origin_error_page_pass_thru_resp_result_model['modified_on'] = '2018-12-08T18:57:52.826000Z'

        # Construct a json representation of a OriginErrorPagePassThruResp model
        origin_error_page_pass_thru_resp_model_json = {}
        origin_error_page_pass_thru_resp_model_json['result'] = origin_error_page_pass_thru_resp_result_model
        origin_error_page_pass_thru_resp_model_json['success'] = True
        origin_error_page_pass_thru_resp_model_json['errors'] = [['testString']]
        origin_error_page_pass_thru_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of OriginErrorPagePassThruResp by calling from_dict on the json representation
        origin_error_page_pass_thru_resp_model = OriginErrorPagePassThruResp.from_dict(origin_error_page_pass_thru_resp_model_json)
        assert origin_error_page_pass_thru_resp_model != False

        # Construct a model instance of OriginErrorPagePassThruResp by calling from_dict on the json representation
        origin_error_page_pass_thru_resp_model_dict = OriginErrorPagePassThruResp.from_dict(origin_error_page_pass_thru_resp_model_json).__dict__
        origin_error_page_pass_thru_resp_model2 = OriginErrorPagePassThruResp(**origin_error_page_pass_thru_resp_model_dict)

        # Verify the model instances are equivalent
        assert origin_error_page_pass_thru_resp_model == origin_error_page_pass_thru_resp_model2

        # Convert model instance back to dict and verify no loss of data
        origin_error_page_pass_thru_resp_model_json2 = origin_error_page_pass_thru_resp_model.to_dict()
        assert origin_error_page_pass_thru_resp_model_json2 == origin_error_page_pass_thru_resp_model_json


class TestModel_OriginMaxHttpVersionResp:
    """
    Test Class for OriginMaxHttpVersionResp
    """

    def test_origin_max_http_version_resp_serialization(self):
        """
        Test serialization/deserialization for OriginMaxHttpVersionResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        origin_max_http_version_resp_result_model = {}  # OriginMaxHttpVersionRespResult
        origin_max_http_version_resp_result_model['id'] = 'origin_max_http_version'
        origin_max_http_version_resp_result_model['value'] = '1'
        origin_max_http_version_resp_result_model['editable'] = True
        origin_max_http_version_resp_result_model['modified_on'] = '2023-09-14T09:49:19.524000Z'

        # Construct a json representation of a OriginMaxHttpVersionResp model
        origin_max_http_version_resp_model_json = {}
        origin_max_http_version_resp_model_json['result'] = origin_max_http_version_resp_result_model
        origin_max_http_version_resp_model_json['success'] = True
        origin_max_http_version_resp_model_json['errors'] = [['testString']]
        origin_max_http_version_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of OriginMaxHttpVersionResp by calling from_dict on the json representation
        origin_max_http_version_resp_model = OriginMaxHttpVersionResp.from_dict(origin_max_http_version_resp_model_json)
        assert origin_max_http_version_resp_model != False

        # Construct a model instance of OriginMaxHttpVersionResp by calling from_dict on the json representation
        origin_max_http_version_resp_model_dict = OriginMaxHttpVersionResp.from_dict(origin_max_http_version_resp_model_json).__dict__
        origin_max_http_version_resp_model2 = OriginMaxHttpVersionResp(**origin_max_http_version_resp_model_dict)

        # Verify the model instances are equivalent
        assert origin_max_http_version_resp_model == origin_max_http_version_resp_model2

        # Convert model instance back to dict and verify no loss of data
        origin_max_http_version_resp_model_json2 = origin_max_http_version_resp_model.to_dict()
        assert origin_max_http_version_resp_model_json2 == origin_max_http_version_resp_model_json


class TestModel_OriginPostQuantumEncryptionResp:
    """
    Test Class for OriginPostQuantumEncryptionResp
    """

    def test_origin_post_quantum_encryption_resp_serialization(self):
        """
        Test serialization/deserialization for OriginPostQuantumEncryptionResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        origin_post_quantum_encryption_resp_result_model = {}  # OriginPostQuantumEncryptionRespResult
        origin_post_quantum_encryption_resp_result_model['id'] = 'origin_pqe'
        origin_post_quantum_encryption_resp_result_model['value'] = 'off'
        origin_post_quantum_encryption_resp_result_model['editable'] = True
        origin_post_quantum_encryption_resp_result_model['modified_on'] = '2023-09-14T09:49:19.524000Z'

        # Construct a json representation of a OriginPostQuantumEncryptionResp model
        origin_post_quantum_encryption_resp_model_json = {}
        origin_post_quantum_encryption_resp_model_json['result'] = origin_post_quantum_encryption_resp_result_model
        origin_post_quantum_encryption_resp_model_json['success'] = True
        origin_post_quantum_encryption_resp_model_json['errors'] = [['testString']]
        origin_post_quantum_encryption_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of OriginPostQuantumEncryptionResp by calling from_dict on the json representation
        origin_post_quantum_encryption_resp_model = OriginPostQuantumEncryptionResp.from_dict(origin_post_quantum_encryption_resp_model_json)
        assert origin_post_quantum_encryption_resp_model != False

        # Construct a model instance of OriginPostQuantumEncryptionResp by calling from_dict on the json representation
        origin_post_quantum_encryption_resp_model_dict = OriginPostQuantumEncryptionResp.from_dict(origin_post_quantum_encryption_resp_model_json).__dict__
        origin_post_quantum_encryption_resp_model2 = OriginPostQuantumEncryptionResp(**origin_post_quantum_encryption_resp_model_dict)

        # Verify the model instances are equivalent
        assert origin_post_quantum_encryption_resp_model == origin_post_quantum_encryption_resp_model2

        # Convert model instance back to dict and verify no loss of data
        origin_post_quantum_encryption_resp_model_json2 = origin_post_quantum_encryption_resp_model.to_dict()
        assert origin_post_quantum_encryption_resp_model_json2 == origin_post_quantum_encryption_resp_model_json


class TestModel_PrefetchPreloadResp:
    """
    Test Class for PrefetchPreloadResp
    """

    def test_prefetch_preload_resp_serialization(self):
        """
        Test serialization/deserialization for PrefetchPreloadResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        prefetch_preload_resp_result_model = {}  # PrefetchPreloadRespResult
        prefetch_preload_resp_result_model['id'] = 'prefetch_preload'
        prefetch_preload_resp_result_model['value'] = 'off'
        prefetch_preload_resp_result_model['editable'] = True
        prefetch_preload_resp_result_model['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a json representation of a PrefetchPreloadResp model
        prefetch_preload_resp_model_json = {}
        prefetch_preload_resp_model_json['result'] = prefetch_preload_resp_result_model
        prefetch_preload_resp_model_json['success'] = True
        prefetch_preload_resp_model_json['errors'] = [['testString']]
        prefetch_preload_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of PrefetchPreloadResp by calling from_dict on the json representation
        prefetch_preload_resp_model = PrefetchPreloadResp.from_dict(prefetch_preload_resp_model_json)
        assert prefetch_preload_resp_model != False

        # Construct a model instance of PrefetchPreloadResp by calling from_dict on the json representation
        prefetch_preload_resp_model_dict = PrefetchPreloadResp.from_dict(prefetch_preload_resp_model_json).__dict__
        prefetch_preload_resp_model2 = PrefetchPreloadResp(**prefetch_preload_resp_model_dict)

        # Verify the model instances are equivalent
        assert prefetch_preload_resp_model == prefetch_preload_resp_model2

        # Convert model instance back to dict and verify no loss of data
        prefetch_preload_resp_model_json2 = prefetch_preload_resp_model.to_dict()
        assert prefetch_preload_resp_model_json2 == prefetch_preload_resp_model_json


class TestModel_ProxyReadTimeoutResp:
    """
    Test Class for ProxyReadTimeoutResp
    """

    def test_proxy_read_timeout_resp_serialization(self):
        """
        Test serialization/deserialization for ProxyReadTimeoutResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        proxy_read_timeout_resp_result_model = {}  # ProxyReadTimeoutRespResult
        proxy_read_timeout_resp_result_model['id'] = 'proxy_read_timeout'
        proxy_read_timeout_resp_result_model['value'] = 100
        proxy_read_timeout_resp_result_model['editable'] = True
        proxy_read_timeout_resp_result_model['modified_on'] = '2018-12-08T18:57:52.826000Z'

        # Construct a json representation of a ProxyReadTimeoutResp model
        proxy_read_timeout_resp_model_json = {}
        proxy_read_timeout_resp_model_json['result'] = proxy_read_timeout_resp_result_model
        proxy_read_timeout_resp_model_json['success'] = True
        proxy_read_timeout_resp_model_json['errors'] = [['testString']]
        proxy_read_timeout_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of ProxyReadTimeoutResp by calling from_dict on the json representation
        proxy_read_timeout_resp_model = ProxyReadTimeoutResp.from_dict(proxy_read_timeout_resp_model_json)
        assert proxy_read_timeout_resp_model != False

        # Construct a model instance of ProxyReadTimeoutResp by calling from_dict on the json representation
        proxy_read_timeout_resp_model_dict = ProxyReadTimeoutResp.from_dict(proxy_read_timeout_resp_model_json).__dict__
        proxy_read_timeout_resp_model2 = ProxyReadTimeoutResp(**proxy_read_timeout_resp_model_dict)

        # Verify the model instances are equivalent
        assert proxy_read_timeout_resp_model == proxy_read_timeout_resp_model2

        # Convert model instance back to dict and verify no loss of data
        proxy_read_timeout_resp_model_json2 = proxy_read_timeout_resp_model.to_dict()
        assert proxy_read_timeout_resp_model_json2 == proxy_read_timeout_resp_model_json


class TestModel_PseudoIpv4Resp:
    """
    Test Class for PseudoIpv4Resp
    """

    def test_pseudo_ipv4_resp_serialization(self):
        """
        Test serialization/deserialization for PseudoIpv4Resp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        pseudo_ipv4_resp_result_model = {}  # PseudoIpv4RespResult
        pseudo_ipv4_resp_result_model['id'] = 'pseudo_ipv4'
        pseudo_ipv4_resp_result_model['value'] = 'add_header'
        pseudo_ipv4_resp_result_model['editable'] = True
        pseudo_ipv4_resp_result_model['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a json representation of a PseudoIpv4Resp model
        pseudo_ipv4_resp_model_json = {}
        pseudo_ipv4_resp_model_json['result'] = pseudo_ipv4_resp_result_model
        pseudo_ipv4_resp_model_json['success'] = True
        pseudo_ipv4_resp_model_json['errors'] = [['testString']]
        pseudo_ipv4_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of PseudoIpv4Resp by calling from_dict on the json representation
        pseudo_ipv4_resp_model = PseudoIpv4Resp.from_dict(pseudo_ipv4_resp_model_json)
        assert pseudo_ipv4_resp_model != False

        # Construct a model instance of PseudoIpv4Resp by calling from_dict on the json representation
        pseudo_ipv4_resp_model_dict = PseudoIpv4Resp.from_dict(pseudo_ipv4_resp_model_json).__dict__
        pseudo_ipv4_resp_model2 = PseudoIpv4Resp(**pseudo_ipv4_resp_model_dict)

        # Verify the model instances are equivalent
        assert pseudo_ipv4_resp_model == pseudo_ipv4_resp_model2

        # Convert model instance back to dict and verify no loss of data
        pseudo_ipv4_resp_model_json2 = pseudo_ipv4_resp_model.to_dict()
        assert pseudo_ipv4_resp_model_json2 == pseudo_ipv4_resp_model_json


class TestModel_ReplaceInsecureJsResp:
    """
    Test Class for ReplaceInsecureJsResp
    """

    def test_replace_insecure_js_resp_serialization(self):
        """
        Test serialization/deserialization for ReplaceInsecureJsResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        replace_insecure_js_resp_result_model = {}  # ReplaceInsecureJsRespResult
        replace_insecure_js_resp_result_model['id'] = 'replace_insecure_js'
        replace_insecure_js_resp_result_model['value'] = 'off'
        replace_insecure_js_resp_result_model['editable'] = True
        replace_insecure_js_resp_result_model['modified_on'] = '2017-01-01T05:20:00.123000Z'

        # Construct a json representation of a ReplaceInsecureJsResp model
        replace_insecure_js_resp_model_json = {}
        replace_insecure_js_resp_model_json['result'] = replace_insecure_js_resp_result_model
        replace_insecure_js_resp_model_json['success'] = True
        replace_insecure_js_resp_model_json['errors'] = [['testString']]
        replace_insecure_js_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of ReplaceInsecureJsResp by calling from_dict on the json representation
        replace_insecure_js_resp_model = ReplaceInsecureJsResp.from_dict(replace_insecure_js_resp_model_json)
        assert replace_insecure_js_resp_model != False

        # Construct a model instance of ReplaceInsecureJsResp by calling from_dict on the json representation
        replace_insecure_js_resp_model_dict = ReplaceInsecureJsResp.from_dict(replace_insecure_js_resp_model_json).__dict__
        replace_insecure_js_resp_model2 = ReplaceInsecureJsResp(**replace_insecure_js_resp_model_dict)

        # Verify the model instances are equivalent
        assert replace_insecure_js_resp_model == replace_insecure_js_resp_model2

        # Convert model instance back to dict and verify no loss of data
        replace_insecure_js_resp_model_json2 = replace_insecure_js_resp_model.to_dict()
        assert replace_insecure_js_resp_model_json2 == replace_insecure_js_resp_model_json


class TestModel_ResponseBufferingResp:
    """
    Test Class for ResponseBufferingResp
    """

    def test_response_buffering_resp_serialization(self):
        """
        Test serialization/deserialization for ResponseBufferingResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_buffering_resp_result_model = {}  # ResponseBufferingRespResult
        response_buffering_resp_result_model['id'] = 'response_buffering'
        response_buffering_resp_result_model['value'] = 'off'
        response_buffering_resp_result_model['editable'] = True
        response_buffering_resp_result_model['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a json representation of a ResponseBufferingResp model
        response_buffering_resp_model_json = {}
        response_buffering_resp_model_json['result'] = response_buffering_resp_result_model
        response_buffering_resp_model_json['success'] = True
        response_buffering_resp_model_json['errors'] = [['testString']]
        response_buffering_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of ResponseBufferingResp by calling from_dict on the json representation
        response_buffering_resp_model = ResponseBufferingResp.from_dict(response_buffering_resp_model_json)
        assert response_buffering_resp_model != False

        # Construct a model instance of ResponseBufferingResp by calling from_dict on the json representation
        response_buffering_resp_model_dict = ResponseBufferingResp.from_dict(response_buffering_resp_model_json).__dict__
        response_buffering_resp_model2 = ResponseBufferingResp(**response_buffering_resp_model_dict)

        # Verify the model instances are equivalent
        assert response_buffering_resp_model == response_buffering_resp_model2

        # Convert model instance back to dict and verify no loss of data
        response_buffering_resp_model_json2 = response_buffering_resp_model.to_dict()
        assert response_buffering_resp_model_json2 == response_buffering_resp_model_json


class TestModel_ScriptLoadOptimizationResp:
    """
    Test Class for ScriptLoadOptimizationResp
    """

    def test_script_load_optimization_resp_serialization(self):
        """
        Test serialization/deserialization for ScriptLoadOptimizationResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        script_load_optimization_resp_result_model = {}  # ScriptLoadOptimizationRespResult
        script_load_optimization_resp_result_model['id'] = 'script_load_optimization'
        script_load_optimization_resp_result_model['value'] = 'off'
        script_load_optimization_resp_result_model['editable'] = True
        script_load_optimization_resp_result_model['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a json representation of a ScriptLoadOptimizationResp model
        script_load_optimization_resp_model_json = {}
        script_load_optimization_resp_model_json['result'] = script_load_optimization_resp_result_model
        script_load_optimization_resp_model_json['success'] = True
        script_load_optimization_resp_model_json['errors'] = [['testString']]
        script_load_optimization_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of ScriptLoadOptimizationResp by calling from_dict on the json representation
        script_load_optimization_resp_model = ScriptLoadOptimizationResp.from_dict(script_load_optimization_resp_model_json)
        assert script_load_optimization_resp_model != False

        # Construct a model instance of ScriptLoadOptimizationResp by calling from_dict on the json representation
        script_load_optimization_resp_model_dict = ScriptLoadOptimizationResp.from_dict(script_load_optimization_resp_model_json).__dict__
        script_load_optimization_resp_model2 = ScriptLoadOptimizationResp(**script_load_optimization_resp_model_dict)

        # Verify the model instances are equivalent
        assert script_load_optimization_resp_model == script_load_optimization_resp_model2

        # Convert model instance back to dict and verify no loss of data
        script_load_optimization_resp_model_json2 = script_load_optimization_resp_model.to_dict()
        assert script_load_optimization_resp_model_json2 == script_load_optimization_resp_model_json


class TestModel_SecurityHeaderResp:
    """
    Test Class for SecurityHeaderResp
    """

    def test_security_header_resp_serialization(self):
        """
        Test serialization/deserialization for SecurityHeaderResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        security_header_resp_result_value_strict_transport_security_model = {}  # SecurityHeaderRespResultValueStrictTransportSecurity
        security_header_resp_result_value_strict_transport_security_model['enabled'] = True
        security_header_resp_result_value_strict_transport_security_model['max_age'] = 86400
        security_header_resp_result_value_strict_transport_security_model['include_subdomains'] = True
        security_header_resp_result_value_strict_transport_security_model['preload'] = True
        security_header_resp_result_value_strict_transport_security_model['nosniff'] = True

        security_header_resp_result_value_model = {}  # SecurityHeaderRespResultValue
        security_header_resp_result_value_model['strict_transport_security'] = security_header_resp_result_value_strict_transport_security_model

        security_header_resp_result_model = {}  # SecurityHeaderRespResult
        security_header_resp_result_model['id'] = 'security_header'
        security_header_resp_result_model['value'] = security_header_resp_result_value_model
        security_header_resp_result_model['editable'] = True
        security_header_resp_result_model['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a json representation of a SecurityHeaderResp model
        security_header_resp_model_json = {}
        security_header_resp_model_json['result'] = security_header_resp_result_model
        security_header_resp_model_json['success'] = True
        security_header_resp_model_json['errors'] = [['testString']]
        security_header_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of SecurityHeaderResp by calling from_dict on the json representation
        security_header_resp_model = SecurityHeaderResp.from_dict(security_header_resp_model_json)
        assert security_header_resp_model != False

        # Construct a model instance of SecurityHeaderResp by calling from_dict on the json representation
        security_header_resp_model_dict = SecurityHeaderResp.from_dict(security_header_resp_model_json).__dict__
        security_header_resp_model2 = SecurityHeaderResp(**security_header_resp_model_dict)

        # Verify the model instances are equivalent
        assert security_header_resp_model == security_header_resp_model2

        # Convert model instance back to dict and verify no loss of data
        security_header_resp_model_json2 = security_header_resp_model.to_dict()
        assert security_header_resp_model_json2 == security_header_resp_model_json


class TestModel_ServerSideExcludeResp:
    """
    Test Class for ServerSideExcludeResp
    """

    def test_server_side_exclude_resp_serialization(self):
        """
        Test serialization/deserialization for ServerSideExcludeResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        server_side_exclude_resp_result_model = {}  # ServerSideExcludeRespResult
        server_side_exclude_resp_result_model['id'] = 'server_side_exclude'
        server_side_exclude_resp_result_model['value'] = 'off'
        server_side_exclude_resp_result_model['editable'] = True
        server_side_exclude_resp_result_model['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a json representation of a ServerSideExcludeResp model
        server_side_exclude_resp_model_json = {}
        server_side_exclude_resp_model_json['result'] = server_side_exclude_resp_result_model
        server_side_exclude_resp_model_json['success'] = True
        server_side_exclude_resp_model_json['errors'] = [['testString']]
        server_side_exclude_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of ServerSideExcludeResp by calling from_dict on the json representation
        server_side_exclude_resp_model = ServerSideExcludeResp.from_dict(server_side_exclude_resp_model_json)
        assert server_side_exclude_resp_model != False

        # Construct a model instance of ServerSideExcludeResp by calling from_dict on the json representation
        server_side_exclude_resp_model_dict = ServerSideExcludeResp.from_dict(server_side_exclude_resp_model_json).__dict__
        server_side_exclude_resp_model2 = ServerSideExcludeResp(**server_side_exclude_resp_model_dict)

        # Verify the model instances are equivalent
        assert server_side_exclude_resp_model == server_side_exclude_resp_model2

        # Convert model instance back to dict and verify no loss of data
        server_side_exclude_resp_model_json2 = server_side_exclude_resp_model.to_dict()
        assert server_side_exclude_resp_model_json2 == server_side_exclude_resp_model_json


class TestModel_TlsClientAuthResp:
    """
    Test Class for TlsClientAuthResp
    """

    def test_tls_client_auth_resp_serialization(self):
        """
        Test serialization/deserialization for TlsClientAuthResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        tls_client_auth_resp_result_model = {}  # TlsClientAuthRespResult
        tls_client_auth_resp_result_model['id'] = 'tls_client_auth'
        tls_client_auth_resp_result_model['value'] = 'off'
        tls_client_auth_resp_result_model['editable'] = True
        tls_client_auth_resp_result_model['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a json representation of a TlsClientAuthResp model
        tls_client_auth_resp_model_json = {}
        tls_client_auth_resp_model_json['result'] = tls_client_auth_resp_result_model
        tls_client_auth_resp_model_json['success'] = True
        tls_client_auth_resp_model_json['errors'] = [['testString']]
        tls_client_auth_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of TlsClientAuthResp by calling from_dict on the json representation
        tls_client_auth_resp_model = TlsClientAuthResp.from_dict(tls_client_auth_resp_model_json)
        assert tls_client_auth_resp_model != False

        # Construct a model instance of TlsClientAuthResp by calling from_dict on the json representation
        tls_client_auth_resp_model_dict = TlsClientAuthResp.from_dict(tls_client_auth_resp_model_json).__dict__
        tls_client_auth_resp_model2 = TlsClientAuthResp(**tls_client_auth_resp_model_dict)

        # Verify the model instances are equivalent
        assert tls_client_auth_resp_model == tls_client_auth_resp_model2

        # Convert model instance back to dict and verify no loss of data
        tls_client_auth_resp_model_json2 = tls_client_auth_resp_model.to_dict()
        assert tls_client_auth_resp_model_json2 == tls_client_auth_resp_model_json


class TestModel_TrueClientIpResp:
    """
    Test Class for TrueClientIpResp
    """

    def test_true_client_ip_resp_serialization(self):
        """
        Test serialization/deserialization for TrueClientIpResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        true_client_ip_resp_result_model = {}  # TrueClientIpRespResult
        true_client_ip_resp_result_model['id'] = 'true_client_ip_header'
        true_client_ip_resp_result_model['value'] = 'off'
        true_client_ip_resp_result_model['editable'] = True
        true_client_ip_resp_result_model['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a json representation of a TrueClientIpResp model
        true_client_ip_resp_model_json = {}
        true_client_ip_resp_model_json['result'] = true_client_ip_resp_result_model
        true_client_ip_resp_model_json['success'] = True
        true_client_ip_resp_model_json['errors'] = [['testString']]
        true_client_ip_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of TrueClientIpResp by calling from_dict on the json representation
        true_client_ip_resp_model = TrueClientIpResp.from_dict(true_client_ip_resp_model_json)
        assert true_client_ip_resp_model != False

        # Construct a model instance of TrueClientIpResp by calling from_dict on the json representation
        true_client_ip_resp_model_dict = TrueClientIpResp.from_dict(true_client_ip_resp_model_json).__dict__
        true_client_ip_resp_model2 = TrueClientIpResp(**true_client_ip_resp_model_dict)

        # Verify the model instances are equivalent
        assert true_client_ip_resp_model == true_client_ip_resp_model2

        # Convert model instance back to dict and verify no loss of data
        true_client_ip_resp_model_json2 = true_client_ip_resp_model.to_dict()
        assert true_client_ip_resp_model_json2 == true_client_ip_resp_model_json


class TestModel_WafResp:
    """
    Test Class for WafResp
    """

    def test_waf_resp_serialization(self):
        """
        Test serialization/deserialization for WafResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        waf_resp_result_model = {}  # WafRespResult
        waf_resp_result_model['id'] = 'waf'
        waf_resp_result_model['value'] = 'off'
        waf_resp_result_model['editable'] = True
        waf_resp_result_model['modified_on'] = '2018-12-08T18:57:43.889000Z'

        # Construct a json representation of a WafResp model
        waf_resp_model_json = {}
        waf_resp_model_json['result'] = waf_resp_result_model
        waf_resp_model_json['success'] = True
        waf_resp_model_json['errors'] = [['testString']]
        waf_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of WafResp by calling from_dict on the json representation
        waf_resp_model = WafResp.from_dict(waf_resp_model_json)
        assert waf_resp_model != False

        # Construct a model instance of WafResp by calling from_dict on the json representation
        waf_resp_model_dict = WafResp.from_dict(waf_resp_model_json).__dict__
        waf_resp_model2 = WafResp(**waf_resp_model_dict)

        # Verify the model instances are equivalent
        assert waf_resp_model == waf_resp_model2

        # Convert model instance back to dict and verify no loss of data
        waf_resp_model_json2 = waf_resp_model.to_dict()
        assert waf_resp_model_json2 == waf_resp_model_json


class TestModel_WebsocketsResp:
    """
    Test Class for WebsocketsResp
    """

    def test_websockets_resp_serialization(self):
        """
        Test serialization/deserialization for WebsocketsResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        websockets_resp_result_model = {}  # WebsocketsRespResult
        websockets_resp_result_model['id'] = 'websockets'
        websockets_resp_result_model['value'] = 'off'
        websockets_resp_result_model['editable'] = True
        websockets_resp_result_model['modified_on'] = '2018-09-14T09:49:19.524000Z'

        # Construct a json representation of a WebsocketsResp model
        websockets_resp_model_json = {}
        websockets_resp_model_json['result'] = websockets_resp_result_model
        websockets_resp_model_json['success'] = True
        websockets_resp_model_json['errors'] = [['testString']]
        websockets_resp_model_json['messages'] = [['testString']]

        # Construct a model instance of WebsocketsResp by calling from_dict on the json representation
        websockets_resp_model = WebsocketsResp.from_dict(websockets_resp_model_json)
        assert websockets_resp_model != False

        # Construct a model instance of WebsocketsResp by calling from_dict on the json representation
        websockets_resp_model_dict = WebsocketsResp.from_dict(websockets_resp_model_json).__dict__
        websockets_resp_model2 = WebsocketsResp(**websockets_resp_model_dict)

        # Verify the model instances are equivalent
        assert websockets_resp_model == websockets_resp_model2

        # Convert model instance back to dict and verify no loss of data
        websockets_resp_model_json2 = websockets_resp_model.to_dict()
        assert websockets_resp_model_json2 == websockets_resp_model_json


class TestModel_ZonesCnameFlatteningResp:
    """
    Test Class for ZonesCnameFlatteningResp
    """

    def test_zones_cname_flattening_resp_serialization(self):
        """
        Test serialization/deserialization for ZonesCnameFlatteningResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        cname_flattening_response_model = {}  # CnameFlatteningResponse
        cname_flattening_response_model['id'] = 'cname_flattening'
        cname_flattening_response_model['value'] = 'flatten_all'
        cname_flattening_response_model['modified_on'] = '2014-01-01T05:20:00.123000Z'
        cname_flattening_response_model['editable'] = True

        # Construct a json representation of a ZonesCnameFlatteningResp model
        zones_cname_flattening_resp_model_json = {}
        zones_cname_flattening_resp_model_json['success'] = True
        zones_cname_flattening_resp_model_json['errors'] = [['testString']]
        zones_cname_flattening_resp_model_json['messages'] = [['testString']]
        zones_cname_flattening_resp_model_json['result'] = cname_flattening_response_model

        # Construct a model instance of ZonesCnameFlatteningResp by calling from_dict on the json representation
        zones_cname_flattening_resp_model = ZonesCnameFlatteningResp.from_dict(zones_cname_flattening_resp_model_json)
        assert zones_cname_flattening_resp_model != False

        # Construct a model instance of ZonesCnameFlatteningResp by calling from_dict on the json representation
        zones_cname_flattening_resp_model_dict = ZonesCnameFlatteningResp.from_dict(zones_cname_flattening_resp_model_json).__dict__
        zones_cname_flattening_resp_model2 = ZonesCnameFlatteningResp(**zones_cname_flattening_resp_model_dict)

        # Verify the model instances are equivalent
        assert zones_cname_flattening_resp_model == zones_cname_flattening_resp_model2

        # Convert model instance back to dict and verify no loss of data
        zones_cname_flattening_resp_model_json2 = zones_cname_flattening_resp_model.to_dict()
        assert zones_cname_flattening_resp_model_json2 == zones_cname_flattening_resp_model_json


class TestModel_ZonesDnssecResp:
    """
    Test Class for ZonesDnssecResp
    """

    def test_zones_dnssec_resp_serialization(self):
        """
        Test serialization/deserialization for ZonesDnssecResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        zones_dnssec_resp_result_model = {}  # ZonesDnssecRespResult
        zones_dnssec_resp_result_model['status'] = 'active'
        zones_dnssec_resp_result_model['flags'] = 257
        zones_dnssec_resp_result_model['algorithm'] = '13'
        zones_dnssec_resp_result_model['key_type'] = 'ECDSAP256SHA256'
        zones_dnssec_resp_result_model['digest_type'] = '2'
        zones_dnssec_resp_result_model['digest_algorithm'] = 'SHA256'
        zones_dnssec_resp_result_model['digest'] = '48E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45'
        zones_dnssec_resp_result_model['ds'] = 'example.com. 3600 IN DS 16953 13 2 248E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45'
        zones_dnssec_resp_result_model['key_tag'] = 42
        zones_dnssec_resp_result_model['public_key'] = 'oXiGYrSTO+LSCJ3mohc8EP+CzF9KxBj8/ydXJ22pKuZP3VAC3/Md/k7xZfz470CoRyZJ6gV6vml07IC3d8xqhA=='

        # Construct a json representation of a ZonesDnssecResp model
        zones_dnssec_resp_model_json = {}
        zones_dnssec_resp_model_json['success'] = True
        zones_dnssec_resp_model_json['errors'] = [['testString']]
        zones_dnssec_resp_model_json['messages'] = [['testString']]
        zones_dnssec_resp_model_json['result'] = zones_dnssec_resp_result_model

        # Construct a model instance of ZonesDnssecResp by calling from_dict on the json representation
        zones_dnssec_resp_model = ZonesDnssecResp.from_dict(zones_dnssec_resp_model_json)
        assert zones_dnssec_resp_model != False

        # Construct a model instance of ZonesDnssecResp by calling from_dict on the json representation
        zones_dnssec_resp_model_dict = ZonesDnssecResp.from_dict(zones_dnssec_resp_model_json).__dict__
        zones_dnssec_resp_model2 = ZonesDnssecResp(**zones_dnssec_resp_model_dict)

        # Verify the model instances are equivalent
        assert zones_dnssec_resp_model == zones_dnssec_resp_model2

        # Convert model instance back to dict and verify no loss of data
        zones_dnssec_resp_model_json2 = zones_dnssec_resp_model.to_dict()
        assert zones_dnssec_resp_model_json2 == zones_dnssec_resp_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
