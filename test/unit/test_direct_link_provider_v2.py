# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2021.
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
Unit Tests for DirectLinkProviderV2
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
from ibm_cloud_networking_services.direct_link_provider_v2 import *

version = 'testString'

_service = DirectLinkProviderV2(
    authenticator=NoAuthAuthenticator(),
    version=version
)

_base_url = 'https://directlink.cloud.ibm.com/provider/v2'
_service.set_service_url(_base_url)

##############################################################################
# Start of Service: ProviderAPIs
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

        service = DirectLinkProviderV2.new_instance(
            version=version,
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, DirectLinkProviderV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = DirectLinkProviderV2.new_instance(
                version=version,
            )

    def test_new_instance_without_required_params(self):
        """
        new_instance_without_required_params()
        """
        with pytest.raises(TypeError, match='new_instance\\(\\) missing \\d required positional arguments?: \'.*\''):
            service = DirectLinkProviderV2.new_instance()

    def test_new_instance_required_param_none(self):
        """
        new_instance_required_param_none()
        """
        with pytest.raises(ValueError, match='version must be provided'):
            service = DirectLinkProviderV2.new_instance(
                version=None,
            )
class TestListProviderGateways():
    """
    Test Class for list_provider_gateways
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_provider_gateways_all_params(self):
        """
        list_provider_gateways()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/gateways')
        mock_response = '{"first": {"href": "https://directlink.cloud.ibm.com/provider/v2/gateways?limit=100"}, "limit": 100, "next": {"href": "https://directlink.cloud.ibm.com/provider/v2/gateways?start=8c4a91a3e2cbd233b5a5b33436855fc2&limit=100", "start": "8c4a91a3e2cbd233b5a5b33436855fc2"}, "total_count": 132, "gateways": [{"bgp_asn": 64999, "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "change_request": {"type": "create_gateway"}, "created_at": "2019-01-01T12:00:00.000Z", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::connect:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "customer_account_id": "4111d05f36894e3cb9b46a43556d9000", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "myGateway", "operational_status": "configuring", "port": {"id": "fffdcb1a-fee4-41c7-9e11-9cd99e65c777"}, "provider_api_managed": true, "speed_mbps": 1000, "type": "connect", "vlan": 10}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        start = 'testString'
        limit = 1

        # Invoke method
        response = _service.list_provider_gateways(
            start=start,
            limit=limit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'start={}'.format(start) in query_string
        assert 'limit={}'.format(limit) in query_string

    def test_list_provider_gateways_all_params_with_retries(self):
        # Enable retries and run test_list_provider_gateways_all_params.
        _service.enable_retries()
        self.test_list_provider_gateways_all_params()

        # Disable retries and run test_list_provider_gateways_all_params.
        _service.disable_retries()
        self.test_list_provider_gateways_all_params()

    @responses.activate
    def test_list_provider_gateways_required_params(self):
        """
        test_list_provider_gateways_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/gateways')
        mock_response = '{"first": {"href": "https://directlink.cloud.ibm.com/provider/v2/gateways?limit=100"}, "limit": 100, "next": {"href": "https://directlink.cloud.ibm.com/provider/v2/gateways?start=8c4a91a3e2cbd233b5a5b33436855fc2&limit=100", "start": "8c4a91a3e2cbd233b5a5b33436855fc2"}, "total_count": 132, "gateways": [{"bgp_asn": 64999, "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "change_request": {"type": "create_gateway"}, "created_at": "2019-01-01T12:00:00.000Z", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::connect:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "customer_account_id": "4111d05f36894e3cb9b46a43556d9000", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "myGateway", "operational_status": "configuring", "port": {"id": "fffdcb1a-fee4-41c7-9e11-9cd99e65c777"}, "provider_api_managed": true, "speed_mbps": 1000, "type": "connect", "vlan": 10}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_provider_gateways()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_provider_gateways_required_params_with_retries(self):
        # Enable retries and run test_list_provider_gateways_required_params.
        _service.enable_retries()
        self.test_list_provider_gateways_required_params()

        # Disable retries and run test_list_provider_gateways_required_params.
        _service.disable_retries()
        self.test_list_provider_gateways_required_params()

    @responses.activate
    def test_list_provider_gateways_value_error(self):
        """
        test_list_provider_gateways_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/gateways')
        mock_response = '{"first": {"href": "https://directlink.cloud.ibm.com/provider/v2/gateways?limit=100"}, "limit": 100, "next": {"href": "https://directlink.cloud.ibm.com/provider/v2/gateways?start=8c4a91a3e2cbd233b5a5b33436855fc2&limit=100", "start": "8c4a91a3e2cbd233b5a5b33436855fc2"}, "total_count": 132, "gateways": [{"bgp_asn": 64999, "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "change_request": {"type": "create_gateway"}, "created_at": "2019-01-01T12:00:00.000Z", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::connect:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "customer_account_id": "4111d05f36894e3cb9b46a43556d9000", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "myGateway", "operational_status": "configuring", "port": {"id": "fffdcb1a-fee4-41c7-9e11-9cd99e65c777"}, "provider_api_managed": true, "speed_mbps": 1000, "type": "connect", "vlan": 10}]}'
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
                _service.list_provider_gateways(**req_copy)


    def test_list_provider_gateways_value_error_with_retries(self):
        # Enable retries and run test_list_provider_gateways_value_error.
        _service.enable_retries()
        self.test_list_provider_gateways_value_error()

        # Disable retries and run test_list_provider_gateways_value_error.
        _service.disable_retries()
        self.test_list_provider_gateways_value_error()

class TestCreateProviderGateway():
    """
    Test Class for create_provider_gateway
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_provider_gateway_all_params(self):
        """
        create_provider_gateway()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/gateways')
        mock_response = '{"bgp_asn": 64999, "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "change_request": {"type": "create_gateway"}, "created_at": "2019-01-01T12:00:00.000Z", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::connect:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "customer_account_id": "4111d05f36894e3cb9b46a43556d9000", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "myGateway", "operational_status": "configuring", "port": {"id": "fffdcb1a-fee4-41c7-9e11-9cd99e65c777"}, "provider_api_managed": true, "speed_mbps": 1000, "type": "connect", "vlan": 10}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a ProviderGatewayPortIdentity model
        provider_gateway_port_identity_model = {}
        provider_gateway_port_identity_model['id'] = 'fffdcb1a-fee4-41c7-9e11-9cd99e65c777'

        # Set up parameter values
        bgp_asn = 64999
        customer_account_id = '4111d05f36894e3cb9b46a43556d9000'
        name = 'myGateway'
        port = provider_gateway_port_identity_model
        speed_mbps = 1000
        bgp_cer_cidr = '10.254.30.78/30'
        bgp_ibm_cidr = '10.254.30.77/30'
        vlan = 10
        check_only = 'testString'

        # Invoke method
        response = _service.create_provider_gateway(
            bgp_asn,
            customer_account_id,
            name,
            port,
            speed_mbps,
            bgp_cer_cidr=bgp_cer_cidr,
            bgp_ibm_cidr=bgp_ibm_cidr,
            vlan=vlan,
            check_only=check_only,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'check_only={}'.format(check_only) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['bgp_asn'] == 64999
        assert req_body['customer_account_id'] == '4111d05f36894e3cb9b46a43556d9000'
        assert req_body['name'] == 'myGateway'
        assert req_body['port'] == provider_gateway_port_identity_model
        assert req_body['speed_mbps'] == 1000
        assert req_body['bgp_cer_cidr'] == '10.254.30.78/30'
        assert req_body['bgp_ibm_cidr'] == '10.254.30.77/30'
        assert req_body['vlan'] == 10

    def test_create_provider_gateway_all_params_with_retries(self):
        # Enable retries and run test_create_provider_gateway_all_params.
        _service.enable_retries()
        self.test_create_provider_gateway_all_params()

        # Disable retries and run test_create_provider_gateway_all_params.
        _service.disable_retries()
        self.test_create_provider_gateway_all_params()

    @responses.activate
    def test_create_provider_gateway_required_params(self):
        """
        test_create_provider_gateway_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/gateways')
        mock_response = '{"bgp_asn": 64999, "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "change_request": {"type": "create_gateway"}, "created_at": "2019-01-01T12:00:00.000Z", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::connect:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "customer_account_id": "4111d05f36894e3cb9b46a43556d9000", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "myGateway", "operational_status": "configuring", "port": {"id": "fffdcb1a-fee4-41c7-9e11-9cd99e65c777"}, "provider_api_managed": true, "speed_mbps": 1000, "type": "connect", "vlan": 10}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a ProviderGatewayPortIdentity model
        provider_gateway_port_identity_model = {}
        provider_gateway_port_identity_model['id'] = 'fffdcb1a-fee4-41c7-9e11-9cd99e65c777'

        # Set up parameter values
        bgp_asn = 64999
        customer_account_id = '4111d05f36894e3cb9b46a43556d9000'
        name = 'myGateway'
        port = provider_gateway_port_identity_model
        speed_mbps = 1000
        bgp_cer_cidr = '10.254.30.78/30'
        bgp_ibm_cidr = '10.254.30.77/30'
        vlan = 10

        # Invoke method
        response = _service.create_provider_gateway(
            bgp_asn,
            customer_account_id,
            name,
            port,
            speed_mbps,
            bgp_cer_cidr=bgp_cer_cidr,
            bgp_ibm_cidr=bgp_ibm_cidr,
            vlan=vlan,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['bgp_asn'] == 64999
        assert req_body['customer_account_id'] == '4111d05f36894e3cb9b46a43556d9000'
        assert req_body['name'] == 'myGateway'
        assert req_body['port'] == provider_gateway_port_identity_model
        assert req_body['speed_mbps'] == 1000
        assert req_body['bgp_cer_cidr'] == '10.254.30.78/30'
        assert req_body['bgp_ibm_cidr'] == '10.254.30.77/30'
        assert req_body['vlan'] == 10

    def test_create_provider_gateway_required_params_with_retries(self):
        # Enable retries and run test_create_provider_gateway_required_params.
        _service.enable_retries()
        self.test_create_provider_gateway_required_params()

        # Disable retries and run test_create_provider_gateway_required_params.
        _service.disable_retries()
        self.test_create_provider_gateway_required_params()

    @responses.activate
    def test_create_provider_gateway_value_error(self):
        """
        test_create_provider_gateway_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/gateways')
        mock_response = '{"bgp_asn": 64999, "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "change_request": {"type": "create_gateway"}, "created_at": "2019-01-01T12:00:00.000Z", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::connect:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "customer_account_id": "4111d05f36894e3cb9b46a43556d9000", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "myGateway", "operational_status": "configuring", "port": {"id": "fffdcb1a-fee4-41c7-9e11-9cd99e65c777"}, "provider_api_managed": true, "speed_mbps": 1000, "type": "connect", "vlan": 10}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a ProviderGatewayPortIdentity model
        provider_gateway_port_identity_model = {}
        provider_gateway_port_identity_model['id'] = 'fffdcb1a-fee4-41c7-9e11-9cd99e65c777'

        # Set up parameter values
        bgp_asn = 64999
        customer_account_id = '4111d05f36894e3cb9b46a43556d9000'
        name = 'myGateway'
        port = provider_gateway_port_identity_model
        speed_mbps = 1000
        bgp_cer_cidr = '10.254.30.78/30'
        bgp_ibm_cidr = '10.254.30.77/30'
        vlan = 10

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "bgp_asn": bgp_asn,
            "customer_account_id": customer_account_id,
            "name": name,
            "port": port,
            "speed_mbps": speed_mbps,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_provider_gateway(**req_copy)


    def test_create_provider_gateway_value_error_with_retries(self):
        # Enable retries and run test_create_provider_gateway_value_error.
        _service.enable_retries()
        self.test_create_provider_gateway_value_error()

        # Disable retries and run test_create_provider_gateway_value_error.
        _service.disable_retries()
        self.test_create_provider_gateway_value_error()

class TestDeleteProviderGateway():
    """
    Test Class for delete_provider_gateway
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_provider_gateway_all_params(self):
        """
        delete_provider_gateway()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/gateways/testString')
        mock_response = '{"bgp_asn": 64999, "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "change_request": {"type": "create_gateway"}, "created_at": "2019-01-01T12:00:00.000Z", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::connect:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "customer_account_id": "4111d05f36894e3cb9b46a43556d9000", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "myGateway", "operational_status": "configuring", "port": {"id": "fffdcb1a-fee4-41c7-9e11-9cd99e65c777"}, "provider_api_managed": true, "speed_mbps": 1000, "type": "connect", "vlan": 10}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.delete_provider_gateway(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_provider_gateway_all_params_with_retries(self):
        # Enable retries and run test_delete_provider_gateway_all_params.
        _service.enable_retries()
        self.test_delete_provider_gateway_all_params()

        # Disable retries and run test_delete_provider_gateway_all_params.
        _service.disable_retries()
        self.test_delete_provider_gateway_all_params()

    @responses.activate
    def test_delete_provider_gateway_value_error(self):
        """
        test_delete_provider_gateway_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/gateways/testString')
        mock_response = '{"bgp_asn": 64999, "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "change_request": {"type": "create_gateway"}, "created_at": "2019-01-01T12:00:00.000Z", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::connect:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "customer_account_id": "4111d05f36894e3cb9b46a43556d9000", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "myGateway", "operational_status": "configuring", "port": {"id": "fffdcb1a-fee4-41c7-9e11-9cd99e65c777"}, "provider_api_managed": true, "speed_mbps": 1000, "type": "connect", "vlan": 10}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_provider_gateway(**req_copy)


    def test_delete_provider_gateway_value_error_with_retries(self):
        # Enable retries and run test_delete_provider_gateway_value_error.
        _service.enable_retries()
        self.test_delete_provider_gateway_value_error()

        # Disable retries and run test_delete_provider_gateway_value_error.
        _service.disable_retries()
        self.test_delete_provider_gateway_value_error()

class TestGetProviderGateway():
    """
    Test Class for get_provider_gateway
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_provider_gateway_all_params(self):
        """
        get_provider_gateway()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/gateways/testString')
        mock_response = '{"bgp_asn": 64999, "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "change_request": {"type": "create_gateway"}, "created_at": "2019-01-01T12:00:00.000Z", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::connect:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "customer_account_id": "4111d05f36894e3cb9b46a43556d9000", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "myGateway", "operational_status": "configuring", "port": {"id": "fffdcb1a-fee4-41c7-9e11-9cd99e65c777"}, "provider_api_managed": true, "speed_mbps": 1000, "type": "connect", "vlan": 10}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.get_provider_gateway(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_provider_gateway_all_params_with_retries(self):
        # Enable retries and run test_get_provider_gateway_all_params.
        _service.enable_retries()
        self.test_get_provider_gateway_all_params()

        # Disable retries and run test_get_provider_gateway_all_params.
        _service.disable_retries()
        self.test_get_provider_gateway_all_params()

    @responses.activate
    def test_get_provider_gateway_value_error(self):
        """
        test_get_provider_gateway_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/gateways/testString')
        mock_response = '{"bgp_asn": 64999, "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "change_request": {"type": "create_gateway"}, "created_at": "2019-01-01T12:00:00.000Z", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::connect:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "customer_account_id": "4111d05f36894e3cb9b46a43556d9000", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "myGateway", "operational_status": "configuring", "port": {"id": "fffdcb1a-fee4-41c7-9e11-9cd99e65c777"}, "provider_api_managed": true, "speed_mbps": 1000, "type": "connect", "vlan": 10}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_provider_gateway(**req_copy)


    def test_get_provider_gateway_value_error_with_retries(self):
        # Enable retries and run test_get_provider_gateway_value_error.
        _service.enable_retries()
        self.test_get_provider_gateway_value_error()

        # Disable retries and run test_get_provider_gateway_value_error.
        _service.disable_retries()
        self.test_get_provider_gateway_value_error()

class TestUpdateProviderGateway():
    """
    Test Class for update_provider_gateway
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_provider_gateway_all_params(self):
        """
        update_provider_gateway()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/gateways/testString')
        mock_response = '{"bgp_asn": 64999, "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "change_request": {"type": "create_gateway"}, "created_at": "2019-01-01T12:00:00.000Z", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::connect:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "customer_account_id": "4111d05f36894e3cb9b46a43556d9000", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "myGateway", "operational_status": "configuring", "port": {"id": "fffdcb1a-fee4-41c7-9e11-9cd99e65c777"}, "provider_api_managed": true, "speed_mbps": 1000, "type": "connect", "vlan": 10}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        bgp_asn = 64999
        bgp_cer_cidr = '169.254.0.10/30'
        bgp_ibm_cidr = '169.254.0.9/30'
        name = 'myNewGateway'
        speed_mbps = 1000
        vlan = 10

        # Invoke method
        response = _service.update_provider_gateway(
            id,
            bgp_asn=bgp_asn,
            bgp_cer_cidr=bgp_cer_cidr,
            bgp_ibm_cidr=bgp_ibm_cidr,
            name=name,
            speed_mbps=speed_mbps,
            vlan=vlan,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['bgp_asn'] == 64999
        assert req_body['bgp_cer_cidr'] == '169.254.0.10/30'
        assert req_body['bgp_ibm_cidr'] == '169.254.0.9/30'
        assert req_body['name'] == 'myNewGateway'
        assert req_body['speed_mbps'] == 1000
        assert req_body['vlan'] == 10

    def test_update_provider_gateway_all_params_with_retries(self):
        # Enable retries and run test_update_provider_gateway_all_params.
        _service.enable_retries()
        self.test_update_provider_gateway_all_params()

        # Disable retries and run test_update_provider_gateway_all_params.
        _service.disable_retries()
        self.test_update_provider_gateway_all_params()

    @responses.activate
    def test_update_provider_gateway_value_error(self):
        """
        test_update_provider_gateway_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/gateways/testString')
        mock_response = '{"bgp_asn": 64999, "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "change_request": {"type": "create_gateway"}, "created_at": "2019-01-01T12:00:00.000Z", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::connect:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "customer_account_id": "4111d05f36894e3cb9b46a43556d9000", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "myGateway", "operational_status": "configuring", "port": {"id": "fffdcb1a-fee4-41c7-9e11-9cd99e65c777"}, "provider_api_managed": true, "speed_mbps": 1000, "type": "connect", "vlan": 10}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        bgp_asn = 64999
        bgp_cer_cidr = '169.254.0.10/30'
        bgp_ibm_cidr = '169.254.0.9/30'
        name = 'myNewGateway'
        speed_mbps = 1000
        vlan = 10

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_provider_gateway(**req_copy)


    def test_update_provider_gateway_value_error_with_retries(self):
        # Enable retries and run test_update_provider_gateway_value_error.
        _service.enable_retries()
        self.test_update_provider_gateway_value_error()

        # Disable retries and run test_update_provider_gateway_value_error.
        _service.disable_retries()
        self.test_update_provider_gateway_value_error()

class TestListProviderPorts():
    """
    Test Class for list_provider_ports
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_provider_ports_all_params(self):
        """
        list_provider_ports()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/ports')
        mock_response = '{"first": {"href": "https://directlink.cloud.ibm.com/provider/v2/ports?limit=100"}, "limit": 100, "next": {"href": "https://directlink.cloud.ibm.com/provider/v2/ports?start=9d5a91a3e2cbd233b5a5b33436855ed1&limit=100", "start": "9d5a91a3e2cbd233b5a5b33436855ed1"}, "total_count": 132, "ports": [{"id": "01122b9b-820f-4c44-8a31-77f1f0806765", "label": "XCR-FRK-CS-SEC-01", "location_display_name": "Dallas 03", "location_name": "dal03", "provider_name": "provider_1", "supported_link_speeds": [21]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        start = 'testString'
        limit = 1

        # Invoke method
        response = _service.list_provider_ports(
            start=start,
            limit=limit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'start={}'.format(start) in query_string
        assert 'limit={}'.format(limit) in query_string

    def test_list_provider_ports_all_params_with_retries(self):
        # Enable retries and run test_list_provider_ports_all_params.
        _service.enable_retries()
        self.test_list_provider_ports_all_params()

        # Disable retries and run test_list_provider_ports_all_params.
        _service.disable_retries()
        self.test_list_provider_ports_all_params()

    @responses.activate
    def test_list_provider_ports_required_params(self):
        """
        test_list_provider_ports_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/ports')
        mock_response = '{"first": {"href": "https://directlink.cloud.ibm.com/provider/v2/ports?limit=100"}, "limit": 100, "next": {"href": "https://directlink.cloud.ibm.com/provider/v2/ports?start=9d5a91a3e2cbd233b5a5b33436855ed1&limit=100", "start": "9d5a91a3e2cbd233b5a5b33436855ed1"}, "total_count": 132, "ports": [{"id": "01122b9b-820f-4c44-8a31-77f1f0806765", "label": "XCR-FRK-CS-SEC-01", "location_display_name": "Dallas 03", "location_name": "dal03", "provider_name": "provider_1", "supported_link_speeds": [21]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_provider_ports()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_provider_ports_required_params_with_retries(self):
        # Enable retries and run test_list_provider_ports_required_params.
        _service.enable_retries()
        self.test_list_provider_ports_required_params()

        # Disable retries and run test_list_provider_ports_required_params.
        _service.disable_retries()
        self.test_list_provider_ports_required_params()

    @responses.activate
    def test_list_provider_ports_value_error(self):
        """
        test_list_provider_ports_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/ports')
        mock_response = '{"first": {"href": "https://directlink.cloud.ibm.com/provider/v2/ports?limit=100"}, "limit": 100, "next": {"href": "https://directlink.cloud.ibm.com/provider/v2/ports?start=9d5a91a3e2cbd233b5a5b33436855ed1&limit=100", "start": "9d5a91a3e2cbd233b5a5b33436855ed1"}, "total_count": 132, "ports": [{"id": "01122b9b-820f-4c44-8a31-77f1f0806765", "label": "XCR-FRK-CS-SEC-01", "location_display_name": "Dallas 03", "location_name": "dal03", "provider_name": "provider_1", "supported_link_speeds": [21]}]}'
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
                _service.list_provider_ports(**req_copy)


    def test_list_provider_ports_value_error_with_retries(self):
        # Enable retries and run test_list_provider_ports_value_error.
        _service.enable_retries()
        self.test_list_provider_ports_value_error()

        # Disable retries and run test_list_provider_ports_value_error.
        _service.disable_retries()
        self.test_list_provider_ports_value_error()

class TestGetProviderPort():
    """
    Test Class for get_provider_port
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_provider_port_all_params(self):
        """
        get_provider_port()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/ports/testString')
        mock_response = '{"id": "01122b9b-820f-4c44-8a31-77f1f0806765", "label": "XCR-FRK-CS-SEC-01", "location_display_name": "Dallas 03", "location_name": "dal03", "provider_name": "provider_1", "supported_link_speeds": [21]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.get_provider_port(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_provider_port_all_params_with_retries(self):
        # Enable retries and run test_get_provider_port_all_params.
        _service.enable_retries()
        self.test_get_provider_port_all_params()

        # Disable retries and run test_get_provider_port_all_params.
        _service.disable_retries()
        self.test_get_provider_port_all_params()

    @responses.activate
    def test_get_provider_port_value_error(self):
        """
        test_get_provider_port_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/ports/testString')
        mock_response = '{"id": "01122b9b-820f-4c44-8a31-77f1f0806765", "label": "XCR-FRK-CS-SEC-01", "location_display_name": "Dallas 03", "location_name": "dal03", "provider_name": "provider_1", "supported_link_speeds": [21]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_provider_port(**req_copy)


    def test_get_provider_port_value_error_with_retries(self):
        # Enable retries and run test_get_provider_port_value_error.
        _service.enable_retries()
        self.test_get_provider_port_value_error()

        # Disable retries and run test_get_provider_port_value_error.
        _service.disable_retries()
        self.test_get_provider_port_value_error()

# endregion
##############################################################################
# End of Service: ProviderAPIs
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_ProviderGateway():
    """
    Test Class for ProviderGateway
    """

    def test_provider_gateway_serialization(self):
        """
        Test serialization/deserialization for ProviderGateway
        """

        # Construct dict forms of any model objects needed in order to build this model.

        provider_gateway_change_request_model = {} # ProviderGatewayChangeRequestProviderGatewayCreate
        provider_gateway_change_request_model['type'] = 'create_gateway'

        provider_gateway_port_reference_model = {} # ProviderGatewayPortReference
        provider_gateway_port_reference_model['id'] = 'fffdcb1a-fee4-41c7-9e11-9cd99e65c777'

        # Construct a json representation of a ProviderGateway model
        provider_gateway_model_json = {}
        provider_gateway_model_json['bgp_asn'] = 64999
        provider_gateway_model_json['bgp_cer_cidr'] = '10.254.30.78/30'
        provider_gateway_model_json['bgp_ibm_asn'] = 13884
        provider_gateway_model_json['bgp_ibm_cidr'] = '10.254.30.77/30'
        provider_gateway_model_json['bgp_status'] = 'active'
        provider_gateway_model_json['change_request'] = provider_gateway_change_request_model
        provider_gateway_model_json['created_at'] = "2019-01-01T12:00:00Z"
        provider_gateway_model_json['crn'] = 'crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::connect:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        provider_gateway_model_json['customer_account_id'] = '4111d05f36894e3cb9b46a43556d9000'
        provider_gateway_model_json['id'] = 'ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        provider_gateway_model_json['name'] = 'myGateway'
        provider_gateway_model_json['operational_status'] = 'configuring'
        provider_gateway_model_json['port'] = provider_gateway_port_reference_model
        provider_gateway_model_json['provider_api_managed'] = True
        provider_gateway_model_json['speed_mbps'] = 1000
        provider_gateway_model_json['type'] = 'connect'
        provider_gateway_model_json['vlan'] = 10

        # Construct a model instance of ProviderGateway by calling from_dict on the json representation
        provider_gateway_model = ProviderGateway.from_dict(provider_gateway_model_json)
        assert provider_gateway_model != False

        # Construct a model instance of ProviderGateway by calling from_dict on the json representation
        provider_gateway_model_dict = ProviderGateway.from_dict(provider_gateway_model_json).__dict__
        provider_gateway_model2 = ProviderGateway(**provider_gateway_model_dict)

        # Verify the model instances are equivalent
        assert provider_gateway_model == provider_gateway_model2

        # Convert model instance back to dict and verify no loss of data
        provider_gateway_model_json2 = provider_gateway_model.to_dict()
        assert provider_gateway_model_json2 == provider_gateway_model_json

class TestModel_ProviderGatewayCollection():
    """
    Test Class for ProviderGatewayCollection
    """

    def test_provider_gateway_collection_serialization(self):
        """
        Test serialization/deserialization for ProviderGatewayCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        provider_gateway_collection_first_model = {} # ProviderGatewayCollectionFirst
        provider_gateway_collection_first_model['href'] = 'https://directlink.cloud.ibm.com/provider/v2/gateways?limit=100'

        provider_gateway_collection_next_model = {} # ProviderGatewayCollectionNext
        provider_gateway_collection_next_model['href'] = 'https://directlink.cloud.ibm.com/provider/v2/gateways?start=8c4a91a3e2cbd233b5a5b33436855fc2&limit=100'
        provider_gateway_collection_next_model['start'] = '8c4a91a3e2cbd233b5a5b33436855fc2'

        provider_gateway_change_request_model = {} # ProviderGatewayChangeRequestProviderGatewayCreate
        provider_gateway_change_request_model['type'] = 'create_gateway'

        provider_gateway_port_reference_model = {} # ProviderGatewayPortReference
        provider_gateway_port_reference_model['id'] = 'fffdcb1a-fee4-41c7-9e11-9cd99e65c777'

        provider_gateway_model = {} # ProviderGateway
        provider_gateway_model['bgp_asn'] = 64999
        provider_gateway_model['bgp_cer_cidr'] = '10.254.30.78/30'
        provider_gateway_model['bgp_ibm_asn'] = 13884
        provider_gateway_model['bgp_ibm_cidr'] = '10.254.30.77/30'
        provider_gateway_model['bgp_status'] = 'active'
        provider_gateway_model['change_request'] = provider_gateway_change_request_model
        provider_gateway_model['created_at'] = "2019-01-01T12:00:00Z"
        provider_gateway_model['crn'] = 'crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::connect:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        provider_gateway_model['customer_account_id'] = '4111d05f36894e3cb9b46a43556d9000'
        provider_gateway_model['id'] = 'ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        provider_gateway_model['name'] = 'myGateway'
        provider_gateway_model['operational_status'] = 'configuring'
        provider_gateway_model['port'] = provider_gateway_port_reference_model
        provider_gateway_model['provider_api_managed'] = True
        provider_gateway_model['speed_mbps'] = 1000
        provider_gateway_model['type'] = 'connect'
        provider_gateway_model['vlan'] = 10

        # Construct a json representation of a ProviderGatewayCollection model
        provider_gateway_collection_model_json = {}
        provider_gateway_collection_model_json['first'] = provider_gateway_collection_first_model
        provider_gateway_collection_model_json['limit'] = 100
        provider_gateway_collection_model_json['next'] = provider_gateway_collection_next_model
        provider_gateway_collection_model_json['total_count'] = 132
        provider_gateway_collection_model_json['gateways'] = [provider_gateway_model]

        # Construct a model instance of ProviderGatewayCollection by calling from_dict on the json representation
        provider_gateway_collection_model = ProviderGatewayCollection.from_dict(provider_gateway_collection_model_json)
        assert provider_gateway_collection_model != False

        # Construct a model instance of ProviderGatewayCollection by calling from_dict on the json representation
        provider_gateway_collection_model_dict = ProviderGatewayCollection.from_dict(provider_gateway_collection_model_json).__dict__
        provider_gateway_collection_model2 = ProviderGatewayCollection(**provider_gateway_collection_model_dict)

        # Verify the model instances are equivalent
        assert provider_gateway_collection_model == provider_gateway_collection_model2

        # Convert model instance back to dict and verify no loss of data
        provider_gateway_collection_model_json2 = provider_gateway_collection_model.to_dict()
        assert provider_gateway_collection_model_json2 == provider_gateway_collection_model_json

class TestModel_ProviderGatewayCollectionFirst():
    """
    Test Class for ProviderGatewayCollectionFirst
    """

    def test_provider_gateway_collection_first_serialization(self):
        """
        Test serialization/deserialization for ProviderGatewayCollectionFirst
        """

        # Construct a json representation of a ProviderGatewayCollectionFirst model
        provider_gateway_collection_first_model_json = {}
        provider_gateway_collection_first_model_json['href'] = 'https://directlink.cloud.ibm.com/provider/v2/gateways?limit=100'

        # Construct a model instance of ProviderGatewayCollectionFirst by calling from_dict on the json representation
        provider_gateway_collection_first_model = ProviderGatewayCollectionFirst.from_dict(provider_gateway_collection_first_model_json)
        assert provider_gateway_collection_first_model != False

        # Construct a model instance of ProviderGatewayCollectionFirst by calling from_dict on the json representation
        provider_gateway_collection_first_model_dict = ProviderGatewayCollectionFirst.from_dict(provider_gateway_collection_first_model_json).__dict__
        provider_gateway_collection_first_model2 = ProviderGatewayCollectionFirst(**provider_gateway_collection_first_model_dict)

        # Verify the model instances are equivalent
        assert provider_gateway_collection_first_model == provider_gateway_collection_first_model2

        # Convert model instance back to dict and verify no loss of data
        provider_gateway_collection_first_model_json2 = provider_gateway_collection_first_model.to_dict()
        assert provider_gateway_collection_first_model_json2 == provider_gateway_collection_first_model_json

class TestModel_ProviderGatewayCollectionNext():
    """
    Test Class for ProviderGatewayCollectionNext
    """

    def test_provider_gateway_collection_next_serialization(self):
        """
        Test serialization/deserialization for ProviderGatewayCollectionNext
        """

        # Construct a json representation of a ProviderGatewayCollectionNext model
        provider_gateway_collection_next_model_json = {}
        provider_gateway_collection_next_model_json['href'] = 'https://directlink.cloud.ibm.com/provider/v2/gateways?start=8c4a91a3e2cbd233b5a5b33436855fc2&limit=100'
        provider_gateway_collection_next_model_json['start'] = '8c4a91a3e2cbd233b5a5b33436855fc2'

        # Construct a model instance of ProviderGatewayCollectionNext by calling from_dict on the json representation
        provider_gateway_collection_next_model = ProviderGatewayCollectionNext.from_dict(provider_gateway_collection_next_model_json)
        assert provider_gateway_collection_next_model != False

        # Construct a model instance of ProviderGatewayCollectionNext by calling from_dict on the json representation
        provider_gateway_collection_next_model_dict = ProviderGatewayCollectionNext.from_dict(provider_gateway_collection_next_model_json).__dict__
        provider_gateway_collection_next_model2 = ProviderGatewayCollectionNext(**provider_gateway_collection_next_model_dict)

        # Verify the model instances are equivalent
        assert provider_gateway_collection_next_model == provider_gateway_collection_next_model2

        # Convert model instance back to dict and verify no loss of data
        provider_gateway_collection_next_model_json2 = provider_gateway_collection_next_model.to_dict()
        assert provider_gateway_collection_next_model_json2 == provider_gateway_collection_next_model_json

class TestModel_ProviderGatewayPortIdentity():
    """
    Test Class for ProviderGatewayPortIdentity
    """

    def test_provider_gateway_port_identity_serialization(self):
        """
        Test serialization/deserialization for ProviderGatewayPortIdentity
        """

        # Construct a json representation of a ProviderGatewayPortIdentity model
        provider_gateway_port_identity_model_json = {}
        provider_gateway_port_identity_model_json['id'] = 'fffdcb1a-fee4-41c7-9e11-9cd99e65c777'

        # Construct a model instance of ProviderGatewayPortIdentity by calling from_dict on the json representation
        provider_gateway_port_identity_model = ProviderGatewayPortIdentity.from_dict(provider_gateway_port_identity_model_json)
        assert provider_gateway_port_identity_model != False

        # Construct a model instance of ProviderGatewayPortIdentity by calling from_dict on the json representation
        provider_gateway_port_identity_model_dict = ProviderGatewayPortIdentity.from_dict(provider_gateway_port_identity_model_json).__dict__
        provider_gateway_port_identity_model2 = ProviderGatewayPortIdentity(**provider_gateway_port_identity_model_dict)

        # Verify the model instances are equivalent
        assert provider_gateway_port_identity_model == provider_gateway_port_identity_model2

        # Convert model instance back to dict and verify no loss of data
        provider_gateway_port_identity_model_json2 = provider_gateway_port_identity_model.to_dict()
        assert provider_gateway_port_identity_model_json2 == provider_gateway_port_identity_model_json

class TestModel_ProviderGatewayPortReference():
    """
    Test Class for ProviderGatewayPortReference
    """

    def test_provider_gateway_port_reference_serialization(self):
        """
        Test serialization/deserialization for ProviderGatewayPortReference
        """

        # Construct a json representation of a ProviderGatewayPortReference model
        provider_gateway_port_reference_model_json = {}
        provider_gateway_port_reference_model_json['id'] = 'fffdcb1a-fee4-41c7-9e11-9cd99e65c777'

        # Construct a model instance of ProviderGatewayPortReference by calling from_dict on the json representation
        provider_gateway_port_reference_model = ProviderGatewayPortReference.from_dict(provider_gateway_port_reference_model_json)
        assert provider_gateway_port_reference_model != False

        # Construct a model instance of ProviderGatewayPortReference by calling from_dict on the json representation
        provider_gateway_port_reference_model_dict = ProviderGatewayPortReference.from_dict(provider_gateway_port_reference_model_json).__dict__
        provider_gateway_port_reference_model2 = ProviderGatewayPortReference(**provider_gateway_port_reference_model_dict)

        # Verify the model instances are equivalent
        assert provider_gateway_port_reference_model == provider_gateway_port_reference_model2

        # Convert model instance back to dict and verify no loss of data
        provider_gateway_port_reference_model_json2 = provider_gateway_port_reference_model.to_dict()
        assert provider_gateway_port_reference_model_json2 == provider_gateway_port_reference_model_json

class TestModel_ProviderPort():
    """
    Test Class for ProviderPort
    """

    def test_provider_port_serialization(self):
        """
        Test serialization/deserialization for ProviderPort
        """

        # Construct a json representation of a ProviderPort model
        provider_port_model_json = {}
        provider_port_model_json['id'] = '01122b9b-820f-4c44-8a31-77f1f0806765'
        provider_port_model_json['label'] = 'XCR-FRK-CS-SEC-01'
        provider_port_model_json['location_display_name'] = 'Dallas 03'
        provider_port_model_json['location_name'] = 'dal03'
        provider_port_model_json['provider_name'] = 'provider_1'
        provider_port_model_json['supported_link_speeds'] = [1000, 2000, 5000, 10000]

        # Construct a model instance of ProviderPort by calling from_dict on the json representation
        provider_port_model = ProviderPort.from_dict(provider_port_model_json)
        assert provider_port_model != False

        # Construct a model instance of ProviderPort by calling from_dict on the json representation
        provider_port_model_dict = ProviderPort.from_dict(provider_port_model_json).__dict__
        provider_port_model2 = ProviderPort(**provider_port_model_dict)

        # Verify the model instances are equivalent
        assert provider_port_model == provider_port_model2

        # Convert model instance back to dict and verify no loss of data
        provider_port_model_json2 = provider_port_model.to_dict()
        assert provider_port_model_json2 == provider_port_model_json

class TestModel_ProviderPortCollection():
    """
    Test Class for ProviderPortCollection
    """

    def test_provider_port_collection_serialization(self):
        """
        Test serialization/deserialization for ProviderPortCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        provider_port_collection_first_model = {} # ProviderPortCollectionFirst
        provider_port_collection_first_model['href'] = 'https://directlink.cloud.ibm.com/provider/v2/ports?limit=100'

        provider_port_collection_next_model = {} # ProviderPortCollectionNext
        provider_port_collection_next_model['href'] = 'https://directlink.cloud.ibm.com/provider/v2/ports?start=9d5a91a3e2cbd233b5a5b33436855ed1&limit=100'
        provider_port_collection_next_model['start'] = '9d5a91a3e2cbd233b5a5b33436855ed1'

        provider_port_model = {} # ProviderPort
        provider_port_model['id'] = '01122b9b-820f-4c44-8a31-77f1f0806765'
        provider_port_model['label'] = 'XCR-FRK-CS-SEC-01'
        provider_port_model['location_display_name'] = 'Dallas 03'
        provider_port_model['location_name'] = 'dal03'
        provider_port_model['provider_name'] = 'provider_1'
        provider_port_model['supported_link_speeds'] = [1000, 2000, 5000, 10000]

        # Construct a json representation of a ProviderPortCollection model
        provider_port_collection_model_json = {}
        provider_port_collection_model_json['first'] = provider_port_collection_first_model
        provider_port_collection_model_json['limit'] = 100
        provider_port_collection_model_json['next'] = provider_port_collection_next_model
        provider_port_collection_model_json['total_count'] = 132
        provider_port_collection_model_json['ports'] = [provider_port_model]

        # Construct a model instance of ProviderPortCollection by calling from_dict on the json representation
        provider_port_collection_model = ProviderPortCollection.from_dict(provider_port_collection_model_json)
        assert provider_port_collection_model != False

        # Construct a model instance of ProviderPortCollection by calling from_dict on the json representation
        provider_port_collection_model_dict = ProviderPortCollection.from_dict(provider_port_collection_model_json).__dict__
        provider_port_collection_model2 = ProviderPortCollection(**provider_port_collection_model_dict)

        # Verify the model instances are equivalent
        assert provider_port_collection_model == provider_port_collection_model2

        # Convert model instance back to dict and verify no loss of data
        provider_port_collection_model_json2 = provider_port_collection_model.to_dict()
        assert provider_port_collection_model_json2 == provider_port_collection_model_json

class TestModel_ProviderPortCollectionFirst():
    """
    Test Class for ProviderPortCollectionFirst
    """

    def test_provider_port_collection_first_serialization(self):
        """
        Test serialization/deserialization for ProviderPortCollectionFirst
        """

        # Construct a json representation of a ProviderPortCollectionFirst model
        provider_port_collection_first_model_json = {}
        provider_port_collection_first_model_json['href'] = 'https://directlink.cloud.ibm.com/provider/v2/ports?limit=100'

        # Construct a model instance of ProviderPortCollectionFirst by calling from_dict on the json representation
        provider_port_collection_first_model = ProviderPortCollectionFirst.from_dict(provider_port_collection_first_model_json)
        assert provider_port_collection_first_model != False

        # Construct a model instance of ProviderPortCollectionFirst by calling from_dict on the json representation
        provider_port_collection_first_model_dict = ProviderPortCollectionFirst.from_dict(provider_port_collection_first_model_json).__dict__
        provider_port_collection_first_model2 = ProviderPortCollectionFirst(**provider_port_collection_first_model_dict)

        # Verify the model instances are equivalent
        assert provider_port_collection_first_model == provider_port_collection_first_model2

        # Convert model instance back to dict and verify no loss of data
        provider_port_collection_first_model_json2 = provider_port_collection_first_model.to_dict()
        assert provider_port_collection_first_model_json2 == provider_port_collection_first_model_json

class TestModel_ProviderPortCollectionNext():
    """
    Test Class for ProviderPortCollectionNext
    """

    def test_provider_port_collection_next_serialization(self):
        """
        Test serialization/deserialization for ProviderPortCollectionNext
        """

        # Construct a json representation of a ProviderPortCollectionNext model
        provider_port_collection_next_model_json = {}
        provider_port_collection_next_model_json['href'] = 'https://directlink.cloud.ibm.com/provider/v2/ports?start=9d5a91a3e2cbd233b5a5b33436855ed1&limit=100'
        provider_port_collection_next_model_json['start'] = '9d5a91a3e2cbd233b5a5b33436855ed1'

        # Construct a model instance of ProviderPortCollectionNext by calling from_dict on the json representation
        provider_port_collection_next_model = ProviderPortCollectionNext.from_dict(provider_port_collection_next_model_json)
        assert provider_port_collection_next_model != False

        # Construct a model instance of ProviderPortCollectionNext by calling from_dict on the json representation
        provider_port_collection_next_model_dict = ProviderPortCollectionNext.from_dict(provider_port_collection_next_model_json).__dict__
        provider_port_collection_next_model2 = ProviderPortCollectionNext(**provider_port_collection_next_model_dict)

        # Verify the model instances are equivalent
        assert provider_port_collection_next_model == provider_port_collection_next_model2

        # Convert model instance back to dict and verify no loss of data
        provider_port_collection_next_model_json2 = provider_port_collection_next_model.to_dict()
        assert provider_port_collection_next_model_json2 == provider_port_collection_next_model_json

class TestModel_ProviderGatewayChangeRequestProviderGatewayCreate():
    """
    Test Class for ProviderGatewayChangeRequestProviderGatewayCreate
    """

    def test_provider_gateway_change_request_provider_gateway_create_serialization(self):
        """
        Test serialization/deserialization for ProviderGatewayChangeRequestProviderGatewayCreate
        """

        # Construct a json representation of a ProviderGatewayChangeRequestProviderGatewayCreate model
        provider_gateway_change_request_provider_gateway_create_model_json = {}
        provider_gateway_change_request_provider_gateway_create_model_json['type'] = 'create_gateway'

        # Construct a model instance of ProviderGatewayChangeRequestProviderGatewayCreate by calling from_dict on the json representation
        provider_gateway_change_request_provider_gateway_create_model = ProviderGatewayChangeRequestProviderGatewayCreate.from_dict(provider_gateway_change_request_provider_gateway_create_model_json)
        assert provider_gateway_change_request_provider_gateway_create_model != False

        # Construct a model instance of ProviderGatewayChangeRequestProviderGatewayCreate by calling from_dict on the json representation
        provider_gateway_change_request_provider_gateway_create_model_dict = ProviderGatewayChangeRequestProviderGatewayCreate.from_dict(provider_gateway_change_request_provider_gateway_create_model_json).__dict__
        provider_gateway_change_request_provider_gateway_create_model2 = ProviderGatewayChangeRequestProviderGatewayCreate(**provider_gateway_change_request_provider_gateway_create_model_dict)

        # Verify the model instances are equivalent
        assert provider_gateway_change_request_provider_gateway_create_model == provider_gateway_change_request_provider_gateway_create_model2

        # Convert model instance back to dict and verify no loss of data
        provider_gateway_change_request_provider_gateway_create_model_json2 = provider_gateway_change_request_provider_gateway_create_model.to_dict()
        assert provider_gateway_change_request_provider_gateway_create_model_json2 == provider_gateway_change_request_provider_gateway_create_model_json

class TestModel_ProviderGatewayChangeRequestProviderGatewayDelete():
    """
    Test Class for ProviderGatewayChangeRequestProviderGatewayDelete
    """

    def test_provider_gateway_change_request_provider_gateway_delete_serialization(self):
        """
        Test serialization/deserialization for ProviderGatewayChangeRequestProviderGatewayDelete
        """

        # Construct a json representation of a ProviderGatewayChangeRequestProviderGatewayDelete model
        provider_gateway_change_request_provider_gateway_delete_model_json = {}
        provider_gateway_change_request_provider_gateway_delete_model_json['type'] = 'delete_gateway'

        # Construct a model instance of ProviderGatewayChangeRequestProviderGatewayDelete by calling from_dict on the json representation
        provider_gateway_change_request_provider_gateway_delete_model = ProviderGatewayChangeRequestProviderGatewayDelete.from_dict(provider_gateway_change_request_provider_gateway_delete_model_json)
        assert provider_gateway_change_request_provider_gateway_delete_model != False

        # Construct a model instance of ProviderGatewayChangeRequestProviderGatewayDelete by calling from_dict on the json representation
        provider_gateway_change_request_provider_gateway_delete_model_dict = ProviderGatewayChangeRequestProviderGatewayDelete.from_dict(provider_gateway_change_request_provider_gateway_delete_model_json).__dict__
        provider_gateway_change_request_provider_gateway_delete_model2 = ProviderGatewayChangeRequestProviderGatewayDelete(**provider_gateway_change_request_provider_gateway_delete_model_dict)

        # Verify the model instances are equivalent
        assert provider_gateway_change_request_provider_gateway_delete_model == provider_gateway_change_request_provider_gateway_delete_model2

        # Convert model instance back to dict and verify no loss of data
        provider_gateway_change_request_provider_gateway_delete_model_json2 = provider_gateway_change_request_provider_gateway_delete_model.to_dict()
        assert provider_gateway_change_request_provider_gateway_delete_model_json2 == provider_gateway_change_request_provider_gateway_delete_model_json

class TestModel_ProviderGatewayChangeRequestProviderGatewayUpdateAttributes():
    """
    Test Class for ProviderGatewayChangeRequestProviderGatewayUpdateAttributes
    """

    def test_provider_gateway_change_request_provider_gateway_update_attributes_serialization(self):
        """
        Test serialization/deserialization for ProviderGatewayChangeRequestProviderGatewayUpdateAttributes
        """

        # Construct dict forms of any model objects needed in order to build this model.

        provider_gateway_update_attributes_updates_item_model = {} # ProviderGatewayUpdateAttributesUpdatesItemProviderGatewaySpeedUpdate
        provider_gateway_update_attributes_updates_item_model['speed_mbps'] = 500

        # Construct a json representation of a ProviderGatewayChangeRequestProviderGatewayUpdateAttributes model
        provider_gateway_change_request_provider_gateway_update_attributes_model_json = {}
        provider_gateway_change_request_provider_gateway_update_attributes_model_json['type'] = 'update_attributes'
        provider_gateway_change_request_provider_gateway_update_attributes_model_json['updates'] = [provider_gateway_update_attributes_updates_item_model]

        # Construct a model instance of ProviderGatewayChangeRequestProviderGatewayUpdateAttributes by calling from_dict on the json representation
        provider_gateway_change_request_provider_gateway_update_attributes_model = ProviderGatewayChangeRequestProviderGatewayUpdateAttributes.from_dict(provider_gateway_change_request_provider_gateway_update_attributes_model_json)
        assert provider_gateway_change_request_provider_gateway_update_attributes_model != False

        # Construct a model instance of ProviderGatewayChangeRequestProviderGatewayUpdateAttributes by calling from_dict on the json representation
        provider_gateway_change_request_provider_gateway_update_attributes_model_dict = ProviderGatewayChangeRequestProviderGatewayUpdateAttributes.from_dict(provider_gateway_change_request_provider_gateway_update_attributes_model_json).__dict__
        provider_gateway_change_request_provider_gateway_update_attributes_model2 = ProviderGatewayChangeRequestProviderGatewayUpdateAttributes(**provider_gateway_change_request_provider_gateway_update_attributes_model_dict)

        # Verify the model instances are equivalent
        assert provider_gateway_change_request_provider_gateway_update_attributes_model == provider_gateway_change_request_provider_gateway_update_attributes_model2

        # Convert model instance back to dict and verify no loss of data
        provider_gateway_change_request_provider_gateway_update_attributes_model_json2 = provider_gateway_change_request_provider_gateway_update_attributes_model.to_dict()
        assert provider_gateway_change_request_provider_gateway_update_attributes_model_json2 == provider_gateway_change_request_provider_gateway_update_attributes_model_json

class TestModel_ProviderGatewayUpdateAttributesUpdatesItemProviderGatewayBGPASNUpdate():
    """
    Test Class for ProviderGatewayUpdateAttributesUpdatesItemProviderGatewayBGPASNUpdate
    """

    def test_provider_gateway_update_attributes_updates_item_provider_gateway_bgpasn_update_serialization(self):
        """
        Test serialization/deserialization for ProviderGatewayUpdateAttributesUpdatesItemProviderGatewayBGPASNUpdate
        """

        # Construct a json representation of a ProviderGatewayUpdateAttributesUpdatesItemProviderGatewayBGPASNUpdate model
        provider_gateway_update_attributes_updates_item_provider_gateway_bgpasn_update_model_json = {}
        provider_gateway_update_attributes_updates_item_provider_gateway_bgpasn_update_model_json['bgp_asn'] = 64999

        # Construct a model instance of ProviderGatewayUpdateAttributesUpdatesItemProviderGatewayBGPASNUpdate by calling from_dict on the json representation
        provider_gateway_update_attributes_updates_item_provider_gateway_bgpasn_update_model = ProviderGatewayUpdateAttributesUpdatesItemProviderGatewayBGPASNUpdate.from_dict(provider_gateway_update_attributes_updates_item_provider_gateway_bgpasn_update_model_json)
        assert provider_gateway_update_attributes_updates_item_provider_gateway_bgpasn_update_model != False

        # Construct a model instance of ProviderGatewayUpdateAttributesUpdatesItemProviderGatewayBGPASNUpdate by calling from_dict on the json representation
        provider_gateway_update_attributes_updates_item_provider_gateway_bgpasn_update_model_dict = ProviderGatewayUpdateAttributesUpdatesItemProviderGatewayBGPASNUpdate.from_dict(provider_gateway_update_attributes_updates_item_provider_gateway_bgpasn_update_model_json).__dict__
        provider_gateway_update_attributes_updates_item_provider_gateway_bgpasn_update_model2 = ProviderGatewayUpdateAttributesUpdatesItemProviderGatewayBGPASNUpdate(**provider_gateway_update_attributes_updates_item_provider_gateway_bgpasn_update_model_dict)

        # Verify the model instances are equivalent
        assert provider_gateway_update_attributes_updates_item_provider_gateway_bgpasn_update_model == provider_gateway_update_attributes_updates_item_provider_gateway_bgpasn_update_model2

        # Convert model instance back to dict and verify no loss of data
        provider_gateway_update_attributes_updates_item_provider_gateway_bgpasn_update_model_json2 = provider_gateway_update_attributes_updates_item_provider_gateway_bgpasn_update_model.to_dict()
        assert provider_gateway_update_attributes_updates_item_provider_gateway_bgpasn_update_model_json2 == provider_gateway_update_attributes_updates_item_provider_gateway_bgpasn_update_model_json

class TestModel_ProviderGatewayUpdateAttributesUpdatesItemProviderGatewayBGPIPUpdate():
    """
    Test Class for ProviderGatewayUpdateAttributesUpdatesItemProviderGatewayBGPIPUpdate
    """

    def test_provider_gateway_update_attributes_updates_item_provider_gateway_bgpip_update_serialization(self):
        """
        Test serialization/deserialization for ProviderGatewayUpdateAttributesUpdatesItemProviderGatewayBGPIPUpdate
        """

        # Construct a json representation of a ProviderGatewayUpdateAttributesUpdatesItemProviderGatewayBGPIPUpdate model
        provider_gateway_update_attributes_updates_item_provider_gateway_bgpip_update_model_json = {}
        provider_gateway_update_attributes_updates_item_provider_gateway_bgpip_update_model_json['bgp_cer_cidr'] = '169.254.0.10/30'
        provider_gateway_update_attributes_updates_item_provider_gateway_bgpip_update_model_json['bgp_ibm_cidr'] = '169.254.0.9/30'

        # Construct a model instance of ProviderGatewayUpdateAttributesUpdatesItemProviderGatewayBGPIPUpdate by calling from_dict on the json representation
        provider_gateway_update_attributes_updates_item_provider_gateway_bgpip_update_model = ProviderGatewayUpdateAttributesUpdatesItemProviderGatewayBGPIPUpdate.from_dict(provider_gateway_update_attributes_updates_item_provider_gateway_bgpip_update_model_json)
        assert provider_gateway_update_attributes_updates_item_provider_gateway_bgpip_update_model != False

        # Construct a model instance of ProviderGatewayUpdateAttributesUpdatesItemProviderGatewayBGPIPUpdate by calling from_dict on the json representation
        provider_gateway_update_attributes_updates_item_provider_gateway_bgpip_update_model_dict = ProviderGatewayUpdateAttributesUpdatesItemProviderGatewayBGPIPUpdate.from_dict(provider_gateway_update_attributes_updates_item_provider_gateway_bgpip_update_model_json).__dict__
        provider_gateway_update_attributes_updates_item_provider_gateway_bgpip_update_model2 = ProviderGatewayUpdateAttributesUpdatesItemProviderGatewayBGPIPUpdate(**provider_gateway_update_attributes_updates_item_provider_gateway_bgpip_update_model_dict)

        # Verify the model instances are equivalent
        assert provider_gateway_update_attributes_updates_item_provider_gateway_bgpip_update_model == provider_gateway_update_attributes_updates_item_provider_gateway_bgpip_update_model2

        # Convert model instance back to dict and verify no loss of data
        provider_gateway_update_attributes_updates_item_provider_gateway_bgpip_update_model_json2 = provider_gateway_update_attributes_updates_item_provider_gateway_bgpip_update_model.to_dict()
        assert provider_gateway_update_attributes_updates_item_provider_gateway_bgpip_update_model_json2 == provider_gateway_update_attributes_updates_item_provider_gateway_bgpip_update_model_json

class TestModel_ProviderGatewayUpdateAttributesUpdatesItemProviderGatewaySpeedUpdate():
    """
    Test Class for ProviderGatewayUpdateAttributesUpdatesItemProviderGatewaySpeedUpdate
    """

    def test_provider_gateway_update_attributes_updates_item_provider_gateway_speed_update_serialization(self):
        """
        Test serialization/deserialization for ProviderGatewayUpdateAttributesUpdatesItemProviderGatewaySpeedUpdate
        """

        # Construct a json representation of a ProviderGatewayUpdateAttributesUpdatesItemProviderGatewaySpeedUpdate model
        provider_gateway_update_attributes_updates_item_provider_gateway_speed_update_model_json = {}
        provider_gateway_update_attributes_updates_item_provider_gateway_speed_update_model_json['speed_mbps'] = 500

        # Construct a model instance of ProviderGatewayUpdateAttributesUpdatesItemProviderGatewaySpeedUpdate by calling from_dict on the json representation
        provider_gateway_update_attributes_updates_item_provider_gateway_speed_update_model = ProviderGatewayUpdateAttributesUpdatesItemProviderGatewaySpeedUpdate.from_dict(provider_gateway_update_attributes_updates_item_provider_gateway_speed_update_model_json)
        assert provider_gateway_update_attributes_updates_item_provider_gateway_speed_update_model != False

        # Construct a model instance of ProviderGatewayUpdateAttributesUpdatesItemProviderGatewaySpeedUpdate by calling from_dict on the json representation
        provider_gateway_update_attributes_updates_item_provider_gateway_speed_update_model_dict = ProviderGatewayUpdateAttributesUpdatesItemProviderGatewaySpeedUpdate.from_dict(provider_gateway_update_attributes_updates_item_provider_gateway_speed_update_model_json).__dict__
        provider_gateway_update_attributes_updates_item_provider_gateway_speed_update_model2 = ProviderGatewayUpdateAttributesUpdatesItemProviderGatewaySpeedUpdate(**provider_gateway_update_attributes_updates_item_provider_gateway_speed_update_model_dict)

        # Verify the model instances are equivalent
        assert provider_gateway_update_attributes_updates_item_provider_gateway_speed_update_model == provider_gateway_update_attributes_updates_item_provider_gateway_speed_update_model2

        # Convert model instance back to dict and verify no loss of data
        provider_gateway_update_attributes_updates_item_provider_gateway_speed_update_model_json2 = provider_gateway_update_attributes_updates_item_provider_gateway_speed_update_model.to_dict()
        assert provider_gateway_update_attributes_updates_item_provider_gateway_speed_update_model_json2 == provider_gateway_update_attributes_updates_item_provider_gateway_speed_update_model_json

class TestModel_ProviderGatewayUpdateAttributesUpdatesItemProviderGatewayVLAN():
    """
    Test Class for ProviderGatewayUpdateAttributesUpdatesItemProviderGatewayVLAN
    """

    def test_provider_gateway_update_attributes_updates_item_provider_gateway_vlan_serialization(self):
        """
        Test serialization/deserialization for ProviderGatewayUpdateAttributesUpdatesItemProviderGatewayVLAN
        """

        # Construct a json representation of a ProviderGatewayUpdateAttributesUpdatesItemProviderGatewayVLAN model
        provider_gateway_update_attributes_updates_item_provider_gateway_vlan_model_json = {}
        provider_gateway_update_attributes_updates_item_provider_gateway_vlan_model_json['vlan'] = 10

        # Construct a model instance of ProviderGatewayUpdateAttributesUpdatesItemProviderGatewayVLAN by calling from_dict on the json representation
        provider_gateway_update_attributes_updates_item_provider_gateway_vlan_model = ProviderGatewayUpdateAttributesUpdatesItemProviderGatewayVLAN.from_dict(provider_gateway_update_attributes_updates_item_provider_gateway_vlan_model_json)
        assert provider_gateway_update_attributes_updates_item_provider_gateway_vlan_model != False

        # Construct a model instance of ProviderGatewayUpdateAttributesUpdatesItemProviderGatewayVLAN by calling from_dict on the json representation
        provider_gateway_update_attributes_updates_item_provider_gateway_vlan_model_dict = ProviderGatewayUpdateAttributesUpdatesItemProviderGatewayVLAN.from_dict(provider_gateway_update_attributes_updates_item_provider_gateway_vlan_model_json).__dict__
        provider_gateway_update_attributes_updates_item_provider_gateway_vlan_model2 = ProviderGatewayUpdateAttributesUpdatesItemProviderGatewayVLAN(**provider_gateway_update_attributes_updates_item_provider_gateway_vlan_model_dict)

        # Verify the model instances are equivalent
        assert provider_gateway_update_attributes_updates_item_provider_gateway_vlan_model == provider_gateway_update_attributes_updates_item_provider_gateway_vlan_model2

        # Convert model instance back to dict and verify no loss of data
        provider_gateway_update_attributes_updates_item_provider_gateway_vlan_model_json2 = provider_gateway_update_attributes_updates_item_provider_gateway_vlan_model.to_dict()
        assert provider_gateway_update_attributes_updates_item_provider_gateway_vlan_model_json2 == provider_gateway_update_attributes_updates_item_provider_gateway_vlan_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
