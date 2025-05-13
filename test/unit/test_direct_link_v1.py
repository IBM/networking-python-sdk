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
Unit Tests for DirectLinkV1
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
from ibm_cloud_networking_services.direct_link_v1 import *

version = 'testString'

_service = DirectLinkV1(
    authenticator=NoAuthAuthenticator(),
    version=version,
)

_base_url = 'https://directlink.cloud.ibm.com/v1'
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
# Start of Service: Gateways
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

        service = DirectLinkV1.new_instance(
            version=version,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DirectLinkV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DirectLinkV1.new_instance(
                version=version,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = DirectLinkV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='version must be provided'):
            service = DirectLinkV1.new_instance(
                version=None,
            )


class TestListGateways:
    """
    Test Class for list_gateways
    """

    @responses.activate
    def test_list_gateways_all_params(self):
        """
        list_gateways()
        """
        # Set up mock
        url = preprocess_url('/gateways')
        mock_response = '{"gateways": [{"as_prepends": [{"created_at": "2019-01-01T12:00:00.000Z", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "length": 4, "policy": "import", "prefix": "172.17.0.0/16", "specific_prefixes": ["192.168.3.0/24"], "updated_at": "2019-01-01T12:00:00.000Z"}], "authentication_key": {"crn": "crn:v1:bluemix:public:kms:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222"}, "bfd_config": {"bfd_status": "up", "bfd_status_updated_at": "2020-08-20T06:58:41.909Z", "interval": 2000, "multiplier": 10}, "bgp_asn": 64999, "bgp_base_cidr": "bgp_base_cidr", "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "bgp_status_updated_at": "2020-08-20T06:58:41.909Z", "carrier_name": "myCarrierName", "change_request": {"type": "create_gateway"}, "completion_notice_reject_reason": "The completion notice file was blank", "connection_mode": "transit", "created_at": "2019-01-01T12:00:00.000Z", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::dedicated:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "cross_account": false, "cross_connect_router": "xcr01.dal03", "customer_name": "newCustomerName", "default_export_route_filter": "permit", "default_import_route_filter": "permit", "global": true, "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "link_status": "up", "link_status_updated_at": "2020-08-20T06:58:41.909Z", "location_display_name": "Dallas 03", "location_name": "dal03", "macsec": {"active": true, "security_policy": "must_secure", "status": "secured", "status_reasons": [{"code": "macsec_cak_failed", "message": "The `authentication_key` failed configuration.", "more_info": "https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK"}]}, "macsec_capability": "non_macsec", "metered": false, "name": "myGateway", "operational_status": "awaiting_completion_notice", "operational_status_reasons": [{"code": "authentication_key_failed", "message": "The `authentication_key` failed configuration.", "more_info": "https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK"}], "patch_panel_completion_notice": "patch panel configuration details", "port": {"id": "54321b1a-fee4-41c7-9e11-9cd99e000aaa"}, "provider_api_managed": false, "resource_group": {"id": "56969d6043e9465c883cb9f7363e78e8"}, "speed_mbps": 1000, "type": "dedicated", "vlan": 10}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_gateways()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_gateways_all_params_with_retries(self):
        # Enable retries and run test_list_gateways_all_params.
        _service.enable_retries()
        self.test_list_gateways_all_params()

        # Disable retries and run test_list_gateways_all_params.
        _service.disable_retries()
        self.test_list_gateways_all_params()

    @responses.activate
    def test_list_gateways_value_error(self):
        """
        test_list_gateways_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways')
        mock_response = '{"gateways": [{"as_prepends": [{"created_at": "2019-01-01T12:00:00.000Z", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "length": 4, "policy": "import", "prefix": "172.17.0.0/16", "specific_prefixes": ["192.168.3.0/24"], "updated_at": "2019-01-01T12:00:00.000Z"}], "authentication_key": {"crn": "crn:v1:bluemix:public:kms:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222"}, "bfd_config": {"bfd_status": "up", "bfd_status_updated_at": "2020-08-20T06:58:41.909Z", "interval": 2000, "multiplier": 10}, "bgp_asn": 64999, "bgp_base_cidr": "bgp_base_cidr", "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "bgp_status_updated_at": "2020-08-20T06:58:41.909Z", "carrier_name": "myCarrierName", "change_request": {"type": "create_gateway"}, "completion_notice_reject_reason": "The completion notice file was blank", "connection_mode": "transit", "created_at": "2019-01-01T12:00:00.000Z", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::dedicated:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "cross_account": false, "cross_connect_router": "xcr01.dal03", "customer_name": "newCustomerName", "default_export_route_filter": "permit", "default_import_route_filter": "permit", "global": true, "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "link_status": "up", "link_status_updated_at": "2020-08-20T06:58:41.909Z", "location_display_name": "Dallas 03", "location_name": "dal03", "macsec": {"active": true, "security_policy": "must_secure", "status": "secured", "status_reasons": [{"code": "macsec_cak_failed", "message": "The `authentication_key` failed configuration.", "more_info": "https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK"}]}, "macsec_capability": "non_macsec", "metered": false, "name": "myGateway", "operational_status": "awaiting_completion_notice", "operational_status_reasons": [{"code": "authentication_key_failed", "message": "The `authentication_key` failed configuration.", "more_info": "https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK"}], "patch_panel_completion_notice": "patch panel configuration details", "port": {"id": "54321b1a-fee4-41c7-9e11-9cd99e000aaa"}, "provider_api_managed": false, "resource_group": {"id": "56969d6043e9465c883cb9f7363e78e8"}, "speed_mbps": 1000, "type": "dedicated", "vlan": 10}]}'
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
                _service.list_gateways(**req_copy)

    def test_list_gateways_value_error_with_retries(self):
        # Enable retries and run test_list_gateways_value_error.
        _service.enable_retries()
        self.test_list_gateways_value_error()

        # Disable retries and run test_list_gateways_value_error.
        _service.disable_retries()
        self.test_list_gateways_value_error()


class TestCreateGateway:
    """
    Test Class for create_gateway
    """

    @responses.activate
    def test_create_gateway_all_params(self):
        """
        create_gateway()
        """
        # Set up mock
        url = preprocess_url('/gateways')
        mock_response = '{"as_prepends": [{"created_at": "2019-01-01T12:00:00.000Z", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "length": 4, "policy": "import", "prefix": "172.17.0.0/16", "specific_prefixes": ["192.168.3.0/24"], "updated_at": "2019-01-01T12:00:00.000Z"}], "authentication_key": {"crn": "crn:v1:bluemix:public:kms:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222"}, "bfd_config": {"bfd_status": "up", "bfd_status_updated_at": "2020-08-20T06:58:41.909Z", "interval": 2000, "multiplier": 10}, "bgp_asn": 64999, "bgp_base_cidr": "bgp_base_cidr", "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "bgp_status_updated_at": "2020-08-20T06:58:41.909Z", "carrier_name": "myCarrierName", "change_request": {"type": "create_gateway"}, "completion_notice_reject_reason": "The completion notice file was blank", "connection_mode": "transit", "created_at": "2019-01-01T12:00:00.000Z", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::dedicated:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "cross_account": false, "cross_connect_router": "xcr01.dal03", "customer_name": "newCustomerName", "default_export_route_filter": "permit", "default_import_route_filter": "permit", "global": true, "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "link_status": "up", "link_status_updated_at": "2020-08-20T06:58:41.909Z", "location_display_name": "Dallas 03", "location_name": "dal03", "macsec": {"active": true, "security_policy": "must_secure", "status": "secured", "status_reasons": [{"code": "macsec_cak_failed", "message": "The `authentication_key` failed configuration.", "more_info": "https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK"}]}, "macsec_capability": "non_macsec", "metered": false, "name": "myGateway", "operational_status": "awaiting_completion_notice", "operational_status_reasons": [{"code": "authentication_key_failed", "message": "The `authentication_key` failed configuration.", "more_info": "https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK"}], "patch_panel_completion_notice": "patch panel configuration details", "port": {"id": "54321b1a-fee4-41c7-9e11-9cd99e000aaa"}, "provider_api_managed": false, "resource_group": {"id": "56969d6043e9465c883cb9f7363e78e8"}, "speed_mbps": 1000, "type": "dedicated", "vlan": 10}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a AsPrependTemplate model
        as_prepend_template_model = {}
        as_prepend_template_model['length'] = 4
        as_prepend_template_model['policy'] = 'import'
        as_prepend_template_model['prefix'] = '172.17.0.0/16'
        as_prepend_template_model['specific_prefixes'] = ['192.168.3.0/24']

        # Construct a dict representation of a AuthenticationKeyIdentityKeyProtectAuthenticationKeyIdentity model
        authentication_key_identity_model = {}
        authentication_key_identity_model['crn'] = 'crn:v1:bluemix:public:kms:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a dict representation of a GatewayBfdConfigTemplate model
        gateway_bfd_config_template_model = {}
        gateway_bfd_config_template_model['interval'] = 2000
        gateway_bfd_config_template_model['multiplier'] = 10

        # Construct a dict representation of a GatewayTemplateRouteFilter model
        gateway_template_route_filter_model = {}
        gateway_template_route_filter_model['action'] = 'permit'
        gateway_template_route_filter_model['ge'] = 25
        gateway_template_route_filter_model['le'] = 30
        gateway_template_route_filter_model['prefix'] = '192.168.100.0/24'

        # Construct a dict representation of a ResourceGroupIdentity model
        resource_group_identity_model = {}
        resource_group_identity_model['id'] = '56969d6043e9465c883cb9f7363e78e8'

        # Construct a dict representation of a HpcsKeyIdentity model
        hpcs_key_identity_model = {}
        hpcs_key_identity_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a dict representation of a GatewayMacsecCakPrototype model
        gateway_macsec_cak_prototype_model = {}
        gateway_macsec_cak_prototype_model['key'] = hpcs_key_identity_model
        gateway_macsec_cak_prototype_model['name'] = '1000'
        gateway_macsec_cak_prototype_model['session'] = 'primary'

        # Construct a dict representation of a SakRekeyPrototypeSakRekeyTimerModePrototype model
        sak_rekey_prototype_model = {}
        sak_rekey_prototype_model['interval'] = 3600
        sak_rekey_prototype_model['mode'] = 'timer'

        # Construct a dict representation of a GatewayMacsecPrototype model
        gateway_macsec_prototype_model = {}
        gateway_macsec_prototype_model['active'] = True
        gateway_macsec_prototype_model['caks'] = [gateway_macsec_cak_prototype_model]
        gateway_macsec_prototype_model['sak_rekey'] = sak_rekey_prototype_model
        gateway_macsec_prototype_model['security_policy'] = 'must_secure'
        gateway_macsec_prototype_model['window_size'] = 64

        # Construct a dict representation of a GatewayTemplateGatewayTypeDedicatedTemplate model
        gateway_template_model = {}
        gateway_template_model['as_prepends'] = [as_prepend_template_model]
        gateway_template_model['authentication_key'] = authentication_key_identity_model
        gateway_template_model['bfd_config'] = gateway_bfd_config_template_model
        gateway_template_model['bgp_asn'] = 64999
        gateway_template_model['bgp_base_cidr'] = 'testString'
        gateway_template_model['bgp_cer_cidr'] = '169.254.0.10/30'
        gateway_template_model['bgp_ibm_cidr'] = '169.254.0.9/30'
        gateway_template_model['connection_mode'] = 'transit'
        gateway_template_model['default_export_route_filter'] = 'permit'
        gateway_template_model['default_import_route_filter'] = 'permit'
        gateway_template_model['export_route_filters'] = [gateway_template_route_filter_model]
        gateway_template_model['global'] = True
        gateway_template_model['import_route_filters'] = [gateway_template_route_filter_model]
        gateway_template_model['metered'] = False
        gateway_template_model['name'] = 'myGateway'
        gateway_template_model['patch_panel_completion_notice'] = 'patch panel configuration details'
        gateway_template_model['resource_group'] = resource_group_identity_model
        gateway_template_model['speed_mbps'] = 1000
        gateway_template_model['type'] = 'dedicated'
        gateway_template_model['carrier_name'] = 'myCarrierName'
        gateway_template_model['cross_connect_router'] = 'xcr01.dal03'
        gateway_template_model['customer_name'] = 'newCustomerName'
        gateway_template_model['location_name'] = 'dal03'
        gateway_template_model['macsec'] = gateway_macsec_prototype_model
        gateway_template_model['macsec_capability'] = 'non_macsec'
        gateway_template_model['vlan'] = 10

        # Set up parameter values
        gateway_template = gateway_template_model

        # Invoke method
        response = _service.create_gateway(
            gateway_template,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == gateway_template

    def test_create_gateway_all_params_with_retries(self):
        # Enable retries and run test_create_gateway_all_params.
        _service.enable_retries()
        self.test_create_gateway_all_params()

        # Disable retries and run test_create_gateway_all_params.
        _service.disable_retries()
        self.test_create_gateway_all_params()

    @responses.activate
    def test_create_gateway_value_error(self):
        """
        test_create_gateway_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways')
        mock_response = '{"as_prepends": [{"created_at": "2019-01-01T12:00:00.000Z", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "length": 4, "policy": "import", "prefix": "172.17.0.0/16", "specific_prefixes": ["192.168.3.0/24"], "updated_at": "2019-01-01T12:00:00.000Z"}], "authentication_key": {"crn": "crn:v1:bluemix:public:kms:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222"}, "bfd_config": {"bfd_status": "up", "bfd_status_updated_at": "2020-08-20T06:58:41.909Z", "interval": 2000, "multiplier": 10}, "bgp_asn": 64999, "bgp_base_cidr": "bgp_base_cidr", "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "bgp_status_updated_at": "2020-08-20T06:58:41.909Z", "carrier_name": "myCarrierName", "change_request": {"type": "create_gateway"}, "completion_notice_reject_reason": "The completion notice file was blank", "connection_mode": "transit", "created_at": "2019-01-01T12:00:00.000Z", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::dedicated:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "cross_account": false, "cross_connect_router": "xcr01.dal03", "customer_name": "newCustomerName", "default_export_route_filter": "permit", "default_import_route_filter": "permit", "global": true, "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "link_status": "up", "link_status_updated_at": "2020-08-20T06:58:41.909Z", "location_display_name": "Dallas 03", "location_name": "dal03", "macsec": {"active": true, "security_policy": "must_secure", "status": "secured", "status_reasons": [{"code": "macsec_cak_failed", "message": "The `authentication_key` failed configuration.", "more_info": "https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK"}]}, "macsec_capability": "non_macsec", "metered": false, "name": "myGateway", "operational_status": "awaiting_completion_notice", "operational_status_reasons": [{"code": "authentication_key_failed", "message": "The `authentication_key` failed configuration.", "more_info": "https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK"}], "patch_panel_completion_notice": "patch panel configuration details", "port": {"id": "54321b1a-fee4-41c7-9e11-9cd99e000aaa"}, "provider_api_managed": false, "resource_group": {"id": "56969d6043e9465c883cb9f7363e78e8"}, "speed_mbps": 1000, "type": "dedicated", "vlan": 10}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a AsPrependTemplate model
        as_prepend_template_model = {}
        as_prepend_template_model['length'] = 4
        as_prepend_template_model['policy'] = 'import'
        as_prepend_template_model['prefix'] = '172.17.0.0/16'
        as_prepend_template_model['specific_prefixes'] = ['192.168.3.0/24']

        # Construct a dict representation of a AuthenticationKeyIdentityKeyProtectAuthenticationKeyIdentity model
        authentication_key_identity_model = {}
        authentication_key_identity_model['crn'] = 'crn:v1:bluemix:public:kms:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a dict representation of a GatewayBfdConfigTemplate model
        gateway_bfd_config_template_model = {}
        gateway_bfd_config_template_model['interval'] = 2000
        gateway_bfd_config_template_model['multiplier'] = 10

        # Construct a dict representation of a GatewayTemplateRouteFilter model
        gateway_template_route_filter_model = {}
        gateway_template_route_filter_model['action'] = 'permit'
        gateway_template_route_filter_model['ge'] = 25
        gateway_template_route_filter_model['le'] = 30
        gateway_template_route_filter_model['prefix'] = '192.168.100.0/24'

        # Construct a dict representation of a ResourceGroupIdentity model
        resource_group_identity_model = {}
        resource_group_identity_model['id'] = '56969d6043e9465c883cb9f7363e78e8'

        # Construct a dict representation of a HpcsKeyIdentity model
        hpcs_key_identity_model = {}
        hpcs_key_identity_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a dict representation of a GatewayMacsecCakPrototype model
        gateway_macsec_cak_prototype_model = {}
        gateway_macsec_cak_prototype_model['key'] = hpcs_key_identity_model
        gateway_macsec_cak_prototype_model['name'] = '1000'
        gateway_macsec_cak_prototype_model['session'] = 'primary'

        # Construct a dict representation of a SakRekeyPrototypeSakRekeyTimerModePrototype model
        sak_rekey_prototype_model = {}
        sak_rekey_prototype_model['interval'] = 3600
        sak_rekey_prototype_model['mode'] = 'timer'

        # Construct a dict representation of a GatewayMacsecPrototype model
        gateway_macsec_prototype_model = {}
        gateway_macsec_prototype_model['active'] = True
        gateway_macsec_prototype_model['caks'] = [gateway_macsec_cak_prototype_model]
        gateway_macsec_prototype_model['sak_rekey'] = sak_rekey_prototype_model
        gateway_macsec_prototype_model['security_policy'] = 'must_secure'
        gateway_macsec_prototype_model['window_size'] = 64

        # Construct a dict representation of a GatewayTemplateGatewayTypeDedicatedTemplate model
        gateway_template_model = {}
        gateway_template_model['as_prepends'] = [as_prepend_template_model]
        gateway_template_model['authentication_key'] = authentication_key_identity_model
        gateway_template_model['bfd_config'] = gateway_bfd_config_template_model
        gateway_template_model['bgp_asn'] = 64999
        gateway_template_model['bgp_base_cidr'] = 'testString'
        gateway_template_model['bgp_cer_cidr'] = '169.254.0.10/30'
        gateway_template_model['bgp_ibm_cidr'] = '169.254.0.9/30'
        gateway_template_model['connection_mode'] = 'transit'
        gateway_template_model['default_export_route_filter'] = 'permit'
        gateway_template_model['default_import_route_filter'] = 'permit'
        gateway_template_model['export_route_filters'] = [gateway_template_route_filter_model]
        gateway_template_model['global'] = True
        gateway_template_model['import_route_filters'] = [gateway_template_route_filter_model]
        gateway_template_model['metered'] = False
        gateway_template_model['name'] = 'myGateway'
        gateway_template_model['patch_panel_completion_notice'] = 'patch panel configuration details'
        gateway_template_model['resource_group'] = resource_group_identity_model
        gateway_template_model['speed_mbps'] = 1000
        gateway_template_model['type'] = 'dedicated'
        gateway_template_model['carrier_name'] = 'myCarrierName'
        gateway_template_model['cross_connect_router'] = 'xcr01.dal03'
        gateway_template_model['customer_name'] = 'newCustomerName'
        gateway_template_model['location_name'] = 'dal03'
        gateway_template_model['macsec'] = gateway_macsec_prototype_model
        gateway_template_model['macsec_capability'] = 'non_macsec'
        gateway_template_model['vlan'] = 10

        # Set up parameter values
        gateway_template = gateway_template_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "gateway_template": gateway_template,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_gateway(**req_copy)

    def test_create_gateway_value_error_with_retries(self):
        # Enable retries and run test_create_gateway_value_error.
        _service.enable_retries()
        self.test_create_gateway_value_error()

        # Disable retries and run test_create_gateway_value_error.
        _service.disable_retries()
        self.test_create_gateway_value_error()


class TestDeleteGateway:
    """
    Test Class for delete_gateway
    """

    @responses.activate
    def test_delete_gateway_all_params(self):
        """
        delete_gateway()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Invoke method
        response = _service.delete_gateway(
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_gateway_all_params_with_retries(self):
        # Enable retries and run test_delete_gateway_all_params.
        _service.enable_retries()
        self.test_delete_gateway_all_params()

        # Disable retries and run test_delete_gateway_all_params.
        _service.disable_retries()
        self.test_delete_gateway_all_params()

    @responses.activate
    def test_delete_gateway_value_error(self):
        """
        test_delete_gateway_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_gateway(**req_copy)

    def test_delete_gateway_value_error_with_retries(self):
        # Enable retries and run test_delete_gateway_value_error.
        _service.enable_retries()
        self.test_delete_gateway_value_error()

        # Disable retries and run test_delete_gateway_value_error.
        _service.disable_retries()
        self.test_delete_gateway_value_error()


class TestGetGateway:
    """
    Test Class for get_gateway
    """

    @responses.activate
    def test_get_gateway_all_params(self):
        """
        get_gateway()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28')
        mock_response = '{"as_prepends": [{"created_at": "2019-01-01T12:00:00.000Z", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "length": 4, "policy": "import", "prefix": "172.17.0.0/16", "specific_prefixes": ["192.168.3.0/24"], "updated_at": "2019-01-01T12:00:00.000Z"}], "authentication_key": {"crn": "crn:v1:bluemix:public:kms:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222"}, "bfd_config": {"bfd_status": "up", "bfd_status_updated_at": "2020-08-20T06:58:41.909Z", "interval": 2000, "multiplier": 10}, "bgp_asn": 64999, "bgp_base_cidr": "bgp_base_cidr", "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "bgp_status_updated_at": "2020-08-20T06:58:41.909Z", "carrier_name": "myCarrierName", "change_request": {"type": "create_gateway"}, "completion_notice_reject_reason": "The completion notice file was blank", "connection_mode": "transit", "created_at": "2019-01-01T12:00:00.000Z", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::dedicated:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "cross_account": false, "cross_connect_router": "xcr01.dal03", "customer_name": "newCustomerName", "default_export_route_filter": "permit", "default_import_route_filter": "permit", "global": true, "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "link_status": "up", "link_status_updated_at": "2020-08-20T06:58:41.909Z", "location_display_name": "Dallas 03", "location_name": "dal03", "macsec": {"active": true, "security_policy": "must_secure", "status": "secured", "status_reasons": [{"code": "macsec_cak_failed", "message": "The `authentication_key` failed configuration.", "more_info": "https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK"}]}, "macsec_capability": "non_macsec", "metered": false, "name": "myGateway", "operational_status": "awaiting_completion_notice", "operational_status_reasons": [{"code": "authentication_key_failed", "message": "The `authentication_key` failed configuration.", "more_info": "https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK"}], "patch_panel_completion_notice": "patch panel configuration details", "port": {"id": "54321b1a-fee4-41c7-9e11-9cd99e000aaa"}, "provider_api_managed": false, "resource_group": {"id": "56969d6043e9465c883cb9f7363e78e8"}, "speed_mbps": 1000, "type": "dedicated", "vlan": 10}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Invoke method
        response = _service.get_gateway(
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_gateway_all_params_with_retries(self):
        # Enable retries and run test_get_gateway_all_params.
        _service.enable_retries()
        self.test_get_gateway_all_params()

        # Disable retries and run test_get_gateway_all_params.
        _service.disable_retries()
        self.test_get_gateway_all_params()

    @responses.activate
    def test_get_gateway_value_error(self):
        """
        test_get_gateway_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28')
        mock_response = '{"as_prepends": [{"created_at": "2019-01-01T12:00:00.000Z", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "length": 4, "policy": "import", "prefix": "172.17.0.0/16", "specific_prefixes": ["192.168.3.0/24"], "updated_at": "2019-01-01T12:00:00.000Z"}], "authentication_key": {"crn": "crn:v1:bluemix:public:kms:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222"}, "bfd_config": {"bfd_status": "up", "bfd_status_updated_at": "2020-08-20T06:58:41.909Z", "interval": 2000, "multiplier": 10}, "bgp_asn": 64999, "bgp_base_cidr": "bgp_base_cidr", "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "bgp_status_updated_at": "2020-08-20T06:58:41.909Z", "carrier_name": "myCarrierName", "change_request": {"type": "create_gateway"}, "completion_notice_reject_reason": "The completion notice file was blank", "connection_mode": "transit", "created_at": "2019-01-01T12:00:00.000Z", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::dedicated:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "cross_account": false, "cross_connect_router": "xcr01.dal03", "customer_name": "newCustomerName", "default_export_route_filter": "permit", "default_import_route_filter": "permit", "global": true, "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "link_status": "up", "link_status_updated_at": "2020-08-20T06:58:41.909Z", "location_display_name": "Dallas 03", "location_name": "dal03", "macsec": {"active": true, "security_policy": "must_secure", "status": "secured", "status_reasons": [{"code": "macsec_cak_failed", "message": "The `authentication_key` failed configuration.", "more_info": "https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK"}]}, "macsec_capability": "non_macsec", "metered": false, "name": "myGateway", "operational_status": "awaiting_completion_notice", "operational_status_reasons": [{"code": "authentication_key_failed", "message": "The `authentication_key` failed configuration.", "more_info": "https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK"}], "patch_panel_completion_notice": "patch panel configuration details", "port": {"id": "54321b1a-fee4-41c7-9e11-9cd99e000aaa"}, "provider_api_managed": false, "resource_group": {"id": "56969d6043e9465c883cb9f7363e78e8"}, "speed_mbps": 1000, "type": "dedicated", "vlan": 10}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_gateway(**req_copy)

    def test_get_gateway_value_error_with_retries(self):
        # Enable retries and run test_get_gateway_value_error.
        _service.enable_retries()
        self.test_get_gateway_value_error()

        # Disable retries and run test_get_gateway_value_error.
        _service.disable_retries()
        self.test_get_gateway_value_error()


class TestUpdateGateway:
    """
    Test Class for update_gateway
    """

    @responses.activate
    def test_update_gateway_all_params(self):
        """
        update_gateway()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28')
        mock_response = '{"as_prepends": [{"created_at": "2019-01-01T12:00:00.000Z", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "length": 4, "policy": "import", "prefix": "172.17.0.0/16", "specific_prefixes": ["192.168.3.0/24"], "updated_at": "2019-01-01T12:00:00.000Z"}], "authentication_key": {"crn": "crn:v1:bluemix:public:kms:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222"}, "bfd_config": {"bfd_status": "up", "bfd_status_updated_at": "2020-08-20T06:58:41.909Z", "interval": 2000, "multiplier": 10}, "bgp_asn": 64999, "bgp_base_cidr": "bgp_base_cidr", "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "bgp_status_updated_at": "2020-08-20T06:58:41.909Z", "carrier_name": "myCarrierName", "change_request": {"type": "create_gateway"}, "completion_notice_reject_reason": "The completion notice file was blank", "connection_mode": "transit", "created_at": "2019-01-01T12:00:00.000Z", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::dedicated:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "cross_account": false, "cross_connect_router": "xcr01.dal03", "customer_name": "newCustomerName", "default_export_route_filter": "permit", "default_import_route_filter": "permit", "global": true, "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "link_status": "up", "link_status_updated_at": "2020-08-20T06:58:41.909Z", "location_display_name": "Dallas 03", "location_name": "dal03", "macsec": {"active": true, "security_policy": "must_secure", "status": "secured", "status_reasons": [{"code": "macsec_cak_failed", "message": "The `authentication_key` failed configuration.", "more_info": "https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK"}]}, "macsec_capability": "non_macsec", "metered": false, "name": "myGateway", "operational_status": "awaiting_completion_notice", "operational_status_reasons": [{"code": "authentication_key_failed", "message": "The `authentication_key` failed configuration.", "more_info": "https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK"}], "patch_panel_completion_notice": "patch panel configuration details", "port": {"id": "54321b1a-fee4-41c7-9e11-9cd99e000aaa"}, "provider_api_managed": false, "resource_group": {"id": "56969d6043e9465c883cb9f7363e78e8"}, "speed_mbps": 1000, "type": "dedicated", "vlan": 10}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a AuthenticationKeyIdentityKeyProtectAuthenticationKeyIdentity model
        authentication_key_identity_model = {}
        authentication_key_identity_model['crn'] = 'crn:v1:bluemix:public:kms:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a dict representation of a GatewayBfdPatchTemplate model
        gateway_bfd_patch_template_model = {}
        gateway_bfd_patch_template_model['interval'] = 2000
        gateway_bfd_patch_template_model['multiplier'] = 10

        # Construct a dict representation of a GatewayPatchTemplate model
        gateway_patch_template_model = {}
        gateway_patch_template_model['authentication_key'] = authentication_key_identity_model
        gateway_patch_template_model['bfd_config'] = gateway_bfd_patch_template_model
        gateway_patch_template_model['bgp_asn'] = 64999
        gateway_patch_template_model['bgp_cer_cidr'] = '169.254.0.10/30'
        gateway_patch_template_model['bgp_ibm_cidr'] = '169.254.0.9/30'
        gateway_patch_template_model['connection_mode'] = 'transit'
        gateway_patch_template_model['default_export_route_filter'] = 'permit'
        gateway_patch_template_model['default_import_route_filter'] = 'permit'
        gateway_patch_template_model['global'] = True
        gateway_patch_template_model['loa_reject_reason'] = 'The port mentioned was incorrect'
        gateway_patch_template_model['metered'] = False
        gateway_patch_template_model['name'] = 'testGateway'
        gateway_patch_template_model['operational_status'] = 'loa_accepted'
        gateway_patch_template_model['patch_panel_completion_notice'] = 'patch panel configuration details'
        gateway_patch_template_model['speed_mbps'] = 1000
        gateway_patch_template_model['vlan'] = 10

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        gateway_patch_template = gateway_patch_template_model

        # Invoke method
        response = _service.update_gateway(
            id,
            gateway_patch_template,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == gateway_patch_template

    def test_update_gateway_all_params_with_retries(self):
        # Enable retries and run test_update_gateway_all_params.
        _service.enable_retries()
        self.test_update_gateway_all_params()

        # Disable retries and run test_update_gateway_all_params.
        _service.disable_retries()
        self.test_update_gateway_all_params()

    @responses.activate
    def test_update_gateway_value_error(self):
        """
        test_update_gateway_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28')
        mock_response = '{"as_prepends": [{"created_at": "2019-01-01T12:00:00.000Z", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "length": 4, "policy": "import", "prefix": "172.17.0.0/16", "specific_prefixes": ["192.168.3.0/24"], "updated_at": "2019-01-01T12:00:00.000Z"}], "authentication_key": {"crn": "crn:v1:bluemix:public:kms:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222"}, "bfd_config": {"bfd_status": "up", "bfd_status_updated_at": "2020-08-20T06:58:41.909Z", "interval": 2000, "multiplier": 10}, "bgp_asn": 64999, "bgp_base_cidr": "bgp_base_cidr", "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "bgp_status_updated_at": "2020-08-20T06:58:41.909Z", "carrier_name": "myCarrierName", "change_request": {"type": "create_gateway"}, "completion_notice_reject_reason": "The completion notice file was blank", "connection_mode": "transit", "created_at": "2019-01-01T12:00:00.000Z", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::dedicated:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "cross_account": false, "cross_connect_router": "xcr01.dal03", "customer_name": "newCustomerName", "default_export_route_filter": "permit", "default_import_route_filter": "permit", "global": true, "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "link_status": "up", "link_status_updated_at": "2020-08-20T06:58:41.909Z", "location_display_name": "Dallas 03", "location_name": "dal03", "macsec": {"active": true, "security_policy": "must_secure", "status": "secured", "status_reasons": [{"code": "macsec_cak_failed", "message": "The `authentication_key` failed configuration.", "more_info": "https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK"}]}, "macsec_capability": "non_macsec", "metered": false, "name": "myGateway", "operational_status": "awaiting_completion_notice", "operational_status_reasons": [{"code": "authentication_key_failed", "message": "The `authentication_key` failed configuration.", "more_info": "https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK"}], "patch_panel_completion_notice": "patch panel configuration details", "port": {"id": "54321b1a-fee4-41c7-9e11-9cd99e000aaa"}, "provider_api_managed": false, "resource_group": {"id": "56969d6043e9465c883cb9f7363e78e8"}, "speed_mbps": 1000, "type": "dedicated", "vlan": 10}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a AuthenticationKeyIdentityKeyProtectAuthenticationKeyIdentity model
        authentication_key_identity_model = {}
        authentication_key_identity_model['crn'] = 'crn:v1:bluemix:public:kms:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a dict representation of a GatewayBfdPatchTemplate model
        gateway_bfd_patch_template_model = {}
        gateway_bfd_patch_template_model['interval'] = 2000
        gateway_bfd_patch_template_model['multiplier'] = 10

        # Construct a dict representation of a GatewayPatchTemplate model
        gateway_patch_template_model = {}
        gateway_patch_template_model['authentication_key'] = authentication_key_identity_model
        gateway_patch_template_model['bfd_config'] = gateway_bfd_patch_template_model
        gateway_patch_template_model['bgp_asn'] = 64999
        gateway_patch_template_model['bgp_cer_cidr'] = '169.254.0.10/30'
        gateway_patch_template_model['bgp_ibm_cidr'] = '169.254.0.9/30'
        gateway_patch_template_model['connection_mode'] = 'transit'
        gateway_patch_template_model['default_export_route_filter'] = 'permit'
        gateway_patch_template_model['default_import_route_filter'] = 'permit'
        gateway_patch_template_model['global'] = True
        gateway_patch_template_model['loa_reject_reason'] = 'The port mentioned was incorrect'
        gateway_patch_template_model['metered'] = False
        gateway_patch_template_model['name'] = 'testGateway'
        gateway_patch_template_model['operational_status'] = 'loa_accepted'
        gateway_patch_template_model['patch_panel_completion_notice'] = 'patch panel configuration details'
        gateway_patch_template_model['speed_mbps'] = 1000
        gateway_patch_template_model['vlan'] = 10

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        gateway_patch_template = gateway_patch_template_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "gateway_patch_template": gateway_patch_template,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_gateway(**req_copy)

    def test_update_gateway_value_error_with_retries(self):
        # Enable retries and run test_update_gateway_value_error.
        _service.enable_retries()
        self.test_update_gateway_value_error()

        # Disable retries and run test_update_gateway_value_error.
        _service.disable_retries()
        self.test_update_gateway_value_error()


class TestCreateGatewayAction:
    """
    Test Class for create_gateway_action
    """

    @responses.activate
    def test_create_gateway_action_all_params(self):
        """
        create_gateway_action()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/actions')
        mock_response = '{"as_prepends": [{"created_at": "2019-01-01T12:00:00.000Z", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "length": 4, "policy": "import", "prefix": "172.17.0.0/16", "specific_prefixes": ["192.168.3.0/24"], "updated_at": "2019-01-01T12:00:00.000Z"}], "authentication_key": {"crn": "crn:v1:bluemix:public:kms:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222"}, "bfd_config": {"bfd_status": "up", "bfd_status_updated_at": "2020-08-20T06:58:41.909Z", "interval": 2000, "multiplier": 10}, "bgp_asn": 64999, "bgp_base_cidr": "bgp_base_cidr", "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "bgp_status_updated_at": "2020-08-20T06:58:41.909Z", "carrier_name": "myCarrierName", "change_request": {"type": "create_gateway"}, "completion_notice_reject_reason": "The completion notice file was blank", "connection_mode": "transit", "created_at": "2019-01-01T12:00:00.000Z", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::dedicated:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "cross_account": false, "cross_connect_router": "xcr01.dal03", "customer_name": "newCustomerName", "default_export_route_filter": "permit", "default_import_route_filter": "permit", "global": true, "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "link_status": "up", "link_status_updated_at": "2020-08-20T06:58:41.909Z", "location_display_name": "Dallas 03", "location_name": "dal03", "macsec": {"active": true, "security_policy": "must_secure", "status": "secured", "status_reasons": [{"code": "macsec_cak_failed", "message": "The `authentication_key` failed configuration.", "more_info": "https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK"}]}, "macsec_capability": "non_macsec", "metered": false, "name": "myGateway", "operational_status": "awaiting_completion_notice", "operational_status_reasons": [{"code": "authentication_key_failed", "message": "The `authentication_key` failed configuration.", "more_info": "https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK"}], "patch_panel_completion_notice": "patch panel configuration details", "port": {"id": "54321b1a-fee4-41c7-9e11-9cd99e000aaa"}, "provider_api_managed": false, "resource_group": {"id": "56969d6043e9465c883cb9f7363e78e8"}, "speed_mbps": 1000, "type": "dedicated", "vlan": 10}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a AsPrependTemplate model
        as_prepend_template_model = {}
        as_prepend_template_model['length'] = 4
        as_prepend_template_model['policy'] = 'import'
        as_prepend_template_model['prefix'] = '172.17.0.0/16'
        as_prepend_template_model['specific_prefixes'] = ['192.168.3.0/24']

        # Construct a dict representation of a AuthenticationKeyIdentityKeyProtectAuthenticationKeyIdentity model
        authentication_key_identity_model = {}
        authentication_key_identity_model['crn'] = 'crn:v1:bluemix:public:kms:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a dict representation of a GatewayBfdConfigActionTemplate model
        gateway_bfd_config_action_template_model = {}
        gateway_bfd_config_action_template_model['interval'] = 2000
        gateway_bfd_config_action_template_model['multiplier'] = 10

        # Construct a dict representation of a GatewayTemplateRouteFilter model
        gateway_template_route_filter_model = {}
        gateway_template_route_filter_model['action'] = 'permit'
        gateway_template_route_filter_model['ge'] = 25
        gateway_template_route_filter_model['le'] = 30
        gateway_template_route_filter_model['prefix'] = '192.168.100.0/24'

        # Construct a dict representation of a ResourceGroupIdentity model
        resource_group_identity_model = {}
        resource_group_identity_model['id'] = '56969d6043e9465c883cb9f7363e78e8'

        # Construct a dict representation of a GatewayActionTemplateUpdatesItemGatewayClientSpeedUpdate model
        gateway_action_template_updates_item_model = {}
        gateway_action_template_updates_item_model['speed_mbps'] = 500

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        action = 'create_gateway_approve'
        as_prepends = [as_prepend_template_model]
        authentication_key = authentication_key_identity_model
        bfd_config = gateway_bfd_config_action_template_model
        connection_mode = 'transit'
        default_export_route_filter = 'permit'
        default_import_route_filter = 'permit'
        export_route_filters = [gateway_template_route_filter_model]
        global_ = True
        import_route_filters = [gateway_template_route_filter_model]
        metered = False
        resource_group = resource_group_identity_model
        updates = [gateway_action_template_updates_item_model]

        # Invoke method
        response = _service.create_gateway_action(
            id,
            action=action,
            as_prepends=as_prepends,
            authentication_key=authentication_key,
            bfd_config=bfd_config,
            connection_mode=connection_mode,
            default_export_route_filter=default_export_route_filter,
            default_import_route_filter=default_import_route_filter,
            export_route_filters=export_route_filters,
            global_=global_,
            import_route_filters=import_route_filters,
            metered=metered,
            resource_group=resource_group,
            updates=updates,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['action'] == 'create_gateway_approve'
        assert req_body['as_prepends'] == [as_prepend_template_model]
        assert req_body['authentication_key'] == authentication_key_identity_model
        assert req_body['bfd_config'] == gateway_bfd_config_action_template_model
        assert req_body['connection_mode'] == 'transit'
        assert req_body['default_export_route_filter'] == 'permit'
        assert req_body['default_import_route_filter'] == 'permit'
        assert req_body['export_route_filters'] == [gateway_template_route_filter_model]
        assert req_body['global'] == True
        assert req_body['import_route_filters'] == [gateway_template_route_filter_model]
        assert req_body['metered'] == False
        assert req_body['resource_group'] == resource_group_identity_model
        assert req_body['updates'] == [gateway_action_template_updates_item_model]

    def test_create_gateway_action_all_params_with_retries(self):
        # Enable retries and run test_create_gateway_action_all_params.
        _service.enable_retries()
        self.test_create_gateway_action_all_params()

        # Disable retries and run test_create_gateway_action_all_params.
        _service.disable_retries()
        self.test_create_gateway_action_all_params()

    @responses.activate
    def test_create_gateway_action_value_error(self):
        """
        test_create_gateway_action_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/actions')
        mock_response = '{"as_prepends": [{"created_at": "2019-01-01T12:00:00.000Z", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "length": 4, "policy": "import", "prefix": "172.17.0.0/16", "specific_prefixes": ["192.168.3.0/24"], "updated_at": "2019-01-01T12:00:00.000Z"}], "authentication_key": {"crn": "crn:v1:bluemix:public:kms:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222"}, "bfd_config": {"bfd_status": "up", "bfd_status_updated_at": "2020-08-20T06:58:41.909Z", "interval": 2000, "multiplier": 10}, "bgp_asn": 64999, "bgp_base_cidr": "bgp_base_cidr", "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "bgp_status_updated_at": "2020-08-20T06:58:41.909Z", "carrier_name": "myCarrierName", "change_request": {"type": "create_gateway"}, "completion_notice_reject_reason": "The completion notice file was blank", "connection_mode": "transit", "created_at": "2019-01-01T12:00:00.000Z", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::dedicated:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "cross_account": false, "cross_connect_router": "xcr01.dal03", "customer_name": "newCustomerName", "default_export_route_filter": "permit", "default_import_route_filter": "permit", "global": true, "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "link_status": "up", "link_status_updated_at": "2020-08-20T06:58:41.909Z", "location_display_name": "Dallas 03", "location_name": "dal03", "macsec": {"active": true, "security_policy": "must_secure", "status": "secured", "status_reasons": [{"code": "macsec_cak_failed", "message": "The `authentication_key` failed configuration.", "more_info": "https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK"}]}, "macsec_capability": "non_macsec", "metered": false, "name": "myGateway", "operational_status": "awaiting_completion_notice", "operational_status_reasons": [{"code": "authentication_key_failed", "message": "The `authentication_key` failed configuration.", "more_info": "https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK"}], "patch_panel_completion_notice": "patch panel configuration details", "port": {"id": "54321b1a-fee4-41c7-9e11-9cd99e000aaa"}, "provider_api_managed": false, "resource_group": {"id": "56969d6043e9465c883cb9f7363e78e8"}, "speed_mbps": 1000, "type": "dedicated", "vlan": 10}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a AsPrependTemplate model
        as_prepend_template_model = {}
        as_prepend_template_model['length'] = 4
        as_prepend_template_model['policy'] = 'import'
        as_prepend_template_model['prefix'] = '172.17.0.0/16'
        as_prepend_template_model['specific_prefixes'] = ['192.168.3.0/24']

        # Construct a dict representation of a AuthenticationKeyIdentityKeyProtectAuthenticationKeyIdentity model
        authentication_key_identity_model = {}
        authentication_key_identity_model['crn'] = 'crn:v1:bluemix:public:kms:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a dict representation of a GatewayBfdConfigActionTemplate model
        gateway_bfd_config_action_template_model = {}
        gateway_bfd_config_action_template_model['interval'] = 2000
        gateway_bfd_config_action_template_model['multiplier'] = 10

        # Construct a dict representation of a GatewayTemplateRouteFilter model
        gateway_template_route_filter_model = {}
        gateway_template_route_filter_model['action'] = 'permit'
        gateway_template_route_filter_model['ge'] = 25
        gateway_template_route_filter_model['le'] = 30
        gateway_template_route_filter_model['prefix'] = '192.168.100.0/24'

        # Construct a dict representation of a ResourceGroupIdentity model
        resource_group_identity_model = {}
        resource_group_identity_model['id'] = '56969d6043e9465c883cb9f7363e78e8'

        # Construct a dict representation of a GatewayActionTemplateUpdatesItemGatewayClientSpeedUpdate model
        gateway_action_template_updates_item_model = {}
        gateway_action_template_updates_item_model['speed_mbps'] = 500

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        action = 'create_gateway_approve'
        as_prepends = [as_prepend_template_model]
        authentication_key = authentication_key_identity_model
        bfd_config = gateway_bfd_config_action_template_model
        connection_mode = 'transit'
        default_export_route_filter = 'permit'
        default_import_route_filter = 'permit'
        export_route_filters = [gateway_template_route_filter_model]
        global_ = True
        import_route_filters = [gateway_template_route_filter_model]
        metered = False
        resource_group = resource_group_identity_model
        updates = [gateway_action_template_updates_item_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_gateway_action(**req_copy)

    def test_create_gateway_action_value_error_with_retries(self):
        # Enable retries and run test_create_gateway_action_value_error.
        _service.enable_retries()
        self.test_create_gateway_action_value_error()

        # Disable retries and run test_create_gateway_action_value_error.
        _service.disable_retries()
        self.test_create_gateway_action_value_error()


class TestListGatewayCompletionNotice:
    """
    Test Class for list_gateway_completion_notice
    """

    @responses.activate
    def test_list_gateway_completion_notice_all_params(self):
        """
        list_gateway_completion_notice()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/completion_notice')
        mock_response = 'This is a mock binary response.'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/pdf',
            status=200,
        )

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Invoke method
        response = _service.list_gateway_completion_notice(
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_gateway_completion_notice_all_params_with_retries(self):
        # Enable retries and run test_list_gateway_completion_notice_all_params.
        _service.enable_retries()
        self.test_list_gateway_completion_notice_all_params()

        # Disable retries and run test_list_gateway_completion_notice_all_params.
        _service.disable_retries()
        self.test_list_gateway_completion_notice_all_params()

    @responses.activate
    def test_list_gateway_completion_notice_value_error(self):
        """
        test_list_gateway_completion_notice_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/completion_notice')
        mock_response = 'This is a mock binary response.'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/pdf',
            status=200,
        )

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_gateway_completion_notice(**req_copy)

    def test_list_gateway_completion_notice_value_error_with_retries(self):
        # Enable retries and run test_list_gateway_completion_notice_value_error.
        _service.enable_retries()
        self.test_list_gateway_completion_notice_value_error()

        # Disable retries and run test_list_gateway_completion_notice_value_error.
        _service.disable_retries()
        self.test_list_gateway_completion_notice_value_error()


class TestCreateGatewayCompletionNotice:
    """
    Test Class for create_gateway_completion_notice
    """

    @responses.activate
    def test_create_gateway_completion_notice_all_params(self):
        """
        create_gateway_completion_notice()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/completion_notice')
        responses.add(
            responses.PUT,
            url,
            status=204,
        )

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        upload = io.BytesIO(b'This is a mock file.').getvalue()
        upload_content_type = 'testString'

        # Invoke method
        response = _service.create_gateway_completion_notice(
            id,
            upload=upload,
            upload_content_type=upload_content_type,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_create_gateway_completion_notice_all_params_with_retries(self):
        # Enable retries and run test_create_gateway_completion_notice_all_params.
        _service.enable_retries()
        self.test_create_gateway_completion_notice_all_params()

        # Disable retries and run test_create_gateway_completion_notice_all_params.
        _service.disable_retries()
        self.test_create_gateway_completion_notice_all_params()

    @responses.activate
    def test_create_gateway_completion_notice_required_params(self):
        """
        test_create_gateway_completion_notice_required_params()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/completion_notice')
        responses.add(
            responses.PUT,
            url,
            status=204,
        )

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Invoke method
        response = _service.create_gateway_completion_notice(
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_create_gateway_completion_notice_required_params_with_retries(self):
        # Enable retries and run test_create_gateway_completion_notice_required_params.
        _service.enable_retries()
        self.test_create_gateway_completion_notice_required_params()

        # Disable retries and run test_create_gateway_completion_notice_required_params.
        _service.disable_retries()
        self.test_create_gateway_completion_notice_required_params()

    @responses.activate
    def test_create_gateway_completion_notice_value_error(self):
        """
        test_create_gateway_completion_notice_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/completion_notice')
        responses.add(
            responses.PUT,
            url,
            status=204,
        )

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_gateway_completion_notice(**req_copy)

    def test_create_gateway_completion_notice_value_error_with_retries(self):
        # Enable retries and run test_create_gateway_completion_notice_value_error.
        _service.enable_retries()
        self.test_create_gateway_completion_notice_value_error()

        # Disable retries and run test_create_gateway_completion_notice_value_error.
        _service.disable_retries()
        self.test_create_gateway_completion_notice_value_error()


class TestListGatewayLetterOfAuthorization:
    """
    Test Class for list_gateway_letter_of_authorization
    """

    @responses.activate
    def test_list_gateway_letter_of_authorization_all_params(self):
        """
        list_gateway_letter_of_authorization()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/letter_of_authorization')
        mock_response = 'This is a mock binary response.'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/pdf',
            status=200,
        )

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Invoke method
        response = _service.list_gateway_letter_of_authorization(
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_gateway_letter_of_authorization_all_params_with_retries(self):
        # Enable retries and run test_list_gateway_letter_of_authorization_all_params.
        _service.enable_retries()
        self.test_list_gateway_letter_of_authorization_all_params()

        # Disable retries and run test_list_gateway_letter_of_authorization_all_params.
        _service.disable_retries()
        self.test_list_gateway_letter_of_authorization_all_params()

    @responses.activate
    def test_list_gateway_letter_of_authorization_value_error(self):
        """
        test_list_gateway_letter_of_authorization_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/letter_of_authorization')
        mock_response = 'This is a mock binary response.'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/pdf',
            status=200,
        )

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_gateway_letter_of_authorization(**req_copy)

    def test_list_gateway_letter_of_authorization_value_error_with_retries(self):
        # Enable retries and run test_list_gateway_letter_of_authorization_value_error.
        _service.enable_retries()
        self.test_list_gateway_letter_of_authorization_value_error()

        # Disable retries and run test_list_gateway_letter_of_authorization_value_error.
        _service.disable_retries()
        self.test_list_gateway_letter_of_authorization_value_error()


class TestGetGatewayStatistics:
    """
    Test Class for get_gateway_statistics
    """

    @responses.activate
    def test_get_gateway_statistics_all_params(self):
        """
        get_gateway_statistics()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/statistics')
        mock_response = '{"statistics": [{"created_at": "2020-08-20T06:58:41.909Z", "data": "MKA statistics text...", "type": "macsec_policy"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        type = 'macsec_mka_session'

        # Invoke method
        response = _service.get_gateway_statistics(
            id,
            type,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'type={}'.format(type) in query_string

    def test_get_gateway_statistics_all_params_with_retries(self):
        # Enable retries and run test_get_gateway_statistics_all_params.
        _service.enable_retries()
        self.test_get_gateway_statistics_all_params()

        # Disable retries and run test_get_gateway_statistics_all_params.
        _service.disable_retries()
        self.test_get_gateway_statistics_all_params()

    @responses.activate
    def test_get_gateway_statistics_value_error(self):
        """
        test_get_gateway_statistics_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/statistics')
        mock_response = '{"statistics": [{"created_at": "2020-08-20T06:58:41.909Z", "data": "MKA statistics text...", "type": "macsec_policy"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        type = 'macsec_mka_session'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "type": type,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_gateway_statistics(**req_copy)

    def test_get_gateway_statistics_value_error_with_retries(self):
        # Enable retries and run test_get_gateway_statistics_value_error.
        _service.enable_retries()
        self.test_get_gateway_statistics_value_error()

        # Disable retries and run test_get_gateway_statistics_value_error.
        _service.disable_retries()
        self.test_get_gateway_statistics_value_error()


class TestGetGatewayStatus:
    """
    Test Class for get_gateway_status
    """

    @responses.activate
    def test_get_gateway_status_all_params(self):
        """
        get_gateway_status()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/status')
        mock_response = '{"status": [{"type": "bgp", "updated_at": "2020-08-20T06:58:41.909Z", "value": "active"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        type = 'bgp'

        # Invoke method
        response = _service.get_gateway_status(
            id,
            type=type,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'type={}'.format(type) in query_string

    def test_get_gateway_status_all_params_with_retries(self):
        # Enable retries and run test_get_gateway_status_all_params.
        _service.enable_retries()
        self.test_get_gateway_status_all_params()

        # Disable retries and run test_get_gateway_status_all_params.
        _service.disable_retries()
        self.test_get_gateway_status_all_params()

    @responses.activate
    def test_get_gateway_status_required_params(self):
        """
        test_get_gateway_status_required_params()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/status')
        mock_response = '{"status": [{"type": "bgp", "updated_at": "2020-08-20T06:58:41.909Z", "value": "active"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Invoke method
        response = _service.get_gateway_status(
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_gateway_status_required_params_with_retries(self):
        # Enable retries and run test_get_gateway_status_required_params.
        _service.enable_retries()
        self.test_get_gateway_status_required_params()

        # Disable retries and run test_get_gateway_status_required_params.
        _service.disable_retries()
        self.test_get_gateway_status_required_params()

    @responses.activate
    def test_get_gateway_status_value_error(self):
        """
        test_get_gateway_status_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/status')
        mock_response = '{"status": [{"type": "bgp", "updated_at": "2020-08-20T06:58:41.909Z", "value": "active"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_gateway_status(**req_copy)

    def test_get_gateway_status_value_error_with_retries(self):
        # Enable retries and run test_get_gateway_status_value_error.
        _service.enable_retries()
        self.test_get_gateway_status_value_error()

        # Disable retries and run test_get_gateway_status_value_error.
        _service.disable_retries()
        self.test_get_gateway_status_value_error()


# endregion
##############################################################################
# End of Service: Gateways
##############################################################################

##############################################################################
# Start of Service: GatewayASPrepends
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

        service = DirectLinkV1.new_instance(
            version=version,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DirectLinkV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DirectLinkV1.new_instance(
                version=version,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = DirectLinkV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='version must be provided'):
            service = DirectLinkV1.new_instance(
                version=None,
            )


class TestListGatewayAsPrepends:
    """
    Test Class for list_gateway_as_prepends
    """

    @responses.activate
    def test_list_gateway_as_prepends_all_params(self):
        """
        list_gateway_as_prepends()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/as_prepends')
        mock_response = '{"as_prepends": [{"created_at": "2019-01-01T12:00:00.000Z", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "length": 4, "policy": "import", "specific_prefixes": ["192.168.3.0/24"], "updated_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Invoke method
        response = _service.list_gateway_as_prepends(
            gateway_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_gateway_as_prepends_all_params_with_retries(self):
        # Enable retries and run test_list_gateway_as_prepends_all_params.
        _service.enable_retries()
        self.test_list_gateway_as_prepends_all_params()

        # Disable retries and run test_list_gateway_as_prepends_all_params.
        _service.disable_retries()
        self.test_list_gateway_as_prepends_all_params()

    @responses.activate
    def test_list_gateway_as_prepends_value_error(self):
        """
        test_list_gateway_as_prepends_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/as_prepends')
        mock_response = '{"as_prepends": [{"created_at": "2019-01-01T12:00:00.000Z", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "length": 4, "policy": "import", "specific_prefixes": ["192.168.3.0/24"], "updated_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "gateway_id": gateway_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_gateway_as_prepends(**req_copy)

    def test_list_gateway_as_prepends_value_error_with_retries(self):
        # Enable retries and run test_list_gateway_as_prepends_value_error.
        _service.enable_retries()
        self.test_list_gateway_as_prepends_value_error()

        # Disable retries and run test_list_gateway_as_prepends_value_error.
        _service.disable_retries()
        self.test_list_gateway_as_prepends_value_error()


class TestReplaceGatewayAsPrepends:
    """
    Test Class for replace_gateway_as_prepends
    """

    @responses.activate
    def test_replace_gateway_as_prepends_all_params(self):
        """
        replace_gateway_as_prepends()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/as_prepends')
        mock_response = '{"as_prepends": [{"created_at": "2019-01-01T12:00:00.000Z", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "length": 4, "policy": "import", "specific_prefixes": ["192.168.3.0/24"], "updated_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a AsPrependPrefixArrayTemplate model
        as_prepend_prefix_array_template_model = {}
        as_prepend_prefix_array_template_model['length'] = 4
        as_prepend_prefix_array_template_model['policy'] = 'import'
        as_prepend_prefix_array_template_model['specific_prefixes'] = ['192.168.3.0/24']

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        if_match = 'W/"96d225c4-56bd-43d9-98fc-d7148e5c5028"'
        as_prepends = [as_prepend_prefix_array_template_model]

        # Invoke method
        response = _service.replace_gateway_as_prepends(
            gateway_id,
            if_match,
            as_prepends=as_prepends,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['as_prepends'] == [as_prepend_prefix_array_template_model]

    def test_replace_gateway_as_prepends_all_params_with_retries(self):
        # Enable retries and run test_replace_gateway_as_prepends_all_params.
        _service.enable_retries()
        self.test_replace_gateway_as_prepends_all_params()

        # Disable retries and run test_replace_gateway_as_prepends_all_params.
        _service.disable_retries()
        self.test_replace_gateway_as_prepends_all_params()

    @responses.activate
    def test_replace_gateway_as_prepends_value_error(self):
        """
        test_replace_gateway_as_prepends_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/as_prepends')
        mock_response = '{"as_prepends": [{"created_at": "2019-01-01T12:00:00.000Z", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "length": 4, "policy": "import", "specific_prefixes": ["192.168.3.0/24"], "updated_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a AsPrependPrefixArrayTemplate model
        as_prepend_prefix_array_template_model = {}
        as_prepend_prefix_array_template_model['length'] = 4
        as_prepend_prefix_array_template_model['policy'] = 'import'
        as_prepend_prefix_array_template_model['specific_prefixes'] = ['192.168.3.0/24']

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        if_match = 'W/"96d225c4-56bd-43d9-98fc-d7148e5c5028"'
        as_prepends = [as_prepend_prefix_array_template_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "gateway_id": gateway_id,
            "if_match": if_match,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_gateway_as_prepends(**req_copy)

    def test_replace_gateway_as_prepends_value_error_with_retries(self):
        # Enable retries and run test_replace_gateway_as_prepends_value_error.
        _service.enable_retries()
        self.test_replace_gateway_as_prepends_value_error()

        # Disable retries and run test_replace_gateway_as_prepends_value_error.
        _service.disable_retries()
        self.test_replace_gateway_as_prepends_value_error()


# endregion
##############################################################################
# End of Service: GatewayASPrepends
##############################################################################

##############################################################################
# Start of Service: GatewayExportRouteFilters
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

        service = DirectLinkV1.new_instance(
            version=version,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DirectLinkV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DirectLinkV1.new_instance(
                version=version,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = DirectLinkV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='version must be provided'):
            service = DirectLinkV1.new_instance(
                version=None,
            )


class TestListGatewayExportRouteFilters:
    """
    Test Class for list_gateway_export_route_filters
    """

    @responses.activate
    def test_list_gateway_export_route_filters_all_params(self):
        """
        list_gateway_export_route_filters()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/export_route_filters')
        mock_response = '{"export_route_filters": [{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2020-11-02T20:40:29.622Z", "ge": 25, "id": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "le": 30, "prefix": "192.168.100.0/24", "updated_at": "2020-11-02T20:40:29.622Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Invoke method
        response = _service.list_gateway_export_route_filters(
            gateway_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_gateway_export_route_filters_all_params_with_retries(self):
        # Enable retries and run test_list_gateway_export_route_filters_all_params.
        _service.enable_retries()
        self.test_list_gateway_export_route_filters_all_params()

        # Disable retries and run test_list_gateway_export_route_filters_all_params.
        _service.disable_retries()
        self.test_list_gateway_export_route_filters_all_params()

    @responses.activate
    def test_list_gateway_export_route_filters_value_error(self):
        """
        test_list_gateway_export_route_filters_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/export_route_filters')
        mock_response = '{"export_route_filters": [{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2020-11-02T20:40:29.622Z", "ge": 25, "id": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "le": 30, "prefix": "192.168.100.0/24", "updated_at": "2020-11-02T20:40:29.622Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "gateway_id": gateway_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_gateway_export_route_filters(**req_copy)

    def test_list_gateway_export_route_filters_value_error_with_retries(self):
        # Enable retries and run test_list_gateway_export_route_filters_value_error.
        _service.enable_retries()
        self.test_list_gateway_export_route_filters_value_error()

        # Disable retries and run test_list_gateway_export_route_filters_value_error.
        _service.disable_retries()
        self.test_list_gateway_export_route_filters_value_error()


class TestCreateGatewayExportRouteFilter:
    """
    Test Class for create_gateway_export_route_filter
    """

    @responses.activate
    def test_create_gateway_export_route_filter_all_params(self):
        """
        create_gateway_export_route_filter()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/export_route_filters')
        mock_response = '{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2020-11-02T20:40:29.622Z", "ge": 25, "id": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "le": 30, "prefix": "192.168.100.0/24", "updated_at": "2020-11-02T20:40:29.622Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        action = 'permit'
        prefix = '192.168.100.0/24'
        before = '1a15dcab-7e40-45e1-b7c5-bc690eaa9782'
        ge = 25
        le = 30

        # Invoke method
        response = _service.create_gateway_export_route_filter(
            gateway_id,
            action,
            prefix,
            before=before,
            ge=ge,
            le=le,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['action'] == 'permit'
        assert req_body['prefix'] == '192.168.100.0/24'
        assert req_body['before'] == '1a15dcab-7e40-45e1-b7c5-bc690eaa9782'
        assert req_body['ge'] == 25
        assert req_body['le'] == 30

    def test_create_gateway_export_route_filter_all_params_with_retries(self):
        # Enable retries and run test_create_gateway_export_route_filter_all_params.
        _service.enable_retries()
        self.test_create_gateway_export_route_filter_all_params()

        # Disable retries and run test_create_gateway_export_route_filter_all_params.
        _service.disable_retries()
        self.test_create_gateway_export_route_filter_all_params()

    @responses.activate
    def test_create_gateway_export_route_filter_value_error(self):
        """
        test_create_gateway_export_route_filter_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/export_route_filters')
        mock_response = '{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2020-11-02T20:40:29.622Z", "ge": 25, "id": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "le": 30, "prefix": "192.168.100.0/24", "updated_at": "2020-11-02T20:40:29.622Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        action = 'permit'
        prefix = '192.168.100.0/24'
        before = '1a15dcab-7e40-45e1-b7c5-bc690eaa9782'
        ge = 25
        le = 30

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "gateway_id": gateway_id,
            "action": action,
            "prefix": prefix,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_gateway_export_route_filter(**req_copy)

    def test_create_gateway_export_route_filter_value_error_with_retries(self):
        # Enable retries and run test_create_gateway_export_route_filter_value_error.
        _service.enable_retries()
        self.test_create_gateway_export_route_filter_value_error()

        # Disable retries and run test_create_gateway_export_route_filter_value_error.
        _service.disable_retries()
        self.test_create_gateway_export_route_filter_value_error()


class TestReplaceGatewayExportRouteFilters:
    """
    Test Class for replace_gateway_export_route_filters
    """

    @responses.activate
    def test_replace_gateway_export_route_filters_all_params(self):
        """
        replace_gateway_export_route_filters()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/export_route_filters')
        mock_response = '{"export_route_filters": [{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2020-11-02T20:40:29.622Z", "ge": 25, "id": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "le": 30, "prefix": "192.168.100.0/24", "updated_at": "2020-11-02T20:40:29.622Z"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a GatewayTemplateRouteFilter model
        gateway_template_route_filter_model = {}
        gateway_template_route_filter_model['action'] = 'permit'
        gateway_template_route_filter_model['ge'] = 25
        gateway_template_route_filter_model['le'] = 30
        gateway_template_route_filter_model['prefix'] = '192.168.100.0/24'

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        if_match = 'W/"96d225c4-56bd-43d9-98fc-d7148e5c5028"'
        export_route_filters = [gateway_template_route_filter_model]

        # Invoke method
        response = _service.replace_gateway_export_route_filters(
            gateway_id,
            if_match,
            export_route_filters=export_route_filters,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['export_route_filters'] == [gateway_template_route_filter_model]

    def test_replace_gateway_export_route_filters_all_params_with_retries(self):
        # Enable retries and run test_replace_gateway_export_route_filters_all_params.
        _service.enable_retries()
        self.test_replace_gateway_export_route_filters_all_params()

        # Disable retries and run test_replace_gateway_export_route_filters_all_params.
        _service.disable_retries()
        self.test_replace_gateway_export_route_filters_all_params()

    @responses.activate
    def test_replace_gateway_export_route_filters_required_params(self):
        """
        test_replace_gateway_export_route_filters_required_params()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/export_route_filters')
        mock_response = '{"export_route_filters": [{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2020-11-02T20:40:29.622Z", "ge": 25, "id": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "le": 30, "prefix": "192.168.100.0/24", "updated_at": "2020-11-02T20:40:29.622Z"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        if_match = 'W/"96d225c4-56bd-43d9-98fc-d7148e5c5028"'

        # Invoke method
        response = _service.replace_gateway_export_route_filters(
            gateway_id,
            if_match,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_replace_gateway_export_route_filters_required_params_with_retries(self):
        # Enable retries and run test_replace_gateway_export_route_filters_required_params.
        _service.enable_retries()
        self.test_replace_gateway_export_route_filters_required_params()

        # Disable retries and run test_replace_gateway_export_route_filters_required_params.
        _service.disable_retries()
        self.test_replace_gateway_export_route_filters_required_params()

    @responses.activate
    def test_replace_gateway_export_route_filters_value_error(self):
        """
        test_replace_gateway_export_route_filters_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/export_route_filters')
        mock_response = '{"export_route_filters": [{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2020-11-02T20:40:29.622Z", "ge": 25, "id": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "le": 30, "prefix": "192.168.100.0/24", "updated_at": "2020-11-02T20:40:29.622Z"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        if_match = 'W/"96d225c4-56bd-43d9-98fc-d7148e5c5028"'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "gateway_id": gateway_id,
            "if_match": if_match,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_gateway_export_route_filters(**req_copy)

    def test_replace_gateway_export_route_filters_value_error_with_retries(self):
        # Enable retries and run test_replace_gateway_export_route_filters_value_error.
        _service.enable_retries()
        self.test_replace_gateway_export_route_filters_value_error()

        # Disable retries and run test_replace_gateway_export_route_filters_value_error.
        _service.disable_retries()
        self.test_replace_gateway_export_route_filters_value_error()


class TestDeleteGatewayExportRouteFilter:
    """
    Test Class for delete_gateway_export_route_filter
    """

    @responses.activate
    def test_delete_gateway_export_route_filter_all_params(self):
        """
        delete_gateway_export_route_filter()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/export_route_filters/0a06fb9b-820f-4c44-8a31-77f1f0806d28')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Invoke method
        response = _service.delete_gateway_export_route_filter(
            gateway_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_gateway_export_route_filter_all_params_with_retries(self):
        # Enable retries and run test_delete_gateway_export_route_filter_all_params.
        _service.enable_retries()
        self.test_delete_gateway_export_route_filter_all_params()

        # Disable retries and run test_delete_gateway_export_route_filter_all_params.
        _service.disable_retries()
        self.test_delete_gateway_export_route_filter_all_params()

    @responses.activate
    def test_delete_gateway_export_route_filter_value_error(self):
        """
        test_delete_gateway_export_route_filter_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/export_route_filters/0a06fb9b-820f-4c44-8a31-77f1f0806d28')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "gateway_id": gateway_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_gateway_export_route_filter(**req_copy)

    def test_delete_gateway_export_route_filter_value_error_with_retries(self):
        # Enable retries and run test_delete_gateway_export_route_filter_value_error.
        _service.enable_retries()
        self.test_delete_gateway_export_route_filter_value_error()

        # Disable retries and run test_delete_gateway_export_route_filter_value_error.
        _service.disable_retries()
        self.test_delete_gateway_export_route_filter_value_error()


class TestGetGatewayExportRouteFilter:
    """
    Test Class for get_gateway_export_route_filter
    """

    @responses.activate
    def test_get_gateway_export_route_filter_all_params(self):
        """
        get_gateway_export_route_filter()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/export_route_filters/0a06fb9b-820f-4c44-8a31-77f1f0806d28')
        mock_response = '{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2020-11-02T20:40:29.622Z", "ge": 25, "id": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "le": 30, "prefix": "192.168.100.0/24", "updated_at": "2020-11-02T20:40:29.622Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Invoke method
        response = _service.get_gateway_export_route_filter(
            gateway_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_gateway_export_route_filter_all_params_with_retries(self):
        # Enable retries and run test_get_gateway_export_route_filter_all_params.
        _service.enable_retries()
        self.test_get_gateway_export_route_filter_all_params()

        # Disable retries and run test_get_gateway_export_route_filter_all_params.
        _service.disable_retries()
        self.test_get_gateway_export_route_filter_all_params()

    @responses.activate
    def test_get_gateway_export_route_filter_value_error(self):
        """
        test_get_gateway_export_route_filter_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/export_route_filters/0a06fb9b-820f-4c44-8a31-77f1f0806d28')
        mock_response = '{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2020-11-02T20:40:29.622Z", "ge": 25, "id": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "le": 30, "prefix": "192.168.100.0/24", "updated_at": "2020-11-02T20:40:29.622Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "gateway_id": gateway_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_gateway_export_route_filter(**req_copy)

    def test_get_gateway_export_route_filter_value_error_with_retries(self):
        # Enable retries and run test_get_gateway_export_route_filter_value_error.
        _service.enable_retries()
        self.test_get_gateway_export_route_filter_value_error()

        # Disable retries and run test_get_gateway_export_route_filter_value_error.
        _service.disable_retries()
        self.test_get_gateway_export_route_filter_value_error()


class TestUpdateGatewayExportRouteFilter:
    """
    Test Class for update_gateway_export_route_filter
    """

    @responses.activate
    def test_update_gateway_export_route_filter_all_params(self):
        """
        update_gateway_export_route_filter()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/export_route_filters/0a06fb9b-820f-4c44-8a31-77f1f0806d28')
        mock_response = '{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2020-11-02T20:40:29.622Z", "ge": 25, "id": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "le": 30, "prefix": "192.168.100.0/24", "updated_at": "2020-11-02T20:40:29.622Z"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a UpdateRouteFilterTemplate model
        update_route_filter_template_model = {}
        update_route_filter_template_model['action'] = 'permit'
        update_route_filter_template_model['before'] = '1a15dcab-7e40-45e1-b7c5-bc690eaa9782'
        update_route_filter_template_model['ge'] = 25
        update_route_filter_template_model['le'] = 30
        update_route_filter_template_model['prefix'] = '192.168.100.0/24'

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        update_route_filter_template = update_route_filter_template_model

        # Invoke method
        response = _service.update_gateway_export_route_filter(
            gateway_id,
            id,
            update_route_filter_template,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == update_route_filter_template

    def test_update_gateway_export_route_filter_all_params_with_retries(self):
        # Enable retries and run test_update_gateway_export_route_filter_all_params.
        _service.enable_retries()
        self.test_update_gateway_export_route_filter_all_params()

        # Disable retries and run test_update_gateway_export_route_filter_all_params.
        _service.disable_retries()
        self.test_update_gateway_export_route_filter_all_params()

    @responses.activate
    def test_update_gateway_export_route_filter_value_error(self):
        """
        test_update_gateway_export_route_filter_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/export_route_filters/0a06fb9b-820f-4c44-8a31-77f1f0806d28')
        mock_response = '{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2020-11-02T20:40:29.622Z", "ge": 25, "id": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "le": 30, "prefix": "192.168.100.0/24", "updated_at": "2020-11-02T20:40:29.622Z"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a UpdateRouteFilterTemplate model
        update_route_filter_template_model = {}
        update_route_filter_template_model['action'] = 'permit'
        update_route_filter_template_model['before'] = '1a15dcab-7e40-45e1-b7c5-bc690eaa9782'
        update_route_filter_template_model['ge'] = 25
        update_route_filter_template_model['le'] = 30
        update_route_filter_template_model['prefix'] = '192.168.100.0/24'

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        update_route_filter_template = update_route_filter_template_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "gateway_id": gateway_id,
            "id": id,
            "update_route_filter_template": update_route_filter_template,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_gateway_export_route_filter(**req_copy)

    def test_update_gateway_export_route_filter_value_error_with_retries(self):
        # Enable retries and run test_update_gateway_export_route_filter_value_error.
        _service.enable_retries()
        self.test_update_gateway_export_route_filter_value_error()

        # Disable retries and run test_update_gateway_export_route_filter_value_error.
        _service.disable_retries()
        self.test_update_gateway_export_route_filter_value_error()


# endregion
##############################################################################
# End of Service: GatewayExportRouteFilters
##############################################################################

##############################################################################
# Start of Service: GatewayImportRouteFilters
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

        service = DirectLinkV1.new_instance(
            version=version,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DirectLinkV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DirectLinkV1.new_instance(
                version=version,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = DirectLinkV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='version must be provided'):
            service = DirectLinkV1.new_instance(
                version=None,
            )


class TestListGatewayImportRouteFilters:
    """
    Test Class for list_gateway_import_route_filters
    """

    @responses.activate
    def test_list_gateway_import_route_filters_all_params(self):
        """
        list_gateway_import_route_filters()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/import_route_filters')
        mock_response = '{"import_route_filters": [{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2020-11-02T20:40:29.622Z", "ge": 25, "id": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "le": 30, "prefix": "192.168.100.0/24", "updated_at": "2020-11-02T20:40:29.622Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Invoke method
        response = _service.list_gateway_import_route_filters(
            gateway_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_gateway_import_route_filters_all_params_with_retries(self):
        # Enable retries and run test_list_gateway_import_route_filters_all_params.
        _service.enable_retries()
        self.test_list_gateway_import_route_filters_all_params()

        # Disable retries and run test_list_gateway_import_route_filters_all_params.
        _service.disable_retries()
        self.test_list_gateway_import_route_filters_all_params()

    @responses.activate
    def test_list_gateway_import_route_filters_value_error(self):
        """
        test_list_gateway_import_route_filters_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/import_route_filters')
        mock_response = '{"import_route_filters": [{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2020-11-02T20:40:29.622Z", "ge": 25, "id": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "le": 30, "prefix": "192.168.100.0/24", "updated_at": "2020-11-02T20:40:29.622Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "gateway_id": gateway_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_gateway_import_route_filters(**req_copy)

    def test_list_gateway_import_route_filters_value_error_with_retries(self):
        # Enable retries and run test_list_gateway_import_route_filters_value_error.
        _service.enable_retries()
        self.test_list_gateway_import_route_filters_value_error()

        # Disable retries and run test_list_gateway_import_route_filters_value_error.
        _service.disable_retries()
        self.test_list_gateway_import_route_filters_value_error()


class TestCreateGatewayImportRouteFilter:
    """
    Test Class for create_gateway_import_route_filter
    """

    @responses.activate
    def test_create_gateway_import_route_filter_all_params(self):
        """
        create_gateway_import_route_filter()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/import_route_filters')
        mock_response = '{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2020-11-02T20:40:29.622Z", "ge": 25, "id": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "le": 30, "prefix": "192.168.100.0/24", "updated_at": "2020-11-02T20:40:29.622Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        action = 'permit'
        prefix = '192.168.100.0/24'
        before = '1a15dcab-7e40-45e1-b7c5-bc690eaa9782'
        ge = 25
        le = 30

        # Invoke method
        response = _service.create_gateway_import_route_filter(
            gateway_id,
            action,
            prefix,
            before=before,
            ge=ge,
            le=le,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['action'] == 'permit'
        assert req_body['prefix'] == '192.168.100.0/24'
        assert req_body['before'] == '1a15dcab-7e40-45e1-b7c5-bc690eaa9782'
        assert req_body['ge'] == 25
        assert req_body['le'] == 30

    def test_create_gateway_import_route_filter_all_params_with_retries(self):
        # Enable retries and run test_create_gateway_import_route_filter_all_params.
        _service.enable_retries()
        self.test_create_gateway_import_route_filter_all_params()

        # Disable retries and run test_create_gateway_import_route_filter_all_params.
        _service.disable_retries()
        self.test_create_gateway_import_route_filter_all_params()

    @responses.activate
    def test_create_gateway_import_route_filter_value_error(self):
        """
        test_create_gateway_import_route_filter_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/import_route_filters')
        mock_response = '{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2020-11-02T20:40:29.622Z", "ge": 25, "id": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "le": 30, "prefix": "192.168.100.0/24", "updated_at": "2020-11-02T20:40:29.622Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        action = 'permit'
        prefix = '192.168.100.0/24'
        before = '1a15dcab-7e40-45e1-b7c5-bc690eaa9782'
        ge = 25
        le = 30

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "gateway_id": gateway_id,
            "action": action,
            "prefix": prefix,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_gateway_import_route_filter(**req_copy)

    def test_create_gateway_import_route_filter_value_error_with_retries(self):
        # Enable retries and run test_create_gateway_import_route_filter_value_error.
        _service.enable_retries()
        self.test_create_gateway_import_route_filter_value_error()

        # Disable retries and run test_create_gateway_import_route_filter_value_error.
        _service.disable_retries()
        self.test_create_gateway_import_route_filter_value_error()


class TestReplaceGatewayImportRouteFilters:
    """
    Test Class for replace_gateway_import_route_filters
    """

    @responses.activate
    def test_replace_gateway_import_route_filters_all_params(self):
        """
        replace_gateway_import_route_filters()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/import_route_filters')
        mock_response = '{"import_route_filters": [{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2020-11-02T20:40:29.622Z", "ge": 25, "id": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "le": 30, "prefix": "192.168.100.0/24", "updated_at": "2020-11-02T20:40:29.622Z"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a GatewayTemplateRouteFilter model
        gateway_template_route_filter_model = {}
        gateway_template_route_filter_model['action'] = 'permit'
        gateway_template_route_filter_model['ge'] = 25
        gateway_template_route_filter_model['le'] = 30
        gateway_template_route_filter_model['prefix'] = '192.168.100.0/24'

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        if_match = 'W/"96d225c4-56bd-43d9-98fc-d7148e5c5028"'
        import_route_filters = [gateway_template_route_filter_model]

        # Invoke method
        response = _service.replace_gateway_import_route_filters(
            gateway_id,
            if_match,
            import_route_filters=import_route_filters,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['import_route_filters'] == [gateway_template_route_filter_model]

    def test_replace_gateway_import_route_filters_all_params_with_retries(self):
        # Enable retries and run test_replace_gateway_import_route_filters_all_params.
        _service.enable_retries()
        self.test_replace_gateway_import_route_filters_all_params()

        # Disable retries and run test_replace_gateway_import_route_filters_all_params.
        _service.disable_retries()
        self.test_replace_gateway_import_route_filters_all_params()

    @responses.activate
    def test_replace_gateway_import_route_filters_required_params(self):
        """
        test_replace_gateway_import_route_filters_required_params()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/import_route_filters')
        mock_response = '{"import_route_filters": [{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2020-11-02T20:40:29.622Z", "ge": 25, "id": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "le": 30, "prefix": "192.168.100.0/24", "updated_at": "2020-11-02T20:40:29.622Z"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        if_match = 'W/"96d225c4-56bd-43d9-98fc-d7148e5c5028"'

        # Invoke method
        response = _service.replace_gateway_import_route_filters(
            gateway_id,
            if_match,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_replace_gateway_import_route_filters_required_params_with_retries(self):
        # Enable retries and run test_replace_gateway_import_route_filters_required_params.
        _service.enable_retries()
        self.test_replace_gateway_import_route_filters_required_params()

        # Disable retries and run test_replace_gateway_import_route_filters_required_params.
        _service.disable_retries()
        self.test_replace_gateway_import_route_filters_required_params()

    @responses.activate
    def test_replace_gateway_import_route_filters_value_error(self):
        """
        test_replace_gateway_import_route_filters_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/import_route_filters')
        mock_response = '{"import_route_filters": [{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2020-11-02T20:40:29.622Z", "ge": 25, "id": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "le": 30, "prefix": "192.168.100.0/24", "updated_at": "2020-11-02T20:40:29.622Z"}]}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        if_match = 'W/"96d225c4-56bd-43d9-98fc-d7148e5c5028"'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "gateway_id": gateway_id,
            "if_match": if_match,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_gateway_import_route_filters(**req_copy)

    def test_replace_gateway_import_route_filters_value_error_with_retries(self):
        # Enable retries and run test_replace_gateway_import_route_filters_value_error.
        _service.enable_retries()
        self.test_replace_gateway_import_route_filters_value_error()

        # Disable retries and run test_replace_gateway_import_route_filters_value_error.
        _service.disable_retries()
        self.test_replace_gateway_import_route_filters_value_error()


class TestDeleteGatewayImportRouteFilter:
    """
    Test Class for delete_gateway_import_route_filter
    """

    @responses.activate
    def test_delete_gateway_import_route_filter_all_params(self):
        """
        delete_gateway_import_route_filter()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/import_route_filters/0a06fb9b-820f-4c44-8a31-77f1f0806d28')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Invoke method
        response = _service.delete_gateway_import_route_filter(
            gateway_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_gateway_import_route_filter_all_params_with_retries(self):
        # Enable retries and run test_delete_gateway_import_route_filter_all_params.
        _service.enable_retries()
        self.test_delete_gateway_import_route_filter_all_params()

        # Disable retries and run test_delete_gateway_import_route_filter_all_params.
        _service.disable_retries()
        self.test_delete_gateway_import_route_filter_all_params()

    @responses.activate
    def test_delete_gateway_import_route_filter_value_error(self):
        """
        test_delete_gateway_import_route_filter_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/import_route_filters/0a06fb9b-820f-4c44-8a31-77f1f0806d28')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "gateway_id": gateway_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_gateway_import_route_filter(**req_copy)

    def test_delete_gateway_import_route_filter_value_error_with_retries(self):
        # Enable retries and run test_delete_gateway_import_route_filter_value_error.
        _service.enable_retries()
        self.test_delete_gateway_import_route_filter_value_error()

        # Disable retries and run test_delete_gateway_import_route_filter_value_error.
        _service.disable_retries()
        self.test_delete_gateway_import_route_filter_value_error()


class TestGetGatewayImportRouteFilter:
    """
    Test Class for get_gateway_import_route_filter
    """

    @responses.activate
    def test_get_gateway_import_route_filter_all_params(self):
        """
        get_gateway_import_route_filter()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/import_route_filters/0a06fb9b-820f-4c44-8a31-77f1f0806d28')
        mock_response = '{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2020-11-02T20:40:29.622Z", "ge": 25, "id": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "le": 30, "prefix": "192.168.100.0/24", "updated_at": "2020-11-02T20:40:29.622Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Invoke method
        response = _service.get_gateway_import_route_filter(
            gateway_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_gateway_import_route_filter_all_params_with_retries(self):
        # Enable retries and run test_get_gateway_import_route_filter_all_params.
        _service.enable_retries()
        self.test_get_gateway_import_route_filter_all_params()

        # Disable retries and run test_get_gateway_import_route_filter_all_params.
        _service.disable_retries()
        self.test_get_gateway_import_route_filter_all_params()

    @responses.activate
    def test_get_gateway_import_route_filter_value_error(self):
        """
        test_get_gateway_import_route_filter_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/import_route_filters/0a06fb9b-820f-4c44-8a31-77f1f0806d28')
        mock_response = '{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2020-11-02T20:40:29.622Z", "ge": 25, "id": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "le": 30, "prefix": "192.168.100.0/24", "updated_at": "2020-11-02T20:40:29.622Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "gateway_id": gateway_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_gateway_import_route_filter(**req_copy)

    def test_get_gateway_import_route_filter_value_error_with_retries(self):
        # Enable retries and run test_get_gateway_import_route_filter_value_error.
        _service.enable_retries()
        self.test_get_gateway_import_route_filter_value_error()

        # Disable retries and run test_get_gateway_import_route_filter_value_error.
        _service.disable_retries()
        self.test_get_gateway_import_route_filter_value_error()


class TestUpdateGatewayImportRouteFilter:
    """
    Test Class for update_gateway_import_route_filter
    """

    @responses.activate
    def test_update_gateway_import_route_filter_all_params(self):
        """
        update_gateway_import_route_filter()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/import_route_filters/0a06fb9b-820f-4c44-8a31-77f1f0806d28')
        mock_response = '{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2020-11-02T20:40:29.622Z", "ge": 25, "id": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "le": 30, "prefix": "192.168.100.0/24", "updated_at": "2020-11-02T20:40:29.622Z"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a UpdateRouteFilterTemplate model
        update_route_filter_template_model = {}
        update_route_filter_template_model['action'] = 'permit'
        update_route_filter_template_model['before'] = '1a15dcab-7e40-45e1-b7c5-bc690eaa9782'
        update_route_filter_template_model['ge'] = 25
        update_route_filter_template_model['le'] = 30
        update_route_filter_template_model['prefix'] = '192.168.100.0/24'

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        update_route_filter_template = update_route_filter_template_model

        # Invoke method
        response = _service.update_gateway_import_route_filter(
            gateway_id,
            id,
            update_route_filter_template,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == update_route_filter_template

    def test_update_gateway_import_route_filter_all_params_with_retries(self):
        # Enable retries and run test_update_gateway_import_route_filter_all_params.
        _service.enable_retries()
        self.test_update_gateway_import_route_filter_all_params()

        # Disable retries and run test_update_gateway_import_route_filter_all_params.
        _service.disable_retries()
        self.test_update_gateway_import_route_filter_all_params()

    @responses.activate
    def test_update_gateway_import_route_filter_value_error(self):
        """
        test_update_gateway_import_route_filter_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/import_route_filters/0a06fb9b-820f-4c44-8a31-77f1f0806d28')
        mock_response = '{"action": "permit", "before": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "created_at": "2020-11-02T20:40:29.622Z", "ge": 25, "id": "1a15dcab-7e40-45e1-b7c5-bc690eaa9782", "le": 30, "prefix": "192.168.100.0/24", "updated_at": "2020-11-02T20:40:29.622Z"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a UpdateRouteFilterTemplate model
        update_route_filter_template_model = {}
        update_route_filter_template_model['action'] = 'permit'
        update_route_filter_template_model['before'] = '1a15dcab-7e40-45e1-b7c5-bc690eaa9782'
        update_route_filter_template_model['ge'] = 25
        update_route_filter_template_model['le'] = 30
        update_route_filter_template_model['prefix'] = '192.168.100.0/24'

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        update_route_filter_template = update_route_filter_template_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "gateway_id": gateway_id,
            "id": id,
            "update_route_filter_template": update_route_filter_template,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_gateway_import_route_filter(**req_copy)

    def test_update_gateway_import_route_filter_value_error_with_retries(self):
        # Enable retries and run test_update_gateway_import_route_filter_value_error.
        _service.enable_retries()
        self.test_update_gateway_import_route_filter_value_error()

        # Disable retries and run test_update_gateway_import_route_filter_value_error.
        _service.disable_retries()
        self.test_update_gateway_import_route_filter_value_error()


# endregion
##############################################################################
# End of Service: GatewayImportRouteFilters
##############################################################################

##############################################################################
# Start of Service: GatewayMACsec
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

        service = DirectLinkV1.new_instance(
            version=version,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DirectLinkV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DirectLinkV1.new_instance(
                version=version,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = DirectLinkV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='version must be provided'):
            service = DirectLinkV1.new_instance(
                version=None,
            )


class TestUnsetGatewayMacsec:
    """
    Test Class for unset_gateway_macsec
    """

    @responses.activate
    def test_unset_gateway_macsec_all_params(self):
        """
        unset_gateway_macsec()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/macsec')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Invoke method
        response = _service.unset_gateway_macsec(
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_unset_gateway_macsec_all_params_with_retries(self):
        # Enable retries and run test_unset_gateway_macsec_all_params.
        _service.enable_retries()
        self.test_unset_gateway_macsec_all_params()

        # Disable retries and run test_unset_gateway_macsec_all_params.
        _service.disable_retries()
        self.test_unset_gateway_macsec_all_params()

    @responses.activate
    def test_unset_gateway_macsec_value_error(self):
        """
        test_unset_gateway_macsec_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/macsec')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.unset_gateway_macsec(**req_copy)

    def test_unset_gateway_macsec_value_error_with_retries(self):
        # Enable retries and run test_unset_gateway_macsec_value_error.
        _service.enable_retries()
        self.test_unset_gateway_macsec_value_error()

        # Disable retries and run test_unset_gateway_macsec_value_error.
        _service.disable_retries()
        self.test_unset_gateway_macsec_value_error()


class TestGetGatewayMacsec:
    """
    Test Class for get_gateway_macsec
    """

    @responses.activate
    def test_get_gateway_macsec_all_params(self):
        """
        get_gateway_macsec()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/macsec')
        mock_response = '{"active": true, "cipher_suite": "gcm_aes_xpn_256", "confidentiality_offset": 0, "created_at": "2020-11-02T20:40:29.622Z", "key_server_priority": 255, "sak_rekey": {"interval": 3600, "mode": "timer"}, "security_policy": "must_secure", "status": "secured", "status_reasons": [{"code": "macsec_cak_failed", "message": "The `authentication_key` failed configuration.", "more_info": "https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK"}], "updated_at": "2020-11-02T20:40:29.622Z", "window_size": 512}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Invoke method
        response = _service.get_gateway_macsec(
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_gateway_macsec_all_params_with_retries(self):
        # Enable retries and run test_get_gateway_macsec_all_params.
        _service.enable_retries()
        self.test_get_gateway_macsec_all_params()

        # Disable retries and run test_get_gateway_macsec_all_params.
        _service.disable_retries()
        self.test_get_gateway_macsec_all_params()

    @responses.activate
    def test_get_gateway_macsec_value_error(self):
        """
        test_get_gateway_macsec_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/macsec')
        mock_response = '{"active": true, "cipher_suite": "gcm_aes_xpn_256", "confidentiality_offset": 0, "created_at": "2020-11-02T20:40:29.622Z", "key_server_priority": 255, "sak_rekey": {"interval": 3600, "mode": "timer"}, "security_policy": "must_secure", "status": "secured", "status_reasons": [{"code": "macsec_cak_failed", "message": "The `authentication_key` failed configuration.", "more_info": "https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK"}], "updated_at": "2020-11-02T20:40:29.622Z", "window_size": 512}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_gateway_macsec(**req_copy)

    def test_get_gateway_macsec_value_error_with_retries(self):
        # Enable retries and run test_get_gateway_macsec_value_error.
        _service.enable_retries()
        self.test_get_gateway_macsec_value_error()

        # Disable retries and run test_get_gateway_macsec_value_error.
        _service.disable_retries()
        self.test_get_gateway_macsec_value_error()


class TestUpdateGatewayMacsec:
    """
    Test Class for update_gateway_macsec
    """

    @responses.activate
    def test_update_gateway_macsec_all_params(self):
        """
        update_gateway_macsec()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/macsec')
        mock_response = '{"active": true, "cipher_suite": "gcm_aes_xpn_256", "confidentiality_offset": 0, "created_at": "2020-11-02T20:40:29.622Z", "key_server_priority": 255, "sak_rekey": {"interval": 3600, "mode": "timer"}, "security_policy": "must_secure", "status": "secured", "status_reasons": [{"code": "macsec_cak_failed", "message": "The `authentication_key` failed configuration.", "more_info": "https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK"}], "updated_at": "2020-11-02T20:40:29.622Z", "window_size": 512}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a SakRekeyPatchSakRekeyTimerModePatch model
        sak_rekey_patch_model = {}
        sak_rekey_patch_model['interval'] = 3600
        sak_rekey_patch_model['mode'] = 'timer'

        # Construct a dict representation of a GatewayMacsecPatch model
        gateway_macsec_patch_model = {}
        gateway_macsec_patch_model['active'] = True
        gateway_macsec_patch_model['sak_rekey'] = sak_rekey_patch_model
        gateway_macsec_patch_model['security_policy'] = 'must_secure'
        gateway_macsec_patch_model['window_size'] = 64

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        gateway_macsec_patch = gateway_macsec_patch_model

        # Invoke method
        response = _service.update_gateway_macsec(
            id,
            gateway_macsec_patch,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == gateway_macsec_patch

    def test_update_gateway_macsec_all_params_with_retries(self):
        # Enable retries and run test_update_gateway_macsec_all_params.
        _service.enable_retries()
        self.test_update_gateway_macsec_all_params()

        # Disable retries and run test_update_gateway_macsec_all_params.
        _service.disable_retries()
        self.test_update_gateway_macsec_all_params()

    @responses.activate
    def test_update_gateway_macsec_value_error(self):
        """
        test_update_gateway_macsec_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/macsec')
        mock_response = '{"active": true, "cipher_suite": "gcm_aes_xpn_256", "confidentiality_offset": 0, "created_at": "2020-11-02T20:40:29.622Z", "key_server_priority": 255, "sak_rekey": {"interval": 3600, "mode": "timer"}, "security_policy": "must_secure", "status": "secured", "status_reasons": [{"code": "macsec_cak_failed", "message": "The `authentication_key` failed configuration.", "more_info": "https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK"}], "updated_at": "2020-11-02T20:40:29.622Z", "window_size": 512}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a SakRekeyPatchSakRekeyTimerModePatch model
        sak_rekey_patch_model = {}
        sak_rekey_patch_model['interval'] = 3600
        sak_rekey_patch_model['mode'] = 'timer'

        # Construct a dict representation of a GatewayMacsecPatch model
        gateway_macsec_patch_model = {}
        gateway_macsec_patch_model['active'] = True
        gateway_macsec_patch_model['sak_rekey'] = sak_rekey_patch_model
        gateway_macsec_patch_model['security_policy'] = 'must_secure'
        gateway_macsec_patch_model['window_size'] = 64

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        gateway_macsec_patch = gateway_macsec_patch_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "gateway_macsec_patch": gateway_macsec_patch,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_gateway_macsec(**req_copy)

    def test_update_gateway_macsec_value_error_with_retries(self):
        # Enable retries and run test_update_gateway_macsec_value_error.
        _service.enable_retries()
        self.test_update_gateway_macsec_value_error()

        # Disable retries and run test_update_gateway_macsec_value_error.
        _service.disable_retries()
        self.test_update_gateway_macsec_value_error()


class TestSetGatewayMacsec:
    """
    Test Class for set_gateway_macsec
    """

    @responses.activate
    def test_set_gateway_macsec_all_params(self):
        """
        set_gateway_macsec()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/macsec')
        mock_response = '{"active": true, "cipher_suite": "gcm_aes_xpn_256", "confidentiality_offset": 0, "created_at": "2020-11-02T20:40:29.622Z", "key_server_priority": 255, "sak_rekey": {"interval": 3600, "mode": "timer"}, "security_policy": "must_secure", "status": "secured", "status_reasons": [{"code": "macsec_cak_failed", "message": "The `authentication_key` failed configuration.", "more_info": "https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK"}], "updated_at": "2020-11-02T20:40:29.622Z", "window_size": 512}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a HpcsKeyIdentity model
        hpcs_key_identity_model = {}
        hpcs_key_identity_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a dict representation of a GatewayMacsecCakPrototype model
        gateway_macsec_cak_prototype_model = {}
        gateway_macsec_cak_prototype_model['key'] = hpcs_key_identity_model
        gateway_macsec_cak_prototype_model['name'] = '1000'
        gateway_macsec_cak_prototype_model['session'] = 'primary'

        # Construct a dict representation of a SakRekeyPrototypeSakRekeyTimerModePrototype model
        sak_rekey_prototype_model = {}
        sak_rekey_prototype_model['interval'] = 3600
        sak_rekey_prototype_model['mode'] = 'timer'

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        active = True
        caks = [gateway_macsec_cak_prototype_model]
        sak_rekey = sak_rekey_prototype_model
        security_policy = 'must_secure'
        window_size = 64
        if_match = 'W/"96d225c4-56bd-43d9-98fc-d7148e5c5028"'

        # Invoke method
        response = _service.set_gateway_macsec(
            id,
            active,
            caks,
            sak_rekey,
            security_policy,
            window_size=window_size,
            if_match=if_match,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['active'] == True
        assert req_body['caks'] == [gateway_macsec_cak_prototype_model]
        assert req_body['sak_rekey'] == sak_rekey_prototype_model
        assert req_body['security_policy'] == 'must_secure'
        assert req_body['window_size'] == 64

    def test_set_gateway_macsec_all_params_with_retries(self):
        # Enable retries and run test_set_gateway_macsec_all_params.
        _service.enable_retries()
        self.test_set_gateway_macsec_all_params()

        # Disable retries and run test_set_gateway_macsec_all_params.
        _service.disable_retries()
        self.test_set_gateway_macsec_all_params()

    @responses.activate
    def test_set_gateway_macsec_required_params(self):
        """
        test_set_gateway_macsec_required_params()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/macsec')
        mock_response = '{"active": true, "cipher_suite": "gcm_aes_xpn_256", "confidentiality_offset": 0, "created_at": "2020-11-02T20:40:29.622Z", "key_server_priority": 255, "sak_rekey": {"interval": 3600, "mode": "timer"}, "security_policy": "must_secure", "status": "secured", "status_reasons": [{"code": "macsec_cak_failed", "message": "The `authentication_key` failed configuration.", "more_info": "https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK"}], "updated_at": "2020-11-02T20:40:29.622Z", "window_size": 512}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a HpcsKeyIdentity model
        hpcs_key_identity_model = {}
        hpcs_key_identity_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a dict representation of a GatewayMacsecCakPrototype model
        gateway_macsec_cak_prototype_model = {}
        gateway_macsec_cak_prototype_model['key'] = hpcs_key_identity_model
        gateway_macsec_cak_prototype_model['name'] = '1000'
        gateway_macsec_cak_prototype_model['session'] = 'primary'

        # Construct a dict representation of a SakRekeyPrototypeSakRekeyTimerModePrototype model
        sak_rekey_prototype_model = {}
        sak_rekey_prototype_model['interval'] = 3600
        sak_rekey_prototype_model['mode'] = 'timer'

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        active = True
        caks = [gateway_macsec_cak_prototype_model]
        sak_rekey = sak_rekey_prototype_model
        security_policy = 'must_secure'
        window_size = 64

        # Invoke method
        response = _service.set_gateway_macsec(
            id,
            active,
            caks,
            sak_rekey,
            security_policy,
            window_size=window_size,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['active'] == True
        assert req_body['caks'] == [gateway_macsec_cak_prototype_model]
        assert req_body['sak_rekey'] == sak_rekey_prototype_model
        assert req_body['security_policy'] == 'must_secure'
        assert req_body['window_size'] == 64

    def test_set_gateway_macsec_required_params_with_retries(self):
        # Enable retries and run test_set_gateway_macsec_required_params.
        _service.enable_retries()
        self.test_set_gateway_macsec_required_params()

        # Disable retries and run test_set_gateway_macsec_required_params.
        _service.disable_retries()
        self.test_set_gateway_macsec_required_params()

    @responses.activate
    def test_set_gateway_macsec_value_error(self):
        """
        test_set_gateway_macsec_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/macsec')
        mock_response = '{"active": true, "cipher_suite": "gcm_aes_xpn_256", "confidentiality_offset": 0, "created_at": "2020-11-02T20:40:29.622Z", "key_server_priority": 255, "sak_rekey": {"interval": 3600, "mode": "timer"}, "security_policy": "must_secure", "status": "secured", "status_reasons": [{"code": "macsec_cak_failed", "message": "The `authentication_key` failed configuration.", "more_info": "https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK"}], "updated_at": "2020-11-02T20:40:29.622Z", "window_size": 512}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a HpcsKeyIdentity model
        hpcs_key_identity_model = {}
        hpcs_key_identity_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a dict representation of a GatewayMacsecCakPrototype model
        gateway_macsec_cak_prototype_model = {}
        gateway_macsec_cak_prototype_model['key'] = hpcs_key_identity_model
        gateway_macsec_cak_prototype_model['name'] = '1000'
        gateway_macsec_cak_prototype_model['session'] = 'primary'

        # Construct a dict representation of a SakRekeyPrototypeSakRekeyTimerModePrototype model
        sak_rekey_prototype_model = {}
        sak_rekey_prototype_model['interval'] = 3600
        sak_rekey_prototype_model['mode'] = 'timer'

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        active = True
        caks = [gateway_macsec_cak_prototype_model]
        sak_rekey = sak_rekey_prototype_model
        security_policy = 'must_secure'
        window_size = 64

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "active": active,
            "caks": caks,
            "sak_rekey": sak_rekey,
            "security_policy": security_policy,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.set_gateway_macsec(**req_copy)

    def test_set_gateway_macsec_value_error_with_retries(self):
        # Enable retries and run test_set_gateway_macsec_value_error.
        _service.enable_retries()
        self.test_set_gateway_macsec_value_error()

        # Disable retries and run test_set_gateway_macsec_value_error.
        _service.disable_retries()
        self.test_set_gateway_macsec_value_error()


class TestListGatewayMacsecCaks:
    """
    Test Class for list_gateway_macsec_caks
    """

    @responses.activate
    def test_list_gateway_macsec_caks_all_params(self):
        """
        list_gateway_macsec_caks()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/macsec/caks')
        mock_response = '{"caks": [{"active_delta": {"key": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222"}, "name": "1000", "status": "active"}, "created_at": "2020-11-02T20:40:29.622Z", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "key": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222"}, "name": "1000", "session": "primary", "status": "active", "updated_at": "2020-11-02T20:40:29.622Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Invoke method
        response = _service.list_gateway_macsec_caks(
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_gateway_macsec_caks_all_params_with_retries(self):
        # Enable retries and run test_list_gateway_macsec_caks_all_params.
        _service.enable_retries()
        self.test_list_gateway_macsec_caks_all_params()

        # Disable retries and run test_list_gateway_macsec_caks_all_params.
        _service.disable_retries()
        self.test_list_gateway_macsec_caks_all_params()

    @responses.activate
    def test_list_gateway_macsec_caks_value_error(self):
        """
        test_list_gateway_macsec_caks_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/macsec/caks')
        mock_response = '{"caks": [{"active_delta": {"key": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222"}, "name": "1000", "status": "active"}, "created_at": "2020-11-02T20:40:29.622Z", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "key": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222"}, "name": "1000", "session": "primary", "status": "active", "updated_at": "2020-11-02T20:40:29.622Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_gateway_macsec_caks(**req_copy)

    def test_list_gateway_macsec_caks_value_error_with_retries(self):
        # Enable retries and run test_list_gateway_macsec_caks_value_error.
        _service.enable_retries()
        self.test_list_gateway_macsec_caks_value_error()

        # Disable retries and run test_list_gateway_macsec_caks_value_error.
        _service.disable_retries()
        self.test_list_gateway_macsec_caks_value_error()


class TestCreateGatewayMacsecCak:
    """
    Test Class for create_gateway_macsec_cak
    """

    @responses.activate
    def test_create_gateway_macsec_cak_all_params(self):
        """
        create_gateway_macsec_cak()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/macsec/caks')
        mock_response = '{"active_delta": {"key": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222"}, "name": "1000", "status": "active"}, "created_at": "2020-11-02T20:40:29.622Z", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "key": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222"}, "name": "1000", "session": "primary", "status": "active", "updated_at": "2020-11-02T20:40:29.622Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a HpcsKeyIdentity model
        hpcs_key_identity_model = {}
        hpcs_key_identity_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        key = hpcs_key_identity_model
        name = '1000'
        session = 'primary'

        # Invoke method
        response = _service.create_gateway_macsec_cak(
            id,
            key,
            name,
            session,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['key'] == hpcs_key_identity_model
        assert req_body['name'] == '1000'
        assert req_body['session'] == 'primary'

    def test_create_gateway_macsec_cak_all_params_with_retries(self):
        # Enable retries and run test_create_gateway_macsec_cak_all_params.
        _service.enable_retries()
        self.test_create_gateway_macsec_cak_all_params()

        # Disable retries and run test_create_gateway_macsec_cak_all_params.
        _service.disable_retries()
        self.test_create_gateway_macsec_cak_all_params()

    @responses.activate
    def test_create_gateway_macsec_cak_value_error(self):
        """
        test_create_gateway_macsec_cak_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/macsec/caks')
        mock_response = '{"active_delta": {"key": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222"}, "name": "1000", "status": "active"}, "created_at": "2020-11-02T20:40:29.622Z", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "key": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222"}, "name": "1000", "session": "primary", "status": "active", "updated_at": "2020-11-02T20:40:29.622Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a HpcsKeyIdentity model
        hpcs_key_identity_model = {}
        hpcs_key_identity_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        key = hpcs_key_identity_model
        name = '1000'
        session = 'primary'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "key": key,
            "name": name,
            "session": session,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_gateway_macsec_cak(**req_copy)

    def test_create_gateway_macsec_cak_value_error_with_retries(self):
        # Enable retries and run test_create_gateway_macsec_cak_value_error.
        _service.enable_retries()
        self.test_create_gateway_macsec_cak_value_error()

        # Disable retries and run test_create_gateway_macsec_cak_value_error.
        _service.disable_retries()
        self.test_create_gateway_macsec_cak_value_error()


class TestDeleteGatewayMacsecCak:
    """
    Test Class for delete_gateway_macsec_cak
    """

    @responses.activate
    def test_delete_gateway_macsec_cak_all_params(self):
        """
        delete_gateway_macsec_cak()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/macsec/caks/ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        cak_id = 'ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'

        # Invoke method
        response = _service.delete_gateway_macsec_cak(
            id,
            cak_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_gateway_macsec_cak_all_params_with_retries(self):
        # Enable retries and run test_delete_gateway_macsec_cak_all_params.
        _service.enable_retries()
        self.test_delete_gateway_macsec_cak_all_params()

        # Disable retries and run test_delete_gateway_macsec_cak_all_params.
        _service.disable_retries()
        self.test_delete_gateway_macsec_cak_all_params()

    @responses.activate
    def test_delete_gateway_macsec_cak_value_error(self):
        """
        test_delete_gateway_macsec_cak_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/macsec/caks/ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        cak_id = 'ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "cak_id": cak_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_gateway_macsec_cak(**req_copy)

    def test_delete_gateway_macsec_cak_value_error_with_retries(self):
        # Enable retries and run test_delete_gateway_macsec_cak_value_error.
        _service.enable_retries()
        self.test_delete_gateway_macsec_cak_value_error()

        # Disable retries and run test_delete_gateway_macsec_cak_value_error.
        _service.disable_retries()
        self.test_delete_gateway_macsec_cak_value_error()


class TestGetGatewayMacsecCak:
    """
    Test Class for get_gateway_macsec_cak
    """

    @responses.activate
    def test_get_gateway_macsec_cak_all_params(self):
        """
        get_gateway_macsec_cak()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/macsec/caks/ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4')
        mock_response = '{"active_delta": {"key": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222"}, "name": "1000", "status": "active"}, "created_at": "2020-11-02T20:40:29.622Z", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "key": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222"}, "name": "1000", "session": "primary", "status": "active", "updated_at": "2020-11-02T20:40:29.622Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        cak_id = 'ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'

        # Invoke method
        response = _service.get_gateway_macsec_cak(
            id,
            cak_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_gateway_macsec_cak_all_params_with_retries(self):
        # Enable retries and run test_get_gateway_macsec_cak_all_params.
        _service.enable_retries()
        self.test_get_gateway_macsec_cak_all_params()

        # Disable retries and run test_get_gateway_macsec_cak_all_params.
        _service.disable_retries()
        self.test_get_gateway_macsec_cak_all_params()

    @responses.activate
    def test_get_gateway_macsec_cak_value_error(self):
        """
        test_get_gateway_macsec_cak_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/macsec/caks/ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4')
        mock_response = '{"active_delta": {"key": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222"}, "name": "1000", "status": "active"}, "created_at": "2020-11-02T20:40:29.622Z", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "key": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222"}, "name": "1000", "session": "primary", "status": "active", "updated_at": "2020-11-02T20:40:29.622Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        cak_id = 'ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "cak_id": cak_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_gateway_macsec_cak(**req_copy)

    def test_get_gateway_macsec_cak_value_error_with_retries(self):
        # Enable retries and run test_get_gateway_macsec_cak_value_error.
        _service.enable_retries()
        self.test_get_gateway_macsec_cak_value_error()

        # Disable retries and run test_get_gateway_macsec_cak_value_error.
        _service.disable_retries()
        self.test_get_gateway_macsec_cak_value_error()


class TestUpdateGatewayMacsecCak:
    """
    Test Class for update_gateway_macsec_cak
    """

    @responses.activate
    def test_update_gateway_macsec_cak_all_params(self):
        """
        update_gateway_macsec_cak()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/macsec/caks/ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4')
        mock_response = '{"active_delta": {"key": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222"}, "name": "1000", "status": "active"}, "created_at": "2020-11-02T20:40:29.622Z", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "key": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222"}, "name": "1000", "session": "primary", "status": "active", "updated_at": "2020-11-02T20:40:29.622Z"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a HpcsKeyIdentity model
        hpcs_key_identity_model = {}
        hpcs_key_identity_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a dict representation of a GatewayMacsecCakPatch model
        gateway_macsec_cak_patch_model = {}
        gateway_macsec_cak_patch_model['key'] = hpcs_key_identity_model
        gateway_macsec_cak_patch_model['name'] = '1000'

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        cak_id = 'ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        gateway_macsec_cak_patch = gateway_macsec_cak_patch_model

        # Invoke method
        response = _service.update_gateway_macsec_cak(
            id,
            cak_id,
            gateway_macsec_cak_patch,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == gateway_macsec_cak_patch

    def test_update_gateway_macsec_cak_all_params_with_retries(self):
        # Enable retries and run test_update_gateway_macsec_cak_all_params.
        _service.enable_retries()
        self.test_update_gateway_macsec_cak_all_params()

        # Disable retries and run test_update_gateway_macsec_cak_all_params.
        _service.disable_retries()
        self.test_update_gateway_macsec_cak_all_params()

    @responses.activate
    def test_update_gateway_macsec_cak_value_error(self):
        """
        test_update_gateway_macsec_cak_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/macsec/caks/ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4')
        mock_response = '{"active_delta": {"key": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222"}, "name": "1000", "status": "active"}, "created_at": "2020-11-02T20:40:29.622Z", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "key": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222"}, "name": "1000", "session": "primary", "status": "active", "updated_at": "2020-11-02T20:40:29.622Z"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a HpcsKeyIdentity model
        hpcs_key_identity_model = {}
        hpcs_key_identity_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a dict representation of a GatewayMacsecCakPatch model
        gateway_macsec_cak_patch_model = {}
        gateway_macsec_cak_patch_model['key'] = hpcs_key_identity_model
        gateway_macsec_cak_patch_model['name'] = '1000'

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        cak_id = 'ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        gateway_macsec_cak_patch = gateway_macsec_cak_patch_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "cak_id": cak_id,
            "gateway_macsec_cak_patch": gateway_macsec_cak_patch,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_gateway_macsec_cak(**req_copy)

    def test_update_gateway_macsec_cak_value_error_with_retries(self):
        # Enable retries and run test_update_gateway_macsec_cak_value_error.
        _service.enable_retries()
        self.test_update_gateway_macsec_cak_value_error()

        # Disable retries and run test_update_gateway_macsec_cak_value_error.
        _service.disable_retries()
        self.test_update_gateway_macsec_cak_value_error()


# endregion
##############################################################################
# End of Service: GatewayMACsec
##############################################################################

##############################################################################
# Start of Service: GatewayRouteReports
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

        service = DirectLinkV1.new_instance(
            version=version,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DirectLinkV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DirectLinkV1.new_instance(
                version=version,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = DirectLinkV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='version must be provided'):
            service = DirectLinkV1.new_instance(
                version=None,
            )


class TestListGatewayRouteReports:
    """
    Test Class for list_gateway_route_reports
    """

    @responses.activate
    def test_list_gateway_route_reports_all_params(self):
        """
        list_gateway_route_reports()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/route_reports')
        mock_response = '{"route_reports": [{"advertised_routes": [{"as_path": "64999 64999 64998 I", "prefix": "172.17.0.0/16"}], "created_at": "2019-01-01T12:00:00.000Z", "gateway_routes": [{"prefix": "172.17.0.0/16"}], "id": "1a15dcab-7e26-45e1-b7c5-bc690eaa9724", "on_prem_routes": [{"as_path": "64999 64999 64998 I", "next_hop": "172.17.0.0", "prefix": "172.17.0.0/16"}], "overlapping_routes": [{"routes": [{"prefix": "172.17.0.0/16", "type": "virtual_connection", "virtual_connection_id": "d2d985d8-1d8e-4e8b-96cd-cee2290ecaff"}]}], "status": "complete", "updated_at": "2019-01-01T12:00:00.000Z", "virtual_connection_routes": [{"routes": [{"active": true, "local_preference": "200", "prefix": "172.17.0.0/16"}], "virtual_connection_id": "3c265a62-91da-4261-a950-950b6af0eb58", "virtual_connection_name": "vpc1", "virtual_connection_type": "vpc"}]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Invoke method
        response = _service.list_gateway_route_reports(
            gateway_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_gateway_route_reports_all_params_with_retries(self):
        # Enable retries and run test_list_gateway_route_reports_all_params.
        _service.enable_retries()
        self.test_list_gateway_route_reports_all_params()

        # Disable retries and run test_list_gateway_route_reports_all_params.
        _service.disable_retries()
        self.test_list_gateway_route_reports_all_params()

    @responses.activate
    def test_list_gateway_route_reports_value_error(self):
        """
        test_list_gateway_route_reports_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/route_reports')
        mock_response = '{"route_reports": [{"advertised_routes": [{"as_path": "64999 64999 64998 I", "prefix": "172.17.0.0/16"}], "created_at": "2019-01-01T12:00:00.000Z", "gateway_routes": [{"prefix": "172.17.0.0/16"}], "id": "1a15dcab-7e26-45e1-b7c5-bc690eaa9724", "on_prem_routes": [{"as_path": "64999 64999 64998 I", "next_hop": "172.17.0.0", "prefix": "172.17.0.0/16"}], "overlapping_routes": [{"routes": [{"prefix": "172.17.0.0/16", "type": "virtual_connection", "virtual_connection_id": "d2d985d8-1d8e-4e8b-96cd-cee2290ecaff"}]}], "status": "complete", "updated_at": "2019-01-01T12:00:00.000Z", "virtual_connection_routes": [{"routes": [{"active": true, "local_preference": "200", "prefix": "172.17.0.0/16"}], "virtual_connection_id": "3c265a62-91da-4261-a950-950b6af0eb58", "virtual_connection_name": "vpc1", "virtual_connection_type": "vpc"}]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "gateway_id": gateway_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_gateway_route_reports(**req_copy)

    def test_list_gateway_route_reports_value_error_with_retries(self):
        # Enable retries and run test_list_gateway_route_reports_value_error.
        _service.enable_retries()
        self.test_list_gateway_route_reports_value_error()

        # Disable retries and run test_list_gateway_route_reports_value_error.
        _service.disable_retries()
        self.test_list_gateway_route_reports_value_error()


class TestCreateGatewayRouteReport:
    """
    Test Class for create_gateway_route_report
    """

    @responses.activate
    def test_create_gateway_route_report_all_params(self):
        """
        create_gateway_route_report()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/route_reports')
        mock_response = '{"advertised_routes": [{"as_path": "64999 64999 64998 I", "prefix": "172.17.0.0/16"}], "created_at": "2019-01-01T12:00:00.000Z", "gateway_routes": [{"prefix": "172.17.0.0/16"}], "id": "1a15dcab-7e26-45e1-b7c5-bc690eaa9724", "on_prem_routes": [{"as_path": "64999 64999 64998 I", "next_hop": "172.17.0.0", "prefix": "172.17.0.0/16"}], "overlapping_routes": [{"routes": [{"prefix": "172.17.0.0/16", "type": "virtual_connection", "virtual_connection_id": "d2d985d8-1d8e-4e8b-96cd-cee2290ecaff"}]}], "status": "complete", "updated_at": "2019-01-01T12:00:00.000Z", "virtual_connection_routes": [{"routes": [{"active": true, "local_preference": "200", "prefix": "172.17.0.0/16"}], "virtual_connection_id": "3c265a62-91da-4261-a950-950b6af0eb58", "virtual_connection_name": "vpc1", "virtual_connection_type": "vpc"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Invoke method
        response = _service.create_gateway_route_report(
            gateway_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_create_gateway_route_report_all_params_with_retries(self):
        # Enable retries and run test_create_gateway_route_report_all_params.
        _service.enable_retries()
        self.test_create_gateway_route_report_all_params()

        # Disable retries and run test_create_gateway_route_report_all_params.
        _service.disable_retries()
        self.test_create_gateway_route_report_all_params()

    @responses.activate
    def test_create_gateway_route_report_value_error(self):
        """
        test_create_gateway_route_report_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/route_reports')
        mock_response = '{"advertised_routes": [{"as_path": "64999 64999 64998 I", "prefix": "172.17.0.0/16"}], "created_at": "2019-01-01T12:00:00.000Z", "gateway_routes": [{"prefix": "172.17.0.0/16"}], "id": "1a15dcab-7e26-45e1-b7c5-bc690eaa9724", "on_prem_routes": [{"as_path": "64999 64999 64998 I", "next_hop": "172.17.0.0", "prefix": "172.17.0.0/16"}], "overlapping_routes": [{"routes": [{"prefix": "172.17.0.0/16", "type": "virtual_connection", "virtual_connection_id": "d2d985d8-1d8e-4e8b-96cd-cee2290ecaff"}]}], "status": "complete", "updated_at": "2019-01-01T12:00:00.000Z", "virtual_connection_routes": [{"routes": [{"active": true, "local_preference": "200", "prefix": "172.17.0.0/16"}], "virtual_connection_id": "3c265a62-91da-4261-a950-950b6af0eb58", "virtual_connection_name": "vpc1", "virtual_connection_type": "vpc"}]}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "gateway_id": gateway_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_gateway_route_report(**req_copy)

    def test_create_gateway_route_report_value_error_with_retries(self):
        # Enable retries and run test_create_gateway_route_report_value_error.
        _service.enable_retries()
        self.test_create_gateway_route_report_value_error()

        # Disable retries and run test_create_gateway_route_report_value_error.
        _service.disable_retries()
        self.test_create_gateway_route_report_value_error()


class TestDeleteGatewayRouteReport:
    """
    Test Class for delete_gateway_route_report
    """

    @responses.activate
    def test_delete_gateway_route_report_all_params(self):
        """
        delete_gateway_route_report()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/route_reports/0a06fb9b-820f-4c44-8a31-77f1f0806d28')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Invoke method
        response = _service.delete_gateway_route_report(
            gateway_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_gateway_route_report_all_params_with_retries(self):
        # Enable retries and run test_delete_gateway_route_report_all_params.
        _service.enable_retries()
        self.test_delete_gateway_route_report_all_params()

        # Disable retries and run test_delete_gateway_route_report_all_params.
        _service.disable_retries()
        self.test_delete_gateway_route_report_all_params()

    @responses.activate
    def test_delete_gateway_route_report_value_error(self):
        """
        test_delete_gateway_route_report_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/route_reports/0a06fb9b-820f-4c44-8a31-77f1f0806d28')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "gateway_id": gateway_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_gateway_route_report(**req_copy)

    def test_delete_gateway_route_report_value_error_with_retries(self):
        # Enable retries and run test_delete_gateway_route_report_value_error.
        _service.enable_retries()
        self.test_delete_gateway_route_report_value_error()

        # Disable retries and run test_delete_gateway_route_report_value_error.
        _service.disable_retries()
        self.test_delete_gateway_route_report_value_error()


class TestGetGatewayRouteReport:
    """
    Test Class for get_gateway_route_report
    """

    @responses.activate
    def test_get_gateway_route_report_all_params(self):
        """
        get_gateway_route_report()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/route_reports/0a06fb9b-820f-4c44-8a31-77f1f0806d28')
        mock_response = '{"advertised_routes": [{"as_path": "64999 64999 64998 I", "prefix": "172.17.0.0/16"}], "created_at": "2019-01-01T12:00:00.000Z", "gateway_routes": [{"prefix": "172.17.0.0/16"}], "id": "1a15dcab-7e26-45e1-b7c5-bc690eaa9724", "on_prem_routes": [{"as_path": "64999 64999 64998 I", "next_hop": "172.17.0.0", "prefix": "172.17.0.0/16"}], "overlapping_routes": [{"routes": [{"prefix": "172.17.0.0/16", "type": "virtual_connection", "virtual_connection_id": "d2d985d8-1d8e-4e8b-96cd-cee2290ecaff"}]}], "status": "complete", "updated_at": "2019-01-01T12:00:00.000Z", "virtual_connection_routes": [{"routes": [{"active": true, "local_preference": "200", "prefix": "172.17.0.0/16"}], "virtual_connection_id": "3c265a62-91da-4261-a950-950b6af0eb58", "virtual_connection_name": "vpc1", "virtual_connection_type": "vpc"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Invoke method
        response = _service.get_gateway_route_report(
            gateway_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_gateway_route_report_all_params_with_retries(self):
        # Enable retries and run test_get_gateway_route_report_all_params.
        _service.enable_retries()
        self.test_get_gateway_route_report_all_params()

        # Disable retries and run test_get_gateway_route_report_all_params.
        _service.disable_retries()
        self.test_get_gateway_route_report_all_params()

    @responses.activate
    def test_get_gateway_route_report_value_error(self):
        """
        test_get_gateway_route_report_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/route_reports/0a06fb9b-820f-4c44-8a31-77f1f0806d28')
        mock_response = '{"advertised_routes": [{"as_path": "64999 64999 64998 I", "prefix": "172.17.0.0/16"}], "created_at": "2019-01-01T12:00:00.000Z", "gateway_routes": [{"prefix": "172.17.0.0/16"}], "id": "1a15dcab-7e26-45e1-b7c5-bc690eaa9724", "on_prem_routes": [{"as_path": "64999 64999 64998 I", "next_hop": "172.17.0.0", "prefix": "172.17.0.0/16"}], "overlapping_routes": [{"routes": [{"prefix": "172.17.0.0/16", "type": "virtual_connection", "virtual_connection_id": "d2d985d8-1d8e-4e8b-96cd-cee2290ecaff"}]}], "status": "complete", "updated_at": "2019-01-01T12:00:00.000Z", "virtual_connection_routes": [{"routes": [{"active": true, "local_preference": "200", "prefix": "172.17.0.0/16"}], "virtual_connection_id": "3c265a62-91da-4261-a950-950b6af0eb58", "virtual_connection_name": "vpc1", "virtual_connection_type": "vpc"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "gateway_id": gateway_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_gateway_route_report(**req_copy)

    def test_get_gateway_route_report_value_error_with_retries(self):
        # Enable retries and run test_get_gateway_route_report_value_error.
        _service.enable_retries()
        self.test_get_gateway_route_report_value_error()

        # Disable retries and run test_get_gateway_route_report_value_error.
        _service.disable_retries()
        self.test_get_gateway_route_report_value_error()


# endregion
##############################################################################
# End of Service: GatewayRouteReports
##############################################################################

##############################################################################
# Start of Service: VirtualConnections
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

        service = DirectLinkV1.new_instance(
            version=version,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DirectLinkV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DirectLinkV1.new_instance(
                version=version,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = DirectLinkV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='version must be provided'):
            service = DirectLinkV1.new_instance(
                version=None,
            )


class TestListGatewayVirtualConnections:
    """
    Test Class for list_gateway_virtual_connections
    """

    @responses.activate
    def test_list_gateway_virtual_connections_all_params(self):
        """
        list_gateway_virtual_connections()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/virtual_connections')
        mock_response = '{"virtual_connections": [{"created_at": "2019-01-01T12:00:00.000Z", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "newVC", "network_account": "00aa14a2e0fb102c8995ebefff865555", "network_id": "crn:v1:bluemix:public:is:us-east:a/28e4d90ac7504be69447111122223333::vpc:aaa81ac8-5e96-42a0-a4b7-6c2e2d1bbbbb", "status": "attached", "type": "vpc"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Invoke method
        response = _service.list_gateway_virtual_connections(
            gateway_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_gateway_virtual_connections_all_params_with_retries(self):
        # Enable retries and run test_list_gateway_virtual_connections_all_params.
        _service.enable_retries()
        self.test_list_gateway_virtual_connections_all_params()

        # Disable retries and run test_list_gateway_virtual_connections_all_params.
        _service.disable_retries()
        self.test_list_gateway_virtual_connections_all_params()

    @responses.activate
    def test_list_gateway_virtual_connections_value_error(self):
        """
        test_list_gateway_virtual_connections_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/virtual_connections')
        mock_response = '{"virtual_connections": [{"created_at": "2019-01-01T12:00:00.000Z", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "newVC", "network_account": "00aa14a2e0fb102c8995ebefff865555", "network_id": "crn:v1:bluemix:public:is:us-east:a/28e4d90ac7504be69447111122223333::vpc:aaa81ac8-5e96-42a0-a4b7-6c2e2d1bbbbb", "status": "attached", "type": "vpc"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "gateway_id": gateway_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_gateway_virtual_connections(**req_copy)

    def test_list_gateway_virtual_connections_value_error_with_retries(self):
        # Enable retries and run test_list_gateway_virtual_connections_value_error.
        _service.enable_retries()
        self.test_list_gateway_virtual_connections_value_error()

        # Disable retries and run test_list_gateway_virtual_connections_value_error.
        _service.disable_retries()
        self.test_list_gateway_virtual_connections_value_error()


class TestCreateGatewayVirtualConnection:
    """
    Test Class for create_gateway_virtual_connection
    """

    @responses.activate
    def test_create_gateway_virtual_connection_all_params(self):
        """
        create_gateway_virtual_connection()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/virtual_connections')
        mock_response = '{"created_at": "2019-01-01T12:00:00.000Z", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "newVC", "network_account": "00aa14a2e0fb102c8995ebefff865555", "network_id": "crn:v1:bluemix:public:is:us-east:a/28e4d90ac7504be69447111122223333::vpc:aaa81ac8-5e96-42a0-a4b7-6c2e2d1bbbbb", "status": "attached", "type": "vpc"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        name = 'newVC'
        type = 'vpc'
        network_id = 'crn:v1:bluemix:public:is:us-east:a/28e4d90ac7504be69447111122223333::vpc:aaa81ac8-5e96-42a0-a4b7-6c2e2d1bbbbb'

        # Invoke method
        response = _service.create_gateway_virtual_connection(
            gateway_id,
            name,
            type,
            network_id=network_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'newVC'
        assert req_body['type'] == 'vpc'
        assert req_body['network_id'] == 'crn:v1:bluemix:public:is:us-east:a/28e4d90ac7504be69447111122223333::vpc:aaa81ac8-5e96-42a0-a4b7-6c2e2d1bbbbb'

    def test_create_gateway_virtual_connection_all_params_with_retries(self):
        # Enable retries and run test_create_gateway_virtual_connection_all_params.
        _service.enable_retries()
        self.test_create_gateway_virtual_connection_all_params()

        # Disable retries and run test_create_gateway_virtual_connection_all_params.
        _service.disable_retries()
        self.test_create_gateway_virtual_connection_all_params()

    @responses.activate
    def test_create_gateway_virtual_connection_value_error(self):
        """
        test_create_gateway_virtual_connection_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/virtual_connections')
        mock_response = '{"created_at": "2019-01-01T12:00:00.000Z", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "newVC", "network_account": "00aa14a2e0fb102c8995ebefff865555", "network_id": "crn:v1:bluemix:public:is:us-east:a/28e4d90ac7504be69447111122223333::vpc:aaa81ac8-5e96-42a0-a4b7-6c2e2d1bbbbb", "status": "attached", "type": "vpc"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        name = 'newVC'
        type = 'vpc'
        network_id = 'crn:v1:bluemix:public:is:us-east:a/28e4d90ac7504be69447111122223333::vpc:aaa81ac8-5e96-42a0-a4b7-6c2e2d1bbbbb'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "gateway_id": gateway_id,
            "name": name,
            "type": type,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_gateway_virtual_connection(**req_copy)

    def test_create_gateway_virtual_connection_value_error_with_retries(self):
        # Enable retries and run test_create_gateway_virtual_connection_value_error.
        _service.enable_retries()
        self.test_create_gateway_virtual_connection_value_error()

        # Disable retries and run test_create_gateway_virtual_connection_value_error.
        _service.disable_retries()
        self.test_create_gateway_virtual_connection_value_error()


class TestDeleteGatewayVirtualConnection:
    """
    Test Class for delete_gateway_virtual_connection
    """

    @responses.activate
    def test_delete_gateway_virtual_connection_all_params(self):
        """
        delete_gateway_virtual_connection()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/virtual_connections/0a06fb9b-820f-4c44-8a31-77f1f0806d28')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Invoke method
        response = _service.delete_gateway_virtual_connection(
            gateway_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_gateway_virtual_connection_all_params_with_retries(self):
        # Enable retries and run test_delete_gateway_virtual_connection_all_params.
        _service.enable_retries()
        self.test_delete_gateway_virtual_connection_all_params()

        # Disable retries and run test_delete_gateway_virtual_connection_all_params.
        _service.disable_retries()
        self.test_delete_gateway_virtual_connection_all_params()

    @responses.activate
    def test_delete_gateway_virtual_connection_value_error(self):
        """
        test_delete_gateway_virtual_connection_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/virtual_connections/0a06fb9b-820f-4c44-8a31-77f1f0806d28')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "gateway_id": gateway_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_gateway_virtual_connection(**req_copy)

    def test_delete_gateway_virtual_connection_value_error_with_retries(self):
        # Enable retries and run test_delete_gateway_virtual_connection_value_error.
        _service.enable_retries()
        self.test_delete_gateway_virtual_connection_value_error()

        # Disable retries and run test_delete_gateway_virtual_connection_value_error.
        _service.disable_retries()
        self.test_delete_gateway_virtual_connection_value_error()


class TestGetGatewayVirtualConnection:
    """
    Test Class for get_gateway_virtual_connection
    """

    @responses.activate
    def test_get_gateway_virtual_connection_all_params(self):
        """
        get_gateway_virtual_connection()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/virtual_connections/0a06fb9b-820f-4c44-8a31-77f1f0806d28')
        mock_response = '{"created_at": "2019-01-01T12:00:00.000Z", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "newVC", "network_account": "00aa14a2e0fb102c8995ebefff865555", "network_id": "crn:v1:bluemix:public:is:us-east:a/28e4d90ac7504be69447111122223333::vpc:aaa81ac8-5e96-42a0-a4b7-6c2e2d1bbbbb", "status": "attached", "type": "vpc"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Invoke method
        response = _service.get_gateway_virtual_connection(
            gateway_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_gateway_virtual_connection_all_params_with_retries(self):
        # Enable retries and run test_get_gateway_virtual_connection_all_params.
        _service.enable_retries()
        self.test_get_gateway_virtual_connection_all_params()

        # Disable retries and run test_get_gateway_virtual_connection_all_params.
        _service.disable_retries()
        self.test_get_gateway_virtual_connection_all_params()

    @responses.activate
    def test_get_gateway_virtual_connection_value_error(self):
        """
        test_get_gateway_virtual_connection_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/virtual_connections/0a06fb9b-820f-4c44-8a31-77f1f0806d28')
        mock_response = '{"created_at": "2019-01-01T12:00:00.000Z", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "newVC", "network_account": "00aa14a2e0fb102c8995ebefff865555", "network_id": "crn:v1:bluemix:public:is:us-east:a/28e4d90ac7504be69447111122223333::vpc:aaa81ac8-5e96-42a0-a4b7-6c2e2d1bbbbb", "status": "attached", "type": "vpc"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "gateway_id": gateway_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_gateway_virtual_connection(**req_copy)

    def test_get_gateway_virtual_connection_value_error_with_retries(self):
        # Enable retries and run test_get_gateway_virtual_connection_value_error.
        _service.enable_retries()
        self.test_get_gateway_virtual_connection_value_error()

        # Disable retries and run test_get_gateway_virtual_connection_value_error.
        _service.disable_retries()
        self.test_get_gateway_virtual_connection_value_error()


class TestUpdateGatewayVirtualConnection:
    """
    Test Class for update_gateway_virtual_connection
    """

    @responses.activate
    def test_update_gateway_virtual_connection_all_params(self):
        """
        update_gateway_virtual_connection()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/virtual_connections/0a06fb9b-820f-4c44-8a31-77f1f0806d28')
        mock_response = '{"created_at": "2019-01-01T12:00:00.000Z", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "newVC", "network_account": "00aa14a2e0fb102c8995ebefff865555", "network_id": "crn:v1:bluemix:public:is:us-east:a/28e4d90ac7504be69447111122223333::vpc:aaa81ac8-5e96-42a0-a4b7-6c2e2d1bbbbb", "status": "attached", "type": "vpc"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a GatewayVirtualConnectionPatchTemplate model
        gateway_virtual_connection_patch_template_model = {}
        gateway_virtual_connection_patch_template_model['name'] = 'newConnectionName'
        gateway_virtual_connection_patch_template_model['status'] = 'attached'

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        gateway_virtual_connection_patch_template = gateway_virtual_connection_patch_template_model

        # Invoke method
        response = _service.update_gateway_virtual_connection(
            gateway_id,
            id,
            gateway_virtual_connection_patch_template,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == gateway_virtual_connection_patch_template

    def test_update_gateway_virtual_connection_all_params_with_retries(self):
        # Enable retries and run test_update_gateway_virtual_connection_all_params.
        _service.enable_retries()
        self.test_update_gateway_virtual_connection_all_params()

        # Disable retries and run test_update_gateway_virtual_connection_all_params.
        _service.disable_retries()
        self.test_update_gateway_virtual_connection_all_params()

    @responses.activate
    def test_update_gateway_virtual_connection_value_error(self):
        """
        test_update_gateway_virtual_connection_value_error()
        """
        # Set up mock
        url = preprocess_url('/gateways/0a06fb9b-820f-4c44-8a31-77f1f0806d28/virtual_connections/0a06fb9b-820f-4c44-8a31-77f1f0806d28')
        mock_response = '{"created_at": "2019-01-01T12:00:00.000Z", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "newVC", "network_account": "00aa14a2e0fb102c8995ebefff865555", "network_id": "crn:v1:bluemix:public:is:us-east:a/28e4d90ac7504be69447111122223333::vpc:aaa81ac8-5e96-42a0-a4b7-6c2e2d1bbbbb", "status": "attached", "type": "vpc"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a GatewayVirtualConnectionPatchTemplate model
        gateway_virtual_connection_patch_template_model = {}
        gateway_virtual_connection_patch_template_model['name'] = 'newConnectionName'
        gateway_virtual_connection_patch_template_model['status'] = 'attached'

        # Set up parameter values
        gateway_id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'
        gateway_virtual_connection_patch_template = gateway_virtual_connection_patch_template_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "gateway_id": gateway_id,
            "id": id,
            "gateway_virtual_connection_patch_template": gateway_virtual_connection_patch_template,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_gateway_virtual_connection(**req_copy)

    def test_update_gateway_virtual_connection_value_error_with_retries(self):
        # Enable retries and run test_update_gateway_virtual_connection_value_error.
        _service.enable_retries()
        self.test_update_gateway_virtual_connection_value_error()

        # Disable retries and run test_update_gateway_virtual_connection_value_error.
        _service.disable_retries()
        self.test_update_gateway_virtual_connection_value_error()


# endregion
##############################################################################
# End of Service: VirtualConnections
##############################################################################

##############################################################################
# Start of Service: OfferingInformation
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

        service = DirectLinkV1.new_instance(
            version=version,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DirectLinkV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DirectLinkV1.new_instance(
                version=version,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = DirectLinkV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='version must be provided'):
            service = DirectLinkV1.new_instance(
                version=None,
            )


class TestListOfferingTypeLocations:
    """
    Test Class for list_offering_type_locations
    """

    @responses.activate
    def test_list_offering_type_locations_all_params(self):
        """
        list_offering_type_locations()
        """
        # Set up mock
        url = preprocess_url('/offering_types/dedicated/locations')
        mock_response = '{"locations": [{"billing_location": "us", "building_colocation_owner": "MyProvider", "display_name": "Dallas 9", "location_type": "PoP", "macsec_enabled": false, "market": "Dallas", "market_geography": "N/S America", "mzr": true, "name": "dal03", "offering_type": "dedicated", "provision_enabled": true, "vpc_region": "us-south"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        offering_type = 'dedicated'

        # Invoke method
        response = _service.list_offering_type_locations(
            offering_type,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_offering_type_locations_all_params_with_retries(self):
        # Enable retries and run test_list_offering_type_locations_all_params.
        _service.enable_retries()
        self.test_list_offering_type_locations_all_params()

        # Disable retries and run test_list_offering_type_locations_all_params.
        _service.disable_retries()
        self.test_list_offering_type_locations_all_params()

    @responses.activate
    def test_list_offering_type_locations_value_error(self):
        """
        test_list_offering_type_locations_value_error()
        """
        # Set up mock
        url = preprocess_url('/offering_types/dedicated/locations')
        mock_response = '{"locations": [{"billing_location": "us", "building_colocation_owner": "MyProvider", "display_name": "Dallas 9", "location_type": "PoP", "macsec_enabled": false, "market": "Dallas", "market_geography": "N/S America", "mzr": true, "name": "dal03", "offering_type": "dedicated", "provision_enabled": true, "vpc_region": "us-south"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        offering_type = 'dedicated'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "offering_type": offering_type,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_offering_type_locations(**req_copy)

    def test_list_offering_type_locations_value_error_with_retries(self):
        # Enable retries and run test_list_offering_type_locations_value_error.
        _service.enable_retries()
        self.test_list_offering_type_locations_value_error()

        # Disable retries and run test_list_offering_type_locations_value_error.
        _service.disable_retries()
        self.test_list_offering_type_locations_value_error()


class TestListOfferingTypeLocationCrossConnectRouters:
    """
    Test Class for list_offering_type_location_cross_connect_routers
    """

    @responses.activate
    def test_list_offering_type_location_cross_connect_routers_all_params(self):
        """
        list_offering_type_location_cross_connect_routers()
        """
        # Set up mock
        url = preprocess_url('/offering_types/dedicated/locations/testString/cross_connect_routers')
        mock_response = '{"cross_connect_routers": [{"capabilities": ["capabilities"], "router_name": "xcr01.dal03", "total_connections": 1}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        offering_type = 'dedicated'
        location_name = 'testString'

        # Invoke method
        response = _service.list_offering_type_location_cross_connect_routers(
            offering_type,
            location_name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_offering_type_location_cross_connect_routers_all_params_with_retries(self):
        # Enable retries and run test_list_offering_type_location_cross_connect_routers_all_params.
        _service.enable_retries()
        self.test_list_offering_type_location_cross_connect_routers_all_params()

        # Disable retries and run test_list_offering_type_location_cross_connect_routers_all_params.
        _service.disable_retries()
        self.test_list_offering_type_location_cross_connect_routers_all_params()

    @responses.activate
    def test_list_offering_type_location_cross_connect_routers_value_error(self):
        """
        test_list_offering_type_location_cross_connect_routers_value_error()
        """
        # Set up mock
        url = preprocess_url('/offering_types/dedicated/locations/testString/cross_connect_routers')
        mock_response = '{"cross_connect_routers": [{"capabilities": ["capabilities"], "router_name": "xcr01.dal03", "total_connections": 1}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        offering_type = 'dedicated'
        location_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "offering_type": offering_type,
            "location_name": location_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_offering_type_location_cross_connect_routers(**req_copy)

    def test_list_offering_type_location_cross_connect_routers_value_error_with_retries(self):
        # Enable retries and run test_list_offering_type_location_cross_connect_routers_value_error.
        _service.enable_retries()
        self.test_list_offering_type_location_cross_connect_routers_value_error()

        # Disable retries and run test_list_offering_type_location_cross_connect_routers_value_error.
        _service.disable_retries()
        self.test_list_offering_type_location_cross_connect_routers_value_error()


class TestListOfferingTypeSpeeds:
    """
    Test Class for list_offering_type_speeds
    """

    @responses.activate
    def test_list_offering_type_speeds_all_params(self):
        """
        list_offering_type_speeds()
        """
        # Set up mock
        url = preprocess_url('/offering_types/dedicated/speeds')
        mock_response = '{"speeds": [{"capabilities": ["capabilities"], "link_speed": 2000, "macsec_enabled": false}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        offering_type = 'dedicated'

        # Invoke method
        response = _service.list_offering_type_speeds(
            offering_type,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_offering_type_speeds_all_params_with_retries(self):
        # Enable retries and run test_list_offering_type_speeds_all_params.
        _service.enable_retries()
        self.test_list_offering_type_speeds_all_params()

        # Disable retries and run test_list_offering_type_speeds_all_params.
        _service.disable_retries()
        self.test_list_offering_type_speeds_all_params()

    @responses.activate
    def test_list_offering_type_speeds_value_error(self):
        """
        test_list_offering_type_speeds_value_error()
        """
        # Set up mock
        url = preprocess_url('/offering_types/dedicated/speeds')
        mock_response = '{"speeds": [{"capabilities": ["capabilities"], "link_speed": 2000, "macsec_enabled": false}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        offering_type = 'dedicated'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "offering_type": offering_type,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_offering_type_speeds(**req_copy)

    def test_list_offering_type_speeds_value_error_with_retries(self):
        # Enable retries and run test_list_offering_type_speeds_value_error.
        _service.enable_retries()
        self.test_list_offering_type_speeds_value_error()

        # Disable retries and run test_list_offering_type_speeds_value_error.
        _service.disable_retries()
        self.test_list_offering_type_speeds_value_error()


# endregion
##############################################################################
# End of Service: OfferingInformation
##############################################################################

##############################################################################
# Start of Service: Ports
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

        service = DirectLinkV1.new_instance(
            version=version,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DirectLinkV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DirectLinkV1.new_instance(
                version=version,
                service_name='TEST_SERVICE_NOT_FOUND',
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = DirectLinkV1.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='version must be provided'):
            service = DirectLinkV1.new_instance(
                version=None,
            )


class TestListPorts:
    """
    Test Class for list_ports
    """

    @responses.activate
    def test_list_ports_all_params(self):
        """
        list_ports()
        """
        # Set up mock
        url = preprocess_url('/ports')
        mock_response = '{"first": {"href": "https://directlink.cloud.ibm.com/v1/ports?limit=100"}, "limit": 100, "next": {"href": "https://directlink.cloud.ibm.com/v1/ports?start=9d5a91a3e2cbd233b5a5b33436855ed1&limit=100", "start": "9d5a91a3e2cbd233b5a5b33436855ed1"}, "total_count": 132, "ports": [{"direct_link_count": 1, "id": "01122b9b-820f-4c44-8a31-77f1f0806765", "label": "XCR-FRK-CS-SEC-01", "location_display_name": "Dallas 03", "location_name": "dal03", "provider_name": "provider_1", "supported_link_speeds": [21]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        start = 'testString'
        limit = 50
        location_name = 'testString'

        # Invoke method
        response = _service.list_ports(
            start=start,
            limit=limit,
            location_name=location_name,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'start={}'.format(start) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'location_name={}'.format(location_name) in query_string

    def test_list_ports_all_params_with_retries(self):
        # Enable retries and run test_list_ports_all_params.
        _service.enable_retries()
        self.test_list_ports_all_params()

        # Disable retries and run test_list_ports_all_params.
        _service.disable_retries()
        self.test_list_ports_all_params()

    @responses.activate
    def test_list_ports_required_params(self):
        """
        test_list_ports_required_params()
        """
        # Set up mock
        url = preprocess_url('/ports')
        mock_response = '{"first": {"href": "https://directlink.cloud.ibm.com/v1/ports?limit=100"}, "limit": 100, "next": {"href": "https://directlink.cloud.ibm.com/v1/ports?start=9d5a91a3e2cbd233b5a5b33436855ed1&limit=100", "start": "9d5a91a3e2cbd233b5a5b33436855ed1"}, "total_count": 132, "ports": [{"direct_link_count": 1, "id": "01122b9b-820f-4c44-8a31-77f1f0806765", "label": "XCR-FRK-CS-SEC-01", "location_display_name": "Dallas 03", "location_name": "dal03", "provider_name": "provider_1", "supported_link_speeds": [21]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Invoke method
        response = _service.list_ports()

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_ports_required_params_with_retries(self):
        # Enable retries and run test_list_ports_required_params.
        _service.enable_retries()
        self.test_list_ports_required_params()

        # Disable retries and run test_list_ports_required_params.
        _service.disable_retries()
        self.test_list_ports_required_params()

    @responses.activate
    def test_list_ports_value_error(self):
        """
        test_list_ports_value_error()
        """
        # Set up mock
        url = preprocess_url('/ports')
        mock_response = '{"first": {"href": "https://directlink.cloud.ibm.com/v1/ports?limit=100"}, "limit": 100, "next": {"href": "https://directlink.cloud.ibm.com/v1/ports?start=9d5a91a3e2cbd233b5a5b33436855ed1&limit=100", "start": "9d5a91a3e2cbd233b5a5b33436855ed1"}, "total_count": 132, "ports": [{"direct_link_count": 1, "id": "01122b9b-820f-4c44-8a31-77f1f0806765", "label": "XCR-FRK-CS-SEC-01", "location_display_name": "Dallas 03", "location_name": "dal03", "provider_name": "provider_1", "supported_link_speeds": [21]}]}'
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
                _service.list_ports(**req_copy)

    def test_list_ports_value_error_with_retries(self):
        # Enable retries and run test_list_ports_value_error.
        _service.enable_retries()
        self.test_list_ports_value_error()

        # Disable retries and run test_list_ports_value_error.
        _service.disable_retries()
        self.test_list_ports_value_error()

    @responses.activate
    def test_list_ports_with_pager_get_next(self):
        """
        test_list_ports_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/ports')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"ports":[{"direct_link_count":1,"id":"01122b9b-820f-4c44-8a31-77f1f0806765","label":"XCR-FRK-CS-SEC-01","location_display_name":"Dallas 03","location_name":"dal03","provider_name":"provider_1","supported_link_speeds":[21]}]}'
        mock_response2 = '{"total_count":2,"limit":1,"ports":[{"direct_link_count":1,"id":"01122b9b-820f-4c44-8a31-77f1f0806765","label":"XCR-FRK-CS-SEC-01","location_display_name":"Dallas 03","location_name":"dal03","provider_name":"provider_1","supported_link_speeds":[21]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = PortsPager(
            client=_service,
            limit=10,
            location_name='testString',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_ports_with_pager_get_all(self):
        """
        test_list_ports_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/ports')
        mock_response1 = '{"next":{"start":"1"},"total_count":2,"limit":1,"ports":[{"direct_link_count":1,"id":"01122b9b-820f-4c44-8a31-77f1f0806765","label":"XCR-FRK-CS-SEC-01","location_display_name":"Dallas 03","location_name":"dal03","provider_name":"provider_1","supported_link_speeds":[21]}]}'
        mock_response2 = '{"total_count":2,"limit":1,"ports":[{"direct_link_count":1,"id":"01122b9b-820f-4c44-8a31-77f1f0806765","label":"XCR-FRK-CS-SEC-01","location_display_name":"Dallas 03","location_name":"dal03","provider_name":"provider_1","supported_link_speeds":[21]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = PortsPager(
            client=_service,
            limit=10,
            location_name='testString',
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestGetPort:
    """
    Test Class for get_port
    """

    @responses.activate
    def test_get_port_all_params(self):
        """
        get_port()
        """
        # Set up mock
        url = preprocess_url('/ports/0a06fb9b-820f-4c44-8a31-77f1f0806d28')
        mock_response = '{"direct_link_count": 1, "id": "01122b9b-820f-4c44-8a31-77f1f0806765", "label": "XCR-FRK-CS-SEC-01", "location_display_name": "Dallas 03", "location_name": "dal03", "provider_name": "provider_1", "supported_link_speeds": [21]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Invoke method
        response = _service.get_port(
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_port_all_params_with_retries(self):
        # Enable retries and run test_get_port_all_params.
        _service.enable_retries()
        self.test_get_port_all_params()

        # Disable retries and run test_get_port_all_params.
        _service.disable_retries()
        self.test_get_port_all_params()

    @responses.activate
    def test_get_port_value_error(self):
        """
        test_get_port_value_error()
        """
        # Set up mock
        url = preprocess_url('/ports/0a06fb9b-820f-4c44-8a31-77f1f0806d28')
        mock_response = '{"direct_link_count": 1, "id": "01122b9b-820f-4c44-8a31-77f1f0806765", "label": "XCR-FRK-CS-SEC-01", "location_display_name": "Dallas 03", "location_name": "dal03", "provider_name": "provider_1", "supported_link_speeds": [21]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        id = '0a06fb9b-820f-4c44-8a31-77f1f0806d28'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_port(**req_copy)

    def test_get_port_value_error_with_retries(self):
        # Enable retries and run test_get_port_value_error.
        _service.enable_retries()
        self.test_get_port_value_error()

        # Disable retries and run test_get_port_value_error.
        _service.disable_retries()
        self.test_get_port_value_error()


# endregion
##############################################################################
# End of Service: Ports
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_AsPrepend:
    """
    Test Class for AsPrepend
    """

    def test_as_prepend_serialization(self):
        """
        Test serialization/deserialization for AsPrepend
        """

        # Construct a json representation of a AsPrepend model
        as_prepend_model_json = {}
        as_prepend_model_json['created_at'] = '2019-01-01T12:00:00Z'
        as_prepend_model_json['id'] = 'ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        as_prepend_model_json['length'] = 4
        as_prepend_model_json['policy'] = 'import'
        as_prepend_model_json['prefix'] = '172.17.0.0/16'
        as_prepend_model_json['specific_prefixes'] = ['192.168.3.0/24']
        as_prepend_model_json['updated_at'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of AsPrepend by calling from_dict on the json representation
        as_prepend_model = AsPrepend.from_dict(as_prepend_model_json)
        assert as_prepend_model != False

        # Construct a model instance of AsPrepend by calling from_dict on the json representation
        as_prepend_model_dict = AsPrepend.from_dict(as_prepend_model_json).__dict__
        as_prepend_model2 = AsPrepend(**as_prepend_model_dict)

        # Verify the model instances are equivalent
        assert as_prepend_model == as_prepend_model2

        # Convert model instance back to dict and verify no loss of data
        as_prepend_model_json2 = as_prepend_model.to_dict()
        assert as_prepend_model_json2 == as_prepend_model_json


class TestModel_AsPrependCollection:
    """
    Test Class for AsPrependCollection
    """

    def test_as_prepend_collection_serialization(self):
        """
        Test serialization/deserialization for AsPrependCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        as_prepend_entry_model = {}  # AsPrependEntry
        as_prepend_entry_model['created_at'] = '2019-01-01T12:00:00Z'
        as_prepend_entry_model['id'] = 'ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        as_prepend_entry_model['length'] = 4
        as_prepend_entry_model['policy'] = 'import'
        as_prepend_entry_model['specific_prefixes'] = ['192.168.3.0/24']
        as_prepend_entry_model['updated_at'] = '2019-01-01T12:00:00Z'

        # Construct a json representation of a AsPrependCollection model
        as_prepend_collection_model_json = {}
        as_prepend_collection_model_json['as_prepends'] = [as_prepend_entry_model]

        # Construct a model instance of AsPrependCollection by calling from_dict on the json representation
        as_prepend_collection_model = AsPrependCollection.from_dict(as_prepend_collection_model_json)
        assert as_prepend_collection_model != False

        # Construct a model instance of AsPrependCollection by calling from_dict on the json representation
        as_prepend_collection_model_dict = AsPrependCollection.from_dict(as_prepend_collection_model_json).__dict__
        as_prepend_collection_model2 = AsPrependCollection(**as_prepend_collection_model_dict)

        # Verify the model instances are equivalent
        assert as_prepend_collection_model == as_prepend_collection_model2

        # Convert model instance back to dict and verify no loss of data
        as_prepend_collection_model_json2 = as_prepend_collection_model.to_dict()
        assert as_prepend_collection_model_json2 == as_prepend_collection_model_json


class TestModel_AsPrependEntry:
    """
    Test Class for AsPrependEntry
    """

    def test_as_prepend_entry_serialization(self):
        """
        Test serialization/deserialization for AsPrependEntry
        """

        # Construct a json representation of a AsPrependEntry model
        as_prepend_entry_model_json = {}
        as_prepend_entry_model_json['created_at'] = '2019-01-01T12:00:00Z'
        as_prepend_entry_model_json['id'] = 'ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        as_prepend_entry_model_json['length'] = 4
        as_prepend_entry_model_json['policy'] = 'import'
        as_prepend_entry_model_json['specific_prefixes'] = ['192.168.3.0/24']
        as_prepend_entry_model_json['updated_at'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of AsPrependEntry by calling from_dict on the json representation
        as_prepend_entry_model = AsPrependEntry.from_dict(as_prepend_entry_model_json)
        assert as_prepend_entry_model != False

        # Construct a model instance of AsPrependEntry by calling from_dict on the json representation
        as_prepend_entry_model_dict = AsPrependEntry.from_dict(as_prepend_entry_model_json).__dict__
        as_prepend_entry_model2 = AsPrependEntry(**as_prepend_entry_model_dict)

        # Verify the model instances are equivalent
        assert as_prepend_entry_model == as_prepend_entry_model2

        # Convert model instance back to dict and verify no loss of data
        as_prepend_entry_model_json2 = as_prepend_entry_model.to_dict()
        assert as_prepend_entry_model_json2 == as_prepend_entry_model_json


class TestModel_AsPrependPrefixArrayTemplate:
    """
    Test Class for AsPrependPrefixArrayTemplate
    """

    def test_as_prepend_prefix_array_template_serialization(self):
        """
        Test serialization/deserialization for AsPrependPrefixArrayTemplate
        """

        # Construct a json representation of a AsPrependPrefixArrayTemplate model
        as_prepend_prefix_array_template_model_json = {}
        as_prepend_prefix_array_template_model_json['length'] = 4
        as_prepend_prefix_array_template_model_json['policy'] = 'import'
        as_prepend_prefix_array_template_model_json['specific_prefixes'] = ['192.168.3.0/24']

        # Construct a model instance of AsPrependPrefixArrayTemplate by calling from_dict on the json representation
        as_prepend_prefix_array_template_model = AsPrependPrefixArrayTemplate.from_dict(as_prepend_prefix_array_template_model_json)
        assert as_prepend_prefix_array_template_model != False

        # Construct a model instance of AsPrependPrefixArrayTemplate by calling from_dict on the json representation
        as_prepend_prefix_array_template_model_dict = AsPrependPrefixArrayTemplate.from_dict(as_prepend_prefix_array_template_model_json).__dict__
        as_prepend_prefix_array_template_model2 = AsPrependPrefixArrayTemplate(**as_prepend_prefix_array_template_model_dict)

        # Verify the model instances are equivalent
        assert as_prepend_prefix_array_template_model == as_prepend_prefix_array_template_model2

        # Convert model instance back to dict and verify no loss of data
        as_prepend_prefix_array_template_model_json2 = as_prepend_prefix_array_template_model.to_dict()
        assert as_prepend_prefix_array_template_model_json2 == as_prepend_prefix_array_template_model_json


class TestModel_AsPrependTemplate:
    """
    Test Class for AsPrependTemplate
    """

    def test_as_prepend_template_serialization(self):
        """
        Test serialization/deserialization for AsPrependTemplate
        """

        # Construct a json representation of a AsPrependTemplate model
        as_prepend_template_model_json = {}
        as_prepend_template_model_json['length'] = 4
        as_prepend_template_model_json['policy'] = 'import'
        as_prepend_template_model_json['prefix'] = '172.17.0.0/16'
        as_prepend_template_model_json['specific_prefixes'] = ['192.168.3.0/24']

        # Construct a model instance of AsPrependTemplate by calling from_dict on the json representation
        as_prepend_template_model = AsPrependTemplate.from_dict(as_prepend_template_model_json)
        assert as_prepend_template_model != False

        # Construct a model instance of AsPrependTemplate by calling from_dict on the json representation
        as_prepend_template_model_dict = AsPrependTemplate.from_dict(as_prepend_template_model_json).__dict__
        as_prepend_template_model2 = AsPrependTemplate(**as_prepend_template_model_dict)

        # Verify the model instances are equivalent
        assert as_prepend_template_model == as_prepend_template_model2

        # Convert model instance back to dict and verify no loss of data
        as_prepend_template_model_json2 = as_prepend_template_model.to_dict()
        assert as_prepend_template_model_json2 == as_prepend_template_model_json


class TestModel_CrossConnectRouter:
    """
    Test Class for CrossConnectRouter
    """

    def test_cross_connect_router_serialization(self):
        """
        Test serialization/deserialization for CrossConnectRouter
        """

        # Construct a json representation of a CrossConnectRouter model
        cross_connect_router_model_json = {}
        cross_connect_router_model_json['capabilities'] = ['testString']
        cross_connect_router_model_json['router_name'] = 'xcr01.dal03'
        cross_connect_router_model_json['total_connections'] = 1

        # Construct a model instance of CrossConnectRouter by calling from_dict on the json representation
        cross_connect_router_model = CrossConnectRouter.from_dict(cross_connect_router_model_json)
        assert cross_connect_router_model != False

        # Construct a model instance of CrossConnectRouter by calling from_dict on the json representation
        cross_connect_router_model_dict = CrossConnectRouter.from_dict(cross_connect_router_model_json).__dict__
        cross_connect_router_model2 = CrossConnectRouter(**cross_connect_router_model_dict)

        # Verify the model instances are equivalent
        assert cross_connect_router_model == cross_connect_router_model2

        # Convert model instance back to dict and verify no loss of data
        cross_connect_router_model_json2 = cross_connect_router_model.to_dict()
        assert cross_connect_router_model_json2 == cross_connect_router_model_json


class TestModel_ExportRouteFilterCollection:
    """
    Test Class for ExportRouteFilterCollection
    """

    def test_export_route_filter_collection_serialization(self):
        """
        Test serialization/deserialization for ExportRouteFilterCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        route_filter_model = {}  # RouteFilter
        route_filter_model['action'] = 'permit'
        route_filter_model['before'] = '1a15dcab-7e40-45e1-b7c5-bc690eaa9782'
        route_filter_model['created_at'] = '2020-11-02T20:40:29.622000Z'
        route_filter_model['ge'] = 25
        route_filter_model['id'] = '1a15dcab-7e40-45e1-b7c5-bc690eaa9782'
        route_filter_model['le'] = 30
        route_filter_model['prefix'] = '192.168.100.0/24'
        route_filter_model['updated_at'] = '2020-11-02T20:40:29.622000Z'

        # Construct a json representation of a ExportRouteFilterCollection model
        export_route_filter_collection_model_json = {}
        export_route_filter_collection_model_json['export_route_filters'] = [route_filter_model]

        # Construct a model instance of ExportRouteFilterCollection by calling from_dict on the json representation
        export_route_filter_collection_model = ExportRouteFilterCollection.from_dict(export_route_filter_collection_model_json)
        assert export_route_filter_collection_model != False

        # Construct a model instance of ExportRouteFilterCollection by calling from_dict on the json representation
        export_route_filter_collection_model_dict = ExportRouteFilterCollection.from_dict(export_route_filter_collection_model_json).__dict__
        export_route_filter_collection_model2 = ExportRouteFilterCollection(**export_route_filter_collection_model_dict)

        # Verify the model instances are equivalent
        assert export_route_filter_collection_model == export_route_filter_collection_model2

        # Convert model instance back to dict and verify no loss of data
        export_route_filter_collection_model_json2 = export_route_filter_collection_model.to_dict()
        assert export_route_filter_collection_model_json2 == export_route_filter_collection_model_json


class TestModel_Gateway:
    """
    Test Class for Gateway
    """

    def test_gateway_serialization(self):
        """
        Test serialization/deserialization for Gateway
        """

        # Construct dict forms of any model objects needed in order to build this model.

        as_prepend_model = {}  # AsPrepend
        as_prepend_model['created_at'] = '2019-01-01T12:00:00Z'
        as_prepend_model['id'] = 'ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        as_prepend_model['length'] = 4
        as_prepend_model['policy'] = 'import'
        as_prepend_model['prefix'] = '172.17.0.0/16'
        as_prepend_model['specific_prefixes'] = ['192.168.3.0/24']
        as_prepend_model['updated_at'] = '2019-01-01T12:00:00Z'

        authentication_key_reference_model = {}  # AuthenticationKeyReferenceKeyProtectAuthenticationKeyReference
        authentication_key_reference_model['crn'] = 'crn:v1:bluemix:public:kms:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        gateway_bfd_config_model = {}  # GatewayBfdConfig
        gateway_bfd_config_model['bfd_status'] = 'up'
        gateway_bfd_config_model['bfd_status_updated_at'] = '2020-08-20T06:58:41.909000Z'
        gateway_bfd_config_model['interval'] = 2000
        gateway_bfd_config_model['multiplier'] = 10

        gateway_change_request_model = {}  # GatewayChangeRequestGatewayClientGatewayCreate
        gateway_change_request_model['type'] = 'create_gateway'

        gateway_macsec_status_reason_model = {}  # GatewayMacsecStatusReason
        gateway_macsec_status_reason_model['code'] = 'macsec_cak_failed'
        gateway_macsec_status_reason_model['message'] = 'The `authentication_key` failed configuration.'
        gateway_macsec_status_reason_model['more_info'] = 'https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK'

        gateway_macsec_reference_model = {}  # GatewayMacsecReference
        gateway_macsec_reference_model['active'] = True
        gateway_macsec_reference_model['security_policy'] = 'must_secure'
        gateway_macsec_reference_model['status'] = 'secured'
        gateway_macsec_reference_model['status_reasons'] = [gateway_macsec_status_reason_model]

        gateway_status_reason_model = {}  # GatewayStatusReason
        gateway_status_reason_model['code'] = 'authentication_key_failed'
        gateway_status_reason_model['message'] = 'The `authentication_key` failed configuration.'
        gateway_status_reason_model['more_info'] = 'https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK'

        gateway_port_reference_model = {}  # GatewayPortReference
        gateway_port_reference_model['id'] = '54321b1a-fee4-41c7-9e11-9cd99e000aaa'

        resource_group_reference_model = {}  # ResourceGroupReference
        resource_group_reference_model['id'] = '56969d6043e9465c883cb9f7363e78e8'

        # Construct a json representation of a Gateway model
        gateway_model_json = {}
        gateway_model_json['as_prepends'] = [as_prepend_model]
        gateway_model_json['authentication_key'] = authentication_key_reference_model
        gateway_model_json['bfd_config'] = gateway_bfd_config_model
        gateway_model_json['bgp_asn'] = 64999
        gateway_model_json['bgp_base_cidr'] = 'testString'
        gateway_model_json['bgp_cer_cidr'] = '10.254.30.78/30'
        gateway_model_json['bgp_ibm_asn'] = 13884
        gateway_model_json['bgp_ibm_cidr'] = '10.254.30.77/30'
        gateway_model_json['bgp_status'] = 'active'
        gateway_model_json['bgp_status_updated_at'] = '2020-08-20T06:58:41.909000Z'
        gateway_model_json['carrier_name'] = 'myCarrierName'
        gateway_model_json['change_request'] = gateway_change_request_model
        gateway_model_json['completion_notice_reject_reason'] = 'The completion notice file was blank'
        gateway_model_json['connection_mode'] = 'transit'
        gateway_model_json['created_at'] = '2019-01-01T12:00:00Z'
        gateway_model_json['crn'] = 'crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::dedicated:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        gateway_model_json['cross_account'] = False
        gateway_model_json['cross_connect_router'] = 'xcr01.dal03'
        gateway_model_json['customer_name'] = 'newCustomerName'
        gateway_model_json['default_export_route_filter'] = 'permit'
        gateway_model_json['default_import_route_filter'] = 'permit'
        gateway_model_json['global'] = True
        gateway_model_json['id'] = 'ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        gateway_model_json['link_status'] = 'up'
        gateway_model_json['link_status_updated_at'] = '2020-08-20T06:58:41.909000Z'
        gateway_model_json['location_display_name'] = 'Dallas 03'
        gateway_model_json['location_name'] = 'dal03'
        gateway_model_json['macsec'] = gateway_macsec_reference_model
        gateway_model_json['macsec_capability'] = 'non_macsec'
        gateway_model_json['metered'] = False
        gateway_model_json['name'] = 'myGateway'
        gateway_model_json['operational_status'] = 'awaiting_completion_notice'
        gateway_model_json['operational_status_reasons'] = [gateway_status_reason_model]
        gateway_model_json['patch_panel_completion_notice'] = 'patch panel configuration details'
        gateway_model_json['port'] = gateway_port_reference_model
        gateway_model_json['provider_api_managed'] = False
        gateway_model_json['resource_group'] = resource_group_reference_model
        gateway_model_json['speed_mbps'] = 1000
        gateway_model_json['type'] = 'dedicated'
        gateway_model_json['vlan'] = 10

        # Construct a model instance of Gateway by calling from_dict on the json representation
        gateway_model = Gateway.from_dict(gateway_model_json)
        assert gateway_model != False

        # Construct a model instance of Gateway by calling from_dict on the json representation
        gateway_model_dict = Gateway.from_dict(gateway_model_json).__dict__
        gateway_model2 = Gateway(**gateway_model_dict)

        # Verify the model instances are equivalent
        assert gateway_model == gateway_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_model_json2 = gateway_model.to_dict()
        assert gateway_model_json2 == gateway_model_json


class TestModel_GatewayBfdConfig:
    """
    Test Class for GatewayBfdConfig
    """

    def test_gateway_bfd_config_serialization(self):
        """
        Test serialization/deserialization for GatewayBfdConfig
        """

        # Construct a json representation of a GatewayBfdConfig model
        gateway_bfd_config_model_json = {}
        gateway_bfd_config_model_json['bfd_status'] = 'up'
        gateway_bfd_config_model_json['bfd_status_updated_at'] = '2020-08-20T06:58:41.909000Z'
        gateway_bfd_config_model_json['interval'] = 2000
        gateway_bfd_config_model_json['multiplier'] = 10

        # Construct a model instance of GatewayBfdConfig by calling from_dict on the json representation
        gateway_bfd_config_model = GatewayBfdConfig.from_dict(gateway_bfd_config_model_json)
        assert gateway_bfd_config_model != False

        # Construct a model instance of GatewayBfdConfig by calling from_dict on the json representation
        gateway_bfd_config_model_dict = GatewayBfdConfig.from_dict(gateway_bfd_config_model_json).__dict__
        gateway_bfd_config_model2 = GatewayBfdConfig(**gateway_bfd_config_model_dict)

        # Verify the model instances are equivalent
        assert gateway_bfd_config_model == gateway_bfd_config_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_bfd_config_model_json2 = gateway_bfd_config_model.to_dict()
        assert gateway_bfd_config_model_json2 == gateway_bfd_config_model_json


class TestModel_GatewayBfdConfigActionTemplate:
    """
    Test Class for GatewayBfdConfigActionTemplate
    """

    def test_gateway_bfd_config_action_template_serialization(self):
        """
        Test serialization/deserialization for GatewayBfdConfigActionTemplate
        """

        # Construct a json representation of a GatewayBfdConfigActionTemplate model
        gateway_bfd_config_action_template_model_json = {}
        gateway_bfd_config_action_template_model_json['interval'] = 2000
        gateway_bfd_config_action_template_model_json['multiplier'] = 10

        # Construct a model instance of GatewayBfdConfigActionTemplate by calling from_dict on the json representation
        gateway_bfd_config_action_template_model = GatewayBfdConfigActionTemplate.from_dict(gateway_bfd_config_action_template_model_json)
        assert gateway_bfd_config_action_template_model != False

        # Construct a model instance of GatewayBfdConfigActionTemplate by calling from_dict on the json representation
        gateway_bfd_config_action_template_model_dict = GatewayBfdConfigActionTemplate.from_dict(gateway_bfd_config_action_template_model_json).__dict__
        gateway_bfd_config_action_template_model2 = GatewayBfdConfigActionTemplate(**gateway_bfd_config_action_template_model_dict)

        # Verify the model instances are equivalent
        assert gateway_bfd_config_action_template_model == gateway_bfd_config_action_template_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_bfd_config_action_template_model_json2 = gateway_bfd_config_action_template_model.to_dict()
        assert gateway_bfd_config_action_template_model_json2 == gateway_bfd_config_action_template_model_json


class TestModel_GatewayBfdConfigTemplate:
    """
    Test Class for GatewayBfdConfigTemplate
    """

    def test_gateway_bfd_config_template_serialization(self):
        """
        Test serialization/deserialization for GatewayBfdConfigTemplate
        """

        # Construct a json representation of a GatewayBfdConfigTemplate model
        gateway_bfd_config_template_model_json = {}
        gateway_bfd_config_template_model_json['interval'] = 2000
        gateway_bfd_config_template_model_json['multiplier'] = 10

        # Construct a model instance of GatewayBfdConfigTemplate by calling from_dict on the json representation
        gateway_bfd_config_template_model = GatewayBfdConfigTemplate.from_dict(gateway_bfd_config_template_model_json)
        assert gateway_bfd_config_template_model != False

        # Construct a model instance of GatewayBfdConfigTemplate by calling from_dict on the json representation
        gateway_bfd_config_template_model_dict = GatewayBfdConfigTemplate.from_dict(gateway_bfd_config_template_model_json).__dict__
        gateway_bfd_config_template_model2 = GatewayBfdConfigTemplate(**gateway_bfd_config_template_model_dict)

        # Verify the model instances are equivalent
        assert gateway_bfd_config_template_model == gateway_bfd_config_template_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_bfd_config_template_model_json2 = gateway_bfd_config_template_model.to_dict()
        assert gateway_bfd_config_template_model_json2 == gateway_bfd_config_template_model_json


class TestModel_GatewayBfdPatchTemplate:
    """
    Test Class for GatewayBfdPatchTemplate
    """

    def test_gateway_bfd_patch_template_serialization(self):
        """
        Test serialization/deserialization for GatewayBfdPatchTemplate
        """

        # Construct a json representation of a GatewayBfdPatchTemplate model
        gateway_bfd_patch_template_model_json = {}
        gateway_bfd_patch_template_model_json['interval'] = 2000
        gateway_bfd_patch_template_model_json['multiplier'] = 10

        # Construct a model instance of GatewayBfdPatchTemplate by calling from_dict on the json representation
        gateway_bfd_patch_template_model = GatewayBfdPatchTemplate.from_dict(gateway_bfd_patch_template_model_json)
        assert gateway_bfd_patch_template_model != False

        # Construct a model instance of GatewayBfdPatchTemplate by calling from_dict on the json representation
        gateway_bfd_patch_template_model_dict = GatewayBfdPatchTemplate.from_dict(gateway_bfd_patch_template_model_json).__dict__
        gateway_bfd_patch_template_model2 = GatewayBfdPatchTemplate(**gateway_bfd_patch_template_model_dict)

        # Verify the model instances are equivalent
        assert gateway_bfd_patch_template_model == gateway_bfd_patch_template_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_bfd_patch_template_model_json2 = gateway_bfd_patch_template_model.to_dict()
        assert gateway_bfd_patch_template_model_json2 == gateway_bfd_patch_template_model_json


class TestModel_GatewayCollection:
    """
    Test Class for GatewayCollection
    """

    def test_gateway_collection_serialization(self):
        """
        Test serialization/deserialization for GatewayCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        as_prepend_model = {}  # AsPrepend
        as_prepend_model['created_at'] = '2019-01-01T12:00:00Z'
        as_prepend_model['id'] = 'ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        as_prepend_model['length'] = 4
        as_prepend_model['policy'] = 'import'
        as_prepend_model['prefix'] = '172.17.0.0/16'
        as_prepend_model['specific_prefixes'] = ['192.168.3.0/24']
        as_prepend_model['updated_at'] = '2019-01-01T12:00:00Z'

        authentication_key_reference_model = {}  # AuthenticationKeyReferenceKeyProtectAuthenticationKeyReference
        authentication_key_reference_model['crn'] = 'crn:v1:bluemix:public:kms:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        gateway_bfd_config_model = {}  # GatewayBfdConfig
        gateway_bfd_config_model['bfd_status'] = 'up'
        gateway_bfd_config_model['bfd_status_updated_at'] = '2020-08-20T06:58:41.909000Z'
        gateway_bfd_config_model['interval'] = 2000
        gateway_bfd_config_model['multiplier'] = 10

        gateway_change_request_model = {}  # GatewayChangeRequestGatewayClientGatewayCreate
        gateway_change_request_model['type'] = 'create_gateway'

        gateway_macsec_status_reason_model = {}  # GatewayMacsecStatusReason
        gateway_macsec_status_reason_model['code'] = 'macsec_cak_failed'
        gateway_macsec_status_reason_model['message'] = 'The `authentication_key` failed configuration.'
        gateway_macsec_status_reason_model['more_info'] = 'https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK'

        gateway_macsec_reference_model = {}  # GatewayMacsecReference
        gateway_macsec_reference_model['active'] = True
        gateway_macsec_reference_model['security_policy'] = 'must_secure'
        gateway_macsec_reference_model['status'] = 'secured'
        gateway_macsec_reference_model['status_reasons'] = [gateway_macsec_status_reason_model]

        gateway_status_reason_model = {}  # GatewayStatusReason
        gateway_status_reason_model['code'] = 'authentication_key_failed'
        gateway_status_reason_model['message'] = 'The `authentication_key` failed configuration.'
        gateway_status_reason_model['more_info'] = 'https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK'

        gateway_port_reference_model = {}  # GatewayPortReference
        gateway_port_reference_model['id'] = '54321b1a-fee4-41c7-9e11-9cd99e000aaa'

        resource_group_reference_model = {}  # ResourceGroupReference
        resource_group_reference_model['id'] = '56969d6043e9465c883cb9f7363e78e8'

        gateway_collection_gateways_item_model = {}  # GatewayCollectionGatewaysItemGateway
        gateway_collection_gateways_item_model['as_prepends'] = [as_prepend_model]
        gateway_collection_gateways_item_model['authentication_key'] = authentication_key_reference_model
        gateway_collection_gateways_item_model['bfd_config'] = gateway_bfd_config_model
        gateway_collection_gateways_item_model['bgp_asn'] = 64999
        gateway_collection_gateways_item_model['bgp_base_cidr'] = 'testString'
        gateway_collection_gateways_item_model['bgp_cer_cidr'] = '10.254.30.78/30'
        gateway_collection_gateways_item_model['bgp_ibm_asn'] = 13884
        gateway_collection_gateways_item_model['bgp_ibm_cidr'] = '10.254.30.77/30'
        gateway_collection_gateways_item_model['bgp_status'] = 'active'
        gateway_collection_gateways_item_model['bgp_status_updated_at'] = '2020-08-20T06:58:41.909000Z'
        gateway_collection_gateways_item_model['carrier_name'] = 'myCarrierName'
        gateway_collection_gateways_item_model['change_request'] = gateway_change_request_model
        gateway_collection_gateways_item_model['completion_notice_reject_reason'] = 'The completion notice file was blank'
        gateway_collection_gateways_item_model['connection_mode'] = 'transit'
        gateway_collection_gateways_item_model['created_at'] = '2019-01-01T12:00:00Z'
        gateway_collection_gateways_item_model['crn'] = 'crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::dedicated:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        gateway_collection_gateways_item_model['cross_account'] = False
        gateway_collection_gateways_item_model['cross_connect_router'] = 'xcr01.dal03'
        gateway_collection_gateways_item_model['customer_name'] = 'newCustomerName'
        gateway_collection_gateways_item_model['default_export_route_filter'] = 'permit'
        gateway_collection_gateways_item_model['default_import_route_filter'] = 'permit'
        gateway_collection_gateways_item_model['global'] = True
        gateway_collection_gateways_item_model['id'] = 'ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        gateway_collection_gateways_item_model['link_status'] = 'up'
        gateway_collection_gateways_item_model['link_status_updated_at'] = '2020-08-20T06:58:41.909000Z'
        gateway_collection_gateways_item_model['location_display_name'] = 'Dallas 03'
        gateway_collection_gateways_item_model['location_name'] = 'dal03'
        gateway_collection_gateways_item_model['macsec'] = gateway_macsec_reference_model
        gateway_collection_gateways_item_model['macsec_capability'] = 'non_macsec'
        gateway_collection_gateways_item_model['metered'] = False
        gateway_collection_gateways_item_model['name'] = 'myGateway'
        gateway_collection_gateways_item_model['operational_status'] = 'awaiting_completion_notice'
        gateway_collection_gateways_item_model['operational_status_reasons'] = [gateway_status_reason_model]
        gateway_collection_gateways_item_model['patch_panel_completion_notice'] = 'patch panel configuration details'
        gateway_collection_gateways_item_model['port'] = gateway_port_reference_model
        gateway_collection_gateways_item_model['provider_api_managed'] = False
        gateway_collection_gateways_item_model['resource_group'] = resource_group_reference_model
        gateway_collection_gateways_item_model['speed_mbps'] = 1000
        gateway_collection_gateways_item_model['type'] = 'dedicated'
        gateway_collection_gateways_item_model['vlan'] = 10

        # Construct a json representation of a GatewayCollection model
        gateway_collection_model_json = {}
        gateway_collection_model_json['gateways'] = [gateway_collection_gateways_item_model]

        # Construct a model instance of GatewayCollection by calling from_dict on the json representation
        gateway_collection_model = GatewayCollection.from_dict(gateway_collection_model_json)
        assert gateway_collection_model != False

        # Construct a model instance of GatewayCollection by calling from_dict on the json representation
        gateway_collection_model_dict = GatewayCollection.from_dict(gateway_collection_model_json).__dict__
        gateway_collection_model2 = GatewayCollection(**gateway_collection_model_dict)

        # Verify the model instances are equivalent
        assert gateway_collection_model == gateway_collection_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_collection_model_json2 = gateway_collection_model.to_dict()
        assert gateway_collection_model_json2 == gateway_collection_model_json


class TestModel_GatewayMacsec:
    """
    Test Class for GatewayMacsec
    """

    def test_gateway_macsec_serialization(self):
        """
        Test serialization/deserialization for GatewayMacsec
        """

        # Construct dict forms of any model objects needed in order to build this model.

        sak_rekey_model = {}  # SakRekeyTimerMode
        sak_rekey_model['interval'] = 3600
        sak_rekey_model['mode'] = 'timer'

        gateway_macsec_status_reason_model = {}  # GatewayMacsecStatusReason
        gateway_macsec_status_reason_model['code'] = 'macsec_cak_failed'
        gateway_macsec_status_reason_model['message'] = 'The `authentication_key` failed configuration.'
        gateway_macsec_status_reason_model['more_info'] = 'https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK'

        # Construct a json representation of a GatewayMacsec model
        gateway_macsec_model_json = {}
        gateway_macsec_model_json['active'] = True
        gateway_macsec_model_json['cipher_suite'] = 'gcm_aes_xpn_256'
        gateway_macsec_model_json['confidentiality_offset'] = 0
        gateway_macsec_model_json['created_at'] = '2020-11-02T20:40:29.622000Z'
        gateway_macsec_model_json['key_server_priority'] = 255
        gateway_macsec_model_json['sak_rekey'] = sak_rekey_model
        gateway_macsec_model_json['security_policy'] = 'must_secure'
        gateway_macsec_model_json['status'] = 'secured'
        gateway_macsec_model_json['status_reasons'] = [gateway_macsec_status_reason_model]
        gateway_macsec_model_json['updated_at'] = '2020-11-02T20:40:29.622000Z'
        gateway_macsec_model_json['window_size'] = 512

        # Construct a model instance of GatewayMacsec by calling from_dict on the json representation
        gateway_macsec_model = GatewayMacsec.from_dict(gateway_macsec_model_json)
        assert gateway_macsec_model != False

        # Construct a model instance of GatewayMacsec by calling from_dict on the json representation
        gateway_macsec_model_dict = GatewayMacsec.from_dict(gateway_macsec_model_json).__dict__
        gateway_macsec_model2 = GatewayMacsec(**gateway_macsec_model_dict)

        # Verify the model instances are equivalent
        assert gateway_macsec_model == gateway_macsec_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_macsec_model_json2 = gateway_macsec_model.to_dict()
        assert gateway_macsec_model_json2 == gateway_macsec_model_json


class TestModel_GatewayMacsecCak:
    """
    Test Class for GatewayMacsecCak
    """

    def test_gateway_macsec_cak_serialization(self):
        """
        Test serialization/deserialization for GatewayMacsecCak
        """

        # Construct dict forms of any model objects needed in order to build this model.

        hpcs_key_reference_model = {}  # HpcsKeyReference
        hpcs_key_reference_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        gateway_macsec_cak_active_delta_model = {}  # GatewayMacsecCakActiveDelta
        gateway_macsec_cak_active_delta_model['key'] = hpcs_key_reference_model
        gateway_macsec_cak_active_delta_model['name'] = '1000'
        gateway_macsec_cak_active_delta_model['status'] = 'active'

        # Construct a json representation of a GatewayMacsecCak model
        gateway_macsec_cak_model_json = {}
        gateway_macsec_cak_model_json['active_delta'] = gateway_macsec_cak_active_delta_model
        gateway_macsec_cak_model_json['created_at'] = '2020-11-02T20:40:29.622000Z'
        gateway_macsec_cak_model_json['id'] = 'ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        gateway_macsec_cak_model_json['key'] = hpcs_key_reference_model
        gateway_macsec_cak_model_json['name'] = '1000'
        gateway_macsec_cak_model_json['session'] = 'primary'
        gateway_macsec_cak_model_json['status'] = 'active'
        gateway_macsec_cak_model_json['updated_at'] = '2020-11-02T20:40:29.622000Z'

        # Construct a model instance of GatewayMacsecCak by calling from_dict on the json representation
        gateway_macsec_cak_model = GatewayMacsecCak.from_dict(gateway_macsec_cak_model_json)
        assert gateway_macsec_cak_model != False

        # Construct a model instance of GatewayMacsecCak by calling from_dict on the json representation
        gateway_macsec_cak_model_dict = GatewayMacsecCak.from_dict(gateway_macsec_cak_model_json).__dict__
        gateway_macsec_cak_model2 = GatewayMacsecCak(**gateway_macsec_cak_model_dict)

        # Verify the model instances are equivalent
        assert gateway_macsec_cak_model == gateway_macsec_cak_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_macsec_cak_model_json2 = gateway_macsec_cak_model.to_dict()
        assert gateway_macsec_cak_model_json2 == gateway_macsec_cak_model_json


class TestModel_GatewayMacsecCakActiveDelta:
    """
    Test Class for GatewayMacsecCakActiveDelta
    """

    def test_gateway_macsec_cak_active_delta_serialization(self):
        """
        Test serialization/deserialization for GatewayMacsecCakActiveDelta
        """

        # Construct dict forms of any model objects needed in order to build this model.

        hpcs_key_reference_model = {}  # HpcsKeyReference
        hpcs_key_reference_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a json representation of a GatewayMacsecCakActiveDelta model
        gateway_macsec_cak_active_delta_model_json = {}
        gateway_macsec_cak_active_delta_model_json['key'] = hpcs_key_reference_model
        gateway_macsec_cak_active_delta_model_json['name'] = '1000'
        gateway_macsec_cak_active_delta_model_json['status'] = 'active'

        # Construct a model instance of GatewayMacsecCakActiveDelta by calling from_dict on the json representation
        gateway_macsec_cak_active_delta_model = GatewayMacsecCakActiveDelta.from_dict(gateway_macsec_cak_active_delta_model_json)
        assert gateway_macsec_cak_active_delta_model != False

        # Construct a model instance of GatewayMacsecCakActiveDelta by calling from_dict on the json representation
        gateway_macsec_cak_active_delta_model_dict = GatewayMacsecCakActiveDelta.from_dict(gateway_macsec_cak_active_delta_model_json).__dict__
        gateway_macsec_cak_active_delta_model2 = GatewayMacsecCakActiveDelta(**gateway_macsec_cak_active_delta_model_dict)

        # Verify the model instances are equivalent
        assert gateway_macsec_cak_active_delta_model == gateway_macsec_cak_active_delta_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_macsec_cak_active_delta_model_json2 = gateway_macsec_cak_active_delta_model.to_dict()
        assert gateway_macsec_cak_active_delta_model_json2 == gateway_macsec_cak_active_delta_model_json


class TestModel_GatewayMacsecCakCollection:
    """
    Test Class for GatewayMacsecCakCollection
    """

    def test_gateway_macsec_cak_collection_serialization(self):
        """
        Test serialization/deserialization for GatewayMacsecCakCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        hpcs_key_reference_model = {}  # HpcsKeyReference
        hpcs_key_reference_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        gateway_macsec_cak_active_delta_model = {}  # GatewayMacsecCakActiveDelta
        gateway_macsec_cak_active_delta_model['key'] = hpcs_key_reference_model
        gateway_macsec_cak_active_delta_model['name'] = '1000'
        gateway_macsec_cak_active_delta_model['status'] = 'active'

        gateway_macsec_cak_model = {}  # GatewayMacsecCak
        gateway_macsec_cak_model['active_delta'] = gateway_macsec_cak_active_delta_model
        gateway_macsec_cak_model['created_at'] = '2020-11-02T20:40:29.622000Z'
        gateway_macsec_cak_model['id'] = 'ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        gateway_macsec_cak_model['key'] = hpcs_key_reference_model
        gateway_macsec_cak_model['name'] = '1000'
        gateway_macsec_cak_model['session'] = 'primary'
        gateway_macsec_cak_model['status'] = 'active'
        gateway_macsec_cak_model['updated_at'] = '2020-11-02T20:40:29.622000Z'

        # Construct a json representation of a GatewayMacsecCakCollection model
        gateway_macsec_cak_collection_model_json = {}
        gateway_macsec_cak_collection_model_json['caks'] = [gateway_macsec_cak_model]

        # Construct a model instance of GatewayMacsecCakCollection by calling from_dict on the json representation
        gateway_macsec_cak_collection_model = GatewayMacsecCakCollection.from_dict(gateway_macsec_cak_collection_model_json)
        assert gateway_macsec_cak_collection_model != False

        # Construct a model instance of GatewayMacsecCakCollection by calling from_dict on the json representation
        gateway_macsec_cak_collection_model_dict = GatewayMacsecCakCollection.from_dict(gateway_macsec_cak_collection_model_json).__dict__
        gateway_macsec_cak_collection_model2 = GatewayMacsecCakCollection(**gateway_macsec_cak_collection_model_dict)

        # Verify the model instances are equivalent
        assert gateway_macsec_cak_collection_model == gateway_macsec_cak_collection_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_macsec_cak_collection_model_json2 = gateway_macsec_cak_collection_model.to_dict()
        assert gateway_macsec_cak_collection_model_json2 == gateway_macsec_cak_collection_model_json


class TestModel_GatewayMacsecCakPatch:
    """
    Test Class for GatewayMacsecCakPatch
    """

    def test_gateway_macsec_cak_patch_serialization(self):
        """
        Test serialization/deserialization for GatewayMacsecCakPatch
        """

        # Construct dict forms of any model objects needed in order to build this model.

        hpcs_key_identity_model = {}  # HpcsKeyIdentity
        hpcs_key_identity_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a json representation of a GatewayMacsecCakPatch model
        gateway_macsec_cak_patch_model_json = {}
        gateway_macsec_cak_patch_model_json['key'] = hpcs_key_identity_model
        gateway_macsec_cak_patch_model_json['name'] = '1000'

        # Construct a model instance of GatewayMacsecCakPatch by calling from_dict on the json representation
        gateway_macsec_cak_patch_model = GatewayMacsecCakPatch.from_dict(gateway_macsec_cak_patch_model_json)
        assert gateway_macsec_cak_patch_model != False

        # Construct a model instance of GatewayMacsecCakPatch by calling from_dict on the json representation
        gateway_macsec_cak_patch_model_dict = GatewayMacsecCakPatch.from_dict(gateway_macsec_cak_patch_model_json).__dict__
        gateway_macsec_cak_patch_model2 = GatewayMacsecCakPatch(**gateway_macsec_cak_patch_model_dict)

        # Verify the model instances are equivalent
        assert gateway_macsec_cak_patch_model == gateway_macsec_cak_patch_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_macsec_cak_patch_model_json2 = gateway_macsec_cak_patch_model.to_dict()
        assert gateway_macsec_cak_patch_model_json2 == gateway_macsec_cak_patch_model_json


class TestModel_GatewayMacsecCakPrototype:
    """
    Test Class for GatewayMacsecCakPrototype
    """

    def test_gateway_macsec_cak_prototype_serialization(self):
        """
        Test serialization/deserialization for GatewayMacsecCakPrototype
        """

        # Construct dict forms of any model objects needed in order to build this model.

        hpcs_key_identity_model = {}  # HpcsKeyIdentity
        hpcs_key_identity_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a json representation of a GatewayMacsecCakPrototype model
        gateway_macsec_cak_prototype_model_json = {}
        gateway_macsec_cak_prototype_model_json['key'] = hpcs_key_identity_model
        gateway_macsec_cak_prototype_model_json['name'] = '1000'
        gateway_macsec_cak_prototype_model_json['session'] = 'primary'

        # Construct a model instance of GatewayMacsecCakPrototype by calling from_dict on the json representation
        gateway_macsec_cak_prototype_model = GatewayMacsecCakPrototype.from_dict(gateway_macsec_cak_prototype_model_json)
        assert gateway_macsec_cak_prototype_model != False

        # Construct a model instance of GatewayMacsecCakPrototype by calling from_dict on the json representation
        gateway_macsec_cak_prototype_model_dict = GatewayMacsecCakPrototype.from_dict(gateway_macsec_cak_prototype_model_json).__dict__
        gateway_macsec_cak_prototype_model2 = GatewayMacsecCakPrototype(**gateway_macsec_cak_prototype_model_dict)

        # Verify the model instances are equivalent
        assert gateway_macsec_cak_prototype_model == gateway_macsec_cak_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_macsec_cak_prototype_model_json2 = gateway_macsec_cak_prototype_model.to_dict()
        assert gateway_macsec_cak_prototype_model_json2 == gateway_macsec_cak_prototype_model_json


class TestModel_GatewayMacsecPatch:
    """
    Test Class for GatewayMacsecPatch
    """

    def test_gateway_macsec_patch_serialization(self):
        """
        Test serialization/deserialization for GatewayMacsecPatch
        """

        # Construct dict forms of any model objects needed in order to build this model.

        sak_rekey_patch_model = {}  # SakRekeyPatchSakRekeyTimerModePatch
        sak_rekey_patch_model['interval'] = 3600
        sak_rekey_patch_model['mode'] = 'timer'

        # Construct a json representation of a GatewayMacsecPatch model
        gateway_macsec_patch_model_json = {}
        gateway_macsec_patch_model_json['active'] = True
        gateway_macsec_patch_model_json['sak_rekey'] = sak_rekey_patch_model
        gateway_macsec_patch_model_json['security_policy'] = 'must_secure'
        gateway_macsec_patch_model_json['window_size'] = 64

        # Construct a model instance of GatewayMacsecPatch by calling from_dict on the json representation
        gateway_macsec_patch_model = GatewayMacsecPatch.from_dict(gateway_macsec_patch_model_json)
        assert gateway_macsec_patch_model != False

        # Construct a model instance of GatewayMacsecPatch by calling from_dict on the json representation
        gateway_macsec_patch_model_dict = GatewayMacsecPatch.from_dict(gateway_macsec_patch_model_json).__dict__
        gateway_macsec_patch_model2 = GatewayMacsecPatch(**gateway_macsec_patch_model_dict)

        # Verify the model instances are equivalent
        assert gateway_macsec_patch_model == gateway_macsec_patch_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_macsec_patch_model_json2 = gateway_macsec_patch_model.to_dict()
        assert gateway_macsec_patch_model_json2 == gateway_macsec_patch_model_json


class TestModel_GatewayMacsecPrototype:
    """
    Test Class for GatewayMacsecPrototype
    """

    def test_gateway_macsec_prototype_serialization(self):
        """
        Test serialization/deserialization for GatewayMacsecPrototype
        """

        # Construct dict forms of any model objects needed in order to build this model.

        hpcs_key_identity_model = {}  # HpcsKeyIdentity
        hpcs_key_identity_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        gateway_macsec_cak_prototype_model = {}  # GatewayMacsecCakPrototype
        gateway_macsec_cak_prototype_model['key'] = hpcs_key_identity_model
        gateway_macsec_cak_prototype_model['name'] = '1000'
        gateway_macsec_cak_prototype_model['session'] = 'primary'

        sak_rekey_prototype_model = {}  # SakRekeyPrototypeSakRekeyTimerModePrototype
        sak_rekey_prototype_model['interval'] = 3600
        sak_rekey_prototype_model['mode'] = 'timer'

        # Construct a json representation of a GatewayMacsecPrototype model
        gateway_macsec_prototype_model_json = {}
        gateway_macsec_prototype_model_json['active'] = True
        gateway_macsec_prototype_model_json['caks'] = [gateway_macsec_cak_prototype_model]
        gateway_macsec_prototype_model_json['sak_rekey'] = sak_rekey_prototype_model
        gateway_macsec_prototype_model_json['security_policy'] = 'must_secure'
        gateway_macsec_prototype_model_json['window_size'] = 64

        # Construct a model instance of GatewayMacsecPrototype by calling from_dict on the json representation
        gateway_macsec_prototype_model = GatewayMacsecPrototype.from_dict(gateway_macsec_prototype_model_json)
        assert gateway_macsec_prototype_model != False

        # Construct a model instance of GatewayMacsecPrototype by calling from_dict on the json representation
        gateway_macsec_prototype_model_dict = GatewayMacsecPrototype.from_dict(gateway_macsec_prototype_model_json).__dict__
        gateway_macsec_prototype_model2 = GatewayMacsecPrototype(**gateway_macsec_prototype_model_dict)

        # Verify the model instances are equivalent
        assert gateway_macsec_prototype_model == gateway_macsec_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_macsec_prototype_model_json2 = gateway_macsec_prototype_model.to_dict()
        assert gateway_macsec_prototype_model_json2 == gateway_macsec_prototype_model_json


class TestModel_GatewayMacsecReference:
    """
    Test Class for GatewayMacsecReference
    """

    def test_gateway_macsec_reference_serialization(self):
        """
        Test serialization/deserialization for GatewayMacsecReference
        """

        # Construct dict forms of any model objects needed in order to build this model.

        gateway_macsec_status_reason_model = {}  # GatewayMacsecStatusReason
        gateway_macsec_status_reason_model['code'] = 'macsec_cak_failed'
        gateway_macsec_status_reason_model['message'] = 'The `authentication_key` failed configuration.'
        gateway_macsec_status_reason_model['more_info'] = 'https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK'

        # Construct a json representation of a GatewayMacsecReference model
        gateway_macsec_reference_model_json = {}
        gateway_macsec_reference_model_json['active'] = True
        gateway_macsec_reference_model_json['security_policy'] = 'must_secure'
        gateway_macsec_reference_model_json['status'] = 'secured'
        gateway_macsec_reference_model_json['status_reasons'] = [gateway_macsec_status_reason_model]

        # Construct a model instance of GatewayMacsecReference by calling from_dict on the json representation
        gateway_macsec_reference_model = GatewayMacsecReference.from_dict(gateway_macsec_reference_model_json)
        assert gateway_macsec_reference_model != False

        # Construct a model instance of GatewayMacsecReference by calling from_dict on the json representation
        gateway_macsec_reference_model_dict = GatewayMacsecReference.from_dict(gateway_macsec_reference_model_json).__dict__
        gateway_macsec_reference_model2 = GatewayMacsecReference(**gateway_macsec_reference_model_dict)

        # Verify the model instances are equivalent
        assert gateway_macsec_reference_model == gateway_macsec_reference_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_macsec_reference_model_json2 = gateway_macsec_reference_model.to_dict()
        assert gateway_macsec_reference_model_json2 == gateway_macsec_reference_model_json


class TestModel_GatewayMacsecStatusReason:
    """
    Test Class for GatewayMacsecStatusReason
    """

    def test_gateway_macsec_status_reason_serialization(self):
        """
        Test serialization/deserialization for GatewayMacsecStatusReason
        """

        # Construct a json representation of a GatewayMacsecStatusReason model
        gateway_macsec_status_reason_model_json = {}
        gateway_macsec_status_reason_model_json['code'] = 'macsec_cak_failed'
        gateway_macsec_status_reason_model_json['message'] = 'The `authentication_key` failed configuration.'
        gateway_macsec_status_reason_model_json['more_info'] = 'https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK'

        # Construct a model instance of GatewayMacsecStatusReason by calling from_dict on the json representation
        gateway_macsec_status_reason_model = GatewayMacsecStatusReason.from_dict(gateway_macsec_status_reason_model_json)
        assert gateway_macsec_status_reason_model != False

        # Construct a model instance of GatewayMacsecStatusReason by calling from_dict on the json representation
        gateway_macsec_status_reason_model_dict = GatewayMacsecStatusReason.from_dict(gateway_macsec_status_reason_model_json).__dict__
        gateway_macsec_status_reason_model2 = GatewayMacsecStatusReason(**gateway_macsec_status_reason_model_dict)

        # Verify the model instances are equivalent
        assert gateway_macsec_status_reason_model == gateway_macsec_status_reason_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_macsec_status_reason_model_json2 = gateway_macsec_status_reason_model.to_dict()
        assert gateway_macsec_status_reason_model_json2 == gateway_macsec_status_reason_model_json


class TestModel_GatewayPatchTemplate:
    """
    Test Class for GatewayPatchTemplate
    """

    def test_gateway_patch_template_serialization(self):
        """
        Test serialization/deserialization for GatewayPatchTemplate
        """

        # Construct dict forms of any model objects needed in order to build this model.

        authentication_key_identity_model = {}  # AuthenticationKeyIdentityKeyProtectAuthenticationKeyIdentity
        authentication_key_identity_model['crn'] = 'crn:v1:bluemix:public:kms:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        gateway_bfd_patch_template_model = {}  # GatewayBfdPatchTemplate
        gateway_bfd_patch_template_model['interval'] = 2000
        gateway_bfd_patch_template_model['multiplier'] = 10

        # Construct a json representation of a GatewayPatchTemplate model
        gateway_patch_template_model_json = {}
        gateway_patch_template_model_json['authentication_key'] = authentication_key_identity_model
        gateway_patch_template_model_json['bfd_config'] = gateway_bfd_patch_template_model
        gateway_patch_template_model_json['bgp_asn'] = 64999
        gateway_patch_template_model_json['bgp_cer_cidr'] = '169.254.0.10/30'
        gateway_patch_template_model_json['bgp_ibm_cidr'] = '169.254.0.9/30'
        gateway_patch_template_model_json['connection_mode'] = 'transit'
        gateway_patch_template_model_json['default_export_route_filter'] = 'permit'
        gateway_patch_template_model_json['default_import_route_filter'] = 'permit'
        gateway_patch_template_model_json['global'] = True
        gateway_patch_template_model_json['loa_reject_reason'] = 'The port mentioned was incorrect'
        gateway_patch_template_model_json['metered'] = False
        gateway_patch_template_model_json['name'] = 'testGateway'
        gateway_patch_template_model_json['operational_status'] = 'loa_accepted'
        gateway_patch_template_model_json['patch_panel_completion_notice'] = 'patch panel configuration details'
        gateway_patch_template_model_json['speed_mbps'] = 1000
        gateway_patch_template_model_json['vlan'] = 10

        # Construct a model instance of GatewayPatchTemplate by calling from_dict on the json representation
        gateway_patch_template_model = GatewayPatchTemplate.from_dict(gateway_patch_template_model_json)
        assert gateway_patch_template_model != False

        # Construct a model instance of GatewayPatchTemplate by calling from_dict on the json representation
        gateway_patch_template_model_dict = GatewayPatchTemplate.from_dict(gateway_patch_template_model_json).__dict__
        gateway_patch_template_model2 = GatewayPatchTemplate(**gateway_patch_template_model_dict)

        # Verify the model instances are equivalent
        assert gateway_patch_template_model == gateway_patch_template_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_patch_template_model_json2 = gateway_patch_template_model.to_dict()
        assert gateway_patch_template_model_json2 == gateway_patch_template_model_json


class TestModel_GatewayPortIdentity:
    """
    Test Class for GatewayPortIdentity
    """

    def test_gateway_port_identity_serialization(self):
        """
        Test serialization/deserialization for GatewayPortIdentity
        """

        # Construct a json representation of a GatewayPortIdentity model
        gateway_port_identity_model_json = {}
        gateway_port_identity_model_json['id'] = 'fffdcb1a-fee4-41c7-9e11-9cd99e65c777'

        # Construct a model instance of GatewayPortIdentity by calling from_dict on the json representation
        gateway_port_identity_model = GatewayPortIdentity.from_dict(gateway_port_identity_model_json)
        assert gateway_port_identity_model != False

        # Construct a model instance of GatewayPortIdentity by calling from_dict on the json representation
        gateway_port_identity_model_dict = GatewayPortIdentity.from_dict(gateway_port_identity_model_json).__dict__
        gateway_port_identity_model2 = GatewayPortIdentity(**gateway_port_identity_model_dict)

        # Verify the model instances are equivalent
        assert gateway_port_identity_model == gateway_port_identity_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_port_identity_model_json2 = gateway_port_identity_model.to_dict()
        assert gateway_port_identity_model_json2 == gateway_port_identity_model_json


class TestModel_GatewayPortReference:
    """
    Test Class for GatewayPortReference
    """

    def test_gateway_port_reference_serialization(self):
        """
        Test serialization/deserialization for GatewayPortReference
        """

        # Construct a json representation of a GatewayPortReference model
        gateway_port_reference_model_json = {}
        gateway_port_reference_model_json['id'] = '54321b1a-fee4-41c7-9e11-9cd99e000aaa'

        # Construct a model instance of GatewayPortReference by calling from_dict on the json representation
        gateway_port_reference_model = GatewayPortReference.from_dict(gateway_port_reference_model_json)
        assert gateway_port_reference_model != False

        # Construct a model instance of GatewayPortReference by calling from_dict on the json representation
        gateway_port_reference_model_dict = GatewayPortReference.from_dict(gateway_port_reference_model_json).__dict__
        gateway_port_reference_model2 = GatewayPortReference(**gateway_port_reference_model_dict)

        # Verify the model instances are equivalent
        assert gateway_port_reference_model == gateway_port_reference_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_port_reference_model_json2 = gateway_port_reference_model.to_dict()
        assert gateway_port_reference_model_json2 == gateway_port_reference_model_json


class TestModel_GatewayStatistic:
    """
    Test Class for GatewayStatistic
    """

    def test_gateway_statistic_serialization(self):
        """
        Test serialization/deserialization for GatewayStatistic
        """

        # Construct a json representation of a GatewayStatistic model
        gateway_statistic_model_json = {}
        gateway_statistic_model_json['created_at'] = '2020-08-20T06:58:41.909000Z'
        gateway_statistic_model_json['data'] = 'MKA statistics text...'
        gateway_statistic_model_json['type'] = 'macsec_policy'

        # Construct a model instance of GatewayStatistic by calling from_dict on the json representation
        gateway_statistic_model = GatewayStatistic.from_dict(gateway_statistic_model_json)
        assert gateway_statistic_model != False

        # Construct a model instance of GatewayStatistic by calling from_dict on the json representation
        gateway_statistic_model_dict = GatewayStatistic.from_dict(gateway_statistic_model_json).__dict__
        gateway_statistic_model2 = GatewayStatistic(**gateway_statistic_model_dict)

        # Verify the model instances are equivalent
        assert gateway_statistic_model == gateway_statistic_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_statistic_model_json2 = gateway_statistic_model.to_dict()
        assert gateway_statistic_model_json2 == gateway_statistic_model_json


class TestModel_GatewayStatisticCollection:
    """
    Test Class for GatewayStatisticCollection
    """

    def test_gateway_statistic_collection_serialization(self):
        """
        Test serialization/deserialization for GatewayStatisticCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        gateway_statistic_model = {}  # GatewayStatistic
        gateway_statistic_model['created_at'] = '2020-08-20T06:58:41.909000Z'
        gateway_statistic_model['data'] = 'MKA statistics text...'
        gateway_statistic_model['type'] = 'macsec_policy'

        # Construct a json representation of a GatewayStatisticCollection model
        gateway_statistic_collection_model_json = {}
        gateway_statistic_collection_model_json['statistics'] = [gateway_statistic_model]

        # Construct a model instance of GatewayStatisticCollection by calling from_dict on the json representation
        gateway_statistic_collection_model = GatewayStatisticCollection.from_dict(gateway_statistic_collection_model_json)
        assert gateway_statistic_collection_model != False

        # Construct a model instance of GatewayStatisticCollection by calling from_dict on the json representation
        gateway_statistic_collection_model_dict = GatewayStatisticCollection.from_dict(gateway_statistic_collection_model_json).__dict__
        gateway_statistic_collection_model2 = GatewayStatisticCollection(**gateway_statistic_collection_model_dict)

        # Verify the model instances are equivalent
        assert gateway_statistic_collection_model == gateway_statistic_collection_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_statistic_collection_model_json2 = gateway_statistic_collection_model.to_dict()
        assert gateway_statistic_collection_model_json2 == gateway_statistic_collection_model_json


class TestModel_GatewayStatusCollection:
    """
    Test Class for GatewayStatusCollection
    """

    def test_gateway_status_collection_serialization(self):
        """
        Test serialization/deserialization for GatewayStatusCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        gateway_status_model = {}  # GatewayStatusGatewayBGPStatus
        gateway_status_model['type'] = 'bgp'
        gateway_status_model['updated_at'] = '2020-08-20T06:58:41.909000Z'
        gateway_status_model['value'] = 'active'

        # Construct a json representation of a GatewayStatusCollection model
        gateway_status_collection_model_json = {}
        gateway_status_collection_model_json['status'] = [gateway_status_model]

        # Construct a model instance of GatewayStatusCollection by calling from_dict on the json representation
        gateway_status_collection_model = GatewayStatusCollection.from_dict(gateway_status_collection_model_json)
        assert gateway_status_collection_model != False

        # Construct a model instance of GatewayStatusCollection by calling from_dict on the json representation
        gateway_status_collection_model_dict = GatewayStatusCollection.from_dict(gateway_status_collection_model_json).__dict__
        gateway_status_collection_model2 = GatewayStatusCollection(**gateway_status_collection_model_dict)

        # Verify the model instances are equivalent
        assert gateway_status_collection_model == gateway_status_collection_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_status_collection_model_json2 = gateway_status_collection_model.to_dict()
        assert gateway_status_collection_model_json2 == gateway_status_collection_model_json


class TestModel_GatewayStatusReason:
    """
    Test Class for GatewayStatusReason
    """

    def test_gateway_status_reason_serialization(self):
        """
        Test serialization/deserialization for GatewayStatusReason
        """

        # Construct a json representation of a GatewayStatusReason model
        gateway_status_reason_model_json = {}
        gateway_status_reason_model_json['code'] = 'authentication_key_failed'
        gateway_status_reason_model_json['message'] = 'The `authentication_key` failed configuration.'
        gateway_status_reason_model_json['more_info'] = 'https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK'

        # Construct a model instance of GatewayStatusReason by calling from_dict on the json representation
        gateway_status_reason_model = GatewayStatusReason.from_dict(gateway_status_reason_model_json)
        assert gateway_status_reason_model != False

        # Construct a model instance of GatewayStatusReason by calling from_dict on the json representation
        gateway_status_reason_model_dict = GatewayStatusReason.from_dict(gateway_status_reason_model_json).__dict__
        gateway_status_reason_model2 = GatewayStatusReason(**gateway_status_reason_model_dict)

        # Verify the model instances are equivalent
        assert gateway_status_reason_model == gateway_status_reason_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_status_reason_model_json2 = gateway_status_reason_model.to_dict()
        assert gateway_status_reason_model_json2 == gateway_status_reason_model_json


class TestModel_GatewayTemplateRouteFilter:
    """
    Test Class for GatewayTemplateRouteFilter
    """

    def test_gateway_template_route_filter_serialization(self):
        """
        Test serialization/deserialization for GatewayTemplateRouteFilter
        """

        # Construct a json representation of a GatewayTemplateRouteFilter model
        gateway_template_route_filter_model_json = {}
        gateway_template_route_filter_model_json['action'] = 'permit'
        gateway_template_route_filter_model_json['ge'] = 25
        gateway_template_route_filter_model_json['le'] = 30
        gateway_template_route_filter_model_json['prefix'] = '192.168.100.0/24'

        # Construct a model instance of GatewayTemplateRouteFilter by calling from_dict on the json representation
        gateway_template_route_filter_model = GatewayTemplateRouteFilter.from_dict(gateway_template_route_filter_model_json)
        assert gateway_template_route_filter_model != False

        # Construct a model instance of GatewayTemplateRouteFilter by calling from_dict on the json representation
        gateway_template_route_filter_model_dict = GatewayTemplateRouteFilter.from_dict(gateway_template_route_filter_model_json).__dict__
        gateway_template_route_filter_model2 = GatewayTemplateRouteFilter(**gateway_template_route_filter_model_dict)

        # Verify the model instances are equivalent
        assert gateway_template_route_filter_model == gateway_template_route_filter_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_template_route_filter_model_json2 = gateway_template_route_filter_model.to_dict()
        assert gateway_template_route_filter_model_json2 == gateway_template_route_filter_model_json


class TestModel_GatewayVirtualConnection:
    """
    Test Class for GatewayVirtualConnection
    """

    def test_gateway_virtual_connection_serialization(self):
        """
        Test serialization/deserialization for GatewayVirtualConnection
        """

        # Construct a json representation of a GatewayVirtualConnection model
        gateway_virtual_connection_model_json = {}
        gateway_virtual_connection_model_json['created_at'] = '2019-01-01T12:00:00Z'
        gateway_virtual_connection_model_json['id'] = 'ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        gateway_virtual_connection_model_json['name'] = 'newVC'
        gateway_virtual_connection_model_json['network_account'] = '00aa14a2e0fb102c8995ebefff865555'
        gateway_virtual_connection_model_json['network_id'] = 'crn:v1:bluemix:public:is:us-east:a/28e4d90ac7504be69447111122223333::vpc:aaa81ac8-5e96-42a0-a4b7-6c2e2d1bbbbb'
        gateway_virtual_connection_model_json['status'] = 'attached'
        gateway_virtual_connection_model_json['type'] = 'vpc'

        # Construct a model instance of GatewayVirtualConnection by calling from_dict on the json representation
        gateway_virtual_connection_model = GatewayVirtualConnection.from_dict(gateway_virtual_connection_model_json)
        assert gateway_virtual_connection_model != False

        # Construct a model instance of GatewayVirtualConnection by calling from_dict on the json representation
        gateway_virtual_connection_model_dict = GatewayVirtualConnection.from_dict(gateway_virtual_connection_model_json).__dict__
        gateway_virtual_connection_model2 = GatewayVirtualConnection(**gateway_virtual_connection_model_dict)

        # Verify the model instances are equivalent
        assert gateway_virtual_connection_model == gateway_virtual_connection_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_virtual_connection_model_json2 = gateway_virtual_connection_model.to_dict()
        assert gateway_virtual_connection_model_json2 == gateway_virtual_connection_model_json


class TestModel_GatewayVirtualConnectionCollection:
    """
    Test Class for GatewayVirtualConnectionCollection
    """

    def test_gateway_virtual_connection_collection_serialization(self):
        """
        Test serialization/deserialization for GatewayVirtualConnectionCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        gateway_virtual_connection_model = {}  # GatewayVirtualConnection
        gateway_virtual_connection_model['created_at'] = '2019-01-01T12:00:00Z'
        gateway_virtual_connection_model['id'] = 'ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        gateway_virtual_connection_model['name'] = 'newVC'
        gateway_virtual_connection_model['network_account'] = '00aa14a2e0fb102c8995ebefff865555'
        gateway_virtual_connection_model['network_id'] = 'crn:v1:bluemix:public:is:us-east:a/28e4d90ac7504be69447111122223333::vpc:aaa81ac8-5e96-42a0-a4b7-6c2e2d1bbbbb'
        gateway_virtual_connection_model['status'] = 'attached'
        gateway_virtual_connection_model['type'] = 'vpc'

        # Construct a json representation of a GatewayVirtualConnectionCollection model
        gateway_virtual_connection_collection_model_json = {}
        gateway_virtual_connection_collection_model_json['virtual_connections'] = [gateway_virtual_connection_model]

        # Construct a model instance of GatewayVirtualConnectionCollection by calling from_dict on the json representation
        gateway_virtual_connection_collection_model = GatewayVirtualConnectionCollection.from_dict(gateway_virtual_connection_collection_model_json)
        assert gateway_virtual_connection_collection_model != False

        # Construct a model instance of GatewayVirtualConnectionCollection by calling from_dict on the json representation
        gateway_virtual_connection_collection_model_dict = GatewayVirtualConnectionCollection.from_dict(gateway_virtual_connection_collection_model_json).__dict__
        gateway_virtual_connection_collection_model2 = GatewayVirtualConnectionCollection(**gateway_virtual_connection_collection_model_dict)

        # Verify the model instances are equivalent
        assert gateway_virtual_connection_collection_model == gateway_virtual_connection_collection_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_virtual_connection_collection_model_json2 = gateway_virtual_connection_collection_model.to_dict()
        assert gateway_virtual_connection_collection_model_json2 == gateway_virtual_connection_collection_model_json


class TestModel_GatewayVirtualConnectionPatchTemplate:
    """
    Test Class for GatewayVirtualConnectionPatchTemplate
    """

    def test_gateway_virtual_connection_patch_template_serialization(self):
        """
        Test serialization/deserialization for GatewayVirtualConnectionPatchTemplate
        """

        # Construct a json representation of a GatewayVirtualConnectionPatchTemplate model
        gateway_virtual_connection_patch_template_model_json = {}
        gateway_virtual_connection_patch_template_model_json['name'] = 'newConnectionName'
        gateway_virtual_connection_patch_template_model_json['status'] = 'attached'

        # Construct a model instance of GatewayVirtualConnectionPatchTemplate by calling from_dict on the json representation
        gateway_virtual_connection_patch_template_model = GatewayVirtualConnectionPatchTemplate.from_dict(gateway_virtual_connection_patch_template_model_json)
        assert gateway_virtual_connection_patch_template_model != False

        # Construct a model instance of GatewayVirtualConnectionPatchTemplate by calling from_dict on the json representation
        gateway_virtual_connection_patch_template_model_dict = GatewayVirtualConnectionPatchTemplate.from_dict(gateway_virtual_connection_patch_template_model_json).__dict__
        gateway_virtual_connection_patch_template_model2 = GatewayVirtualConnectionPatchTemplate(**gateway_virtual_connection_patch_template_model_dict)

        # Verify the model instances are equivalent
        assert gateway_virtual_connection_patch_template_model == gateway_virtual_connection_patch_template_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_virtual_connection_patch_template_model_json2 = gateway_virtual_connection_patch_template_model.to_dict()
        assert gateway_virtual_connection_patch_template_model_json2 == gateway_virtual_connection_patch_template_model_json


class TestModel_HpcsKeyIdentity:
    """
    Test Class for HpcsKeyIdentity
    """

    def test_hpcs_key_identity_serialization(self):
        """
        Test serialization/deserialization for HpcsKeyIdentity
        """

        # Construct a json representation of a HpcsKeyIdentity model
        hpcs_key_identity_model_json = {}
        hpcs_key_identity_model_json['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a model instance of HpcsKeyIdentity by calling from_dict on the json representation
        hpcs_key_identity_model = HpcsKeyIdentity.from_dict(hpcs_key_identity_model_json)
        assert hpcs_key_identity_model != False

        # Construct a model instance of HpcsKeyIdentity by calling from_dict on the json representation
        hpcs_key_identity_model_dict = HpcsKeyIdentity.from_dict(hpcs_key_identity_model_json).__dict__
        hpcs_key_identity_model2 = HpcsKeyIdentity(**hpcs_key_identity_model_dict)

        # Verify the model instances are equivalent
        assert hpcs_key_identity_model == hpcs_key_identity_model2

        # Convert model instance back to dict and verify no loss of data
        hpcs_key_identity_model_json2 = hpcs_key_identity_model.to_dict()
        assert hpcs_key_identity_model_json2 == hpcs_key_identity_model_json


class TestModel_HpcsKeyReference:
    """
    Test Class for HpcsKeyReference
    """

    def test_hpcs_key_reference_serialization(self):
        """
        Test serialization/deserialization for HpcsKeyReference
        """

        # Construct a json representation of a HpcsKeyReference model
        hpcs_key_reference_model_json = {}
        hpcs_key_reference_model_json['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a model instance of HpcsKeyReference by calling from_dict on the json representation
        hpcs_key_reference_model = HpcsKeyReference.from_dict(hpcs_key_reference_model_json)
        assert hpcs_key_reference_model != False

        # Construct a model instance of HpcsKeyReference by calling from_dict on the json representation
        hpcs_key_reference_model_dict = HpcsKeyReference.from_dict(hpcs_key_reference_model_json).__dict__
        hpcs_key_reference_model2 = HpcsKeyReference(**hpcs_key_reference_model_dict)

        # Verify the model instances are equivalent
        assert hpcs_key_reference_model == hpcs_key_reference_model2

        # Convert model instance back to dict and verify no loss of data
        hpcs_key_reference_model_json2 = hpcs_key_reference_model.to_dict()
        assert hpcs_key_reference_model_json2 == hpcs_key_reference_model_json


class TestModel_ImportRouteFilterCollection:
    """
    Test Class for ImportRouteFilterCollection
    """

    def test_import_route_filter_collection_serialization(self):
        """
        Test serialization/deserialization for ImportRouteFilterCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        route_filter_model = {}  # RouteFilter
        route_filter_model['action'] = 'permit'
        route_filter_model['before'] = '1a15dcab-7e40-45e1-b7c5-bc690eaa9782'
        route_filter_model['created_at'] = '2020-11-02T20:40:29.622000Z'
        route_filter_model['ge'] = 25
        route_filter_model['id'] = '1a15dcab-7e40-45e1-b7c5-bc690eaa9782'
        route_filter_model['le'] = 30
        route_filter_model['prefix'] = '192.168.100.0/24'
        route_filter_model['updated_at'] = '2020-11-02T20:40:29.622000Z'

        # Construct a json representation of a ImportRouteFilterCollection model
        import_route_filter_collection_model_json = {}
        import_route_filter_collection_model_json['import_route_filters'] = [route_filter_model]

        # Construct a model instance of ImportRouteFilterCollection by calling from_dict on the json representation
        import_route_filter_collection_model = ImportRouteFilterCollection.from_dict(import_route_filter_collection_model_json)
        assert import_route_filter_collection_model != False

        # Construct a model instance of ImportRouteFilterCollection by calling from_dict on the json representation
        import_route_filter_collection_model_dict = ImportRouteFilterCollection.from_dict(import_route_filter_collection_model_json).__dict__
        import_route_filter_collection_model2 = ImportRouteFilterCollection(**import_route_filter_collection_model_dict)

        # Verify the model instances are equivalent
        assert import_route_filter_collection_model == import_route_filter_collection_model2

        # Convert model instance back to dict and verify no loss of data
        import_route_filter_collection_model_json2 = import_route_filter_collection_model.to_dict()
        assert import_route_filter_collection_model_json2 == import_route_filter_collection_model_json


class TestModel_LocationCollection:
    """
    Test Class for LocationCollection
    """

    def test_location_collection_serialization(self):
        """
        Test serialization/deserialization for LocationCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        location_output_model = {}  # LocationOutput
        location_output_model['billing_location'] = 'us'
        location_output_model['building_colocation_owner'] = 'MyProvider'
        location_output_model['display_name'] = 'Dallas 9'
        location_output_model['location_type'] = 'PoP'
        location_output_model['macsec_enabled'] = False
        location_output_model['market'] = 'Dallas'
        location_output_model['market_geography'] = 'N/S America'
        location_output_model['mzr'] = True
        location_output_model['name'] = 'dal03'
        location_output_model['offering_type'] = 'dedicated'
        location_output_model['provision_enabled'] = True
        location_output_model['vpc_region'] = 'us-south'

        # Construct a json representation of a LocationCollection model
        location_collection_model_json = {}
        location_collection_model_json['locations'] = [location_output_model]

        # Construct a model instance of LocationCollection by calling from_dict on the json representation
        location_collection_model = LocationCollection.from_dict(location_collection_model_json)
        assert location_collection_model != False

        # Construct a model instance of LocationCollection by calling from_dict on the json representation
        location_collection_model_dict = LocationCollection.from_dict(location_collection_model_json).__dict__
        location_collection_model2 = LocationCollection(**location_collection_model_dict)

        # Verify the model instances are equivalent
        assert location_collection_model == location_collection_model2

        # Convert model instance back to dict and verify no loss of data
        location_collection_model_json2 = location_collection_model.to_dict()
        assert location_collection_model_json2 == location_collection_model_json


class TestModel_LocationCrossConnectRouterCollection:
    """
    Test Class for LocationCrossConnectRouterCollection
    """

    def test_location_cross_connect_router_collection_serialization(self):
        """
        Test serialization/deserialization for LocationCrossConnectRouterCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        cross_connect_router_model = {}  # CrossConnectRouter
        cross_connect_router_model['capabilities'] = ['testString']
        cross_connect_router_model['router_name'] = 'xcr01.dal03'
        cross_connect_router_model['total_connections'] = 1

        # Construct a json representation of a LocationCrossConnectRouterCollection model
        location_cross_connect_router_collection_model_json = {}
        location_cross_connect_router_collection_model_json['cross_connect_routers'] = [cross_connect_router_model]

        # Construct a model instance of LocationCrossConnectRouterCollection by calling from_dict on the json representation
        location_cross_connect_router_collection_model = LocationCrossConnectRouterCollection.from_dict(location_cross_connect_router_collection_model_json)
        assert location_cross_connect_router_collection_model != False

        # Construct a model instance of LocationCrossConnectRouterCollection by calling from_dict on the json representation
        location_cross_connect_router_collection_model_dict = LocationCrossConnectRouterCollection.from_dict(location_cross_connect_router_collection_model_json).__dict__
        location_cross_connect_router_collection_model2 = LocationCrossConnectRouterCollection(**location_cross_connect_router_collection_model_dict)

        # Verify the model instances are equivalent
        assert location_cross_connect_router_collection_model == location_cross_connect_router_collection_model2

        # Convert model instance back to dict and verify no loss of data
        location_cross_connect_router_collection_model_json2 = location_cross_connect_router_collection_model.to_dict()
        assert location_cross_connect_router_collection_model_json2 == location_cross_connect_router_collection_model_json


class TestModel_LocationOutput:
    """
    Test Class for LocationOutput
    """

    def test_location_output_serialization(self):
        """
        Test serialization/deserialization for LocationOutput
        """

        # Construct a json representation of a LocationOutput model
        location_output_model_json = {}
        location_output_model_json['billing_location'] = 'us'
        location_output_model_json['building_colocation_owner'] = 'MyProvider'
        location_output_model_json['display_name'] = 'Dallas 9'
        location_output_model_json['location_type'] = 'PoP'
        location_output_model_json['macsec_enabled'] = False
        location_output_model_json['market'] = 'Dallas'
        location_output_model_json['market_geography'] = 'N/S America'
        location_output_model_json['mzr'] = True
        location_output_model_json['name'] = 'dal03'
        location_output_model_json['offering_type'] = 'dedicated'
        location_output_model_json['provision_enabled'] = True
        location_output_model_json['vpc_region'] = 'us-south'

        # Construct a model instance of LocationOutput by calling from_dict on the json representation
        location_output_model = LocationOutput.from_dict(location_output_model_json)
        assert location_output_model != False

        # Construct a model instance of LocationOutput by calling from_dict on the json representation
        location_output_model_dict = LocationOutput.from_dict(location_output_model_json).__dict__
        location_output_model2 = LocationOutput(**location_output_model_dict)

        # Verify the model instances are equivalent
        assert location_output_model == location_output_model2

        # Convert model instance back to dict and verify no loss of data
        location_output_model_json2 = location_output_model.to_dict()
        assert location_output_model_json2 == location_output_model_json


class TestModel_OfferingSpeed:
    """
    Test Class for OfferingSpeed
    """

    def test_offering_speed_serialization(self):
        """
        Test serialization/deserialization for OfferingSpeed
        """

        # Construct a json representation of a OfferingSpeed model
        offering_speed_model_json = {}
        offering_speed_model_json['capabilities'] = ['metered', 'unmetered']
        offering_speed_model_json['link_speed'] = 2000
        offering_speed_model_json['macsec_enabled'] = False

        # Construct a model instance of OfferingSpeed by calling from_dict on the json representation
        offering_speed_model = OfferingSpeed.from_dict(offering_speed_model_json)
        assert offering_speed_model != False

        # Construct a model instance of OfferingSpeed by calling from_dict on the json representation
        offering_speed_model_dict = OfferingSpeed.from_dict(offering_speed_model_json).__dict__
        offering_speed_model2 = OfferingSpeed(**offering_speed_model_dict)

        # Verify the model instances are equivalent
        assert offering_speed_model == offering_speed_model2

        # Convert model instance back to dict and verify no loss of data
        offering_speed_model_json2 = offering_speed_model.to_dict()
        assert offering_speed_model_json2 == offering_speed_model_json


class TestModel_OfferingSpeedCollection:
    """
    Test Class for OfferingSpeedCollection
    """

    def test_offering_speed_collection_serialization(self):
        """
        Test serialization/deserialization for OfferingSpeedCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        offering_speed_model = {}  # OfferingSpeed
        offering_speed_model['capabilities'] = ['metered', 'unmetered']
        offering_speed_model['link_speed'] = 2000
        offering_speed_model['macsec_enabled'] = False

        # Construct a json representation of a OfferingSpeedCollection model
        offering_speed_collection_model_json = {}
        offering_speed_collection_model_json['speeds'] = [offering_speed_model]

        # Construct a model instance of OfferingSpeedCollection by calling from_dict on the json representation
        offering_speed_collection_model = OfferingSpeedCollection.from_dict(offering_speed_collection_model_json)
        assert offering_speed_collection_model != False

        # Construct a model instance of OfferingSpeedCollection by calling from_dict on the json representation
        offering_speed_collection_model_dict = OfferingSpeedCollection.from_dict(offering_speed_collection_model_json).__dict__
        offering_speed_collection_model2 = OfferingSpeedCollection(**offering_speed_collection_model_dict)

        # Verify the model instances are equivalent
        assert offering_speed_collection_model == offering_speed_collection_model2

        # Convert model instance back to dict and verify no loss of data
        offering_speed_collection_model_json2 = offering_speed_collection_model.to_dict()
        assert offering_speed_collection_model_json2 == offering_speed_collection_model_json


class TestModel_Port:
    """
    Test Class for Port
    """

    def test_port_serialization(self):
        """
        Test serialization/deserialization for Port
        """

        # Construct a json representation of a Port model
        port_model_json = {}
        port_model_json['direct_link_count'] = 1
        port_model_json['id'] = '01122b9b-820f-4c44-8a31-77f1f0806765'
        port_model_json['label'] = 'XCR-FRK-CS-SEC-01'
        port_model_json['location_display_name'] = 'Dallas 03'
        port_model_json['location_name'] = 'dal03'
        port_model_json['provider_name'] = 'provider_1'
        port_model_json['supported_link_speeds'] = [1000, 2000, 5000, 10000]

        # Construct a model instance of Port by calling from_dict on the json representation
        port_model = Port.from_dict(port_model_json)
        assert port_model != False

        # Construct a model instance of Port by calling from_dict on the json representation
        port_model_dict = Port.from_dict(port_model_json).__dict__
        port_model2 = Port(**port_model_dict)

        # Verify the model instances are equivalent
        assert port_model == port_model2

        # Convert model instance back to dict and verify no loss of data
        port_model_json2 = port_model.to_dict()
        assert port_model_json2 == port_model_json


class TestModel_PortCollection:
    """
    Test Class for PortCollection
    """

    def test_port_collection_serialization(self):
        """
        Test serialization/deserialization for PortCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        ports_paginated_collection_first_model = {}  # PortsPaginatedCollectionFirst
        ports_paginated_collection_first_model['href'] = 'https://directlink.cloud.ibm.com/v1/ports?limit=100'

        ports_paginated_collection_next_model = {}  # PortsPaginatedCollectionNext
        ports_paginated_collection_next_model['href'] = 'https://directlink.cloud.ibm.com/v1/ports?start=9d5a91a3e2cbd233b5a5b33436855ed1&limit=100'
        ports_paginated_collection_next_model['start'] = '9d5a91a3e2cbd233b5a5b33436855ed1'

        port_model = {}  # Port
        port_model['direct_link_count'] = 1
        port_model['id'] = '01122b9b-820f-4c44-8a31-77f1f0806765'
        port_model['label'] = 'XCR-FRK-CS-SEC-01'
        port_model['location_display_name'] = 'Dallas 03'
        port_model['location_name'] = 'dal03'
        port_model['provider_name'] = 'provider_1'
        port_model['supported_link_speeds'] = [1000, 2000, 5000, 10000]

        # Construct a json representation of a PortCollection model
        port_collection_model_json = {}
        port_collection_model_json['first'] = ports_paginated_collection_first_model
        port_collection_model_json['limit'] = 100
        port_collection_model_json['next'] = ports_paginated_collection_next_model
        port_collection_model_json['total_count'] = 132
        port_collection_model_json['ports'] = [port_model]

        # Construct a model instance of PortCollection by calling from_dict on the json representation
        port_collection_model = PortCollection.from_dict(port_collection_model_json)
        assert port_collection_model != False

        # Construct a model instance of PortCollection by calling from_dict on the json representation
        port_collection_model_dict = PortCollection.from_dict(port_collection_model_json).__dict__
        port_collection_model2 = PortCollection(**port_collection_model_dict)

        # Verify the model instances are equivalent
        assert port_collection_model == port_collection_model2

        # Convert model instance back to dict and verify no loss of data
        port_collection_model_json2 = port_collection_model.to_dict()
        assert port_collection_model_json2 == port_collection_model_json


class TestModel_PortsPaginatedCollectionFirst:
    """
    Test Class for PortsPaginatedCollectionFirst
    """

    def test_ports_paginated_collection_first_serialization(self):
        """
        Test serialization/deserialization for PortsPaginatedCollectionFirst
        """

        # Construct a json representation of a PortsPaginatedCollectionFirst model
        ports_paginated_collection_first_model_json = {}
        ports_paginated_collection_first_model_json['href'] = 'https://directlink.cloud.ibm.com/v1/ports?limit=100'

        # Construct a model instance of PortsPaginatedCollectionFirst by calling from_dict on the json representation
        ports_paginated_collection_first_model = PortsPaginatedCollectionFirst.from_dict(ports_paginated_collection_first_model_json)
        assert ports_paginated_collection_first_model != False

        # Construct a model instance of PortsPaginatedCollectionFirst by calling from_dict on the json representation
        ports_paginated_collection_first_model_dict = PortsPaginatedCollectionFirst.from_dict(ports_paginated_collection_first_model_json).__dict__
        ports_paginated_collection_first_model2 = PortsPaginatedCollectionFirst(**ports_paginated_collection_first_model_dict)

        # Verify the model instances are equivalent
        assert ports_paginated_collection_first_model == ports_paginated_collection_first_model2

        # Convert model instance back to dict and verify no loss of data
        ports_paginated_collection_first_model_json2 = ports_paginated_collection_first_model.to_dict()
        assert ports_paginated_collection_first_model_json2 == ports_paginated_collection_first_model_json


class TestModel_PortsPaginatedCollectionNext:
    """
    Test Class for PortsPaginatedCollectionNext
    """

    def test_ports_paginated_collection_next_serialization(self):
        """
        Test serialization/deserialization for PortsPaginatedCollectionNext
        """

        # Construct a json representation of a PortsPaginatedCollectionNext model
        ports_paginated_collection_next_model_json = {}
        ports_paginated_collection_next_model_json['href'] = 'https://directlink.cloud.ibm.com/v1/ports?start=9d5a91a3e2cbd233b5a5b33436855ed1&limit=100'
        ports_paginated_collection_next_model_json['start'] = '9d5a91a3e2cbd233b5a5b33436855ed1'

        # Construct a model instance of PortsPaginatedCollectionNext by calling from_dict on the json representation
        ports_paginated_collection_next_model = PortsPaginatedCollectionNext.from_dict(ports_paginated_collection_next_model_json)
        assert ports_paginated_collection_next_model != False

        # Construct a model instance of PortsPaginatedCollectionNext by calling from_dict on the json representation
        ports_paginated_collection_next_model_dict = PortsPaginatedCollectionNext.from_dict(ports_paginated_collection_next_model_json).__dict__
        ports_paginated_collection_next_model2 = PortsPaginatedCollectionNext(**ports_paginated_collection_next_model_dict)

        # Verify the model instances are equivalent
        assert ports_paginated_collection_next_model == ports_paginated_collection_next_model2

        # Convert model instance back to dict and verify no loss of data
        ports_paginated_collection_next_model_json2 = ports_paginated_collection_next_model.to_dict()
        assert ports_paginated_collection_next_model_json2 == ports_paginated_collection_next_model_json


class TestModel_ResourceGroupIdentity:
    """
    Test Class for ResourceGroupIdentity
    """

    def test_resource_group_identity_serialization(self):
        """
        Test serialization/deserialization for ResourceGroupIdentity
        """

        # Construct a json representation of a ResourceGroupIdentity model
        resource_group_identity_model_json = {}
        resource_group_identity_model_json['id'] = '56969d6043e9465c883cb9f7363e78e8'

        # Construct a model instance of ResourceGroupIdentity by calling from_dict on the json representation
        resource_group_identity_model = ResourceGroupIdentity.from_dict(resource_group_identity_model_json)
        assert resource_group_identity_model != False

        # Construct a model instance of ResourceGroupIdentity by calling from_dict on the json representation
        resource_group_identity_model_dict = ResourceGroupIdentity.from_dict(resource_group_identity_model_json).__dict__
        resource_group_identity_model2 = ResourceGroupIdentity(**resource_group_identity_model_dict)

        # Verify the model instances are equivalent
        assert resource_group_identity_model == resource_group_identity_model2

        # Convert model instance back to dict and verify no loss of data
        resource_group_identity_model_json2 = resource_group_identity_model.to_dict()
        assert resource_group_identity_model_json2 == resource_group_identity_model_json


class TestModel_ResourceGroupReference:
    """
    Test Class for ResourceGroupReference
    """

    def test_resource_group_reference_serialization(self):
        """
        Test serialization/deserialization for ResourceGroupReference
        """

        # Construct a json representation of a ResourceGroupReference model
        resource_group_reference_model_json = {}
        resource_group_reference_model_json['id'] = '56969d6043e9465c883cb9f7363e78e8'

        # Construct a model instance of ResourceGroupReference by calling from_dict on the json representation
        resource_group_reference_model = ResourceGroupReference.from_dict(resource_group_reference_model_json)
        assert resource_group_reference_model != False

        # Construct a model instance of ResourceGroupReference by calling from_dict on the json representation
        resource_group_reference_model_dict = ResourceGroupReference.from_dict(resource_group_reference_model_json).__dict__
        resource_group_reference_model2 = ResourceGroupReference(**resource_group_reference_model_dict)

        # Verify the model instances are equivalent
        assert resource_group_reference_model == resource_group_reference_model2

        # Convert model instance back to dict and verify no loss of data
        resource_group_reference_model_json2 = resource_group_reference_model.to_dict()
        assert resource_group_reference_model_json2 == resource_group_reference_model_json


class TestModel_RouteFilter:
    """
    Test Class for RouteFilter
    """

    def test_route_filter_serialization(self):
        """
        Test serialization/deserialization for RouteFilter
        """

        # Construct a json representation of a RouteFilter model
        route_filter_model_json = {}
        route_filter_model_json['action'] = 'permit'
        route_filter_model_json['before'] = '1a15dcab-7e40-45e1-b7c5-bc690eaa9782'
        route_filter_model_json['created_at'] = '2020-11-02T20:40:29.622000Z'
        route_filter_model_json['ge'] = 25
        route_filter_model_json['id'] = '1a15dcab-7e40-45e1-b7c5-bc690eaa9782'
        route_filter_model_json['le'] = 30
        route_filter_model_json['prefix'] = '192.168.100.0/24'
        route_filter_model_json['updated_at'] = '2020-11-02T20:40:29.622000Z'

        # Construct a model instance of RouteFilter by calling from_dict on the json representation
        route_filter_model = RouteFilter.from_dict(route_filter_model_json)
        assert route_filter_model != False

        # Construct a model instance of RouteFilter by calling from_dict on the json representation
        route_filter_model_dict = RouteFilter.from_dict(route_filter_model_json).__dict__
        route_filter_model2 = RouteFilter(**route_filter_model_dict)

        # Verify the model instances are equivalent
        assert route_filter_model == route_filter_model2

        # Convert model instance back to dict and verify no loss of data
        route_filter_model_json2 = route_filter_model.to_dict()
        assert route_filter_model_json2 == route_filter_model_json


class TestModel_RouteReport:
    """
    Test Class for RouteReport
    """

    def test_route_report_serialization(self):
        """
        Test serialization/deserialization for RouteReport
        """

        # Construct dict forms of any model objects needed in order to build this model.

        route_report_advertised_route_model = {}  # RouteReportAdvertisedRoute
        route_report_advertised_route_model['as_path'] = '64999 64999 64998 I'
        route_report_advertised_route_model['prefix'] = '172.17.0.0/16'

        route_report_route_model = {}  # RouteReportRoute
        route_report_route_model['prefix'] = '172.17.0.0/16'

        route_report_on_prem_route_model = {}  # RouteReportOnPremRoute
        route_report_on_prem_route_model['as_path'] = '64999 64999 64998 I'
        route_report_on_prem_route_model['next_hop'] = '172.17.0.0'
        route_report_on_prem_route_model['prefix'] = '172.17.0.0/16'

        route_report_overlapping_route_model = {}  # RouteReportOverlappingRouteForConnection
        route_report_overlapping_route_model['prefix'] = '172.17.0.0/16'
        route_report_overlapping_route_model['type'] = 'virtual_connection'
        route_report_overlapping_route_model['virtual_connection_id'] = 'd2d985d8-1d8e-4e8b-96cd-cee2290ecaff'

        route_report_overlapping_route_group_model = {}  # RouteReportOverlappingRouteGroup
        route_report_overlapping_route_group_model['routes'] = [route_report_overlapping_route_model]

        route_report_virtual_connection_route_model = {}  # RouteReportVirtualConnectionRoute
        route_report_virtual_connection_route_model['active'] = True
        route_report_virtual_connection_route_model['local_preference'] = '200'
        route_report_virtual_connection_route_model['prefix'] = '172.17.0.0/16'

        route_report_connection_model = {}  # RouteReportConnection
        route_report_connection_model['routes'] = [route_report_virtual_connection_route_model]
        route_report_connection_model['virtual_connection_id'] = '3c265a62-91da-4261-a950-950b6af0eb58'
        route_report_connection_model['virtual_connection_name'] = 'vpc1'
        route_report_connection_model['virtual_connection_type'] = 'vpc'

        # Construct a json representation of a RouteReport model
        route_report_model_json = {}
        route_report_model_json['advertised_routes'] = [route_report_advertised_route_model]
        route_report_model_json['created_at'] = '2019-01-01T12:00:00Z'
        route_report_model_json['gateway_routes'] = [route_report_route_model]
        route_report_model_json['id'] = '1a15dcab-7e26-45e1-b7c5-bc690eaa9724'
        route_report_model_json['on_prem_routes'] = [route_report_on_prem_route_model]
        route_report_model_json['overlapping_routes'] = [route_report_overlapping_route_group_model]
        route_report_model_json['status'] = 'complete'
        route_report_model_json['updated_at'] = '2019-01-01T12:00:00Z'
        route_report_model_json['virtual_connection_routes'] = [route_report_connection_model]

        # Construct a model instance of RouteReport by calling from_dict on the json representation
        route_report_model = RouteReport.from_dict(route_report_model_json)
        assert route_report_model != False

        # Construct a model instance of RouteReport by calling from_dict on the json representation
        route_report_model_dict = RouteReport.from_dict(route_report_model_json).__dict__
        route_report_model2 = RouteReport(**route_report_model_dict)

        # Verify the model instances are equivalent
        assert route_report_model == route_report_model2

        # Convert model instance back to dict and verify no loss of data
        route_report_model_json2 = route_report_model.to_dict()
        assert route_report_model_json2 == route_report_model_json


class TestModel_RouteReportAdvertisedRoute:
    """
    Test Class for RouteReportAdvertisedRoute
    """

    def test_route_report_advertised_route_serialization(self):
        """
        Test serialization/deserialization for RouteReportAdvertisedRoute
        """

        # Construct a json representation of a RouteReportAdvertisedRoute model
        route_report_advertised_route_model_json = {}
        route_report_advertised_route_model_json['as_path'] = '64999 64999 64998 I'
        route_report_advertised_route_model_json['prefix'] = '172.17.0.0/16'

        # Construct a model instance of RouteReportAdvertisedRoute by calling from_dict on the json representation
        route_report_advertised_route_model = RouteReportAdvertisedRoute.from_dict(route_report_advertised_route_model_json)
        assert route_report_advertised_route_model != False

        # Construct a model instance of RouteReportAdvertisedRoute by calling from_dict on the json representation
        route_report_advertised_route_model_dict = RouteReportAdvertisedRoute.from_dict(route_report_advertised_route_model_json).__dict__
        route_report_advertised_route_model2 = RouteReportAdvertisedRoute(**route_report_advertised_route_model_dict)

        # Verify the model instances are equivalent
        assert route_report_advertised_route_model == route_report_advertised_route_model2

        # Convert model instance back to dict and verify no loss of data
        route_report_advertised_route_model_json2 = route_report_advertised_route_model.to_dict()
        assert route_report_advertised_route_model_json2 == route_report_advertised_route_model_json


class TestModel_RouteReportCollection:
    """
    Test Class for RouteReportCollection
    """

    def test_route_report_collection_serialization(self):
        """
        Test serialization/deserialization for RouteReportCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        route_report_advertised_route_model = {}  # RouteReportAdvertisedRoute
        route_report_advertised_route_model['as_path'] = '64999 64999 64998 I'
        route_report_advertised_route_model['prefix'] = '172.17.0.0/16'

        route_report_route_model = {}  # RouteReportRoute
        route_report_route_model['prefix'] = '172.17.0.0/16'

        route_report_on_prem_route_model = {}  # RouteReportOnPremRoute
        route_report_on_prem_route_model['as_path'] = '64999 64999 64998 I'
        route_report_on_prem_route_model['next_hop'] = '172.17.0.0'
        route_report_on_prem_route_model['prefix'] = '172.17.0.0/16'

        route_report_overlapping_route_model = {}  # RouteReportOverlappingRouteForConnection
        route_report_overlapping_route_model['prefix'] = '172.17.0.0/16'
        route_report_overlapping_route_model['type'] = 'virtual_connection'
        route_report_overlapping_route_model['virtual_connection_id'] = 'd2d985d8-1d8e-4e8b-96cd-cee2290ecaff'

        route_report_overlapping_route_group_model = {}  # RouteReportOverlappingRouteGroup
        route_report_overlapping_route_group_model['routes'] = [route_report_overlapping_route_model]

        route_report_virtual_connection_route_model = {}  # RouteReportVirtualConnectionRoute
        route_report_virtual_connection_route_model['active'] = True
        route_report_virtual_connection_route_model['local_preference'] = '200'
        route_report_virtual_connection_route_model['prefix'] = '172.17.0.0/16'

        route_report_connection_model = {}  # RouteReportConnection
        route_report_connection_model['routes'] = [route_report_virtual_connection_route_model]
        route_report_connection_model['virtual_connection_id'] = '3c265a62-91da-4261-a950-950b6af0eb58'
        route_report_connection_model['virtual_connection_name'] = 'vpc1'
        route_report_connection_model['virtual_connection_type'] = 'vpc'

        route_report_model = {}  # RouteReport
        route_report_model['advertised_routes'] = [route_report_advertised_route_model]
        route_report_model['created_at'] = '2019-01-01T12:00:00Z'
        route_report_model['gateway_routes'] = [route_report_route_model]
        route_report_model['id'] = '1a15dcab-7e26-45e1-b7c5-bc690eaa9724'
        route_report_model['on_prem_routes'] = [route_report_on_prem_route_model]
        route_report_model['overlapping_routes'] = [route_report_overlapping_route_group_model]
        route_report_model['status'] = 'complete'
        route_report_model['updated_at'] = '2019-01-01T12:00:00Z'
        route_report_model['virtual_connection_routes'] = [route_report_connection_model]

        # Construct a json representation of a RouteReportCollection model
        route_report_collection_model_json = {}
        route_report_collection_model_json['route_reports'] = [route_report_model]

        # Construct a model instance of RouteReportCollection by calling from_dict on the json representation
        route_report_collection_model = RouteReportCollection.from_dict(route_report_collection_model_json)
        assert route_report_collection_model != False

        # Construct a model instance of RouteReportCollection by calling from_dict on the json representation
        route_report_collection_model_dict = RouteReportCollection.from_dict(route_report_collection_model_json).__dict__
        route_report_collection_model2 = RouteReportCollection(**route_report_collection_model_dict)

        # Verify the model instances are equivalent
        assert route_report_collection_model == route_report_collection_model2

        # Convert model instance back to dict and verify no loss of data
        route_report_collection_model_json2 = route_report_collection_model.to_dict()
        assert route_report_collection_model_json2 == route_report_collection_model_json


class TestModel_RouteReportConnection:
    """
    Test Class for RouteReportConnection
    """

    def test_route_report_connection_serialization(self):
        """
        Test serialization/deserialization for RouteReportConnection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        route_report_virtual_connection_route_model = {}  # RouteReportVirtualConnectionRoute
        route_report_virtual_connection_route_model['active'] = True
        route_report_virtual_connection_route_model['local_preference'] = '200'
        route_report_virtual_connection_route_model['prefix'] = '172.17.0.0/16'

        # Construct a json representation of a RouteReportConnection model
        route_report_connection_model_json = {}
        route_report_connection_model_json['routes'] = [route_report_virtual_connection_route_model]
        route_report_connection_model_json['virtual_connection_id'] = '3c265a62-91da-4261-a950-950b6af0eb58'
        route_report_connection_model_json['virtual_connection_name'] = 'vpc1'
        route_report_connection_model_json['virtual_connection_type'] = 'vpc'

        # Construct a model instance of RouteReportConnection by calling from_dict on the json representation
        route_report_connection_model = RouteReportConnection.from_dict(route_report_connection_model_json)
        assert route_report_connection_model != False

        # Construct a model instance of RouteReportConnection by calling from_dict on the json representation
        route_report_connection_model_dict = RouteReportConnection.from_dict(route_report_connection_model_json).__dict__
        route_report_connection_model2 = RouteReportConnection(**route_report_connection_model_dict)

        # Verify the model instances are equivalent
        assert route_report_connection_model == route_report_connection_model2

        # Convert model instance back to dict and verify no loss of data
        route_report_connection_model_json2 = route_report_connection_model.to_dict()
        assert route_report_connection_model_json2 == route_report_connection_model_json


class TestModel_RouteReportOnPremRoute:
    """
    Test Class for RouteReportOnPremRoute
    """

    def test_route_report_on_prem_route_serialization(self):
        """
        Test serialization/deserialization for RouteReportOnPremRoute
        """

        # Construct a json representation of a RouteReportOnPremRoute model
        route_report_on_prem_route_model_json = {}
        route_report_on_prem_route_model_json['as_path'] = '64999 64999 64998 I'
        route_report_on_prem_route_model_json['next_hop'] = '172.17.0.0'
        route_report_on_prem_route_model_json['prefix'] = '172.17.0.0/16'

        # Construct a model instance of RouteReportOnPremRoute by calling from_dict on the json representation
        route_report_on_prem_route_model = RouteReportOnPremRoute.from_dict(route_report_on_prem_route_model_json)
        assert route_report_on_prem_route_model != False

        # Construct a model instance of RouteReportOnPremRoute by calling from_dict on the json representation
        route_report_on_prem_route_model_dict = RouteReportOnPremRoute.from_dict(route_report_on_prem_route_model_json).__dict__
        route_report_on_prem_route_model2 = RouteReportOnPremRoute(**route_report_on_prem_route_model_dict)

        # Verify the model instances are equivalent
        assert route_report_on_prem_route_model == route_report_on_prem_route_model2

        # Convert model instance back to dict and verify no loss of data
        route_report_on_prem_route_model_json2 = route_report_on_prem_route_model.to_dict()
        assert route_report_on_prem_route_model_json2 == route_report_on_prem_route_model_json


class TestModel_RouteReportOverlappingRouteGroup:
    """
    Test Class for RouteReportOverlappingRouteGroup
    """

    def test_route_report_overlapping_route_group_serialization(self):
        """
        Test serialization/deserialization for RouteReportOverlappingRouteGroup
        """

        # Construct dict forms of any model objects needed in order to build this model.

        route_report_overlapping_route_model = {}  # RouteReportOverlappingRouteForConnection
        route_report_overlapping_route_model['prefix'] = '172.17.0.0/16'
        route_report_overlapping_route_model['type'] = 'virtual_connection'
        route_report_overlapping_route_model['virtual_connection_id'] = 'd2d985d8-1d8e-4e8b-96cd-cee2290ecaff'

        # Construct a json representation of a RouteReportOverlappingRouteGroup model
        route_report_overlapping_route_group_model_json = {}
        route_report_overlapping_route_group_model_json['routes'] = [route_report_overlapping_route_model]

        # Construct a model instance of RouteReportOverlappingRouteGroup by calling from_dict on the json representation
        route_report_overlapping_route_group_model = RouteReportOverlappingRouteGroup.from_dict(route_report_overlapping_route_group_model_json)
        assert route_report_overlapping_route_group_model != False

        # Construct a model instance of RouteReportOverlappingRouteGroup by calling from_dict on the json representation
        route_report_overlapping_route_group_model_dict = RouteReportOverlappingRouteGroup.from_dict(route_report_overlapping_route_group_model_json).__dict__
        route_report_overlapping_route_group_model2 = RouteReportOverlappingRouteGroup(**route_report_overlapping_route_group_model_dict)

        # Verify the model instances are equivalent
        assert route_report_overlapping_route_group_model == route_report_overlapping_route_group_model2

        # Convert model instance back to dict and verify no loss of data
        route_report_overlapping_route_group_model_json2 = route_report_overlapping_route_group_model.to_dict()
        assert route_report_overlapping_route_group_model_json2 == route_report_overlapping_route_group_model_json


class TestModel_RouteReportRoute:
    """
    Test Class for RouteReportRoute
    """

    def test_route_report_route_serialization(self):
        """
        Test serialization/deserialization for RouteReportRoute
        """

        # Construct a json representation of a RouteReportRoute model
        route_report_route_model_json = {}
        route_report_route_model_json['prefix'] = '172.17.0.0/16'

        # Construct a model instance of RouteReportRoute by calling from_dict on the json representation
        route_report_route_model = RouteReportRoute.from_dict(route_report_route_model_json)
        assert route_report_route_model != False

        # Construct a model instance of RouteReportRoute by calling from_dict on the json representation
        route_report_route_model_dict = RouteReportRoute.from_dict(route_report_route_model_json).__dict__
        route_report_route_model2 = RouteReportRoute(**route_report_route_model_dict)

        # Verify the model instances are equivalent
        assert route_report_route_model == route_report_route_model2

        # Convert model instance back to dict and verify no loss of data
        route_report_route_model_json2 = route_report_route_model.to_dict()
        assert route_report_route_model_json2 == route_report_route_model_json


class TestModel_RouteReportVirtualConnectionRoute:
    """
    Test Class for RouteReportVirtualConnectionRoute
    """

    def test_route_report_virtual_connection_route_serialization(self):
        """
        Test serialization/deserialization for RouteReportVirtualConnectionRoute
        """

        # Construct a json representation of a RouteReportVirtualConnectionRoute model
        route_report_virtual_connection_route_model_json = {}
        route_report_virtual_connection_route_model_json['active'] = True
        route_report_virtual_connection_route_model_json['local_preference'] = '200'
        route_report_virtual_connection_route_model_json['prefix'] = '172.17.0.0/16'

        # Construct a model instance of RouteReportVirtualConnectionRoute by calling from_dict on the json representation
        route_report_virtual_connection_route_model = RouteReportVirtualConnectionRoute.from_dict(route_report_virtual_connection_route_model_json)
        assert route_report_virtual_connection_route_model != False

        # Construct a model instance of RouteReportVirtualConnectionRoute by calling from_dict on the json representation
        route_report_virtual_connection_route_model_dict = RouteReportVirtualConnectionRoute.from_dict(route_report_virtual_connection_route_model_json).__dict__
        route_report_virtual_connection_route_model2 = RouteReportVirtualConnectionRoute(**route_report_virtual_connection_route_model_dict)

        # Verify the model instances are equivalent
        assert route_report_virtual_connection_route_model == route_report_virtual_connection_route_model2

        # Convert model instance back to dict and verify no loss of data
        route_report_virtual_connection_route_model_json2 = route_report_virtual_connection_route_model.to_dict()
        assert route_report_virtual_connection_route_model_json2 == route_report_virtual_connection_route_model_json


class TestModel_UpdateRouteFilterTemplate:
    """
    Test Class for UpdateRouteFilterTemplate
    """

    def test_update_route_filter_template_serialization(self):
        """
        Test serialization/deserialization for UpdateRouteFilterTemplate
        """

        # Construct a json representation of a UpdateRouteFilterTemplate model
        update_route_filter_template_model_json = {}
        update_route_filter_template_model_json['action'] = 'permit'
        update_route_filter_template_model_json['before'] = '1a15dcab-7e40-45e1-b7c5-bc690eaa9782'
        update_route_filter_template_model_json['ge'] = 25
        update_route_filter_template_model_json['le'] = 30
        update_route_filter_template_model_json['prefix'] = '192.168.100.0/24'

        # Construct a model instance of UpdateRouteFilterTemplate by calling from_dict on the json representation
        update_route_filter_template_model = UpdateRouteFilterTemplate.from_dict(update_route_filter_template_model_json)
        assert update_route_filter_template_model != False

        # Construct a model instance of UpdateRouteFilterTemplate by calling from_dict on the json representation
        update_route_filter_template_model_dict = UpdateRouteFilterTemplate.from_dict(update_route_filter_template_model_json).__dict__
        update_route_filter_template_model2 = UpdateRouteFilterTemplate(**update_route_filter_template_model_dict)

        # Verify the model instances are equivalent
        assert update_route_filter_template_model == update_route_filter_template_model2

        # Convert model instance back to dict and verify no loss of data
        update_route_filter_template_model_json2 = update_route_filter_template_model.to_dict()
        assert update_route_filter_template_model_json2 == update_route_filter_template_model_json


class TestModel_AuthenticationKeyIdentityHpcsAuthenticationKeyIdentity:
    """
    Test Class for AuthenticationKeyIdentityHpcsAuthenticationKeyIdentity
    """

    def test_authentication_key_identity_hpcs_authentication_key_identity_serialization(self):
        """
        Test serialization/deserialization for AuthenticationKeyIdentityHpcsAuthenticationKeyIdentity
        """

        # Construct a json representation of a AuthenticationKeyIdentityHpcsAuthenticationKeyIdentity model
        authentication_key_identity_hpcs_authentication_key_identity_model_json = {}
        authentication_key_identity_hpcs_authentication_key_identity_model_json['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a model instance of AuthenticationKeyIdentityHpcsAuthenticationKeyIdentity by calling from_dict on the json representation
        authentication_key_identity_hpcs_authentication_key_identity_model = AuthenticationKeyIdentityHpcsAuthenticationKeyIdentity.from_dict(authentication_key_identity_hpcs_authentication_key_identity_model_json)
        assert authentication_key_identity_hpcs_authentication_key_identity_model != False

        # Construct a model instance of AuthenticationKeyIdentityHpcsAuthenticationKeyIdentity by calling from_dict on the json representation
        authentication_key_identity_hpcs_authentication_key_identity_model_dict = AuthenticationKeyIdentityHpcsAuthenticationKeyIdentity.from_dict(authentication_key_identity_hpcs_authentication_key_identity_model_json).__dict__
        authentication_key_identity_hpcs_authentication_key_identity_model2 = AuthenticationKeyIdentityHpcsAuthenticationKeyIdentity(**authentication_key_identity_hpcs_authentication_key_identity_model_dict)

        # Verify the model instances are equivalent
        assert authentication_key_identity_hpcs_authentication_key_identity_model == authentication_key_identity_hpcs_authentication_key_identity_model2

        # Convert model instance back to dict and verify no loss of data
        authentication_key_identity_hpcs_authentication_key_identity_model_json2 = authentication_key_identity_hpcs_authentication_key_identity_model.to_dict()
        assert authentication_key_identity_hpcs_authentication_key_identity_model_json2 == authentication_key_identity_hpcs_authentication_key_identity_model_json


class TestModel_AuthenticationKeyIdentityKeyProtectAuthenticationKeyIdentity:
    """
    Test Class for AuthenticationKeyIdentityKeyProtectAuthenticationKeyIdentity
    """

    def test_authentication_key_identity_key_protect_authentication_key_identity_serialization(self):
        """
        Test serialization/deserialization for AuthenticationKeyIdentityKeyProtectAuthenticationKeyIdentity
        """

        # Construct a json representation of a AuthenticationKeyIdentityKeyProtectAuthenticationKeyIdentity model
        authentication_key_identity_key_protect_authentication_key_identity_model_json = {}
        authentication_key_identity_key_protect_authentication_key_identity_model_json['crn'] = 'crn:v1:bluemix:public:kms:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a model instance of AuthenticationKeyIdentityKeyProtectAuthenticationKeyIdentity by calling from_dict on the json representation
        authentication_key_identity_key_protect_authentication_key_identity_model = AuthenticationKeyIdentityKeyProtectAuthenticationKeyIdentity.from_dict(authentication_key_identity_key_protect_authentication_key_identity_model_json)
        assert authentication_key_identity_key_protect_authentication_key_identity_model != False

        # Construct a model instance of AuthenticationKeyIdentityKeyProtectAuthenticationKeyIdentity by calling from_dict on the json representation
        authentication_key_identity_key_protect_authentication_key_identity_model_dict = AuthenticationKeyIdentityKeyProtectAuthenticationKeyIdentity.from_dict(authentication_key_identity_key_protect_authentication_key_identity_model_json).__dict__
        authentication_key_identity_key_protect_authentication_key_identity_model2 = AuthenticationKeyIdentityKeyProtectAuthenticationKeyIdentity(**authentication_key_identity_key_protect_authentication_key_identity_model_dict)

        # Verify the model instances are equivalent
        assert authentication_key_identity_key_protect_authentication_key_identity_model == authentication_key_identity_key_protect_authentication_key_identity_model2

        # Convert model instance back to dict and verify no loss of data
        authentication_key_identity_key_protect_authentication_key_identity_model_json2 = authentication_key_identity_key_protect_authentication_key_identity_model.to_dict()
        assert authentication_key_identity_key_protect_authentication_key_identity_model_json2 == authentication_key_identity_key_protect_authentication_key_identity_model_json


class TestModel_AuthenticationKeyReferenceHpcsAuthenticationKeyReference:
    """
    Test Class for AuthenticationKeyReferenceHpcsAuthenticationKeyReference
    """

    def test_authentication_key_reference_hpcs_authentication_key_reference_serialization(self):
        """
        Test serialization/deserialization for AuthenticationKeyReferenceHpcsAuthenticationKeyReference
        """

        # Construct a json representation of a AuthenticationKeyReferenceHpcsAuthenticationKeyReference model
        authentication_key_reference_hpcs_authentication_key_reference_model_json = {}
        authentication_key_reference_hpcs_authentication_key_reference_model_json['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a model instance of AuthenticationKeyReferenceHpcsAuthenticationKeyReference by calling from_dict on the json representation
        authentication_key_reference_hpcs_authentication_key_reference_model = AuthenticationKeyReferenceHpcsAuthenticationKeyReference.from_dict(authentication_key_reference_hpcs_authentication_key_reference_model_json)
        assert authentication_key_reference_hpcs_authentication_key_reference_model != False

        # Construct a model instance of AuthenticationKeyReferenceHpcsAuthenticationKeyReference by calling from_dict on the json representation
        authentication_key_reference_hpcs_authentication_key_reference_model_dict = AuthenticationKeyReferenceHpcsAuthenticationKeyReference.from_dict(authentication_key_reference_hpcs_authentication_key_reference_model_json).__dict__
        authentication_key_reference_hpcs_authentication_key_reference_model2 = AuthenticationKeyReferenceHpcsAuthenticationKeyReference(**authentication_key_reference_hpcs_authentication_key_reference_model_dict)

        # Verify the model instances are equivalent
        assert authentication_key_reference_hpcs_authentication_key_reference_model == authentication_key_reference_hpcs_authentication_key_reference_model2

        # Convert model instance back to dict and verify no loss of data
        authentication_key_reference_hpcs_authentication_key_reference_model_json2 = authentication_key_reference_hpcs_authentication_key_reference_model.to_dict()
        assert authentication_key_reference_hpcs_authentication_key_reference_model_json2 == authentication_key_reference_hpcs_authentication_key_reference_model_json


class TestModel_AuthenticationKeyReferenceKeyProtectAuthenticationKeyReference:
    """
    Test Class for AuthenticationKeyReferenceKeyProtectAuthenticationKeyReference
    """

    def test_authentication_key_reference_key_protect_authentication_key_reference_serialization(self):
        """
        Test serialization/deserialization for AuthenticationKeyReferenceKeyProtectAuthenticationKeyReference
        """

        # Construct a json representation of a AuthenticationKeyReferenceKeyProtectAuthenticationKeyReference model
        authentication_key_reference_key_protect_authentication_key_reference_model_json = {}
        authentication_key_reference_key_protect_authentication_key_reference_model_json['crn'] = 'crn:v1:bluemix:public:kms:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a model instance of AuthenticationKeyReferenceKeyProtectAuthenticationKeyReference by calling from_dict on the json representation
        authentication_key_reference_key_protect_authentication_key_reference_model = AuthenticationKeyReferenceKeyProtectAuthenticationKeyReference.from_dict(authentication_key_reference_key_protect_authentication_key_reference_model_json)
        assert authentication_key_reference_key_protect_authentication_key_reference_model != False

        # Construct a model instance of AuthenticationKeyReferenceKeyProtectAuthenticationKeyReference by calling from_dict on the json representation
        authentication_key_reference_key_protect_authentication_key_reference_model_dict = AuthenticationKeyReferenceKeyProtectAuthenticationKeyReference.from_dict(authentication_key_reference_key_protect_authentication_key_reference_model_json).__dict__
        authentication_key_reference_key_protect_authentication_key_reference_model2 = AuthenticationKeyReferenceKeyProtectAuthenticationKeyReference(**authentication_key_reference_key_protect_authentication_key_reference_model_dict)

        # Verify the model instances are equivalent
        assert authentication_key_reference_key_protect_authentication_key_reference_model == authentication_key_reference_key_protect_authentication_key_reference_model2

        # Convert model instance back to dict and verify no loss of data
        authentication_key_reference_key_protect_authentication_key_reference_model_json2 = authentication_key_reference_key_protect_authentication_key_reference_model.to_dict()
        assert authentication_key_reference_key_protect_authentication_key_reference_model_json2 == authentication_key_reference_key_protect_authentication_key_reference_model_json


class TestModel_GatewayActionTemplateUpdatesItemGatewayClientBGPASNUpdate:
    """
    Test Class for GatewayActionTemplateUpdatesItemGatewayClientBGPASNUpdate
    """

    def test_gateway_action_template_updates_item_gateway_client_bgpasn_update_serialization(self):
        """
        Test serialization/deserialization for GatewayActionTemplateUpdatesItemGatewayClientBGPASNUpdate
        """

        # Construct a json representation of a GatewayActionTemplateUpdatesItemGatewayClientBGPASNUpdate model
        gateway_action_template_updates_item_gateway_client_bgpasn_update_model_json = {}
        gateway_action_template_updates_item_gateway_client_bgpasn_update_model_json['bgp_asn'] = 64999

        # Construct a model instance of GatewayActionTemplateUpdatesItemGatewayClientBGPASNUpdate by calling from_dict on the json representation
        gateway_action_template_updates_item_gateway_client_bgpasn_update_model = GatewayActionTemplateUpdatesItemGatewayClientBGPASNUpdate.from_dict(gateway_action_template_updates_item_gateway_client_bgpasn_update_model_json)
        assert gateway_action_template_updates_item_gateway_client_bgpasn_update_model != False

        # Construct a model instance of GatewayActionTemplateUpdatesItemGatewayClientBGPASNUpdate by calling from_dict on the json representation
        gateway_action_template_updates_item_gateway_client_bgpasn_update_model_dict = GatewayActionTemplateUpdatesItemGatewayClientBGPASNUpdate.from_dict(gateway_action_template_updates_item_gateway_client_bgpasn_update_model_json).__dict__
        gateway_action_template_updates_item_gateway_client_bgpasn_update_model2 = GatewayActionTemplateUpdatesItemGatewayClientBGPASNUpdate(**gateway_action_template_updates_item_gateway_client_bgpasn_update_model_dict)

        # Verify the model instances are equivalent
        assert gateway_action_template_updates_item_gateway_client_bgpasn_update_model == gateway_action_template_updates_item_gateway_client_bgpasn_update_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_action_template_updates_item_gateway_client_bgpasn_update_model_json2 = gateway_action_template_updates_item_gateway_client_bgpasn_update_model.to_dict()
        assert gateway_action_template_updates_item_gateway_client_bgpasn_update_model_json2 == gateway_action_template_updates_item_gateway_client_bgpasn_update_model_json


class TestModel_GatewayActionTemplateUpdatesItemGatewayClientBGPIPUpdate:
    """
    Test Class for GatewayActionTemplateUpdatesItemGatewayClientBGPIPUpdate
    """

    def test_gateway_action_template_updates_item_gateway_client_bgpip_update_serialization(self):
        """
        Test serialization/deserialization for GatewayActionTemplateUpdatesItemGatewayClientBGPIPUpdate
        """

        # Construct a json representation of a GatewayActionTemplateUpdatesItemGatewayClientBGPIPUpdate model
        gateway_action_template_updates_item_gateway_client_bgpip_update_model_json = {}
        gateway_action_template_updates_item_gateway_client_bgpip_update_model_json['bgp_cer_cidr'] = '169.254.0.10/30'
        gateway_action_template_updates_item_gateway_client_bgpip_update_model_json['bgp_ibm_cidr'] = '169.254.0.9/30'

        # Construct a model instance of GatewayActionTemplateUpdatesItemGatewayClientBGPIPUpdate by calling from_dict on the json representation
        gateway_action_template_updates_item_gateway_client_bgpip_update_model = GatewayActionTemplateUpdatesItemGatewayClientBGPIPUpdate.from_dict(gateway_action_template_updates_item_gateway_client_bgpip_update_model_json)
        assert gateway_action_template_updates_item_gateway_client_bgpip_update_model != False

        # Construct a model instance of GatewayActionTemplateUpdatesItemGatewayClientBGPIPUpdate by calling from_dict on the json representation
        gateway_action_template_updates_item_gateway_client_bgpip_update_model_dict = GatewayActionTemplateUpdatesItemGatewayClientBGPIPUpdate.from_dict(gateway_action_template_updates_item_gateway_client_bgpip_update_model_json).__dict__
        gateway_action_template_updates_item_gateway_client_bgpip_update_model2 = GatewayActionTemplateUpdatesItemGatewayClientBGPIPUpdate(**gateway_action_template_updates_item_gateway_client_bgpip_update_model_dict)

        # Verify the model instances are equivalent
        assert gateway_action_template_updates_item_gateway_client_bgpip_update_model == gateway_action_template_updates_item_gateway_client_bgpip_update_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_action_template_updates_item_gateway_client_bgpip_update_model_json2 = gateway_action_template_updates_item_gateway_client_bgpip_update_model.to_dict()
        assert gateway_action_template_updates_item_gateway_client_bgpip_update_model_json2 == gateway_action_template_updates_item_gateway_client_bgpip_update_model_json


class TestModel_GatewayActionTemplateUpdatesItemGatewayClientSpeedUpdate:
    """
    Test Class for GatewayActionTemplateUpdatesItemGatewayClientSpeedUpdate
    """

    def test_gateway_action_template_updates_item_gateway_client_speed_update_serialization(self):
        """
        Test serialization/deserialization for GatewayActionTemplateUpdatesItemGatewayClientSpeedUpdate
        """

        # Construct a json representation of a GatewayActionTemplateUpdatesItemGatewayClientSpeedUpdate model
        gateway_action_template_updates_item_gateway_client_speed_update_model_json = {}
        gateway_action_template_updates_item_gateway_client_speed_update_model_json['speed_mbps'] = 500

        # Construct a model instance of GatewayActionTemplateUpdatesItemGatewayClientSpeedUpdate by calling from_dict on the json representation
        gateway_action_template_updates_item_gateway_client_speed_update_model = GatewayActionTemplateUpdatesItemGatewayClientSpeedUpdate.from_dict(gateway_action_template_updates_item_gateway_client_speed_update_model_json)
        assert gateway_action_template_updates_item_gateway_client_speed_update_model != False

        # Construct a model instance of GatewayActionTemplateUpdatesItemGatewayClientSpeedUpdate by calling from_dict on the json representation
        gateway_action_template_updates_item_gateway_client_speed_update_model_dict = GatewayActionTemplateUpdatesItemGatewayClientSpeedUpdate.from_dict(gateway_action_template_updates_item_gateway_client_speed_update_model_json).__dict__
        gateway_action_template_updates_item_gateway_client_speed_update_model2 = GatewayActionTemplateUpdatesItemGatewayClientSpeedUpdate(**gateway_action_template_updates_item_gateway_client_speed_update_model_dict)

        # Verify the model instances are equivalent
        assert gateway_action_template_updates_item_gateway_client_speed_update_model == gateway_action_template_updates_item_gateway_client_speed_update_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_action_template_updates_item_gateway_client_speed_update_model_json2 = gateway_action_template_updates_item_gateway_client_speed_update_model.to_dict()
        assert gateway_action_template_updates_item_gateway_client_speed_update_model_json2 == gateway_action_template_updates_item_gateway_client_speed_update_model_json


class TestModel_GatewayActionTemplateUpdatesItemGatewayClientVLANUpdate:
    """
    Test Class for GatewayActionTemplateUpdatesItemGatewayClientVLANUpdate
    """

    def test_gateway_action_template_updates_item_gateway_client_vlan_update_serialization(self):
        """
        Test serialization/deserialization for GatewayActionTemplateUpdatesItemGatewayClientVLANUpdate
        """

        # Construct a json representation of a GatewayActionTemplateUpdatesItemGatewayClientVLANUpdate model
        gateway_action_template_updates_item_gateway_client_vlan_update_model_json = {}
        gateway_action_template_updates_item_gateway_client_vlan_update_model_json['vlan'] = 10

        # Construct a model instance of GatewayActionTemplateUpdatesItemGatewayClientVLANUpdate by calling from_dict on the json representation
        gateway_action_template_updates_item_gateway_client_vlan_update_model = GatewayActionTemplateUpdatesItemGatewayClientVLANUpdate.from_dict(gateway_action_template_updates_item_gateway_client_vlan_update_model_json)
        assert gateway_action_template_updates_item_gateway_client_vlan_update_model != False

        # Construct a model instance of GatewayActionTemplateUpdatesItemGatewayClientVLANUpdate by calling from_dict on the json representation
        gateway_action_template_updates_item_gateway_client_vlan_update_model_dict = GatewayActionTemplateUpdatesItemGatewayClientVLANUpdate.from_dict(gateway_action_template_updates_item_gateway_client_vlan_update_model_json).__dict__
        gateway_action_template_updates_item_gateway_client_vlan_update_model2 = GatewayActionTemplateUpdatesItemGatewayClientVLANUpdate(**gateway_action_template_updates_item_gateway_client_vlan_update_model_dict)

        # Verify the model instances are equivalent
        assert gateway_action_template_updates_item_gateway_client_vlan_update_model == gateway_action_template_updates_item_gateway_client_vlan_update_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_action_template_updates_item_gateway_client_vlan_update_model_json2 = gateway_action_template_updates_item_gateway_client_vlan_update_model.to_dict()
        assert gateway_action_template_updates_item_gateway_client_vlan_update_model_json2 == gateway_action_template_updates_item_gateway_client_vlan_update_model_json


class TestModel_GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientBGPASNUpdate:
    """
    Test Class for GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientBGPASNUpdate
    """

    def test_gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpasn_update_serialization(self):
        """
        Test serialization/deserialization for GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientBGPASNUpdate
        """

        # Construct a json representation of a GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientBGPASNUpdate model
        gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpasn_update_model_json = {}
        gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpasn_update_model_json['bgp_asn'] = 64999

        # Construct a model instance of GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientBGPASNUpdate by calling from_dict on the json representation
        gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpasn_update_model = GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientBGPASNUpdate.from_dict(gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpasn_update_model_json)
        assert gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpasn_update_model != False

        # Construct a model instance of GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientBGPASNUpdate by calling from_dict on the json representation
        gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpasn_update_model_dict = GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientBGPASNUpdate.from_dict(gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpasn_update_model_json).__dict__
        gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpasn_update_model2 = GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientBGPASNUpdate(**gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpasn_update_model_dict)

        # Verify the model instances are equivalent
        assert gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpasn_update_model == gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpasn_update_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpasn_update_model_json2 = gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpasn_update_model.to_dict()
        assert gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpasn_update_model_json2 == gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpasn_update_model_json


class TestModel_GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientBGPIPUpdate:
    """
    Test Class for GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientBGPIPUpdate
    """

    def test_gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpip_update_serialization(self):
        """
        Test serialization/deserialization for GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientBGPIPUpdate
        """

        # Construct a json representation of a GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientBGPIPUpdate model
        gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpip_update_model_json = {}
        gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpip_update_model_json['bgp_cer_cidr'] = '169.254.0.10/30'
        gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpip_update_model_json['bgp_ibm_cidr'] = '169.254.0.9/30'

        # Construct a model instance of GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientBGPIPUpdate by calling from_dict on the json representation
        gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpip_update_model = GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientBGPIPUpdate.from_dict(gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpip_update_model_json)
        assert gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpip_update_model != False

        # Construct a model instance of GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientBGPIPUpdate by calling from_dict on the json representation
        gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpip_update_model_dict = GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientBGPIPUpdate.from_dict(gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpip_update_model_json).__dict__
        gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpip_update_model2 = GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientBGPIPUpdate(**gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpip_update_model_dict)

        # Verify the model instances are equivalent
        assert gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpip_update_model == gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpip_update_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpip_update_model_json2 = gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpip_update_model.to_dict()
        assert gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpip_update_model_json2 == gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_bgpip_update_model_json


class TestModel_GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientSpeedUpdate:
    """
    Test Class for GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientSpeedUpdate
    """

    def test_gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_speed_update_serialization(self):
        """
        Test serialization/deserialization for GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientSpeedUpdate
        """

        # Construct a json representation of a GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientSpeedUpdate model
        gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_speed_update_model_json = {}
        gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_speed_update_model_json['speed_mbps'] = 500

        # Construct a model instance of GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientSpeedUpdate by calling from_dict on the json representation
        gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_speed_update_model = GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientSpeedUpdate.from_dict(gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_speed_update_model_json)
        assert gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_speed_update_model != False

        # Construct a model instance of GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientSpeedUpdate by calling from_dict on the json representation
        gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_speed_update_model_dict = GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientSpeedUpdate.from_dict(gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_speed_update_model_json).__dict__
        gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_speed_update_model2 = GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientSpeedUpdate(**gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_speed_update_model_dict)

        # Verify the model instances are equivalent
        assert gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_speed_update_model == gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_speed_update_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_speed_update_model_json2 = gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_speed_update_model.to_dict()
        assert gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_speed_update_model_json2 == gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_speed_update_model_json


class TestModel_GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientVLANUpdate:
    """
    Test Class for GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientVLANUpdate
    """

    def test_gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_vlan_update_serialization(self):
        """
        Test serialization/deserialization for GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientVLANUpdate
        """

        # Construct a json representation of a GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientVLANUpdate model
        gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_vlan_update_model_json = {}
        gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_vlan_update_model_json['vlan'] = 10

        # Construct a model instance of GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientVLANUpdate by calling from_dict on the json representation
        gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_vlan_update_model = GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientVLANUpdate.from_dict(gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_vlan_update_model_json)
        assert gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_vlan_update_model != False

        # Construct a model instance of GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientVLANUpdate by calling from_dict on the json representation
        gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_vlan_update_model_dict = GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientVLANUpdate.from_dict(gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_vlan_update_model_json).__dict__
        gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_vlan_update_model2 = GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientVLANUpdate(**gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_vlan_update_model_dict)

        # Verify the model instances are equivalent
        assert gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_vlan_update_model == gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_vlan_update_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_vlan_update_model_json2 = gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_vlan_update_model.to_dict()
        assert gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_vlan_update_model_json2 == gateway_change_request_gateway_client_gateway_update_attributes_updates_item_gateway_client_vlan_update_model_json


class TestModel_GatewayChangeRequestGatewayClientGatewayCreate:
    """
    Test Class for GatewayChangeRequestGatewayClientGatewayCreate
    """

    def test_gateway_change_request_gateway_client_gateway_create_serialization(self):
        """
        Test serialization/deserialization for GatewayChangeRequestGatewayClientGatewayCreate
        """

        # Construct a json representation of a GatewayChangeRequestGatewayClientGatewayCreate model
        gateway_change_request_gateway_client_gateway_create_model_json = {}
        gateway_change_request_gateway_client_gateway_create_model_json['type'] = 'create_gateway'

        # Construct a model instance of GatewayChangeRequestGatewayClientGatewayCreate by calling from_dict on the json representation
        gateway_change_request_gateway_client_gateway_create_model = GatewayChangeRequestGatewayClientGatewayCreate.from_dict(gateway_change_request_gateway_client_gateway_create_model_json)
        assert gateway_change_request_gateway_client_gateway_create_model != False

        # Construct a model instance of GatewayChangeRequestGatewayClientGatewayCreate by calling from_dict on the json representation
        gateway_change_request_gateway_client_gateway_create_model_dict = GatewayChangeRequestGatewayClientGatewayCreate.from_dict(gateway_change_request_gateway_client_gateway_create_model_json).__dict__
        gateway_change_request_gateway_client_gateway_create_model2 = GatewayChangeRequestGatewayClientGatewayCreate(**gateway_change_request_gateway_client_gateway_create_model_dict)

        # Verify the model instances are equivalent
        assert gateway_change_request_gateway_client_gateway_create_model == gateway_change_request_gateway_client_gateway_create_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_change_request_gateway_client_gateway_create_model_json2 = gateway_change_request_gateway_client_gateway_create_model.to_dict()
        assert gateway_change_request_gateway_client_gateway_create_model_json2 == gateway_change_request_gateway_client_gateway_create_model_json


class TestModel_GatewayChangeRequestGatewayClientGatewayDelete:
    """
    Test Class for GatewayChangeRequestGatewayClientGatewayDelete
    """

    def test_gateway_change_request_gateway_client_gateway_delete_serialization(self):
        """
        Test serialization/deserialization for GatewayChangeRequestGatewayClientGatewayDelete
        """

        # Construct a json representation of a GatewayChangeRequestGatewayClientGatewayDelete model
        gateway_change_request_gateway_client_gateway_delete_model_json = {}
        gateway_change_request_gateway_client_gateway_delete_model_json['type'] = 'delete_gateway'

        # Construct a model instance of GatewayChangeRequestGatewayClientGatewayDelete by calling from_dict on the json representation
        gateway_change_request_gateway_client_gateway_delete_model = GatewayChangeRequestGatewayClientGatewayDelete.from_dict(gateway_change_request_gateway_client_gateway_delete_model_json)
        assert gateway_change_request_gateway_client_gateway_delete_model != False

        # Construct a model instance of GatewayChangeRequestGatewayClientGatewayDelete by calling from_dict on the json representation
        gateway_change_request_gateway_client_gateway_delete_model_dict = GatewayChangeRequestGatewayClientGatewayDelete.from_dict(gateway_change_request_gateway_client_gateway_delete_model_json).__dict__
        gateway_change_request_gateway_client_gateway_delete_model2 = GatewayChangeRequestGatewayClientGatewayDelete(**gateway_change_request_gateway_client_gateway_delete_model_dict)

        # Verify the model instances are equivalent
        assert gateway_change_request_gateway_client_gateway_delete_model == gateway_change_request_gateway_client_gateway_delete_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_change_request_gateway_client_gateway_delete_model_json2 = gateway_change_request_gateway_client_gateway_delete_model.to_dict()
        assert gateway_change_request_gateway_client_gateway_delete_model_json2 == gateway_change_request_gateway_client_gateway_delete_model_json


class TestModel_GatewayChangeRequestGatewayClientGatewayUpdateAttributes:
    """
    Test Class for GatewayChangeRequestGatewayClientGatewayUpdateAttributes
    """

    def test_gateway_change_request_gateway_client_gateway_update_attributes_serialization(self):
        """
        Test serialization/deserialization for GatewayChangeRequestGatewayClientGatewayUpdateAttributes
        """

        # Construct dict forms of any model objects needed in order to build this model.

        gateway_change_request_gateway_client_gateway_update_attributes_updates_item_model = {}  # GatewayChangeRequestGatewayClientGatewayUpdateAttributesUpdatesItemGatewayClientSpeedUpdate
        gateway_change_request_gateway_client_gateway_update_attributes_updates_item_model['speed_mbps'] = 500

        # Construct a json representation of a GatewayChangeRequestGatewayClientGatewayUpdateAttributes model
        gateway_change_request_gateway_client_gateway_update_attributes_model_json = {}
        gateway_change_request_gateway_client_gateway_update_attributes_model_json['type'] = 'update_attributes'
        gateway_change_request_gateway_client_gateway_update_attributes_model_json['updates'] = [gateway_change_request_gateway_client_gateway_update_attributes_updates_item_model]

        # Construct a model instance of GatewayChangeRequestGatewayClientGatewayUpdateAttributes by calling from_dict on the json representation
        gateway_change_request_gateway_client_gateway_update_attributes_model = GatewayChangeRequestGatewayClientGatewayUpdateAttributes.from_dict(gateway_change_request_gateway_client_gateway_update_attributes_model_json)
        assert gateway_change_request_gateway_client_gateway_update_attributes_model != False

        # Construct a model instance of GatewayChangeRequestGatewayClientGatewayUpdateAttributes by calling from_dict on the json representation
        gateway_change_request_gateway_client_gateway_update_attributes_model_dict = GatewayChangeRequestGatewayClientGatewayUpdateAttributes.from_dict(gateway_change_request_gateway_client_gateway_update_attributes_model_json).__dict__
        gateway_change_request_gateway_client_gateway_update_attributes_model2 = GatewayChangeRequestGatewayClientGatewayUpdateAttributes(**gateway_change_request_gateway_client_gateway_update_attributes_model_dict)

        # Verify the model instances are equivalent
        assert gateway_change_request_gateway_client_gateway_update_attributes_model == gateway_change_request_gateway_client_gateway_update_attributes_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_change_request_gateway_client_gateway_update_attributes_model_json2 = gateway_change_request_gateway_client_gateway_update_attributes_model.to_dict()
        assert gateway_change_request_gateway_client_gateway_update_attributes_model_json2 == gateway_change_request_gateway_client_gateway_update_attributes_model_json


class TestModel_GatewayCollectionGatewaysItemCrossAccountGateway:
    """
    Test Class for GatewayCollectionGatewaysItemCrossAccountGateway
    """

    def test_gateway_collection_gateways_item_cross_account_gateway_serialization(self):
        """
        Test serialization/deserialization for GatewayCollectionGatewaysItemCrossAccountGateway
        """

        # Construct dict forms of any model objects needed in order to build this model.

        gateway_port_reference_model = {}  # GatewayPortReference
        gateway_port_reference_model['id'] = '54321b1a-fee4-41c7-9e11-9cd99e000aaa'

        # Construct a json representation of a GatewayCollectionGatewaysItemCrossAccountGateway model
        gateway_collection_gateways_item_cross_account_gateway_model_json = {}
        gateway_collection_gateways_item_cross_account_gateway_model_json['bgp_status'] = 'active'
        gateway_collection_gateways_item_cross_account_gateway_model_json['bgp_status_updated_at'] = '2020-08-20T06:58:41.909000Z'
        gateway_collection_gateways_item_cross_account_gateway_model_json['connection_mode'] = 'transit'
        gateway_collection_gateways_item_cross_account_gateway_model_json['created_at'] = '2019-01-01T12:00:00Z'
        gateway_collection_gateways_item_cross_account_gateway_model_json['crn'] = 'crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::dedicated:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        gateway_collection_gateways_item_cross_account_gateway_model_json['cross_account'] = True
        gateway_collection_gateways_item_cross_account_gateway_model_json['cross_connect_router'] = 'xcr01.dal03'
        gateway_collection_gateways_item_cross_account_gateway_model_json['global'] = True
        gateway_collection_gateways_item_cross_account_gateway_model_json['id'] = 'ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        gateway_collection_gateways_item_cross_account_gateway_model_json['link_status'] = 'up'
        gateway_collection_gateways_item_cross_account_gateway_model_json['link_status_updated_at'] = '2020-08-20T06:58:41.909000Z'
        gateway_collection_gateways_item_cross_account_gateway_model_json['location_display_name'] = 'Dallas 03'
        gateway_collection_gateways_item_cross_account_gateway_model_json['location_name'] = 'dal03'
        gateway_collection_gateways_item_cross_account_gateway_model_json['name'] = 'myGateway'
        gateway_collection_gateways_item_cross_account_gateway_model_json['operational_status'] = 'awaiting_completion_notice'
        gateway_collection_gateways_item_cross_account_gateway_model_json['port'] = gateway_port_reference_model
        gateway_collection_gateways_item_cross_account_gateway_model_json['speed_mbps'] = 1000
        gateway_collection_gateways_item_cross_account_gateway_model_json['type'] = 'dedicated'

        # Construct a model instance of GatewayCollectionGatewaysItemCrossAccountGateway by calling from_dict on the json representation
        gateway_collection_gateways_item_cross_account_gateway_model = GatewayCollectionGatewaysItemCrossAccountGateway.from_dict(gateway_collection_gateways_item_cross_account_gateway_model_json)
        assert gateway_collection_gateways_item_cross_account_gateway_model != False

        # Construct a model instance of GatewayCollectionGatewaysItemCrossAccountGateway by calling from_dict on the json representation
        gateway_collection_gateways_item_cross_account_gateway_model_dict = GatewayCollectionGatewaysItemCrossAccountGateway.from_dict(gateway_collection_gateways_item_cross_account_gateway_model_json).__dict__
        gateway_collection_gateways_item_cross_account_gateway_model2 = GatewayCollectionGatewaysItemCrossAccountGateway(**gateway_collection_gateways_item_cross_account_gateway_model_dict)

        # Verify the model instances are equivalent
        assert gateway_collection_gateways_item_cross_account_gateway_model == gateway_collection_gateways_item_cross_account_gateway_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_collection_gateways_item_cross_account_gateway_model_json2 = gateway_collection_gateways_item_cross_account_gateway_model.to_dict()
        assert gateway_collection_gateways_item_cross_account_gateway_model_json2 == gateway_collection_gateways_item_cross_account_gateway_model_json


class TestModel_GatewayCollectionGatewaysItemGateway:
    """
    Test Class for GatewayCollectionGatewaysItemGateway
    """

    def test_gateway_collection_gateways_item_gateway_serialization(self):
        """
        Test serialization/deserialization for GatewayCollectionGatewaysItemGateway
        """

        # Construct dict forms of any model objects needed in order to build this model.

        as_prepend_model = {}  # AsPrepend
        as_prepend_model['created_at'] = '2019-01-01T12:00:00Z'
        as_prepend_model['id'] = 'ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        as_prepend_model['length'] = 4
        as_prepend_model['policy'] = 'import'
        as_prepend_model['prefix'] = '172.17.0.0/16'
        as_prepend_model['specific_prefixes'] = ['192.168.3.0/24']
        as_prepend_model['updated_at'] = '2019-01-01T12:00:00Z'

        authentication_key_reference_model = {}  # AuthenticationKeyReferenceKeyProtectAuthenticationKeyReference
        authentication_key_reference_model['crn'] = 'crn:v1:bluemix:public:kms:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        gateway_bfd_config_model = {}  # GatewayBfdConfig
        gateway_bfd_config_model['bfd_status'] = 'up'
        gateway_bfd_config_model['bfd_status_updated_at'] = '2020-08-20T06:58:41.909000Z'
        gateway_bfd_config_model['interval'] = 2000
        gateway_bfd_config_model['multiplier'] = 10

        gateway_change_request_model = {}  # GatewayChangeRequestGatewayClientGatewayCreate
        gateway_change_request_model['type'] = 'create_gateway'

        gateway_macsec_status_reason_model = {}  # GatewayMacsecStatusReason
        gateway_macsec_status_reason_model['code'] = 'macsec_cak_failed'
        gateway_macsec_status_reason_model['message'] = 'The `authentication_key` failed configuration.'
        gateway_macsec_status_reason_model['more_info'] = 'https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK'

        gateway_macsec_reference_model = {}  # GatewayMacsecReference
        gateway_macsec_reference_model['active'] = True
        gateway_macsec_reference_model['security_policy'] = 'must_secure'
        gateway_macsec_reference_model['status'] = 'secured'
        gateway_macsec_reference_model['status_reasons'] = [gateway_macsec_status_reason_model]

        gateway_status_reason_model = {}  # GatewayStatusReason
        gateway_status_reason_model['code'] = 'authentication_key_failed'
        gateway_status_reason_model['message'] = 'The `authentication_key` failed configuration.'
        gateway_status_reason_model['more_info'] = 'https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK'

        gateway_port_reference_model = {}  # GatewayPortReference
        gateway_port_reference_model['id'] = '54321b1a-fee4-41c7-9e11-9cd99e000aaa'

        resource_group_reference_model = {}  # ResourceGroupReference
        resource_group_reference_model['id'] = '56969d6043e9465c883cb9f7363e78e8'

        # Construct a json representation of a GatewayCollectionGatewaysItemGateway model
        gateway_collection_gateways_item_gateway_model_json = {}
        gateway_collection_gateways_item_gateway_model_json['as_prepends'] = [as_prepend_model]
        gateway_collection_gateways_item_gateway_model_json['authentication_key'] = authentication_key_reference_model
        gateway_collection_gateways_item_gateway_model_json['bfd_config'] = gateway_bfd_config_model
        gateway_collection_gateways_item_gateway_model_json['bgp_asn'] = 64999
        gateway_collection_gateways_item_gateway_model_json['bgp_base_cidr'] = 'testString'
        gateway_collection_gateways_item_gateway_model_json['bgp_cer_cidr'] = '10.254.30.78/30'
        gateway_collection_gateways_item_gateway_model_json['bgp_ibm_asn'] = 13884
        gateway_collection_gateways_item_gateway_model_json['bgp_ibm_cidr'] = '10.254.30.77/30'
        gateway_collection_gateways_item_gateway_model_json['bgp_status'] = 'active'
        gateway_collection_gateways_item_gateway_model_json['bgp_status_updated_at'] = '2020-08-20T06:58:41.909000Z'
        gateway_collection_gateways_item_gateway_model_json['carrier_name'] = 'myCarrierName'
        gateway_collection_gateways_item_gateway_model_json['change_request'] = gateway_change_request_model
        gateway_collection_gateways_item_gateway_model_json['completion_notice_reject_reason'] = 'The completion notice file was blank'
        gateway_collection_gateways_item_gateway_model_json['connection_mode'] = 'transit'
        gateway_collection_gateways_item_gateway_model_json['created_at'] = '2019-01-01T12:00:00Z'
        gateway_collection_gateways_item_gateway_model_json['crn'] = 'crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::dedicated:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        gateway_collection_gateways_item_gateway_model_json['cross_account'] = False
        gateway_collection_gateways_item_gateway_model_json['cross_connect_router'] = 'xcr01.dal03'
        gateway_collection_gateways_item_gateway_model_json['customer_name'] = 'newCustomerName'
        gateway_collection_gateways_item_gateway_model_json['default_export_route_filter'] = 'permit'
        gateway_collection_gateways_item_gateway_model_json['default_import_route_filter'] = 'permit'
        gateway_collection_gateways_item_gateway_model_json['global'] = True
        gateway_collection_gateways_item_gateway_model_json['id'] = 'ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        gateway_collection_gateways_item_gateway_model_json['link_status'] = 'up'
        gateway_collection_gateways_item_gateway_model_json['link_status_updated_at'] = '2020-08-20T06:58:41.909000Z'
        gateway_collection_gateways_item_gateway_model_json['location_display_name'] = 'Dallas 03'
        gateway_collection_gateways_item_gateway_model_json['location_name'] = 'dal03'
        gateway_collection_gateways_item_gateway_model_json['macsec'] = gateway_macsec_reference_model
        gateway_collection_gateways_item_gateway_model_json['macsec_capability'] = 'non_macsec'
        gateway_collection_gateways_item_gateway_model_json['metered'] = False
        gateway_collection_gateways_item_gateway_model_json['name'] = 'myGateway'
        gateway_collection_gateways_item_gateway_model_json['operational_status'] = 'awaiting_completion_notice'
        gateway_collection_gateways_item_gateway_model_json['operational_status_reasons'] = [gateway_status_reason_model]
        gateway_collection_gateways_item_gateway_model_json['patch_panel_completion_notice'] = 'patch panel configuration details'
        gateway_collection_gateways_item_gateway_model_json['port'] = gateway_port_reference_model
        gateway_collection_gateways_item_gateway_model_json['provider_api_managed'] = False
        gateway_collection_gateways_item_gateway_model_json['resource_group'] = resource_group_reference_model
        gateway_collection_gateways_item_gateway_model_json['speed_mbps'] = 1000
        gateway_collection_gateways_item_gateway_model_json['type'] = 'dedicated'
        gateway_collection_gateways_item_gateway_model_json['vlan'] = 10

        # Construct a model instance of GatewayCollectionGatewaysItemGateway by calling from_dict on the json representation
        gateway_collection_gateways_item_gateway_model = GatewayCollectionGatewaysItemGateway.from_dict(gateway_collection_gateways_item_gateway_model_json)
        assert gateway_collection_gateways_item_gateway_model != False

        # Construct a model instance of GatewayCollectionGatewaysItemGateway by calling from_dict on the json representation
        gateway_collection_gateways_item_gateway_model_dict = GatewayCollectionGatewaysItemGateway.from_dict(gateway_collection_gateways_item_gateway_model_json).__dict__
        gateway_collection_gateways_item_gateway_model2 = GatewayCollectionGatewaysItemGateway(**gateway_collection_gateways_item_gateway_model_dict)

        # Verify the model instances are equivalent
        assert gateway_collection_gateways_item_gateway_model == gateway_collection_gateways_item_gateway_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_collection_gateways_item_gateway_model_json2 = gateway_collection_gateways_item_gateway_model.to_dict()
        assert gateway_collection_gateways_item_gateway_model_json2 == gateway_collection_gateways_item_gateway_model_json


class TestModel_GatewayStatusGatewayBFDStatus:
    """
    Test Class for GatewayStatusGatewayBFDStatus
    """

    def test_gateway_status_gateway_bfd_status_serialization(self):
        """
        Test serialization/deserialization for GatewayStatusGatewayBFDStatus
        """

        # Construct a json representation of a GatewayStatusGatewayBFDStatus model
        gateway_status_gateway_bfd_status_model_json = {}
        gateway_status_gateway_bfd_status_model_json['type'] = 'bfd'
        gateway_status_gateway_bfd_status_model_json['updated_at'] = '2020-08-20T06:58:41.909000Z'
        gateway_status_gateway_bfd_status_model_json['value'] = 'up'

        # Construct a model instance of GatewayStatusGatewayBFDStatus by calling from_dict on the json representation
        gateway_status_gateway_bfd_status_model = GatewayStatusGatewayBFDStatus.from_dict(gateway_status_gateway_bfd_status_model_json)
        assert gateway_status_gateway_bfd_status_model != False

        # Construct a model instance of GatewayStatusGatewayBFDStatus by calling from_dict on the json representation
        gateway_status_gateway_bfd_status_model_dict = GatewayStatusGatewayBFDStatus.from_dict(gateway_status_gateway_bfd_status_model_json).__dict__
        gateway_status_gateway_bfd_status_model2 = GatewayStatusGatewayBFDStatus(**gateway_status_gateway_bfd_status_model_dict)

        # Verify the model instances are equivalent
        assert gateway_status_gateway_bfd_status_model == gateway_status_gateway_bfd_status_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_status_gateway_bfd_status_model_json2 = gateway_status_gateway_bfd_status_model.to_dict()
        assert gateway_status_gateway_bfd_status_model_json2 == gateway_status_gateway_bfd_status_model_json


class TestModel_GatewayStatusGatewayBGPStatus:
    """
    Test Class for GatewayStatusGatewayBGPStatus
    """

    def test_gateway_status_gateway_bgp_status_serialization(self):
        """
        Test serialization/deserialization for GatewayStatusGatewayBGPStatus
        """

        # Construct a json representation of a GatewayStatusGatewayBGPStatus model
        gateway_status_gateway_bgp_status_model_json = {}
        gateway_status_gateway_bgp_status_model_json['type'] = 'bgp'
        gateway_status_gateway_bgp_status_model_json['updated_at'] = '2020-08-20T06:58:41.909000Z'
        gateway_status_gateway_bgp_status_model_json['value'] = 'active'

        # Construct a model instance of GatewayStatusGatewayBGPStatus by calling from_dict on the json representation
        gateway_status_gateway_bgp_status_model = GatewayStatusGatewayBGPStatus.from_dict(gateway_status_gateway_bgp_status_model_json)
        assert gateway_status_gateway_bgp_status_model != False

        # Construct a model instance of GatewayStatusGatewayBGPStatus by calling from_dict on the json representation
        gateway_status_gateway_bgp_status_model_dict = GatewayStatusGatewayBGPStatus.from_dict(gateway_status_gateway_bgp_status_model_json).__dict__
        gateway_status_gateway_bgp_status_model2 = GatewayStatusGatewayBGPStatus(**gateway_status_gateway_bgp_status_model_dict)

        # Verify the model instances are equivalent
        assert gateway_status_gateway_bgp_status_model == gateway_status_gateway_bgp_status_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_status_gateway_bgp_status_model_json2 = gateway_status_gateway_bgp_status_model.to_dict()
        assert gateway_status_gateway_bgp_status_model_json2 == gateway_status_gateway_bgp_status_model_json


class TestModel_GatewayStatusGatewayLinkStatus:
    """
    Test Class for GatewayStatusGatewayLinkStatus
    """

    def test_gateway_status_gateway_link_status_serialization(self):
        """
        Test serialization/deserialization for GatewayStatusGatewayLinkStatus
        """

        # Construct a json representation of a GatewayStatusGatewayLinkStatus model
        gateway_status_gateway_link_status_model_json = {}
        gateway_status_gateway_link_status_model_json['type'] = 'link'
        gateway_status_gateway_link_status_model_json['updated_at'] = '2020-08-20T06:58:41.909000Z'
        gateway_status_gateway_link_status_model_json['value'] = 'up'

        # Construct a model instance of GatewayStatusGatewayLinkStatus by calling from_dict on the json representation
        gateway_status_gateway_link_status_model = GatewayStatusGatewayLinkStatus.from_dict(gateway_status_gateway_link_status_model_json)
        assert gateway_status_gateway_link_status_model != False

        # Construct a model instance of GatewayStatusGatewayLinkStatus by calling from_dict on the json representation
        gateway_status_gateway_link_status_model_dict = GatewayStatusGatewayLinkStatus.from_dict(gateway_status_gateway_link_status_model_json).__dict__
        gateway_status_gateway_link_status_model2 = GatewayStatusGatewayLinkStatus(**gateway_status_gateway_link_status_model_dict)

        # Verify the model instances are equivalent
        assert gateway_status_gateway_link_status_model == gateway_status_gateway_link_status_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_status_gateway_link_status_model_json2 = gateway_status_gateway_link_status_model.to_dict()
        assert gateway_status_gateway_link_status_model_json2 == gateway_status_gateway_link_status_model_json


class TestModel_GatewayTemplateGatewayTypeConnectTemplate:
    """
    Test Class for GatewayTemplateGatewayTypeConnectTemplate
    """

    def test_gateway_template_gateway_type_connect_template_serialization(self):
        """
        Test serialization/deserialization for GatewayTemplateGatewayTypeConnectTemplate
        """

        # Construct dict forms of any model objects needed in order to build this model.

        as_prepend_template_model = {}  # AsPrependTemplate
        as_prepend_template_model['length'] = 4
        as_prepend_template_model['policy'] = 'import'
        as_prepend_template_model['prefix'] = '172.17.0.0/16'
        as_prepend_template_model['specific_prefixes'] = ['192.168.3.0/24']

        authentication_key_identity_model = {}  # AuthenticationKeyIdentityKeyProtectAuthenticationKeyIdentity
        authentication_key_identity_model['crn'] = 'crn:v1:bluemix:public:kms:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        gateway_bfd_config_template_model = {}  # GatewayBfdConfigTemplate
        gateway_bfd_config_template_model['interval'] = 2000
        gateway_bfd_config_template_model['multiplier'] = 10

        gateway_template_route_filter_model = {}  # GatewayTemplateRouteFilter
        gateway_template_route_filter_model['action'] = 'permit'
        gateway_template_route_filter_model['ge'] = 25
        gateway_template_route_filter_model['le'] = 30
        gateway_template_route_filter_model['prefix'] = '192.168.100.0/24'

        resource_group_identity_model = {}  # ResourceGroupIdentity
        resource_group_identity_model['id'] = '56969d6043e9465c883cb9f7363e78e8'

        gateway_port_identity_model = {}  # GatewayPortIdentity
        gateway_port_identity_model['id'] = 'fffdcb1a-fee4-41c7-9e11-9cd99e65c777'

        # Construct a json representation of a GatewayTemplateGatewayTypeConnectTemplate model
        gateway_template_gateway_type_connect_template_model_json = {}
        gateway_template_gateway_type_connect_template_model_json['as_prepends'] = [as_prepend_template_model]
        gateway_template_gateway_type_connect_template_model_json['authentication_key'] = authentication_key_identity_model
        gateway_template_gateway_type_connect_template_model_json['bfd_config'] = gateway_bfd_config_template_model
        gateway_template_gateway_type_connect_template_model_json['bgp_asn'] = 64999
        gateway_template_gateway_type_connect_template_model_json['bgp_base_cidr'] = 'testString'
        gateway_template_gateway_type_connect_template_model_json['bgp_cer_cidr'] = '169.254.0.10/30'
        gateway_template_gateway_type_connect_template_model_json['bgp_ibm_cidr'] = '169.254.0.9/30'
        gateway_template_gateway_type_connect_template_model_json['connection_mode'] = 'transit'
        gateway_template_gateway_type_connect_template_model_json['default_export_route_filter'] = 'permit'
        gateway_template_gateway_type_connect_template_model_json['default_import_route_filter'] = 'permit'
        gateway_template_gateway_type_connect_template_model_json['export_route_filters'] = [gateway_template_route_filter_model]
        gateway_template_gateway_type_connect_template_model_json['global'] = True
        gateway_template_gateway_type_connect_template_model_json['import_route_filters'] = [gateway_template_route_filter_model]
        gateway_template_gateway_type_connect_template_model_json['metered'] = False
        gateway_template_gateway_type_connect_template_model_json['name'] = 'myGateway'
        gateway_template_gateway_type_connect_template_model_json['patch_panel_completion_notice'] = 'patch panel configuration details'
        gateway_template_gateway_type_connect_template_model_json['resource_group'] = resource_group_identity_model
        gateway_template_gateway_type_connect_template_model_json['speed_mbps'] = 1000
        gateway_template_gateway_type_connect_template_model_json['type'] = 'dedicated'
        gateway_template_gateway_type_connect_template_model_json['port'] = gateway_port_identity_model

        # Construct a model instance of GatewayTemplateGatewayTypeConnectTemplate by calling from_dict on the json representation
        gateway_template_gateway_type_connect_template_model = GatewayTemplateGatewayTypeConnectTemplate.from_dict(gateway_template_gateway_type_connect_template_model_json)
        assert gateway_template_gateway_type_connect_template_model != False

        # Construct a model instance of GatewayTemplateGatewayTypeConnectTemplate by calling from_dict on the json representation
        gateway_template_gateway_type_connect_template_model_dict = GatewayTemplateGatewayTypeConnectTemplate.from_dict(gateway_template_gateway_type_connect_template_model_json).__dict__
        gateway_template_gateway_type_connect_template_model2 = GatewayTemplateGatewayTypeConnectTemplate(**gateway_template_gateway_type_connect_template_model_dict)

        # Verify the model instances are equivalent
        assert gateway_template_gateway_type_connect_template_model == gateway_template_gateway_type_connect_template_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_template_gateway_type_connect_template_model_json2 = gateway_template_gateway_type_connect_template_model.to_dict()
        assert gateway_template_gateway_type_connect_template_model_json2 == gateway_template_gateway_type_connect_template_model_json


class TestModel_GatewayTemplateGatewayTypeDedicatedTemplate:
    """
    Test Class for GatewayTemplateGatewayTypeDedicatedTemplate
    """

    def test_gateway_template_gateway_type_dedicated_template_serialization(self):
        """
        Test serialization/deserialization for GatewayTemplateGatewayTypeDedicatedTemplate
        """

        # Construct dict forms of any model objects needed in order to build this model.

        as_prepend_template_model = {}  # AsPrependTemplate
        as_prepend_template_model['length'] = 4
        as_prepend_template_model['policy'] = 'import'
        as_prepend_template_model['prefix'] = '172.17.0.0/16'
        as_prepend_template_model['specific_prefixes'] = ['192.168.3.0/24']

        authentication_key_identity_model = {}  # AuthenticationKeyIdentityKeyProtectAuthenticationKeyIdentity
        authentication_key_identity_model['crn'] = 'crn:v1:bluemix:public:kms:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        gateway_bfd_config_template_model = {}  # GatewayBfdConfigTemplate
        gateway_bfd_config_template_model['interval'] = 2000
        gateway_bfd_config_template_model['multiplier'] = 10

        gateway_template_route_filter_model = {}  # GatewayTemplateRouteFilter
        gateway_template_route_filter_model['action'] = 'permit'
        gateway_template_route_filter_model['ge'] = 25
        gateway_template_route_filter_model['le'] = 30
        gateway_template_route_filter_model['prefix'] = '192.168.100.0/24'

        resource_group_identity_model = {}  # ResourceGroupIdentity
        resource_group_identity_model['id'] = '56969d6043e9465c883cb9f7363e78e8'

        hpcs_key_identity_model = {}  # HpcsKeyIdentity
        hpcs_key_identity_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        gateway_macsec_cak_prototype_model = {}  # GatewayMacsecCakPrototype
        gateway_macsec_cak_prototype_model['key'] = hpcs_key_identity_model
        gateway_macsec_cak_prototype_model['name'] = '1000'
        gateway_macsec_cak_prototype_model['session'] = 'primary'

        sak_rekey_prototype_model = {}  # SakRekeyPrototypeSakRekeyTimerModePrototype
        sak_rekey_prototype_model['interval'] = 3600
        sak_rekey_prototype_model['mode'] = 'timer'

        gateway_macsec_prototype_model = {}  # GatewayMacsecPrototype
        gateway_macsec_prototype_model['active'] = True
        gateway_macsec_prototype_model['caks'] = [gateway_macsec_cak_prototype_model]
        gateway_macsec_prototype_model['sak_rekey'] = sak_rekey_prototype_model
        gateway_macsec_prototype_model['security_policy'] = 'must_secure'
        gateway_macsec_prototype_model['window_size'] = 64

        # Construct a json representation of a GatewayTemplateGatewayTypeDedicatedTemplate model
        gateway_template_gateway_type_dedicated_template_model_json = {}
        gateway_template_gateway_type_dedicated_template_model_json['as_prepends'] = [as_prepend_template_model]
        gateway_template_gateway_type_dedicated_template_model_json['authentication_key'] = authentication_key_identity_model
        gateway_template_gateway_type_dedicated_template_model_json['bfd_config'] = gateway_bfd_config_template_model
        gateway_template_gateway_type_dedicated_template_model_json['bgp_asn'] = 64999
        gateway_template_gateway_type_dedicated_template_model_json['bgp_base_cidr'] = 'testString'
        gateway_template_gateway_type_dedicated_template_model_json['bgp_cer_cidr'] = '169.254.0.10/30'
        gateway_template_gateway_type_dedicated_template_model_json['bgp_ibm_cidr'] = '169.254.0.9/30'
        gateway_template_gateway_type_dedicated_template_model_json['connection_mode'] = 'transit'
        gateway_template_gateway_type_dedicated_template_model_json['default_export_route_filter'] = 'permit'
        gateway_template_gateway_type_dedicated_template_model_json['default_import_route_filter'] = 'permit'
        gateway_template_gateway_type_dedicated_template_model_json['export_route_filters'] = [gateway_template_route_filter_model]
        gateway_template_gateway_type_dedicated_template_model_json['global'] = True
        gateway_template_gateway_type_dedicated_template_model_json['import_route_filters'] = [gateway_template_route_filter_model]
        gateway_template_gateway_type_dedicated_template_model_json['metered'] = False
        gateway_template_gateway_type_dedicated_template_model_json['name'] = 'myGateway'
        gateway_template_gateway_type_dedicated_template_model_json['patch_panel_completion_notice'] = 'patch panel configuration details'
        gateway_template_gateway_type_dedicated_template_model_json['resource_group'] = resource_group_identity_model
        gateway_template_gateway_type_dedicated_template_model_json['speed_mbps'] = 1000
        gateway_template_gateway_type_dedicated_template_model_json['type'] = 'dedicated'
        gateway_template_gateway_type_dedicated_template_model_json['carrier_name'] = 'myCarrierName'
        gateway_template_gateway_type_dedicated_template_model_json['cross_connect_router'] = 'xcr01.dal03'
        gateway_template_gateway_type_dedicated_template_model_json['customer_name'] = 'newCustomerName'
        gateway_template_gateway_type_dedicated_template_model_json['location_name'] = 'dal03'
        gateway_template_gateway_type_dedicated_template_model_json['macsec'] = gateway_macsec_prototype_model
        gateway_template_gateway_type_dedicated_template_model_json['macsec_capability'] = 'non_macsec'
        gateway_template_gateway_type_dedicated_template_model_json['vlan'] = 10

        # Construct a model instance of GatewayTemplateGatewayTypeDedicatedTemplate by calling from_dict on the json representation
        gateway_template_gateway_type_dedicated_template_model = GatewayTemplateGatewayTypeDedicatedTemplate.from_dict(gateway_template_gateway_type_dedicated_template_model_json)
        assert gateway_template_gateway_type_dedicated_template_model != False

        # Construct a model instance of GatewayTemplateGatewayTypeDedicatedTemplate by calling from_dict on the json representation
        gateway_template_gateway_type_dedicated_template_model_dict = GatewayTemplateGatewayTypeDedicatedTemplate.from_dict(gateway_template_gateway_type_dedicated_template_model_json).__dict__
        gateway_template_gateway_type_dedicated_template_model2 = GatewayTemplateGatewayTypeDedicatedTemplate(**gateway_template_gateway_type_dedicated_template_model_dict)

        # Verify the model instances are equivalent
        assert gateway_template_gateway_type_dedicated_template_model == gateway_template_gateway_type_dedicated_template_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_template_gateway_type_dedicated_template_model_json2 = gateway_template_gateway_type_dedicated_template_model.to_dict()
        assert gateway_template_gateway_type_dedicated_template_model_json2 == gateway_template_gateway_type_dedicated_template_model_json


class TestModel_GetGatewayResponseCrossAccountGateway:
    """
    Test Class for GetGatewayResponseCrossAccountGateway
    """

    def test_get_gateway_response_cross_account_gateway_serialization(self):
        """
        Test serialization/deserialization for GetGatewayResponseCrossAccountGateway
        """

        # Construct dict forms of any model objects needed in order to build this model.

        gateway_port_reference_model = {}  # GatewayPortReference
        gateway_port_reference_model['id'] = '54321b1a-fee4-41c7-9e11-9cd99e000aaa'

        # Construct a json representation of a GetGatewayResponseCrossAccountGateway model
        get_gateway_response_cross_account_gateway_model_json = {}
        get_gateway_response_cross_account_gateway_model_json['bgp_status'] = 'active'
        get_gateway_response_cross_account_gateway_model_json['bgp_status_updated_at'] = '2020-08-20T06:58:41.909000Z'
        get_gateway_response_cross_account_gateway_model_json['connection_mode'] = 'transit'
        get_gateway_response_cross_account_gateway_model_json['created_at'] = '2019-01-01T12:00:00Z'
        get_gateway_response_cross_account_gateway_model_json['crn'] = 'crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::dedicated:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        get_gateway_response_cross_account_gateway_model_json['cross_account'] = True
        get_gateway_response_cross_account_gateway_model_json['cross_connect_router'] = 'xcr01.dal03'
        get_gateway_response_cross_account_gateway_model_json['global'] = True
        get_gateway_response_cross_account_gateway_model_json['id'] = 'ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        get_gateway_response_cross_account_gateway_model_json['link_status'] = 'up'
        get_gateway_response_cross_account_gateway_model_json['link_status_updated_at'] = '2020-08-20T06:58:41.909000Z'
        get_gateway_response_cross_account_gateway_model_json['location_display_name'] = 'Dallas 03'
        get_gateway_response_cross_account_gateway_model_json['location_name'] = 'dal03'
        get_gateway_response_cross_account_gateway_model_json['name'] = 'myGateway'
        get_gateway_response_cross_account_gateway_model_json['operational_status'] = 'awaiting_completion_notice'
        get_gateway_response_cross_account_gateway_model_json['port'] = gateway_port_reference_model
        get_gateway_response_cross_account_gateway_model_json['speed_mbps'] = 1000
        get_gateway_response_cross_account_gateway_model_json['type'] = 'dedicated'

        # Construct a model instance of GetGatewayResponseCrossAccountGateway by calling from_dict on the json representation
        get_gateway_response_cross_account_gateway_model = GetGatewayResponseCrossAccountGateway.from_dict(get_gateway_response_cross_account_gateway_model_json)
        assert get_gateway_response_cross_account_gateway_model != False

        # Construct a model instance of GetGatewayResponseCrossAccountGateway by calling from_dict on the json representation
        get_gateway_response_cross_account_gateway_model_dict = GetGatewayResponseCrossAccountGateway.from_dict(get_gateway_response_cross_account_gateway_model_json).__dict__
        get_gateway_response_cross_account_gateway_model2 = GetGatewayResponseCrossAccountGateway(**get_gateway_response_cross_account_gateway_model_dict)

        # Verify the model instances are equivalent
        assert get_gateway_response_cross_account_gateway_model == get_gateway_response_cross_account_gateway_model2

        # Convert model instance back to dict and verify no loss of data
        get_gateway_response_cross_account_gateway_model_json2 = get_gateway_response_cross_account_gateway_model.to_dict()
        assert get_gateway_response_cross_account_gateway_model_json2 == get_gateway_response_cross_account_gateway_model_json


class TestModel_GetGatewayResponseGateway:
    """
    Test Class for GetGatewayResponseGateway
    """

    def test_get_gateway_response_gateway_serialization(self):
        """
        Test serialization/deserialization for GetGatewayResponseGateway
        """

        # Construct dict forms of any model objects needed in order to build this model.

        as_prepend_model = {}  # AsPrepend
        as_prepend_model['created_at'] = '2019-01-01T12:00:00Z'
        as_prepend_model['id'] = 'ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        as_prepend_model['length'] = 4
        as_prepend_model['policy'] = 'import'
        as_prepend_model['prefix'] = '172.17.0.0/16'
        as_prepend_model['specific_prefixes'] = ['192.168.3.0/24']
        as_prepend_model['updated_at'] = '2019-01-01T12:00:00Z'

        authentication_key_reference_model = {}  # AuthenticationKeyReferenceKeyProtectAuthenticationKeyReference
        authentication_key_reference_model['crn'] = 'crn:v1:bluemix:public:kms:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        gateway_bfd_config_model = {}  # GatewayBfdConfig
        gateway_bfd_config_model['bfd_status'] = 'up'
        gateway_bfd_config_model['bfd_status_updated_at'] = '2020-08-20T06:58:41.909000Z'
        gateway_bfd_config_model['interval'] = 2000
        gateway_bfd_config_model['multiplier'] = 10

        gateway_change_request_model = {}  # GatewayChangeRequestGatewayClientGatewayCreate
        gateway_change_request_model['type'] = 'create_gateway'

        gateway_macsec_status_reason_model = {}  # GatewayMacsecStatusReason
        gateway_macsec_status_reason_model['code'] = 'macsec_cak_failed'
        gateway_macsec_status_reason_model['message'] = 'The `authentication_key` failed configuration.'
        gateway_macsec_status_reason_model['more_info'] = 'https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK'

        gateway_macsec_reference_model = {}  # GatewayMacsecReference
        gateway_macsec_reference_model['active'] = True
        gateway_macsec_reference_model['security_policy'] = 'must_secure'
        gateway_macsec_reference_model['status'] = 'secured'
        gateway_macsec_reference_model['status_reasons'] = [gateway_macsec_status_reason_model]

        gateway_status_reason_model = {}  # GatewayStatusReason
        gateway_status_reason_model['code'] = 'authentication_key_failed'
        gateway_status_reason_model['message'] = 'The `authentication_key` failed configuration.'
        gateway_status_reason_model['more_info'] = 'https://cloud.ibm.com/docs/dl/TODO_ADD_DOCS_LINK'

        gateway_port_reference_model = {}  # GatewayPortReference
        gateway_port_reference_model['id'] = '54321b1a-fee4-41c7-9e11-9cd99e000aaa'

        resource_group_reference_model = {}  # ResourceGroupReference
        resource_group_reference_model['id'] = '56969d6043e9465c883cb9f7363e78e8'

        # Construct a json representation of a GetGatewayResponseGateway model
        get_gateway_response_gateway_model_json = {}
        get_gateway_response_gateway_model_json['as_prepends'] = [as_prepend_model]
        get_gateway_response_gateway_model_json['authentication_key'] = authentication_key_reference_model
        get_gateway_response_gateway_model_json['bfd_config'] = gateway_bfd_config_model
        get_gateway_response_gateway_model_json['bgp_asn'] = 64999
        get_gateway_response_gateway_model_json['bgp_base_cidr'] = 'testString'
        get_gateway_response_gateway_model_json['bgp_cer_cidr'] = '10.254.30.78/30'
        get_gateway_response_gateway_model_json['bgp_ibm_asn'] = 13884
        get_gateway_response_gateway_model_json['bgp_ibm_cidr'] = '10.254.30.77/30'
        get_gateway_response_gateway_model_json['bgp_status'] = 'active'
        get_gateway_response_gateway_model_json['bgp_status_updated_at'] = '2020-08-20T06:58:41.909000Z'
        get_gateway_response_gateway_model_json['carrier_name'] = 'myCarrierName'
        get_gateway_response_gateway_model_json['change_request'] = gateway_change_request_model
        get_gateway_response_gateway_model_json['completion_notice_reject_reason'] = 'The completion notice file was blank'
        get_gateway_response_gateway_model_json['connection_mode'] = 'transit'
        get_gateway_response_gateway_model_json['created_at'] = '2019-01-01T12:00:00Z'
        get_gateway_response_gateway_model_json['crn'] = 'crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::dedicated:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        get_gateway_response_gateway_model_json['cross_account'] = False
        get_gateway_response_gateway_model_json['cross_connect_router'] = 'xcr01.dal03'
        get_gateway_response_gateway_model_json['customer_name'] = 'newCustomerName'
        get_gateway_response_gateway_model_json['default_export_route_filter'] = 'permit'
        get_gateway_response_gateway_model_json['default_import_route_filter'] = 'permit'
        get_gateway_response_gateway_model_json['global'] = True
        get_gateway_response_gateway_model_json['id'] = 'ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        get_gateway_response_gateway_model_json['link_status'] = 'up'
        get_gateway_response_gateway_model_json['link_status_updated_at'] = '2020-08-20T06:58:41.909000Z'
        get_gateway_response_gateway_model_json['location_display_name'] = 'Dallas 03'
        get_gateway_response_gateway_model_json['location_name'] = 'dal03'
        get_gateway_response_gateway_model_json['macsec'] = gateway_macsec_reference_model
        get_gateway_response_gateway_model_json['macsec_capability'] = 'non_macsec'
        get_gateway_response_gateway_model_json['metered'] = False
        get_gateway_response_gateway_model_json['name'] = 'myGateway'
        get_gateway_response_gateway_model_json['operational_status'] = 'awaiting_completion_notice'
        get_gateway_response_gateway_model_json['operational_status_reasons'] = [gateway_status_reason_model]
        get_gateway_response_gateway_model_json['patch_panel_completion_notice'] = 'patch panel configuration details'
        get_gateway_response_gateway_model_json['port'] = gateway_port_reference_model
        get_gateway_response_gateway_model_json['provider_api_managed'] = False
        get_gateway_response_gateway_model_json['resource_group'] = resource_group_reference_model
        get_gateway_response_gateway_model_json['speed_mbps'] = 1000
        get_gateway_response_gateway_model_json['type'] = 'dedicated'
        get_gateway_response_gateway_model_json['vlan'] = 10

        # Construct a model instance of GetGatewayResponseGateway by calling from_dict on the json representation
        get_gateway_response_gateway_model = GetGatewayResponseGateway.from_dict(get_gateway_response_gateway_model_json)
        assert get_gateway_response_gateway_model != False

        # Construct a model instance of GetGatewayResponseGateway by calling from_dict on the json representation
        get_gateway_response_gateway_model_dict = GetGatewayResponseGateway.from_dict(get_gateway_response_gateway_model_json).__dict__
        get_gateway_response_gateway_model2 = GetGatewayResponseGateway(**get_gateway_response_gateway_model_dict)

        # Verify the model instances are equivalent
        assert get_gateway_response_gateway_model == get_gateway_response_gateway_model2

        # Convert model instance back to dict and verify no loss of data
        get_gateway_response_gateway_model_json2 = get_gateway_response_gateway_model.to_dict()
        assert get_gateway_response_gateway_model_json2 == get_gateway_response_gateway_model_json


class TestModel_RouteReportOverlappingRouteForConnection:
    """
    Test Class for RouteReportOverlappingRouteForConnection
    """

    def test_route_report_overlapping_route_for_connection_serialization(self):
        """
        Test serialization/deserialization for RouteReportOverlappingRouteForConnection
        """

        # Construct a json representation of a RouteReportOverlappingRouteForConnection model
        route_report_overlapping_route_for_connection_model_json = {}
        route_report_overlapping_route_for_connection_model_json['prefix'] = '172.17.0.0/16'
        route_report_overlapping_route_for_connection_model_json['type'] = 'virtual_connection'
        route_report_overlapping_route_for_connection_model_json['virtual_connection_id'] = 'd2d985d8-1d8e-4e8b-96cd-cee2290ecaff'

        # Construct a model instance of RouteReportOverlappingRouteForConnection by calling from_dict on the json representation
        route_report_overlapping_route_for_connection_model = RouteReportOverlappingRouteForConnection.from_dict(route_report_overlapping_route_for_connection_model_json)
        assert route_report_overlapping_route_for_connection_model != False

        # Construct a model instance of RouteReportOverlappingRouteForConnection by calling from_dict on the json representation
        route_report_overlapping_route_for_connection_model_dict = RouteReportOverlappingRouteForConnection.from_dict(route_report_overlapping_route_for_connection_model_json).__dict__
        route_report_overlapping_route_for_connection_model2 = RouteReportOverlappingRouteForConnection(**route_report_overlapping_route_for_connection_model_dict)

        # Verify the model instances are equivalent
        assert route_report_overlapping_route_for_connection_model == route_report_overlapping_route_for_connection_model2

        # Convert model instance back to dict and verify no loss of data
        route_report_overlapping_route_for_connection_model_json2 = route_report_overlapping_route_for_connection_model.to_dict()
        assert route_report_overlapping_route_for_connection_model_json2 == route_report_overlapping_route_for_connection_model_json


class TestModel_RouteReportOverlappingRouteForOthers:
    """
    Test Class for RouteReportOverlappingRouteForOthers
    """

    def test_route_report_overlapping_route_for_others_serialization(self):
        """
        Test serialization/deserialization for RouteReportOverlappingRouteForOthers
        """

        # Construct a json representation of a RouteReportOverlappingRouteForOthers model
        route_report_overlapping_route_for_others_model_json = {}
        route_report_overlapping_route_for_others_model_json['prefix'] = '172.17.0.0/16'
        route_report_overlapping_route_for_others_model_json['type'] = 'gateway'

        # Construct a model instance of RouteReportOverlappingRouteForOthers by calling from_dict on the json representation
        route_report_overlapping_route_for_others_model = RouteReportOverlappingRouteForOthers.from_dict(route_report_overlapping_route_for_others_model_json)
        assert route_report_overlapping_route_for_others_model != False

        # Construct a model instance of RouteReportOverlappingRouteForOthers by calling from_dict on the json representation
        route_report_overlapping_route_for_others_model_dict = RouteReportOverlappingRouteForOthers.from_dict(route_report_overlapping_route_for_others_model_json).__dict__
        route_report_overlapping_route_for_others_model2 = RouteReportOverlappingRouteForOthers(**route_report_overlapping_route_for_others_model_dict)

        # Verify the model instances are equivalent
        assert route_report_overlapping_route_for_others_model == route_report_overlapping_route_for_others_model2

        # Convert model instance back to dict and verify no loss of data
        route_report_overlapping_route_for_others_model_json2 = route_report_overlapping_route_for_others_model.to_dict()
        assert route_report_overlapping_route_for_others_model_json2 == route_report_overlapping_route_for_others_model_json


class TestModel_SakRekeyPacketNumberRolloverMode:
    """
    Test Class for SakRekeyPacketNumberRolloverMode
    """

    def test_sak_rekey_packet_number_rollover_mode_serialization(self):
        """
        Test serialization/deserialization for SakRekeyPacketNumberRolloverMode
        """

        # Construct a json representation of a SakRekeyPacketNumberRolloverMode model
        sak_rekey_packet_number_rollover_mode_model_json = {}
        sak_rekey_packet_number_rollover_mode_model_json['mode'] = 'packet_number_rollover'

        # Construct a model instance of SakRekeyPacketNumberRolloverMode by calling from_dict on the json representation
        sak_rekey_packet_number_rollover_mode_model = SakRekeyPacketNumberRolloverMode.from_dict(sak_rekey_packet_number_rollover_mode_model_json)
        assert sak_rekey_packet_number_rollover_mode_model != False

        # Construct a model instance of SakRekeyPacketNumberRolloverMode by calling from_dict on the json representation
        sak_rekey_packet_number_rollover_mode_model_dict = SakRekeyPacketNumberRolloverMode.from_dict(sak_rekey_packet_number_rollover_mode_model_json).__dict__
        sak_rekey_packet_number_rollover_mode_model2 = SakRekeyPacketNumberRolloverMode(**sak_rekey_packet_number_rollover_mode_model_dict)

        # Verify the model instances are equivalent
        assert sak_rekey_packet_number_rollover_mode_model == sak_rekey_packet_number_rollover_mode_model2

        # Convert model instance back to dict and verify no loss of data
        sak_rekey_packet_number_rollover_mode_model_json2 = sak_rekey_packet_number_rollover_mode_model.to_dict()
        assert sak_rekey_packet_number_rollover_mode_model_json2 == sak_rekey_packet_number_rollover_mode_model_json


class TestModel_SakRekeyPatchSakRekeyPacketNumberRolloverModePatch:
    """
    Test Class for SakRekeyPatchSakRekeyPacketNumberRolloverModePatch
    """

    def test_sak_rekey_patch_sak_rekey_packet_number_rollover_mode_patch_serialization(self):
        """
        Test serialization/deserialization for SakRekeyPatchSakRekeyPacketNumberRolloverModePatch
        """

        # Construct a json representation of a SakRekeyPatchSakRekeyPacketNumberRolloverModePatch model
        sak_rekey_patch_sak_rekey_packet_number_rollover_mode_patch_model_json = {}
        sak_rekey_patch_sak_rekey_packet_number_rollover_mode_patch_model_json['mode'] = 'packet_number_rollover'

        # Construct a model instance of SakRekeyPatchSakRekeyPacketNumberRolloverModePatch by calling from_dict on the json representation
        sak_rekey_patch_sak_rekey_packet_number_rollover_mode_patch_model = SakRekeyPatchSakRekeyPacketNumberRolloverModePatch.from_dict(sak_rekey_patch_sak_rekey_packet_number_rollover_mode_patch_model_json)
        assert sak_rekey_patch_sak_rekey_packet_number_rollover_mode_patch_model != False

        # Construct a model instance of SakRekeyPatchSakRekeyPacketNumberRolloverModePatch by calling from_dict on the json representation
        sak_rekey_patch_sak_rekey_packet_number_rollover_mode_patch_model_dict = SakRekeyPatchSakRekeyPacketNumberRolloverModePatch.from_dict(sak_rekey_patch_sak_rekey_packet_number_rollover_mode_patch_model_json).__dict__
        sak_rekey_patch_sak_rekey_packet_number_rollover_mode_patch_model2 = SakRekeyPatchSakRekeyPacketNumberRolloverModePatch(**sak_rekey_patch_sak_rekey_packet_number_rollover_mode_patch_model_dict)

        # Verify the model instances are equivalent
        assert sak_rekey_patch_sak_rekey_packet_number_rollover_mode_patch_model == sak_rekey_patch_sak_rekey_packet_number_rollover_mode_patch_model2

        # Convert model instance back to dict and verify no loss of data
        sak_rekey_patch_sak_rekey_packet_number_rollover_mode_patch_model_json2 = sak_rekey_patch_sak_rekey_packet_number_rollover_mode_patch_model.to_dict()
        assert sak_rekey_patch_sak_rekey_packet_number_rollover_mode_patch_model_json2 == sak_rekey_patch_sak_rekey_packet_number_rollover_mode_patch_model_json


class TestModel_SakRekeyPatchSakRekeyTimerModePatch:
    """
    Test Class for SakRekeyPatchSakRekeyTimerModePatch
    """

    def test_sak_rekey_patch_sak_rekey_timer_mode_patch_serialization(self):
        """
        Test serialization/deserialization for SakRekeyPatchSakRekeyTimerModePatch
        """

        # Construct a json representation of a SakRekeyPatchSakRekeyTimerModePatch model
        sak_rekey_patch_sak_rekey_timer_mode_patch_model_json = {}
        sak_rekey_patch_sak_rekey_timer_mode_patch_model_json['interval'] = 3600
        sak_rekey_patch_sak_rekey_timer_mode_patch_model_json['mode'] = 'timer'

        # Construct a model instance of SakRekeyPatchSakRekeyTimerModePatch by calling from_dict on the json representation
        sak_rekey_patch_sak_rekey_timer_mode_patch_model = SakRekeyPatchSakRekeyTimerModePatch.from_dict(sak_rekey_patch_sak_rekey_timer_mode_patch_model_json)
        assert sak_rekey_patch_sak_rekey_timer_mode_patch_model != False

        # Construct a model instance of SakRekeyPatchSakRekeyTimerModePatch by calling from_dict on the json representation
        sak_rekey_patch_sak_rekey_timer_mode_patch_model_dict = SakRekeyPatchSakRekeyTimerModePatch.from_dict(sak_rekey_patch_sak_rekey_timer_mode_patch_model_json).__dict__
        sak_rekey_patch_sak_rekey_timer_mode_patch_model2 = SakRekeyPatchSakRekeyTimerModePatch(**sak_rekey_patch_sak_rekey_timer_mode_patch_model_dict)

        # Verify the model instances are equivalent
        assert sak_rekey_patch_sak_rekey_timer_mode_patch_model == sak_rekey_patch_sak_rekey_timer_mode_patch_model2

        # Convert model instance back to dict and verify no loss of data
        sak_rekey_patch_sak_rekey_timer_mode_patch_model_json2 = sak_rekey_patch_sak_rekey_timer_mode_patch_model.to_dict()
        assert sak_rekey_patch_sak_rekey_timer_mode_patch_model_json2 == sak_rekey_patch_sak_rekey_timer_mode_patch_model_json


class TestModel_SakRekeyPrototypeSakRekeyPacketNumberRolloverModePrototype:
    """
    Test Class for SakRekeyPrototypeSakRekeyPacketNumberRolloverModePrototype
    """

    def test_sak_rekey_prototype_sak_rekey_packet_number_rollover_mode_prototype_serialization(self):
        """
        Test serialization/deserialization for SakRekeyPrototypeSakRekeyPacketNumberRolloverModePrototype
        """

        # Construct a json representation of a SakRekeyPrototypeSakRekeyPacketNumberRolloverModePrototype model
        sak_rekey_prototype_sak_rekey_packet_number_rollover_mode_prototype_model_json = {}
        sak_rekey_prototype_sak_rekey_packet_number_rollover_mode_prototype_model_json['mode'] = 'packet_number_rollover'

        # Construct a model instance of SakRekeyPrototypeSakRekeyPacketNumberRolloverModePrototype by calling from_dict on the json representation
        sak_rekey_prototype_sak_rekey_packet_number_rollover_mode_prototype_model = SakRekeyPrototypeSakRekeyPacketNumberRolloverModePrototype.from_dict(sak_rekey_prototype_sak_rekey_packet_number_rollover_mode_prototype_model_json)
        assert sak_rekey_prototype_sak_rekey_packet_number_rollover_mode_prototype_model != False

        # Construct a model instance of SakRekeyPrototypeSakRekeyPacketNumberRolloverModePrototype by calling from_dict on the json representation
        sak_rekey_prototype_sak_rekey_packet_number_rollover_mode_prototype_model_dict = SakRekeyPrototypeSakRekeyPacketNumberRolloverModePrototype.from_dict(sak_rekey_prototype_sak_rekey_packet_number_rollover_mode_prototype_model_json).__dict__
        sak_rekey_prototype_sak_rekey_packet_number_rollover_mode_prototype_model2 = SakRekeyPrototypeSakRekeyPacketNumberRolloverModePrototype(**sak_rekey_prototype_sak_rekey_packet_number_rollover_mode_prototype_model_dict)

        # Verify the model instances are equivalent
        assert sak_rekey_prototype_sak_rekey_packet_number_rollover_mode_prototype_model == sak_rekey_prototype_sak_rekey_packet_number_rollover_mode_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        sak_rekey_prototype_sak_rekey_packet_number_rollover_mode_prototype_model_json2 = sak_rekey_prototype_sak_rekey_packet_number_rollover_mode_prototype_model.to_dict()
        assert sak_rekey_prototype_sak_rekey_packet_number_rollover_mode_prototype_model_json2 == sak_rekey_prototype_sak_rekey_packet_number_rollover_mode_prototype_model_json


class TestModel_SakRekeyPrototypeSakRekeyTimerModePrototype:
    """
    Test Class for SakRekeyPrototypeSakRekeyTimerModePrototype
    """

    def test_sak_rekey_prototype_sak_rekey_timer_mode_prototype_serialization(self):
        """
        Test serialization/deserialization for SakRekeyPrototypeSakRekeyTimerModePrototype
        """

        # Construct a json representation of a SakRekeyPrototypeSakRekeyTimerModePrototype model
        sak_rekey_prototype_sak_rekey_timer_mode_prototype_model_json = {}
        sak_rekey_prototype_sak_rekey_timer_mode_prototype_model_json['interval'] = 3600
        sak_rekey_prototype_sak_rekey_timer_mode_prototype_model_json['mode'] = 'timer'

        # Construct a model instance of SakRekeyPrototypeSakRekeyTimerModePrototype by calling from_dict on the json representation
        sak_rekey_prototype_sak_rekey_timer_mode_prototype_model = SakRekeyPrototypeSakRekeyTimerModePrototype.from_dict(sak_rekey_prototype_sak_rekey_timer_mode_prototype_model_json)
        assert sak_rekey_prototype_sak_rekey_timer_mode_prototype_model != False

        # Construct a model instance of SakRekeyPrototypeSakRekeyTimerModePrototype by calling from_dict on the json representation
        sak_rekey_prototype_sak_rekey_timer_mode_prototype_model_dict = SakRekeyPrototypeSakRekeyTimerModePrototype.from_dict(sak_rekey_prototype_sak_rekey_timer_mode_prototype_model_json).__dict__
        sak_rekey_prototype_sak_rekey_timer_mode_prototype_model2 = SakRekeyPrototypeSakRekeyTimerModePrototype(**sak_rekey_prototype_sak_rekey_timer_mode_prototype_model_dict)

        # Verify the model instances are equivalent
        assert sak_rekey_prototype_sak_rekey_timer_mode_prototype_model == sak_rekey_prototype_sak_rekey_timer_mode_prototype_model2

        # Convert model instance back to dict and verify no loss of data
        sak_rekey_prototype_sak_rekey_timer_mode_prototype_model_json2 = sak_rekey_prototype_sak_rekey_timer_mode_prototype_model.to_dict()
        assert sak_rekey_prototype_sak_rekey_timer_mode_prototype_model_json2 == sak_rekey_prototype_sak_rekey_timer_mode_prototype_model_json


class TestModel_SakRekeyTimerMode:
    """
    Test Class for SakRekeyTimerMode
    """

    def test_sak_rekey_timer_mode_serialization(self):
        """
        Test serialization/deserialization for SakRekeyTimerMode
        """

        # Construct a json representation of a SakRekeyTimerMode model
        sak_rekey_timer_mode_model_json = {}
        sak_rekey_timer_mode_model_json['interval'] = 3600
        sak_rekey_timer_mode_model_json['mode'] = 'timer'

        # Construct a model instance of SakRekeyTimerMode by calling from_dict on the json representation
        sak_rekey_timer_mode_model = SakRekeyTimerMode.from_dict(sak_rekey_timer_mode_model_json)
        assert sak_rekey_timer_mode_model != False

        # Construct a model instance of SakRekeyTimerMode by calling from_dict on the json representation
        sak_rekey_timer_mode_model_dict = SakRekeyTimerMode.from_dict(sak_rekey_timer_mode_model_json).__dict__
        sak_rekey_timer_mode_model2 = SakRekeyTimerMode(**sak_rekey_timer_mode_model_dict)

        # Verify the model instances are equivalent
        assert sak_rekey_timer_mode_model == sak_rekey_timer_mode_model2

        # Convert model instance back to dict and verify no loss of data
        sak_rekey_timer_mode_model_json2 = sak_rekey_timer_mode_model.to_dict()
        assert sak_rekey_timer_mode_model_json2 == sak_rekey_timer_mode_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################