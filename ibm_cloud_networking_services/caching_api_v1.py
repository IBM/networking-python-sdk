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
This document describes CIS caching  API.
"""

from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class CachingApiV1(BaseService):
    """The Caching API V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'caching_api'

    @classmethod
    def new_instance(cls,
                     crn: str,
                     zone_id: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'CachingApiV1':
        """
        Return a new client for the Caching API service using the specified
               parameters and external configuration.

        :param str crn: cloud resource name.

        :param str zone_id: zone id.
        """
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_id is None:
            raise ValueError('zone_id must be provided')

        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            crn,
            zone_id,
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(self,
                 crn: str,
                 zone_id: str,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the Caching API service.

        :param str crn: cloud resource name.

        :param str zone_id: zone id.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_id is None:
            raise ValueError('zone_id must be provided')

        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)
        self.crn = crn
        self.zone_id = zone_id


    #########################
    # Cache Settings
    #########################


    def purge_all(self, **kwargs) -> DetailedResponse:
        """
        purge all files under a specific domain.

        All resources in CDN edge servers' cache should be removed. This may have dramatic
        affects on your origin server load after performing this action.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PurgeAllResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='purge_all')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/purge_cache/purge_all'.format(*self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def purge_by_urls(self, *, files: List[str] = None, **kwargs) -> DetailedResponse:
        """
        purge individual files by URLs.

        Granularly remove one or more files from CDN edge servers' cache either by
        specifying URLs.

        :param List[str] files: (optional) purge url array.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PurgeAllResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='purge_by_urls')
        headers.update(sdk_headers)

        data = {
            'files': files
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/purge_cache/purge_by_urls'.format(*self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def purge_by_cache_tags(self, *, tags: List[str] = None, **kwargs) -> DetailedResponse:
        """
        Purge files by Cache-Tags.

        Granularly remove one or more files from CDN edge servers' cache either by
        specifying the associated Cache-Tags.

        :param List[str] tags: (optional) array of tags.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PurgeAllResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='purge_by_cache_tags')
        headers.update(sdk_headers)

        data = {
            'tags': tags
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/purge_cache/purge_by_cache_tags'.format(*self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def purge_by_hosts(self, *, hosts: List[str] = None, **kwargs) -> DetailedResponse:
        """
        purge individual files by hostnames.

        Granularly remove one or more files from CDN edge servers' cache either by
        specifying the hostnames.

        :param List[str] hosts: (optional) hosts name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PurgeAllResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='purge_by_hosts')
        headers.update(sdk_headers)

        data = {
            'hosts': hosts
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/purge_cache/purge_by_hosts'.format(*self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_browser_cache_ttl(self, **kwargs) -> DetailedResponse:
        """
        Get browser cache TTL setting.

        Browser Cache TTL (in seconds) specifies how long CDN edge servers cached
        resources will remain on your visitors' computers.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BrowserTTLResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_browser_cache_ttl')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/browser_cache_ttl'.format(*self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_browser_cache_ttl(self, *, value: int = None, **kwargs) -> DetailedResponse:
        """
        Change browser cache TTL setting.

        Browser Cache TTL (in seconds) specifies how long CDN edge servers cached
        resources will remain on your visitors' computers.

        :param int value: (optional) ttl value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BrowserTTLResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_browser_cache_ttl')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/browser_cache_ttl'.format(*self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_development_mode(self, **kwargs) -> DetailedResponse:
        """
        Get development mode setting.

        Get development mode setting.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeveopmentModeResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_development_mode')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/development_mode'.format(*self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_development_mode(self, *, value: str = None, **kwargs) -> DetailedResponse:
        """
        Change development mode setting.

        Change development mode setting.

        :param str value: (optional) on/off value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeveopmentModeResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_development_mode')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/development_mode'.format(*self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_query_string_sort(self, **kwargs) -> DetailedResponse:
        """
        Get Enable Query String Sort setting.

        Get Enable Query String Sort setting.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `EnableQueryStringSortResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_query_string_sort')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/sort_query_string_for_cache'.format(*self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_query_string_sort(self, *, value: str = None, **kwargs) -> DetailedResponse:
        """
        Change Enable Query String Sort setting.

        Change Enable Query String Sort setting.

        :param str value: (optional) on/off property value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `EnableQueryStringSortResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_query_string_sort')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/sort_query_string_for_cache'.format(*self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # cacheLevel
    #########################


    def get_cache_level(self, **kwargs) -> DetailedResponse:
        """
        Get cache level setting of a specific zone.

        Get cache level setting of a specific zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CacheLevelResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_cache_level')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/cache_level'.format(*self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_cache_level(self, *, value: str = None, **kwargs) -> DetailedResponse:
        """
        Set cache level setting for a specific zone.

        The `basic` setting will cache most static resources (i.e., css, images, and
        JavaScript). The `simplified` setting will ignore the query string when delivering
        a cached resource. The `aggressive` setting will cache all static resources,
        including ones with a query string.

        :param str value: (optional) cache level.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CacheLevelResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_cache_level')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/cache_level'.format(*self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

