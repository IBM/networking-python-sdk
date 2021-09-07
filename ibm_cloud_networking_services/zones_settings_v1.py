# coding: utf-8

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

# IBM OpenAPI SDK Code Generator Version: 3.29.1-b338fb38-20210313-010605
 
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


    def get_zone_dnssec(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get zone DNSSEC.

        Get DNSSEC setting for a given zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ZonesDnssecResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_zone_dnssec')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/dnssec'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_zone_dnssec(self,
        *,
        status: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update zone DNSSEC.

        Update DNSSEC setting for given zone.

        :param str status: (optional) Status.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ZonesDnssecResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_zone_dnssec')
        headers.update(sdk_headers)

        data = {
            'status': status
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
        url = '/v1/{crn}/zones/{zone_identifier}/dnssec'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_zone_cname_flattening(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get zone CNAME flattening.

        Get CNAME flattening setting for a given zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ZonesCnameFlatteningResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_zone_cname_flattening')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/settings/cname_flattening'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_zone_cname_flattening(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update zone CNAME flattening.

        Update CNAME flattening setting for given zone.

        :param str value: (optional) Valid values are "flatten_at_root",
               "flatten_all". "flatten_at_root" - Flatten CNAME at root domain. This is
               the default value. "flatten_all" - Flatten all CNAME records under your
               domain.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ZonesCnameFlatteningResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_zone_cname_flattening')
        headers.update(sdk_headers)

        data = {
            'value': value
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
        url = '/v1/{crn}/zones/{zone_identifier}/settings/cname_flattening'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_opportunistic_encryption(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get opportunistic encryption setting.

        Get opportunistic encryption setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `OpportunisticEncryptionResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_opportunistic_encryption')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/settings/opportunistic_encryption'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_opportunistic_encryption(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update opportunistic encryption setting.

        Update opportunistic encryption setting for a zone.

        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `OpportunisticEncryptionResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_opportunistic_encryption')
        headers.update(sdk_headers)

        data = {
            'value': value
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
        url = '/v1/{crn}/zones/{zone_identifier}/settings/opportunistic_encryption'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_challenge_ttl(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get challenge TTL setting.

        Get challenge TTL setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ChallengeTtlResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_challenge_ttl')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/settings/challenge_ttl'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_challenge_ttl(self,
        *,
        value: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update challenge TTL setting.

        Update challenge TTL setting for a zone.

        :param int value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ChallengeTtlResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_challenge_ttl')
        headers.update(sdk_headers)

        data = {
            'value': value
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
        url = '/v1/{crn}/zones/{zone_identifier}/settings/challenge_ttl'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_automatic_https_rewrites(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get automatic https rewrites setting.

        Get automatic https rewrites setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AutomaticHttpsRewritesResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_automatic_https_rewrites')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/settings/automatic_https_rewrites'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_automatic_https_rewrites(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update automatic https rewrites setting.

        Update automatic https rewrites setting for a zone.

        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AutomaticHttpsRewritesResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_automatic_https_rewrites')
        headers.update(sdk_headers)

        data = {
            'value': value
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
        url = '/v1/{crn}/zones/{zone_identifier}/settings/automatic_https_rewrites'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_true_client_ip(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get true client IP setting.

        Get true client IP setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TrueClientIpResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_true_client_ip')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/settings/true_client_ip_header'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_true_client_ip(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update true client IP setting.

        Update true client IP setting for a zone.

        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TrueClientIpResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_true_client_ip')
        headers.update(sdk_headers)

        data = {
            'value': value
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
        url = '/v1/{crn}/zones/{zone_identifier}/settings/true_client_ip_header'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_always_use_https(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get always use https setting.

        Get always use https setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AlwaysUseHttpsResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_always_use_https')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/settings/always_use_https'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_always_use_https(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update always use https setting.

        Update always use https setting for a zone.

        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AlwaysUseHttpsResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_always_use_https')
        headers.update(sdk_headers)

        data = {
            'value': value
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
        url = '/v1/{crn}/zones/{zone_identifier}/settings/always_use_https'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_image_size_optimization(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get image size optimization setting.

        Get image size optimization setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ImageSizeOptimizationResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_image_size_optimization')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/settings/image_size_optimization'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_image_size_optimization(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update image size optimization setting.

        Update image size optimization setting for a zone.

        :param str value: (optional) Valid values are "lossy", "off", "lossless".
               "lossy" - The file size of JPEG images is reduced using lossy compression,
               which may reduce visual quality. "off" - Disable Image Size Optimization.
               "lossless" - Reduce the size of image files without impacting visual
               quality.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ImageSizeOptimizationResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_image_size_optimization')
        headers.update(sdk_headers)

        data = {
            'value': value
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
        url = '/v1/{crn}/zones/{zone_identifier}/settings/image_size_optimization'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_script_load_optimization(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get script load optimization setting.

        Get script load optimization setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ScriptLoadOptimizationResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_script_load_optimization')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/settings/script_load_optimization'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_script_load_optimization(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update script load optimization setting.

        Update script load optimization setting for a zone.

        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ScriptLoadOptimizationResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_script_load_optimization')
        headers.update(sdk_headers)

        data = {
            'value': value
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
        url = '/v1/{crn}/zones/{zone_identifier}/settings/script_load_optimization'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_image_load_optimization(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get image load optimizationn setting.

        Get image load optimizationn setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ImageLoadOptimizationResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_image_load_optimization')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/settings/image_load_optimization'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_image_load_optimization(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update image load optimizationn setting.

        Update image load optimizationn setting for a zone.

        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ImageLoadOptimizationResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_image_load_optimization')
        headers.update(sdk_headers)

        data = {
            'value': value
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
        url = '/v1/{crn}/zones/{zone_identifier}/settings/image_load_optimization'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_minify(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get minify setting.

        Get minify setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `MinifyResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_minify')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/settings/minify'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_minify(self,
        *,
        value: 'MinifySettingValue' = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update minify setting.

        Update minify setting for a zone.

        :param MinifySettingValue value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `MinifyResp` object
        """

        if value is not None:
            value = convert_model(value)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_minify')
        headers.update(sdk_headers)

        data = {
            'value': value
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
        url = '/v1/{crn}/zones/{zone_identifier}/settings/minify'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_min_tls_version(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get minimum TLS version setting.

        Get minimum TLS version setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `MinTlsVersionResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_min_tls_version')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/settings/min_tls_version'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_min_tls_version(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update minimum TLS version setting.

        Update minimum TLS version setting for a zone.

        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `MinTlsVersionResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_min_tls_version')
        headers.update(sdk_headers)

        data = {
            'value': value
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
        url = '/v1/{crn}/zones/{zone_identifier}/settings/min_tls_version'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_ip_geolocation(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get IP geolocation setting.

        Get IP geolocation setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `IpGeolocationResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_ip_geolocation')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/settings/ip_geolocation'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_ip_geolocation(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update IP geolocation setting.

        Update IP geolocation setting for a zone.

        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `IpGeolocationResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_ip_geolocation')
        headers.update(sdk_headers)

        data = {
            'value': value
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
        url = '/v1/{crn}/zones/{zone_identifier}/settings/ip_geolocation'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_server_side_exclude(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get server side exclude setting.

        Get server side exclude setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ServerSideExcludeResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_server_side_exclude')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/settings/server_side_exclude'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_server_side_exclude(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update server side exclude setting.

        Update server side exclude setting for a zone.

        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ServerSideExcludeResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_server_side_exclude')
        headers.update(sdk_headers)

        data = {
            'value': value
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
        url = '/v1/{crn}/zones/{zone_identifier}/settings/server_side_exclude'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_security_header(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get HTTP strict transport security setting.

        Get HTTP strict transport security setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SecurityHeaderResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_security_header')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/settings/security_header'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_security_header(self,
        *,
        value: 'SecurityHeaderSettingValue' = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update HTTP strict transport security setting.

        Update HTTP strict transport security setting for a zone.

        :param SecurityHeaderSettingValue value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SecurityHeaderResp` object
        """

        if value is not None:
            value = convert_model(value)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_security_header')
        headers.update(sdk_headers)

        data = {
            'value': value
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
        url = '/v1/{crn}/zones/{zone_identifier}/settings/security_header'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_mobile_redirect(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get mobile redirect setting.

        Get mobile redirect setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `MobileRedirectResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_mobile_redirect')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/settings/mobile_redirect'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_mobile_redirect(self,
        *,
        value: 'MobileRedirecSettingValue' = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update mobile redirect setting.

        Update mobile redirect setting for a zone.

        :param MobileRedirecSettingValue value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `MobileRedirectResp` object
        """

        if value is not None:
            value = convert_model(value)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_mobile_redirect')
        headers.update(sdk_headers)

        data = {
            'value': value
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
        url = '/v1/{crn}/zones/{zone_identifier}/settings/mobile_redirect'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_prefetch_preload(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get prefetch URLs from header setting.

        Get prefetch URLs from header setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PrefetchPreloadResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_prefetch_preload')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/settings/prefetch_preload'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_prefetch_preload(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update prefetch URLs from header setting.

        Update prefetch URLs from header setting for a zone.

        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PrefetchPreloadResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_prefetch_preload')
        headers.update(sdk_headers)

        data = {
            'value': value
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
        url = '/v1/{crn}/zones/{zone_identifier}/settings/prefetch_preload'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_http2(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get http/2 setting.

        Get http/2 setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Http2Resp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_http2')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/settings/http2'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_http2(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update http/2 setting.

        Update http/2 setting for a zone.

        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Http2Resp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_http2')
        headers.update(sdk_headers)

        data = {
            'value': value
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
        url = '/v1/{crn}/zones/{zone_identifier}/settings/http2'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_http3(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get http/3 setting.

        Get http/3 setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Http3Resp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_http3')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/settings/http3'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_http3(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update http/3 setting.

        Update http/3 setting for a zone.

        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Http3Resp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_http3')
        headers.update(sdk_headers)

        data = {
            'value': value
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
        url = '/v1/{crn}/zones/{zone_identifier}/settings/http3'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_ipv6(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get IPv6 compatibility setting.

        Get IPv6 compatibility setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Ipv6Resp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_ipv6')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/settings/ipv6'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_ipv6(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update IPv6 compatibility setting.

        Update IPv6 compatibility setting for a zone.

        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Ipv6Resp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_ipv6')
        headers.update(sdk_headers)

        data = {
            'value': value
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
        url = '/v1/{crn}/zones/{zone_identifier}/settings/ipv6'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_web_sockets(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get web sockets setting.

        Get web sockets setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `WebsocketsResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_web_sockets')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/settings/websockets'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_web_sockets(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update web sockets setting.

        Update web sockets setting for a zone.

        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `WebsocketsResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_web_sockets')
        headers.update(sdk_headers)

        data = {
            'value': value
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
        url = '/v1/{crn}/zones/{zone_identifier}/settings/websockets'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_pseudo_ipv4(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get pseudo IPv4 setting.

        Get pseudo IPv4 setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PseudoIpv4Resp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_pseudo_ipv4')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/settings/pseudo_ipv4'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_pseudo_ipv4(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update pseudo IPv4 setting.

        Update pseudo IPv4 setting for a zone.

        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PseudoIpv4Resp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_pseudo_ipv4')
        headers.update(sdk_headers)

        data = {
            'value': value
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
        url = '/v1/{crn}/zones/{zone_identifier}/settings/pseudo_ipv4'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_response_buffering(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get response buffering setting.

        Get response buffering setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResponseBufferingResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_response_buffering')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/settings/response_buffering'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_response_buffering(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update response buffering setting.

        Update response buffering setting for a zone.

        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResponseBufferingResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_response_buffering')
        headers.update(sdk_headers)

        data = {
            'value': value
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
        url = '/v1/{crn}/zones/{zone_identifier}/settings/response_buffering'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_hotlink_protection(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get hotlink protection setting.

        Get hotlink protection setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `HotlinkProtectionResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_hotlink_protection')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/settings/hotlink_protection'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_hotlink_protection(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update hotlink protection setting.

        Update hotlink protection setting for a zone.

        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `HotlinkProtectionResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_hotlink_protection')
        headers.update(sdk_headers)

        data = {
            'value': value
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
        url = '/v1/{crn}/zones/{zone_identifier}/settings/hotlink_protection'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_max_upload(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get maximum upload size setting.

        Get maximum upload size setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `MaxUploadResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_max_upload')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/settings/max_upload'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_max_upload(self,
        *,
        value: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update maximum upload size setting.

        Update maximum upload size setting for a zone.

        :param int value: (optional) Valid values(in MB) for "max_upload" are 100,
               125, 150, 175, 200, 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475,
               500. Values 225, 250, 275, 300, 325, 350, 375, 400, 425, 450, 475, 500 are
               only for Enterprise Plan.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `MaxUploadResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_max_upload')
        headers.update(sdk_headers)

        data = {
            'value': value
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
        url = '/v1/{crn}/zones/{zone_identifier}/settings/max_upload'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_tls_client_auth(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get TLS Client Auth setting.

        Get TLS Client Auth setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TlsClientAuthResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_tls_client_auth')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/settings/tls_client_auth'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_tls_client_auth(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update TLS Client Auth setting.

        Update TLS Client Auth setting for a zone.

        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `TlsClientAuthResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_tls_client_auth')
        headers.update(sdk_headers)

        data = {
            'value': value
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
        url = '/v1/{crn}/zones/{zone_identifier}/settings/tls_client_auth'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_browser_check(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get browser check setting.

        Get browser check setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BrowserCheckResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_browser_check')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/settings/browser_check'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_browser_check(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update browser check setting.

        Update browser check setting for a zone.

        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BrowserCheckResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_browser_check')
        headers.update(sdk_headers)

        data = {
            'value': value
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
        url = '/v1/{crn}/zones/{zone_identifier}/settings/browser_check'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_enable_error_pages_on(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get enable error pages on setting.

        Get enable error pages on setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `OriginErrorPagePassThruResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_enable_error_pages_on')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/settings/origin_error_page_pass_thru'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_enable_error_pages_on(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update enable error pages on setting.

        Update enable error pages on setting for a zone.

        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `OriginErrorPagePassThruResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_enable_error_pages_on')
        headers.update(sdk_headers)

        data = {
            'value': value
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
        url = '/v1/{crn}/zones/{zone_identifier}/settings/origin_error_page_pass_thru'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_web_application_firewall(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get web application firewall setting.

        Get web application firewall setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `WafResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_web_application_firewall')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/settings/waf'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_web_application_firewall(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update web application firewall setting.

        A Web Application Firewall (WAF) blocks requests that contain malicious content.

        :param str value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `WafResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_web_application_firewall')
        headers.update(sdk_headers)

        data = {
            'value': value
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
        url = '/v1/{crn}/zones/{zone_identifier}/settings/waf'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_ciphers(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get ciphers setting.

        Get ciphers setting for a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CiphersResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_ciphers')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/settings/ciphers'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_ciphers(self,
        *,
        value: List[str] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update ciphers setting.

        Update ciphers setting for a zone.

        :param List[str] value: (optional) Value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CiphersResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_ciphers')
        headers.update(sdk_headers)

        data = {
            'value': value
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
        url = '/v1/{crn}/zones/{zone_identifier}/settings/ciphers'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class AlwaysUseHttpsRespResult():
    """
    Container for response information.

    :attr str id: ID.
    :attr str value: Value.
    :attr bool editable: Editable.
    :attr datetime modified_on: Modified date.
    """

    def __init__(self,
                 id: str,
                 value: str,
                 editable: bool,
                 modified_on: datetime) -> None:
        """
        Initialize a AlwaysUseHttpsRespResult object.

        :param str id: ID.
        :param str value: Value.
        :param bool editable: Editable.
        :param datetime modified_on: Modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AlwaysUseHttpsRespResult':
        """Initialize a AlwaysUseHttpsRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in AlwaysUseHttpsRespResult JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in AlwaysUseHttpsRespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in AlwaysUseHttpsRespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in AlwaysUseHttpsRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AlwaysUseHttpsRespResult object from a json dictionary."""
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
        """Return a `str` version of this AlwaysUseHttpsRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AlwaysUseHttpsRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AlwaysUseHttpsRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AutomaticHttpsRewritesRespResult():
    """
    Container for response information.

    :attr str id: ID.
    :attr str value: Value.
    :attr bool editable: Editable.
    :attr datetime modified_on: Modified date.
    """

    def __init__(self,
                 id: str,
                 value: str,
                 editable: bool,
                 modified_on: datetime) -> None:
        """
        Initialize a AutomaticHttpsRewritesRespResult object.

        :param str id: ID.
        :param str value: Value.
        :param bool editable: Editable.
        :param datetime modified_on: Modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AutomaticHttpsRewritesRespResult':
        """Initialize a AutomaticHttpsRewritesRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in AutomaticHttpsRewritesRespResult JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in AutomaticHttpsRewritesRespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in AutomaticHttpsRewritesRespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in AutomaticHttpsRewritesRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AutomaticHttpsRewritesRespResult object from a json dictionary."""
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
        """Return a `str` version of this AutomaticHttpsRewritesRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AutomaticHttpsRewritesRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AutomaticHttpsRewritesRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class BrowserCheckRespResult():
    """
    Container for response information.

    :attr str id: ID.
    :attr str value: Value.
    :attr bool editable: Editable.
    :attr datetime modified_on: Modified date.
    """

    def __init__(self,
                 id: str,
                 value: str,
                 editable: bool,
                 modified_on: datetime) -> None:
        """
        Initialize a BrowserCheckRespResult object.

        :param str id: ID.
        :param str value: Value.
        :param bool editable: Editable.
        :param datetime modified_on: Modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BrowserCheckRespResult':
        """Initialize a BrowserCheckRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in BrowserCheckRespResult JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in BrowserCheckRespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in BrowserCheckRespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in BrowserCheckRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BrowserCheckRespResult object from a json dictionary."""
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
        """Return a `str` version of this BrowserCheckRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BrowserCheckRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BrowserCheckRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ChallengeTtlRespResult():
    """
    Container for response information.

    :attr str id: ID.
    :attr int value: Value.
    :attr bool editable: Editable.
    :attr datetime modified_on: Modified date.
    """

    def __init__(self,
                 id: str,
                 value: int,
                 editable: bool,
                 modified_on: datetime) -> None:
        """
        Initialize a ChallengeTtlRespResult object.

        :param str id: ID.
        :param int value: Value.
        :param bool editable: Editable.
        :param datetime modified_on: Modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ChallengeTtlRespResult':
        """Initialize a ChallengeTtlRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ChallengeTtlRespResult JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in ChallengeTtlRespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in ChallengeTtlRespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in ChallengeTtlRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ChallengeTtlRespResult object from a json dictionary."""
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
        """Return a `str` version of this ChallengeTtlRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ChallengeTtlRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ChallengeTtlRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CiphersRespResult():
    """
    Container for response information.

    :attr str id: ID.
    :attr List[str] value: Value.
    :attr bool editable: Editable.
    :attr datetime modified_on: Modified date.
    """

    def __init__(self,
                 id: str,
                 value: List[str],
                 editable: bool,
                 modified_on: datetime) -> None:
        """
        Initialize a CiphersRespResult object.

        :param str id: ID.
        :param List[str] value: Value.
        :param bool editable: Editable.
        :param datetime modified_on: Modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CiphersRespResult':
        """Initialize a CiphersRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in CiphersRespResult JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in CiphersRespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in CiphersRespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in CiphersRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CiphersRespResult object from a json dictionary."""
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
        """Return a `str` version of this CiphersRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CiphersRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CiphersRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class HotlinkProtectionRespResult():
    """
    Container for response information.

    :attr str id: ID.
    :attr str value: Value.
    :attr bool editable: Editable.
    :attr datetime modified_on: Modified date.
    """

    def __init__(self,
                 id: str,
                 value: str,
                 editable: bool,
                 modified_on: datetime) -> None:
        """
        Initialize a HotlinkProtectionRespResult object.

        :param str id: ID.
        :param str value: Value.
        :param bool editable: Editable.
        :param datetime modified_on: Modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HotlinkProtectionRespResult':
        """Initialize a HotlinkProtectionRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in HotlinkProtectionRespResult JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in HotlinkProtectionRespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in HotlinkProtectionRespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in HotlinkProtectionRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HotlinkProtectionRespResult object from a json dictionary."""
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
        """Return a `str` version of this HotlinkProtectionRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HotlinkProtectionRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HotlinkProtectionRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Http2RespResult():
    """
    Container for response information.

    :attr str id: ID.
    :attr str value: Value.
    :attr bool editable: Editable.
    :attr datetime modified_on: Modified date.
    """

    def __init__(self,
                 id: str,
                 value: str,
                 editable: bool,
                 modified_on: datetime) -> None:
        """
        Initialize a Http2RespResult object.

        :param str id: ID.
        :param str value: Value.
        :param bool editable: Editable.
        :param datetime modified_on: Modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Http2RespResult':
        """Initialize a Http2RespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in Http2RespResult JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in Http2RespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in Http2RespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in Http2RespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Http2RespResult object from a json dictionary."""
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
        """Return a `str` version of this Http2RespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Http2RespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Http2RespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Http3RespResult():
    """
    Container for response information.

    :attr str id: ID.
    :attr str value: Value.
    :attr bool editable: Editable.
    :attr datetime modified_on: Modified date.
    """

    def __init__(self,
                 id: str,
                 value: str,
                 editable: bool,
                 modified_on: datetime) -> None:
        """
        Initialize a Http3RespResult object.

        :param str id: ID.
        :param str value: Value.
        :param bool editable: Editable.
        :param datetime modified_on: Modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Http3RespResult':
        """Initialize a Http3RespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in Http3RespResult JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in Http3RespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in Http3RespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in Http3RespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Http3RespResult object from a json dictionary."""
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
        """Return a `str` version of this Http3RespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Http3RespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Http3RespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ImageLoadOptimizationRespResult():
    """
    Container for response information.

    :attr str id: ID.
    :attr str value: Value.
    :attr bool editable: Editable.
    :attr datetime modified_on: Modified date.
    """

    def __init__(self,
                 id: str,
                 value: str,
                 editable: bool,
                 modified_on: datetime) -> None:
        """
        Initialize a ImageLoadOptimizationRespResult object.

        :param str id: ID.
        :param str value: Value.
        :param bool editable: Editable.
        :param datetime modified_on: Modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ImageLoadOptimizationRespResult':
        """Initialize a ImageLoadOptimizationRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ImageLoadOptimizationRespResult JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in ImageLoadOptimizationRespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in ImageLoadOptimizationRespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in ImageLoadOptimizationRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ImageLoadOptimizationRespResult object from a json dictionary."""
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
        """Return a `str` version of this ImageLoadOptimizationRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ImageLoadOptimizationRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ImageLoadOptimizationRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ImageSizeOptimizationRespResult():
    """
    Container for response information.

    :attr str id: ID.
    :attr str value: Value.
    :attr bool editable: Editable.
    :attr datetime modified_on: Modified date.
    """

    def __init__(self,
                 id: str,
                 value: str,
                 editable: bool,
                 modified_on: datetime) -> None:
        """
        Initialize a ImageSizeOptimizationRespResult object.

        :param str id: ID.
        :param str value: Value.
        :param bool editable: Editable.
        :param datetime modified_on: Modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ImageSizeOptimizationRespResult':
        """Initialize a ImageSizeOptimizationRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ImageSizeOptimizationRespResult JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in ImageSizeOptimizationRespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in ImageSizeOptimizationRespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in ImageSizeOptimizationRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ImageSizeOptimizationRespResult object from a json dictionary."""
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
        """Return a `str` version of this ImageSizeOptimizationRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ImageSizeOptimizationRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ImageSizeOptimizationRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class IpGeolocationRespResult():
    """
    Container for response information.

    :attr str id: ID.
    :attr str value: Value.
    :attr bool editable: Editable.
    :attr datetime modified_on: Modified date.
    """

    def __init__(self,
                 id: str,
                 value: str,
                 editable: bool,
                 modified_on: datetime) -> None:
        """
        Initialize a IpGeolocationRespResult object.

        :param str id: ID.
        :param str value: Value.
        :param bool editable: Editable.
        :param datetime modified_on: Modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'IpGeolocationRespResult':
        """Initialize a IpGeolocationRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in IpGeolocationRespResult JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in IpGeolocationRespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in IpGeolocationRespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in IpGeolocationRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IpGeolocationRespResult object from a json dictionary."""
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
        """Return a `str` version of this IpGeolocationRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'IpGeolocationRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'IpGeolocationRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Ipv6RespResult():
    """
    Container for response information.

    :attr str id: ID.
    :attr str value: Value.
    :attr bool editable: Editable.
    :attr datetime modified_on: Modified date.
    """

    def __init__(self,
                 id: str,
                 value: str,
                 editable: bool,
                 modified_on: datetime) -> None:
        """
        Initialize a Ipv6RespResult object.

        :param str id: ID.
        :param str value: Value.
        :param bool editable: Editable.
        :param datetime modified_on: Modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Ipv6RespResult':
        """Initialize a Ipv6RespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in Ipv6RespResult JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in Ipv6RespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in Ipv6RespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in Ipv6RespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Ipv6RespResult object from a json dictionary."""
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
        """Return a `str` version of this Ipv6RespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Ipv6RespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Ipv6RespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class MaxUploadRespResult():
    """
    Container for response information.

    :attr str id: ID.
    :attr int value: Value.
    :attr bool editable: Editable.
    :attr datetime modified_on: Modified date.
    """

    def __init__(self,
                 id: str,
                 value: int,
                 editable: bool,
                 modified_on: datetime) -> None:
        """
        Initialize a MaxUploadRespResult object.

        :param str id: ID.
        :param int value: Value.
        :param bool editable: Editable.
        :param datetime modified_on: Modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MaxUploadRespResult':
        """Initialize a MaxUploadRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in MaxUploadRespResult JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in MaxUploadRespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in MaxUploadRespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in MaxUploadRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MaxUploadRespResult object from a json dictionary."""
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
        """Return a `str` version of this MaxUploadRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MaxUploadRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MaxUploadRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class MinTlsVersionRespResult():
    """
    Container for response information.

    :attr str id: ID.
    :attr str value: Value.
    :attr bool editable: Editable.
    :attr datetime modified_on: Modified date.
    """

    def __init__(self,
                 id: str,
                 value: str,
                 editable: bool,
                 modified_on: datetime) -> None:
        """
        Initialize a MinTlsVersionRespResult object.

        :param str id: ID.
        :param str value: Value.
        :param bool editable: Editable.
        :param datetime modified_on: Modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MinTlsVersionRespResult':
        """Initialize a MinTlsVersionRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in MinTlsVersionRespResult JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in MinTlsVersionRespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in MinTlsVersionRespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in MinTlsVersionRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MinTlsVersionRespResult object from a json dictionary."""
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
        """Return a `str` version of this MinTlsVersionRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MinTlsVersionRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MinTlsVersionRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class MinifyRespResult():
    """
    Container for response information.

    :attr str id: ID.
    :attr MinifyRespResultValue value: Value.
    :attr bool editable: Editable.
    :attr datetime modified_on: Modified date.
    """

    def __init__(self,
                 id: str,
                 value: 'MinifyRespResultValue',
                 editable: bool,
                 modified_on: datetime) -> None:
        """
        Initialize a MinifyRespResult object.

        :param str id: ID.
        :param MinifyRespResultValue value: Value.
        :param bool editable: Editable.
        :param datetime modified_on: Modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MinifyRespResult':
        """Initialize a MinifyRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in MinifyRespResult JSON')
        if 'value' in _dict:
            args['value'] = MinifyRespResultValue.from_dict(_dict.get('value'))
        else:
            raise ValueError('Required property \'value\' not present in MinifyRespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in MinifyRespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in MinifyRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MinifyRespResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value.to_dict()
        if hasattr(self, 'editable') and self.editable is not None:
            _dict['editable'] = self.editable
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = datetime_to_string(self.modified_on)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MinifyRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MinifyRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MinifyRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class MinifyRespResultValue():
    """
    Value.

    :attr str css: css.
    :attr str html: html.
    :attr str js: js.
    """

    def __init__(self,
                 css: str,
                 html: str,
                 js: str) -> None:
        """
        Initialize a MinifyRespResultValue object.

        :param str css: css.
        :param str html: html.
        :param str js: js.
        """
        self.css = css
        self.html = html
        self.js = js

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MinifyRespResultValue':
        """Initialize a MinifyRespResultValue object from a json dictionary."""
        args = {}
        if 'css' in _dict:
            args['css'] = _dict.get('css')
        else:
            raise ValueError('Required property \'css\' not present in MinifyRespResultValue JSON')
        if 'html' in _dict:
            args['html'] = _dict.get('html')
        else:
            raise ValueError('Required property \'html\' not present in MinifyRespResultValue JSON')
        if 'js' in _dict:
            args['js'] = _dict.get('js')
        else:
            raise ValueError('Required property \'js\' not present in MinifyRespResultValue JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MinifyRespResultValue object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'css') and self.css is not None:
            _dict['css'] = self.css
        if hasattr(self, 'html') and self.html is not None:
            _dict['html'] = self.html
        if hasattr(self, 'js') and self.js is not None:
            _dict['js'] = self.js
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MinifyRespResultValue object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MinifyRespResultValue') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MinifyRespResultValue') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class MinifySettingValue():
    """
    Value.

    :attr str css: Automatically minify all CSS for your website.
    :attr str html: Automatically minify all HTML for your website.
    :attr str js: Automatically minify all JavaScript for your website.
    """

    def __init__(self,
                 css: str,
                 html: str,
                 js: str) -> None:
        """
        Initialize a MinifySettingValue object.

        :param str css: Automatically minify all CSS for your website.
        :param str html: Automatically minify all HTML for your website.
        :param str js: Automatically minify all JavaScript for your website.
        """
        self.css = css
        self.html = html
        self.js = js

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MinifySettingValue':
        """Initialize a MinifySettingValue object from a json dictionary."""
        args = {}
        if 'css' in _dict:
            args['css'] = _dict.get('css')
        else:
            raise ValueError('Required property \'css\' not present in MinifySettingValue JSON')
        if 'html' in _dict:
            args['html'] = _dict.get('html')
        else:
            raise ValueError('Required property \'html\' not present in MinifySettingValue JSON')
        if 'js' in _dict:
            args['js'] = _dict.get('js')
        else:
            raise ValueError('Required property \'js\' not present in MinifySettingValue JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MinifySettingValue object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'css') and self.css is not None:
            _dict['css'] = self.css
        if hasattr(self, 'html') and self.html is not None:
            _dict['html'] = self.html
        if hasattr(self, 'js') and self.js is not None:
            _dict['js'] = self.js
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MinifySettingValue object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MinifySettingValue') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MinifySettingValue') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class CssEnum(str, Enum):
        """
        Automatically minify all CSS for your website.
        """
        ON = 'on'
        OFF = 'off'


    class HtmlEnum(str, Enum):
        """
        Automatically minify all HTML for your website.
        """
        ON = 'on'
        OFF = 'off'


    class JsEnum(str, Enum):
        """
        Automatically minify all JavaScript for your website.
        """
        ON = 'on'
        OFF = 'off'


class MobileRedirecSettingValue():
    """
    Value.

    :attr str status: Whether or not the mobile redirection is enabled.
    :attr str mobile_subdomain: Which subdomain prefix you wish to redirect visitors
          on mobile devices to.
    :attr bool strip_uri: Whether to drop the current page path and redirect to the
          mobile subdomain URL root or to keep the path and redirect to the same page on
          the mobile subdomain.
    """

    def __init__(self,
                 status: str,
                 mobile_subdomain: str,
                 strip_uri: bool) -> None:
        """
        Initialize a MobileRedirecSettingValue object.

        :param str status: Whether or not the mobile redirection is enabled.
        :param str mobile_subdomain: Which subdomain prefix you wish to redirect
               visitors on mobile devices to.
        :param bool strip_uri: Whether to drop the current page path and redirect
               to the mobile subdomain URL root or to keep the path and redirect to the
               same page on the mobile subdomain.
        """
        self.status = status
        self.mobile_subdomain = mobile_subdomain
        self.strip_uri = strip_uri

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MobileRedirecSettingValue':
        """Initialize a MobileRedirecSettingValue object from a json dictionary."""
        args = {}
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError('Required property \'status\' not present in MobileRedirecSettingValue JSON')
        if 'mobile_subdomain' in _dict:
            args['mobile_subdomain'] = _dict.get('mobile_subdomain')
        else:
            raise ValueError('Required property \'mobile_subdomain\' not present in MobileRedirecSettingValue JSON')
        if 'strip_uri' in _dict:
            args['strip_uri'] = _dict.get('strip_uri')
        else:
            raise ValueError('Required property \'strip_uri\' not present in MobileRedirecSettingValue JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MobileRedirecSettingValue object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'mobile_subdomain') and self.mobile_subdomain is not None:
            _dict['mobile_subdomain'] = self.mobile_subdomain
        if hasattr(self, 'strip_uri') and self.strip_uri is not None:
            _dict['strip_uri'] = self.strip_uri
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MobileRedirecSettingValue object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MobileRedirecSettingValue') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MobileRedirecSettingValue') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        Whether or not the mobile redirection is enabled.
        """
        ON = 'on'
        OFF = 'off'


class MobileRedirectRespResult():
    """
    Container for response information.

    :attr str id: ID.
    :attr MobileRedirectRespResultValue value: Value.
    :attr bool editable: Editable.
    :attr datetime modified_on: Modified date.
    """

    def __init__(self,
                 id: str,
                 value: 'MobileRedirectRespResultValue',
                 editable: bool,
                 modified_on: datetime) -> None:
        """
        Initialize a MobileRedirectRespResult object.

        :param str id: ID.
        :param MobileRedirectRespResultValue value: Value.
        :param bool editable: Editable.
        :param datetime modified_on: Modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MobileRedirectRespResult':
        """Initialize a MobileRedirectRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in MobileRedirectRespResult JSON')
        if 'value' in _dict:
            args['value'] = MobileRedirectRespResultValue.from_dict(_dict.get('value'))
        else:
            raise ValueError('Required property \'value\' not present in MobileRedirectRespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in MobileRedirectRespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in MobileRedirectRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MobileRedirectRespResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value.to_dict()
        if hasattr(self, 'editable') and self.editable is not None:
            _dict['editable'] = self.editable
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = datetime_to_string(self.modified_on)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MobileRedirectRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MobileRedirectRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MobileRedirectRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class MobileRedirectRespResultValue():
    """
    Value.

    :attr str status: Whether or not the mobile redirection is enabled.
    :attr str mobile_subdomain: Which subdomain prefix you wish to redirect visitors
          on mobile devices to.
    :attr bool strip_uri: Whether to drop the current page path and redirect to the
          mobile subdomain URL root or to keep the path and redirect to the same page on
          the mobile subdomain.
    """

    def __init__(self,
                 status: str,
                 mobile_subdomain: str,
                 strip_uri: bool) -> None:
        """
        Initialize a MobileRedirectRespResultValue object.

        :param str status: Whether or not the mobile redirection is enabled.
        :param str mobile_subdomain: Which subdomain prefix you wish to redirect
               visitors on mobile devices to.
        :param bool strip_uri: Whether to drop the current page path and redirect
               to the mobile subdomain URL root or to keep the path and redirect to the
               same page on the mobile subdomain.
        """
        self.status = status
        self.mobile_subdomain = mobile_subdomain
        self.strip_uri = strip_uri

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MobileRedirectRespResultValue':
        """Initialize a MobileRedirectRespResultValue object from a json dictionary."""
        args = {}
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError('Required property \'status\' not present in MobileRedirectRespResultValue JSON')
        if 'mobile_subdomain' in _dict:
            args['mobile_subdomain'] = _dict.get('mobile_subdomain')
        else:
            raise ValueError('Required property \'mobile_subdomain\' not present in MobileRedirectRespResultValue JSON')
        if 'strip_uri' in _dict:
            args['strip_uri'] = _dict.get('strip_uri')
        else:
            raise ValueError('Required property \'strip_uri\' not present in MobileRedirectRespResultValue JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MobileRedirectRespResultValue object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'mobile_subdomain') and self.mobile_subdomain is not None:
            _dict['mobile_subdomain'] = self.mobile_subdomain
        if hasattr(self, 'strip_uri') and self.strip_uri is not None:
            _dict['strip_uri'] = self.strip_uri
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MobileRedirectRespResultValue object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MobileRedirectRespResultValue') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MobileRedirectRespResultValue') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class OpportunisticEncryptionRespResult():
    """
    Container for response information.

    :attr str id: ID.
    :attr str value: Value.
    :attr bool editable: Editable.
    :attr datetime modified_on: Modified date.
    """

    def __init__(self,
                 id: str,
                 value: str,
                 editable: bool,
                 modified_on: datetime) -> None:
        """
        Initialize a OpportunisticEncryptionRespResult object.

        :param str id: ID.
        :param str value: Value.
        :param bool editable: Editable.
        :param datetime modified_on: Modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'OpportunisticEncryptionRespResult':
        """Initialize a OpportunisticEncryptionRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in OpportunisticEncryptionRespResult JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in OpportunisticEncryptionRespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in OpportunisticEncryptionRespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in OpportunisticEncryptionRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a OpportunisticEncryptionRespResult object from a json dictionary."""
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
        """Return a `str` version of this OpportunisticEncryptionRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'OpportunisticEncryptionRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'OpportunisticEncryptionRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class OriginErrorPagePassThruRespResult():
    """
    Container for response information.

    :attr str id: ID.
    :attr str value: Value.
    :attr bool editable: Editable.
    :attr datetime modified_on: Modified date.
    """

    def __init__(self,
                 id: str,
                 value: str,
                 editable: bool,
                 modified_on: datetime) -> None:
        """
        Initialize a OriginErrorPagePassThruRespResult object.

        :param str id: ID.
        :param str value: Value.
        :param bool editable: Editable.
        :param datetime modified_on: Modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'OriginErrorPagePassThruRespResult':
        """Initialize a OriginErrorPagePassThruRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in OriginErrorPagePassThruRespResult JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in OriginErrorPagePassThruRespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in OriginErrorPagePassThruRespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in OriginErrorPagePassThruRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a OriginErrorPagePassThruRespResult object from a json dictionary."""
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
        """Return a `str` version of this OriginErrorPagePassThruRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'OriginErrorPagePassThruRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'OriginErrorPagePassThruRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PrefetchPreloadRespResult():
    """
    Container for response information.

    :attr str id: ID.
    :attr str value: Value.
    :attr bool editable: Editable.
    :attr datetime modified_on: Modified date.
    """

    def __init__(self,
                 id: str,
                 value: str,
                 editable: bool,
                 modified_on: datetime) -> None:
        """
        Initialize a PrefetchPreloadRespResult object.

        :param str id: ID.
        :param str value: Value.
        :param bool editable: Editable.
        :param datetime modified_on: Modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PrefetchPreloadRespResult':
        """Initialize a PrefetchPreloadRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in PrefetchPreloadRespResult JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in PrefetchPreloadRespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in PrefetchPreloadRespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in PrefetchPreloadRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PrefetchPreloadRespResult object from a json dictionary."""
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
        """Return a `str` version of this PrefetchPreloadRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PrefetchPreloadRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PrefetchPreloadRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PseudoIpv4RespResult():
    """
    Container for response information.

    :attr str id: ID.
    :attr str value: Value.
    :attr bool editable: Editable.
    :attr datetime modified_on: Modified date.
    """

    def __init__(self,
                 id: str,
                 value: str,
                 editable: bool,
                 modified_on: datetime) -> None:
        """
        Initialize a PseudoIpv4RespResult object.

        :param str id: ID.
        :param str value: Value.
        :param bool editable: Editable.
        :param datetime modified_on: Modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PseudoIpv4RespResult':
        """Initialize a PseudoIpv4RespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in PseudoIpv4RespResult JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in PseudoIpv4RespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in PseudoIpv4RespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in PseudoIpv4RespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PseudoIpv4RespResult object from a json dictionary."""
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
        """Return a `str` version of this PseudoIpv4RespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PseudoIpv4RespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PseudoIpv4RespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResponseBufferingRespResult():
    """
    Container for response information.

    :attr str id: ID.
    :attr str value: Value.
    :attr bool editable: Editable.
    :attr datetime modified_on: Modified date.
    """

    def __init__(self,
                 id: str,
                 value: str,
                 editable: bool,
                 modified_on: datetime) -> None:
        """
        Initialize a ResponseBufferingRespResult object.

        :param str id: ID.
        :param str value: Value.
        :param bool editable: Editable.
        :param datetime modified_on: Modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResponseBufferingRespResult':
        """Initialize a ResponseBufferingRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ResponseBufferingRespResult JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in ResponseBufferingRespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in ResponseBufferingRespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in ResponseBufferingRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResponseBufferingRespResult object from a json dictionary."""
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
        """Return a `str` version of this ResponseBufferingRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResponseBufferingRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResponseBufferingRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ScriptLoadOptimizationRespResult():
    """
    Container for response information.

    :attr str id: ID.
    :attr str value: Value.
    :attr bool editable: Editable.
    :attr datetime modified_on: Modified date.
    """

    def __init__(self,
                 id: str,
                 value: str,
                 editable: bool,
                 modified_on: datetime) -> None:
        """
        Initialize a ScriptLoadOptimizationRespResult object.

        :param str id: ID.
        :param str value: Value.
        :param bool editable: Editable.
        :param datetime modified_on: Modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ScriptLoadOptimizationRespResult':
        """Initialize a ScriptLoadOptimizationRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ScriptLoadOptimizationRespResult JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in ScriptLoadOptimizationRespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in ScriptLoadOptimizationRespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in ScriptLoadOptimizationRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ScriptLoadOptimizationRespResult object from a json dictionary."""
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
        """Return a `str` version of this ScriptLoadOptimizationRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ScriptLoadOptimizationRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ScriptLoadOptimizationRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SecurityHeaderRespResult():
    """
    Container for response information.

    :attr str id: ID.
    :attr SecurityHeaderRespResultValue value: Value.
    :attr bool editable: Editable.
    :attr datetime modified_on: Modified date.
    """

    def __init__(self,
                 id: str,
                 value: 'SecurityHeaderRespResultValue',
                 editable: bool,
                 modified_on: datetime) -> None:
        """
        Initialize a SecurityHeaderRespResult object.

        :param str id: ID.
        :param SecurityHeaderRespResultValue value: Value.
        :param bool editable: Editable.
        :param datetime modified_on: Modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SecurityHeaderRespResult':
        """Initialize a SecurityHeaderRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in SecurityHeaderRespResult JSON')
        if 'value' in _dict:
            args['value'] = SecurityHeaderRespResultValue.from_dict(_dict.get('value'))
        else:
            raise ValueError('Required property \'value\' not present in SecurityHeaderRespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in SecurityHeaderRespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in SecurityHeaderRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SecurityHeaderRespResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value.to_dict()
        if hasattr(self, 'editable') and self.editable is not None:
            _dict['editable'] = self.editable
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = datetime_to_string(self.modified_on)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SecurityHeaderRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SecurityHeaderRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SecurityHeaderRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SecurityHeaderRespResultValue():
    """
    Value.

    :attr SecurityHeaderRespResultValueStrictTransportSecurity
          strict_transport_security: Strict transport security.
    """

    def __init__(self,
                 strict_transport_security: 'SecurityHeaderRespResultValueStrictTransportSecurity') -> None:
        """
        Initialize a SecurityHeaderRespResultValue object.

        :param SecurityHeaderRespResultValueStrictTransportSecurity
               strict_transport_security: Strict transport security.
        """
        self.strict_transport_security = strict_transport_security

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SecurityHeaderRespResultValue':
        """Initialize a SecurityHeaderRespResultValue object from a json dictionary."""
        args = {}
        if 'strict_transport_security' in _dict:
            args['strict_transport_security'] = SecurityHeaderRespResultValueStrictTransportSecurity.from_dict(_dict.get('strict_transport_security'))
        else:
            raise ValueError('Required property \'strict_transport_security\' not present in SecurityHeaderRespResultValue JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SecurityHeaderRespResultValue object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'strict_transport_security') and self.strict_transport_security is not None:
            _dict['strict_transport_security'] = self.strict_transport_security.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SecurityHeaderRespResultValue object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SecurityHeaderRespResultValue') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SecurityHeaderRespResultValue') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SecurityHeaderRespResultValueStrictTransportSecurity():
    """
    Strict transport security.

    :attr bool enabled: Whether or not security header is enabled.
    :attr int max_age: Max age in seconds.
    :attr bool include_subdomains: Include all subdomains.
    :attr bool nosniff: Whether or not to include 'X-Content-Type-Options:nosniff'
          header.
    """

    def __init__(self,
                 enabled: bool,
                 max_age: int,
                 include_subdomains: bool,
                 nosniff: bool) -> None:
        """
        Initialize a SecurityHeaderRespResultValueStrictTransportSecurity object.

        :param bool enabled: Whether or not security header is enabled.
        :param int max_age: Max age in seconds.
        :param bool include_subdomains: Include all subdomains.
        :param bool nosniff: Whether or not to include
               'X-Content-Type-Options:nosniff' header.
        """
        self.enabled = enabled
        self.max_age = max_age
        self.include_subdomains = include_subdomains
        self.nosniff = nosniff

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SecurityHeaderRespResultValueStrictTransportSecurity':
        """Initialize a SecurityHeaderRespResultValueStrictTransportSecurity object from a json dictionary."""
        args = {}
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        else:
            raise ValueError('Required property \'enabled\' not present in SecurityHeaderRespResultValueStrictTransportSecurity JSON')
        if 'max_age' in _dict:
            args['max_age'] = _dict.get('max_age')
        else:
            raise ValueError('Required property \'max_age\' not present in SecurityHeaderRespResultValueStrictTransportSecurity JSON')
        if 'include_subdomains' in _dict:
            args['include_subdomains'] = _dict.get('include_subdomains')
        else:
            raise ValueError('Required property \'include_subdomains\' not present in SecurityHeaderRespResultValueStrictTransportSecurity JSON')
        if 'nosniff' in _dict:
            args['nosniff'] = _dict.get('nosniff')
        else:
            raise ValueError('Required property \'nosniff\' not present in SecurityHeaderRespResultValueStrictTransportSecurity JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SecurityHeaderRespResultValueStrictTransportSecurity object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'max_age') and self.max_age is not None:
            _dict['max_age'] = self.max_age
        if hasattr(self, 'include_subdomains') and self.include_subdomains is not None:
            _dict['include_subdomains'] = self.include_subdomains
        if hasattr(self, 'nosniff') and self.nosniff is not None:
            _dict['nosniff'] = self.nosniff
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SecurityHeaderRespResultValueStrictTransportSecurity object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SecurityHeaderRespResultValueStrictTransportSecurity') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SecurityHeaderRespResultValueStrictTransportSecurity') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SecurityHeaderSettingValue():
    """
    Value.

    :attr SecurityHeaderSettingValueStrictTransportSecurity
          strict_transport_security: Strict transport security.
    """

    def __init__(self,
                 strict_transport_security: 'SecurityHeaderSettingValueStrictTransportSecurity') -> None:
        """
        Initialize a SecurityHeaderSettingValue object.

        :param SecurityHeaderSettingValueStrictTransportSecurity
               strict_transport_security: Strict transport security.
        """
        self.strict_transport_security = strict_transport_security

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SecurityHeaderSettingValue':
        """Initialize a SecurityHeaderSettingValue object from a json dictionary."""
        args = {}
        if 'strict_transport_security' in _dict:
            args['strict_transport_security'] = SecurityHeaderSettingValueStrictTransportSecurity.from_dict(_dict.get('strict_transport_security'))
        else:
            raise ValueError('Required property \'strict_transport_security\' not present in SecurityHeaderSettingValue JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SecurityHeaderSettingValue object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'strict_transport_security') and self.strict_transport_security is not None:
            _dict['strict_transport_security'] = self.strict_transport_security.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SecurityHeaderSettingValue object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SecurityHeaderSettingValue') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SecurityHeaderSettingValue') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SecurityHeaderSettingValueStrictTransportSecurity():
    """
    Strict transport security.

    :attr bool enabled: Whether or not security header is enabled.
    :attr int max_age: Max age in seconds.
    :attr bool include_subdomains: Include all subdomains.
    :attr bool nosniff: Whether or not to include 'X-Content-Type-Options:nosniff'
          header.
    """

    def __init__(self,
                 enabled: bool,
                 max_age: int,
                 include_subdomains: bool,
                 nosniff: bool) -> None:
        """
        Initialize a SecurityHeaderSettingValueStrictTransportSecurity object.

        :param bool enabled: Whether or not security header is enabled.
        :param int max_age: Max age in seconds.
        :param bool include_subdomains: Include all subdomains.
        :param bool nosniff: Whether or not to include
               'X-Content-Type-Options:nosniff' header.
        """
        self.enabled = enabled
        self.max_age = max_age
        self.include_subdomains = include_subdomains
        self.nosniff = nosniff

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SecurityHeaderSettingValueStrictTransportSecurity':
        """Initialize a SecurityHeaderSettingValueStrictTransportSecurity object from a json dictionary."""
        args = {}
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        else:
            raise ValueError('Required property \'enabled\' not present in SecurityHeaderSettingValueStrictTransportSecurity JSON')
        if 'max_age' in _dict:
            args['max_age'] = _dict.get('max_age')
        else:
            raise ValueError('Required property \'max_age\' not present in SecurityHeaderSettingValueStrictTransportSecurity JSON')
        if 'include_subdomains' in _dict:
            args['include_subdomains'] = _dict.get('include_subdomains')
        else:
            raise ValueError('Required property \'include_subdomains\' not present in SecurityHeaderSettingValueStrictTransportSecurity JSON')
        if 'nosniff' in _dict:
            args['nosniff'] = _dict.get('nosniff')
        else:
            raise ValueError('Required property \'nosniff\' not present in SecurityHeaderSettingValueStrictTransportSecurity JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SecurityHeaderSettingValueStrictTransportSecurity object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'max_age') and self.max_age is not None:
            _dict['max_age'] = self.max_age
        if hasattr(self, 'include_subdomains') and self.include_subdomains is not None:
            _dict['include_subdomains'] = self.include_subdomains
        if hasattr(self, 'nosniff') and self.nosniff is not None:
            _dict['nosniff'] = self.nosniff
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SecurityHeaderSettingValueStrictTransportSecurity object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SecurityHeaderSettingValueStrictTransportSecurity') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SecurityHeaderSettingValueStrictTransportSecurity') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ServerSideExcludeRespResult():
    """
    Container for response information.

    :attr str id: ID.
    :attr str value: Value.
    :attr bool editable: Editable.
    :attr datetime modified_on: Modified date.
    """

    def __init__(self,
                 id: str,
                 value: str,
                 editable: bool,
                 modified_on: datetime) -> None:
        """
        Initialize a ServerSideExcludeRespResult object.

        :param str id: ID.
        :param str value: Value.
        :param bool editable: Editable.
        :param datetime modified_on: Modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ServerSideExcludeRespResult':
        """Initialize a ServerSideExcludeRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in ServerSideExcludeRespResult JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in ServerSideExcludeRespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in ServerSideExcludeRespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in ServerSideExcludeRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ServerSideExcludeRespResult object from a json dictionary."""
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
        """Return a `str` version of this ServerSideExcludeRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ServerSideExcludeRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ServerSideExcludeRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class TlsClientAuthRespResult():
    """
    Container for response information.

    :attr str id: ID.
    :attr str value: Value.
    :attr bool editable: Editable.
    :attr datetime modified_on: Modified date.
    """

    def __init__(self,
                 id: str,
                 value: str,
                 editable: bool,
                 modified_on: datetime) -> None:
        """
        Initialize a TlsClientAuthRespResult object.

        :param str id: ID.
        :param str value: Value.
        :param bool editable: Editable.
        :param datetime modified_on: Modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TlsClientAuthRespResult':
        """Initialize a TlsClientAuthRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in TlsClientAuthRespResult JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in TlsClientAuthRespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in TlsClientAuthRespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in TlsClientAuthRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TlsClientAuthRespResult object from a json dictionary."""
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
        """Return a `str` version of this TlsClientAuthRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TlsClientAuthRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TlsClientAuthRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class TrueClientIpRespResult():
    """
    Container for response information.

    :attr str id: ID.
    :attr str value: Value.
    :attr bool editable: Editable.
    :attr datetime modified_on: Modified date.
    """

    def __init__(self,
                 id: str,
                 value: str,
                 editable: bool,
                 modified_on: datetime) -> None:
        """
        Initialize a TrueClientIpRespResult object.

        :param str id: ID.
        :param str value: Value.
        :param bool editable: Editable.
        :param datetime modified_on: Modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TrueClientIpRespResult':
        """Initialize a TrueClientIpRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in TrueClientIpRespResult JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in TrueClientIpRespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in TrueClientIpRespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in TrueClientIpRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TrueClientIpRespResult object from a json dictionary."""
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
        """Return a `str` version of this TrueClientIpRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TrueClientIpRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TrueClientIpRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class WafRespResult():
    """
    Container for response information.

    :attr str id: ID.
    :attr str value: Value.
    :attr bool editable: Editable.
    :attr datetime modified_on: Modified date.
    """

    def __init__(self,
                 id: str,
                 value: str,
                 editable: bool,
                 modified_on: datetime) -> None:
        """
        Initialize a WafRespResult object.

        :param str id: ID.
        :param str value: Value.
        :param bool editable: Editable.
        :param datetime modified_on: Modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WafRespResult':
        """Initialize a WafRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in WafRespResult JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in WafRespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in WafRespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in WafRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WafRespResult object from a json dictionary."""
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
        """Return a `str` version of this WafRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WafRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WafRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class WebsocketsRespResult():
    """
    Container for response information.

    :attr str id: ID.
    :attr str value: Value.
    :attr bool editable: Editable.
    :attr datetime modified_on: Modified date.
    """

    def __init__(self,
                 id: str,
                 value: str,
                 editable: bool,
                 modified_on: datetime) -> None:
        """
        Initialize a WebsocketsRespResult object.

        :param str id: ID.
        :param str value: Value.
        :param bool editable: Editable.
        :param datetime modified_on: Modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WebsocketsRespResult':
        """Initialize a WebsocketsRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in WebsocketsRespResult JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in WebsocketsRespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in WebsocketsRespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in WebsocketsRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WebsocketsRespResult object from a json dictionary."""
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
        """Return a `str` version of this WebsocketsRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WebsocketsRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WebsocketsRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ZonesDnssecRespResult():
    """
    Container for response information.

    :attr str status: (optional) Status.
    :attr int flags: (optional) Flags.
    :attr str algorithm: (optional) Algorithm.
    :attr str key_type: (optional) Key type.
    :attr str digest_type: (optional) Digest type.
    :attr str digest_algorithm: (optional) Digest algorithm.
    :attr str digest: (optional) Digest.
    :attr str ds: (optional) DS.
    :attr int key_tag: (optional) Key tag.
    :attr str public_key: (optional) Public key.
    """

    def __init__(self,
                 *,
                 status: str = None,
                 flags: int = None,
                 algorithm: str = None,
                 key_type: str = None,
                 digest_type: str = None,
                 digest_algorithm: str = None,
                 digest: str = None,
                 ds: str = None,
                 key_tag: int = None,
                 public_key: str = None) -> None:
        """
        Initialize a ZonesDnssecRespResult object.

        :param str status: (optional) Status.
        :param int flags: (optional) Flags.
        :param str algorithm: (optional) Algorithm.
        :param str key_type: (optional) Key type.
        :param str digest_type: (optional) Digest type.
        :param str digest_algorithm: (optional) Digest algorithm.
        :param str digest: (optional) Digest.
        :param str ds: (optional) DS.
        :param int key_tag: (optional) Key tag.
        :param str public_key: (optional) Public key.
        """
        self.status = status
        self.flags = flags
        self.algorithm = algorithm
        self.key_type = key_type
        self.digest_type = digest_type
        self.digest_algorithm = digest_algorithm
        self.digest = digest
        self.ds = ds
        self.key_tag = key_tag
        self.public_key = public_key

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ZonesDnssecRespResult':
        """Initialize a ZonesDnssecRespResult object from a json dictionary."""
        args = {}
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'flags' in _dict:
            args['flags'] = _dict.get('flags')
        if 'algorithm' in _dict:
            args['algorithm'] = _dict.get('algorithm')
        if 'key_type' in _dict:
            args['key_type'] = _dict.get('key_type')
        if 'digest_type' in _dict:
            args['digest_type'] = _dict.get('digest_type')
        if 'digest_algorithm' in _dict:
            args['digest_algorithm'] = _dict.get('digest_algorithm')
        if 'digest' in _dict:
            args['digest'] = _dict.get('digest')
        if 'ds' in _dict:
            args['ds'] = _dict.get('ds')
        if 'key_tag' in _dict:
            args['key_tag'] = _dict.get('key_tag')
        if 'public_key' in _dict:
            args['public_key'] = _dict.get('public_key')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ZonesDnssecRespResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'flags') and self.flags is not None:
            _dict['flags'] = self.flags
        if hasattr(self, 'algorithm') and self.algorithm is not None:
            _dict['algorithm'] = self.algorithm
        if hasattr(self, 'key_type') and self.key_type is not None:
            _dict['key_type'] = self.key_type
        if hasattr(self, 'digest_type') and self.digest_type is not None:
            _dict['digest_type'] = self.digest_type
        if hasattr(self, 'digest_algorithm') and self.digest_algorithm is not None:
            _dict['digest_algorithm'] = self.digest_algorithm
        if hasattr(self, 'digest') and self.digest is not None:
            _dict['digest'] = self.digest
        if hasattr(self, 'ds') and self.ds is not None:
            _dict['ds'] = self.ds
        if hasattr(self, 'key_tag') and self.key_tag is not None:
            _dict['key_tag'] = self.key_tag
        if hasattr(self, 'public_key') and self.public_key is not None:
            _dict['public_key'] = self.public_key
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ZonesDnssecRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ZonesDnssecRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ZonesDnssecRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        Status.
        """
        ACTIVE = 'active'
        DISABLED = 'disabled'
        PENDING = 'pending'
        PENDING_DISABLED = 'pending-disabled'
        ERROR = 'error'


class AlwaysUseHttpsResp():
    """
    Always use http response.

    :attr AlwaysUseHttpsRespResult result: Container for response information.
    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    """

    def __init__(self,
                 result: 'AlwaysUseHttpsRespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]]) -> None:
        """
        Initialize a AlwaysUseHttpsResp object.

        :param AlwaysUseHttpsRespResult result: Container for response information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AlwaysUseHttpsResp':
        """Initialize a AlwaysUseHttpsResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = AlwaysUseHttpsRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in AlwaysUseHttpsResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in AlwaysUseHttpsResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in AlwaysUseHttpsResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in AlwaysUseHttpsResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AlwaysUseHttpsResp object from a json dictionary."""
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
        """Return a `str` version of this AlwaysUseHttpsResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AlwaysUseHttpsResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AlwaysUseHttpsResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AutomaticHttpsRewritesResp():
    """
    automatic https rewrite response.

    :attr AutomaticHttpsRewritesRespResult result: Container for response
          information.
    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    """

    def __init__(self,
                 result: 'AutomaticHttpsRewritesRespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]]) -> None:
        """
        Initialize a AutomaticHttpsRewritesResp object.

        :param AutomaticHttpsRewritesRespResult result: Container for response
               information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AutomaticHttpsRewritesResp':
        """Initialize a AutomaticHttpsRewritesResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = AutomaticHttpsRewritesRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in AutomaticHttpsRewritesResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in AutomaticHttpsRewritesResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in AutomaticHttpsRewritesResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in AutomaticHttpsRewritesResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AutomaticHttpsRewritesResp object from a json dictionary."""
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
        """Return a `str` version of this AutomaticHttpsRewritesResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AutomaticHttpsRewritesResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AutomaticHttpsRewritesResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class BrowserCheckResp():
    """
    Browser Check response.

    :attr BrowserCheckRespResult result: Container for response information.
    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    """

    def __init__(self,
                 result: 'BrowserCheckRespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]]) -> None:
        """
        Initialize a BrowserCheckResp object.

        :param BrowserCheckRespResult result: Container for response information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BrowserCheckResp':
        """Initialize a BrowserCheckResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = BrowserCheckRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in BrowserCheckResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in BrowserCheckResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in BrowserCheckResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in BrowserCheckResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BrowserCheckResp object from a json dictionary."""
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
        """Return a `str` version of this BrowserCheckResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BrowserCheckResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BrowserCheckResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ChallengeTtlResp():
    """
    challenge TTL response.

    :attr ChallengeTtlRespResult result: Container for response information.
    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    """

    def __init__(self,
                 result: 'ChallengeTtlRespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]]) -> None:
        """
        Initialize a ChallengeTtlResp object.

        :param ChallengeTtlRespResult result: Container for response information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ChallengeTtlResp':
        """Initialize a ChallengeTtlResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = ChallengeTtlRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in ChallengeTtlResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in ChallengeTtlResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in ChallengeTtlResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in ChallengeTtlResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ChallengeTtlResp object from a json dictionary."""
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
        """Return a `str` version of this ChallengeTtlResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ChallengeTtlResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ChallengeTtlResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CiphersResp():
    """
    Ciphers response.

    :attr CiphersRespResult result: Container for response information.
    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    """

    def __init__(self,
                 result: 'CiphersRespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]]) -> None:
        """
        Initialize a CiphersResp object.

        :param CiphersRespResult result: Container for response information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CiphersResp':
        """Initialize a CiphersResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = CiphersRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in CiphersResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in CiphersResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in CiphersResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in CiphersResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CiphersResp object from a json dictionary."""
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
        """Return a `str` version of this CiphersResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CiphersResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CiphersResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CnameFlatteningResponse():
    """
    CNAME Flattening response.

    :attr str id: (optional) id.
    :attr str value: (optional) value.
    :attr datetime modified_on: (optional) Date when it is modified.
    :attr bool editable: (optional) editable.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 value: str = None,
                 modified_on: datetime = None,
                 editable: bool = None) -> None:
        """
        Initialize a CnameFlatteningResponse object.

        :param str id: (optional) id.
        :param str value: (optional) value.
        :param datetime modified_on: (optional) Date when it is modified.
        :param bool editable: (optional) editable.
        """
        self.id = id
        self.value = value
        self.modified_on = modified_on
        self.editable = editable

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CnameFlatteningResponse':
        """Initialize a CnameFlatteningResponse object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CnameFlatteningResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = datetime_to_string(self.modified_on)
        if hasattr(self, 'editable') and self.editable is not None:
            _dict['editable'] = self.editable
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CnameFlatteningResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CnameFlatteningResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CnameFlatteningResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ValueEnum(str, Enum):
        """
        value.
        """
        FLATTEN_ALL = 'flatten_all'
        FLATTEN_AT_ROOT = 'flatten_at_root'


class HotlinkProtectionResp():
    """
    Hotlink Protection response.

    :attr HotlinkProtectionRespResult result: Container for response information.
    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    """

    def __init__(self,
                 result: 'HotlinkProtectionRespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]]) -> None:
        """
        Initialize a HotlinkProtectionResp object.

        :param HotlinkProtectionRespResult result: Container for response
               information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HotlinkProtectionResp':
        """Initialize a HotlinkProtectionResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = HotlinkProtectionRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in HotlinkProtectionResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in HotlinkProtectionResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in HotlinkProtectionResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in HotlinkProtectionResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HotlinkProtectionResp object from a json dictionary."""
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
        """Return a `str` version of this HotlinkProtectionResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HotlinkProtectionResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HotlinkProtectionResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Http2Resp():
    """
    HTTP2 Response.

    :attr Http2RespResult result: Container for response information.
    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    """

    def __init__(self,
                 result: 'Http2RespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]]) -> None:
        """
        Initialize a Http2Resp object.

        :param Http2RespResult result: Container for response information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Http2Resp':
        """Initialize a Http2Resp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = Http2RespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in Http2Resp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in Http2Resp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in Http2Resp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in Http2Resp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Http2Resp object from a json dictionary."""
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
        """Return a `str` version of this Http2Resp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Http2Resp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Http2Resp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Http3Resp():
    """
    HTTP3 Response.

    :attr Http3RespResult result: Container for response information.
    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    """

    def __init__(self,
                 result: 'Http3RespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]]) -> None:
        """
        Initialize a Http3Resp object.

        :param Http3RespResult result: Container for response information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Http3Resp':
        """Initialize a Http3Resp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = Http3RespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in Http3Resp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in Http3Resp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in Http3Resp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in Http3Resp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Http3Resp object from a json dictionary."""
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
        """Return a `str` version of this Http3Resp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Http3Resp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Http3Resp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ImageLoadOptimizationResp():
    """
    Image Load Optimization response.

    :attr ImageLoadOptimizationRespResult result: Container for response
          information.
    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    """

    def __init__(self,
                 result: 'ImageLoadOptimizationRespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]]) -> None:
        """
        Initialize a ImageLoadOptimizationResp object.

        :param ImageLoadOptimizationRespResult result: Container for response
               information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ImageLoadOptimizationResp':
        """Initialize a ImageLoadOptimizationResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = ImageLoadOptimizationRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in ImageLoadOptimizationResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in ImageLoadOptimizationResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in ImageLoadOptimizationResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in ImageLoadOptimizationResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ImageLoadOptimizationResp object from a json dictionary."""
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
        """Return a `str` version of this ImageLoadOptimizationResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ImageLoadOptimizationResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ImageLoadOptimizationResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ImageSizeOptimizationResp():
    """
    Image size optimization response.

    :attr ImageSizeOptimizationRespResult result: Container for response
          information.
    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    """

    def __init__(self,
                 result: 'ImageSizeOptimizationRespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]]) -> None:
        """
        Initialize a ImageSizeOptimizationResp object.

        :param ImageSizeOptimizationRespResult result: Container for response
               information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ImageSizeOptimizationResp':
        """Initialize a ImageSizeOptimizationResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = ImageSizeOptimizationRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in ImageSizeOptimizationResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in ImageSizeOptimizationResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in ImageSizeOptimizationResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in ImageSizeOptimizationResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ImageSizeOptimizationResp object from a json dictionary."""
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
        """Return a `str` version of this ImageSizeOptimizationResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ImageSizeOptimizationResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ImageSizeOptimizationResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class IpGeolocationResp():
    """
    IP Geolocation response.

    :attr IpGeolocationRespResult result: Container for response information.
    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    """

    def __init__(self,
                 result: 'IpGeolocationRespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]]) -> None:
        """
        Initialize a IpGeolocationResp object.

        :param IpGeolocationRespResult result: Container for response information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'IpGeolocationResp':
        """Initialize a IpGeolocationResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = IpGeolocationRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in IpGeolocationResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in IpGeolocationResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in IpGeolocationResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in IpGeolocationResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IpGeolocationResp object from a json dictionary."""
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
        """Return a `str` version of this IpGeolocationResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'IpGeolocationResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'IpGeolocationResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Ipv6Resp():
    """
    IPv6 Response.

    :attr Ipv6RespResult result: Container for response information.
    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    """

    def __init__(self,
                 result: 'Ipv6RespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]]) -> None:
        """
        Initialize a Ipv6Resp object.

        :param Ipv6RespResult result: Container for response information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Ipv6Resp':
        """Initialize a Ipv6Resp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = Ipv6RespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in Ipv6Resp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in Ipv6Resp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in Ipv6Resp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in Ipv6Resp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Ipv6Resp object from a json dictionary."""
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
        """Return a `str` version of this Ipv6Resp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Ipv6Resp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Ipv6Resp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class MaxUploadResp():
    """
    Maximum upload response.

    :attr MaxUploadRespResult result: Container for response information.
    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    """

    def __init__(self,
                 result: 'MaxUploadRespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]]) -> None:
        """
        Initialize a MaxUploadResp object.

        :param MaxUploadRespResult result: Container for response information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MaxUploadResp':
        """Initialize a MaxUploadResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = MaxUploadRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in MaxUploadResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in MaxUploadResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in MaxUploadResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in MaxUploadResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MaxUploadResp object from a json dictionary."""
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
        """Return a `str` version of this MaxUploadResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MaxUploadResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MaxUploadResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class MinTlsVersionResp():
    """
    Minimum TLS Version response.

    :attr MinTlsVersionRespResult result: Container for response information.
    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    """

    def __init__(self,
                 result: 'MinTlsVersionRespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]]) -> None:
        """
        Initialize a MinTlsVersionResp object.

        :param MinTlsVersionRespResult result: Container for response information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MinTlsVersionResp':
        """Initialize a MinTlsVersionResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = MinTlsVersionRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in MinTlsVersionResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in MinTlsVersionResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in MinTlsVersionResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in MinTlsVersionResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MinTlsVersionResp object from a json dictionary."""
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
        """Return a `str` version of this MinTlsVersionResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MinTlsVersionResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MinTlsVersionResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class MinifyResp():
    """
    Minify response.

    :attr MinifyRespResult result: Container for response information.
    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    """

    def __init__(self,
                 result: 'MinifyRespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]]) -> None:
        """
        Initialize a MinifyResp object.

        :param MinifyRespResult result: Container for response information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MinifyResp':
        """Initialize a MinifyResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = MinifyRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in MinifyResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in MinifyResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in MinifyResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in MinifyResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MinifyResp object from a json dictionary."""
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
        """Return a `str` version of this MinifyResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MinifyResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MinifyResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class MobileRedirectResp():
    """
    Mobile Redirect Response.

    :attr MobileRedirectRespResult result: Container for response information.
    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    """

    def __init__(self,
                 result: 'MobileRedirectRespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]]) -> None:
        """
        Initialize a MobileRedirectResp object.

        :param MobileRedirectRespResult result: Container for response information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MobileRedirectResp':
        """Initialize a MobileRedirectResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = MobileRedirectRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in MobileRedirectResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in MobileRedirectResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in MobileRedirectResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in MobileRedirectResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MobileRedirectResp object from a json dictionary."""
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
        """Return a `str` version of this MobileRedirectResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MobileRedirectResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MobileRedirectResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class OpportunisticEncryptionResp():
    """
    Oppertunistic encryption response.

    :attr OpportunisticEncryptionRespResult result: Container for response
          information.
    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    """

    def __init__(self,
                 result: 'OpportunisticEncryptionRespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]]) -> None:
        """
        Initialize a OpportunisticEncryptionResp object.

        :param OpportunisticEncryptionRespResult result: Container for response
               information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'OpportunisticEncryptionResp':
        """Initialize a OpportunisticEncryptionResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = OpportunisticEncryptionRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in OpportunisticEncryptionResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in OpportunisticEncryptionResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in OpportunisticEncryptionResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in OpportunisticEncryptionResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a OpportunisticEncryptionResp object from a json dictionary."""
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
        """Return a `str` version of this OpportunisticEncryptionResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'OpportunisticEncryptionResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'OpportunisticEncryptionResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class OriginErrorPagePassThruResp():
    """
    origin error page pass through response.

    :attr OriginErrorPagePassThruRespResult result: Container for response
          information.
    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    """

    def __init__(self,
                 result: 'OriginErrorPagePassThruRespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]]) -> None:
        """
        Initialize a OriginErrorPagePassThruResp object.

        :param OriginErrorPagePassThruRespResult result: Container for response
               information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'OriginErrorPagePassThruResp':
        """Initialize a OriginErrorPagePassThruResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = OriginErrorPagePassThruRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in OriginErrorPagePassThruResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in OriginErrorPagePassThruResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in OriginErrorPagePassThruResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in OriginErrorPagePassThruResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a OriginErrorPagePassThruResp object from a json dictionary."""
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
        """Return a `str` version of this OriginErrorPagePassThruResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'OriginErrorPagePassThruResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'OriginErrorPagePassThruResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PrefetchPreloadResp():
    """
    Prefetch & Preload Response.

    :attr PrefetchPreloadRespResult result: Container for response information.
    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    """

    def __init__(self,
                 result: 'PrefetchPreloadRespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]]) -> None:
        """
        Initialize a PrefetchPreloadResp object.

        :param PrefetchPreloadRespResult result: Container for response
               information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PrefetchPreloadResp':
        """Initialize a PrefetchPreloadResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = PrefetchPreloadRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in PrefetchPreloadResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in PrefetchPreloadResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in PrefetchPreloadResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in PrefetchPreloadResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PrefetchPreloadResp object from a json dictionary."""
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
        """Return a `str` version of this PrefetchPreloadResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PrefetchPreloadResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PrefetchPreloadResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PseudoIpv4Resp():
    """
    Pseudo ipv4 response.

    :attr PseudoIpv4RespResult result: Container for response information.
    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    """

    def __init__(self,
                 result: 'PseudoIpv4RespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]]) -> None:
        """
        Initialize a PseudoIpv4Resp object.

        :param PseudoIpv4RespResult result: Container for response information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PseudoIpv4Resp':
        """Initialize a PseudoIpv4Resp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = PseudoIpv4RespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in PseudoIpv4Resp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in PseudoIpv4Resp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in PseudoIpv4Resp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in PseudoIpv4Resp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PseudoIpv4Resp object from a json dictionary."""
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
        """Return a `str` version of this PseudoIpv4Resp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PseudoIpv4Resp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PseudoIpv4Resp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResponseBufferingResp():
    """
    Buffering response.

    :attr ResponseBufferingRespResult result: Container for response information.
    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    """

    def __init__(self,
                 result: 'ResponseBufferingRespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]]) -> None:
        """
        Initialize a ResponseBufferingResp object.

        :param ResponseBufferingRespResult result: Container for response
               information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResponseBufferingResp':
        """Initialize a ResponseBufferingResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = ResponseBufferingRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in ResponseBufferingResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in ResponseBufferingResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in ResponseBufferingResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in ResponseBufferingResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResponseBufferingResp object from a json dictionary."""
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
        """Return a `str` version of this ResponseBufferingResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResponseBufferingResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResponseBufferingResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ScriptLoadOptimizationResp():
    """
    Script load optimization response.

    :attr ScriptLoadOptimizationRespResult result: Container for response
          information.
    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    """

    def __init__(self,
                 result: 'ScriptLoadOptimizationRespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]]) -> None:
        """
        Initialize a ScriptLoadOptimizationResp object.

        :param ScriptLoadOptimizationRespResult result: Container for response
               information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ScriptLoadOptimizationResp':
        """Initialize a ScriptLoadOptimizationResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = ScriptLoadOptimizationRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in ScriptLoadOptimizationResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in ScriptLoadOptimizationResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in ScriptLoadOptimizationResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in ScriptLoadOptimizationResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ScriptLoadOptimizationResp object from a json dictionary."""
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
        """Return a `str` version of this ScriptLoadOptimizationResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ScriptLoadOptimizationResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ScriptLoadOptimizationResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SecurityHeaderResp():
    """
    Response of Security Header.

    :attr SecurityHeaderRespResult result: Container for response information.
    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    """

    def __init__(self,
                 result: 'SecurityHeaderRespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]]) -> None:
        """
        Initialize a SecurityHeaderResp object.

        :param SecurityHeaderRespResult result: Container for response information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SecurityHeaderResp':
        """Initialize a SecurityHeaderResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = SecurityHeaderRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in SecurityHeaderResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in SecurityHeaderResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in SecurityHeaderResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in SecurityHeaderResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SecurityHeaderResp object from a json dictionary."""
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
        """Return a `str` version of this SecurityHeaderResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SecurityHeaderResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SecurityHeaderResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ServerSideExcludeResp():
    """
    Response of server side exclude.

    :attr ServerSideExcludeRespResult result: Container for response information.
    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    """

    def __init__(self,
                 result: 'ServerSideExcludeRespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]]) -> None:
        """
        Initialize a ServerSideExcludeResp object.

        :param ServerSideExcludeRespResult result: Container for response
               information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ServerSideExcludeResp':
        """Initialize a ServerSideExcludeResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = ServerSideExcludeRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in ServerSideExcludeResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in ServerSideExcludeResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in ServerSideExcludeResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in ServerSideExcludeResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ServerSideExcludeResp object from a json dictionary."""
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
        """Return a `str` version of this ServerSideExcludeResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ServerSideExcludeResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ServerSideExcludeResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class TlsClientAuthResp():
    """
    TLS Client authentication response.

    :attr TlsClientAuthRespResult result: Container for response information.
    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    """

    def __init__(self,
                 result: 'TlsClientAuthRespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]]) -> None:
        """
        Initialize a TlsClientAuthResp object.

        :param TlsClientAuthRespResult result: Container for response information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TlsClientAuthResp':
        """Initialize a TlsClientAuthResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = TlsClientAuthRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in TlsClientAuthResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in TlsClientAuthResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in TlsClientAuthResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in TlsClientAuthResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TlsClientAuthResp object from a json dictionary."""
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
        """Return a `str` version of this TlsClientAuthResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TlsClientAuthResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TlsClientAuthResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class TrueClientIpResp():
    """
    true client IP response.

    :attr TrueClientIpRespResult result: Container for response information.
    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    """

    def __init__(self,
                 result: 'TrueClientIpRespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]]) -> None:
        """
        Initialize a TrueClientIpResp object.

        :param TrueClientIpRespResult result: Container for response information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TrueClientIpResp':
        """Initialize a TrueClientIpResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = TrueClientIpRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in TrueClientIpResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in TrueClientIpResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in TrueClientIpResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in TrueClientIpResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TrueClientIpResp object from a json dictionary."""
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
        """Return a `str` version of this TrueClientIpResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TrueClientIpResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TrueClientIpResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class WafResp():
    """
    WAF Response.

    :attr WafRespResult result: Container for response information.
    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    """

    def __init__(self,
                 result: 'WafRespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]]) -> None:
        """
        Initialize a WafResp object.

        :param WafRespResult result: Container for response information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WafResp':
        """Initialize a WafResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = WafRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in WafResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in WafResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in WafResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in WafResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WafResp object from a json dictionary."""
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
        """Return a `str` version of this WafResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WafResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WafResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class WebsocketsResp():
    """
    Websocket Response.

    :attr WebsocketsRespResult result: Container for response information.
    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    """

    def __init__(self,
                 result: 'WebsocketsRespResult',
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]]) -> None:
        """
        Initialize a WebsocketsResp object.

        :param WebsocketsRespResult result: Container for response information.
        :param bool success: Was the get successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.result = result
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WebsocketsResp':
        """Initialize a WebsocketsResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = WebsocketsRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in WebsocketsResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in WebsocketsResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in WebsocketsResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in WebsocketsResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WebsocketsResp object from a json dictionary."""
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
        """Return a `str` version of this WebsocketsResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WebsocketsResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WebsocketsResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ZonesCnameFlatteningResp():
    """
    Zones CNAME flattening response.

    :attr bool success: Was operation successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr CnameFlatteningResponse result: CNAME Flattening response.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'CnameFlatteningResponse') -> None:
        """
        Initialize a ZonesCnameFlatteningResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param CnameFlatteningResponse result: CNAME Flattening response.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ZonesCnameFlatteningResp':
        """Initialize a ZonesCnameFlatteningResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in ZonesCnameFlatteningResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in ZonesCnameFlatteningResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in ZonesCnameFlatteningResp JSON')
        if 'result' in _dict:
            args['result'] = CnameFlatteningResponse.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in ZonesCnameFlatteningResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ZonesCnameFlatteningResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = self.messages
        if hasattr(self, 'result') and self.result is not None:
            _dict['result'] = self.result.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ZonesCnameFlatteningResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ZonesCnameFlatteningResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ZonesCnameFlatteningResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ZonesDnssecResp():
    """
    Zones DNS Sec Response.

    :attr bool success: Was operation successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr ZonesDnssecRespResult result: Container for response information.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'ZonesDnssecRespResult') -> None:
        """
        Initialize a ZonesDnssecResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param ZonesDnssecRespResult result: Container for response information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ZonesDnssecResp':
        """Initialize a ZonesDnssecResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in ZonesDnssecResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in ZonesDnssecResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in ZonesDnssecResp JSON')
        if 'result' in _dict:
            args['result'] = ZonesDnssecRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in ZonesDnssecResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ZonesDnssecResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = self.messages
        if hasattr(self, 'result') and self.result is not None:
            _dict['result'] = self.result.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ZonesDnssecResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ZonesDnssecResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ZonesDnssecResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other