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
Unit Tests for AuthenticatedOriginPullApiV1
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
from ibm_cloud_networking_services.authenticated_origin_pull_api_v1 import *

crn = 'testString'
zone_identifier = 'testString'

_service = AuthenticatedOriginPullApiV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn,
    zone_identifier=zone_identifier
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
    else:
        return re.compile(request_url.rstrip('/') + '/+')


##############################################################################
# Start of Service: ZoneLevelAuthenticatedOriginPull
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

        service = AuthenticatedOriginPullApiV1.new_instance(
            crn=crn,
            zone_identifier=zone_identifier,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, AuthenticatedOriginPullApiV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = AuthenticatedOriginPullApiV1.new_instance(
                crn=crn,
                zone_identifier=zone_identifier,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = AuthenticatedOriginPullApiV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='crn must be provided'):
            service = AuthenticatedOriginPullApiV1.new_instance(
                crn=None,
                zone_identifier=None,
            )
class TestGetZoneOriginPullSettings():
    """
    Test Class for get_zone_origin_pull_settings
    """

    @responses.activate
    def test_get_zone_origin_pull_settings_all_params(self):
        """
        get_zone_origin_pull_settings()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth/settings')
        mock_response = '{"result": {"enabled": true}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.get_zone_origin_pull_settings(
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_zone_origin_pull_settings_all_params_with_retries(self):
        # Enable retries and run test_get_zone_origin_pull_settings_all_params.
        _service.enable_retries()
        self.test_get_zone_origin_pull_settings_all_params()

        # Disable retries and run test_get_zone_origin_pull_settings_all_params.
        _service.disable_retries()
        self.test_get_zone_origin_pull_settings_all_params()

    @responses.activate
    def test_get_zone_origin_pull_settings_required_params(self):
        """
        test_get_zone_origin_pull_settings_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth/settings')
        mock_response = '{"result": {"enabled": true}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.get_zone_origin_pull_settings()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_zone_origin_pull_settings_required_params_with_retries(self):
        # Enable retries and run test_get_zone_origin_pull_settings_required_params.
        _service.enable_retries()
        self.test_get_zone_origin_pull_settings_required_params()

        # Disable retries and run test_get_zone_origin_pull_settings_required_params.
        _service.disable_retries()
        self.test_get_zone_origin_pull_settings_required_params()

    @responses.activate
    def test_get_zone_origin_pull_settings_value_error(self):
        """
        test_get_zone_origin_pull_settings_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth/settings')
        mock_response = '{"result": {"enabled": true}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
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
                _service.get_zone_origin_pull_settings(**req_copy)


    def test_get_zone_origin_pull_settings_value_error_with_retries(self):
        # Enable retries and run test_get_zone_origin_pull_settings_value_error.
        _service.enable_retries()
        self.test_get_zone_origin_pull_settings_value_error()

        # Disable retries and run test_get_zone_origin_pull_settings_value_error.
        _service.disable_retries()
        self.test_get_zone_origin_pull_settings_value_error()

class TestSetZoneOriginPullSettings():
    """
    Test Class for set_zone_origin_pull_settings
    """

    @responses.activate
    def test_set_zone_origin_pull_settings_all_params(self):
        """
        set_zone_origin_pull_settings()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth/settings')
        mock_response = '{"result": {"enabled": true}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        enabled = True
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.set_zone_origin_pull_settings(
            enabled=enabled,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['enabled'] == True

    def test_set_zone_origin_pull_settings_all_params_with_retries(self):
        # Enable retries and run test_set_zone_origin_pull_settings_all_params.
        _service.enable_retries()
        self.test_set_zone_origin_pull_settings_all_params()

        # Disable retries and run test_set_zone_origin_pull_settings_all_params.
        _service.disable_retries()
        self.test_set_zone_origin_pull_settings_all_params()

    @responses.activate
    def test_set_zone_origin_pull_settings_required_params(self):
        """
        test_set_zone_origin_pull_settings_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth/settings')
        mock_response = '{"result": {"enabled": true}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.set_zone_origin_pull_settings()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_set_zone_origin_pull_settings_required_params_with_retries(self):
        # Enable retries and run test_set_zone_origin_pull_settings_required_params.
        _service.enable_retries()
        self.test_set_zone_origin_pull_settings_required_params()

        # Disable retries and run test_set_zone_origin_pull_settings_required_params.
        _service.disable_retries()
        self.test_set_zone_origin_pull_settings_required_params()

    @responses.activate
    def test_set_zone_origin_pull_settings_value_error(self):
        """
        test_set_zone_origin_pull_settings_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth/settings')
        mock_response = '{"result": {"enabled": true}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(responses.PUT,
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
                _service.set_zone_origin_pull_settings(**req_copy)


    def test_set_zone_origin_pull_settings_value_error_with_retries(self):
        # Enable retries and run test_set_zone_origin_pull_settings_value_error.
        _service.enable_retries()
        self.test_set_zone_origin_pull_settings_value_error()

        # Disable retries and run test_set_zone_origin_pull_settings_value_error.
        _service.disable_retries()
        self.test_set_zone_origin_pull_settings_value_error()

class TestListZoneOriginPullCertificates():
    """
    Test Class for list_zone_origin_pull_certificates
    """

    @responses.activate
    def test_list_zone_origin_pull_certificates_all_params(self):
        """
        list_zone_origin_pull_certificates()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth')
        mock_response = '{"result": [{"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "certificate": "-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n", "issuer": "GlobalSign", "signature": "SHA256WithRSA", "status": "active", "expires_on": "2100-01-01T05:20:00Z", "uploaded_on": "2100-01-01T05:20:00Z"}], "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.list_zone_origin_pull_certificates(
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_zone_origin_pull_certificates_all_params_with_retries(self):
        # Enable retries and run test_list_zone_origin_pull_certificates_all_params.
        _service.enable_retries()
        self.test_list_zone_origin_pull_certificates_all_params()

        # Disable retries and run test_list_zone_origin_pull_certificates_all_params.
        _service.disable_retries()
        self.test_list_zone_origin_pull_certificates_all_params()

    @responses.activate
    def test_list_zone_origin_pull_certificates_required_params(self):
        """
        test_list_zone_origin_pull_certificates_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth')
        mock_response = '{"result": [{"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "certificate": "-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n", "issuer": "GlobalSign", "signature": "SHA256WithRSA", "status": "active", "expires_on": "2100-01-01T05:20:00Z", "uploaded_on": "2100-01-01T05:20:00Z"}], "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_zone_origin_pull_certificates()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_zone_origin_pull_certificates_required_params_with_retries(self):
        # Enable retries and run test_list_zone_origin_pull_certificates_required_params.
        _service.enable_retries()
        self.test_list_zone_origin_pull_certificates_required_params()

        # Disable retries and run test_list_zone_origin_pull_certificates_required_params.
        _service.disable_retries()
        self.test_list_zone_origin_pull_certificates_required_params()

    @responses.activate
    def test_list_zone_origin_pull_certificates_value_error(self):
        """
        test_list_zone_origin_pull_certificates_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth')
        mock_response = '{"result": [{"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "certificate": "-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n", "issuer": "GlobalSign", "signature": "SHA256WithRSA", "status": "active", "expires_on": "2100-01-01T05:20:00Z", "uploaded_on": "2100-01-01T05:20:00Z"}], "success": true, "errors": ["errors"], "messages": ["messages"]}'
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
                _service.list_zone_origin_pull_certificates(**req_copy)


    def test_list_zone_origin_pull_certificates_value_error_with_retries(self):
        # Enable retries and run test_list_zone_origin_pull_certificates_value_error.
        _service.enable_retries()
        self.test_list_zone_origin_pull_certificates_value_error()

        # Disable retries and run test_list_zone_origin_pull_certificates_value_error.
        _service.disable_retries()
        self.test_list_zone_origin_pull_certificates_value_error()

class TestUploadZoneOriginPullCertificate():
    """
    Test Class for upload_zone_origin_pull_certificate
    """

    @responses.activate
    def test_upload_zone_origin_pull_certificate_all_params(self):
        """
        upload_zone_origin_pull_certificate()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth')
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "certificate": "-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n", "issuer": "GlobalSign", "signature": "SHA256WithRSA", "status": "active", "expires_on": "2100-01-01T05:20:00Z", "uploaded_on": "2100-01-01T05:20:00Z"}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        certificate = '-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n'
        private_key = '-----BEGIN RSA PRIVATE KEY-----\n......\n-----END RSA PRIVATE KEY-----\n'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.upload_zone_origin_pull_certificate(
            certificate=certificate,
            private_key=private_key,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['certificate'] == '-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n'
        assert req_body['private_key'] == '-----BEGIN RSA PRIVATE KEY-----\n......\n-----END RSA PRIVATE KEY-----\n'

    def test_upload_zone_origin_pull_certificate_all_params_with_retries(self):
        # Enable retries and run test_upload_zone_origin_pull_certificate_all_params.
        _service.enable_retries()
        self.test_upload_zone_origin_pull_certificate_all_params()

        # Disable retries and run test_upload_zone_origin_pull_certificate_all_params.
        _service.disable_retries()
        self.test_upload_zone_origin_pull_certificate_all_params()

    @responses.activate
    def test_upload_zone_origin_pull_certificate_required_params(self):
        """
        test_upload_zone_origin_pull_certificate_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth')
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "certificate": "-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n", "issuer": "GlobalSign", "signature": "SHA256WithRSA", "status": "active", "expires_on": "2100-01-01T05:20:00Z", "uploaded_on": "2100-01-01T05:20:00Z"}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.upload_zone_origin_pull_certificate()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_upload_zone_origin_pull_certificate_required_params_with_retries(self):
        # Enable retries and run test_upload_zone_origin_pull_certificate_required_params.
        _service.enable_retries()
        self.test_upload_zone_origin_pull_certificate_required_params()

        # Disable retries and run test_upload_zone_origin_pull_certificate_required_params.
        _service.disable_retries()
        self.test_upload_zone_origin_pull_certificate_required_params()

    @responses.activate
    def test_upload_zone_origin_pull_certificate_value_error(self):
        """
        test_upload_zone_origin_pull_certificate_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth')
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "certificate": "-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n", "issuer": "GlobalSign", "signature": "SHA256WithRSA", "status": "active", "expires_on": "2100-01-01T05:20:00Z", "uploaded_on": "2100-01-01T05:20:00Z"}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
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
                _service.upload_zone_origin_pull_certificate(**req_copy)


    def test_upload_zone_origin_pull_certificate_value_error_with_retries(self):
        # Enable retries and run test_upload_zone_origin_pull_certificate_value_error.
        _service.enable_retries()
        self.test_upload_zone_origin_pull_certificate_value_error()

        # Disable retries and run test_upload_zone_origin_pull_certificate_value_error.
        _service.disable_retries()
        self.test_upload_zone_origin_pull_certificate_value_error()

class TestGetZoneOriginPullCertificate():
    """
    Test Class for get_zone_origin_pull_certificate
    """

    @responses.activate
    def test_get_zone_origin_pull_certificate_all_params(self):
        """
        get_zone_origin_pull_certificate()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth/testString')
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "certificate": "-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n", "issuer": "GlobalSign", "signature": "SHA256WithRSA", "status": "active", "expires_on": "2100-01-01T05:20:00Z", "uploaded_on": "2100-01-01T05:20:00Z"}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cert_identifier = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.get_zone_origin_pull_certificate(
            cert_identifier,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_zone_origin_pull_certificate_all_params_with_retries(self):
        # Enable retries and run test_get_zone_origin_pull_certificate_all_params.
        _service.enable_retries()
        self.test_get_zone_origin_pull_certificate_all_params()

        # Disable retries and run test_get_zone_origin_pull_certificate_all_params.
        _service.disable_retries()
        self.test_get_zone_origin_pull_certificate_all_params()

    @responses.activate
    def test_get_zone_origin_pull_certificate_required_params(self):
        """
        test_get_zone_origin_pull_certificate_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth/testString')
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "certificate": "-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n", "issuer": "GlobalSign", "signature": "SHA256WithRSA", "status": "active", "expires_on": "2100-01-01T05:20:00Z", "uploaded_on": "2100-01-01T05:20:00Z"}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cert_identifier = 'testString'

        # Invoke method
        response = _service.get_zone_origin_pull_certificate(
            cert_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_zone_origin_pull_certificate_required_params_with_retries(self):
        # Enable retries and run test_get_zone_origin_pull_certificate_required_params.
        _service.enable_retries()
        self.test_get_zone_origin_pull_certificate_required_params()

        # Disable retries and run test_get_zone_origin_pull_certificate_required_params.
        _service.disable_retries()
        self.test_get_zone_origin_pull_certificate_required_params()

    @responses.activate
    def test_get_zone_origin_pull_certificate_value_error(self):
        """
        test_get_zone_origin_pull_certificate_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth/testString')
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "certificate": "-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n", "issuer": "GlobalSign", "signature": "SHA256WithRSA", "status": "active", "expires_on": "2100-01-01T05:20:00Z", "uploaded_on": "2100-01-01T05:20:00Z"}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cert_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cert_identifier": cert_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_zone_origin_pull_certificate(**req_copy)


    def test_get_zone_origin_pull_certificate_value_error_with_retries(self):
        # Enable retries and run test_get_zone_origin_pull_certificate_value_error.
        _service.enable_retries()
        self.test_get_zone_origin_pull_certificate_value_error()

        # Disable retries and run test_get_zone_origin_pull_certificate_value_error.
        _service.disable_retries()
        self.test_get_zone_origin_pull_certificate_value_error()

class TestDeleteZoneOriginPullCertificate():
    """
    Test Class for delete_zone_origin_pull_certificate
    """

    @responses.activate
    def test_delete_zone_origin_pull_certificate_all_params(self):
        """
        delete_zone_origin_pull_certificate()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth/testString')
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "certificate": "-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n", "issuer": "GlobalSign", "signature": "SHA256WithRSA", "status": "active", "expires_on": "2100-01-01T05:20:00Z", "uploaded_on": "2100-01-01T05:20:00Z"}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cert_identifier = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.delete_zone_origin_pull_certificate(
            cert_identifier,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_zone_origin_pull_certificate_all_params_with_retries(self):
        # Enable retries and run test_delete_zone_origin_pull_certificate_all_params.
        _service.enable_retries()
        self.test_delete_zone_origin_pull_certificate_all_params()

        # Disable retries and run test_delete_zone_origin_pull_certificate_all_params.
        _service.disable_retries()
        self.test_delete_zone_origin_pull_certificate_all_params()

    @responses.activate
    def test_delete_zone_origin_pull_certificate_required_params(self):
        """
        test_delete_zone_origin_pull_certificate_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth/testString')
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "certificate": "-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n", "issuer": "GlobalSign", "signature": "SHA256WithRSA", "status": "active", "expires_on": "2100-01-01T05:20:00Z", "uploaded_on": "2100-01-01T05:20:00Z"}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cert_identifier = 'testString'

        # Invoke method
        response = _service.delete_zone_origin_pull_certificate(
            cert_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_zone_origin_pull_certificate_required_params_with_retries(self):
        # Enable retries and run test_delete_zone_origin_pull_certificate_required_params.
        _service.enable_retries()
        self.test_delete_zone_origin_pull_certificate_required_params()

        # Disable retries and run test_delete_zone_origin_pull_certificate_required_params.
        _service.disable_retries()
        self.test_delete_zone_origin_pull_certificate_required_params()

    @responses.activate
    def test_delete_zone_origin_pull_certificate_value_error(self):
        """
        test_delete_zone_origin_pull_certificate_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth/testString')
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "certificate": "-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n", "issuer": "GlobalSign", "signature": "SHA256WithRSA", "status": "active", "expires_on": "2100-01-01T05:20:00Z", "uploaded_on": "2100-01-01T05:20:00Z"}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cert_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cert_identifier": cert_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_zone_origin_pull_certificate(**req_copy)


    def test_delete_zone_origin_pull_certificate_value_error_with_retries(self):
        # Enable retries and run test_delete_zone_origin_pull_certificate_value_error.
        _service.enable_retries()
        self.test_delete_zone_origin_pull_certificate_value_error()

        # Disable retries and run test_delete_zone_origin_pull_certificate_value_error.
        _service.disable_retries()
        self.test_delete_zone_origin_pull_certificate_value_error()

