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
CIS Zones Settings
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

class ZonesSettingsV1(BaseService):
    """The Zones Settings V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'zones_settings'

    @classmethod
    def new_instance(cls,
                     crn: str,
                     zone_identifier: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'ZonesSettingsV1':
        """
        Return a new client for the Zones Settings service using the specified
               parameters and external configuration.

        :param str crn: Full url-encoded cloud resource name (CRN) of resource
               instance.

        :param str zone_identifier: Zone identifier.
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
        Construct a new client for the Zones Settings service.

        :param str crn: Full url-encoded cloud resource name (CRN) of resource
               instance.

        :param str zone_identifier: Zone identifier.

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
    # Zones Settings
    #########################


    def get_zone_dnssec(self, **kwargs) -> DetailedResponse:
        """
        Get zone DNSSEC.

        Get DNSSEC setting for a given zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_zone_dnssec')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/dnssec'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_zone_dnssec(self, *, accept: str = None, status: str = None, **kwargs) -> DetailedResponse:
        """
        Update zone DNSSEC.

        Update DNSSEC setting for given zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param str status: (optional) Status.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ZonesDnssecResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_zone_dnssec')
        headers.update(sdk_headers)

        data = {
            'status': status
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/dnssec'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_zone_cname_flattening(self, *, accept: str = None, **kwargs) -> DetailedResponse:
        """
        Get zone CNAME flattening.

        Get CNAME flattening setting for a given zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ZonesCnameFlatteningResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_zone_cname_flattening')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/cname_flattening'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_zone_cname_flattening(self, *, accept: str = None, value: str = None, **kwargs) -> DetailedResponse:
        """
        Update zone CNAME flattening.

        Update CNAME flattening setting for given zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param str value: (optional) Valid values are "flatten_at_root",
               "flatten_all". "flatten_at_root" - Flatten CNAME at root domain. This is
               the default value. "flatten_all" - Flatten all CNAME records under your
               domain.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ZonesCnameFlatteningResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_zone_cname_flattening')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/cname_flattening'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_opportunistic_encryption(self, *, accept: str = None, **kwargs) -> DetailedResponse:
        """
        Get opportunistic encryption setting.

        Get opportunistic encryption setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `OpportunisticEncryptionResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_opportunistic_encryption')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/opportunistic_encryption'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_opportunistic_encryption(self, *, accept: str = None, value: str = None, **kwargs) -> DetailedResponse:
        """
        Update opportunistic encryption setting.

        Update opportunistic encryption setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `OpportunisticEncryptionResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_opportunistic_encryption')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/opportunistic_encryption'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_challenge_ttl(self, *, accept: str = None, **kwargs) -> DetailedResponse:
        """
        Get challenge TTL setting.

        Get challenge TTL setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ChallengeTtlResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_challenge_ttl')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/challenge_ttl'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_challenge_ttl(self, *, accept: str = None, value: int = None, **kwargs) -> DetailedResponse:
        """
        Update challenge TTL setting.

        Update challenge TTL setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param int value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ChallengeTtlResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_challenge_ttl')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/challenge_ttl'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_automatic_https_rewrites(self, *, accept: str = None, **kwargs) -> DetailedResponse:
        """
        Get automatic https rewrites setting.

        Get automatic https rewrites setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AutomaticHttpsRewritesResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_automatic_https_rewrites')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/automatic_https_rewrites'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_automatic_https_rewrites(self, *, accept: str = None, value: str = None, **kwargs) -> DetailedResponse:
        """
        Update automatic https rewrites setting.

        Update automatic https rewrites setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AutomaticHttpsRewritesResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_automatic_https_rewrites')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/automatic_https_rewrites'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_ture_client_ip(self, *, accept: str = None, **kwargs) -> DetailedResponse:
        """
        Get true client IP setting.

        Get true client IP setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TrueClientIpResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_ture_client_ip')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/true_client_ip_header'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_true_client_ip(self, *, accept: str = None, value: str = None, **kwargs) -> DetailedResponse:
        """
        Update true client IP setting.

        Update true client IP setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TrueClientIpResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_true_client_ip')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/true_client_ip_header'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_always_use_https(self, *, accept: str = None, **kwargs) -> DetailedResponse:
        """
        Get always use https setting.

        Get always use https setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AlwaysUseHttpsResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_always_use_https')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/always_use_https'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_always_use_https(self, *, accept: str = None, value: str = None, **kwargs) -> DetailedResponse:
        """
        Update always use https setting.

        Update always use https setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AlwaysUseHttpsResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_always_use_https')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/always_use_https'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_image_size_optimization(self, *, accept: str = None, **kwargs) -> DetailedResponse:
        """
        Get image size optimization setting.

        Get image size optimization setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ImageSizeOptimizationResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_image_size_optimization')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/image_size_optimization'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_image_size_optimization(self, *, accept: str = None, value: str = None, **kwargs) -> DetailedResponse:
        """
        Update image size optimization setting.

        Update image size optimization setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param str value: (optional) Valid values are "lossy", "off", "lossless".
               "lossy" - The file size of JPEG images is reduced using lossy compression,
               which may reduce visual quality. "off" - Disable Image Size Optimization.
               "lossless" - Reduce the size of image files without impacting visual
               quality.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ImageSizeOptimizationResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_image_size_optimization')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/image_size_optimization'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_script_load_optimization(self, *, accept: str = None, **kwargs) -> DetailedResponse:
        """
        Get script load optimization setting.

        Get script load optimization setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ScriptLoadOptimizationResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_script_load_optimization')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/script_load_optimization'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_script_load_optimization(self, *, accept: str = None, value: str = None, **kwargs) -> DetailedResponse:
        """
        Update script load optimization setting.

        Update script load optimization setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ScriptLoadOptimizationResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_script_load_optimization')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/script_load_optimization'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_image_load_optimization(self, *, accept: str = None, **kwargs) -> DetailedResponse:
        """
        Get image load optimizationn setting.

        Get image load optimizationn setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ImageLoadOptimizationResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_image_load_optimization')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/image_load_optimization'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_image_load_optimization(self, *, accept: str = None, value: str = None, **kwargs) -> DetailedResponse:
        """
        Update image load optimizationn setting.

        Update image load optimizationn setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ImageLoadOptimizationResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_image_load_optimization')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/image_load_optimization'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_minify(self, *, accept: str = None, **kwargs) -> DetailedResponse:
        """
        Get minify setting.

        Get minify setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `MinifyResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_minify')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/minify'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    def update_minify(self, *, accept: str = None, value: 'MinifySettingValue' = None, **kwargs) -> DetailedResponse:
        """
        Update minify setting.

        Update minify setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param MinifySettingValue value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `MinifyResp` object
        """

        if value is not None:
            value = convert_model(value)
        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_minify')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/minify'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_min_tls_version(self, *, accept: str = None, **kwargs) -> DetailedResponse:
        """
        Get minimum TLS version setting.

        Get minimum TLS version setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `MinTlsVersionResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_min_tls_version')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/min_tls_version'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_min_tls_version(self, *, accept: str = None, value: str = None, **kwargs) -> DetailedResponse:
        """
        Update minimum TLS version setting.

        Update minimum TLS version setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `MinTlsVersionResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_min_tls_version')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/min_tls_version'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_ip_geolocation(self, *, accept: str = None, **kwargs) -> DetailedResponse:
        """
        Get IP geolocation setting.

        Get IP geolocation setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `IpGeolocationResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_ip_geolocation')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/ip_geolocation'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_ip_geolocation(self, *, accept: str = None, value: str = None, **kwargs) -> DetailedResponse:
        """
        Update IP geolocation setting.

        Update IP geolocation setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `IpGeolocationResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_ip_geolocation')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/ip_geolocation'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_server_side_exclude(self, *, accept: str = None, **kwargs) -> DetailedResponse:
        """
        Get server side exclude setting.

        Get server side exclude setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ServerSideExcludeResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_server_side_exclude')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/server_side_exclude'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_server_side_exclude(self, *, accept: str = None, value: str = None, **kwargs) -> DetailedResponse:
        """
        Update server side exclude setting.

        Update server side exclude setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ServerSideExcludeResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_server_side_exclude')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/server_side_exclude'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_security_header(self, *, accept: str = None, **kwargs) -> DetailedResponse:
        """
        Get HTTP strict transport security setting.

        Get HTTP strict transport security setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SecurityHeaderResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_security_header')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/security_header'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_security_header(self, *, accept: str = None, value: 'SecurityHeaderSettingValue' = None, **kwargs) -> DetailedResponse:
        """
        Update HTTP strict transport security setting.

        Update HTTP strict transport security setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param SecurityHeaderSettingValue value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SecurityHeaderResp` object
        """

        if value is not None:
            value = convert_model(value)
        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_security_header')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/security_header'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_mobile_redirect(self, *, accept: str = None, **kwargs) -> DetailedResponse:
        """
        Get mobile redirect setting.

        Get mobile redirect setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `MobileRedirectResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_mobile_redirect')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/mobile_redirect'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_mobile_redirect(self, *, accept: str = None, value: 'MobileRedirecSettingValue' = None, **kwargs) -> DetailedResponse:
        """
        Update mobile redirect setting.

        Update mobile redirect setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param MobileRedirecSettingValue value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `MobileRedirectResp` object
        """

        if value is not None:
            value = convert_model(value)
        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_mobile_redirect')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/mobile_redirect'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_prefetch_preload(self, *, accept: str = None, **kwargs) -> DetailedResponse:
        """
        Get prefetch URLs from header setting.

        Get prefetch URLs from header setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PrefetchPreloadResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_prefetch_preload')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/prefetch_preload'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_prefetch_preload(self, *, accept: str = None, value: str = None, **kwargs) -> DetailedResponse:
        """
        Update prefetch URLs from header setting.

        Update prefetch URLs from header setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PrefetchPreloadResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_prefetch_preload')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/prefetch_preload'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_http2(self, *, accept: str = None, **kwargs) -> DetailedResponse:
        """
        Get http/2 setting.

        Get http/2 setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Http2Resp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_http2')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/http2'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_http2(self, *, accept: str = None, value: str = None, **kwargs) -> DetailedResponse:
        """
        Update http/2 setting.

        Update http/2 setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Http2Resp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_http2')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/http2'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_ipv6(self, *, accept: str = None, **kwargs) -> DetailedResponse:
        """
        Get IPv6 compatibility setting.

        Get IPv6 compatibility setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Ipv6Resp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_ipv6')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/ipv6'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_ipv6(self, *, accept: str = None, value: str = None, **kwargs) -> DetailedResponse:
        """
        Update IPv6 compatibility setting.

        Update IPv6 compatibility setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Ipv6Resp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_ipv6')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/ipv6'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_web_sockets(self, *, accept: str = None, **kwargs) -> DetailedResponse:
        """
        Get web sockets setting.

        Get web sockets setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `WebsocketsResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_web_sockets')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/websockets'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_web_sockets(self, *, accept: str = None, value: str = None, **kwargs) -> DetailedResponse:
        """
        Update web sockets setting.

        Update web sockets setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `WebsocketsResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_web_sockets')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/websockets'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_pseudo_ipv4(self, *, accept: str = None, **kwargs) -> DetailedResponse:
        """
        Get pseudo IPv4 setting.

        Get pseudo IPv4 setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PseudoIpv4Resp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_pseudo_ipv4')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/pseudo_ipv4'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_pseudo_ipv4(self, *, accept: str = None, value: str = None, **kwargs) -> DetailedResponse:
        """
        Update pseudo IPv4 setting.

        Update pseudo IPv4 setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PseudoIpv4Resp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_pseudo_ipv4')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/pseudo_ipv4'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_response_buffering(self, *, accept: str = None, **kwargs) -> DetailedResponse:
        """
        Get response buffering setting.

        Get response buffering setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResponseBufferingResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_response_buffering')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/response_buffering'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_response_buffering(self, *, accept: str = None, value: str = None, **kwargs) -> DetailedResponse:
        """
        Update response buffering setting.

        Update response buffering setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResponseBufferingResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_response_buffering')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/response_buffering'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_hotlink_protection(self, *, accept: str = None, **kwargs) -> DetailedResponse:
        """
        Get hotlink protection setting.

        Get hotlink protection setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `HotlinkProtectionResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_hotlink_protection')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/hotlink_protection'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_hotlink_protection(self, *, accept: str = None, value: str = None, **kwargs) -> DetailedResponse:
        """
        Update hotlink protection setting.

        Update hotlink protection setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `HotlinkProtectionResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_hotlink_protection')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/hotlink_protection'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_max_upload(self, *, accept: str = None, **kwargs) -> DetailedResponse:
        """
        Get maximum upload size setting.

        Get maximum upload size setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `MaxUploadResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_max_upload')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/max_upload'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_max_upload(self, *, accept: str = None, value: int = None, **kwargs) -> DetailedResponse:
        """
        Update maximum upload size setting.

        Update maximum upload size setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param int value: (optional) Valid values(in MB) for "max_upload" are 100,
               125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475,
               500. Values 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500 are
               only for Enterprise Plan.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `MaxUploadResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_max_upload')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/max_upload'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_tls_client_auth(self, *, accept: str = None, **kwargs) -> DetailedResponse:
        """
        Get TLS Client Auth setting.

        Get TLS Client Auth setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TlsClientAuthResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_tls_client_auth')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/tls_client_auth'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_tls_client_auth(self, *, accept: str = None, value: str = None, **kwargs) -> DetailedResponse:
        """
        Update TLS Client Auth setting.

        Update TLS Client Auth setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TlsClientAuthResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_tls_client_auth')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/tls_client_auth'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_browser_check(self, *, accept: str = None, **kwargs) -> DetailedResponse:
        """
        Get browser check setting.

        Get browser check setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BrowserCheckResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_browser_check')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/browser_check'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_browser_check(self, *, accept: str = None, value: str = None, **kwargs) -> DetailedResponse:
        """
        Update browser check setting.

        Update browser check setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BrowserCheckResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_browser_check')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/browser_check'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_enable_error_pages_on(self, **kwargs) -> DetailedResponse:
        """
        Get enable error pages on setting.

        Get enable error pages on setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_enable_error_pages_on')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/origin_error_page_pass_thru'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_enable_error_pages_on(self, *, accept: str = None, value: str = None, **kwargs) -> DetailedResponse:
        """
        Update enable error pages on setting.

        Update enable error pages on setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `OriginErrorPagePassThruResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_enable_error_pages_on')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/origin_error_page_pass_thru'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_web_application_firewall(self, *, accept: str = None, **kwargs) -> DetailedResponse:
        """
        Get web application firewall setting.

        Get web application firewall setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `WafResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_web_application_firewall')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/waf'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_web_application_firewall(self, *, accept: str = None, value: str = None, **kwargs) -> DetailedResponse:
        """
        Update web application firewall setting.

        A Web Application Firewall (WAF) blocks requests that contain malicious content.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `WafResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_web_application_firewall')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/waf'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_ciphers(self, *, accept: str = None, **kwargs) -> DetailedResponse:
        """
        Get ciphers setting.

        Get ciphers setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CiphersResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_ciphers')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/ciphers'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_ciphers(self, *, accept: str = None, value: List[List[str]] = None, **kwargs) -> DetailedResponse:
        """
        Update ciphers setting.

        Update ciphers setting for a zone.

        :param str accept: (optional) The type of the response: *_/_* or
               application/json.
        :param List[List[str]] value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CiphersResp` object
        """

        headers = {
            'Accept': accept
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_ciphers')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/ciphers'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

