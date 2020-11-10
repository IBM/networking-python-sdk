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
    # SSL Certificate
    #########################


    def list_certificates(self,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_certificates')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/ssl/certificate_packs'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def order_certificate(self,
        *,
        type: str = None,
        hosts: List[str] = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Order dedicated certificate.

        Order a dedicated certificate for a given zone. The zone should be active before
        placing an order of a dedicated certificate.

        :param str type: (optional) priorities.
        :param List[str] hosts: (optional) host name.
        :param str x_correlation_id: (optional) uuid, identify a session.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DedicatedCertificateResp` object
        """

        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='order_certificate')
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

        url = '/v1/{0}/zones/{1}/ssl/certificate_packs'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_certificate(self,
        cert_identifier: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_certificate')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/ssl/certificate_packs/{2}'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier, cert_identifier))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_ssl_setting(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get SSL setting.

        For a given zone identifier, get SSL setting.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SslSettingResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_ssl_setting')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/ssl'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def change_ssl_setting(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Change SSL setting.

        For a given zone identifier, change SSL setting.

        :param str value: (optional) value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SslSettingResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='change_ssl_setting')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/ssl'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def list_custom_certificates(self,
        **kwargs
    ) -> DetailedResponse:
        """
        List all custom certificates.

        For a given zone identifier, list all custom certificates.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListCustomCertsResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_custom_certificates')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/custom_certificates'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def upload_custom_certificate(self,
        *,
        certificate: str = None,
        private_key: str = None,
        bundle_method: str = None,
        geo_restrictions: 'CustomCertReqGeoRestrictions' = None,
        **kwargs
    ) -> DetailedResponse:
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='upload_custom_certificate')
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

        url = '/v1/{0}/zones/{1}/custom_certificates'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_custom_certificate(self,
        custom_cert_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get custom certificate.

        For a given zone identifier, get a custom certificates.

        :param str custom_cert_id: custom certificate id.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CustomCertResp` object
        """

        if custom_cert_id is None:
            raise ValueError('custom_cert_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_custom_certificate')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/custom_certificates/{2}'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier, custom_cert_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_custom_certificate(self,
        custom_cert_id: str,
        *,
        certificate: str = None,
        private_key: str = None,
        bundle_method: str = None,
        geo_restrictions: 'CustomCertReqGeoRestrictions' = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update custom certificate.

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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_custom_certificate')
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

        url = '/v1/{0}/zones/{1}/custom_certificates/{2}'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier, custom_cert_id))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_custom_certificate(self,
        custom_cert_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete custom certificate.

        For a given zone identifier, delete a custom certificates.

        :param str custom_cert_id: custom certificate id.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if custom_cert_id is None:
            raise ValueError('custom_cert_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_custom_certificate')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/custom_certificates/{2}'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier, custom_cert_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def change_certificate_priority(self,
        *,
        certificates: List['CertPriorityReqCertificatesItem'] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Set certificate priority.

        For a given zone identifier, set priority of certificates.

        :param List[CertPriorityReqCertificatesItem] certificates: (optional)
               certificates array.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if certificates is not None:
            certificates = [convert_model(x) for x in certificates]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='change_certificate_priority')
        headers.update(sdk_headers)

        data = {
            'certificates': certificates
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/custom_certificates/prioritize'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_universal_certificate_setting(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get details of universal certificate.

        For a given zone identifier, get universal certificate.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `UniversalSettingResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_universal_certificate_setting')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/ssl/universal/settings'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def change_universal_certificate_setting(self,
        *,
        enabled: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Enable or Disable universal certificate.

        change universal certificate setting.

        :param bool enabled: (optional) enabled.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='change_universal_certificate_setting')
        headers.update(sdk_headers)

        data = {
            'enabled': enabled
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/ssl/universal/settings'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_tls12_setting(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get TLS 1.2 only setting.

        For a given zone identifier, get TLS 1.2 only setting.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Tls12SettingResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_tls12_setting')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/tls_1_2_only'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def change_tls12_setting(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Set TLS 1.2 setting.

        For a given zone identifier, set TLS 1.2 setting.

        :param str value: (optional) value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Tls12SettingResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='change_tls12_setting')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/tls_1_2_only'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_tls13_setting(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get TLS 1.3 setting.

        For a given zone identifier, get TLS 1.3 setting.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Tls13SettingResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_tls13_setting')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/tls_1_3'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def change_tls13_setting(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Set TLS 1.3 setting.

        For a given zone identifier, set TLS 1.3 setting.

        :param str value: (optional) value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Tls13SettingResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='change_tls13_setting')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/tls_1_3'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class CertPriorityReqCertificatesItem():
    """
    certificate items.

    :attr str id: identifier.
    :attr int priority: certificate priority.
    """

    def __init__(self,
                 id: str,
                 priority: int) -> None:
        """
        Initialize a CertPriorityReqCertificatesItem object.

        :param str id: identifier.
        :param int priority: certificate priority.
        """
        self.id = id
        self.priority = priority

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CertPriorityReqCertificatesItem':
        """Initialize a CertPriorityReqCertificatesItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in CertPriorityReqCertificatesItem JSON')
        if 'priority' in _dict:
            args['priority'] = _dict.get('priority')
        else:
            raise ValueError('Required property \'priority\' not present in CertPriorityReqCertificatesItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CertPriorityReqCertificatesItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'priority') and self.priority is not None:
            _dict['priority'] = self.priority
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CertPriorityReqCertificatesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CertPriorityReqCertificatesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CertPriorityReqCertificatesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CustomCertReqGeoRestrictions():
    """
    geo restrictions.

    :attr str label: properties.
    """

    def __init__(self,
                 label: str) -> None:
        """
        Initialize a CustomCertReqGeoRestrictions object.

        :param str label: properties.
        """
        self.label = label

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CustomCertReqGeoRestrictions':
        """Initialize a CustomCertReqGeoRestrictions object from a json dictionary."""
        args = {}
        if 'label' in _dict:
            args['label'] = _dict.get('label')
        else:
            raise ValueError('Required property \'label\' not present in CustomCertReqGeoRestrictions JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CustomCertReqGeoRestrictions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CustomCertReqGeoRestrictions object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CustomCertReqGeoRestrictions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CustomCertReqGeoRestrictions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class LabelEnum(str, Enum):
        """
        properties.
        """
        US = 'us'
        EU = 'eu'
        HIGHEST_SECURITY = 'highest_security'


class Tls12SettingRespMessagesItem():
    """
    Tls12SettingRespMessagesItem.

    :attr str status: (optional) status.
    """

    def __init__(self,
                 *,
                 status: str = None) -> None:
        """
        Initialize a Tls12SettingRespMessagesItem object.

        :param str status: (optional) status.
        """
        self.status = status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Tls12SettingRespMessagesItem':
        """Initialize a Tls12SettingRespMessagesItem object from a json dictionary."""
        args = {}
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Tls12SettingRespMessagesItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Tls12SettingRespMessagesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Tls12SettingRespMessagesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Tls12SettingRespMessagesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Tls12SettingRespResult():
    """
    result.

    :attr str id: identifier.
    :attr str value: value.
    :attr bool editable: editable.
    :attr datetime modified_on: modified date.
    """

    def __init__(self,
                 id: str,
                 value: str,
                 editable: bool,
                 modified_on: datetime) -> None:
        """
        Initialize a Tls12SettingRespResult object.

        :param str id: identifier.
        :param str value: value.
        :param bool editable: editable.
        :param datetime modified_on: modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Tls12SettingRespResult':
        """Initialize a Tls12SettingRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in Tls12SettingRespResult JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in Tls12SettingRespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in Tls12SettingRespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in Tls12SettingRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Tls12SettingRespResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'editable') and self.editable is not None:
            _dict['editable'] = self.editable
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = datetime_to_string(self.modified_on)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Tls12SettingRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Tls12SettingRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Tls12SettingRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class IdEnum(str, Enum):
        """
        identifier.
        """
        TLS_1_2_ONLY = 'tls_1_2_only'


class Tls13SettingRespResult():
    """
    result.

    :attr str id: identifier.
    :attr str value: value.
    :attr bool editable: editable.
    :attr datetime modified_on: modified date.
    """

    def __init__(self,
                 id: str,
                 value: str,
                 editable: bool,
                 modified_on: datetime) -> None:
        """
        Initialize a Tls13SettingRespResult object.

        :param str id: identifier.
        :param str value: value.
        :param bool editable: editable.
        :param datetime modified_on: modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Tls13SettingRespResult':
        """Initialize a Tls13SettingRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in Tls13SettingRespResult JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in Tls13SettingRespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in Tls13SettingRespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in Tls13SettingRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Tls13SettingRespResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'editable') and self.editable is not None:
            _dict['editable'] = self.editable
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = datetime_to_string(self.modified_on)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Tls13SettingRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Tls13SettingRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Tls13SettingRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class IdEnum(str, Enum):
        """
        identifier.
        """
        TLS_1_3 = 'tls_1_3'


class UniversalSettingRespResult():
    """
    result.

    :attr bool enabled: enabled.
    """

    def __init__(self,
                 enabled: bool) -> None:
        """
        Initialize a UniversalSettingRespResult object.

        :param bool enabled: enabled.
        """
        self.enabled = enabled

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UniversalSettingRespResult':
        """Initialize a UniversalSettingRespResult object from a json dictionary."""
        args = {}
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        else:
            raise ValueError('Required property \'enabled\' not present in UniversalSettingRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UniversalSettingRespResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UniversalSettingRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UniversalSettingRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UniversalSettingRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Certificate():
    """
    certificate.

    :attr object id: identifier.
    :attr List[str] hosts: host name.
    :attr str status: status.
    """

    def __init__(self,
                 id: object,
                 hosts: List[str],
                 status: str) -> None:
        """
        Initialize a Certificate object.

        :param object id: identifier.
        :param List[str] hosts: host name.
        :param str status: status.
        """
        self.id = id
        self.hosts = hosts
        self.status = status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Certificate':
        """Initialize a Certificate object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in Certificate JSON')
        if 'hosts' in _dict:
            args['hosts'] = _dict.get('hosts')
        else:
            raise ValueError('Required property \'hosts\' not present in Certificate JSON')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError('Required property \'status\' not present in Certificate JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Certificate object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'hosts') and self.hosts is not None:
            _dict['hosts'] = self.hosts
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Certificate object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Certificate') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Certificate') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CustomCertPack():
    """
    custom certificate pack.

    :attr str id: identifier.
    :attr List[str] hosts: host name.
    :attr str issuer: issuer.
    :attr str signature: signature.
    :attr str status: status.
    :attr str bundle_method: bundle method.
    :attr str zone_id: zone identifier.
    :attr str uploaded_on: uploaded date.
    :attr str modified_on: modified date.
    :attr str expires_on: expire date.
    :attr float priority: priority.
    """

    def __init__(self,
                 id: str,
                 hosts: List[str],
                 issuer: str,
                 signature: str,
                 status: str,
                 bundle_method: str,
                 zone_id: str,
                 uploaded_on: str,
                 modified_on: str,
                 expires_on: str,
                 priority: float) -> None:
        """
        Initialize a CustomCertPack object.

        :param str id: identifier.
        :param List[str] hosts: host name.
        :param str issuer: issuer.
        :param str signature: signature.
        :param str status: status.
        :param str bundle_method: bundle method.
        :param str zone_id: zone identifier.
        :param str uploaded_on: uploaded date.
        :param str modified_on: modified date.
        :param str expires_on: expire date.
        :param float priority: priority.
        """
        self.id = id
        self.hosts = hosts
        self.issuer = issuer
        self.signature = signature
        self.status = status
        self.bundle_method = bundle_method
        self.zone_id = zone_id
        self.uploaded_on = uploaded_on
        self.modified_on = modified_on
        self.expires_on = expires_on
        self.priority = priority

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CustomCertPack':
        """Initialize a CustomCertPack object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in CustomCertPack JSON')
        if 'hosts' in _dict:
            args['hosts'] = _dict.get('hosts')
        else:
            raise ValueError('Required property \'hosts\' not present in CustomCertPack JSON')
        if 'issuer' in _dict:
            args['issuer'] = _dict.get('issuer')
        else:
            raise ValueError('Required property \'issuer\' not present in CustomCertPack JSON')
        if 'signature' in _dict:
            args['signature'] = _dict.get('signature')
        else:
            raise ValueError('Required property \'signature\' not present in CustomCertPack JSON')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError('Required property \'status\' not present in CustomCertPack JSON')
        if 'bundle_method' in _dict:
            args['bundle_method'] = _dict.get('bundle_method')
        else:
            raise ValueError('Required property \'bundle_method\' not present in CustomCertPack JSON')
        if 'zone_id' in _dict:
            args['zone_id'] = _dict.get('zone_id')
        else:
            raise ValueError('Required property \'zone_id\' not present in CustomCertPack JSON')
        if 'uploaded_on' in _dict:
            args['uploaded_on'] = _dict.get('uploaded_on')
        else:
            raise ValueError('Required property \'uploaded_on\' not present in CustomCertPack JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        else:
            raise ValueError('Required property \'modified_on\' not present in CustomCertPack JSON')
        if 'expires_on' in _dict:
            args['expires_on'] = _dict.get('expires_on')
        else:
            raise ValueError('Required property \'expires_on\' not present in CustomCertPack JSON')
        if 'priority' in _dict:
            args['priority'] = _dict.get('priority')
        else:
            raise ValueError('Required property \'priority\' not present in CustomCertPack JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CustomCertPack object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'hosts') and self.hosts is not None:
            _dict['hosts'] = self.hosts
        if hasattr(self, 'issuer') and self.issuer is not None:
            _dict['issuer'] = self.issuer
        if hasattr(self, 'signature') and self.signature is not None:
            _dict['signature'] = self.signature
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'bundle_method') and self.bundle_method is not None:
            _dict['bundle_method'] = self.bundle_method
        if hasattr(self, 'zone_id') and self.zone_id is not None:
            _dict['zone_id'] = self.zone_id
        if hasattr(self, 'uploaded_on') and self.uploaded_on is not None:
            _dict['uploaded_on'] = self.uploaded_on
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = self.modified_on
        if hasattr(self, 'expires_on') and self.expires_on is not None:
            _dict['expires_on'] = self.expires_on
        if hasattr(self, 'priority') and self.priority is not None:
            _dict['priority'] = self.priority
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CustomCertPack object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CustomCertPack') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CustomCertPack') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CustomCertResp():
    """
    custom certificate response.

    :attr CustomCertPack result: custom certificate pack.
    :attr bool success: success.
    :attr List[List[str]] errors: errors.
    :attr List[Tls12SettingRespMessagesItem] messages: messages.
    """

    def __init__(self,
                 result: 'CustomCertPack',
                 success: bool,
                 errors: List[List[str]],
                 messages: List['Tls12SettingRespMessagesItem']) -> None:
        """
        Initialize a CustomCertResp object.

        :param CustomCertPack result: custom certificate pack.
        :param bool success: success.
        :param List[List[str]] errors: errors.
        :param List[Tls12SettingRespMessagesItem] messages: messages.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CustomCertResp':
        """Initialize a CustomCertResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = CustomCertPack.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in CustomCertResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in CustomCertResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in CustomCertResp JSON')
        if 'messages' in _dict:
            args['messages'] = [Tls12SettingRespMessagesItem.from_dict(x) for x in _dict.get('messages')]
        else:
            raise ValueError('Required property \'messages\' not present in CustomCertResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CustomCertResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'result') and self.result is not None:
            _dict['result'] = self.result.to_dict()
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = [x.to_dict() for x in self.messages]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CustomCertResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CustomCertResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CustomCertResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DedicatedCertificatePack():
    """
    dedicated certificate packs.

    :attr str id: identifier.
    :attr str type: certificate type.
    :attr List[str] hosts: host name.
    :attr List[Certificate] certificates: certificates.
    :attr object primary_certificate: primary certificate.
    :attr str status: status.
    """

    def __init__(self,
                 id: str,
                 type: str,
                 hosts: List[str],
                 certificates: List['Certificate'],
                 primary_certificate: object,
                 status: str) -> None:
        """
        Initialize a DedicatedCertificatePack object.

        :param str id: identifier.
        :param str type: certificate type.
        :param List[str] hosts: host name.
        :param List[Certificate] certificates: certificates.
        :param object primary_certificate: primary certificate.
        :param str status: status.
        """
        self.id = id
        self.type = type
        self.hosts = hosts
        self.certificates = certificates
        self.primary_certificate = primary_certificate
        self.status = status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DedicatedCertificatePack':
        """Initialize a DedicatedCertificatePack object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in DedicatedCertificatePack JSON')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in DedicatedCertificatePack JSON')
        if 'hosts' in _dict:
            args['hosts'] = _dict.get('hosts')
        else:
            raise ValueError('Required property \'hosts\' not present in DedicatedCertificatePack JSON')
        if 'certificates' in _dict:
            args['certificates'] = [Certificate.from_dict(x) for x in _dict.get('certificates')]
        else:
            raise ValueError('Required property \'certificates\' not present in DedicatedCertificatePack JSON')
        if 'primary_certificate' in _dict:
            args['primary_certificate'] = _dict.get('primary_certificate')
        else:
            raise ValueError('Required property \'primary_certificate\' not present in DedicatedCertificatePack JSON')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError('Required property \'status\' not present in DedicatedCertificatePack JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DedicatedCertificatePack object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'hosts') and self.hosts is not None:
            _dict['hosts'] = self.hosts
        if hasattr(self, 'certificates') and self.certificates is not None:
            _dict['certificates'] = [x.to_dict() for x in self.certificates]
        if hasattr(self, 'primary_certificate') and self.primary_certificate is not None:
            _dict['primary_certificate'] = self.primary_certificate
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DedicatedCertificatePack object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DedicatedCertificatePack') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DedicatedCertificatePack') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DedicatedCertificateResp():
    """
    certificate response.

    :attr DedicatedCertificatePack result: dedicated certificate packs.
    :attr ResultInfo result_info: result information.
    :attr bool success: success.
    :attr List[List[str]] errors: errors.
    :attr List[Tls12SettingRespMessagesItem] messages: messages.
    """

    def __init__(self,
                 result: 'DedicatedCertificatePack',
                 result_info: 'ResultInfo',
                 success: bool,
                 errors: List[List[str]],
                 messages: List['Tls12SettingRespMessagesItem']) -> None:
        """
        Initialize a DedicatedCertificateResp object.

        :param DedicatedCertificatePack result: dedicated certificate packs.
        :param ResultInfo result_info: result information.
        :param bool success: success.
        :param List[List[str]] errors: errors.
        :param List[Tls12SettingRespMessagesItem] messages: messages.
        """
        self.result = result
        self.result_info = result_info
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DedicatedCertificateResp':
        """Initialize a DedicatedCertificateResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = DedicatedCertificatePack.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in DedicatedCertificateResp JSON')
        if 'result_info' in _dict:
            args['result_info'] = ResultInfo.from_dict(_dict.get('result_info'))
        else:
            raise ValueError('Required property \'result_info\' not present in DedicatedCertificateResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in DedicatedCertificateResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in DedicatedCertificateResp JSON')
        if 'messages' in _dict:
            args['messages'] = [Tls12SettingRespMessagesItem.from_dict(x) for x in _dict.get('messages')]
        else:
            raise ValueError('Required property \'messages\' not present in DedicatedCertificateResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DedicatedCertificateResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'result') and self.result is not None:
            _dict['result'] = self.result.to_dict()
        if hasattr(self, 'result_info') and self.result_info is not None:
            _dict['result_info'] = self.result_info.to_dict()
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = [x.to_dict() for x in self.messages]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DedicatedCertificateResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DedicatedCertificateResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DedicatedCertificateResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListCertificateResp():
    """
    certificate response.

    :attr List[DedicatedCertificatePack] result: certificate packs.
    :attr ResultInfo result_info: result information.
    :attr bool success: success.
    :attr List[List[str]] errors: errors.
    :attr List[Tls12SettingRespMessagesItem] messages: messages.
    """

    def __init__(self,
                 result: List['DedicatedCertificatePack'],
                 result_info: 'ResultInfo',
                 success: bool,
                 errors: List[List[str]],
                 messages: List['Tls12SettingRespMessagesItem']) -> None:
        """
        Initialize a ListCertificateResp object.

        :param List[DedicatedCertificatePack] result: certificate packs.
        :param ResultInfo result_info: result information.
        :param bool success: success.
        :param List[List[str]] errors: errors.
        :param List[Tls12SettingRespMessagesItem] messages: messages.
        """
        self.result = result
        self.result_info = result_info
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListCertificateResp':
        """Initialize a ListCertificateResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = [DedicatedCertificatePack.from_dict(x) for x in _dict.get('result')]
        else:
            raise ValueError('Required property \'result\' not present in ListCertificateResp JSON')
        if 'result_info' in _dict:
            args['result_info'] = ResultInfo.from_dict(_dict.get('result_info'))
        else:
            raise ValueError('Required property \'result_info\' not present in ListCertificateResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in ListCertificateResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in ListCertificateResp JSON')
        if 'messages' in _dict:
            args['messages'] = [Tls12SettingRespMessagesItem.from_dict(x) for x in _dict.get('messages')]
        else:
            raise ValueError('Required property \'messages\' not present in ListCertificateResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListCertificateResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'result') and self.result is not None:
            _dict['result'] = [x.to_dict() for x in self.result]
        if hasattr(self, 'result_info') and self.result_info is not None:
            _dict['result_info'] = self.result_info.to_dict()
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = [x.to_dict() for x in self.messages]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListCertificateResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListCertificateResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListCertificateResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListCustomCertsResp():
    """
    custom certificate response.

    :attr List[CustomCertPack] result: custom certificate packs.
    :attr ResultInfo result_info: result information.
    :attr bool success: success.
    :attr List[List[str]] errors: errors.
    :attr List[Tls12SettingRespMessagesItem] messages: messages.
    """

    def __init__(self,
                 result: List['CustomCertPack'],
                 result_info: 'ResultInfo',
                 success: bool,
                 errors: List[List[str]],
                 messages: List['Tls12SettingRespMessagesItem']) -> None:
        """
        Initialize a ListCustomCertsResp object.

        :param List[CustomCertPack] result: custom certificate packs.
        :param ResultInfo result_info: result information.
        :param bool success: success.
        :param List[List[str]] errors: errors.
        :param List[Tls12SettingRespMessagesItem] messages: messages.
        """
        self.result = result
        self.result_info = result_info
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListCustomCertsResp':
        """Initialize a ListCustomCertsResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = [CustomCertPack.from_dict(x) for x in _dict.get('result')]
        else:
            raise ValueError('Required property \'result\' not present in ListCustomCertsResp JSON')
        if 'result_info' in _dict:
            args['result_info'] = ResultInfo.from_dict(_dict.get('result_info'))
        else:
            raise ValueError('Required property \'result_info\' not present in ListCustomCertsResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in ListCustomCertsResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in ListCustomCertsResp JSON')
        if 'messages' in _dict:
            args['messages'] = [Tls12SettingRespMessagesItem.from_dict(x) for x in _dict.get('messages')]
        else:
            raise ValueError('Required property \'messages\' not present in ListCustomCertsResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListCustomCertsResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'result') and self.result is not None:
            _dict['result'] = [x.to_dict() for x in self.result]
        if hasattr(self, 'result_info') and self.result_info is not None:
            _dict['result_info'] = self.result_info.to_dict()
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = [x.to_dict() for x in self.messages]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListCustomCertsResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListCustomCertsResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListCustomCertsResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResultInfo():
    """
    result information.

    :attr int page: page number.
    :attr int per_page: per page count.
    :attr int count: count.
    :attr int total_count: total count.
    """

    def __init__(self,
                 page: int,
                 per_page: int,
                 count: int,
                 total_count: int) -> None:
        """
        Initialize a ResultInfo object.

        :param int page: page number.
        :param int per_page: per page count.
        :param int count: count.
        :param int total_count: total count.
        """
        self.page = page
        self.per_page = per_page
        self.count = count
        self.total_count = total_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResultInfo':
        """Initialize a ResultInfo object from a json dictionary."""
        args = {}
        if 'page' in _dict:
            args['page'] = _dict.get('page')
        else:
            raise ValueError('Required property \'page\' not present in ResultInfo JSON')
        if 'per_page' in _dict:
            args['per_page'] = _dict.get('per_page')
        else:
            raise ValueError('Required property \'per_page\' not present in ResultInfo JSON')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        else:
            raise ValueError('Required property \'count\' not present in ResultInfo JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in ResultInfo JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResultInfo object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'page') and self.page is not None:
            _dict['page'] = self.page
        if hasattr(self, 'per_page') and self.per_page is not None:
            _dict['per_page'] = self.per_page
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResultInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResultInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResultInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SslSetting():
    """
    ssl setting.

    :attr str id: identifier.
    :attr str value: value.
    :attr bool editable: editable.
    :attr str modified_on: modified date.
    """

    def __init__(self,
                 id: str,
                 value: str,
                 editable: bool,
                 modified_on: str) -> None:
        """
        Initialize a SslSetting object.

        :param str id: identifier.
        :param str value: value.
        :param bool editable: editable.
        :param str modified_on: modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SslSetting':
        """Initialize a SslSetting object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in SslSetting JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in SslSetting JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in SslSetting JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        else:
            raise ValueError('Required property \'modified_on\' not present in SslSetting JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SslSetting object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'editable') and self.editable is not None:
            _dict['editable'] = self.editable
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = self.modified_on
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SslSetting object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SslSetting') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SslSetting') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SslSettingResp():
    """
    ssl setting response.

    :attr bool success: success.
    :attr SslSetting result: ssl setting.
    :attr List[List[str]] errors: errors.
    :attr List[Tls12SettingRespMessagesItem] messages: messages.
    """

    def __init__(self,
                 success: bool,
                 result: 'SslSetting',
                 errors: List[List[str]],
                 messages: List['Tls12SettingRespMessagesItem']) -> None:
        """
        Initialize a SslSettingResp object.

        :param bool success: success.
        :param SslSetting result: ssl setting.
        :param List[List[str]] errors: errors.
        :param List[Tls12SettingRespMessagesItem] messages: messages.
        """
        self.success = success
        self.result = result
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SslSettingResp':
        """Initialize a SslSettingResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in SslSettingResp JSON')
        if 'result' in _dict:
            args['result'] = SslSetting.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in SslSettingResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in SslSettingResp JSON')
        if 'messages' in _dict:
            args['messages'] = [Tls12SettingRespMessagesItem.from_dict(x) for x in _dict.get('messages')]
        else:
            raise ValueError('Required property \'messages\' not present in SslSettingResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SslSettingResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'result') and self.result is not None:
            _dict['result'] = self.result.to_dict()
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = [x.to_dict() for x in self.messages]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SslSettingResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SslSettingResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SslSettingResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Tls12SettingResp():
    """
    tls 1.2 setting response.

    :attr Tls12SettingRespResult result: result.
    :attr bool success: success.
    :attr List[List[str]] errors: errors.
    :attr List[Tls12SettingRespMessagesItem] messages: messages.
    """

    def __init__(self,
                 result: 'Tls12SettingRespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List['Tls12SettingRespMessagesItem']) -> None:
        """
        Initialize a Tls12SettingResp object.

        :param Tls12SettingRespResult result: result.
        :param bool success: success.
        :param List[List[str]] errors: errors.
        :param List[Tls12SettingRespMessagesItem] messages: messages.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Tls12SettingResp':
        """Initialize a Tls12SettingResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = Tls12SettingRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in Tls12SettingResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in Tls12SettingResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in Tls12SettingResp JSON')
        if 'messages' in _dict:
            args['messages'] = [Tls12SettingRespMessagesItem.from_dict(x) for x in _dict.get('messages')]
        else:
            raise ValueError('Required property \'messages\' not present in Tls12SettingResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Tls12SettingResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'result') and self.result is not None:
            _dict['result'] = self.result.to_dict()
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = [x.to_dict() for x in self.messages]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Tls12SettingResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Tls12SettingResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Tls12SettingResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Tls13SettingResp():
    """
    tls 1.3 setting response.

    :attr Tls13SettingRespResult result: result.
    :attr bool success: success.
    :attr List[List[str]] errors: errors.
    :attr List[Tls12SettingRespMessagesItem] messages: messages.
    """

    def __init__(self,
                 result: 'Tls13SettingRespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List['Tls12SettingRespMessagesItem']) -> None:
        """
        Initialize a Tls13SettingResp object.

        :param Tls13SettingRespResult result: result.
        :param bool success: success.
        :param List[List[str]] errors: errors.
        :param List[Tls12SettingRespMessagesItem] messages: messages.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Tls13SettingResp':
        """Initialize a Tls13SettingResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = Tls13SettingRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in Tls13SettingResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in Tls13SettingResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in Tls13SettingResp JSON')
        if 'messages' in _dict:
            args['messages'] = [Tls12SettingRespMessagesItem.from_dict(x) for x in _dict.get('messages')]
        else:
            raise ValueError('Required property \'messages\' not present in Tls13SettingResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Tls13SettingResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'result') and self.result is not None:
            _dict['result'] = self.result.to_dict()
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = [x.to_dict() for x in self.messages]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Tls13SettingResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Tls13SettingResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Tls13SettingResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class UniversalSettingResp():
    """
    universal setting response.

    :attr UniversalSettingRespResult result: result.
    :attr bool success: success.
    :attr List[List[str]] errors: errors.
    :attr List[Tls12SettingRespMessagesItem] messages: messages.
    """

    def __init__(self,
                 result: 'UniversalSettingRespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List['Tls12SettingRespMessagesItem']) -> None:
        """
        Initialize a UniversalSettingResp object.

        :param UniversalSettingRespResult result: result.
        :param bool success: success.
        :param List[List[str]] errors: errors.
        :param List[Tls12SettingRespMessagesItem] messages: messages.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UniversalSettingResp':
        """Initialize a UniversalSettingResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = UniversalSettingRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in UniversalSettingResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in UniversalSettingResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in UniversalSettingResp JSON')
        if 'messages' in _dict:
            args['messages'] = [Tls12SettingRespMessagesItem.from_dict(x) for x in _dict.get('messages')]
        else:
            raise ValueError('Required property \'messages\' not present in UniversalSettingResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UniversalSettingResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'result') and self.result is not None:
            _dict['result'] = self.result.to_dict()
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = [x.to_dict() for x in self.messages]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UniversalSettingResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UniversalSettingResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UniversalSettingResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