# endregion
##############################################################################
# End of Service: ZoneLevelAuthenticatedOriginPull
##############################################################################

##############################################################################
# Start of Service: PerHostnameAuthenticatedOriginPull
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

        service = AuthenticatedOriginPullApiV1.new_instance(
            crn=crn,
            zone_identifier=zone_identifier,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, AuthenticatedOriginPullApiV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = AuthenticatedOriginPullApiV1.new_instance(
                crn=crn,
                zone_identifier=zone_identifier,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = AuthenticatedOriginPullApiV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='crn must be provided'):
            service = AuthenticatedOriginPullApiV1.new_instance(
                crn=None,
                zone_identifier=None,
            )
class TestSetHostnameOriginPullSettings():
    """
    Test Class for set_hostname_origin_pull_settings
    """

    @responses.activate
    def test_set_hostname_origin_pull_settings_all_params(self):
        """
        set_hostname_origin_pull_settings()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth/hostnames')
        mock_response = '{"result": [{"hostname": "app.example.com", "cert_id": "2458ce5a-0c35-4c7f-82c7-8e9487d3ff60", "enabled": true, "status": "active", "created_at": "2100-01-01T05:20:00.000Z", "updated_at": "2100-01-01T05:20:00.000Z", "cert_status": "active", "issuer": "GlobalSign", "signature": "SHA256WithRSA", "serial_number": "6743787633689793699141714808227354901", "certificate": "-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n", "cert_uploaded_on": "2019-10-28T18:11:23.374Z", "cert_updated_at": "2100-01-01T05:20:00.000Z", "expires_on": "2100-01-01T05:20:00.000Z"}], "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a HostnameOriginPullSettings model
        hostname_origin_pull_settings_model = {}
        hostname_origin_pull_settings_model['hostname'] = 'app.example.com'
        hostname_origin_pull_settings_model['cert_id'] = '2458ce5a-0c35-4c7f-82c7-8e9487d3ff60'
        hostname_origin_pull_settings_model['enabled'] = True

        # Set up parameter values
        config = [hostname_origin_pull_settings_model]
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.set_hostname_origin_pull_settings(
            config=config,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['config'] == [hostname_origin_pull_settings_model]

    def test_set_hostname_origin_pull_settings_all_params_with_retries(self):
        # Enable retries and run test_set_hostname_origin_pull_settings_all_params.
        _service.enable_retries()
        self.test_set_hostname_origin_pull_settings_all_params()

        # Disable retries and run test_set_hostname_origin_pull_settings_all_params.
        _service.disable_retries()
        self.test_set_hostname_origin_pull_settings_all_params()

    @responses.activate
    def test_set_hostname_origin_pull_settings_required_params(self):
        """
        test_set_hostname_origin_pull_settings_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth/hostnames')
        mock_response = '{"result": [{"hostname": "app.example.com", "cert_id": "2458ce5a-0c35-4c7f-82c7-8e9487d3ff60", "enabled": true, "status": "active", "created_at": "2100-01-01T05:20:00.000Z", "updated_at": "2100-01-01T05:20:00.000Z", "cert_status": "active", "issuer": "GlobalSign", "signature": "SHA256WithRSA", "serial_number": "6743787633689793699141714808227354901", "certificate": "-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n", "cert_uploaded_on": "2019-10-28T18:11:23.374Z", "cert_updated_at": "2100-01-01T05:20:00.000Z", "expires_on": "2100-01-01T05:20:00.000Z"}], "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.set_hostname_origin_pull_settings()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_set_hostname_origin_pull_settings_required_params_with_retries(self):
        # Enable retries and run test_set_hostname_origin_pull_settings_required_params.
        _service.enable_retries()
        self.test_set_hostname_origin_pull_settings_required_params()

        # Disable retries and run test_set_hostname_origin_pull_settings_required_params.
        _service.disable_retries()
        self.test_set_hostname_origin_pull_settings_required_params()

    @responses.activate
    def test_set_hostname_origin_pull_settings_value_error(self):
        """
        test_set_hostname_origin_pull_settings_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth/hostnames')
        mock_response = '{"result": [{"hostname": "app.example.com", "cert_id": "2458ce5a-0c35-4c7f-82c7-8e9487d3ff60", "enabled": true, "status": "active", "created_at": "2100-01-01T05:20:00.000Z", "updated_at": "2100-01-01T05:20:00.000Z", "cert_status": "active", "issuer": "GlobalSign", "signature": "SHA256WithRSA", "serial_number": "6743787633689793699141714808227354901", "certificate": "-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n", "cert_uploaded_on": "2019-10-28T18:11:23.374Z", "cert_updated_at": "2100-01-01T05:20:00.000Z", "expires_on": "2100-01-01T05:20:00.000Z"}], "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(responses.PUT,
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
                _service.set_hostname_origin_pull_settings(**req_copy)


    def test_set_hostname_origin_pull_settings_value_error_with_retries(self):
        # Enable retries and run test_set_hostname_origin_pull_settings_value_error.
        _service.enable_retries()
        self.test_set_hostname_origin_pull_settings_value_error()

        # Disable retries and run test_set_hostname_origin_pull_settings_value_error.
        _service.disable_retries()
        self.test_set_hostname_origin_pull_settings_value_error()

class TestGetHostnameOriginPullSettings():
    """
    Test Class for get_hostname_origin_pull_settings
    """

    @responses.activate
    def test_get_hostname_origin_pull_settings_all_params(self):
        """
        get_hostname_origin_pull_settings()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth/hostnames/testString')
        mock_response = '{"result": {"hostname": "app.example.com", "cert_id": "2458ce5a-0c35-4c7f-82c7-8e9487d3ff60", "enabled": true, "status": "active", "created_at": "2100-01-01T05:20:00.000Z", "updated_at": "2100-01-01T05:20:00.000Z", "cert_status": "active", "issuer": "GlobalSign", "signature": "SHA256WithRSA", "serial_number": "6743787633689793699141714808227354901", "certificate": "-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n", "cert_uploaded_on": "2019-10-28T18:11:23.374Z", "cert_updated_at": "2100-01-01T05:20:00.000Z", "expires_on": "2100-01-01T05:20:00.000Z"}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        hostname = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.get_hostname_origin_pull_settings(
            hostname,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_hostname_origin_pull_settings_all_params_with_retries(self):
        # Enable retries and run test_get_hostname_origin_pull_settings_all_params.
        _service.enable_retries()
        self.test_get_hostname_origin_pull_settings_all_params()

        # Disable retries and run test_get_hostname_origin_pull_settings_all_params.
        _service.disable_retries()
        self.test_get_hostname_origin_pull_settings_all_params()

    @responses.activate
    def test_get_hostname_origin_pull_settings_required_params(self):
        """
        test_get_hostname_origin_pull_settings_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth/hostnames/testString')
        mock_response = '{"result": {"hostname": "app.example.com", "cert_id": "2458ce5a-0c35-4c7f-82c7-8e9487d3ff60", "enabled": true, "status": "active", "created_at": "2100-01-01T05:20:00.000Z", "updated_at": "2100-01-01T05:20:00.000Z", "cert_status": "active", "issuer": "GlobalSign", "signature": "SHA256WithRSA", "serial_number": "6743787633689793699141714808227354901", "certificate": "-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n", "cert_uploaded_on": "2019-10-28T18:11:23.374Z", "cert_updated_at": "2100-01-01T05:20:00.000Z", "expires_on": "2100-01-01T05:20:00.000Z"}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        hostname = 'testString'

        # Invoke method
        response = _service.get_hostname_origin_pull_settings(
            hostname,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_hostname_origin_pull_settings_required_params_with_retries(self):
        # Enable retries and run test_get_hostname_origin_pull_settings_required_params.
        _service.enable_retries()
        self.test_get_hostname_origin_pull_settings_required_params()

        # Disable retries and run test_get_hostname_origin_pull_settings_required_params.
        _service.disable_retries()
        self.test_get_hostname_origin_pull_settings_required_params()

    @responses.activate
    def test_get_hostname_origin_pull_settings_value_error(self):
        """
        test_get_hostname_origin_pull_settings_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth/hostnames/testString')
        mock_response = '{"result": {"hostname": "app.example.com", "cert_id": "2458ce5a-0c35-4c7f-82c7-8e9487d3ff60", "enabled": true, "status": "active", "created_at": "2100-01-01T05:20:00.000Z", "updated_at": "2100-01-01T05:20:00.000Z", "cert_status": "active", "issuer": "GlobalSign", "signature": "SHA256WithRSA", "serial_number": "6743787633689793699141714808227354901", "certificate": "-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n", "cert_uploaded_on": "2019-10-28T18:11:23.374Z", "cert_updated_at": "2100-01-01T05:20:00.000Z", "expires_on": "2100-01-01T05:20:00.000Z"}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        hostname = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "hostname": hostname,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_hostname_origin_pull_settings(**req_copy)


    def test_get_hostname_origin_pull_settings_value_error_with_retries(self):
        # Enable retries and run test_get_hostname_origin_pull_settings_value_error.
        _service.enable_retries()
        self.test_get_hostname_origin_pull_settings_value_error()

        # Disable retries and run test_get_hostname_origin_pull_settings_value_error.
        _service.disable_retries()
        self.test_get_hostname_origin_pull_settings_value_error()

class TestUploadHostnameOriginPullCertificate():
    """
    Test Class for upload_hostname_origin_pull_certificate
    """

    @responses.activate
    def test_upload_hostname_origin_pull_certificate_all_params(self):
        """
        upload_hostname_origin_pull_certificate()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth/hostnames/certificates')
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "certificate": "-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n", "issuer": "GlobalSign", "signature": "SHA256WithRSA", "serial_number": "6743787633689793699141714808227354901", "status": "active", "expires_on": "2100-01-01T05:20:00Z", "uploaded_on": "2100-01-01T05:20:00Z"}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        certificate = '-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n'
        private_key = '-----BEGIN RSA PRIVATE KEY-----\n......\n-----END RSA PRIVATE KEY-----\n'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.upload_hostname_origin_pull_certificate(
            certificate=certificate,
            private_key=private_key,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['certificate'] == '-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n'
        assert req_body['private_key'] == '-----BEGIN RSA PRIVATE KEY-----\n......\n-----END RSA PRIVATE KEY-----\n'

    def test_upload_hostname_origin_pull_certificate_all_params_with_retries(self):
        # Enable retries and run test_upload_hostname_origin_pull_certificate_all_params.
        _service.enable_retries()
        self.test_upload_hostname_origin_pull_certificate_all_params()

        # Disable retries and run test_upload_hostname_origin_pull_certificate_all_params.
        _service.disable_retries()
        self.test_upload_hostname_origin_pull_certificate_all_params()

    @responses.activate
    def test_upload_hostname_origin_pull_certificate_required_params(self):
        """
        test_upload_hostname_origin_pull_certificate_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth/hostnames/certificates')
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "certificate": "-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n", "issuer": "GlobalSign", "signature": "SHA256WithRSA", "serial_number": "6743787633689793699141714808227354901", "status": "active", "expires_on": "2100-01-01T05:20:00Z", "uploaded_on": "2100-01-01T05:20:00Z"}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.upload_hostname_origin_pull_certificate()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_upload_hostname_origin_pull_certificate_required_params_with_retries(self):
        # Enable retries and run test_upload_hostname_origin_pull_certificate_required_params.
        _service.enable_retries()
        self.test_upload_hostname_origin_pull_certificate_required_params()

        # Disable retries and run test_upload_hostname_origin_pull_certificate_required_params.
        _service.disable_retries()
        self.test_upload_hostname_origin_pull_certificate_required_params()

    @responses.activate
    def test_upload_hostname_origin_pull_certificate_value_error(self):
        """
        test_upload_hostname_origin_pull_certificate_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth/hostnames/certificates')
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "certificate": "-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n", "issuer": "GlobalSign", "signature": "SHA256WithRSA", "serial_number": "6743787633689793699141714808227354901", "status": "active", "expires_on": "2100-01-01T05:20:00Z", "uploaded_on": "2100-01-01T05:20:00Z"}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
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
                _service.upload_hostname_origin_pull_certificate(**req_copy)


    def test_upload_hostname_origin_pull_certificate_value_error_with_retries(self):
        # Enable retries and run test_upload_hostname_origin_pull_certificate_value_error.
        _service.enable_retries()
        self.test_upload_hostname_origin_pull_certificate_value_error()

        # Disable retries and run test_upload_hostname_origin_pull_certificate_value_error.
        _service.disable_retries()
        self.test_upload_hostname_origin_pull_certificate_value_error()

class TestGetHostnameOriginPullCertificate():
    """
    Test Class for get_hostname_origin_pull_certificate
    """

    @responses.activate
    def test_get_hostname_origin_pull_certificate_all_params(self):
        """
        get_hostname_origin_pull_certificate()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth/hostnames/certificates/testString')
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "certificate": "-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n", "issuer": "GlobalSign", "signature": "SHA256WithRSA", "serial_number": "6743787633689793699141714808227354901", "status": "active", "expires_on": "2100-01-01T05:20:00Z", "uploaded_on": "2100-01-01T05:20:00Z"}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cert_identifier = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.get_hostname_origin_pull_certificate(
            cert_identifier,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_hostname_origin_pull_certificate_all_params_with_retries(self):
        # Enable retries and run test_get_hostname_origin_pull_certificate_all_params.
        _service.enable_retries()
        self.test_get_hostname_origin_pull_certificate_all_params()

        # Disable retries and run test_get_hostname_origin_pull_certificate_all_params.
        _service.disable_retries()
        self.test_get_hostname_origin_pull_certificate_all_params()

    @responses.activate
    def test_get_hostname_origin_pull_certificate_required_params(self):
        """
        test_get_hostname_origin_pull_certificate_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth/hostnames/certificates/testString')
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "certificate": "-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n", "issuer": "GlobalSign", "signature": "SHA256WithRSA", "serial_number": "6743787633689793699141714808227354901", "status": "active", "expires_on": "2100-01-01T05:20:00Z", "uploaded_on": "2100-01-01T05:20:00Z"}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cert_identifier = 'testString'

        # Invoke method
        response = _service.get_hostname_origin_pull_certificate(
            cert_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_hostname_origin_pull_certificate_required_params_with_retries(self):
        # Enable retries and run test_get_hostname_origin_pull_certificate_required_params.
        _service.enable_retries()
        self.test_get_hostname_origin_pull_certificate_required_params()

        # Disable retries and run test_get_hostname_origin_pull_certificate_required_params.
        _service.disable_retries()
        self.test_get_hostname_origin_pull_certificate_required_params()

    @responses.activate
    def test_get_hostname_origin_pull_certificate_value_error(self):
        """
        test_get_hostname_origin_pull_certificate_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth/hostnames/certificates/testString')
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "certificate": "-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n", "issuer": "GlobalSign", "signature": "SHA256WithRSA", "serial_number": "6743787633689793699141714808227354901", "status": "active", "expires_on": "2100-01-01T05:20:00Z", "uploaded_on": "2100-01-01T05:20:00Z"}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cert_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cert_identifier": cert_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_hostname_origin_pull_certificate(**req_copy)


    def test_get_hostname_origin_pull_certificate_value_error_with_retries(self):
        # Enable retries and run test_get_hostname_origin_pull_certificate_value_error.
        _service.enable_retries()
        self.test_get_hostname_origin_pull_certificate_value_error()

        # Disable retries and run test_get_hostname_origin_pull_certificate_value_error.
        _service.disable_retries()
        self.test_get_hostname_origin_pull_certificate_value_error()

