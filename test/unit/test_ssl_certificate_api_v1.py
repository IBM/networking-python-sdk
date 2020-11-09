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
import re
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

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # list_certificates()
    #--------------------------------------------------------
    @responses.activate
    def test_list_certificates_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/ssl/certificate_packs')
        mock_response = '{"result": [{"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "type": "dedicated", "hosts": ["example.com"], "certificates": [{"id": {"anyKey": "anyValue"}, "hosts": ["example.com"], "status": "active"}], "primary_certificate": {"anyKey": "anyValue"}, "status": "active"}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        x_correlation_id = 'testString'

        # Invoke method
        response = service.list_certificates(
            x_correlation_id=x_correlation_id,
            headers={}
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
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/ssl/certificate_packs')
        mock_response = '{"result": [{"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "type": "dedicated", "hosts": ["example.com"], "certificates": [{"id": {"anyKey": "anyValue"}, "hosts": ["example.com"], "status": "active"}], "primary_certificate": {"anyKey": "anyValue"}, "status": "active"}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
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


    #--------------------------------------------------------
    # test_list_certificates_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_certificates_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/ssl/certificate_packs')
        mock_response = '{"result": [{"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "type": "dedicated", "hosts": ["example.com"], "certificates": [{"id": {"anyKey": "anyValue"}, "hosts": ["example.com"], "status": "active"}], "primary_certificate": {"anyKey": "anyValue"}, "status": "active"}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
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
                service.list_certificates(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for order_certificate
#-----------------------------------------------------------------------------
class TestOrderCertificate():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # order_certificate()
    #--------------------------------------------------------
    @responses.activate
    def test_order_certificate_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/ssl/certificate_packs')
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "type": "dedicated", "hosts": ["example.com"], "certificates": [{"id": {"anyKey": "anyValue"}, "hosts": ["example.com"], "status": "active"}], "primary_certificate": {"anyKey": "anyValue"}, "status": "active"}, "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
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
            x_correlation_id=x_correlation_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'dedicated'
        assert req_body['hosts'] == ['example.com']


    #--------------------------------------------------------
    # test_order_certificate_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_order_certificate_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/ssl/certificate_packs')
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "type": "dedicated", "hosts": ["example.com"], "certificates": [{"id": {"anyKey": "anyValue"}, "hosts": ["example.com"], "status": "active"}], "primary_certificate": {"anyKey": "anyValue"}, "status": "active"}, "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
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


    #--------------------------------------------------------
    # test_order_certificate_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_order_certificate_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/ssl/certificate_packs')
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "type": "dedicated", "hosts": ["example.com"], "certificates": [{"id": {"anyKey": "anyValue"}, "hosts": ["example.com"], "status": "active"}], "primary_certificate": {"anyKey": "anyValue"}, "status": "active"}, "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
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
                service.order_certificate(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_certificate
#-----------------------------------------------------------------------------
class TestDeleteCertificate():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # delete_certificate()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_certificate_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/ssl/certificate_packs/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        cert_identifier = 'testString'
        x_correlation_id = 'testString'

        # Invoke method
        response = service.delete_certificate(
            cert_identifier,
            x_correlation_id=x_correlation_id,
            headers={}
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
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/ssl/certificate_packs/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        cert_identifier = 'testString'

        # Invoke method
        response = service.delete_certificate(
            cert_identifier,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_certificate_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_certificate_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/ssl/certificate_packs/testString')
        responses.add(responses.DELETE,
                      url,
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
                service.delete_certificate(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_ssl_setting
#-----------------------------------------------------------------------------
class TestGetSslSetting():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_ssl_setting()
    #--------------------------------------------------------
    @responses.activate
    def test_get_ssl_setting_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/ssl')
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
    # test_get_ssl_setting_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_ssl_setting_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/ssl')
        mock_response = '{"success": true, "result": {"id": "ssl", "value": "off", "editable": true, "modified_on": "2017-01-01T05:20:00.12345Z"}, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
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
                service.get_ssl_setting(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for change_ssl_setting
#-----------------------------------------------------------------------------
class TestChangeSslSetting():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # change_ssl_setting()
    #--------------------------------------------------------
    @responses.activate
    def test_change_ssl_setting_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/ssl')
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
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'off'


    #--------------------------------------------------------
    # test_change_ssl_setting_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_change_ssl_setting_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/ssl')
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


    #--------------------------------------------------------
    # test_change_ssl_setting_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_change_ssl_setting_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/ssl')
        mock_response = '{"success": true, "result": {"id": "ssl", "value": "off", "editable": true, "modified_on": "2017-01-01T05:20:00.12345Z"}, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.PATCH,
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
                service.change_ssl_setting(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for list_custom_certificates
#-----------------------------------------------------------------------------
class TestListCustomCertificates():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # list_custom_certificates()
    #--------------------------------------------------------
    @responses.activate
    def test_list_custom_certificates_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/custom_certificates')
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
    # test_list_custom_certificates_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_list_custom_certificates_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/custom_certificates')
        mock_response = '{"result": [{"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "hosts": ["example.com"], "issuer": "/Country=US/Organization=Lets Encrypt/CommonName=Lets Encrypt Authority X3", "signature": "SHA256WithRSA", "status": "active", "bundle_method": "bundle_method", "zone_id": "zone_id", "uploaded_on": "uploaded_on", "modified_on": "modified_on", "expires_on": "expires_on", "priority": 8}], "result_info": {"page": 1, "per_page": 2, "count": 1, "total_count": 200}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
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
                service.list_custom_certificates(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for upload_custom_certificate
#-----------------------------------------------------------------------------
class TestUploadCustomCertificate():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # upload_custom_certificate()
    #--------------------------------------------------------
    @responses.activate
    def test_upload_custom_certificate_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/custom_certificates')
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "hosts": ["example.com"], "issuer": "/Country=US/Organization=Lets Encrypt/CommonName=Lets Encrypt Authority X3", "signature": "SHA256WithRSA", "status": "active", "bundle_method": "bundle_method", "zone_id": "zone_id", "uploaded_on": "uploaded_on", "modified_on": "modified_on", "expires_on": "expires_on", "priority": 8}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a CustomCertReqGeoRestrictions model
        custom_cert_req_geo_restrictions_model = {}
        custom_cert_req_geo_restrictions_model['label'] = 'us'

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
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['certificate'] == 'testString'
        assert req_body['private_key'] == 'testString'
        assert req_body['bundle_method'] == 'ubiquitous'
        assert req_body['geo_restrictions'] == custom_cert_req_geo_restrictions_model


    #--------------------------------------------------------
    # test_upload_custom_certificate_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_upload_custom_certificate_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/custom_certificates')
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


    #--------------------------------------------------------
    # test_upload_custom_certificate_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_upload_custom_certificate_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/custom_certificates')
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "hosts": ["example.com"], "issuer": "/Country=US/Organization=Lets Encrypt/CommonName=Lets Encrypt Authority X3", "signature": "SHA256WithRSA", "status": "active", "bundle_method": "bundle_method", "zone_id": "zone_id", "uploaded_on": "uploaded_on", "modified_on": "modified_on", "expires_on": "expires_on", "priority": 8}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
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
                service.upload_custom_certificate(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_custom_certificate
#-----------------------------------------------------------------------------
class TestGetCustomCertificate():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_custom_certificate()
    #--------------------------------------------------------
    @responses.activate
    def test_get_custom_certificate_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/custom_certificates/testString')
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
            custom_cert_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_custom_certificate_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_custom_certificate_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/custom_certificates/testString')
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "hosts": ["example.com"], "issuer": "/Country=US/Organization=Lets Encrypt/CommonName=Lets Encrypt Authority X3", "signature": "SHA256WithRSA", "status": "active", "bundle_method": "bundle_method", "zone_id": "zone_id", "uploaded_on": "uploaded_on", "modified_on": "modified_on", "expires_on": "expires_on", "priority": 8}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        custom_cert_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "custom_cert_id": custom_cert_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.get_custom_certificate(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for update_custom_certificate
#-----------------------------------------------------------------------------
class TestUpdateCustomCertificate():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # update_custom_certificate()
    #--------------------------------------------------------
    @responses.activate
    def test_update_custom_certificate_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/custom_certificates/testString')
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "hosts": ["example.com"], "issuer": "/Country=US/Organization=Lets Encrypt/CommonName=Lets Encrypt Authority X3", "signature": "SHA256WithRSA", "status": "active", "bundle_method": "bundle_method", "zone_id": "zone_id", "uploaded_on": "uploaded_on", "modified_on": "modified_on", "expires_on": "expires_on", "priority": 8}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a CustomCertReqGeoRestrictions model
        custom_cert_req_geo_restrictions_model = {}
        custom_cert_req_geo_restrictions_model['label'] = 'us'

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
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['certificate'] == 'testString'
        assert req_body['private_key'] == 'testString'
        assert req_body['bundle_method'] == 'ubiquitous'
        assert req_body['geo_restrictions'] == custom_cert_req_geo_restrictions_model


    #--------------------------------------------------------
    # test_update_custom_certificate_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_update_custom_certificate_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/custom_certificates/testString')
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
            custom_cert_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_update_custom_certificate_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_update_custom_certificate_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/custom_certificates/testString')
        mock_response = '{"result": {"id": "0f405ba2-8c18-49eb-a30b-28b85427780f", "hosts": ["example.com"], "issuer": "/Country=US/Organization=Lets Encrypt/CommonName=Lets Encrypt Authority X3", "signature": "SHA256WithRSA", "status": "active", "bundle_method": "bundle_method", "zone_id": "zone_id", "uploaded_on": "uploaded_on", "modified_on": "modified_on", "expires_on": "expires_on", "priority": 8}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        custom_cert_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "custom_cert_id": custom_cert_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.update_custom_certificate(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for delete_custom_certificate
#-----------------------------------------------------------------------------
class TestDeleteCustomCertificate():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # delete_custom_certificate()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_custom_certificate_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/custom_certificates/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        custom_cert_id = 'testString'

        # Invoke method
        response = service.delete_custom_certificate(
            custom_cert_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_delete_custom_certificate_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_custom_certificate_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/custom_certificates/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        custom_cert_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "custom_cert_id": custom_cert_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_custom_certificate(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for change_certificate_priority
#-----------------------------------------------------------------------------
class TestChangeCertificatePriority():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # change_certificate_priority()
    #--------------------------------------------------------
    @responses.activate
    def test_change_certificate_priority_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/custom_certificates/prioritize')
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Construct a dict representation of a CertPriorityReqCertificatesItem model
        cert_priority_req_certificates_item_model = {}
        cert_priority_req_certificates_item_model['id'] = '5a7805061c76ada191ed06f989cc3dac'
        cert_priority_req_certificates_item_model['priority'] = 1

        # Set up parameter values
        certificates = [cert_priority_req_certificates_item_model]

        # Invoke method
        response = service.change_certificate_priority(
            certificates=certificates,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['certificates'] == [cert_priority_req_certificates_item_model]


    #--------------------------------------------------------
    # test_change_certificate_priority_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_change_certificate_priority_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/custom_certificates/prioritize')
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Invoke method
        response = service.change_certificate_priority()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_change_certificate_priority_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_change_certificate_priority_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/custom_certificates/prioritize')
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.change_certificate_priority(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_universal_certificate_setting
#-----------------------------------------------------------------------------
class TestGetUniversalCertificateSetting():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_universal_certificate_setting()
    #--------------------------------------------------------
    @responses.activate
    def test_get_universal_certificate_setting_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/ssl/universal/settings')
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
    # test_get_universal_certificate_setting_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_universal_certificate_setting_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/ssl/universal/settings')
        mock_response = '{"result": {"enabled": true}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
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
                service.get_universal_certificate_setting(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for change_universal_certificate_setting
#-----------------------------------------------------------------------------
class TestChangeUniversalCertificateSetting():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # change_universal_certificate_setting()
    #--------------------------------------------------------
    @responses.activate
    def test_change_universal_certificate_setting_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/ssl/universal/settings')
        responses.add(responses.PATCH,
                      url,
                      status=200)

        # Set up parameter values
        enabled = True

        # Invoke method
        response = service.change_universal_certificate_setting(
            enabled=enabled,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['enabled'] == True


    #--------------------------------------------------------
    # test_change_universal_certificate_setting_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_change_universal_certificate_setting_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/ssl/universal/settings')
        responses.add(responses.PATCH,
                      url,
                      status=200)

        # Invoke method
        response = service.change_universal_certificate_setting()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_change_universal_certificate_setting_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_change_universal_certificate_setting_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/ssl/universal/settings')
        responses.add(responses.PATCH,
                      url,
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.change_universal_certificate_setting(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_tls12_setting
#-----------------------------------------------------------------------------
class TestGetTls12Setting():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_tls12_setting()
    #--------------------------------------------------------
    @responses.activate
    def test_get_tls12_setting_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/tls_1_2_only')
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
    # test_get_tls12_setting_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_tls12_setting_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/tls_1_2_only')
        mock_response = '{"result": {"id": "tls_1_2_only", "value": "on", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
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
                service.get_tls12_setting(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for change_tls12_setting
#-----------------------------------------------------------------------------
class TestChangeTls12Setting():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # change_tls12_setting()
    #--------------------------------------------------------
    @responses.activate
    def test_change_tls12_setting_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/tls_1_2_only')
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
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'on'


    #--------------------------------------------------------
    # test_change_tls12_setting_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_change_tls12_setting_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/tls_1_2_only')
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


    #--------------------------------------------------------
    # test_change_tls12_setting_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_change_tls12_setting_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/tls_1_2_only')
        mock_response = '{"result": {"id": "tls_1_2_only", "value": "on", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.PATCH,
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
                service.change_tls12_setting(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for get_tls13_setting
#-----------------------------------------------------------------------------
class TestGetTls13Setting():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # get_tls13_setting()
    #--------------------------------------------------------
    @responses.activate
    def test_get_tls13_setting_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/tls_1_3')
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
    # test_get_tls13_setting_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_get_tls13_setting_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/tls_1_3')
        mock_response = '{"result": {"id": "tls_1_3", "value": "on", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
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
                service.get_tls13_setting(**req_copy)



#-----------------------------------------------------------------------------
# Test Class for change_tls13_setting
#-----------------------------------------------------------------------------
class TestChangeTls13Setting():

    # Preprocess the request URL to ensure the mock response will be found.
    def preprocess_url(self, request_url: str):
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    #--------------------------------------------------------
    # change_tls13_setting()
    #--------------------------------------------------------
    @responses.activate
    def test_change_tls13_setting_all_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/tls_1_3')
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
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'on'


    #--------------------------------------------------------
    # test_change_tls13_setting_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_change_tls13_setting_required_params(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/tls_1_3')
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


    #--------------------------------------------------------
    # test_change_tls13_setting_value_error()
    #--------------------------------------------------------
    @responses.activate
    def test_change_tls13_setting_value_error(self):
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/testString/zones/testString/settings/tls_1_3')
        mock_response = '{"result": {"id": "tls_1_3", "value": "on", "editable": true, "modified_on": "2019-01-01T12:00:00"}, "success": true, "errors": [["errors"]], "messages": [{"status": "OK"}]}'
        responses.add(responses.PATCH,
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
                service.change_tls13_setting(**req_copy)



# endregion
##############################################################################
# End of Service: SSLCertificate
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
#-----------------------------------------------------------------------------
# Test Class for CertPriorityReqCertificatesItem
#-----------------------------------------------------------------------------
class TestCertPriorityReqCertificatesItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for CertPriorityReqCertificatesItem
    #--------------------------------------------------------
    def test_cert_priority_req_certificates_item_serialization(self):

        # Construct a json representation of a CertPriorityReqCertificatesItem model
        cert_priority_req_certificates_item_model_json = {}
        cert_priority_req_certificates_item_model_json['id'] = '5a7805061c76ada191ed06f989cc3dac'
        cert_priority_req_certificates_item_model_json['priority'] = 1

        # Construct a model instance of CertPriorityReqCertificatesItem by calling from_dict on the json representation
        cert_priority_req_certificates_item_model = CertPriorityReqCertificatesItem.from_dict(cert_priority_req_certificates_item_model_json)
        assert cert_priority_req_certificates_item_model != False

        # Construct a model instance of CertPriorityReqCertificatesItem by calling from_dict on the json representation
        cert_priority_req_certificates_item_model_dict = CertPriorityReqCertificatesItem.from_dict(cert_priority_req_certificates_item_model_json).__dict__
        cert_priority_req_certificates_item_model2 = CertPriorityReqCertificatesItem(**cert_priority_req_certificates_item_model_dict)

        # Verify the model instances are equivalent
        assert cert_priority_req_certificates_item_model == cert_priority_req_certificates_item_model2

        # Convert model instance back to dict and verify no loss of data
        cert_priority_req_certificates_item_model_json2 = cert_priority_req_certificates_item_model.to_dict()
        assert cert_priority_req_certificates_item_model_json2 == cert_priority_req_certificates_item_model_json

#-----------------------------------------------------------------------------
# Test Class for CustomCertReqGeoRestrictions
#-----------------------------------------------------------------------------
class TestCustomCertReqGeoRestrictions():

    #--------------------------------------------------------
    # Test serialization/deserialization for CustomCertReqGeoRestrictions
    #--------------------------------------------------------
    def test_custom_cert_req_geo_restrictions_serialization(self):

        # Construct a json representation of a CustomCertReqGeoRestrictions model
        custom_cert_req_geo_restrictions_model_json = {}
        custom_cert_req_geo_restrictions_model_json['label'] = 'us'

        # Construct a model instance of CustomCertReqGeoRestrictions by calling from_dict on the json representation
        custom_cert_req_geo_restrictions_model = CustomCertReqGeoRestrictions.from_dict(custom_cert_req_geo_restrictions_model_json)
        assert custom_cert_req_geo_restrictions_model != False

        # Construct a model instance of CustomCertReqGeoRestrictions by calling from_dict on the json representation
        custom_cert_req_geo_restrictions_model_dict = CustomCertReqGeoRestrictions.from_dict(custom_cert_req_geo_restrictions_model_json).__dict__
        custom_cert_req_geo_restrictions_model2 = CustomCertReqGeoRestrictions(**custom_cert_req_geo_restrictions_model_dict)

        # Verify the model instances are equivalent
        assert custom_cert_req_geo_restrictions_model == custom_cert_req_geo_restrictions_model2

        # Convert model instance back to dict and verify no loss of data
        custom_cert_req_geo_restrictions_model_json2 = custom_cert_req_geo_restrictions_model.to_dict()
        assert custom_cert_req_geo_restrictions_model_json2 == custom_cert_req_geo_restrictions_model_json

#-----------------------------------------------------------------------------
# Test Class for Tls12SettingRespMessagesItem
#-----------------------------------------------------------------------------
class TestTls12SettingRespMessagesItem():

    #--------------------------------------------------------
    # Test serialization/deserialization for Tls12SettingRespMessagesItem
    #--------------------------------------------------------
    def test_tls12_setting_resp_messages_item_serialization(self):

        # Construct a json representation of a Tls12SettingRespMessagesItem model
        tls12_setting_resp_messages_item_model_json = {}
        tls12_setting_resp_messages_item_model_json['status'] = 'OK'

        # Construct a model instance of Tls12SettingRespMessagesItem by calling from_dict on the json representation
        tls12_setting_resp_messages_item_model = Tls12SettingRespMessagesItem.from_dict(tls12_setting_resp_messages_item_model_json)
        assert tls12_setting_resp_messages_item_model != False

        # Construct a model instance of Tls12SettingRespMessagesItem by calling from_dict on the json representation
        tls12_setting_resp_messages_item_model_dict = Tls12SettingRespMessagesItem.from_dict(tls12_setting_resp_messages_item_model_json).__dict__
        tls12_setting_resp_messages_item_model2 = Tls12SettingRespMessagesItem(**tls12_setting_resp_messages_item_model_dict)

        # Verify the model instances are equivalent
        assert tls12_setting_resp_messages_item_model == tls12_setting_resp_messages_item_model2

        # Convert model instance back to dict and verify no loss of data
        tls12_setting_resp_messages_item_model_json2 = tls12_setting_resp_messages_item_model.to_dict()
        assert tls12_setting_resp_messages_item_model_json2 == tls12_setting_resp_messages_item_model_json

#-----------------------------------------------------------------------------
# Test Class for Tls12SettingRespResult
#-----------------------------------------------------------------------------
class TestTls12SettingRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for Tls12SettingRespResult
    #--------------------------------------------------------
    def test_tls12_setting_resp_result_serialization(self):

        # Construct a json representation of a Tls12SettingRespResult model
        tls12_setting_resp_result_model_json = {}
        tls12_setting_resp_result_model_json['id'] = 'tls_1_2_only'
        tls12_setting_resp_result_model_json['value'] = 'on'
        tls12_setting_resp_result_model_json['editable'] = True
        tls12_setting_resp_result_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of Tls12SettingRespResult by calling from_dict on the json representation
        tls12_setting_resp_result_model = Tls12SettingRespResult.from_dict(tls12_setting_resp_result_model_json)
        assert tls12_setting_resp_result_model != False

        # Construct a model instance of Tls12SettingRespResult by calling from_dict on the json representation
        tls12_setting_resp_result_model_dict = Tls12SettingRespResult.from_dict(tls12_setting_resp_result_model_json).__dict__
        tls12_setting_resp_result_model2 = Tls12SettingRespResult(**tls12_setting_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert tls12_setting_resp_result_model == tls12_setting_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        tls12_setting_resp_result_model_json2 = tls12_setting_resp_result_model.to_dict()
        assert tls12_setting_resp_result_model_json2 == tls12_setting_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for Tls13SettingRespResult
#-----------------------------------------------------------------------------
class TestTls13SettingRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for Tls13SettingRespResult
    #--------------------------------------------------------
    def test_tls13_setting_resp_result_serialization(self):

        # Construct a json representation of a Tls13SettingRespResult model
        tls13_setting_resp_result_model_json = {}
        tls13_setting_resp_result_model_json['id'] = 'tls_1_3'
        tls13_setting_resp_result_model_json['value'] = 'on'
        tls13_setting_resp_result_model_json['editable'] = True
        tls13_setting_resp_result_model_json['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of Tls13SettingRespResult by calling from_dict on the json representation
        tls13_setting_resp_result_model = Tls13SettingRespResult.from_dict(tls13_setting_resp_result_model_json)
        assert tls13_setting_resp_result_model != False

        # Construct a model instance of Tls13SettingRespResult by calling from_dict on the json representation
        tls13_setting_resp_result_model_dict = Tls13SettingRespResult.from_dict(tls13_setting_resp_result_model_json).__dict__
        tls13_setting_resp_result_model2 = Tls13SettingRespResult(**tls13_setting_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert tls13_setting_resp_result_model == tls13_setting_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        tls13_setting_resp_result_model_json2 = tls13_setting_resp_result_model.to_dict()
        assert tls13_setting_resp_result_model_json2 == tls13_setting_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for UniversalSettingRespResult
#-----------------------------------------------------------------------------
class TestUniversalSettingRespResult():

    #--------------------------------------------------------
    # Test serialization/deserialization for UniversalSettingRespResult
    #--------------------------------------------------------
    def test_universal_setting_resp_result_serialization(self):

        # Construct a json representation of a UniversalSettingRespResult model
        universal_setting_resp_result_model_json = {}
        universal_setting_resp_result_model_json['enabled'] = True

        # Construct a model instance of UniversalSettingRespResult by calling from_dict on the json representation
        universal_setting_resp_result_model = UniversalSettingRespResult.from_dict(universal_setting_resp_result_model_json)
        assert universal_setting_resp_result_model != False

        # Construct a model instance of UniversalSettingRespResult by calling from_dict on the json representation
        universal_setting_resp_result_model_dict = UniversalSettingRespResult.from_dict(universal_setting_resp_result_model_json).__dict__
        universal_setting_resp_result_model2 = UniversalSettingRespResult(**universal_setting_resp_result_model_dict)

        # Verify the model instances are equivalent
        assert universal_setting_resp_result_model == universal_setting_resp_result_model2

        # Convert model instance back to dict and verify no loss of data
        universal_setting_resp_result_model_json2 = universal_setting_resp_result_model.to_dict()
        assert universal_setting_resp_result_model_json2 == universal_setting_resp_result_model_json

#-----------------------------------------------------------------------------
# Test Class for Certificate
#-----------------------------------------------------------------------------
class TestCertificate():

    #--------------------------------------------------------
    # Test serialization/deserialization for Certificate
    #--------------------------------------------------------
    def test_certificate_serialization(self):

        # Construct a json representation of a Certificate model
        certificate_model_json = {}
        certificate_model_json['id'] = { 'foo': 'bar' }
        certificate_model_json['hosts'] = ['example.com']
        certificate_model_json['status'] = 'active'

        # Construct a model instance of Certificate by calling from_dict on the json representation
        certificate_model = Certificate.from_dict(certificate_model_json)
        assert certificate_model != False

        # Construct a model instance of Certificate by calling from_dict on the json representation
        certificate_model_dict = Certificate.from_dict(certificate_model_json).__dict__
        certificate_model2 = Certificate(**certificate_model_dict)

        # Verify the model instances are equivalent
        assert certificate_model == certificate_model2

        # Convert model instance back to dict and verify no loss of data
        certificate_model_json2 = certificate_model.to_dict()
        assert certificate_model_json2 == certificate_model_json

#-----------------------------------------------------------------------------
# Test Class for CustomCertPack
#-----------------------------------------------------------------------------
class TestCustomCertPack():

    #--------------------------------------------------------
    # Test serialization/deserialization for CustomCertPack
    #--------------------------------------------------------
    def test_custom_cert_pack_serialization(self):

        # Construct a json representation of a CustomCertPack model
        custom_cert_pack_model_json = {}
        custom_cert_pack_model_json['id'] = '0f405ba2-8c18-49eb-a30b-28b85427780f'
        custom_cert_pack_model_json['hosts'] = ['example.com']
        custom_cert_pack_model_json['issuer'] = '/Country=US/Organization=Lets Encrypt/CommonName=Lets Encrypt Authority X3'
        custom_cert_pack_model_json['signature'] = 'SHA256WithRSA'
        custom_cert_pack_model_json['status'] = 'active'
        custom_cert_pack_model_json['bundle_method'] = 'testString'
        custom_cert_pack_model_json['zone_id'] = 'testString'
        custom_cert_pack_model_json['uploaded_on'] = 'testString'
        custom_cert_pack_model_json['modified_on'] = 'testString'
        custom_cert_pack_model_json['expires_on'] = 'testString'
        custom_cert_pack_model_json['priority'] = 36.0

        # Construct a model instance of CustomCertPack by calling from_dict on the json representation
        custom_cert_pack_model = CustomCertPack.from_dict(custom_cert_pack_model_json)
        assert custom_cert_pack_model != False

        # Construct a model instance of CustomCertPack by calling from_dict on the json representation
        custom_cert_pack_model_dict = CustomCertPack.from_dict(custom_cert_pack_model_json).__dict__
        custom_cert_pack_model2 = CustomCertPack(**custom_cert_pack_model_dict)

        # Verify the model instances are equivalent
        assert custom_cert_pack_model == custom_cert_pack_model2

        # Convert model instance back to dict and verify no loss of data
        custom_cert_pack_model_json2 = custom_cert_pack_model.to_dict()
        assert custom_cert_pack_model_json2 == custom_cert_pack_model_json

#-----------------------------------------------------------------------------
# Test Class for CustomCertResp
#-----------------------------------------------------------------------------
class TestCustomCertResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for CustomCertResp
    #--------------------------------------------------------
    def test_custom_cert_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        custom_cert_pack_model = {} # CustomCertPack
        custom_cert_pack_model['id'] = '0f405ba2-8c18-49eb-a30b-28b85427780f'
        custom_cert_pack_model['hosts'] = ['example.com']
        custom_cert_pack_model['issuer'] = '/Country=US/Organization=Lets Encrypt/CommonName=Lets Encrypt Authority X3'
        custom_cert_pack_model['signature'] = 'SHA256WithRSA'
        custom_cert_pack_model['status'] = 'active'
        custom_cert_pack_model['bundle_method'] = 'testString'
        custom_cert_pack_model['zone_id'] = 'testString'
        custom_cert_pack_model['uploaded_on'] = 'testString'
        custom_cert_pack_model['modified_on'] = 'testString'
        custom_cert_pack_model['expires_on'] = 'testString'
        custom_cert_pack_model['priority'] = 36.0

        tls12_setting_resp_messages_item_model = {} # Tls12SettingRespMessagesItem
        tls12_setting_resp_messages_item_model['status'] = 'OK'

        # Construct a json representation of a CustomCertResp model
        custom_cert_resp_model_json = {}
        custom_cert_resp_model_json['result'] = custom_cert_pack_model
        custom_cert_resp_model_json['success'] = True
        custom_cert_resp_model_json['errors'] = [['testString']]
        custom_cert_resp_model_json['messages'] = [tls12_setting_resp_messages_item_model]

        # Construct a model instance of CustomCertResp by calling from_dict on the json representation
        custom_cert_resp_model = CustomCertResp.from_dict(custom_cert_resp_model_json)
        assert custom_cert_resp_model != False

        # Construct a model instance of CustomCertResp by calling from_dict on the json representation
        custom_cert_resp_model_dict = CustomCertResp.from_dict(custom_cert_resp_model_json).__dict__
        custom_cert_resp_model2 = CustomCertResp(**custom_cert_resp_model_dict)

        # Verify the model instances are equivalent
        assert custom_cert_resp_model == custom_cert_resp_model2

        # Convert model instance back to dict and verify no loss of data
        custom_cert_resp_model_json2 = custom_cert_resp_model.to_dict()
        assert custom_cert_resp_model_json2 == custom_cert_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for DedicatedCertificatePack
#-----------------------------------------------------------------------------
class TestDedicatedCertificatePack():

    #--------------------------------------------------------
    # Test serialization/deserialization for DedicatedCertificatePack
    #--------------------------------------------------------
    def test_dedicated_certificate_pack_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        certificate_model = {} # Certificate
        certificate_model['id'] = { 'foo': 'bar' }
        certificate_model['hosts'] = ['example.com']
        certificate_model['status'] = 'active'

        # Construct a json representation of a DedicatedCertificatePack model
        dedicated_certificate_pack_model_json = {}
        dedicated_certificate_pack_model_json['id'] = '0f405ba2-8c18-49eb-a30b-28b85427780f'
        dedicated_certificate_pack_model_json['type'] = 'dedicated'
        dedicated_certificate_pack_model_json['hosts'] = ['example.com']
        dedicated_certificate_pack_model_json['certificates'] = [certificate_model]
        dedicated_certificate_pack_model_json['primary_certificate'] = { 'foo': 'bar' }
        dedicated_certificate_pack_model_json['status'] = 'active'

        # Construct a model instance of DedicatedCertificatePack by calling from_dict on the json representation
        dedicated_certificate_pack_model = DedicatedCertificatePack.from_dict(dedicated_certificate_pack_model_json)
        assert dedicated_certificate_pack_model != False

        # Construct a model instance of DedicatedCertificatePack by calling from_dict on the json representation
        dedicated_certificate_pack_model_dict = DedicatedCertificatePack.from_dict(dedicated_certificate_pack_model_json).__dict__
        dedicated_certificate_pack_model2 = DedicatedCertificatePack(**dedicated_certificate_pack_model_dict)

        # Verify the model instances are equivalent
        assert dedicated_certificate_pack_model == dedicated_certificate_pack_model2

        # Convert model instance back to dict and verify no loss of data
        dedicated_certificate_pack_model_json2 = dedicated_certificate_pack_model.to_dict()
        assert dedicated_certificate_pack_model_json2 == dedicated_certificate_pack_model_json

#-----------------------------------------------------------------------------
# Test Class for DedicatedCertificateResp
#-----------------------------------------------------------------------------
class TestDedicatedCertificateResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for DedicatedCertificateResp
    #--------------------------------------------------------
    def test_dedicated_certificate_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        certificate_model = {} # Certificate
        certificate_model['id'] = { 'foo': 'bar' }
        certificate_model['hosts'] = ['example.com']
        certificate_model['status'] = 'active'

        dedicated_certificate_pack_model = {} # DedicatedCertificatePack
        dedicated_certificate_pack_model['id'] = '0f405ba2-8c18-49eb-a30b-28b85427780f'
        dedicated_certificate_pack_model['type'] = 'dedicated'
        dedicated_certificate_pack_model['hosts'] = ['example.com']
        dedicated_certificate_pack_model['certificates'] = [certificate_model]
        dedicated_certificate_pack_model['primary_certificate'] = { 'foo': 'bar' }
        dedicated_certificate_pack_model['status'] = 'active'

        result_info_model = {} # ResultInfo
        result_info_model['page'] = 1
        result_info_model['per_page'] = 2
        result_info_model['count'] = 1
        result_info_model['total_count'] = 200

        tls12_setting_resp_messages_item_model = {} # Tls12SettingRespMessagesItem
        tls12_setting_resp_messages_item_model['status'] = 'OK'

        # Construct a json representation of a DedicatedCertificateResp model
        dedicated_certificate_resp_model_json = {}
        dedicated_certificate_resp_model_json['result'] = dedicated_certificate_pack_model
        dedicated_certificate_resp_model_json['result_info'] = result_info_model
        dedicated_certificate_resp_model_json['success'] = True
        dedicated_certificate_resp_model_json['errors'] = [['testString']]
        dedicated_certificate_resp_model_json['messages'] = [tls12_setting_resp_messages_item_model]

        # Construct a model instance of DedicatedCertificateResp by calling from_dict on the json representation
        dedicated_certificate_resp_model = DedicatedCertificateResp.from_dict(dedicated_certificate_resp_model_json)
        assert dedicated_certificate_resp_model != False

        # Construct a model instance of DedicatedCertificateResp by calling from_dict on the json representation
        dedicated_certificate_resp_model_dict = DedicatedCertificateResp.from_dict(dedicated_certificate_resp_model_json).__dict__
        dedicated_certificate_resp_model2 = DedicatedCertificateResp(**dedicated_certificate_resp_model_dict)

        # Verify the model instances are equivalent
        assert dedicated_certificate_resp_model == dedicated_certificate_resp_model2

        # Convert model instance back to dict and verify no loss of data
        dedicated_certificate_resp_model_json2 = dedicated_certificate_resp_model.to_dict()
        assert dedicated_certificate_resp_model_json2 == dedicated_certificate_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for ListCertificateResp
#-----------------------------------------------------------------------------
class TestListCertificateResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for ListCertificateResp
    #--------------------------------------------------------
    def test_list_certificate_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        certificate_model = {} # Certificate
        certificate_model['id'] = { 'foo': 'bar' }
        certificate_model['hosts'] = ['example.com']
        certificate_model['status'] = 'active'

        dedicated_certificate_pack_model = {} # DedicatedCertificatePack
        dedicated_certificate_pack_model['id'] = '0f405ba2-8c18-49eb-a30b-28b85427780f'
        dedicated_certificate_pack_model['type'] = 'dedicated'
        dedicated_certificate_pack_model['hosts'] = ['example.com']
        dedicated_certificate_pack_model['certificates'] = [certificate_model]
        dedicated_certificate_pack_model['primary_certificate'] = { 'foo': 'bar' }
        dedicated_certificate_pack_model['status'] = 'active'

        result_info_model = {} # ResultInfo
        result_info_model['page'] = 1
        result_info_model['per_page'] = 2
        result_info_model['count'] = 1
        result_info_model['total_count'] = 200

        tls12_setting_resp_messages_item_model = {} # Tls12SettingRespMessagesItem
        tls12_setting_resp_messages_item_model['status'] = 'OK'

        # Construct a json representation of a ListCertificateResp model
        list_certificate_resp_model_json = {}
        list_certificate_resp_model_json['result'] = [dedicated_certificate_pack_model]
        list_certificate_resp_model_json['result_info'] = result_info_model
        list_certificate_resp_model_json['success'] = True
        list_certificate_resp_model_json['errors'] = [['testString']]
        list_certificate_resp_model_json['messages'] = [tls12_setting_resp_messages_item_model]

        # Construct a model instance of ListCertificateResp by calling from_dict on the json representation
        list_certificate_resp_model = ListCertificateResp.from_dict(list_certificate_resp_model_json)
        assert list_certificate_resp_model != False

        # Construct a model instance of ListCertificateResp by calling from_dict on the json representation
        list_certificate_resp_model_dict = ListCertificateResp.from_dict(list_certificate_resp_model_json).__dict__
        list_certificate_resp_model2 = ListCertificateResp(**list_certificate_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_certificate_resp_model == list_certificate_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_certificate_resp_model_json2 = list_certificate_resp_model.to_dict()
        assert list_certificate_resp_model_json2 == list_certificate_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for ListCustomCertsResp
#-----------------------------------------------------------------------------
class TestListCustomCertsResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for ListCustomCertsResp
    #--------------------------------------------------------
    def test_list_custom_certs_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        custom_cert_pack_model = {} # CustomCertPack
        custom_cert_pack_model['id'] = '0f405ba2-8c18-49eb-a30b-28b85427780f'
        custom_cert_pack_model['hosts'] = ['example.com']
        custom_cert_pack_model['issuer'] = '/Country=US/Organization=Lets Encrypt/CommonName=Lets Encrypt Authority X3'
        custom_cert_pack_model['signature'] = 'SHA256WithRSA'
        custom_cert_pack_model['status'] = 'active'
        custom_cert_pack_model['bundle_method'] = 'testString'
        custom_cert_pack_model['zone_id'] = 'testString'
        custom_cert_pack_model['uploaded_on'] = 'testString'
        custom_cert_pack_model['modified_on'] = 'testString'
        custom_cert_pack_model['expires_on'] = 'testString'
        custom_cert_pack_model['priority'] = 36.0

        result_info_model = {} # ResultInfo
        result_info_model['page'] = 1
        result_info_model['per_page'] = 2
        result_info_model['count'] = 1
        result_info_model['total_count'] = 200

        tls12_setting_resp_messages_item_model = {} # Tls12SettingRespMessagesItem
        tls12_setting_resp_messages_item_model['status'] = 'OK'

        # Construct a json representation of a ListCustomCertsResp model
        list_custom_certs_resp_model_json = {}
        list_custom_certs_resp_model_json['result'] = [custom_cert_pack_model]
        list_custom_certs_resp_model_json['result_info'] = result_info_model
        list_custom_certs_resp_model_json['success'] = True
        list_custom_certs_resp_model_json['errors'] = [['testString']]
        list_custom_certs_resp_model_json['messages'] = [tls12_setting_resp_messages_item_model]

        # Construct a model instance of ListCustomCertsResp by calling from_dict on the json representation
        list_custom_certs_resp_model = ListCustomCertsResp.from_dict(list_custom_certs_resp_model_json)
        assert list_custom_certs_resp_model != False

        # Construct a model instance of ListCustomCertsResp by calling from_dict on the json representation
        list_custom_certs_resp_model_dict = ListCustomCertsResp.from_dict(list_custom_certs_resp_model_json).__dict__
        list_custom_certs_resp_model2 = ListCustomCertsResp(**list_custom_certs_resp_model_dict)

        # Verify the model instances are equivalent
        assert list_custom_certs_resp_model == list_custom_certs_resp_model2

        # Convert model instance back to dict and verify no loss of data
        list_custom_certs_resp_model_json2 = list_custom_certs_resp_model.to_dict()
        assert list_custom_certs_resp_model_json2 == list_custom_certs_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for ResultInfo
#-----------------------------------------------------------------------------
class TestResultInfo():

    #--------------------------------------------------------
    # Test serialization/deserialization for ResultInfo
    #--------------------------------------------------------
    def test_result_info_serialization(self):

        # Construct a json representation of a ResultInfo model
        result_info_model_json = {}
        result_info_model_json['page'] = 1
        result_info_model_json['per_page'] = 2
        result_info_model_json['count'] = 1
        result_info_model_json['total_count'] = 200

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

#-----------------------------------------------------------------------------
# Test Class for SslSetting
#-----------------------------------------------------------------------------
class TestSslSetting():

    #--------------------------------------------------------
    # Test serialization/deserialization for SslSetting
    #--------------------------------------------------------
    def test_ssl_setting_serialization(self):

        # Construct a json representation of a SslSetting model
        ssl_setting_model_json = {}
        ssl_setting_model_json['id'] = 'ssl'
        ssl_setting_model_json['value'] = 'off'
        ssl_setting_model_json['editable'] = True
        ssl_setting_model_json['modified_on'] = '2017-01-01T05:20:00.12345Z'

        # Construct a model instance of SslSetting by calling from_dict on the json representation
        ssl_setting_model = SslSetting.from_dict(ssl_setting_model_json)
        assert ssl_setting_model != False

        # Construct a model instance of SslSetting by calling from_dict on the json representation
        ssl_setting_model_dict = SslSetting.from_dict(ssl_setting_model_json).__dict__
        ssl_setting_model2 = SslSetting(**ssl_setting_model_dict)

        # Verify the model instances are equivalent
        assert ssl_setting_model == ssl_setting_model2

        # Convert model instance back to dict and verify no loss of data
        ssl_setting_model_json2 = ssl_setting_model.to_dict()
        assert ssl_setting_model_json2 == ssl_setting_model_json

#-----------------------------------------------------------------------------
# Test Class for SslSettingResp
#-----------------------------------------------------------------------------
class TestSslSettingResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for SslSettingResp
    #--------------------------------------------------------
    def test_ssl_setting_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        ssl_setting_model = {} # SslSetting
        ssl_setting_model['id'] = 'ssl'
        ssl_setting_model['value'] = 'off'
        ssl_setting_model['editable'] = True
        ssl_setting_model['modified_on'] = '2017-01-01T05:20:00.12345Z'

        tls12_setting_resp_messages_item_model = {} # Tls12SettingRespMessagesItem
        tls12_setting_resp_messages_item_model['status'] = 'OK'

        # Construct a json representation of a SslSettingResp model
        ssl_setting_resp_model_json = {}
        ssl_setting_resp_model_json['success'] = True
        ssl_setting_resp_model_json['result'] = ssl_setting_model
        ssl_setting_resp_model_json['errors'] = [['testString']]
        ssl_setting_resp_model_json['messages'] = [tls12_setting_resp_messages_item_model]

        # Construct a model instance of SslSettingResp by calling from_dict on the json representation
        ssl_setting_resp_model = SslSettingResp.from_dict(ssl_setting_resp_model_json)
        assert ssl_setting_resp_model != False

        # Construct a model instance of SslSettingResp by calling from_dict on the json representation
        ssl_setting_resp_model_dict = SslSettingResp.from_dict(ssl_setting_resp_model_json).__dict__
        ssl_setting_resp_model2 = SslSettingResp(**ssl_setting_resp_model_dict)

        # Verify the model instances are equivalent
        assert ssl_setting_resp_model == ssl_setting_resp_model2

        # Convert model instance back to dict and verify no loss of data
        ssl_setting_resp_model_json2 = ssl_setting_resp_model.to_dict()
        assert ssl_setting_resp_model_json2 == ssl_setting_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for Tls12SettingResp
#-----------------------------------------------------------------------------
class TestTls12SettingResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for Tls12SettingResp
    #--------------------------------------------------------
    def test_tls12_setting_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        tls12_setting_resp_messages_item_model = {} # Tls12SettingRespMessagesItem
        tls12_setting_resp_messages_item_model['status'] = 'OK'

        tls12_setting_resp_result_model = {} # Tls12SettingRespResult
        tls12_setting_resp_result_model['id'] = 'tls_1_2_only'
        tls12_setting_resp_result_model['value'] = 'on'
        tls12_setting_resp_result_model['editable'] = True
        tls12_setting_resp_result_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a Tls12SettingResp model
        tls12_setting_resp_model_json = {}
        tls12_setting_resp_model_json['result'] = tls12_setting_resp_result_model
        tls12_setting_resp_model_json['success'] = True
        tls12_setting_resp_model_json['errors'] = [['testString']]
        tls12_setting_resp_model_json['messages'] = [tls12_setting_resp_messages_item_model]

        # Construct a model instance of Tls12SettingResp by calling from_dict on the json representation
        tls12_setting_resp_model = Tls12SettingResp.from_dict(tls12_setting_resp_model_json)
        assert tls12_setting_resp_model != False

        # Construct a model instance of Tls12SettingResp by calling from_dict on the json representation
        tls12_setting_resp_model_dict = Tls12SettingResp.from_dict(tls12_setting_resp_model_json).__dict__
        tls12_setting_resp_model2 = Tls12SettingResp(**tls12_setting_resp_model_dict)

        # Verify the model instances are equivalent
        assert tls12_setting_resp_model == tls12_setting_resp_model2

        # Convert model instance back to dict and verify no loss of data
        tls12_setting_resp_model_json2 = tls12_setting_resp_model.to_dict()
        assert tls12_setting_resp_model_json2 == tls12_setting_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for Tls13SettingResp
#-----------------------------------------------------------------------------
class TestTls13SettingResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for Tls13SettingResp
    #--------------------------------------------------------
    def test_tls13_setting_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        tls12_setting_resp_messages_item_model = {} # Tls12SettingRespMessagesItem
        tls12_setting_resp_messages_item_model['status'] = 'OK'

        tls13_setting_resp_result_model = {} # Tls13SettingRespResult
        tls13_setting_resp_result_model['id'] = 'tls_1_3'
        tls13_setting_resp_result_model['value'] = 'on'
        tls13_setting_resp_result_model['editable'] = True
        tls13_setting_resp_result_model['modified_on'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a Tls13SettingResp model
        tls13_setting_resp_model_json = {}
        tls13_setting_resp_model_json['result'] = tls13_setting_resp_result_model
        tls13_setting_resp_model_json['success'] = True
        tls13_setting_resp_model_json['errors'] = [['testString']]
        tls13_setting_resp_model_json['messages'] = [tls12_setting_resp_messages_item_model]

        # Construct a model instance of Tls13SettingResp by calling from_dict on the json representation
        tls13_setting_resp_model = Tls13SettingResp.from_dict(tls13_setting_resp_model_json)
        assert tls13_setting_resp_model != False

        # Construct a model instance of Tls13SettingResp by calling from_dict on the json representation
        tls13_setting_resp_model_dict = Tls13SettingResp.from_dict(tls13_setting_resp_model_json).__dict__
        tls13_setting_resp_model2 = Tls13SettingResp(**tls13_setting_resp_model_dict)

        # Verify the model instances are equivalent
        assert tls13_setting_resp_model == tls13_setting_resp_model2

        # Convert model instance back to dict and verify no loss of data
        tls13_setting_resp_model_json2 = tls13_setting_resp_model.to_dict()
        assert tls13_setting_resp_model_json2 == tls13_setting_resp_model_json

#-----------------------------------------------------------------------------
# Test Class for UniversalSettingResp
#-----------------------------------------------------------------------------
class TestUniversalSettingResp():

    #--------------------------------------------------------
    # Test serialization/deserialization for UniversalSettingResp
    #--------------------------------------------------------
    def test_universal_setting_resp_serialization(self):

        # Construct dict forms of any model objects needed in order to build this model.

        tls12_setting_resp_messages_item_model = {} # Tls12SettingRespMessagesItem
        tls12_setting_resp_messages_item_model['status'] = 'OK'

        universal_setting_resp_result_model = {} # UniversalSettingRespResult
        universal_setting_resp_result_model['enabled'] = True

        # Construct a json representation of a UniversalSettingResp model
        universal_setting_resp_model_json = {}
        universal_setting_resp_model_json['result'] = universal_setting_resp_result_model
        universal_setting_resp_model_json['success'] = True
        universal_setting_resp_model_json['errors'] = [['testString']]
        universal_setting_resp_model_json['messages'] = [tls12_setting_resp_messages_item_model]

        # Construct a model instance of UniversalSettingResp by calling from_dict on the json representation
        universal_setting_resp_model = UniversalSettingResp.from_dict(universal_setting_resp_model_json)
        assert universal_setting_resp_model != False

        # Construct a model instance of UniversalSettingResp by calling from_dict on the json representation
        universal_setting_resp_model_dict = UniversalSettingResp.from_dict(universal_setting_resp_model_json).__dict__
        universal_setting_resp_model2 = UniversalSettingResp(**universal_setting_resp_model_dict)

        # Verify the model instances are equivalent
        assert universal_setting_resp_model == universal_setting_resp_model2

        # Convert model instance back to dict and verify no loss of data
        universal_setting_resp_model_json2 = universal_setting_resp_model.to_dict()
        assert universal_setting_resp_model_json2 == universal_setting_resp_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
