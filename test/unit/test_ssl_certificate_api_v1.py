# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.
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
import json
import pytest
import responses
from ibm_cloud_networking_services.ssl_certificate_api_v1 import *

crn = 'testString'
zone_identifier = 'testString'

service = SslCertificateApiV1(
    authenticator=NoAuthAuthenticator(),
    crn=crn,
    zone_identifier=zone_identifier
    )

base_url = 'https://api.cis.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: SSLCertificate
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_certificates
#-----------------------------------------------------------------------------
class TestListCertificates():

    #--------------------------------------------------------
    # list_certificates()
    #--------------------------------------------------------
    @responses.activate
    def test_list_certificates_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/ssl/certificate_packs'
        mock_response = '{"result": [{"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "type": "dedicated", "hosts": ["example.com"], "certificates": [{"id": "436627", "hosts": ["example.com"], "status": "active"}], "primary_certificate": 0}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        x_correlation_id = 'testString'

        # Invoke method
        response = service.list_certificates(
            x_correlation_id=x_correlation_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_certificates_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_certificates_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/ssl/certificate_packs'
        mock_response = '{"result": [{"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "type": "dedicated", "hosts": ["example.com"], "certificates": [{"id": "436627", "hosts": ["example.com"], "status": "active"}], "primary_certificate": 0}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_certificates()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for order_certificate
#-----------------------------------------------------------------------------
class TestOrderCertificate():

    #--------------------------------------------------------
    # order_certificate()
    #--------------------------------------------------------
    @responses.activate
    def test_order_certificate_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/ssl/certificate_packs'
        mock_response = '{"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "type": "dedicated", "hosts": ["example.com"], "certificates": [{"id": "436627", "hosts": ["example.com"], "status": "active"}], "primary_certificate": 0}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        type = 'dedicated'
        hosts = ['example.com']
        x_correlation_id = 'testString'

        # Invoke method
        response = service.order_certificate(
            type=type,
            hosts=hosts,
            x_correlation_id=x_correlation_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == type
        assert req_body['hosts'] == hosts


    #--------------------------------------------------------
    # test_order_certificate_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_order_certificate_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/ssl/certificate_packs'
        mock_response = '{"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "type": "dedicated", "hosts": ["example.com"], "certificates": [{"id": "436627", "hosts": ["example.com"], "status": "active"}], "primary_certificate": 0}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.order_certificate()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for delete_certificate
#-----------------------------------------------------------------------------
class TestDeleteCertificate():

    #--------------------------------------------------------
    # delete_certificate()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_certificate_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/ssl/certificate_packs/testString'
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        cert_identifier = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = service.delete_certificate(
            cert_identifier,
            x_correlation_id=x_correlation_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_certificate_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_certificate_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/ssl/certificate_packs/testString'
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        cert_identifier = 'testString'

        # Invoke method
        response = service.delete_certificate(
            cert_identifier
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_ssl_setting
#-----------------------------------------------------------------------------
class TestGetSslSetting():

    #--------------------------------------------------------
    # get_ssl_setting()
    #--------------------------------------------------------
    @responses.activate
    def test_get_ssl_setting_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/ssl'
        mock_response = '{"success": true, "result": {"id": "ssl", "value": "off", "editable": true, "modified_on": "2017-01-01T05:20:00.12345Z"}, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_ssl_setting()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_ssl_setting_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_ssl_setting_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/ssl'
        mock_response = '{"success": true, "result": {"id": "ssl", "value": "off", "editable": true, "modified_on": "2017-01-01T05:20:00.12345Z"}, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_ssl_setting()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for change_ssl_setting
#-----------------------------------------------------------------------------
class TestChangeSslSetting():

    #--------------------------------------------------------
    # change_ssl_setting()
    #--------------------------------------------------------
    @responses.activate
    def test_change_ssl_setting_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/ssl'
        mock_response = '{"success": true, "result": {"id": "ssl", "value": "off", "editable": true, "modified_on": "2017-01-01T05:20:00.12345Z"}, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'off'

        # Invoke method
        response = service.change_ssl_setting(
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_change_ssl_setting_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_change_ssl_setting_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/ssl'
        mock_response = '{"success": true, "result": {"id": "ssl", "value": "off", "editable": true, "modified_on": "2017-01-01T05:20:00.12345Z"}, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.change_ssl_setting()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for list_custom_certificates
#-----------------------------------------------------------------------------
class TestListCustomCertificates():

    #--------------------------------------------------------
    # list_custom_certificates()
    #--------------------------------------------------------
    @responses.activate
    def test_list_custom_certificates_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/custom_certificates'
        mock_response = '{"result": [{"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "hosts": ["example.com"], "issuer": "/Country=US/Organization=Lets Encrypt/CommonName=Lets Encrypt Authority X3", "signature": "SHA256WithRSA", "status": "active", "bundle_method": "bundle_method", "zone_id": "zone_id", "uploaded_on": "uploaded_on", "modified_on": "modified_on", "expires_on": "expires_on", "priority": 8}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_custom_certificates()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_list_custom_certificates_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_list_custom_certificates_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/custom_certificates'
        mock_response = '{"result": [{"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "hosts": ["example.com"], "issuer": "/Country=US/Organization=Lets Encrypt/CommonName=Lets Encrypt Authority X3", "signature": "SHA256WithRSA", "status": "active", "bundle_method": "bundle_method", "zone_id": "zone_id", "uploaded_on": "uploaded_on", "modified_on": "modified_on", "expires_on": "expires_on", "priority": 8}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_custom_certificates()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for upload_custom_certificate
#-----------------------------------------------------------------------------
class TestUploadCustomCertificate():

    #--------------------------------------------------------
    # upload_custom_certificate()
    #--------------------------------------------------------
    @responses.activate
    def test_upload_custom_certificate_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/custom_certificates'
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "hosts": ["example.com"], "issuer": "/Country=US/Organization=Lets Encrypt/CommonName=Lets Encrypt Authority X3", "signature": "SHA256WithRSA", "status": "active", "bundle_method": "bundle_method", "zone_id": "zone_id", "uploaded_on": "uploaded_on", "modified_on": "modified_on", "expires_on": "expires_on", "priority": 8}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a CustomCertReqGeoRestrictions model
        custom_cert_req_geo_restrictions_model =  {
            'label': 'us'
        }

        # Set up parameter values
        certificate = 'testString'
        private_key = 'testString'
        bundle_method = 'ubiquitous'
        geo_restrictions = custom_cert_req_geo_restrictions_model

        # Invoke method
        response = service.upload_custom_certificate(
            certificate=certificate,
            private_key=private_key,
            bundle_method=bundle_method,
            geo_restrictions=geo_restrictions,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['certificate'] == certificate
        assert req_body['private_key'] == private_key
        assert req_body['bundle_method'] == bundle_method
        assert req_body['geo_restrictions'] == geo_restrictions


    #--------------------------------------------------------
    # test_upload_custom_certificate_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_upload_custom_certificate_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/custom_certificates'
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "hosts": ["example.com"], "issuer": "/Country=US/Organization=Lets Encrypt/CommonName=Lets Encrypt Authority X3", "signature": "SHA256WithRSA", "status": "active", "bundle_method": "bundle_method", "zone_id": "zone_id", "uploaded_on": "uploaded_on", "modified_on": "modified_on", "expires_on": "expires_on", "priority": 8}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.upload_custom_certificate()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_custom_certificate
#-----------------------------------------------------------------------------
class TestGetCustomCertificate():

    #--------------------------------------------------------
    # get_custom_certificate()
    #--------------------------------------------------------
    @responses.activate
    def test_get_custom_certificate_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/custom_certificates/testString'
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "hosts": ["example.com"], "issuer": "/Country=US/Organization=Lets Encrypt/CommonName=Lets Encrypt Authority X3", "signature": "SHA256WithRSA", "status": "active", "bundle_method": "bundle_method", "zone_id": "zone_id", "uploaded_on": "uploaded_on", "modified_on": "modified_on", "expires_on": "expires_on", "priority": 8}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        custom_cert_id = 'testString'

        # Invoke method
        response = service.get_custom_certificate(
            custom_cert_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_custom_certificate_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_custom_certificate_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/custom_certificates/testString'
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "hosts": ["example.com"], "issuer": "/Country=US/Organization=Lets Encrypt/CommonName=Lets Encrypt Authority X3", "signature": "SHA256WithRSA", "status": "active", "bundle_method": "bundle_method", "zone_id": "zone_id", "uploaded_on": "uploaded_on", "modified_on": "modified_on", "expires_on": "expires_on", "priority": 8}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        custom_cert_id = 'testString'

        # Invoke method
        response = service.get_custom_certificate(
            custom_cert_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for update_custom_certificate
#-----------------------------------------------------------------------------
class TestUpdateCustomCertificate():

    #--------------------------------------------------------
    # update_custom_certificate()
    #--------------------------------------------------------
    @responses.activate
    def test_update_custom_certificate_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/custom_certificates/testString'
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "hosts": ["example.com"], "issuer": "/Country=US/Organization=Lets Encrypt/CommonName=Lets Encrypt Authority X3", "signature": "SHA256WithRSA", "status": "active", "bundle_method": "bundle_method", "zone_id": "zone_id", "uploaded_on": "uploaded_on", "modified_on": "modified_on", "expires_on": "expires_on", "priority": 8}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a CustomCertReqGeoRestrictions model
        custom_cert_req_geo_restrictions_model =  {
            'label': 'us'
        }

        # Set up parameter values
        custom_cert_id = 'testString'
        certificate = 'testString'
        private_key = 'testString'
        bundle_method = 'ubiquitous'
        geo_restrictions = custom_cert_req_geo_restrictions_model

        # Invoke method
        response = service.update_custom_certificate(
            custom_cert_id,
            certificate=certificate,
            private_key=private_key,
            bundle_method=bundle_method,
            geo_restrictions=geo_restrictions,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['certificate'] == certificate
        assert req_body['private_key'] == private_key
        assert req_body['bundle_method'] == bundle_method
        assert req_body['geo_restrictions'] == geo_restrictions


    #--------------------------------------------------------
    # test_update_custom_certificate_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_custom_certificate_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/custom_certificates/testString'
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "hosts": ["example.com"], "issuer": "/Country=US/Organization=Lets Encrypt/CommonName=Lets Encrypt Authority X3", "signature": "SHA256WithRSA", "status": "active", "bundle_method": "bundle_method", "zone_id": "zone_id", "uploaded_on": "uploaded_on", "modified_on": "modified_on", "expires_on": "expires_on", "priority": 8}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        custom_cert_id = 'testString'

        # Invoke method
        response = service.update_custom_certificate(
            custom_cert_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for delete_custom_certificate
#-----------------------------------------------------------------------------
class TestDeleteCustomCertificate():

    #--------------------------------------------------------
    # delete_custom_certificate()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_custom_certificate_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/custom_certificates/testString'
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        custom_cert_id = 'testString'

        # Invoke method
        response = service.delete_custom_certificate(
            custom_cert_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_custom_certificate_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_custom_certificate_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/custom_certificates/testString'
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        custom_cert_id = 'testString'

        # Invoke method
        response = service.delete_custom_certificate(
            custom_cert_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for change_certificate_priority
#-----------------------------------------------------------------------------
class TestChangeCertificatePriority():

    #--------------------------------------------------------
    # change_certificate_priority()
    #--------------------------------------------------------
    @responses.activate
    def test_change_certificate_priority_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/custom_certificates/prioritize'
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Construct a dict representation of a CertPriorityReqCertificatesItem model
        cert_priority_req_certificates_item_model =  {
            'id': '5a7805061c76ada191ed06f989cc3dac',
            'priority': 1
        }

        # Set up parameter values
        certificates = [cert_priority_req_certificates_item_model]

        # Invoke method
        response = service.change_certificate_priority(
            certificates=certificates,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['certificates'] == certificates


    #--------------------------------------------------------
    # test_change_certificate_priority_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_change_certificate_priority_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/custom_certificates/prioritize'
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Invoke method
        response = service.change_certificate_priority()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_universal_certificate_setting
#-----------------------------------------------------------------------------
class TestGetUniversalCertificateSetting():

    #--------------------------------------------------------
    # get_universal_certificate_setting()
    #--------------------------------------------------------
    @responses.activate
    def test_get_universal_certificate_setting_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/ssl/universal/settings'
        mock_response = '{"result": {"enabled": true}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_universal_certificate_setting()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_universal_certificate_setting_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_universal_certificate_setting_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/ssl/universal/settings'
        mock_response = '{"result": {"enabled": true}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_universal_certificate_setting()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for change_universal_certificate_setting
#-----------------------------------------------------------------------------
class TestChangeUniversalCertificateSetting():

    #--------------------------------------------------------
    # change_universal_certificate_setting()
    #--------------------------------------------------------
    @responses.activate
    def test_change_universal_certificate_setting_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/ssl/universal/settings'
        responses.add(responses.PATCH,
                      url,
                      status=200)

        # Set up parameter values
        enabled = True

        # Invoke method
        response = service.change_universal_certificate_setting(
            enabled=enabled,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['enabled'] == enabled


    #--------------------------------------------------------
    # test_change_universal_certificate_setting_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_change_universal_certificate_setting_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/ssl/universal/settings'
        responses.add(responses.PATCH,
                      url,
                      status=200)

        # Invoke method
        response = service.change_universal_certificate_setting()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_tls12_setting
#-----------------------------------------------------------------------------
class TestGetTls12Setting():

    #--------------------------------------------------------
    # get_tls12_setting()
    #--------------------------------------------------------
    @responses.activate
    def test_get_tls12_setting_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/tls_1_2_only'
        mock_response = '{"result": {"id": "tls_1_2_only", "value": "on", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_tls12_setting()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_tls12_setting_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_tls12_setting_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/tls_1_2_only'
        mock_response = '{"result": {"id": "tls_1_2_only", "value": "on", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_tls12_setting()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for change_tls12_setting
#-----------------------------------------------------------------------------
class TestChangeTls12Setting():

    #--------------------------------------------------------
    # change_tls12_setting()
    #--------------------------------------------------------
    @responses.activate
    def test_change_tls12_setting_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/tls_1_2_only'
        mock_response = '{"result": {"id": "tls_1_2_only", "value": "on", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'on'

        # Invoke method
        response = service.change_tls12_setting(
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_change_tls12_setting_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_change_tls12_setting_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/tls_1_2_only'
        mock_response = '{"result": {"id": "tls_1_2_only", "value": "on", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.change_tls12_setting()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_tls13_setting
#-----------------------------------------------------------------------------
class TestGetTls13Setting():

    #--------------------------------------------------------
    # get_tls13_setting()
    #--------------------------------------------------------
    @responses.activate
    def test_get_tls13_setting_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/tls_1_3'
        mock_response = '{"result": {"id": "tls_1_3", "value": "on", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_tls13_setting()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_tls13_setting_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_tls13_setting_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/tls_1_3'
        mock_response = '{"result": {"id": "tls_1_3", "value": "on", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.get_tls13_setting()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for change_tls13_setting
#-----------------------------------------------------------------------------
class TestChangeTls13Setting():

    #--------------------------------------------------------
    # change_tls13_setting()
    #--------------------------------------------------------
    @responses.activate
    def test_change_tls13_setting_all_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/tls_1_3'
        mock_response = '{"result": {"id": "tls_1_3", "value": "on", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        value = 'on'

        # Invoke method
        response = service.change_tls13_setting(
            value=value,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == value


    #--------------------------------------------------------
    # test_change_tls13_setting_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_change_tls13_setting_required_params(self):
        # Set up mock
        url = base_url + '/v1/testString/zones/testString/settings/tls_1_3'
        mock_response = '{"result": {"id": "tls_1_3", "value": "on", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.change_tls13_setting()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


# endregion
##############################################################################
# End of Service: SSLCertificate
##############################################################################