class TestDeleteHostnameOriginPullCertificate():
    """
    Test Class for delete_hostname_origin_pull_certificate
    """

    @responses.activate
    def test_delete_hostname_origin_pull_certificate_all_params(self):
        """
        delete_hostname_origin_pull_certificate()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth/hostnames/certificates/testString')
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "certificate": "-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n", "issuer": "GlobalSign", "signature": "SHA256WithRSA", "serial_number": "6743787633689793699141714808227354901", "status": "active", "expires_on": "2100-01-01T05:20:00Z", "uploaded_on": "2100-01-01T05:20:00Z"}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cert_identifier = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = _service.delete_hostname_origin_pull_certificate(
            cert_identifier,
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_hostname_origin_pull_certificate_all_params_with_retries(self):
        # Enable retries and run test_delete_hostname_origin_pull_certificate_all_params.
        _service.enable_retries()
        self.test_delete_hostname_origin_pull_certificate_all_params()

        # Disable retries and run test_delete_hostname_origin_pull_certificate_all_params.
        _service.disable_retries()
        self.test_delete_hostname_origin_pull_certificate_all_params()

    @responses.activate
    def test_delete_hostname_origin_pull_certificate_required_params(self):
        """
        test_delete_hostname_origin_pull_certificate_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth/hostnames/certificates/testString')
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "certificate": "-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n", "issuer": "GlobalSign", "signature": "SHA256WithRSA", "serial_number": "6743787633689793699141714808227354901", "status": "active", "expires_on": "2100-01-01T05:20:00Z", "uploaded_on": "2100-01-01T05:20:00Z"}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cert_identifier = 'testString'

        # Invoke method
        response = _service.delete_hostname_origin_pull_certificate(
            cert_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_delete_hostname_origin_pull_certificate_required_params_with_retries(self):
        # Enable retries and run test_delete_hostname_origin_pull_certificate_required_params.
        _service.enable_retries()
        self.test_delete_hostname_origin_pull_certificate_required_params()

        # Disable retries and run test_delete_hostname_origin_pull_certificate_required_params.
        _service.disable_retries()
        self.test_delete_hostname_origin_pull_certificate_required_params()

    @responses.activate
    def test_delete_hostname_origin_pull_certificate_value_error(self):
        """
        test_delete_hostname_origin_pull_certificate_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/testString/zones/testString/origin_tls_client_auth/hostnames/certificates/testString')
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "certificate": "-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n", "issuer": "GlobalSign", "signature": "SHA256WithRSA", "serial_number": "6743787633689793699141714808227354901", "status": "active", "expires_on": "2100-01-01T05:20:00Z", "uploaded_on": "2100-01-01T05:20:00Z"}, "success": true, "errors": ["errors"], "messages": ["messages"]}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        cert_identifier = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "cert_identifier": cert_identifier,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_hostname_origin_pull_certificate(**req_copy)


    def test_delete_hostname_origin_pull_certificate_value_error_with_retries(self):
        # Enable retries and run test_delete_hostname_origin_pull_certificate_value_error.
        _service.enable_retries()
        self.test_delete_hostname_origin_pull_certificate_value_error()

        # Disable retries and run test_delete_hostname_origin_pull_certificate_value_error.
        _service.disable_retries()
        self.test_delete_hostname_origin_pull_certificate_value_error()

# endregion
##############################################################################
# End of Service: PerHostnameAuthenticatedOriginPull
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_GetZoneOriginPullSettingsRespResult():
    """
    Test Class for GetZoneOriginPullSettingsRespResult
    """

    def test_get_zone_origin_pull_settings_resp_result_serialization(self):
        """
        Test serialization/deserialization for GetZoneOriginPullSettingsRespResult
        """

        # Construct a json representation of a GetZoneOriginPullSettingsRespResult model
        get_zone_origin_pull_settings_resp_result_model_json = {}
        get_zone_origin_pull_settings_resp_result_model_json['enabled'] = True

        # Construct a model instance of GetZoneOriginPullSettingsRespResult by calling from_dict on the json representation
        get_zone_origin_pull_settings_resp_result_model = GetZoneOriginPullSettingsRespResult.from_dict(get_zone_origin_pull_settings_resp_result_model_json)
        assert get_zone_origin_pull_settings_resp_result_model != False

        # Construct a model instance of GetZoneOriginPullSettingsRespResult by calling from_dict on the json representation
        get_zone_origin_pull_settings_resp_result_model_dict = GetZoneOriginPullSettingsRespResult.from_dict(get_zone_origin_pull_settings_resp_result_model_json).__dict__
        get_zone_origin_pull_settings_resp_result_model2 = GetZoneOriginPullSettingsRespResult(**get_zone_origin_pull_settings_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert get_zone_origin_pull_settings_resp_result_model == get_zone_origin_pull_settings_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        get_zone_origin_pull_settings_resp_result_model_json2 = get_zone_origin_pull_settings_resp_result_model.to_dict()
        assert get_zone_origin_pull_settings_resp_result_model_json2 == get_zone_origin_pull_settings_resp_result_model_json

class TestModel_CertificatePack():
    """
    Test Class for CertificatePack
    """

    def test_certificate_pack_serialization(self):
        """
        Test serialization/deserialization for CertificatePack
        """

        # Construct a json representation of a CertificatePack model
        certificate_pack_model_json = {}
        certificate_pack_model_json['id'] = '0f405ba2-8c18-49eb-a30b-28b85427780f'
        certificate_pack_model_json['certificate'] = '-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n'
        certificate_pack_model_json['issuer'] = 'GlobalSign'
        certificate_pack_model_json['signature'] = 'SHA256WithRSA'
        certificate_pack_model_json['status'] = 'active'
        certificate_pack_model_json['expires_on'] = '2100-01-01T05:20:00Z'
        certificate_pack_model_json['uploaded_on'] = '2100-01-01T05:20:00Z'

        # Construct a model instance of CertificatePack by calling from_dict on the json representation
        certificate_pack_model = CertificatePack.from_dict(certificate_pack_model_json)
        assert certificate_pack_model != False

        # Construct a model instance of CertificatePack by calling from_dict on the json representation
        certificate_pack_model_dict = CertificatePack.from_dict(certificate_pack_model_json).__dict__
        certificate_pack_model2 = CertificatePack(**certificate_pack_model_dict)

        # Verify the model instances are equivalent
        assert certificate_pack_model == certificate_pack_model2

        # Convert model instance back to dict and verify no loss of data
        certificate_pack_model_json2 = certificate_pack_model.to_dict()
        assert certificate_pack_model_json2 == certificate_pack_model_json

class TestModel_GetHostnameOriginPullSettingsResp():
    """
    Test Class for GetHostnameOriginPullSettingsResp
    """

    def test_get_hostname_origin_pull_settings_resp_serialization(self):
        """
        Test serialization/deserialization for GetHostnameOriginPullSettingsResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        hostname_settings_resp_model = {} # HostnameSettingsResp
        hostname_settings_resp_model['hostname'] = 'app.example.com'
        hostname_settings_resp_model['cert_id'] = '2458ce5a-0c35-4c7f-82c7-8e9487d3ff60'
        hostname_settings_resp_model['enabled'] = True
        hostname_settings_resp_model['status'] = 'active'
        hostname_settings_resp_model['created_at'] = '2100-01-01T05:20:00Z'
        hostname_settings_resp_model['updated_at'] = '2100-01-01T05:20:00Z'
        hostname_settings_resp_model['cert_status'] = 'active'
        hostname_settings_resp_model['issuer'] = 'GlobalSign'
        hostname_settings_resp_model['signature'] = 'SHA256WithRSA'
        hostname_settings_resp_model['serial_number'] = '6743787633689793699141714808227354901'
        hostname_settings_resp_model['certificate'] = '-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n'
        hostname_settings_resp_model['cert_uploaded_on'] = '2019-10-28T18:11:23.374000Z'
        hostname_settings_resp_model['cert_updated_at'] = '2100-01-01T05:20:00Z'
        hostname_settings_resp_model['expires_on'] = '2100-01-01T05:20:00Z'

        # Construct a json representation of a GetHostnameOriginPullSettingsResp model
        get_hostname_origin_pull_settings_resp_model_json = {}
        get_hostname_origin_pull_settings_resp_model_json['result'] = hostname_settings_resp_model
        get_hostname_origin_pull_settings_resp_model_json['success'] = True
        get_hostname_origin_pull_settings_resp_model_json['errors'] = ['testString']
        get_hostname_origin_pull_settings_resp_model_json['messages'] = ['testString']

        # Construct a model instance of GetHostnameOriginPullSettingsResp by calling from_dict on the json representation
        get_hostname_origin_pull_settings_resp_model = GetHostnameOriginPullSettingsResp.from_dict(get_hostname_origin_pull_settings_resp_model_json)
        assert get_hostname_origin_pull_settings_resp_model != False

        # Construct a model instance of GetHostnameOriginPullSettingsResp by calling from_dict on the json representation
        get_hostname_origin_pull_settings_resp_model_dict = GetHostnameOriginPullSettingsResp.from_dict(get_hostname_origin_pull_settings_resp_model_json).__dict__
        get_hostname_origin_pull_settings_resp_model2 = GetHostnameOriginPullSettingsResp(**get_hostname_origin_pull_settings_resp_model_dict)

        # Verify the model instances are equivalent
        assert get_hostname_origin_pull_settings_resp_model == get_hostname_origin_pull_settings_resp_model2

        # Convert model instance back to dict and verify no loss of data
        get_hostname_origin_pull_settings_resp_model_json2 = get_hostname_origin_pull_settings_resp_model.to_dict()
        assert get_hostname_origin_pull_settings_resp_model_json2 == get_hostname_origin_pull_settings_resp_model_json

class TestModel_GetZoneOriginPullSettingsResp():
    """
    Test Class for GetZoneOriginPullSettingsResp
    """

    def test_get_zone_origin_pull_settings_resp_serialization(self):
        """
        Test serialization/deserialization for GetZoneOriginPullSettingsResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        get_zone_origin_pull_settings_resp_result_model = {} # GetZoneOriginPullSettingsRespResult
        get_zone_origin_pull_settings_resp_result_model['enabled'] = True

        # Construct a json representation of a GetZoneOriginPullSettingsResp model
        get_zone_origin_pull_settings_resp_model_json = {}
        get_zone_origin_pull_settings_resp_model_json['result'] = get_zone_origin_pull_settings_resp_result_model
        get_zone_origin_pull_settings_resp_model_json['success'] = True
        get_zone_origin_pull_settings_resp_model_json['errors'] = ['testString']
        get_zone_origin_pull_settings_resp_model_json['messages'] = ['testString']

        # Construct a model instance of GetZoneOriginPullSettingsResp by calling from_dict on the json representation
        get_zone_origin_pull_settings_resp_model = GetZoneOriginPullSettingsResp.from_dict(get_zone_origin_pull_settings_resp_model_json)
        assert get_zone_origin_pull_settings_resp_model != False

        # Construct a model instance of GetZoneOriginPullSettingsResp by calling from_dict on the json representation
        get_zone_origin_pull_settings_resp_model_dict = GetZoneOriginPullSettingsResp.from_dict(get_zone_origin_pull_settings_resp_model_json).__dict__
        get_zone_origin_pull_settings_resp_model2 = GetZoneOriginPullSettingsResp(**get_zone_origin_pull_settings_resp_model_dict)

        # Verify the model instances are equivalent
        assert get_zone_origin_pull_settings_resp_model == get_zone_origin_pull_settings_resp_model2

        # Convert model instance back to dict and verify no loss of data
        get_zone_origin_pull_settings_resp_model_json2 = get_zone_origin_pull_settings_resp_model.to_dict()
        assert get_zone_origin_pull_settings_resp_model_json2 == get_zone_origin_pull_settings_resp_model_json

class TestModel_HostnameCertificatePack():
    """
    Test Class for HostnameCertificatePack
    """

    def test_hostname_certificate_pack_serialization(self):
        """
        Test serialization/deserialization for HostnameCertificatePack
        """

        # Construct a json representation of a HostnameCertificatePack model
        hostname_certificate_pack_model_json = {}
        hostname_certificate_pack_model_json['id'] = '0f405ba2-8c18-49eb-a30b-28b85427780f'
        hostname_certificate_pack_model_json['certificate'] = '-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n'
        hostname_certificate_pack_model_json['issuer'] = 'GlobalSign'
        hostname_certificate_pack_model_json['signature'] = 'SHA256WithRSA'
        hostname_certificate_pack_model_json['serial_number'] = '6743787633689793699141714808227354901'
        hostname_certificate_pack_model_json['status'] = 'active'
        hostname_certificate_pack_model_json['expires_on'] = '2100-01-01T05:20:00Z'
        hostname_certificate_pack_model_json['uploaded_on'] = '2100-01-01T05:20:00Z'

        # Construct a model instance of HostnameCertificatePack by calling from_dict on the json representation
        hostname_certificate_pack_model = HostnameCertificatePack.from_dict(hostname_certificate_pack_model_json)
        assert hostname_certificate_pack_model != False

        # Construct a model instance of HostnameCertificatePack by calling from_dict on the json representation
        hostname_certificate_pack_model_dict = HostnameCertificatePack.from_dict(hostname_certificate_pack_model_json).__dict__
        hostname_certificate_pack_model2 = HostnameCertificatePack(**hostname_certificate_pack_model_dict)

        # Verify the model instances are equivalent
        assert hostname_certificate_pack_model == hostname_certificate_pack_model2

        # Convert model instance back to dict and verify no loss of data
        hostname_certificate_pack_model_json2 = hostname_certificate_pack_model.to_dict()
        assert hostname_certificate_pack_model_json2 == hostname_certificate_pack_model_json

class TestModel_HostnameOriginPullCertificateResp():
    """
    Test Class for HostnameOriginPullCertificateResp
    """

    def test_hostname_origin_pull_certificate_resp_serialization(self):
        """
        Test serialization/deserialization for HostnameOriginPullCertificateResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        hostname_certificate_pack_model = {} # HostnameCertificatePack
        hostname_certificate_pack_model['id'] = '0f405ba2-8c18-49eb-a30b-28b85427780f'
        hostname_certificate_pack_model['certificate'] = '-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n'
        hostname_certificate_pack_model['issuer'] = 'GlobalSign'
        hostname_certificate_pack_model['signature'] = 'SHA256WithRSA'
        hostname_certificate_pack_model['serial_number'] = '6743787633689793699141714808227354901'
        hostname_certificate_pack_model['status'] = 'active'
        hostname_certificate_pack_model['expires_on'] = '2100-01-01T05:20:00Z'
        hostname_certificate_pack_model['uploaded_on'] = '2100-01-01T05:20:00Z'

        # Construct a json representation of a HostnameOriginPullCertificateResp model
        hostname_origin_pull_certificate_resp_model_json = {}
        hostname_origin_pull_certificate_resp_model_json['result'] = hostname_certificate_pack_model
        hostname_origin_pull_certificate_resp_model_json['success'] = True
        hostname_origin_pull_certificate_resp_model_json['errors'] = ['testString']
        hostname_origin_pull_certificate_resp_model_json['messages'] = ['testString']

        # Construct a model instance of HostnameOriginPullCertificateResp by calling from_dict on the json representation
        hostname_origin_pull_certificate_resp_model = HostnameOriginPullCertificateResp.from_dict(hostname_origin_pull_certificate_resp_model_json)
        assert hostname_origin_pull_certificate_resp_model != False

        # Construct a model instance of HostnameOriginPullCertificateResp by calling from_dict on the json representation
        hostname_origin_pull_certificate_resp_model_dict = HostnameOriginPullCertificateResp.from_dict(hostname_origin_pull_certificate_resp_model_json).__dict__
        hostname_origin_pull_certificate_resp_model2 = HostnameOriginPullCertificateResp(**hostname_origin_pull_certificate_resp_model_dict)

        # Verify the model instances are equivalent
        assert hostname_origin_pull_certificate_resp_model == hostname_origin_pull_certificate_resp_model2

        # Convert model instance back to dict and verify no loss of data
        hostname_origin_pull_certificate_resp_model_json2 = hostname_origin_pull_certificate_resp_model.to_dict()
        assert hostname_origin_pull_certificate_resp_model_json2 == hostname_origin_pull_certificate_resp_model_json

class TestModel_HostnameOriginPullSettings():
    """
    Test Class for HostnameOriginPullSettings
    """

    def test_hostname_origin_pull_settings_serialization(self):
        """
        Test serialization/deserialization for HostnameOriginPullSettings
        """

        # Construct a json representation of a HostnameOriginPullSettings model
        hostname_origin_pull_settings_model_json = {}
        hostname_origin_pull_settings_model_json['hostname'] = 'app.example.com'
        hostname_origin_pull_settings_model_json['cert_id'] = '2458ce5a-0c35-4c7f-82c7-8e9487d3ff60'
        hostname_origin_pull_settings_model_json['enabled'] = True

        # Construct a model instance of HostnameOriginPullSettings by calling from_dict on the json representation
        hostname_origin_pull_settings_model = HostnameOriginPullSettings.from_dict(hostname_origin_pull_settings_model_json)
        assert hostname_origin_pull_settings_model != False

        # Construct a model instance of HostnameOriginPullSettings by calling from_dict on the json representation
        hostname_origin_pull_settings_model_dict = HostnameOriginPullSettings.from_dict(hostname_origin_pull_settings_model_json).__dict__
        hostname_origin_pull_settings_model2 = HostnameOriginPullSettings(**hostname_origin_pull_settings_model_dict)

        # Verify the model instances are equivalent
        assert hostname_origin_pull_settings_model == hostname_origin_pull_settings_model2

        # Convert model instance back to dict and verify no loss of data
        hostname_origin_pull_settings_model_json2 = hostname_origin_pull_settings_model.to_dict()
        assert hostname_origin_pull_settings_model_json2 == hostname_origin_pull_settings_model_json

class TestModel_HostnameSettingsResp():
    """
    Test Class for HostnameSettingsResp
    """

    def test_hostname_settings_resp_serialization(self):
        """
        Test serialization/deserialization for HostnameSettingsResp
        """

        # Construct a json representation of a HostnameSettingsResp model
        hostname_settings_resp_model_json = {}
        hostname_settings_resp_model_json['hostname'] = 'app.example.com'
        hostname_settings_resp_model_json['cert_id'] = '2458ce5a-0c35-4c7f-82c7-8e9487d3ff60'
        hostname_settings_resp_model_json['enabled'] = True
        hostname_settings_resp_model_json['status'] = 'active'
        hostname_settings_resp_model_json['created_at'] = '2100-01-01T05:20:00Z'
        hostname_settings_resp_model_json['updated_at'] = '2100-01-01T05:20:00Z'
        hostname_settings_resp_model_json['cert_status'] = 'active'
        hostname_settings_resp_model_json['issuer'] = 'GlobalSign'
        hostname_settings_resp_model_json['signature'] = 'SHA256WithRSA'
        hostname_settings_resp_model_json['serial_number'] = '6743787633689793699141714808227354901'
        hostname_settings_resp_model_json['certificate'] = '-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n'
        hostname_settings_resp_model_json['cert_uploaded_on'] = '2019-10-28T18:11:23.374000Z'
        hostname_settings_resp_model_json['cert_updated_at'] = '2100-01-01T05:20:00Z'
        hostname_settings_resp_model_json['expires_on'] = '2100-01-01T05:20:00Z'

        # Construct a model instance of HostnameSettingsResp by calling from_dict on the json representation
        hostname_settings_resp_model = HostnameSettingsResp.from_dict(hostname_settings_resp_model_json)
        assert hostname_settings_resp_model != False

        # Construct a model instance of HostnameSettingsResp by calling from_dict on the json representation
        hostname_settings_resp_model_dict = HostnameSettingsResp.from_dict(hostname_settings_resp_model_json).__dict__
        hostname_settings_resp_model2 = HostnameSettingsResp(**hostname_settings_resp_model_dict)

        # Verify the model instances are equivalent
        assert hostname_settings_resp_model == hostname_settings_resp_model2

        # Convert model instance back to dict and verify no loss of data
        hostname_settings_resp_model_json2 = hostname_settings_resp_model.to_dict()
        assert hostname_settings_resp_model_json2 == hostname_settings_resp_model_json

class TestModel_ListHostnameOriginPullSettingsResp():
    """
    Test Class for ListHostnameOriginPullSettingsResp
    """

    def test_list_hostname_origin_pull_settings_resp_serialization(self):
        """
        Test serialization/deserialization for ListHostnameOriginPullSettingsResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        hostname_settings_resp_model = {} # HostnameSettingsResp
        hostname_settings_resp_model['hostname'] = 'app.example.com'
        hostname_settings_resp_model['cert_id'] = '2458ce5a-0c35-4c7f-82c7-8e9487d3ff60'
        hostname_settings_resp_model['enabled'] = True
        hostname_settings_resp_model['status'] = 'active'
        hostname_settings_resp_model['created_at'] = '2100-01-01T05:20:00Z'
        hostname_settings_resp_model['updated_at'] = '2100-01-01T05:20:00Z'
        hostname_settings_resp_model['cert_status'] = 'active'
        hostname_settings_resp_model['issuer'] = 'GlobalSign'
        hostname_settings_resp_model['signature'] = 'SHA256WithRSA'
        hostname_settings_resp_model['serial_number'] = '6743787633689793699141714808227354901'
        hostname_settings_resp_model['certificate'] = '-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n'
        hostname_settings_resp_model['cert_uploaded_on'] = '2019-10-28T18:11:23.374000Z'
        hostname_settings_resp_model['cert_updated_at'] = '2100-01-01T05:20:00Z'
        hostname_settings_resp_model['expires_on'] = '2100-01-01T05:20:00Z'

        # Construct a json representation of a ListHostnameOriginPullSettingsResp model
        list_hostname_origin_pull_settings_resp_model_json = {}
        list_hostname_origin_pull_settings_resp_model_json['result'] = [hostname_settings_resp_model]
        list_hostname_origin_pull_settings_resp_model_json['success'] = True
        list_hostname_origin_pull_settings_resp_model_json['errors'] = ['testString']
        list_hostname_origin_pull_settings_resp_model_json['messages'] = ['testString']

        # Construct a model instance of ListHostnameOriginPullSettingsResp by calling from_dict on the json representation
        list_hostname_origin_pull_settings_resp_model = ListHostnameOriginPullSettingsResp.from_dict(list_hostname_origin_pull_settings_resp_model_json)
        assert list_hostname_origin_pull_settings_resp_model != False

        # Construct a model instance of ListHostnameOriginPullSettingsResp by calling from_dict on the json representation
        list_hostname_origin_pull_settings_resp_model_dict = ListHostnameOriginPullSettingsResp.from_dict(list_hostname_origin_pull_settings_resp_model_json).__dict__
        list_hostname_origin_pull_settings_resp_model2 = ListHostnameOriginPullSettingsResp(**list_hostname_origin_pull_settings_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_hostname_origin_pull_settings_resp_model == list_hostname_origin_pull_settings_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_hostname_origin_pull_settings_resp_model_json2 = list_hostname_origin_pull_settings_resp_model.to_dict()
        assert list_hostname_origin_pull_settings_resp_model_json2 == list_hostname_origin_pull_settings_resp_model_json

class TestModel_ListZoneOriginPullCertificatesResp():
    """
    Test Class for ListZoneOriginPullCertificatesResp
    """

    def test_list_zone_origin_pull_certificates_resp_serialization(self):
        """
        Test serialization/deserialization for ListZoneOriginPullCertificatesResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        certificate_pack_model = {} # CertificatePack
        certificate_pack_model['id'] = '0f405ba2-8c18-49eb-a30b-28b85427780f'
        certificate_pack_model['certificate'] = '-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n'
        certificate_pack_model['issuer'] = 'GlobalSign'
        certificate_pack_model['signature'] = 'SHA256WithRSA'
        certificate_pack_model['status'] = 'active'
        certificate_pack_model['expires_on'] = '2100-01-01T05:20:00Z'
        certificate_pack_model['uploaded_on'] = '2100-01-01T05:20:00Z'

        # Construct a json representation of a ListZoneOriginPullCertificatesResp model
        list_zone_origin_pull_certificates_resp_model_json = {}
        list_zone_origin_pull_certificates_resp_model_json['result'] = [certificate_pack_model]
        list_zone_origin_pull_certificates_resp_model_json['success'] = True
        list_zone_origin_pull_certificates_resp_model_json['errors'] = ['testString']
        list_zone_origin_pull_certificates_resp_model_json['messages'] = ['testString']

        # Construct a model instance of ListZoneOriginPullCertificatesResp by calling from_dict on the json representation
        list_zone_origin_pull_certificates_resp_model = ListZoneOriginPullCertificatesResp.from_dict(list_zone_origin_pull_certificates_resp_model_json)
        assert list_zone_origin_pull_certificates_resp_model != False

        # Construct a model instance of ListZoneOriginPullCertificatesResp by calling from_dict on the json representation
        list_zone_origin_pull_certificates_resp_model_dict = ListZoneOriginPullCertificatesResp.from_dict(list_zone_origin_pull_certificates_resp_model_json).__dict__
        list_zone_origin_pull_certificates_resp_model2 = ListZoneOriginPullCertificatesResp(**list_zone_origin_pull_certificates_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_zone_origin_pull_certificates_resp_model == list_zone_origin_pull_certificates_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_zone_origin_pull_certificates_resp_model_json2 = list_zone_origin_pull_certificates_resp_model.to_dict()
        assert list_zone_origin_pull_certificates_resp_model_json2 == list_zone_origin_pull_certificates_resp_model_json

class TestModel_ZoneOriginPullCertificateResp():
    """
    Test Class for ZoneOriginPullCertificateResp
    """

    def test_zone_origin_pull_certificate_resp_serialization(self):
        """
        Test serialization/deserialization for ZoneOriginPullCertificateResp
        """

        # Construct dict forms of any model objects needed in order to build this model.

        certificate_pack_model = {} # CertificatePack
        certificate_pack_model['id'] = '0f405ba2-8c18-49eb-a30b-28b85427780f'
        certificate_pack_model['certificate'] = '-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n'
        certificate_pack_model['issuer'] = 'GlobalSign'
        certificate_pack_model['signature'] = 'SHA256WithRSA'
        certificate_pack_model['status'] = 'active'
        certificate_pack_model['expires_on'] = '2100-01-01T05:20:00Z'
        certificate_pack_model['uploaded_on'] = '2100-01-01T05:20:00Z'

        # Construct a json representation of a ZoneOriginPullCertificateResp model
        zone_origin_pull_certificate_resp_model_json = {}
        zone_origin_pull_certificate_resp_model_json['result'] = certificate_pack_model
        zone_origin_pull_certificate_resp_model_json['success'] = True
        zone_origin_pull_certificate_resp_model_json['errors'] = ['testString']
        zone_origin_pull_certificate_resp_model_json['messages'] = ['testString']

        # Construct a model instance of ZoneOriginPullCertificateResp by calling from_dict on the json representation
        zone_origin_pull_certificate_resp_model = ZoneOriginPullCertificateResp.from_dict(zone_origin_pull_certificate_resp_model_json)
        assert zone_origin_pull_certificate_resp_model != False

        # Construct a model instance of ZoneOriginPullCertificateResp by calling from_dict on the json representation
        zone_origin_pull_certificate_resp_model_dict = ZoneOriginPullCertificateResp.from_dict(zone_origin_pull_certificate_resp_model_json).__dict__
        zone_origin_pull_certificate_resp_model2 = ZoneOriginPullCertificateResp(**zone_origin_pull_certificate_resp_model_dict)

        # Verify the model instances are equivalent
        assert zone_origin_pull_certificate_resp_model == zone_origin_pull_certificate_resp_model2

        # Convert model instance back to dict and verify no loss of data
        zone_origin_pull_certificate_resp_model_json2 = zone_origin_pull_certificate_resp_model.to_dict()
        assert zone_origin_pull_certificate_resp_model_json2 == zone_origin_pull_certificate_resp_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
