# coding: utf-8

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

# IBM OpenAPI SDK Code Generator Version: 3.49.0-be9b22fb-20220504-154308
 
"""
Authenticated Origin Pull

API Version: 1.0.0
"""

from datetime import datetime
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

class AuthenticatedOriginPullApiV1(BaseService):
    """The Authenticated Origin Pull API V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'authenticated_origin_pull_api'

    @classmethod
    def new_instance(cls,
                     crn: str,
                     zone_identifier: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'AuthenticatedOriginPullApiV1':
        """
        Return a new client for the Authenticated Origin Pull API service using the
               specified parameters and external configuration.

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
        Construct a new client for the Authenticated Origin Pull API service.

        :param str crn: cloud resource name.

        :param str zone_identifier: zone identifier.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
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
    # Zone-Level Authenticated Origin Pull
    #########################


    def get_zone_origin_pull_settings(self,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get Zone level Authenticated Origin Pull Settings.

        Get whether zone-level authenticated origin pulls is enabled or not. It is false
        by default.

        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `GetZoneOriginPullSettingsResp` object
        """

        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_zone_origin_pull_settings')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/origin_tls_client_auth/settings'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def set_zone_origin_pull_settings(self,
        *,
        enabled: bool = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Set Zone level Authenticated Origin Pull Settings.

        Enable or disable zone-level authenticated origin pulls. 'enabled' should be set
        true either before/after the certificate is uploaded to see the certificate in
        use.

        :param bool enabled: (optional) enabled.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `GetZoneOriginPullSettingsResp` object
        """

        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='set_zone_origin_pull_settings')
        headers.update(sdk_headers)

        data = {
            'enabled': enabled
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/origin_tls_client_auth/settings'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def list_zone_origin_pull_certificates(self,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List Zone level Authenticated Origin Pull Certificates.

        List zone-level authenticated origin pulls certificates.

        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListZoneOriginPullCertificatesResp` object
        """

        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_zone_origin_pull_certificates')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/origin_tls_client_auth'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def upload_zone_origin_pull_certificate(self,
        *,
        certificate: str = None,
        private_key: str = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Upload Zone level Authenticated Origin Pull Certificate.

        Upload your own certificate you want Cloudflare to use for edge-to-origin
        communication to override the shared certificate Please note that it is important
        to keep only one certificate active. Also, make sure to enable zone-level
        authenticated  origin pulls by making a PUT call to settings endpoint to see the
        uploaded certificate in use.

        :param str certificate: (optional) the zone's leaf certificate.
        :param str private_key: (optional) the zone's private key.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ZoneOriginPullCertificateResp` object
        """

        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='upload_zone_origin_pull_certificate')
        headers.update(sdk_headers)

        data = {
            'certificate': certificate,
            'private_key': private_key
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/origin_tls_client_auth'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def get_zone_origin_pull_certificate(self,
        cert_identifier: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a Zone level Authenticated Origin Pull Certificate.

        Get a zone-level authenticated origin pulls certificate.

        :param str cert_identifier: cedrtificate identifier.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ZoneOriginPullCertificateResp` object
        """

        if cert_identifier is None:
            raise ValueError('cert_identifier must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_zone_origin_pull_certificate')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'cert_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier, cert_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/origin_tls_client_auth/{cert_identifier}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def delete_zone_origin_pull_certificate(self,
        cert_identifier: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a Zone level Authenticated Origin Pull Certificate.

        Delete a zone-level authenticated origin pulls certificate.

        :param str cert_identifier: cedrtificate identifier.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ZoneOriginPullCertificateResp` object
        """

        if cert_identifier is None:
            raise ValueError('cert_identifier must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_zone_origin_pull_certificate')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'cert_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier, cert_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/origin_tls_client_auth/{cert_identifier}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Per-hostname Authenticated Origin Pull
    #########################


    def set_hostname_origin_pull_settings(self,
        *,
        config: List['HostnameOriginPullSettings'] = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Set Hostname level Authenticated Origin Pull Settings.

        Associate a hostname to a certificate and enable, disable or invalidate the
        association. If disabled, client certificate will not be sent to the hostname even
        if activated at the zone level. 100 maximum associations on a single certificate
        are allowed.

        :param List[HostnameOriginPullSettings] config: (optional) An array with
               items in the settings request.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListHostnameOriginPullSettingsResp` object
        """

        if config is not None:
            config = [convert_model(x) for x in config]
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='set_hostname_origin_pull_settings')
        headers.update(sdk_headers)

        data = {
            'config': config
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/origin_tls_client_auth/hostnames'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def get_hostname_origin_pull_settings(self,
        hostname: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get Hostname level Authenticated Origin Pull Settings.

        Get hostname-level authenticated origin pulls settings.

        :param str hostname: the hostname on the origin for which the client
               certificate associate.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `GetHostnameOriginPullSettingsResp` object
        """

        if hostname is None:
            raise ValueError('hostname must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_hostname_origin_pull_settings')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'hostname']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier, hostname)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/origin_tls_client_auth/hostnames/{hostname}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def upload_hostname_origin_pull_certificate(self,
        *,
        certificate: str = None,
        private_key: str = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Upload Hostname level Authenticated Origin Pull Certificate.

        Upload a certificate to be used for client authentication on a hostname. 10
        hostname certificates per zone are allowed.

        :param str certificate: (optional) the zone's leaf certificate.
        :param str private_key: (optional) the zone's private key.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `HostnameOriginPullCertificateResp` object
        """

        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='upload_hostname_origin_pull_certificate')
        headers.update(sdk_headers)

        data = {
            'certificate': certificate,
            'private_key': private_key
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/origin_tls_client_auth/hostnames/certificates'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def get_hostname_origin_pull_certificate(self,
        cert_identifier: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a Hostname level Authenticated Origin Pull Certificate.

        Get the certificate by ID to be used for client authentication on a hostname.

        :param str cert_identifier: cedrtificate identifier.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `HostnameOriginPullCertificateResp` object
        """

        if cert_identifier is None:
            raise ValueError('cert_identifier must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_hostname_origin_pull_certificate')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'cert_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier, cert_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/origin_tls_client_auth/hostnames/certificates/{cert_identifier}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def delete_hostname_origin_pull_certificate(self,
        cert_identifier: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a Hostname level Authenticated Origin Pull Certificate.

        Delete the certificate by ID to be used for client authentication on a hostname.

        :param str cert_identifier: cedrtificate identifier.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `HostnameOriginPullCertificateResp` object
        """

        if cert_identifier is None:
            raise ValueError('cert_identifier must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_hostname_origin_pull_certificate')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'cert_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier, cert_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/origin_tls_client_auth/hostnames/certificates/{cert_identifier}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


##############################################################################
# Models
##############################################################################


class GetZoneOriginPullSettingsRespResult():
    """
    result.

    :attr bool enabled: enabled.
    """

    def __init__(self,
                 enabled: bool) -> None:
        """
        Initialize a GetZoneOriginPullSettingsRespResult object.

        :param bool enabled: enabled.
        """
        self.enabled = enabled

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GetZoneOriginPullSettingsRespResult':
        """Initialize a GetZoneOriginPullSettingsRespResult object from a json dictionary."""
        args = {}
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        else:
            raise ValueError('Required property \'enabled\' not present in GetZoneOriginPullSettingsRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GetZoneOriginPullSettingsRespResult object from a json dictionary."""
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
        """Return a `str` version of this GetZoneOriginPullSettingsRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GetZoneOriginPullSettingsRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GetZoneOriginPullSettingsRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CertificatePack():
    """
    certificate pack.

    :attr str id: (optional) certificate identifier tag.
    :attr str certificate: (optional) the zone's leaf certificate.
    :attr str issuer: (optional) the certificate authority that issued the
          certificate.
    :attr str signature: (optional) the type of hash used for the certificate.
    :attr str status: (optional) status of the certificate activation.
    :attr str expires_on: (optional) when the certificate from the authority
          expires.
    :attr str uploaded_on: (optional) the time the certificate was uploaded.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 certificate: str = None,
                 issuer: str = None,
                 signature: str = None,
                 status: str = None,
                 expires_on: str = None,
                 uploaded_on: str = None) -> None:
        """
        Initialize a CertificatePack object.

        :param str id: (optional) certificate identifier tag.
        :param str certificate: (optional) the zone's leaf certificate.
        :param str issuer: (optional) the certificate authority that issued the
               certificate.
        :param str signature: (optional) the type of hash used for the certificate.
        :param str status: (optional) status of the certificate activation.
        :param str expires_on: (optional) when the certificate from the authority
               expires.
        :param str uploaded_on: (optional) the time the certificate was uploaded.
        """
        self.id = id
        self.certificate = certificate
        self.issuer = issuer
        self.signature = signature
        self.status = status
        self.expires_on = expires_on
        self.uploaded_on = uploaded_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CertificatePack':
        """Initialize a CertificatePack object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'certificate' in _dict:
            args['certificate'] = _dict.get('certificate')
        if 'issuer' in _dict:
            args['issuer'] = _dict.get('issuer')
        if 'signature' in _dict:
            args['signature'] = _dict.get('signature')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'expires_on' in _dict:
            args['expires_on'] = _dict.get('expires_on')
        if 'uploaded_on' in _dict:
            args['uploaded_on'] = _dict.get('uploaded_on')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CertificatePack object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'certificate') and self.certificate is not None:
            _dict['certificate'] = self.certificate
        if hasattr(self, 'issuer') and self.issuer is not None:
            _dict['issuer'] = self.issuer
        if hasattr(self, 'signature') and self.signature is not None:
            _dict['signature'] = self.signature
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'expires_on') and self.expires_on is not None:
            _dict['expires_on'] = self.expires_on
        if hasattr(self, 'uploaded_on') and self.uploaded_on is not None:
            _dict['uploaded_on'] = self.uploaded_on
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CertificatePack object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CertificatePack') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CertificatePack') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class GetHostnameOriginPullSettingsResp():
    """
    detail of the hostname level authenticated origin pull settings response.

    :attr HostnameSettingsResp result: (optional) hostname level authenticated
          origin pull settings response.
    :attr bool success: (optional) success.
    :attr List[str] errors: (optional)
    :attr List[str] messages: (optional)
    """

    def __init__(self,
                 *,
                 result: 'HostnameSettingsResp' = None,
                 success: bool = None,
                 errors: List[str] = None,
                 messages: List[str] = None) -> None:
        """
        Initialize a GetHostnameOriginPullSettingsResp object.

        :param HostnameSettingsResp result: (optional) hostname level authenticated
               origin pull settings response.
        :param bool success: (optional) success.
        :param List[str] errors: (optional)
        :param List[str] messages: (optional)
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GetHostnameOriginPullSettingsResp':
        """Initialize a GetHostnameOriginPullSettingsResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = HostnameSettingsResp.from_dict(_dict.get('result'))
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GetHostnameOriginPullSettingsResp object from a json dictionary."""
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
            _dict['messages'] = self.messages
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GetHostnameOriginPullSettingsResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GetHostnameOriginPullSettingsResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GetHostnameOriginPullSettingsResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class GetZoneOriginPullSettingsResp():
    """
    zone level authenticated origin pull settings response.

    :attr GetZoneOriginPullSettingsRespResult result: (optional) result.
    :attr bool success: (optional) success.
    :attr List[str] errors: (optional)
    :attr List[str] messages: (optional)
    """

    def __init__(self,
                 *,
                 result: 'GetZoneOriginPullSettingsRespResult' = None,
                 success: bool = None,
                 errors: List[str] = None,
                 messages: List[str] = None) -> None:
        """
        Initialize a GetZoneOriginPullSettingsResp object.

        :param GetZoneOriginPullSettingsRespResult result: (optional) result.
        :param bool success: (optional) success.
        :param List[str] errors: (optional)
        :param List[str] messages: (optional)
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'GetZoneOriginPullSettingsResp':
        """Initialize a GetZoneOriginPullSettingsResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = GetZoneOriginPullSettingsRespResult.from_dict(_dict.get('result'))
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a GetZoneOriginPullSettingsResp object from a json dictionary."""
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
            _dict['messages'] = self.messages
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this GetZoneOriginPullSettingsResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'GetZoneOriginPullSettingsResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'GetZoneOriginPullSettingsResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class HostnameCertificatePack():
    """
    certificate pack.

    :attr str id: (optional) certificate identifier tag.
    :attr str certificate: (optional) the zone's leaf certificate.
    :attr str issuer: (optional) the certificate authority that issued the
          certificate.
    :attr str signature: (optional) the type of hash used for the certificate.
    :attr str serial_number: (optional) the serial number on the uploaded
          certificate.
    :attr str status: (optional) status of the certificate activation.
    :attr str expires_on: (optional) when the certificate from the authority
          expires.
    :attr str uploaded_on: (optional) the time the certificate was uploaded.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 certificate: str = None,
                 issuer: str = None,
                 signature: str = None,
                 serial_number: str = None,
                 status: str = None,
                 expires_on: str = None,
                 uploaded_on: str = None) -> None:
        """
        Initialize a HostnameCertificatePack object.

        :param str id: (optional) certificate identifier tag.
        :param str certificate: (optional) the zone's leaf certificate.
        :param str issuer: (optional) the certificate authority that issued the
               certificate.
        :param str signature: (optional) the type of hash used for the certificate.
        :param str serial_number: (optional) the serial number on the uploaded
               certificate.
        :param str status: (optional) status of the certificate activation.
        :param str expires_on: (optional) when the certificate from the authority
               expires.
        :param str uploaded_on: (optional) the time the certificate was uploaded.
        """
        self.id = id
        self.certificate = certificate
        self.issuer = issuer
        self.signature = signature
        self.serial_number = serial_number
        self.status = status
        self.expires_on = expires_on
        self.uploaded_on = uploaded_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HostnameCertificatePack':
        """Initialize a HostnameCertificatePack object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'certificate' in _dict:
            args['certificate'] = _dict.get('certificate')
        if 'issuer' in _dict:
            args['issuer'] = _dict.get('issuer')
        if 'signature' in _dict:
            args['signature'] = _dict.get('signature')
        if 'serial_number' in _dict:
            args['serial_number'] = _dict.get('serial_number')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'expires_on' in _dict:
            args['expires_on'] = _dict.get('expires_on')
        if 'uploaded_on' in _dict:
            args['uploaded_on'] = _dict.get('uploaded_on')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HostnameCertificatePack object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'certificate') and self.certificate is not None:
            _dict['certificate'] = self.certificate
        if hasattr(self, 'issuer') and self.issuer is not None:
            _dict['issuer'] = self.issuer
        if hasattr(self, 'signature') and self.signature is not None:
            _dict['signature'] = self.signature
        if hasattr(self, 'serial_number') and self.serial_number is not None:
            _dict['serial_number'] = self.serial_number
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'expires_on') and self.expires_on is not None:
            _dict['expires_on'] = self.expires_on
        if hasattr(self, 'uploaded_on') and self.uploaded_on is not None:
            _dict['uploaded_on'] = self.uploaded_on
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HostnameCertificatePack object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HostnameCertificatePack') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HostnameCertificatePack') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class HostnameOriginPullCertificateResp():
    """
    certificate response.

    :attr HostnameCertificatePack result: (optional) certificate pack.
    :attr bool success: (optional) success.
    :attr List[str] errors: (optional)
    :attr List[str] messages: (optional)
    """

    def __init__(self,
                 *,
                 result: 'HostnameCertificatePack' = None,
                 success: bool = None,
                 errors: List[str] = None,
                 messages: List[str] = None) -> None:
        """
        Initialize a HostnameOriginPullCertificateResp object.

        :param HostnameCertificatePack result: (optional) certificate pack.
        :param bool success: (optional) success.
        :param List[str] errors: (optional)
        :param List[str] messages: (optional)
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HostnameOriginPullCertificateResp':
        """Initialize a HostnameOriginPullCertificateResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = HostnameCertificatePack.from_dict(_dict.get('result'))
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HostnameOriginPullCertificateResp object from a json dictionary."""
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
            _dict['messages'] = self.messages
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HostnameOriginPullCertificateResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HostnameOriginPullCertificateResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HostnameOriginPullCertificateResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class HostnameOriginPullSettings():
    """
    hostname-level authenticated origin pull settings request.

    :attr str hostname: the hostname on the origin for which the client certificate
          uploaded will be used.
    :attr str cert_id: certificate identifier tag.
    :attr bool enabled: enabled.
    """

    def __init__(self,
                 hostname: str,
                 cert_id: str,
                 enabled: bool) -> None:
        """
        Initialize a HostnameOriginPullSettings object.

        :param str hostname: the hostname on the origin for which the client
               certificate uploaded will be used.
        :param str cert_id: certificate identifier tag.
        :param bool enabled: enabled.
        """
        self.hostname = hostname
        self.cert_id = cert_id
        self.enabled = enabled

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HostnameOriginPullSettings':
        """Initialize a HostnameOriginPullSettings object from a json dictionary."""
        args = {}
        if 'hostname' in _dict:
            args['hostname'] = _dict.get('hostname')
        else:
            raise ValueError('Required property \'hostname\' not present in HostnameOriginPullSettings JSON')
        if 'cert_id' in _dict:
            args['cert_id'] = _dict.get('cert_id')
        else:
            raise ValueError('Required property \'cert_id\' not present in HostnameOriginPullSettings JSON')
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        else:
            raise ValueError('Required property \'enabled\' not present in HostnameOriginPullSettings JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HostnameOriginPullSettings object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'hostname') and self.hostname is not None:
            _dict['hostname'] = self.hostname
        if hasattr(self, 'cert_id') and self.cert_id is not None:
            _dict['cert_id'] = self.cert_id
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HostnameOriginPullSettings object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HostnameOriginPullSettings') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HostnameOriginPullSettings') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class HostnameSettingsResp():
    """
    hostname level authenticated origin pull settings response.

    :attr str hostname: (optional) the hostname on the origin for which the client
          certificate uploaded will be used.
    :attr str cert_id: (optional) certificate identifier tag.
    :attr bool enabled: (optional) enabled.
    :attr str status: (optional) status of the certificate activation.
    :attr datetime created_at: (optional) the time when the certificate was created.
    :attr datetime updated_at: (optional) the time when the certificate was updated.
    :attr str cert_status: (optional) status of the certificate or the association.
    :attr str issuer: (optional) the certificate authority that issued the
          certificate.
    :attr str signature: (optional) the type of hash used for the certificate.
    :attr str serial_number: (optional) the serial number on the uploaded
          certificate.
    :attr str certificate: (optional) the zone's leaf certificate.
    :attr datetime cert_uploaded_on: (optional) the time the certificate was
          uploaded.
    :attr datetime cert_updated_at: (optional) the time when the certificate was
          updated.
    :attr datetime expires_on: (optional) the date when the certificate expires.
    """

    def __init__(self,
                 *,
                 hostname: str = None,
                 cert_id: str = None,
                 enabled: bool = None,
                 status: str = None,
                 created_at: datetime = None,
                 updated_at: datetime = None,
                 cert_status: str = None,
                 issuer: str = None,
                 signature: str = None,
                 serial_number: str = None,
                 certificate: str = None,
                 cert_uploaded_on: datetime = None,
                 cert_updated_at: datetime = None,
                 expires_on: datetime = None) -> None:
        """
        Initialize a HostnameSettingsResp object.

        :param str hostname: (optional) the hostname on the origin for which the
               client certificate uploaded will be used.
        :param str cert_id: (optional) certificate identifier tag.
        :param bool enabled: (optional) enabled.
        :param str status: (optional) status of the certificate activation.
        :param datetime created_at: (optional) the time when the certificate was
               created.
        :param datetime updated_at: (optional) the time when the certificate was
               updated.
        :param str cert_status: (optional) status of the certificate or the
               association.
        :param str issuer: (optional) the certificate authority that issued the
               certificate.
        :param str signature: (optional) the type of hash used for the certificate.
        :param str serial_number: (optional) the serial number on the uploaded
               certificate.
        :param str certificate: (optional) the zone's leaf certificate.
        :param datetime cert_uploaded_on: (optional) the time the certificate was
               uploaded.
        :param datetime cert_updated_at: (optional) the time when the certificate
               was updated.
        :param datetime expires_on: (optional) the date when the certificate
               expires.
        """
        self.hostname = hostname
        self.cert_id = cert_id
        self.enabled = enabled
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
        self.cert_status = cert_status
        self.issuer = issuer
        self.signature = signature
        self.serial_number = serial_number
        self.certificate = certificate
        self.cert_uploaded_on = cert_uploaded_on
        self.cert_updated_at = cert_updated_at
        self.expires_on = expires_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HostnameSettingsResp':
        """Initialize a HostnameSettingsResp object from a json dictionary."""
        args = {}
        if 'hostname' in _dict:
            args['hostname'] = _dict.get('hostname')
        if 'cert_id' in _dict:
            args['cert_id'] = _dict.get('cert_id')
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'created_at' in _dict:
            args['created_at'] = string_to_datetime(_dict.get('created_at'))
        if 'updated_at' in _dict:
            args['updated_at'] = string_to_datetime(_dict.get('updated_at'))
        if 'cert_status' in _dict:
            args['cert_status'] = _dict.get('cert_status')
        if 'issuer' in _dict:
            args['issuer'] = _dict.get('issuer')
        if 'signature' in _dict:
            args['signature'] = _dict.get('signature')
        if 'serial_number' in _dict:
            args['serial_number'] = _dict.get('serial_number')
        if 'certificate' in _dict:
            args['certificate'] = _dict.get('certificate')
        if 'cert_uploaded_on' in _dict:
            args['cert_uploaded_on'] = string_to_datetime(_dict.get('cert_uploaded_on'))
        if 'cert_updated_at' in _dict:
            args['cert_updated_at'] = string_to_datetime(_dict.get('cert_updated_at'))
        if 'expires_on' in _dict:
            args['expires_on'] = string_to_datetime(_dict.get('expires_on'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HostnameSettingsResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'hostname') and self.hostname is not None:
            _dict['hostname'] = self.hostname
        if hasattr(self, 'cert_id') and self.cert_id is not None:
            _dict['cert_id'] = self.cert_id
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'created_at') and self.created_at is not None:
            _dict['created_at'] = datetime_to_string(self.created_at)
        if hasattr(self, 'updated_at') and self.updated_at is not None:
            _dict['updated_at'] = datetime_to_string(self.updated_at)
        if hasattr(self, 'cert_status') and self.cert_status is not None:
            _dict['cert_status'] = self.cert_status
        if hasattr(self, 'issuer') and self.issuer is not None:
            _dict['issuer'] = self.issuer
        if hasattr(self, 'signature') and self.signature is not None:
            _dict['signature'] = self.signature
        if hasattr(self, 'serial_number') and self.serial_number is not None:
            _dict['serial_number'] = self.serial_number
        if hasattr(self, 'certificate') and self.certificate is not None:
            _dict['certificate'] = self.certificate
        if hasattr(self, 'cert_uploaded_on') and self.cert_uploaded_on is not None:
            _dict['cert_uploaded_on'] = datetime_to_string(self.cert_uploaded_on)
        if hasattr(self, 'cert_updated_at') and self.cert_updated_at is not None:
            _dict['cert_updated_at'] = datetime_to_string(self.cert_updated_at)
        if hasattr(self, 'expires_on') and self.expires_on is not None:
            _dict['expires_on'] = datetime_to_string(self.expires_on)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HostnameSettingsResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HostnameSettingsResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HostnameSettingsResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListHostnameOriginPullSettingsResp():
    """
    array of hostname level authenticated origin pull settings response.

    :attr List[HostnameSettingsResp] result: (optional) array of hostname settings
          response.
    :attr bool success: (optional) success.
    :attr List[str] errors: (optional)
    :attr List[str] messages: (optional)
    """

    def __init__(self,
                 *,
                 result: List['HostnameSettingsResp'] = None,
                 success: bool = None,
                 errors: List[str] = None,
                 messages: List[str] = None) -> None:
        """
        Initialize a ListHostnameOriginPullSettingsResp object.

        :param List[HostnameSettingsResp] result: (optional) array of hostname
               settings response.
        :param bool success: (optional) success.
        :param List[str] errors: (optional)
        :param List[str] messages: (optional)
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListHostnameOriginPullSettingsResp':
        """Initialize a ListHostnameOriginPullSettingsResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = [HostnameSettingsResp.from_dict(x) for x in _dict.get('result')]
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListHostnameOriginPullSettingsResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'result') and self.result is not None:
            _dict['result'] = [x.to_dict() for x in self.result]
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = self.messages
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListHostnameOriginPullSettingsResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListHostnameOriginPullSettingsResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListHostnameOriginPullSettingsResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListZoneOriginPullCertificatesResp():
    """
    certificate response.

    :attr List[CertificatePack] result: (optional) list certificate packs.
    :attr bool success: (optional) success.
    :attr List[str] errors: (optional)
    :attr List[str] messages: (optional)
    """

    def __init__(self,
                 *,
                 result: List['CertificatePack'] = None,
                 success: bool = None,
                 errors: List[str] = None,
                 messages: List[str] = None) -> None:
        """
        Initialize a ListZoneOriginPullCertificatesResp object.

        :param List[CertificatePack] result: (optional) list certificate packs.
        :param bool success: (optional) success.
        :param List[str] errors: (optional)
        :param List[str] messages: (optional)
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListZoneOriginPullCertificatesResp':
        """Initialize a ListZoneOriginPullCertificatesResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = [CertificatePack.from_dict(x) for x in _dict.get('result')]
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListZoneOriginPullCertificatesResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'result') and self.result is not None:
            _dict['result'] = [x.to_dict() for x in self.result]
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = self.messages
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListZoneOriginPullCertificatesResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListZoneOriginPullCertificatesResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListZoneOriginPullCertificatesResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ZoneOriginPullCertificateResp():
    """
    zone level authenticated origin pull certificate response.

    :attr CertificatePack result: (optional) certificate pack.
    :attr bool success: (optional) success.
    :attr List[str] errors: (optional)
    :attr List[str] messages: (optional)
    """

    def __init__(self,
                 *,
                 result: 'CertificatePack' = None,
                 success: bool = None,
                 errors: List[str] = None,
                 messages: List[str] = None) -> None:
        """
        Initialize a ZoneOriginPullCertificateResp object.

        :param CertificatePack result: (optional) certificate pack.
        :param bool success: (optional) success.
        :param List[str] errors: (optional)
        :param List[str] messages: (optional)
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ZoneOriginPullCertificateResp':
        """Initialize a ZoneOriginPullCertificateResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = CertificatePack.from_dict(_dict.get('result'))
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ZoneOriginPullCertificateResp object from a json dictionary."""
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
            _dict['messages'] = self.messages
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ZoneOriginPullCertificateResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ZoneOriginPullCertificateResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ZoneOriginPullCertificateResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
