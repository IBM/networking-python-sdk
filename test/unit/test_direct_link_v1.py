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

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import io
import json
import pytest
import requests
import responses
import tempfile
from ibm_cloud_networking_services.direct_link_v1 import *

version = 'testString'

service = DirectLinkV1(
    authenticator=NoAuthAuthenticator(),
    version=version
    )

base_url = 'https://directlink.cloud.ibm.com/v1'
service.set_service_url(base_url)

##############################################################################
# Start of Service: Gateways
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_gateways
#-----------------------------------------------------------------------------
class TestListGateways():

    #--------------------------------------------------------
    # list_gateways()
    #--------------------------------------------------------
    @responses.activate
    def test_list_gateways_all_params(self):
        # Set up mock
        url = base_url + '/gateways'
        mock_response = '{"gateways": [{"authentication_key": {"crn": "crn:v1:bluemix:public:kms:us-south:a/766d8d374a484f029d0fca5a40a52a1c:5d343839-07d3-4213-a950-0f71ed45423f:key:7fc1a0ba-4633-48cb-997b-5749787c952c"}, "bgp_asn": 64999, "bgp_base_cidr": "bgp_base_cidr", "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "carrier_name": "myCarrierName", "change_request": {"type": "create_gateway"}, "completion_notice_reject_reason": "The completion notice file was blank", "connection_mode": "transit", "created_at": "2019-01-01T12:00:00", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::dedicated:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "cross_connect_router": "xcr01.dal03", "customer_name": "newCustomerName", "global": true, "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "link_status": "up", "location_display_name": "Dallas 03", "location_name": "dal03", "macsec_config": {"active": true, "active_cak": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222", "status": "status"}, "cipher_suite": "gcm_aes_xpn_256", "confidentiality_offset": 0, "cryptographic_algorithm": "aes_256_cmac", "fallback_cak": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222", "status": "status"}, "key_server_priority": 255, "primary_cak": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222", "status": "status"}, "sak_expiry_time": 3600, "security_policy": "must_secure", "status": "secured", "window_size": 64}, "metered": false, "name": "myGateway", "operational_status": "awaiting_completion_notice", "port": {"id": "54321b1a-fee4-41c7-9e11-9cd99e000aaa"}, "provider_api_managed": false, "resource_group": {"id": "56969d6043e9465c883cb9f7363e78e8"}, "speed_mbps": 1000, "type": "dedicated", "vlan": 10}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_gateways()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_gateways_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_gateways_value_error(self):
        # Set up mock
        url = base_url + '/gateways'
        mock_response = '{"gateways": [{"authentication_key": {"crn": "crn:v1:bluemix:public:kms:us-south:a/766d8d374a484f029d0fca5a40a52a1c:5d343839-07d3-4213-a950-0f71ed45423f:key:7fc1a0ba-4633-48cb-997b-5749787c952c"}, "bgp_asn": 64999, "bgp_base_cidr": "bgp_base_cidr", "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "carrier_name": "myCarrierName", "change_request": {"type": "create_gateway"}, "completion_notice_reject_reason": "The completion notice file was blank", "connection_mode": "transit", "created_at": "2019-01-01T12:00:00", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::dedicated:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "cross_connect_router": "xcr01.dal03", "customer_name": "newCustomerName", "global": true, "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "link_status": "up", "location_display_name": "Dallas 03", "location_name": "dal03", "macsec_config": {"active": true, "active_cak": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222", "status": "status"}, "cipher_suite": "gcm_aes_xpn_256", "confidentiality_offset": 0, "cryptographic_algorithm": "aes_256_cmac", "fallback_cak": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222", "status": "status"}, "key_server_priority": 255, "primary_cak": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222", "status": "status"}, "sak_expiry_time": 3600, "security_policy": "must_secure", "status": "secured", "window_size": 64}, "metered": false, "name": "myGateway", "operational_status": "awaiting_completion_notice", "port": {"id": "54321b1a-fee4-41c7-9e11-9cd99e000aaa"}, "provider_api_managed": false, "resource_group": {"id": "56969d6043e9465c883cb9f7363e78e8"}, "speed_mbps": 1000, "type": "dedicated", "vlan": 10}]}'
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
                service.list_gateways(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for create_gateway
#-----------------------------------------------------------------------------
class TestCreateGateway():

    #--------------------------------------------------------
    # create_gateway()
    #--------------------------------------------------------
    @responses.activate
    def test_create_gateway_all_params(self):
        # Set up mock
        url = base_url + '/gateways'
        mock_response = '{"authentication_key": {"crn": "crn:v1:bluemix:public:kms:us-south:a/766d8d374a484f029d0fca5a40a52a1c:5d343839-07d3-4213-a950-0f71ed45423f:key:7fc1a0ba-4633-48cb-997b-5749787c952c"}, "bgp_asn": 64999, "bgp_base_cidr": "bgp_base_cidr", "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "carrier_name": "myCarrierName", "change_request": {"type": "create_gateway"}, "completion_notice_reject_reason": "The completion notice file was blank", "connection_mode": "transit", "created_at": "2019-01-01T12:00:00", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::dedicated:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "cross_connect_router": "xcr01.dal03", "customer_name": "newCustomerName", "global": true, "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "link_status": "up", "location_display_name": "Dallas 03", "location_name": "dal03", "macsec_config": {"active": true, "active_cak": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222", "status": "status"}, "cipher_suite": "gcm_aes_xpn_256", "confidentiality_offset": 0, "cryptographic_algorithm": "aes_256_cmac", "fallback_cak": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222", "status": "status"}, "key_server_priority": 255, "primary_cak": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222", "status": "status"}, "sak_expiry_time": 3600, "security_policy": "must_secure", "status": "secured", "window_size": 64}, "metered": false, "name": "myGateway", "operational_status": "awaiting_completion_notice", "port": {"id": "54321b1a-fee4-41c7-9e11-9cd99e000aaa"}, "provider_api_managed": false, "resource_group": {"id": "56969d6043e9465c883cb9f7363e78e8"}, "speed_mbps": 1000, "type": "dedicated", "vlan": 10}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a GatewayMacsecConfigTemplateFallbackCak model
        gateway_macsec_config_template_fallback_cak_model = {}
        gateway_macsec_config_template_fallback_cak_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a dict representation of a GatewayMacsecConfigTemplatePrimaryCak model
        gateway_macsec_config_template_primary_cak_model = {}
        gateway_macsec_config_template_primary_cak_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a dict representation of a GatewayMacsecConfigTemplate model
        gateway_macsec_config_template_model = {}
        gateway_macsec_config_template_model['active'] = True
        gateway_macsec_config_template_model['fallback_cak'] = gateway_macsec_config_template_fallback_cak_model
        gateway_macsec_config_template_model['primary_cak'] = gateway_macsec_config_template_primary_cak_model
        gateway_macsec_config_template_model['window_size'] = 148809600

        # Construct a dict representation of a GatewayTemplateGatewayTypeDedicatedTemplateAuthenticationKey model
        gateway_template_gateway_type_dedicated_template_authentication_key_model = {}
        gateway_template_gateway_type_dedicated_template_authentication_key_model['crn'] = 'crn:v1:bluemix:public:kms:us-south:a/766d8d374a484f029d0fca5a40a52a1c:5d343839-07d3-4213-a950-0f71ed45423f:key:7fc1a0ba-4633-48cb-997b-5749787c952c'

        # Construct a dict representation of a ResourceGroupIdentity model
        resource_group_identity_model = {}
        resource_group_identity_model['id'] = '56969d6043e9465c883cb9f7363e78e8'

        # Construct a dict representation of a GatewayTemplateGatewayTypeDedicatedTemplate model
        gateway_template_model = {}
        gateway_template_model['authentication_key'] = gateway_template_gateway_type_dedicated_template_authentication_key_model
        gateway_template_model['bgp_asn'] = 64999
        gateway_template_model['bgp_base_cidr'] = 'testString'
        gateway_template_model['bgp_cer_cidr'] = '169.254.0.10/30'
        gateway_template_model['bgp_ibm_cidr'] = '169.254.0.9/30'
        gateway_template_model['connection_mode'] = 'transit'
        gateway_template_model['global'] = True
        gateway_template_model['metered'] = False
        gateway_template_model['name'] = 'myGateway'
        gateway_template_model['resource_group'] = resource_group_identity_model
        gateway_template_model['speed_mbps'] = 1000
        gateway_template_model['type'] = 'dedicated'
        gateway_template_model['carrier_name'] = 'myCarrierName'
        gateway_template_model['cross_connect_router'] = 'xcr01.dal03'
        gateway_template_model['customer_name'] = 'newCustomerName'
        gateway_template_model['location_name'] = 'dal03'
        gateway_template_model['macsec_config'] = gateway_macsec_config_template_model

        # Set up parameter values
        gateway_template = gateway_template_model

        # Invoke method
        response = service.create_gateway(
            gateway_template,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == gateway_template


    #--------------------------------------------------------
    # test_create_gateway_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_gateway_value_error(self):
        # Set up mock
        url = base_url + '/gateways'
        mock_response = '{"authentication_key": {"crn": "crn:v1:bluemix:public:kms:us-south:a/766d8d374a484f029d0fca5a40a52a1c:5d343839-07d3-4213-a950-0f71ed45423f:key:7fc1a0ba-4633-48cb-997b-5749787c952c"}, "bgp_asn": 64999, "bgp_base_cidr": "bgp_base_cidr", "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "carrier_name": "myCarrierName", "change_request": {"type": "create_gateway"}, "completion_notice_reject_reason": "The completion notice file was blank", "connection_mode": "transit", "created_at": "2019-01-01T12:00:00", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::dedicated:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "cross_connect_router": "xcr01.dal03", "customer_name": "newCustomerName", "global": true, "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "link_status": "up", "location_display_name": "Dallas 03", "location_name": "dal03", "macsec_config": {"active": true, "active_cak": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222", "status": "status"}, "cipher_suite": "gcm_aes_xpn_256", "confidentiality_offset": 0, "cryptographic_algorithm": "aes_256_cmac", "fallback_cak": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222", "status": "status"}, "key_server_priority": 255, "primary_cak": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222", "status": "status"}, "sak_expiry_time": 3600, "security_policy": "must_secure", "status": "secured", "window_size": 64}, "metered": false, "name": "myGateway", "operational_status": "awaiting_completion_notice", "port": {"id": "54321b1a-fee4-41c7-9e11-9cd99e000aaa"}, "provider_api_managed": false, "resource_group": {"id": "56969d6043e9465c883cb9f7363e78e8"}, "speed_mbps": 1000, "type": "dedicated", "vlan": 10}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a GatewayMacsecConfigTemplateFallbackCak model
        gateway_macsec_config_template_fallback_cak_model = {}
        gateway_macsec_config_template_fallback_cak_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a dict representation of a GatewayMacsecConfigTemplatePrimaryCak model
        gateway_macsec_config_template_primary_cak_model = {}
        gateway_macsec_config_template_primary_cak_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a dict representation of a GatewayMacsecConfigTemplate model
        gateway_macsec_config_template_model = {}
        gateway_macsec_config_template_model['active'] = True
        gateway_macsec_config_template_model['fallback_cak'] = gateway_macsec_config_template_fallback_cak_model
        gateway_macsec_config_template_model['primary_cak'] = gateway_macsec_config_template_primary_cak_model
        gateway_macsec_config_template_model['window_size'] = 148809600

        # Construct a dict representation of a GatewayTemplateGatewayTypeDedicatedTemplateAuthenticationKey model
        gateway_template_gateway_type_dedicated_template_authentication_key_model = {}
        gateway_template_gateway_type_dedicated_template_authentication_key_model['crn'] = 'crn:v1:bluemix:public:kms:us-south:a/766d8d374a484f029d0fca5a40a52a1c:5d343839-07d3-4213-a950-0f71ed45423f:key:7fc1a0ba-4633-48cb-997b-5749787c952c'

        # Construct a dict representation of a ResourceGroupIdentity model
        resource_group_identity_model = {}
        resource_group_identity_model['id'] = '56969d6043e9465c883cb9f7363e78e8'

        # Construct a dict representation of a GatewayTemplateGatewayTypeDedicatedTemplate model
        gateway_template_model = {}
        gateway_template_model['authentication_key'] = gateway_template_gateway_type_dedicated_template_authentication_key_model
        gateway_template_model['bgp_asn'] = 64999
        gateway_template_model['bgp_base_cidr'] = 'testString'
        gateway_template_model['bgp_cer_cidr'] = '169.254.0.10/30'
        gateway_template_model['bgp_ibm_cidr'] = '169.254.0.9/30'
        gateway_template_model['connection_mode'] = 'transit'
        gateway_template_model['global'] = True
        gateway_template_model['metered'] = False
        gateway_template_model['name'] = 'myGateway'
        gateway_template_model['resource_group'] = resource_group_identity_model
        gateway_template_model['speed_mbps'] = 1000
        gateway_template_model['type'] = 'dedicated'
        gateway_template_model['carrier_name'] = 'myCarrierName'
        gateway_template_model['cross_connect_router'] = 'xcr01.dal03'
        gateway_template_model['customer_name'] = 'newCustomerName'
        gateway_template_model['location_name'] = 'dal03'
        gateway_template_model['macsec_config'] = gateway_macsec_config_template_model

        # Set up parameter values
        gateway_template = gateway_template_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "gateway_template": gateway_template,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.create_gateway(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_gateway
#-----------------------------------------------------------------------------
class TestDeleteGateway():

    #--------------------------------------------------------
    # delete_gateway()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_gateway_all_params(self):
        # Set up mock
        url = base_url + '/gateways/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.delete_gateway(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_delete_gateway_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_gateway_value_error(self):
        # Set up mock
        url = base_url + '/gateways/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_gateway(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_gateway
#-----------------------------------------------------------------------------
class TestGetGateway():

    #--------------------------------------------------------
    # get_gateway()
    #--------------------------------------------------------
    @responses.activate
    def test_get_gateway_all_params(self):
        # Set up mock
        url = base_url + '/gateways/testString'
        mock_response = '{"authentication_key": {"crn": "crn:v1:bluemix:public:kms:us-south:a/766d8d374a484f029d0fca5a40a52a1c:5d343839-07d3-4213-a950-0f71ed45423f:key:7fc1a0ba-4633-48cb-997b-5749787c952c"}, "bgp_asn": 64999, "bgp_base_cidr": "bgp_base_cidr", "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "carrier_name": "myCarrierName", "change_request": {"type": "create_gateway"}, "completion_notice_reject_reason": "The completion notice file was blank", "connection_mode": "transit", "created_at": "2019-01-01T12:00:00", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::dedicated:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "cross_connect_router": "xcr01.dal03", "customer_name": "newCustomerName", "global": true, "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "link_status": "up", "location_display_name": "Dallas 03", "location_name": "dal03", "macsec_config": {"active": true, "active_cak": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222", "status": "status"}, "cipher_suite": "gcm_aes_xpn_256", "confidentiality_offset": 0, "cryptographic_algorithm": "aes_256_cmac", "fallback_cak": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222", "status": "status"}, "key_server_priority": 255, "primary_cak": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222", "status": "status"}, "sak_expiry_time": 3600, "security_policy": "must_secure", "status": "secured", "window_size": 64}, "metered": false, "name": "myGateway", "operational_status": "awaiting_completion_notice", "port": {"id": "54321b1a-fee4-41c7-9e11-9cd99e000aaa"}, "provider_api_managed": false, "resource_group": {"id": "56969d6043e9465c883cb9f7363e78e8"}, "speed_mbps": 1000, "type": "dedicated", "vlan": 10}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_gateway(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_gateway_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_gateway_value_error(self):
        # Set up mock
        url = base_url + '/gateways/testString'
        mock_response = '{"authentication_key": {"crn": "crn:v1:bluemix:public:kms:us-south:a/766d8d374a484f029d0fca5a40a52a1c:5d343839-07d3-4213-a950-0f71ed45423f:key:7fc1a0ba-4633-48cb-997b-5749787c952c"}, "bgp_asn": 64999, "bgp_base_cidr": "bgp_base_cidr", "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "carrier_name": "myCarrierName", "change_request": {"type": "create_gateway"}, "completion_notice_reject_reason": "The completion notice file was blank", "connection_mode": "transit", "created_at": "2019-01-01T12:00:00", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::dedicated:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "cross_connect_router": "xcr01.dal03", "customer_name": "newCustomerName", "global": true, "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "link_status": "up", "location_display_name": "Dallas 03", "location_name": "dal03", "macsec_config": {"active": true, "active_cak": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222", "status": "status"}, "cipher_suite": "gcm_aes_xpn_256", "confidentiality_offset": 0, "cryptographic_algorithm": "aes_256_cmac", "fallback_cak": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222", "status": "status"}, "key_server_priority": 255, "primary_cak": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222", "status": "status"}, "sak_expiry_time": 3600, "security_policy": "must_secure", "status": "secured", "window_size": 64}, "metered": false, "name": "myGateway", "operational_status": "awaiting_completion_notice", "port": {"id": "54321b1a-fee4-41c7-9e11-9cd99e000aaa"}, "provider_api_managed": false, "resource_group": {"id": "56969d6043e9465c883cb9f7363e78e8"}, "speed_mbps": 1000, "type": "dedicated", "vlan": 10}'
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
                service.get_gateway(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_gateway
#-----------------------------------------------------------------------------
class TestUpdateGateway():

    #--------------------------------------------------------
    # update_gateway()
    #--------------------------------------------------------
    @responses.activate
    def test_update_gateway_all_params(self):
        # Set up mock
        url = base_url + '/gateways/testString'
        mock_response = '{"authentication_key": {"crn": "crn:v1:bluemix:public:kms:us-south:a/766d8d374a484f029d0fca5a40a52a1c:5d343839-07d3-4213-a950-0f71ed45423f:key:7fc1a0ba-4633-48cb-997b-5749787c952c"}, "bgp_asn": 64999, "bgp_base_cidr": "bgp_base_cidr", "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "carrier_name": "myCarrierName", "change_request": {"type": "create_gateway"}, "completion_notice_reject_reason": "The completion notice file was blank", "connection_mode": "transit", "created_at": "2019-01-01T12:00:00", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::dedicated:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "cross_connect_router": "xcr01.dal03", "customer_name": "newCustomerName", "global": true, "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "link_status": "up", "location_display_name": "Dallas 03", "location_name": "dal03", "macsec_config": {"active": true, "active_cak": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222", "status": "status"}, "cipher_suite": "gcm_aes_xpn_256", "confidentiality_offset": 0, "cryptographic_algorithm": "aes_256_cmac", "fallback_cak": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222", "status": "status"}, "key_server_priority": 255, "primary_cak": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222", "status": "status"}, "sak_expiry_time": 3600, "security_policy": "must_secure", "status": "secured", "window_size": 64}, "metered": false, "name": "myGateway", "operational_status": "awaiting_completion_notice", "port": {"id": "54321b1a-fee4-41c7-9e11-9cd99e000aaa"}, "provider_api_managed": false, "resource_group": {"id": "56969d6043e9465c883cb9f7363e78e8"}, "speed_mbps": 1000, "type": "dedicated", "vlan": 10}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a GatewayPatchTemplateAuthenticationKey model
        gateway_patch_template_authentication_key_model = {}
        gateway_patch_template_authentication_key_model['crn'] = 'crn:v1:bluemix:public:kms:us-south:a/766d8d374a484f029d0fca5a40a52a1c:5d343839-07d3-4213-a950-0f71ed45423f:key:7fc1a0ba-4633-48cb-997b-5749787c952c'

        # Construct a dict representation of a GatewayMacsecConfigPatchTemplateFallbackCak model
        gateway_macsec_config_patch_template_fallback_cak_model = {}
        gateway_macsec_config_patch_template_fallback_cak_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a dict representation of a GatewayMacsecConfigPatchTemplatePrimaryCak model
        gateway_macsec_config_patch_template_primary_cak_model = {}
        gateway_macsec_config_patch_template_primary_cak_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a dict representation of a GatewayMacsecConfigPatchTemplate model
        gateway_macsec_config_patch_template_model = {}
        gateway_macsec_config_patch_template_model['active'] = True
        gateway_macsec_config_patch_template_model['fallback_cak'] = gateway_macsec_config_patch_template_fallback_cak_model
        gateway_macsec_config_patch_template_model['primary_cak'] = gateway_macsec_config_patch_template_primary_cak_model
        gateway_macsec_config_patch_template_model['window_size'] = 512

        # Set up parameter values
        id = 'testString'
        authentication_key = gateway_patch_template_authentication_key_model
        connection_mode = 'transit'
        global_ = True
        loa_reject_reason = 'The port mentioned was incorrect'
        macsec_config = gateway_macsec_config_patch_template_model
        metered = False
        name = 'testGateway'
        operational_status = 'loa_accepted'
        speed_mbps = 1000

        # Invoke method
        response = service.update_gateway(
            id,
            authentication_key=authentication_key,
            connection_mode=connection_mode,
            global_=global_,
            loa_reject_reason=loa_reject_reason,
            macsec_config=macsec_config,
            metered=metered,
            name=name,
            operational_status=operational_status,
            speed_mbps=speed_mbps,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['authentication_key'] == gateway_patch_template_authentication_key_model
        assert req_body['connection_mode'] == 'transit'
        assert req_body['global'] == True
        assert req_body['loa_reject_reason'] == 'The port mentioned was incorrect'
        assert req_body['macsec_config'] == gateway_macsec_config_patch_template_model
        assert req_body['metered'] == False
        assert req_body['name'] == 'testGateway'
        assert req_body['operational_status'] == 'loa_accepted'
        assert req_body['speed_mbps'] == 1000


    #--------------------------------------------------------
    # test_update_gateway_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_gateway_value_error(self):
        # Set up mock
        url = base_url + '/gateways/testString'
        mock_response = '{"authentication_key": {"crn": "crn:v1:bluemix:public:kms:us-south:a/766d8d374a484f029d0fca5a40a52a1c:5d343839-07d3-4213-a950-0f71ed45423f:key:7fc1a0ba-4633-48cb-997b-5749787c952c"}, "bgp_asn": 64999, "bgp_base_cidr": "bgp_base_cidr", "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "carrier_name": "myCarrierName", "change_request": {"type": "create_gateway"}, "completion_notice_reject_reason": "The completion notice file was blank", "connection_mode": "transit", "created_at": "2019-01-01T12:00:00", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::dedicated:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "cross_connect_router": "xcr01.dal03", "customer_name": "newCustomerName", "global": true, "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "link_status": "up", "location_display_name": "Dallas 03", "location_name": "dal03", "macsec_config": {"active": true, "active_cak": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222", "status": "status"}, "cipher_suite": "gcm_aes_xpn_256", "confidentiality_offset": 0, "cryptographic_algorithm": "aes_256_cmac", "fallback_cak": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222", "status": "status"}, "key_server_priority": 255, "primary_cak": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222", "status": "status"}, "sak_expiry_time": 3600, "security_policy": "must_secure", "status": "secured", "window_size": 64}, "metered": false, "name": "myGateway", "operational_status": "awaiting_completion_notice", "port": {"id": "54321b1a-fee4-41c7-9e11-9cd99e000aaa"}, "provider_api_managed": false, "resource_group": {"id": "56969d6043e9465c883cb9f7363e78e8"}, "speed_mbps": 1000, "type": "dedicated", "vlan": 10}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a GatewayPatchTemplateAuthenticationKey model
        gateway_patch_template_authentication_key_model = {}
        gateway_patch_template_authentication_key_model['crn'] = 'crn:v1:bluemix:public:kms:us-south:a/766d8d374a484f029d0fca5a40a52a1c:5d343839-07d3-4213-a950-0f71ed45423f:key:7fc1a0ba-4633-48cb-997b-5749787c952c'

        # Construct a dict representation of a GatewayMacsecConfigPatchTemplateFallbackCak model
        gateway_macsec_config_patch_template_fallback_cak_model = {}
        gateway_macsec_config_patch_template_fallback_cak_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a dict representation of a GatewayMacsecConfigPatchTemplatePrimaryCak model
        gateway_macsec_config_patch_template_primary_cak_model = {}
        gateway_macsec_config_patch_template_primary_cak_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a dict representation of a GatewayMacsecConfigPatchTemplate model
        gateway_macsec_config_patch_template_model = {}
        gateway_macsec_config_patch_template_model['active'] = True
        gateway_macsec_config_patch_template_model['fallback_cak'] = gateway_macsec_config_patch_template_fallback_cak_model
        gateway_macsec_config_patch_template_model['primary_cak'] = gateway_macsec_config_patch_template_primary_cak_model
        gateway_macsec_config_patch_template_model['window_size'] = 512

        # Set up parameter values
        id = 'testString'
        authentication_key = gateway_patch_template_authentication_key_model
        connection_mode = 'transit'
        global_ = True
        loa_reject_reason = 'The port mentioned was incorrect'
        macsec_config = gateway_macsec_config_patch_template_model
        metered = False
        name = 'testGateway'
        operational_status = 'loa_accepted'
        speed_mbps = 1000

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_gateway(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for create_gateway_action
#-----------------------------------------------------------------------------
class TestCreateGatewayAction():

    #--------------------------------------------------------
    # create_gateway_action()
    #--------------------------------------------------------
    @responses.activate
    def test_create_gateway_action_all_params(self):
        # Set up mock
        url = base_url + '/gateways/testString/actions'
        mock_response = '{"authentication_key": {"crn": "crn:v1:bluemix:public:kms:us-south:a/766d8d374a484f029d0fca5a40a52a1c:5d343839-07d3-4213-a950-0f71ed45423f:key:7fc1a0ba-4633-48cb-997b-5749787c952c"}, "bgp_asn": 64999, "bgp_base_cidr": "bgp_base_cidr", "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "carrier_name": "myCarrierName", "change_request": {"type": "create_gateway"}, "completion_notice_reject_reason": "The completion notice file was blank", "connection_mode": "transit", "created_at": "2019-01-01T12:00:00", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::dedicated:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "cross_connect_router": "xcr01.dal03", "customer_name": "newCustomerName", "global": true, "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "link_status": "up", "location_display_name": "Dallas 03", "location_name": "dal03", "macsec_config": {"active": true, "active_cak": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222", "status": "status"}, "cipher_suite": "gcm_aes_xpn_256", "confidentiality_offset": 0, "cryptographic_algorithm": "aes_256_cmac", "fallback_cak": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222", "status": "status"}, "key_server_priority": 255, "primary_cak": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222", "status": "status"}, "sak_expiry_time": 3600, "security_policy": "must_secure", "status": "secured", "window_size": 64}, "metered": false, "name": "myGateway", "operational_status": "awaiting_completion_notice", "port": {"id": "54321b1a-fee4-41c7-9e11-9cd99e000aaa"}, "provider_api_managed": false, "resource_group": {"id": "56969d6043e9465c883cb9f7363e78e8"}, "speed_mbps": 1000, "type": "dedicated", "vlan": 10}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a GatewayActionTemplateAuthenticationKey model
        gateway_action_template_authentication_key_model = {}
        gateway_action_template_authentication_key_model['crn'] = 'crn:v1:bluemix:public:kms:us-south:a/766d8d374a484f029d0fca5a40a52a1c:5d343839-07d3-4213-a950-0f71ed45423f:key:7fc1a0ba-4633-48cb-997b-5749787c952c'

        # Construct a dict representation of a ResourceGroupIdentity model
        resource_group_identity_model = {}
        resource_group_identity_model['id'] = '56969d6043e9465c883cb9f7363e78e8'

        # Set up parameter values
        id = 'testString'
        action = 'create_gateway_approve'
        authentication_key = gateway_action_template_authentication_key_model
        connection_mode = 'transit'
        global_ = True
        metered = False
        resource_group = resource_group_identity_model
        updates = [{ 'foo': 'bar' }]

        # Invoke method
        response = service.create_gateway_action(
            id,
            action,
            authentication_key=authentication_key,
            connection_mode=connection_mode,
            global_=global_,
            metered=metered,
            resource_group=resource_group,
            updates=updates,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['action'] == 'create_gateway_approve'
        assert req_body['authentication_key'] == gateway_action_template_authentication_key_model
        assert req_body['connection_mode'] == 'transit'
        assert req_body['global'] == True
        assert req_body['metered'] == False
        assert req_body['resource_group'] == resource_group_identity_model
        assert req_body['updates'] == [{ 'foo': 'bar' }]


    #--------------------------------------------------------
    # test_create_gateway_action_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_gateway_action_value_error(self):
        # Set up mock
        url = base_url + '/gateways/testString/actions'
        mock_response = '{"authentication_key": {"crn": "crn:v1:bluemix:public:kms:us-south:a/766d8d374a484f029d0fca5a40a52a1c:5d343839-07d3-4213-a950-0f71ed45423f:key:7fc1a0ba-4633-48cb-997b-5749787c952c"}, "bgp_asn": 64999, "bgp_base_cidr": "bgp_base_cidr", "bgp_cer_cidr": "10.254.30.78/30", "bgp_ibm_asn": 13884, "bgp_ibm_cidr": "10.254.30.77/30", "bgp_status": "active", "carrier_name": "myCarrierName", "change_request": {"type": "create_gateway"}, "completion_notice_reject_reason": "The completion notice file was blank", "connection_mode": "transit", "created_at": "2019-01-01T12:00:00", "crn": "crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::dedicated:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "cross_connect_router": "xcr01.dal03", "customer_name": "newCustomerName", "global": true, "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "link_status": "up", "location_display_name": "Dallas 03", "location_name": "dal03", "macsec_config": {"active": true, "active_cak": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222", "status": "status"}, "cipher_suite": "gcm_aes_xpn_256", "confidentiality_offset": 0, "cryptographic_algorithm": "aes_256_cmac", "fallback_cak": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222", "status": "status"}, "key_server_priority": 255, "primary_cak": {"crn": "crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222", "status": "status"}, "sak_expiry_time": 3600, "security_policy": "must_secure", "status": "secured", "window_size": 64}, "metered": false, "name": "myGateway", "operational_status": "awaiting_completion_notice", "port": {"id": "54321b1a-fee4-41c7-9e11-9cd99e000aaa"}, "provider_api_managed": false, "resource_group": {"id": "56969d6043e9465c883cb9f7363e78e8"}, "speed_mbps": 1000, "type": "dedicated", "vlan": 10}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a GatewayActionTemplateAuthenticationKey model
        gateway_action_template_authentication_key_model = {}
        gateway_action_template_authentication_key_model['crn'] = 'crn:v1:bluemix:public:kms:us-south:a/766d8d374a484f029d0fca5a40a52a1c:5d343839-07d3-4213-a950-0f71ed45423f:key:7fc1a0ba-4633-48cb-997b-5749787c952c'

        # Construct a dict representation of a ResourceGroupIdentity model
        resource_group_identity_model = {}
        resource_group_identity_model['id'] = '56969d6043e9465c883cb9f7363e78e8'

        # Set up parameter values
        id = 'testString'
        action = 'create_gateway_approve'
        authentication_key = gateway_action_template_authentication_key_model
        connection_mode = 'transit'
        global_ = True
        metered = False
        resource_group = resource_group_identity_model
        updates = [{ 'foo': 'bar' }]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "action": action,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.create_gateway_action(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for list_gateway_completion_notice
#-----------------------------------------------------------------------------
class TestListGatewayCompletionNotice():

    #--------------------------------------------------------
    # list_gateway_completion_notice()
    #--------------------------------------------------------
    @responses.activate
    def test_list_gateway_completion_notice_all_params(self):
        # Set up mock
        url = base_url + '/gateways/testString/completion_notice'
        mock_response = 'Contents of response byte-stream...'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/pdf',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.list_gateway_completion_notice(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_gateway_completion_notice_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_gateway_completion_notice_value_error(self):
        # Set up mock
        url = base_url + '/gateways/testString/completion_notice'
        mock_response = 'Contents of response byte-stream...'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/pdf',
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
                service.list_gateway_completion_notice(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for create_gateway_completion_notice
#-----------------------------------------------------------------------------
class TestCreateGatewayCompletionNotice():

    #--------------------------------------------------------
    # create_gateway_completion_notice()
    #--------------------------------------------------------
    @responses.activate
    def test_create_gateway_completion_notice_all_params(self):
        # Set up mock
        url = base_url + '/gateways/testString/completion_notice'
        responses.add(responses.PUT,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'
        upload = io.BytesIO(b'This is a mock file.').getvalue()
        upload_content_type = 'testString'

        # Invoke method
        response = service.create_gateway_completion_notice(
            id,
            upload=upload,
            upload_content_type=upload_content_type,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_create_gateway_completion_notice_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_gateway_completion_notice_required_params(self):
        # Set up mock
        url = base_url + '/gateways/testString/completion_notice'
        responses.add(responses.PUT,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.create_gateway_completion_notice(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_create_gateway_completion_notice_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_gateway_completion_notice_value_error(self):
        # Set up mock
        url = base_url + '/gateways/testString/completion_notice'
        responses.add(responses.PUT,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.create_gateway_completion_notice(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for list_gateway_letter_of_authorization
#-----------------------------------------------------------------------------
class TestListGatewayLetterOfAuthorization():

    #--------------------------------------------------------
    # list_gateway_letter_of_authorization()
    #--------------------------------------------------------
    @responses.activate
    def test_list_gateway_letter_of_authorization_all_params(self):
        # Set up mock
        url = base_url + '/gateways/testString/letter_of_authorization'
        mock_response = 'Contents of response byte-stream...'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/pdf',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.list_gateway_letter_of_authorization(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_gateway_letter_of_authorization_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_gateway_letter_of_authorization_value_error(self):
        # Set up mock
        url = base_url + '/gateways/testString/letter_of_authorization'
        mock_response = 'Contents of response byte-stream...'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/pdf',
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
                service.list_gateway_letter_of_authorization(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_gateway_statistics
#-----------------------------------------------------------------------------
class TestGetGatewayStatistics():

    #--------------------------------------------------------
    # get_gateway_statistics()
    #--------------------------------------------------------
    @responses.activate
    def test_get_gateway_statistics_all_params(self):
        # Set up mock
        url = base_url + '/gateways/testString/statistics'
        mock_response = '{"statistics": [{"created_at": "2019-01-01T12:00:00", "data": "MKA statistics text...", "type": "macsec_policy"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        type = 'macsec_mka'

        # Invoke method
        response = service.get_gateway_statistics(
            id,
            type,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'type={}'.format(type) in query_string


    #--------------------------------------------------------
    # test_get_gateway_statistics_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_gateway_statistics_value_error(self):
        # Set up mock
        url = base_url + '/gateways/testString/statistics'
        mock_response = '{"statistics": [{"created_at": "2019-01-01T12:00:00", "data": "MKA statistics text...", "type": "macsec_policy"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'
        type = 'macsec_mka'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
            "type": type,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_gateway_statistics(**req_copy)



# endregion
##############################################################################
# End of Service: Gateways
##############################################################################

##############################################################################
# Start of Service: OfferingInformation
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_offering_type_locations
#-----------------------------------------------------------------------------
class TestListOfferingTypeLocations():

    #--------------------------------------------------------
    # list_offering_type_locations()
    #--------------------------------------------------------
    @responses.activate
    def test_list_offering_type_locations_all_params(self):
        # Set up mock
        url = base_url + '/offering_types/dedicated/locations'
        mock_response = '{"locations": [{"billing_location": "us", "building_colocation_owner": "MyProvider", "display_name": "Dallas 9", "location_type": "PoP", "macsec_enabled": false, "market": "Dallas", "market_geography": "N/S America", "mzr": true, "name": "dal03", "offering_type": "dedicated", "provision_enabled": true, "vpc_region": "us-south"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        offering_type = 'dedicated'

        # Invoke method
        response = service.list_offering_type_locations(
            offering_type,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_offering_type_locations_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_offering_type_locations_value_error(self):
        # Set up mock
        url = base_url + '/offering_types/dedicated/locations'
        mock_response = '{"locations": [{"billing_location": "us", "building_colocation_owner": "MyProvider", "display_name": "Dallas 9", "location_type": "PoP", "macsec_enabled": false, "market": "Dallas", "market_geography": "N/S America", "mzr": true, "name": "dal03", "offering_type": "dedicated", "provision_enabled": true, "vpc_region": "us-south"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        offering_type = 'dedicated'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "offering_type": offering_type,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_offering_type_locations(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for list_offering_type_location_cross_connect_routers
#-----------------------------------------------------------------------------
class TestListOfferingTypeLocationCrossConnectRouters():

    #--------------------------------------------------------
    # list_offering_type_location_cross_connect_routers()
    #--------------------------------------------------------
    @responses.activate
    def test_list_offering_type_location_cross_connect_routers_all_params(self):
        # Set up mock
        url = base_url + '/offering_types/dedicated/locations/testString/cross_connect_routers'
        mock_response = '{"cross_connect_routers": [{"capabilities": ["capabilities"], "router_name": "xcr01.dal03", "total_connections": 1}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        offering_type = 'dedicated'
        location_name = 'testString'

        # Invoke method
        response = service.list_offering_type_location_cross_connect_routers(
            offering_type,
            location_name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_offering_type_location_cross_connect_routers_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_offering_type_location_cross_connect_routers_value_error(self):
        # Set up mock
        url = base_url + '/offering_types/dedicated/locations/testString/cross_connect_routers'
        mock_response = '{"cross_connect_routers": [{"capabilities": ["capabilities"], "router_name": "xcr01.dal03", "total_connections": 1}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        offering_type = 'dedicated'
        location_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "offering_type": offering_type,
            "location_name": location_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_offering_type_location_cross_connect_routers(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for list_offering_type_speeds
#-----------------------------------------------------------------------------
class TestListOfferingTypeSpeeds():

    #--------------------------------------------------------
    # list_offering_type_speeds()
    #--------------------------------------------------------
    @responses.activate
    def test_list_offering_type_speeds_all_params(self):
        # Set up mock
        url = base_url + '/offering_types/dedicated/speeds'
        mock_response = '{"speeds": [{"capabilities": ["capabilities"], "link_speed": 2000, "macsec_enabled": false}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        offering_type = 'dedicated'

        # Invoke method
        response = service.list_offering_type_speeds(
            offering_type,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_offering_type_speeds_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_offering_type_speeds_value_error(self):
        # Set up mock
        url = base_url + '/offering_types/dedicated/speeds'
        mock_response = '{"speeds": [{"capabilities": ["capabilities"], "link_speed": 2000, "macsec_enabled": false}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        offering_type = 'dedicated'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "offering_type": offering_type,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_offering_type_speeds(**req_copy)



# endregion
##############################################################################
# End of Service: OfferingInformation
##############################################################################

##############################################################################
# Start of Service: Ports
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_ports
#-----------------------------------------------------------------------------
class TestListPorts():

    #--------------------------------------------------------
    # list_ports()
    #--------------------------------------------------------
    @responses.activate
    def test_list_ports_all_params(self):
        # Set up mock
        url = base_url + '/ports'
        mock_response = '{"first": {"href": "https://directlink.cloud.ibm.com/v1/ports?limit=100"}, "limit": 100, "next": {"href": "https://directlink.cloud.ibm.com/v1/ports?start=9d5a91a3e2cbd233b5a5b33436855ed1&limit=100", "start": "9d5a91a3e2cbd233b5a5b33436855ed1"}, "total_count": 132, "ports": [{"direct_link_count": 1, "id": "01122b9b-820f-4c44-8a31-77f1f0806765", "label": "XCR-FRK-CS-SEC-01", "location_display_name": "Dallas 03", "location_name": "dal03", "provider_name": "provider_1", "supported_link_speeds": [21]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        start = 'testString'
        limit = 38
        location_name = 'testString'

        # Invoke method
        response = service.list_ports(
            start=start,
            limit=limit,
            location_name=location_name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = requests.utils.unquote(query_string)
        assert 'start={}'.format(start) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'location_name={}'.format(location_name) in query_string


    #--------------------------------------------------------
    # test_list_ports_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_ports_required_params(self):
        # Set up mock
        url = base_url + '/ports'
        mock_response = '{"first": {"href": "https://directlink.cloud.ibm.com/v1/ports?limit=100"}, "limit": 100, "next": {"href": "https://directlink.cloud.ibm.com/v1/ports?start=9d5a91a3e2cbd233b5a5b33436855ed1&limit=100", "start": "9d5a91a3e2cbd233b5a5b33436855ed1"}, "total_count": 132, "ports": [{"direct_link_count": 1, "id": "01122b9b-820f-4c44-8a31-77f1f0806765", "label": "XCR-FRK-CS-SEC-01", "location_display_name": "Dallas 03", "location_name": "dal03", "provider_name": "provider_1", "supported_link_speeds": [21]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_ports()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_ports_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_ports_value_error(self):
        # Set up mock
        url = base_url + '/ports'
        mock_response = '{"first": {"href": "https://directlink.cloud.ibm.com/v1/ports?limit=100"}, "limit": 100, "next": {"href": "https://directlink.cloud.ibm.com/v1/ports?start=9d5a91a3e2cbd233b5a5b33436855ed1&limit=100", "start": "9d5a91a3e2cbd233b5a5b33436855ed1"}, "total_count": 132, "ports": [{"direct_link_count": 1, "id": "01122b9b-820f-4c44-8a31-77f1f0806765", "label": "XCR-FRK-CS-SEC-01", "location_display_name": "Dallas 03", "location_name": "dal03", "provider_name": "provider_1", "supported_link_speeds": [21]}]}'
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
                service.list_ports(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_port
#-----------------------------------------------------------------------------
class TestGetPort():

    #--------------------------------------------------------
    # get_port()
    #--------------------------------------------------------
    @responses.activate
    def test_get_port_all_params(self):
        # Set up mock
        url = base_url + '/ports/testString'
        mock_response = '{"direct_link_count": 1, "id": "01122b9b-820f-4c44-8a31-77f1f0806765", "label": "XCR-FRK-CS-SEC-01", "location_display_name": "Dallas 03", "location_name": "dal03", "provider_name": "provider_1", "supported_link_speeds": [21]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = service.get_port(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_port_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_port_value_error(self):
        # Set up mock
        url = base_url + '/ports/testString'
        mock_response = '{"direct_link_count": 1, "id": "01122b9b-820f-4c44-8a31-77f1f0806765", "label": "XCR-FRK-CS-SEC-01", "location_display_name": "Dallas 03", "location_name": "dal03", "provider_name": "provider_1", "supported_link_speeds": [21]}'
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
                service.get_port(**req_copy)



# endregion
##############################################################################
# End of Service: Ports
##############################################################################

##############################################################################
# Start of Service: VirtualConnections
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_gateway_virtual_connections
#-----------------------------------------------------------------------------
class TestListGatewayVirtualConnections():

    #--------------------------------------------------------
    # list_gateway_virtual_connections()
    #--------------------------------------------------------
    @responses.activate
    def test_list_gateway_virtual_connections_all_params(self):
        # Set up mock
        url = base_url + '/gateways/testString/virtual_connections'
        mock_response = '{"virtual_connections": [{"created_at": "2019-01-01T12:00:00", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "newVC", "network_account": "00aa14a2e0fb102c8995ebefff865555", "network_id": "crn:v1:bluemix:public:is:us-east:a/28e4d90ac7504be69447111122223333::vpc:aaa81ac8-5e96-42a0-a4b7-6c2e2d1bbbbb", "status": "attached", "type": "vpc"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        gateway_id = 'testString'

        # Invoke method
        response = service.list_gateway_virtual_connections(
            gateway_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_gateway_virtual_connections_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_gateway_virtual_connections_value_error(self):
        # Set up mock
        url = base_url + '/gateways/testString/virtual_connections'
        mock_response = '{"virtual_connections": [{"created_at": "2019-01-01T12:00:00", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "newVC", "network_account": "00aa14a2e0fb102c8995ebefff865555", "network_id": "crn:v1:bluemix:public:is:us-east:a/28e4d90ac7504be69447111122223333::vpc:aaa81ac8-5e96-42a0-a4b7-6c2e2d1bbbbb", "status": "attached", "type": "vpc"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        gateway_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "gateway_id": gateway_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_gateway_virtual_connections(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for create_gateway_virtual_connection
#-----------------------------------------------------------------------------
class TestCreateGatewayVirtualConnection():

    #--------------------------------------------------------
    # create_gateway_virtual_connection()
    #--------------------------------------------------------
    @responses.activate
    def test_create_gateway_virtual_connection_all_params(self):
        # Set up mock
        url = base_url + '/gateways/testString/virtual_connections'
        mock_response = '{"created_at": "2019-01-01T12:00:00", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "newVC", "network_account": "00aa14a2e0fb102c8995ebefff865555", "network_id": "crn:v1:bluemix:public:is:us-east:a/28e4d90ac7504be69447111122223333::vpc:aaa81ac8-5e96-42a0-a4b7-6c2e2d1bbbbb", "status": "attached", "type": "vpc"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        gateway_id = 'testString'
        name = 'newVC'
        type = 'vpc'
        network_id = 'crn:v1:bluemix:public:is:us-east:a/28e4d90ac7504be69447111122223333::vpc:aaa81ac8-5e96-42a0-a4b7-6c2e2d1bbbbb'

        # Invoke method
        response = service.create_gateway_virtual_connection(
            gateway_id,
            name,
            type,
            network_id=network_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'newVC'
        assert req_body['type'] == 'vpc'
        assert req_body['network_id'] == 'crn:v1:bluemix:public:is:us-east:a/28e4d90ac7504be69447111122223333::vpc:aaa81ac8-5e96-42a0-a4b7-6c2e2d1bbbbb'


    #--------------------------------------------------------
    # test_create_gateway_virtual_connection_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_create_gateway_virtual_connection_value_error(self):
        # Set up mock
        url = base_url + '/gateways/testString/virtual_connections'
        mock_response = '{"created_at": "2019-01-01T12:00:00", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "newVC", "network_account": "00aa14a2e0fb102c8995ebefff865555", "network_id": "crn:v1:bluemix:public:is:us-east:a/28e4d90ac7504be69447111122223333::vpc:aaa81ac8-5e96-42a0-a4b7-6c2e2d1bbbbb", "status": "attached", "type": "vpc"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        gateway_id = 'testString'
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
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.create_gateway_virtual_connection(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_gateway_virtual_connection
#-----------------------------------------------------------------------------
class TestDeleteGatewayVirtualConnection():

    #--------------------------------------------------------
    # delete_gateway_virtual_connection()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_gateway_virtual_connection_all_params(self):
        # Set up mock
        url = base_url + '/gateways/testString/virtual_connections/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        gateway_id = 'testString'
        id = 'testString'

        # Invoke method
        response = service.delete_gateway_virtual_connection(
            gateway_id,
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    #--------------------------------------------------------
    # test_delete_gateway_virtual_connection_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_gateway_virtual_connection_value_error(self):
        # Set up mock
        url = base_url + '/gateways/testString/virtual_connections/testString'
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        gateway_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "gateway_id": gateway_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_gateway_virtual_connection(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_gateway_virtual_connection
#-----------------------------------------------------------------------------
class TestGetGatewayVirtualConnection():

    #--------------------------------------------------------
    # get_gateway_virtual_connection()
    #--------------------------------------------------------
    @responses.activate
    def test_get_gateway_virtual_connection_all_params(self):
        # Set up mock
        url = base_url + '/gateways/testString/virtual_connections/testString'
        mock_response = '{"created_at": "2019-01-01T12:00:00", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "newVC", "network_account": "00aa14a2e0fb102c8995ebefff865555", "network_id": "crn:v1:bluemix:public:is:us-east:a/28e4d90ac7504be69447111122223333::vpc:aaa81ac8-5e96-42a0-a4b7-6c2e2d1bbbbb", "status": "attached", "type": "vpc"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        gateway_id = 'testString'
        id = 'testString'

        # Invoke method
        response = service.get_gateway_virtual_connection(
            gateway_id,
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_gateway_virtual_connection_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_gateway_virtual_connection_value_error(self):
        # Set up mock
        url = base_url + '/gateways/testString/virtual_connections/testString'
        mock_response = '{"created_at": "2019-01-01T12:00:00", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "newVC", "network_account": "00aa14a2e0fb102c8995ebefff865555", "network_id": "crn:v1:bluemix:public:is:us-east:a/28e4d90ac7504be69447111122223333::vpc:aaa81ac8-5e96-42a0-a4b7-6c2e2d1bbbbb", "status": "attached", "type": "vpc"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        gateway_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "gateway_id": gateway_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_gateway_virtual_connection(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_gateway_virtual_connection
#-----------------------------------------------------------------------------
class TestUpdateGatewayVirtualConnection():

    #--------------------------------------------------------
    # update_gateway_virtual_connection()
    #--------------------------------------------------------
    @responses.activate
    def test_update_gateway_virtual_connection_all_params(self):
        # Set up mock
        url = base_url + '/gateways/testString/virtual_connections/testString'
        mock_response = '{"created_at": "2019-01-01T12:00:00", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "newVC", "network_account": "00aa14a2e0fb102c8995ebefff865555", "network_id": "crn:v1:bluemix:public:is:us-east:a/28e4d90ac7504be69447111122223333::vpc:aaa81ac8-5e96-42a0-a4b7-6c2e2d1bbbbb", "status": "attached", "type": "vpc"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        gateway_id = 'testString'
        id = 'testString'
        name = 'newConnectionName'
        status = 'attached'

        # Invoke method
        response = service.update_gateway_virtual_connection(
            gateway_id,
            id,
            name=name,
            status=status,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'newConnectionName'
        assert req_body['status'] == 'attached'


    #--------------------------------------------------------
    # test_update_gateway_virtual_connection_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_gateway_virtual_connection_value_error(self):
        # Set up mock
        url = base_url + '/gateways/testString/virtual_connections/testString'
        mock_response = '{"created_at": "2019-01-01T12:00:00", "id": "ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4", "name": "newVC", "network_account": "00aa14a2e0fb102c8995ebefff865555", "network_id": "crn:v1:bluemix:public:is:us-east:a/28e4d90ac7504be69447111122223333::vpc:aaa81ac8-5e96-42a0-a4b7-6c2e2d1bbbbb", "status": "attached", "type": "vpc"}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        gateway_id = 'testString'
        id = 'testString'
        name = 'newConnectionName'
        status = 'attached'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "gateway_id": gateway_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_gateway_virtual_connection(**req_copy)



# endregion
##############################################################################
# End of Service: VirtualConnections
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for CrossConnectRouter
#-----------------------------------------------------------------------------
class TestCrossConnectRouter():

    #--------------------------------------------------------
    # Test serialization/deserialization for CrossConnectRouter
    #--------------------------------------------------------
    def test_cross_connect_router_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for Gateway
#-----------------------------------------------------------------------------
class TestGateway():

    #--------------------------------------------------------
    # Test serialization/deserialization for Gateway
    #--------------------------------------------------------
    def test_gateway_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        gateway_macsec_config_active_cak_model = {} # GatewayMacsecConfigActiveCak
        gateway_macsec_config_active_cak_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'
        gateway_macsec_config_active_cak_model['status'] = 'testString'

        gateway_macsec_config_fallback_cak_model = {} # GatewayMacsecConfigFallbackCak
        gateway_macsec_config_fallback_cak_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'
        gateway_macsec_config_fallback_cak_model['status'] = 'testString'

        gateway_macsec_config_primary_cak_model = {} # GatewayMacsecConfigPrimaryCak
        gateway_macsec_config_primary_cak_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'
        gateway_macsec_config_primary_cak_model['status'] = 'testString'

        gateway_authentication_key_model = {} # GatewayAuthenticationKey
        gateway_authentication_key_model['crn'] = 'crn:v1:bluemix:public:kms:us-south:a/766d8d374a484f029d0fca5a40a52a1c:5d343839-07d3-4213-a950-0f71ed45423f:key:7fc1a0ba-4633-48cb-997b-5749787c952c'

        gateway_change_request_model = {} # GatewayChangeRequest
        gateway_change_request_model['type'] = 'create_gateway'

        gateway_macsec_config_model = {} # GatewayMacsecConfig
        gateway_macsec_config_model['active'] = True
        gateway_macsec_config_model['active_cak'] = gateway_macsec_config_active_cak_model
        gateway_macsec_config_model['cipher_suite'] = 'gcm_aes_xpn_256'
        gateway_macsec_config_model['confidentiality_offset'] = 0
        gateway_macsec_config_model['cryptographic_algorithm'] = 'aes_256_cmac'
        gateway_macsec_config_model['fallback_cak'] = gateway_macsec_config_fallback_cak_model
        gateway_macsec_config_model['key_server_priority'] = 255
        gateway_macsec_config_model['primary_cak'] = gateway_macsec_config_primary_cak_model
        gateway_macsec_config_model['sak_expiry_time'] = 3600
        gateway_macsec_config_model['security_policy'] = 'must_secure'
        gateway_macsec_config_model['status'] = 'secured'
        gateway_macsec_config_model['window_size'] = 64

        gateway_port_model = {} # GatewayPort
        gateway_port_model['id'] = '54321b1a-fee4-41c7-9e11-9cd99e000aaa'

        resource_group_reference_model = {} # ResourceGroupReference
        resource_group_reference_model['id'] = '56969d6043e9465c883cb9f7363e78e8'

        # Construct a json representation of a Gateway model
        gateway_model_json = {}
        gateway_model_json['authentication_key'] = gateway_authentication_key_model
        gateway_model_json['bgp_asn'] = 64999
        gateway_model_json['bgp_base_cidr'] = 'testString'
        gateway_model_json['bgp_cer_cidr'] = '10.254.30.78/30'
        gateway_model_json['bgp_ibm_asn'] = 13884
        gateway_model_json['bgp_ibm_cidr'] = '10.254.30.77/30'
        gateway_model_json['bgp_status'] = 'active'
        gateway_model_json['carrier_name'] = 'myCarrierName'
        gateway_model_json['change_request'] = gateway_change_request_model
        gateway_model_json['completion_notice_reject_reason'] = 'The completion notice file was blank'
        gateway_model_json['connection_mode'] = 'transit'
        gateway_model_json['created_at'] = '2020-01-28T18:40:40.123456Z'
        gateway_model_json['crn'] = 'crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::dedicated:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        gateway_model_json['cross_connect_router'] = 'xcr01.dal03'
        gateway_model_json['customer_name'] = 'newCustomerName'
        gateway_model_json['global'] = True
        gateway_model_json['id'] = 'ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        gateway_model_json['link_status'] = 'up'
        gateway_model_json['location_display_name'] = 'Dallas 03'
        gateway_model_json['location_name'] = 'dal03'
        gateway_model_json['macsec_config'] = gateway_macsec_config_model
        gateway_model_json['metered'] = False
        gateway_model_json['name'] = 'myGateway'
        gateway_model_json['operational_status'] = 'awaiting_completion_notice'
        gateway_model_json['port'] = gateway_port_model
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

#-----------------------------------------------------------------------------
# Test Class for GatewayActionTemplateAuthenticationKey
#-----------------------------------------------------------------------------
class TestGatewayActionTemplateAuthenticationKey():

    #--------------------------------------------------------
    # Test serialization/deserialization for GatewayActionTemplateAuthenticationKey
    #--------------------------------------------------------
    def test_gateway_action_template_authentication_key_serialization(self):

        # Construct a json representation of a GatewayActionTemplateAuthenticationKey model
        gateway_action_template_authentication_key_model_json = {}
        gateway_action_template_authentication_key_model_json['crn'] = 'crn:v1:bluemix:public:kms:us-south:a/766d8d374a484f029d0fca5a40a52a1c:5d343839-07d3-4213-a950-0f71ed45423f:key:7fc1a0ba-4633-48cb-997b-5749787c952c'

        # Construct a model instance of GatewayActionTemplateAuthenticationKey by calling from_dict on the json representation
        gateway_action_template_authentication_key_model = GatewayActionTemplateAuthenticationKey.from_dict(gateway_action_template_authentication_key_model_json)
        assert gateway_action_template_authentication_key_model != False

        # Construct a model instance of GatewayActionTemplateAuthenticationKey by calling from_dict on the json representation
        gateway_action_template_authentication_key_model_dict = GatewayActionTemplateAuthenticationKey.from_dict(gateway_action_template_authentication_key_model_json).__dict__
        gateway_action_template_authentication_key_model2 = GatewayActionTemplateAuthenticationKey(**gateway_action_template_authentication_key_model_dict)

        # Verify the model instances are equivalent
        assert gateway_action_template_authentication_key_model == gateway_action_template_authentication_key_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_action_template_authentication_key_model_json2 = gateway_action_template_authentication_key_model.to_dict()
        assert gateway_action_template_authentication_key_model_json2 == gateway_action_template_authentication_key_model_json

#-----------------------------------------------------------------------------
# Test Class for GatewayAuthenticationKey
#-----------------------------------------------------------------------------
class TestGatewayAuthenticationKey():

    #--------------------------------------------------------
    # Test serialization/deserialization for GatewayAuthenticationKey
    #--------------------------------------------------------
    def test_gateway_authentication_key_serialization(self):

        # Construct a json representation of a GatewayAuthenticationKey model
        gateway_authentication_key_model_json = {}
        gateway_authentication_key_model_json['crn'] = 'crn:v1:bluemix:public:kms:us-south:a/766d8d374a484f029d0fca5a40a52a1c:5d343839-07d3-4213-a950-0f71ed45423f:key:7fc1a0ba-4633-48cb-997b-5749787c952c'

        # Construct a model instance of GatewayAuthenticationKey by calling from_dict on the json representation
        gateway_authentication_key_model = GatewayAuthenticationKey.from_dict(gateway_authentication_key_model_json)
        assert gateway_authentication_key_model != False

        # Construct a model instance of GatewayAuthenticationKey by calling from_dict on the json representation
        gateway_authentication_key_model_dict = GatewayAuthenticationKey.from_dict(gateway_authentication_key_model_json).__dict__
        gateway_authentication_key_model2 = GatewayAuthenticationKey(**gateway_authentication_key_model_dict)

        # Verify the model instances are equivalent
        assert gateway_authentication_key_model == gateway_authentication_key_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_authentication_key_model_json2 = gateway_authentication_key_model.to_dict()
        assert gateway_authentication_key_model_json2 == gateway_authentication_key_model_json

#-----------------------------------------------------------------------------
# Test Class for GatewayCollection
#-----------------------------------------------------------------------------
class TestGatewayCollection():

    #--------------------------------------------------------
    # Test serialization/deserialization for GatewayCollection
    #--------------------------------------------------------
    def test_gateway_collection_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        gateway_macsec_config_active_cak_model = {} # GatewayMacsecConfigActiveCak
        gateway_macsec_config_active_cak_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'
        gateway_macsec_config_active_cak_model['status'] = 'testString'

        gateway_macsec_config_fallback_cak_model = {} # GatewayMacsecConfigFallbackCak
        gateway_macsec_config_fallback_cak_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'
        gateway_macsec_config_fallback_cak_model['status'] = 'testString'

        gateway_macsec_config_primary_cak_model = {} # GatewayMacsecConfigPrimaryCak
        gateway_macsec_config_primary_cak_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'
        gateway_macsec_config_primary_cak_model['status'] = 'testString'

        gateway_authentication_key_model = {} # GatewayAuthenticationKey
        gateway_authentication_key_model['crn'] = 'crn:v1:bluemix:public:kms:us-south:a/766d8d374a484f029d0fca5a40a52a1c:5d343839-07d3-4213-a950-0f71ed45423f:key:7fc1a0ba-4633-48cb-997b-5749787c952c'

        gateway_change_request_model = {} # GatewayChangeRequest
        gateway_change_request_model['type'] = 'create_gateway'

        gateway_macsec_config_model = {} # GatewayMacsecConfig
        gateway_macsec_config_model['active'] = True
        gateway_macsec_config_model['active_cak'] = gateway_macsec_config_active_cak_model
        gateway_macsec_config_model['cipher_suite'] = 'gcm_aes_xpn_256'
        gateway_macsec_config_model['confidentiality_offset'] = 0
        gateway_macsec_config_model['cryptographic_algorithm'] = 'aes_256_cmac'
        gateway_macsec_config_model['fallback_cak'] = gateway_macsec_config_fallback_cak_model
        gateway_macsec_config_model['key_server_priority'] = 255
        gateway_macsec_config_model['primary_cak'] = gateway_macsec_config_primary_cak_model
        gateway_macsec_config_model['sak_expiry_time'] = 3600
        gateway_macsec_config_model['security_policy'] = 'must_secure'
        gateway_macsec_config_model['status'] = 'secured'
        gateway_macsec_config_model['window_size'] = 64

        gateway_port_model = {} # GatewayPort
        gateway_port_model['id'] = '54321b1a-fee4-41c7-9e11-9cd99e000aaa'

        resource_group_reference_model = {} # ResourceGroupReference
        resource_group_reference_model['id'] = '56969d6043e9465c883cb9f7363e78e8'

        gateway_model = {} # Gateway
        gateway_model['authentication_key'] = gateway_authentication_key_model
        gateway_model['bgp_asn'] = 64999
        gateway_model['bgp_base_cidr'] = 'testString'
        gateway_model['bgp_cer_cidr'] = '10.254.30.78/30'
        gateway_model['bgp_ibm_asn'] = 13884
        gateway_model['bgp_ibm_cidr'] = '10.254.30.77/30'
        gateway_model['bgp_status'] = 'active'
        gateway_model['carrier_name'] = 'myCarrierName'
        gateway_model['change_request'] = gateway_change_request_model
        gateway_model['completion_notice_reject_reason'] = 'The completion notice file was blank'
        gateway_model['connection_mode'] = 'transit'
        gateway_model['created_at'] = '2020-01-28T18:40:40.123456Z'
        gateway_model['crn'] = 'crn:v1:bluemix:public:directlink:dal03:a/4111d05f36894e3cb9b46a43556d9000::dedicated:ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        gateway_model['cross_connect_router'] = 'xcr01.dal03'
        gateway_model['customer_name'] = 'newCustomerName'
        gateway_model['global'] = True
        gateway_model['id'] = 'ef4dcb1a-fee4-41c7-9e11-9cd99e65c1f4'
        gateway_model['link_status'] = 'up'
        gateway_model['location_display_name'] = 'Dallas 03'
        gateway_model['location_name'] = 'dal03'
        gateway_model['macsec_config'] = gateway_macsec_config_model
        gateway_model['metered'] = False
        gateway_model['name'] = 'myGateway'
        gateway_model['operational_status'] = 'awaiting_completion_notice'
        gateway_model['port'] = gateway_port_model
        gateway_model['provider_api_managed'] = False
        gateway_model['resource_group'] = resource_group_reference_model
        gateway_model['speed_mbps'] = 1000
        gateway_model['type'] = 'dedicated'
        gateway_model['vlan'] = 10

        # Construct a json representation of a GatewayCollection model
        gateway_collection_model_json = {}
        gateway_collection_model_json['gateways'] = [gateway_model]

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

#-----------------------------------------------------------------------------
# Test Class for GatewayMacsecConfig
#-----------------------------------------------------------------------------
class TestGatewayMacsecConfig():

    #--------------------------------------------------------
    # Test serialization/deserialization for GatewayMacsecConfig
    #--------------------------------------------------------
    def test_gateway_macsec_config_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        gateway_macsec_config_active_cak_model = {} # GatewayMacsecConfigActiveCak
        gateway_macsec_config_active_cak_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'
        gateway_macsec_config_active_cak_model['status'] = 'testString'

        gateway_macsec_config_fallback_cak_model = {} # GatewayMacsecConfigFallbackCak
        gateway_macsec_config_fallback_cak_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'
        gateway_macsec_config_fallback_cak_model['status'] = 'testString'

        gateway_macsec_config_primary_cak_model = {} # GatewayMacsecConfigPrimaryCak
        gateway_macsec_config_primary_cak_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'
        gateway_macsec_config_primary_cak_model['status'] = 'testString'

        # Construct a json representation of a GatewayMacsecConfig model
        gateway_macsec_config_model_json = {}
        gateway_macsec_config_model_json['active'] = True
        gateway_macsec_config_model_json['active_cak'] = gateway_macsec_config_active_cak_model
        gateway_macsec_config_model_json['cipher_suite'] = 'gcm_aes_xpn_256'
        gateway_macsec_config_model_json['confidentiality_offset'] = 0
        gateway_macsec_config_model_json['cryptographic_algorithm'] = 'aes_256_cmac'
        gateway_macsec_config_model_json['fallback_cak'] = gateway_macsec_config_fallback_cak_model
        gateway_macsec_config_model_json['key_server_priority'] = 255
        gateway_macsec_config_model_json['primary_cak'] = gateway_macsec_config_primary_cak_model
        gateway_macsec_config_model_json['sak_expiry_time'] = 3600
        gateway_macsec_config_model_json['security_policy'] = 'must_secure'
        gateway_macsec_config_model_json['status'] = 'secured'
        gateway_macsec_config_model_json['window_size'] = 64

        # Construct a model instance of GatewayMacsecConfig by calling from_dict on the json representation
        gateway_macsec_config_model = GatewayMacsecConfig.from_dict(gateway_macsec_config_model_json)
        assert gateway_macsec_config_model != False

        # Construct a model instance of GatewayMacsecConfig by calling from_dict on the json representation
        gateway_macsec_config_model_dict = GatewayMacsecConfig.from_dict(gateway_macsec_config_model_json).__dict__
        gateway_macsec_config_model2 = GatewayMacsecConfig(**gateway_macsec_config_model_dict)

        # Verify the model instances are equivalent
        assert gateway_macsec_config_model == gateway_macsec_config_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_macsec_config_model_json2 = gateway_macsec_config_model.to_dict()
        assert gateway_macsec_config_model_json2 == gateway_macsec_config_model_json

#-----------------------------------------------------------------------------
# Test Class for GatewayMacsecConfigActiveCak
#-----------------------------------------------------------------------------
class TestGatewayMacsecConfigActiveCak():

    #--------------------------------------------------------
    # Test serialization/deserialization for GatewayMacsecConfigActiveCak
    #--------------------------------------------------------
    def test_gateway_macsec_config_active_cak_serialization(self):

        # Construct a json representation of a GatewayMacsecConfigActiveCak model
        gateway_macsec_config_active_cak_model_json = {}
        gateway_macsec_config_active_cak_model_json['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'
        gateway_macsec_config_active_cak_model_json['status'] = 'testString'

        # Construct a model instance of GatewayMacsecConfigActiveCak by calling from_dict on the json representation
        gateway_macsec_config_active_cak_model = GatewayMacsecConfigActiveCak.from_dict(gateway_macsec_config_active_cak_model_json)
        assert gateway_macsec_config_active_cak_model != False

        # Construct a model instance of GatewayMacsecConfigActiveCak by calling from_dict on the json representation
        gateway_macsec_config_active_cak_model_dict = GatewayMacsecConfigActiveCak.from_dict(gateway_macsec_config_active_cak_model_json).__dict__
        gateway_macsec_config_active_cak_model2 = GatewayMacsecConfigActiveCak(**gateway_macsec_config_active_cak_model_dict)

        # Verify the model instances are equivalent
        assert gateway_macsec_config_active_cak_model == gateway_macsec_config_active_cak_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_macsec_config_active_cak_model_json2 = gateway_macsec_config_active_cak_model.to_dict()
        assert gateway_macsec_config_active_cak_model_json2 == gateway_macsec_config_active_cak_model_json

#-----------------------------------------------------------------------------
# Test Class for GatewayMacsecConfigFallbackCak
#-----------------------------------------------------------------------------
class TestGatewayMacsecConfigFallbackCak():

    #--------------------------------------------------------
    # Test serialization/deserialization for GatewayMacsecConfigFallbackCak
    #--------------------------------------------------------
    def test_gateway_macsec_config_fallback_cak_serialization(self):

        # Construct a json representation of a GatewayMacsecConfigFallbackCak model
        gateway_macsec_config_fallback_cak_model_json = {}
        gateway_macsec_config_fallback_cak_model_json['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'
        gateway_macsec_config_fallback_cak_model_json['status'] = 'testString'

        # Construct a model instance of GatewayMacsecConfigFallbackCak by calling from_dict on the json representation
        gateway_macsec_config_fallback_cak_model = GatewayMacsecConfigFallbackCak.from_dict(gateway_macsec_config_fallback_cak_model_json)
        assert gateway_macsec_config_fallback_cak_model != False

        # Construct a model instance of GatewayMacsecConfigFallbackCak by calling from_dict on the json representation
        gateway_macsec_config_fallback_cak_model_dict = GatewayMacsecConfigFallbackCak.from_dict(gateway_macsec_config_fallback_cak_model_json).__dict__
        gateway_macsec_config_fallback_cak_model2 = GatewayMacsecConfigFallbackCak(**gateway_macsec_config_fallback_cak_model_dict)

        # Verify the model instances are equivalent
        assert gateway_macsec_config_fallback_cak_model == gateway_macsec_config_fallback_cak_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_macsec_config_fallback_cak_model_json2 = gateway_macsec_config_fallback_cak_model.to_dict()
        assert gateway_macsec_config_fallback_cak_model_json2 == gateway_macsec_config_fallback_cak_model_json

#-----------------------------------------------------------------------------
# Test Class for GatewayMacsecConfigPatchTemplate
#-----------------------------------------------------------------------------
class TestGatewayMacsecConfigPatchTemplate():

    #--------------------------------------------------------
    # Test serialization/deserialization for GatewayMacsecConfigPatchTemplate
    #--------------------------------------------------------
    def test_gateway_macsec_config_patch_template_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        gateway_macsec_config_patch_template_fallback_cak_model = {} # GatewayMacsecConfigPatchTemplateFallbackCak
        gateway_macsec_config_patch_template_fallback_cak_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        gateway_macsec_config_patch_template_primary_cak_model = {} # GatewayMacsecConfigPatchTemplatePrimaryCak
        gateway_macsec_config_patch_template_primary_cak_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a json representation of a GatewayMacsecConfigPatchTemplate model
        gateway_macsec_config_patch_template_model_json = {}
        gateway_macsec_config_patch_template_model_json['active'] = True
        gateway_macsec_config_patch_template_model_json['fallback_cak'] = gateway_macsec_config_patch_template_fallback_cak_model
        gateway_macsec_config_patch_template_model_json['primary_cak'] = gateway_macsec_config_patch_template_primary_cak_model
        gateway_macsec_config_patch_template_model_json['window_size'] = 512

        # Construct a model instance of GatewayMacsecConfigPatchTemplate by calling from_dict on the json representation
        gateway_macsec_config_patch_template_model = GatewayMacsecConfigPatchTemplate.from_dict(gateway_macsec_config_patch_template_model_json)
        assert gateway_macsec_config_patch_template_model != False

        # Construct a model instance of GatewayMacsecConfigPatchTemplate by calling from_dict on the json representation
        gateway_macsec_config_patch_template_model_dict = GatewayMacsecConfigPatchTemplate.from_dict(gateway_macsec_config_patch_template_model_json).__dict__
        gateway_macsec_config_patch_template_model2 = GatewayMacsecConfigPatchTemplate(**gateway_macsec_config_patch_template_model_dict)

        # Verify the model instances are equivalent
        assert gateway_macsec_config_patch_template_model == gateway_macsec_config_patch_template_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_macsec_config_patch_template_model_json2 = gateway_macsec_config_patch_template_model.to_dict()
        assert gateway_macsec_config_patch_template_model_json2 == gateway_macsec_config_patch_template_model_json

#-----------------------------------------------------------------------------
# Test Class for GatewayMacsecConfigPatchTemplateFallbackCak
#-----------------------------------------------------------------------------
class TestGatewayMacsecConfigPatchTemplateFallbackCak():

    #--------------------------------------------------------
    # Test serialization/deserialization for GatewayMacsecConfigPatchTemplateFallbackCak
    #--------------------------------------------------------
    def test_gateway_macsec_config_patch_template_fallback_cak_serialization(self):

        # Construct a json representation of a GatewayMacsecConfigPatchTemplateFallbackCak model
        gateway_macsec_config_patch_template_fallback_cak_model_json = {}
        gateway_macsec_config_patch_template_fallback_cak_model_json['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a model instance of GatewayMacsecConfigPatchTemplateFallbackCak by calling from_dict on the json representation
        gateway_macsec_config_patch_template_fallback_cak_model = GatewayMacsecConfigPatchTemplateFallbackCak.from_dict(gateway_macsec_config_patch_template_fallback_cak_model_json)
        assert gateway_macsec_config_patch_template_fallback_cak_model != False

        # Construct a model instance of GatewayMacsecConfigPatchTemplateFallbackCak by calling from_dict on the json representation
        gateway_macsec_config_patch_template_fallback_cak_model_dict = GatewayMacsecConfigPatchTemplateFallbackCak.from_dict(gateway_macsec_config_patch_template_fallback_cak_model_json).__dict__
        gateway_macsec_config_patch_template_fallback_cak_model2 = GatewayMacsecConfigPatchTemplateFallbackCak(**gateway_macsec_config_patch_template_fallback_cak_model_dict)

        # Verify the model instances are equivalent
        assert gateway_macsec_config_patch_template_fallback_cak_model == gateway_macsec_config_patch_template_fallback_cak_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_macsec_config_patch_template_fallback_cak_model_json2 = gateway_macsec_config_patch_template_fallback_cak_model.to_dict()
        assert gateway_macsec_config_patch_template_fallback_cak_model_json2 == gateway_macsec_config_patch_template_fallback_cak_model_json

#-----------------------------------------------------------------------------
# Test Class for GatewayMacsecConfigPatchTemplatePrimaryCak
#-----------------------------------------------------------------------------
class TestGatewayMacsecConfigPatchTemplatePrimaryCak():

    #--------------------------------------------------------
    # Test serialization/deserialization for GatewayMacsecConfigPatchTemplatePrimaryCak
    #--------------------------------------------------------
    def test_gateway_macsec_config_patch_template_primary_cak_serialization(self):

        # Construct a json representation of a GatewayMacsecConfigPatchTemplatePrimaryCak model
        gateway_macsec_config_patch_template_primary_cak_model_json = {}
        gateway_macsec_config_patch_template_primary_cak_model_json['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a model instance of GatewayMacsecConfigPatchTemplatePrimaryCak by calling from_dict on the json representation
        gateway_macsec_config_patch_template_primary_cak_model = GatewayMacsecConfigPatchTemplatePrimaryCak.from_dict(gateway_macsec_config_patch_template_primary_cak_model_json)
        assert gateway_macsec_config_patch_template_primary_cak_model != False

        # Construct a model instance of GatewayMacsecConfigPatchTemplatePrimaryCak by calling from_dict on the json representation
        gateway_macsec_config_patch_template_primary_cak_model_dict = GatewayMacsecConfigPatchTemplatePrimaryCak.from_dict(gateway_macsec_config_patch_template_primary_cak_model_json).__dict__
        gateway_macsec_config_patch_template_primary_cak_model2 = GatewayMacsecConfigPatchTemplatePrimaryCak(**gateway_macsec_config_patch_template_primary_cak_model_dict)

        # Verify the model instances are equivalent
        assert gateway_macsec_config_patch_template_primary_cak_model == gateway_macsec_config_patch_template_primary_cak_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_macsec_config_patch_template_primary_cak_model_json2 = gateway_macsec_config_patch_template_primary_cak_model.to_dict()
        assert gateway_macsec_config_patch_template_primary_cak_model_json2 == gateway_macsec_config_patch_template_primary_cak_model_json

#-----------------------------------------------------------------------------
# Test Class for GatewayMacsecConfigPrimaryCak
#-----------------------------------------------------------------------------
class TestGatewayMacsecConfigPrimaryCak():

    #--------------------------------------------------------
    # Test serialization/deserialization for GatewayMacsecConfigPrimaryCak
    #--------------------------------------------------------
    def test_gateway_macsec_config_primary_cak_serialization(self):

        # Construct a json representation of a GatewayMacsecConfigPrimaryCak model
        gateway_macsec_config_primary_cak_model_json = {}
        gateway_macsec_config_primary_cak_model_json['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'
        gateway_macsec_config_primary_cak_model_json['status'] = 'testString'

        # Construct a model instance of GatewayMacsecConfigPrimaryCak by calling from_dict on the json representation
        gateway_macsec_config_primary_cak_model = GatewayMacsecConfigPrimaryCak.from_dict(gateway_macsec_config_primary_cak_model_json)
        assert gateway_macsec_config_primary_cak_model != False

        # Construct a model instance of GatewayMacsecConfigPrimaryCak by calling from_dict on the json representation
        gateway_macsec_config_primary_cak_model_dict = GatewayMacsecConfigPrimaryCak.from_dict(gateway_macsec_config_primary_cak_model_json).__dict__
        gateway_macsec_config_primary_cak_model2 = GatewayMacsecConfigPrimaryCak(**gateway_macsec_config_primary_cak_model_dict)

        # Verify the model instances are equivalent
        assert gateway_macsec_config_primary_cak_model == gateway_macsec_config_primary_cak_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_macsec_config_primary_cak_model_json2 = gateway_macsec_config_primary_cak_model.to_dict()
        assert gateway_macsec_config_primary_cak_model_json2 == gateway_macsec_config_primary_cak_model_json

#-----------------------------------------------------------------------------
# Test Class for GatewayMacsecConfigTemplate
#-----------------------------------------------------------------------------
class TestGatewayMacsecConfigTemplate():

    #--------------------------------------------------------
    # Test serialization/deserialization for GatewayMacsecConfigTemplate
    #--------------------------------------------------------
    def test_gateway_macsec_config_template_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        gateway_macsec_config_template_fallback_cak_model = {} # GatewayMacsecConfigTemplateFallbackCak
        gateway_macsec_config_template_fallback_cak_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        gateway_macsec_config_template_primary_cak_model = {} # GatewayMacsecConfigTemplatePrimaryCak
        gateway_macsec_config_template_primary_cak_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a json representation of a GatewayMacsecConfigTemplate model
        gateway_macsec_config_template_model_json = {}
        gateway_macsec_config_template_model_json['active'] = True
        gateway_macsec_config_template_model_json['fallback_cak'] = gateway_macsec_config_template_fallback_cak_model
        gateway_macsec_config_template_model_json['primary_cak'] = gateway_macsec_config_template_primary_cak_model
        gateway_macsec_config_template_model_json['window_size'] = 148809600

        # Construct a model instance of GatewayMacsecConfigTemplate by calling from_dict on the json representation
        gateway_macsec_config_template_model = GatewayMacsecConfigTemplate.from_dict(gateway_macsec_config_template_model_json)
        assert gateway_macsec_config_template_model != False

        # Construct a model instance of GatewayMacsecConfigTemplate by calling from_dict on the json representation
        gateway_macsec_config_template_model_dict = GatewayMacsecConfigTemplate.from_dict(gateway_macsec_config_template_model_json).__dict__
        gateway_macsec_config_template_model2 = GatewayMacsecConfigTemplate(**gateway_macsec_config_template_model_dict)

        # Verify the model instances are equivalent
        assert gateway_macsec_config_template_model == gateway_macsec_config_template_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_macsec_config_template_model_json2 = gateway_macsec_config_template_model.to_dict()
        assert gateway_macsec_config_template_model_json2 == gateway_macsec_config_template_model_json

#-----------------------------------------------------------------------------
# Test Class for GatewayMacsecConfigTemplateFallbackCak
#-----------------------------------------------------------------------------
class TestGatewayMacsecConfigTemplateFallbackCak():

    #--------------------------------------------------------
    # Test serialization/deserialization for GatewayMacsecConfigTemplateFallbackCak
    #--------------------------------------------------------
    def test_gateway_macsec_config_template_fallback_cak_serialization(self):

        # Construct a json representation of a GatewayMacsecConfigTemplateFallbackCak model
        gateway_macsec_config_template_fallback_cak_model_json = {}
        gateway_macsec_config_template_fallback_cak_model_json['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a model instance of GatewayMacsecConfigTemplateFallbackCak by calling from_dict on the json representation
        gateway_macsec_config_template_fallback_cak_model = GatewayMacsecConfigTemplateFallbackCak.from_dict(gateway_macsec_config_template_fallback_cak_model_json)
        assert gateway_macsec_config_template_fallback_cak_model != False

        # Construct a model instance of GatewayMacsecConfigTemplateFallbackCak by calling from_dict on the json representation
        gateway_macsec_config_template_fallback_cak_model_dict = GatewayMacsecConfigTemplateFallbackCak.from_dict(gateway_macsec_config_template_fallback_cak_model_json).__dict__
        gateway_macsec_config_template_fallback_cak_model2 = GatewayMacsecConfigTemplateFallbackCak(**gateway_macsec_config_template_fallback_cak_model_dict)

        # Verify the model instances are equivalent
        assert gateway_macsec_config_template_fallback_cak_model == gateway_macsec_config_template_fallback_cak_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_macsec_config_template_fallback_cak_model_json2 = gateway_macsec_config_template_fallback_cak_model.to_dict()
        assert gateway_macsec_config_template_fallback_cak_model_json2 == gateway_macsec_config_template_fallback_cak_model_json

#-----------------------------------------------------------------------------
# Test Class for GatewayMacsecConfigTemplatePrimaryCak
#-----------------------------------------------------------------------------
class TestGatewayMacsecConfigTemplatePrimaryCak():

    #--------------------------------------------------------
    # Test serialization/deserialization for GatewayMacsecConfigTemplatePrimaryCak
    #--------------------------------------------------------
    def test_gateway_macsec_config_template_primary_cak_serialization(self):

        # Construct a json representation of a GatewayMacsecConfigTemplatePrimaryCak model
        gateway_macsec_config_template_primary_cak_model_json = {}
        gateway_macsec_config_template_primary_cak_model_json['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        # Construct a model instance of GatewayMacsecConfigTemplatePrimaryCak by calling from_dict on the json representation
        gateway_macsec_config_template_primary_cak_model = GatewayMacsecConfigTemplatePrimaryCak.from_dict(gateway_macsec_config_template_primary_cak_model_json)
        assert gateway_macsec_config_template_primary_cak_model != False

        # Construct a model instance of GatewayMacsecConfigTemplatePrimaryCak by calling from_dict on the json representation
        gateway_macsec_config_template_primary_cak_model_dict = GatewayMacsecConfigTemplatePrimaryCak.from_dict(gateway_macsec_config_template_primary_cak_model_json).__dict__
        gateway_macsec_config_template_primary_cak_model2 = GatewayMacsecConfigTemplatePrimaryCak(**gateway_macsec_config_template_primary_cak_model_dict)

        # Verify the model instances are equivalent
        assert gateway_macsec_config_template_primary_cak_model == gateway_macsec_config_template_primary_cak_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_macsec_config_template_primary_cak_model_json2 = gateway_macsec_config_template_primary_cak_model.to_dict()
        assert gateway_macsec_config_template_primary_cak_model_json2 == gateway_macsec_config_template_primary_cak_model_json

#-----------------------------------------------------------------------------
# Test Class for GatewayPatchTemplateAuthenticationKey
#-----------------------------------------------------------------------------
class TestGatewayPatchTemplateAuthenticationKey():

    #--------------------------------------------------------
    # Test serialization/deserialization for GatewayPatchTemplateAuthenticationKey
    #--------------------------------------------------------
    def test_gateway_patch_template_authentication_key_serialization(self):

        # Construct a json representation of a GatewayPatchTemplateAuthenticationKey model
        gateway_patch_template_authentication_key_model_json = {}
        gateway_patch_template_authentication_key_model_json['crn'] = 'crn:v1:bluemix:public:kms:us-south:a/766d8d374a484f029d0fca5a40a52a1c:5d343839-07d3-4213-a950-0f71ed45423f:key:7fc1a0ba-4633-48cb-997b-5749787c952c'

        # Construct a model instance of GatewayPatchTemplateAuthenticationKey by calling from_dict on the json representation
        gateway_patch_template_authentication_key_model = GatewayPatchTemplateAuthenticationKey.from_dict(gateway_patch_template_authentication_key_model_json)
        assert gateway_patch_template_authentication_key_model != False

        # Construct a model instance of GatewayPatchTemplateAuthenticationKey by calling from_dict on the json representation
        gateway_patch_template_authentication_key_model_dict = GatewayPatchTemplateAuthenticationKey.from_dict(gateway_patch_template_authentication_key_model_json).__dict__
        gateway_patch_template_authentication_key_model2 = GatewayPatchTemplateAuthenticationKey(**gateway_patch_template_authentication_key_model_dict)

        # Verify the model instances are equivalent
        assert gateway_patch_template_authentication_key_model == gateway_patch_template_authentication_key_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_patch_template_authentication_key_model_json2 = gateway_patch_template_authentication_key_model.to_dict()
        assert gateway_patch_template_authentication_key_model_json2 == gateway_patch_template_authentication_key_model_json

#-----------------------------------------------------------------------------
# Test Class for GatewayPort
#-----------------------------------------------------------------------------
class TestGatewayPort():

    #--------------------------------------------------------
    # Test serialization/deserialization for GatewayPort
    #--------------------------------------------------------
    def test_gateway_port_serialization(self):

        # Construct a json representation of a GatewayPort model
        gateway_port_model_json = {}
        gateway_port_model_json['id'] = '54321b1a-fee4-41c7-9e11-9cd99e000aaa'

        # Construct a model instance of GatewayPort by calling from_dict on the json representation
        gateway_port_model = GatewayPort.from_dict(gateway_port_model_json)
        assert gateway_port_model != False

        # Construct a model instance of GatewayPort by calling from_dict on the json representation
        gateway_port_model_dict = GatewayPort.from_dict(gateway_port_model_json).__dict__
        gateway_port_model2 = GatewayPort(**gateway_port_model_dict)

        # Verify the model instances are equivalent
        assert gateway_port_model == gateway_port_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_port_model_json2 = gateway_port_model.to_dict()
        assert gateway_port_model_json2 == gateway_port_model_json

#-----------------------------------------------------------------------------
# Test Class for GatewayPortIdentity
#-----------------------------------------------------------------------------
class TestGatewayPortIdentity():

    #--------------------------------------------------------
    # Test serialization/deserialization for GatewayPortIdentity
    #--------------------------------------------------------
    def test_gateway_port_identity_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for GatewayStatistic
#-----------------------------------------------------------------------------
class TestGatewayStatistic():

    #--------------------------------------------------------
    # Test serialization/deserialization for GatewayStatistic
    #--------------------------------------------------------
    def test_gateway_statistic_serialization(self):

        # Construct a json representation of a GatewayStatistic model
        gateway_statistic_model_json = {}
        gateway_statistic_model_json['created_at'] = '2020-01-28T18:40:40.123456Z'
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

#-----------------------------------------------------------------------------
# Test Class for GatewayStatisticCollection
#-----------------------------------------------------------------------------
class TestGatewayStatisticCollection():

    #--------------------------------------------------------
    # Test serialization/deserialization for GatewayStatisticCollection
    #--------------------------------------------------------
    def test_gateway_statistic_collection_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        gateway_statistic_model = {} # GatewayStatistic
        gateway_statistic_model['created_at'] = '2020-01-28T18:40:40.123456Z'
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

#-----------------------------------------------------------------------------
# Test Class for GatewayTemplateAuthenticationKey
#-----------------------------------------------------------------------------
class TestGatewayTemplateAuthenticationKey():

    #--------------------------------------------------------
    # Test serialization/deserialization for GatewayTemplateAuthenticationKey
    #--------------------------------------------------------
    def test_gateway_template_authentication_key_serialization(self):

        # Construct a json representation of a GatewayTemplateAuthenticationKey model
        gateway_template_authentication_key_model_json = {}
        gateway_template_authentication_key_model_json['crn'] = 'crn:v1:bluemix:public:kms:us-south:a/766d8d374a484f029d0fca5a40a52a1c:5d343839-07d3-4213-a950-0f71ed45423f:key:7fc1a0ba-4633-48cb-997b-5749787c952c'

        # Construct a model instance of GatewayTemplateAuthenticationKey by calling from_dict on the json representation
        gateway_template_authentication_key_model = GatewayTemplateAuthenticationKey.from_dict(gateway_template_authentication_key_model_json)
        assert gateway_template_authentication_key_model != False

        # Construct a model instance of GatewayTemplateAuthenticationKey by calling from_dict on the json representation
        gateway_template_authentication_key_model_dict = GatewayTemplateAuthenticationKey.from_dict(gateway_template_authentication_key_model_json).__dict__
        gateway_template_authentication_key_model2 = GatewayTemplateAuthenticationKey(**gateway_template_authentication_key_model_dict)

        # Verify the model instances are equivalent
        assert gateway_template_authentication_key_model == gateway_template_authentication_key_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_template_authentication_key_model_json2 = gateway_template_authentication_key_model.to_dict()
        assert gateway_template_authentication_key_model_json2 == gateway_template_authentication_key_model_json

#-----------------------------------------------------------------------------
# Test Class for GatewayTemplateGatewayTypeConnectTemplateAuthenticationKey
#-----------------------------------------------------------------------------
class TestGatewayTemplateGatewayTypeConnectTemplateAuthenticationKey():

    #--------------------------------------------------------
    # Test serialization/deserialization for GatewayTemplateGatewayTypeConnectTemplateAuthenticationKey
    #--------------------------------------------------------
    def test_gateway_template_gateway_type_connect_template_authentication_key_serialization(self):

        # Construct a json representation of a GatewayTemplateGatewayTypeConnectTemplateAuthenticationKey model
        gateway_template_gateway_type_connect_template_authentication_key_model_json = {}
        gateway_template_gateway_type_connect_template_authentication_key_model_json['crn'] = 'crn:v1:bluemix:public:kms:us-south:a/766d8d374a484f029d0fca5a40a52a1c:5d343839-07d3-4213-a950-0f71ed45423f:key:7fc1a0ba-4633-48cb-997b-5749787c952c'

        # Construct a model instance of GatewayTemplateGatewayTypeConnectTemplateAuthenticationKey by calling from_dict on the json representation
        gateway_template_gateway_type_connect_template_authentication_key_model = GatewayTemplateGatewayTypeConnectTemplateAuthenticationKey.from_dict(gateway_template_gateway_type_connect_template_authentication_key_model_json)
        assert gateway_template_gateway_type_connect_template_authentication_key_model != False

        # Construct a model instance of GatewayTemplateGatewayTypeConnectTemplateAuthenticationKey by calling from_dict on the json representation
        gateway_template_gateway_type_connect_template_authentication_key_model_dict = GatewayTemplateGatewayTypeConnectTemplateAuthenticationKey.from_dict(gateway_template_gateway_type_connect_template_authentication_key_model_json).__dict__
        gateway_template_gateway_type_connect_template_authentication_key_model2 = GatewayTemplateGatewayTypeConnectTemplateAuthenticationKey(**gateway_template_gateway_type_connect_template_authentication_key_model_dict)

        # Verify the model instances are equivalent
        assert gateway_template_gateway_type_connect_template_authentication_key_model == gateway_template_gateway_type_connect_template_authentication_key_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_template_gateway_type_connect_template_authentication_key_model_json2 = gateway_template_gateway_type_connect_template_authentication_key_model.to_dict()
        assert gateway_template_gateway_type_connect_template_authentication_key_model_json2 == gateway_template_gateway_type_connect_template_authentication_key_model_json

#-----------------------------------------------------------------------------
# Test Class for GatewayTemplateGatewayTypeDedicatedTemplateAuthenticationKey
#-----------------------------------------------------------------------------
class TestGatewayTemplateGatewayTypeDedicatedTemplateAuthenticationKey():

    #--------------------------------------------------------
    # Test serialization/deserialization for GatewayTemplateGatewayTypeDedicatedTemplateAuthenticationKey
    #--------------------------------------------------------
    def test_gateway_template_gateway_type_dedicated_template_authentication_key_serialization(self):

        # Construct a json representation of a GatewayTemplateGatewayTypeDedicatedTemplateAuthenticationKey model
        gateway_template_gateway_type_dedicated_template_authentication_key_model_json = {}
        gateway_template_gateway_type_dedicated_template_authentication_key_model_json['crn'] = 'crn:v1:bluemix:public:kms:us-south:a/766d8d374a484f029d0fca5a40a52a1c:5d343839-07d3-4213-a950-0f71ed45423f:key:7fc1a0ba-4633-48cb-997b-5749787c952c'

        # Construct a model instance of GatewayTemplateGatewayTypeDedicatedTemplateAuthenticationKey by calling from_dict on the json representation
        gateway_template_gateway_type_dedicated_template_authentication_key_model = GatewayTemplateGatewayTypeDedicatedTemplateAuthenticationKey.from_dict(gateway_template_gateway_type_dedicated_template_authentication_key_model_json)
        assert gateway_template_gateway_type_dedicated_template_authentication_key_model != False

        # Construct a model instance of GatewayTemplateGatewayTypeDedicatedTemplateAuthenticationKey by calling from_dict on the json representation
        gateway_template_gateway_type_dedicated_template_authentication_key_model_dict = GatewayTemplateGatewayTypeDedicatedTemplateAuthenticationKey.from_dict(gateway_template_gateway_type_dedicated_template_authentication_key_model_json).__dict__
        gateway_template_gateway_type_dedicated_template_authentication_key_model2 = GatewayTemplateGatewayTypeDedicatedTemplateAuthenticationKey(**gateway_template_gateway_type_dedicated_template_authentication_key_model_dict)

        # Verify the model instances are equivalent
        assert gateway_template_gateway_type_dedicated_template_authentication_key_model == gateway_template_gateway_type_dedicated_template_authentication_key_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_template_gateway_type_dedicated_template_authentication_key_model_json2 = gateway_template_gateway_type_dedicated_template_authentication_key_model.to_dict()
        assert gateway_template_gateway_type_dedicated_template_authentication_key_model_json2 == gateway_template_gateway_type_dedicated_template_authentication_key_model_json

#-----------------------------------------------------------------------------
# Test Class for GatewayVirtualConnection
#-----------------------------------------------------------------------------
class TestGatewayVirtualConnection():

    #--------------------------------------------------------
    # Test serialization/deserialization for GatewayVirtualConnection
    #--------------------------------------------------------
    def test_gateway_virtual_connection_serialization(self):

        # Construct a json representation of a GatewayVirtualConnection model
        gateway_virtual_connection_model_json = {}
        gateway_virtual_connection_model_json['created_at'] = '2020-01-28T18:40:40.123456Z'
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

#-----------------------------------------------------------------------------
# Test Class for GatewayVirtualConnectionCollection
#-----------------------------------------------------------------------------
class TestGatewayVirtualConnectionCollection():

    #--------------------------------------------------------
    # Test serialization/deserialization for GatewayVirtualConnectionCollection
    #--------------------------------------------------------
    def test_gateway_virtual_connection_collection_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        gateway_virtual_connection_model = {} # GatewayVirtualConnection
        gateway_virtual_connection_model['created_at'] = '2020-01-28T18:40:40.123456Z'
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

#-----------------------------------------------------------------------------
# Test Class for LocationCollection
#-----------------------------------------------------------------------------
class TestLocationCollection():

    #--------------------------------------------------------
    # Test serialization/deserialization for LocationCollection
    #--------------------------------------------------------
    def test_location_collection_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        location_output_model = {} # LocationOutput
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

#-----------------------------------------------------------------------------
# Test Class for LocationCrossConnectRouterCollection
#-----------------------------------------------------------------------------
class TestLocationCrossConnectRouterCollection():

    #--------------------------------------------------------
    # Test serialization/deserialization for LocationCrossConnectRouterCollection
    #--------------------------------------------------------
    def test_location_cross_connect_router_collection_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        cross_connect_router_model = {} # CrossConnectRouter
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

#-----------------------------------------------------------------------------
# Test Class for LocationOutput
#-----------------------------------------------------------------------------
class TestLocationOutput():

    #--------------------------------------------------------
    # Test serialization/deserialization for LocationOutput
    #--------------------------------------------------------
    def test_location_output_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for OfferingSpeed
#-----------------------------------------------------------------------------
class TestOfferingSpeed():

    #--------------------------------------------------------
    # Test serialization/deserialization for OfferingSpeed
    #--------------------------------------------------------
    def test_offering_speed_serialization(self):

        # Construct a json representation of a OfferingSpeed model
        offering_speed_model_json = {}
        offering_speed_model_json['capabilities'] = ['testString']
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

#-----------------------------------------------------------------------------
# Test Class for OfferingSpeedCollection
#-----------------------------------------------------------------------------
class TestOfferingSpeedCollection():

    #--------------------------------------------------------
    # Test serialization/deserialization for OfferingSpeedCollection
    #--------------------------------------------------------
    def test_offering_speed_collection_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        offering_speed_model = {} # OfferingSpeed
        offering_speed_model['capabilities'] = ['testString']
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

#-----------------------------------------------------------------------------
# Test Class for Port
#-----------------------------------------------------------------------------
class TestPort():

    #--------------------------------------------------------
    # Test serialization/deserialization for Port
    #--------------------------------------------------------
    def test_port_serialization(self):

        # Construct a json representation of a Port model
        port_model_json = {}
        port_model_json['direct_link_count'] = 1
        port_model_json['id'] = '01122b9b-820f-4c44-8a31-77f1f0806765'
        port_model_json['label'] = 'XCR-FRK-CS-SEC-01'
        port_model_json['location_display_name'] = 'Dallas 03'
        port_model_json['location_name'] = 'dal03'
        port_model_json['provider_name'] = 'provider_1'
        port_model_json['supported_link_speeds'] = [38]

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

#-----------------------------------------------------------------------------
# Test Class for PortCollection
#-----------------------------------------------------------------------------
class TestPortCollection():

    #--------------------------------------------------------
    # Test serialization/deserialization for PortCollection
    #--------------------------------------------------------
    def test_port_collection_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        port_model = {} # Port
        port_model['direct_link_count'] = 1
        port_model['id'] = '01122b9b-820f-4c44-8a31-77f1f0806765'
        port_model['label'] = 'XCR-FRK-CS-SEC-01'
        port_model['location_display_name'] = 'Dallas 03'
        port_model['location_name'] = 'dal03'
        port_model['provider_name'] = 'provider_1'
        port_model['supported_link_speeds'] = [38]

        ports_paginated_collection_first_model = {} # PortsPaginatedCollectionFirst
        ports_paginated_collection_first_model['href'] = 'https://directlink.cloud.ibm.com/v1/ports?limit=100'

        ports_paginated_collection_next_model = {} # PortsPaginatedCollectionNext
        ports_paginated_collection_next_model['href'] = 'https://directlink.cloud.ibm.com/v1/ports?start=9d5a91a3e2cbd233b5a5b33436855ed1&limit=100'
        ports_paginated_collection_next_model['start'] = '9d5a91a3e2cbd233b5a5b33436855ed1'

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

#-----------------------------------------------------------------------------
# Test Class for PortsPaginatedCollectionFirst
#-----------------------------------------------------------------------------
class TestPortsPaginatedCollectionFirst():

    #--------------------------------------------------------
    # Test serialization/deserialization for PortsPaginatedCollectionFirst
    #--------------------------------------------------------
    def test_ports_paginated_collection_first_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for PortsPaginatedCollectionNext
#-----------------------------------------------------------------------------
class TestPortsPaginatedCollectionNext():

    #--------------------------------------------------------
    # Test serialization/deserialization for PortsPaginatedCollectionNext
    #--------------------------------------------------------
    def test_ports_paginated_collection_next_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for ResourceGroupIdentity
#-----------------------------------------------------------------------------
class TestResourceGroupIdentity():

    #--------------------------------------------------------
    # Test serialization/deserialization for ResourceGroupIdentity
    #--------------------------------------------------------
    def test_resource_group_identity_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for ResourceGroupReference
#-----------------------------------------------------------------------------
class TestResourceGroupReference():

    #--------------------------------------------------------
    # Test serialization/deserialization for ResourceGroupReference
    #--------------------------------------------------------
    def test_resource_group_reference_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for GatewayChangeRequestGatewayClientGatewayCreate
#-----------------------------------------------------------------------------
class TestGatewayChangeRequestGatewayClientGatewayCreate():

    #--------------------------------------------------------
    # Test serialization/deserialization for GatewayChangeRequestGatewayClientGatewayCreate
    #--------------------------------------------------------
    def test_gateway_change_request_gateway_client_gateway_create_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for GatewayChangeRequestGatewayClientGatewayDelete
#-----------------------------------------------------------------------------
class TestGatewayChangeRequestGatewayClientGatewayDelete():

    #--------------------------------------------------------
    # Test serialization/deserialization for GatewayChangeRequestGatewayClientGatewayDelete
    #--------------------------------------------------------
    def test_gateway_change_request_gateway_client_gateway_delete_serialization(self):

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

#-----------------------------------------------------------------------------
# Test Class for GatewayChangeRequestGatewayClientGatewayUpdateAttributes
#-----------------------------------------------------------------------------
class TestGatewayChangeRequestGatewayClientGatewayUpdateAttributes():

    #--------------------------------------------------------
    # Test serialization/deserialization for GatewayChangeRequestGatewayClientGatewayUpdateAttributes
    #--------------------------------------------------------
    def test_gateway_change_request_gateway_client_gateway_update_attributes_serialization(self):

        # Construct a json representation of a GatewayChangeRequestGatewayClientGatewayUpdateAttributes model
        gateway_change_request_gateway_client_gateway_update_attributes_model_json = {}
        gateway_change_request_gateway_client_gateway_update_attributes_model_json['type'] = 'update_attributes'
        gateway_change_request_gateway_client_gateway_update_attributes_model_json['updates'] = [{ 'foo': 'bar' }]

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

#-----------------------------------------------------------------------------
# Test Class for GatewayTemplateGatewayTypeConnectTemplate
#-----------------------------------------------------------------------------
class TestGatewayTemplateGatewayTypeConnectTemplate():

    #--------------------------------------------------------
    # Test serialization/deserialization for GatewayTemplateGatewayTypeConnectTemplate
    #--------------------------------------------------------
    def test_gateway_template_gateway_type_connect_template_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        gateway_port_identity_model = {} # GatewayPortIdentity
        gateway_port_identity_model['id'] = 'fffdcb1a-fee4-41c7-9e11-9cd99e65c777'

        gateway_template_gateway_type_connect_template_authentication_key_model = {} # GatewayTemplateGatewayTypeConnectTemplateAuthenticationKey
        gateway_template_gateway_type_connect_template_authentication_key_model['crn'] = 'crn:v1:bluemix:public:kms:us-south:a/766d8d374a484f029d0fca5a40a52a1c:5d343839-07d3-4213-a950-0f71ed45423f:key:7fc1a0ba-4633-48cb-997b-5749787c952c'

        resource_group_identity_model = {} # ResourceGroupIdentity
        resource_group_identity_model['id'] = '56969d6043e9465c883cb9f7363e78e8'

        # Construct a json representation of a GatewayTemplateGatewayTypeConnectTemplate model
        gateway_template_gateway_type_connect_template_model_json = {}
        gateway_template_gateway_type_connect_template_model_json['authentication_key'] = gateway_template_gateway_type_connect_template_authentication_key_model
        gateway_template_gateway_type_connect_template_model_json['bgp_asn'] = 64999
        gateway_template_gateway_type_connect_template_model_json['bgp_base_cidr'] = 'testString'
        gateway_template_gateway_type_connect_template_model_json['bgp_cer_cidr'] = '169.254.0.10/30'
        gateway_template_gateway_type_connect_template_model_json['bgp_ibm_cidr'] = '169.254.0.9/30'
        gateway_template_gateway_type_connect_template_model_json['connection_mode'] = 'transit'
        gateway_template_gateway_type_connect_template_model_json['global'] = True
        gateway_template_gateway_type_connect_template_model_json['metered'] = False
        gateway_template_gateway_type_connect_template_model_json['name'] = 'myGateway'
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

#-----------------------------------------------------------------------------
# Test Class for GatewayTemplateGatewayTypeDedicatedTemplate
#-----------------------------------------------------------------------------
class TestGatewayTemplateGatewayTypeDedicatedTemplate():

    #--------------------------------------------------------
    # Test serialization/deserialization for GatewayTemplateGatewayTypeDedicatedTemplate
    #--------------------------------------------------------
    def test_gateway_template_gateway_type_dedicated_template_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        gateway_macsec_config_template_fallback_cak_model = {} # GatewayMacsecConfigTemplateFallbackCak
        gateway_macsec_config_template_fallback_cak_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        gateway_macsec_config_template_primary_cak_model = {} # GatewayMacsecConfigTemplatePrimaryCak
        gateway_macsec_config_template_primary_cak_model['crn'] = 'crn:v1:bluemix:public:hs-crypto:us-south:a/4111d05f36894e3cb9b46a43556d9000:abc111b8-37aa-4034-9def-f2607c87aaaa:key:bbb222bc-430a-4de9-9aad-84e5bb022222'

        gateway_macsec_config_template_model = {} # GatewayMacsecConfigTemplate
        gateway_macsec_config_template_model['active'] = True
        gateway_macsec_config_template_model['fallback_cak'] = gateway_macsec_config_template_fallback_cak_model
        gateway_macsec_config_template_model['primary_cak'] = gateway_macsec_config_template_primary_cak_model
        gateway_macsec_config_template_model['window_size'] = 148809600

        gateway_template_gateway_type_dedicated_template_authentication_key_model = {} # GatewayTemplateGatewayTypeDedicatedTemplateAuthenticationKey
        gateway_template_gateway_type_dedicated_template_authentication_key_model['crn'] = 'crn:v1:bluemix:public:kms:us-south:a/766d8d374a484f029d0fca5a40a52a1c:5d343839-07d3-4213-a950-0f71ed45423f:key:7fc1a0ba-4633-48cb-997b-5749787c952c'

        resource_group_identity_model = {} # ResourceGroupIdentity
        resource_group_identity_model['id'] = '56969d6043e9465c883cb9f7363e78e8'

        # Construct a json representation of a GatewayTemplateGatewayTypeDedicatedTemplate model
        gateway_template_gateway_type_dedicated_template_model_json = {}
        gateway_template_gateway_type_dedicated_template_model_json['authentication_key'] = gateway_template_gateway_type_dedicated_template_authentication_key_model
        gateway_template_gateway_type_dedicated_template_model_json['bgp_asn'] = 64999
        gateway_template_gateway_type_dedicated_template_model_json['bgp_base_cidr'] = 'testString'
        gateway_template_gateway_type_dedicated_template_model_json['bgp_cer_cidr'] = '169.254.0.10/30'
        gateway_template_gateway_type_dedicated_template_model_json['bgp_ibm_cidr'] = '169.254.0.9/30'
        gateway_template_gateway_type_dedicated_template_model_json['connection_mode'] = 'transit'
        gateway_template_gateway_type_dedicated_template_model_json['global'] = True
        gateway_template_gateway_type_dedicated_template_model_json['metered'] = False
        gateway_template_gateway_type_dedicated_template_model_json['name'] = 'myGateway'
        gateway_template_gateway_type_dedicated_template_model_json['resource_group'] = resource_group_identity_model
        gateway_template_gateway_type_dedicated_template_model_json['speed_mbps'] = 1000
        gateway_template_gateway_type_dedicated_template_model_json['type'] = 'dedicated'
        gateway_template_gateway_type_dedicated_template_model_json['carrier_name'] = 'myCarrierName'
        gateway_template_gateway_type_dedicated_template_model_json['cross_connect_router'] = 'xcr01.dal03'
        gateway_template_gateway_type_dedicated_template_model_json['customer_name'] = 'newCustomerName'
        gateway_template_gateway_type_dedicated_template_model_json['location_name'] = 'dal03'
        gateway_template_gateway_type_dedicated_template_model_json['macsec_config'] = gateway_macsec_config_template_model

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


# endregion
##############################################################################
# End of Model Tests
##############################################################################
