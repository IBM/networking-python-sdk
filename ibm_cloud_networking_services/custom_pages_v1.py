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
Custom Pages
"""

from datetime import datetime
from enum import Enum
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class CustomPagesV1(BaseService):
    """The Custom Pages V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'custom_pages'

    @classmethod
    def new_instance(cls,
                     crn: str,
                     zone_identifier: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'CustomPagesV1':
        """
        Return a new client for the Custom Pages service using the specified
               parameters and external configuration.

        :param str crn: Full crn of the service instance.

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
        Construct a new client for the Custom Pages service.

        :param str crn: Full crn of the service instance.

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
    # Custom Pages
    #########################


    def list_instance_custom_pages(self, **kwargs) -> DetailedResponse:
        """
        List all custom pages for a given instance.

        List all custom pages for a given instance.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListCustomPagesResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='list_instance_custom_pages')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/custom_pages'.format(*self.encode_path_vars(self.crn))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_instance_custom_page(self, page_identifier: str, **kwargs) -> DetailedResponse:
        """
        Get a custom page for a given instance.

        Get a specific custom page for a given instance.

        :param str page_identifier: Custom page identifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CustomPageSpecificResp` object
        """

        if page_identifier is None:
            raise ValueError('page_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_instance_custom_page')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/custom_pages/{1}'.format(*self.encode_path_vars(self.crn, page_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_instance_custom_page(self, page_identifier: str, *, url: str = None, state: str = None, **kwargs) -> DetailedResponse:
        """
        Update a custom page for a given instance.

        Update a specific custom page for a given instance.

        :param str page_identifier: Custom page identifier.
        :param str url: (optional) A URL that is associated with the Custom Page.
        :param str state: (optional) The Custom Page state.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CustomPageSpecificResp` object
        """

        if page_identifier is None:
            raise ValueError('page_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_instance_custom_page')
        headers.update(sdk_headers)

        data = {
            'url': url,
            'state': state
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/custom_pages/{1}'.format(*self.encode_path_vars(self.crn, page_identifier))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def list_zone_custom_pages(self, **kwargs) -> DetailedResponse:
        """
        List all custom pages for a given zone.

        List all custom pages for a given zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListCustomPagesResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='list_zone_custom_pages')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/custom_pages'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_zone_custom_page(self, page_identifier: str, **kwargs) -> DetailedResponse:
        """
        Get a custom page for a given zone.

        Get a specific custom page for a given zone.

        :param str page_identifier: Custom page identifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CustomPageSpecificResp` object
        """

        if page_identifier is None:
            raise ValueError('page_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_zone_custom_page')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/custom_pages/{2}'.format(*self.encode_path_vars(self.crn, self.zone_identifier, page_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_zone_custom_page(self, page_identifier: str, *, url: str = None, state: str = None, **kwargs) -> DetailedResponse:
        """
        Update a custom page for a given zone.

        Update a specific custom page for a given zone.

        :param str page_identifier: Custom page identifier.
        :param str url: (optional) A URL that is associated with the Custom Page.
        :param str state: (optional) The Custom Page state.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CustomPageSpecificResp` object
        """

        if page_identifier is None:
            raise ValueError('page_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_zone_custom_page')
        headers.update(sdk_headers)

        data = {
            'url': url,
            'state': state
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/custom_pages/{2}'.format(*self.encode_path_vars(self.crn, self.zone_identifier, page_identifier))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


class GetInstanceCustomPageEnums:
    """
    Enums for get_instance_custom_page parameters.
    """

    class PageIdentifier(Enum):
        """
        Custom page identifier.
        """
        BASIC_CHALLENGE = 'basic_challenge'
        WAF_CHALLENGE = 'waf_challenge'
        WAF_BLOCK = 'waf_block'
        RATELIMIT_BLOCK = 'ratelimit_block'
        COUNTRY_CHALLENGE = 'country_challenge'
        IP_BLOCK = 'ip_block'
        UNDER_ATTACK = 'under_attack'


class UpdateInstanceCustomPageEnums:
    """
    Enums for update_instance_custom_page parameters.
    """

    class PageIdentifier(Enum):
        """
        Custom page identifier.
        """
        BASIC_CHALLENGE = 'basic_challenge'
        WAF_CHALLENGE = 'waf_challenge'
        WAF_BLOCK = 'waf_block'
        RATELIMIT_BLOCK = 'ratelimit_block'
        COUNTRY_CHALLENGE = 'country_challenge'
        IP_BLOCK = 'ip_block'
        UNDER_ATTACK = 'under_attack'


class GetZoneCustomPageEnums:
    """
    Enums for get_zone_custom_page parameters.
    """

    class PageIdentifier(Enum):
        """
        Custom page identifier.
        """
        BASIC_CHALLENGE = 'basic_challenge'
        WAF_CHALLENGE = 'waf_challenge'
        WAF_BLOCK = 'waf_block'
        RATELIMIT_BLOCK = 'ratelimit_block'
        COUNTRY_CHALLENGE = 'country_challenge'
        IP_BLOCK = 'ip_block'
        UNDER_ATTACK = 'under_attack'


class UpdateZoneCustomPageEnums:
    """
    Enums for update_zone_custom_page parameters.
    """

    class PageIdentifier(Enum):
        """
        Custom page identifier.
        """
        BASIC_CHALLENGE = 'basic_challenge'
        WAF_CHALLENGE = 'waf_challenge'
        WAF_BLOCK = 'waf_block'
        RATELIMIT_BLOCK = 'ratelimit_block'
        COUNTRY_CHALLENGE = 'country_challenge'
        IP_BLOCK = 'ip_block'
        UNDER_ATTACK = 'under_attack'
