# coding: utf-8

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

"""
SSL Certificate
"""

from datetime import datetime
from enum import Enum
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model, datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class SslCertificateApiV1(BaseService):
    """The SSL Certificate API V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'ssl_certificate_api'

    @classmethod
    def new_instance(cls,
                     crn: str,
                     zone_identifier: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'SslCertificateApiV1':
        """
        Return a new client for the SSL Certificate API service using the specified
               parameters and external configuration.

        :param str crn: cloud resource name.

        :param str zone_identifier: zone identifier.
        """
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_identifier is None:
            raise ValueError('zone_identifier must be provided')

        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            crn,
            zone_identifier,
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(self,
                 crn: str,
                 zone_identifier: str,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the SSL Certificate API service.

        :param str crn: cloud resource name.

        :param str zone_identifier: zone identifier.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_identifier is None:
            raise ValueError('zone_identifier must be provided')

        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)
        self.crn = crn
        self.zone_identifier = zone_identifier


    #########################
    # List certificates
    #########################


    def list_certificates(self, *, x_correlation_id: str = None, **kwargs) -> DetailedResponse:
        """
        List all certificates.

        CIS automatically add an active DNS zone to a universal SSL certificate, shared
        among multiple customers. Customer may order dedicated certificates for the owning
        zones. This API list all certificates for a given zone, including shared and
        dedicated certificates.

        :param str x_correlation_id: (optional) uuid, identify a session.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListCertificateResp` object
        """

        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='list_certificates')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/ssl/certificate_packs'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Order a certificate
    #########################


    def order_certificate(self, *, type: str = None, hosts: List[str] = None, x_correlation_id: str = None, **kwargs) -> DetailedResponse:
        """
        Order a dedicated certificate.

        Order a dedicated certificate for a given zone. The zone should be active before
        placing an order of a dedicated certificate.

        :param str type: (optional) priorities.
        :param List[str] hosts: (optional) host name.
        :param str x_correlation_id: (optional) uuid, identify a session.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DedicatedCertificatePack` object
        """

        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='order_certificate')
        headers.update(sdk_headers)

        data = {
            'type': type,
            'hosts': hosts
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/ssl/certificate_packs'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Delete a certificate
    #########################


    def delete_certificate(self, cert_identifier: str, *, x_correlation_id: str = None, **kwargs) -> DetailedResponse:
        """
        Delete a certificate.

        Delete a given certificate.

        :param str cert_identifier: cedrtificate identifier.
        :param str x_correlation_id: (optional) uuid, identify a session.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if cert_identifier is None:
            raise ValueError('cert_identifier must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='delete_certificate')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/ssl/certificate_packs/{2}'.format(*self.encode_path_vars(self.crn, self.zone_identifier, cert_identifier))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Get SSL setting
    #########################


    def get_ssl_setting(self, **kwargs) -> DetailedResponse:
        """
        get SSL setting.

        For a given zone identifier, get SSL setting.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SslSettingResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_ssl_setting')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/ssl'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Change SSL setting
    #########################


    def change_ssl_setting(self, *, value: str = None, **kwargs) -> DetailedResponse:
        """
        change SSL setting.

        For a given zone identifier, change SSL setting.

        :param str value: (optional) value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SslSettingResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='change_ssl_setting')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/ssl'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # List custom certificates
    #########################


    def list_custom_certificates(self, **kwargs) -> DetailedResponse:
        """
        list all custom certificates.

        For a given zone identifier, list all custom certificates.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListCustomCertsResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='list_custom_certificates')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/custom_certificates'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Upload a custom certificate
    #########################


    def upload_custom_certificate(self, *, certificate: str = None, private_key: str = None, bundle_method: str = None, geo_restrictions: 'CustomCertReqGeoRestrictions' = None, **kwargs) -> DetailedResponse:
        """
        Upload a custom certificate.

        For a given zone identifier, upload a custom certificates.

        :param str certificate: (optional) certificates.
        :param str private_key: (optional) private key.
        :param str bundle_method: (optional) Methods shown in UI mapping to API:
               Compatible(ubiquitous), Modern(optimal), User Defined(force).
        :param CustomCertReqGeoRestrictions geo_restrictions: (optional) geo
               restrictions.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CustomCertResp` object
        """

        if geo_restrictions is not None:
            geo_restrictions = convert_model(geo_restrictions)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='upload_custom_certificate')
        headers.update(sdk_headers)

        data = {
            'certificate': certificate,
            'private_key': private_key,
            'bundle_method': bundle_method,
            'geo_restrictions': geo_restrictions
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/custom_certificates'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Get a custom certificate
    #########################


    def get_custom_certificate(self, custom_cert_id: str, **kwargs) -> DetailedResponse:
        """
        Get details of specified custom certificate.

        For a given zone identifier, get a custom certificates.

        :param str custom_cert_id: custom certificate id.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CustomCertResp` object
        """

        if custom_cert_id is None:
            raise ValueError('custom_cert_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_custom_certificate')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/custom_certificates/{2}'.format(*self.encode_path_vars(self.crn, self.zone_identifier, custom_cert_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Update custom certificate
    #########################


    def update_custom_certificate(self, custom_cert_id: str, *, certificate: str = None, private_key: str = None, bundle_method: str = None, geo_restrictions: 'CustomCertReqGeoRestrictions' = None, **kwargs) -> DetailedResponse:
        """
        Update specified custom certificate.

        For a given zone identifier, update a custom certificates.

        :param str custom_cert_id: custom certificate id.
        :param str certificate: (optional) certificates.
        :param str private_key: (optional) private key.
        :param str bundle_method: (optional) Methods shown in UI mapping to API:
               Compatible(ubiquitous), Modern(optimal), User Defined(force).
        :param CustomCertReqGeoRestrictions geo_restrictions: (optional) geo
               restrictions.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CustomCertResp` object
        """

        if custom_cert_id is None:
            raise ValueError('custom_cert_id must be provided')
        if geo_restrictions is not None:
            geo_restrictions = convert_model(geo_restrictions)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_custom_certificate')
        headers.update(sdk_headers)

        data = {
            'certificate': certificate,
            'private_key': private_key,
            'bundle_method': bundle_method,
            'geo_restrictions': geo_restrictions
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/custom_certificates/{2}'.format(*self.encode_path_vars(self.crn, self.zone_identifier, custom_cert_id))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Delete a custom certificate
    #########################


    def delete_custom_certificate(self, custom_cert_id: str, **kwargs) -> DetailedResponse:
        """
        Delete a given custom certificate.

        For a given zone identifier, delete a custom certificates.

        :param str custom_cert_id: custom certificate id.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if custom_cert_id is None:
            raise ValueError('custom_cert_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='delete_custom_certificate')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/custom_certificates/{2}'.format(*self.encode_path_vars(self.crn, self.zone_identifier, custom_cert_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Set certificate priority
    #########################


    def change_certificate_priority(self, *, certificates: List['CertPriorityReqCertificatesItem'] = None, **kwargs) -> DetailedResponse:
        """
        Set priority for given certificates.

        For a given zone identifier, set priority of certificates.

        :param List[CertPriorityReqCertificatesItem] certificates: (optional)
               certificates array.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if certificates is not None:
            certificates = [ convert_model(x) for x in certificates ]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='change_certificate_priority')
        headers.update(sdk_headers)

        data = {
            'certificates': certificates
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/custom_certificates/prioritize'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Get universal certificate
    #########################


    def get_universal_certificate_setting(self, **kwargs) -> DetailedResponse:
        """
        For a given zone identifier, get details of universal certificate.

        For a given zone identifier, get universal certificate.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `UniversalSettingResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_universal_certificate_setting')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/ssl/universal/settings'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Set universal certificate
    #########################


    def change_universal_certificate_setting(self, *, enabled: bool = None, **kwargs) -> DetailedResponse:
        """
        For a given zone identifier, enable or disable universal certificate.

        change universal certificate setting.

        :param bool enabled: (optional) enabled.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='change_universal_certificate_setting')
        headers.update(sdk_headers)

        data = {
            'enabled': enabled
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/ssl/universal/settings'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Get tls_1_2_only setting
    #########################


    def get_tls12_setting(self, **kwargs) -> DetailedResponse:
        """
        For a given zone identifier, get tls_1_2_only setting.

        For a given zone identifier, get tls_1_2_only setting.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Tls12SettingResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_tls12_setting')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/tls_1_2_only'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Set tls_1_2_only setting
    #########################


    def change_tls12_setting(self, *, value: str = None, **kwargs) -> DetailedResponse:
        """
        For a given zone identifier, set tls_1_2 setting.

        For a given zone identifier, set tls_1_2 setting.

        :param str value: (optional) value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Tls12SettingResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='change_tls12_setting')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/tls_1_2_only'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Get tls_1_3 setting
    #########################


    def get_tls13_setting(self, **kwargs) -> DetailedResponse:
        """
        For a given zone identifier, get tls_1_3 setting.

        For a given zone identifier, get tls_1_3 setting.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Tls13SettingResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_tls13_setting')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/tls_1_3'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Set tls_1_3 setting
    #########################


    def change_tls13_setting(self, *, value: str = None, **kwargs) -> DetailedResponse:
        """
        For a given zone identifier, set tls_1_3 setting.

        For a given zone identifier, set tls_1_3 setting.

        :param str value: (optional) value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Tls13SettingResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='change_tls13_setting')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/tls_1_3'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

