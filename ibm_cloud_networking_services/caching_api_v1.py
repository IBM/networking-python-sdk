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


    def purge_all(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Purge all.

        All resources in CDN edge servers' cache should be removed. This may have dramatic
        affects on your origin server load after performing this action.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PurgeAllResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='purge_all')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/purge_cache/purge_all'.format(
            *self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def purge_by_urls(self,
        *,
        files: List[str] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Purge URLs.

        Granularly remove one or more files from CDN edge servers' cache either by
        specifying URLs.

        :param List[str] files: (optional) purge url array.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PurgeAllResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='purge_by_urls')
        headers.update(sdk_headers)

        data = {
            'files': files
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/purge_cache/purge_by_urls'.format(
            *self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def purge_by_cache_tags(self,
        *,
        tags: List[str] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Purge Cache-Tags.

        Granularly remove one or more files from CDN edge servers' cache either by
        specifying the associated Cache-Tags.

        :param List[str] tags: (optional) array of tags.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PurgeAllResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='purge_by_cache_tags')
        headers.update(sdk_headers)

        data = {
            'tags': tags
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/purge_cache/purge_by_cache_tags'.format(
            *self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def purge_by_hosts(self,
        *,
        hosts: List[str] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Purge host names.

        Granularly remove one or more files from CDN edge servers' cache either by
        specifying the hostnames.

        :param List[str] hosts: (optional) hosts name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PurgeAllResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='purge_by_hosts')
        headers.update(sdk_headers)

        data = {
            'hosts': hosts
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/purge_cache/purge_by_hosts'.format(
            *self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_browser_cache_ttl(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get browser cache TTL setting.

        Browser Cache TTL (in seconds) specifies how long CDN edge servers cached
        resources will remain on your visitors' computers.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BrowserTTLResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_browser_cache_ttl')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/browser_cache_ttl'.format(
            *self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_browser_cache_ttl(self,
        *,
        value: int = None,
        **kwargs
    ) -> DetailedResponse:
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_browser_cache_ttl')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/browser_cache_ttl'.format(
            *self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_development_mode(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get development mode setting.

        Get development mode setting.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeveopmentModeResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_development_mode')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/development_mode'.format(
            *self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_development_mode(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Change development mode setting.

        Change development mode setting.

        :param str value: (optional) on/off value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeveopmentModeResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_development_mode')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/development_mode'.format(
            *self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_query_string_sort(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get Enable Query String Sort setting.

        Get Enable Query String Sort setting.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `EnableQueryStringSortResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_query_string_sort')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/sort_query_string_for_cache'.format(
            *self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_query_string_sort(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Change Enable Query String Sort setting.

        Change Enable Query String Sort setting.

        :param str value: (optional) on/off property value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `EnableQueryStringSortResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_query_string_sort')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/sort_query_string_for_cache'.format(
            *self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # cacheLevel
    #########################


    def get_cache_level(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get cache level setting of a specific zone.

        Get cache level setting of a specific zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CacheLevelResponse` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_cache_level')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/cache_level'.format(
            *self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_cache_level(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_cache_level')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/cache_level'.format(
            *self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class BrowserTTLResponseResult():
    """
    result object.

    :attr str id: (optional) ttl type.
    :attr int value: (optional) ttl value.
    :attr bool editable: (optional) editable.
    :attr str modified_on: (optional) modified date.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 value: int = None,
                 editable: bool = None,
                 modified_on: str = None) -> None:
        """
        Initialize a BrowserTTLResponseResult object.

        :param str id: (optional) ttl type.
        :param int value: (optional) ttl value.
        :param bool editable: (optional) editable.
        :param str modified_on: (optional) modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BrowserTTLResponseResult':
        """Initialize a BrowserTTLResponseResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BrowserTTLResponseResult object from a json dictionary."""
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
        """Return a `str` version of this BrowserTTLResponseResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BrowserTTLResponseResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BrowserTTLResponseResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CacheLevelResponseResult():
    """
    result.

    :attr str id: (optional) cache level.
    :attr str value: (optional) cache level.
    :attr bool editable: (optional) editable value.
    :attr str modified_on: (optional) modified date.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 value: str = None,
                 editable: bool = None,
                 modified_on: str = None) -> None:
        """
        Initialize a CacheLevelResponseResult object.

        :param str id: (optional) cache level.
        :param str value: (optional) cache level.
        :param bool editable: (optional) editable value.
        :param str modified_on: (optional) modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CacheLevelResponseResult':
        """Initialize a CacheLevelResponseResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CacheLevelResponseResult object from a json dictionary."""
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
        """Return a `str` version of this CacheLevelResponseResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CacheLevelResponseResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CacheLevelResponseResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DeveopmentModeResponseResult():
    """
    result object.

    :attr str id: (optional) object id.
    :attr str value: (optional) on/off value.
    :attr bool editable: (optional) editable value.
    :attr str modified_on: (optional) modified date.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 value: str = None,
                 editable: bool = None,
                 modified_on: str = None) -> None:
        """
        Initialize a DeveopmentModeResponseResult object.

        :param str id: (optional) object id.
        :param str value: (optional) on/off value.
        :param bool editable: (optional) editable value.
        :param str modified_on: (optional) modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeveopmentModeResponseResult':
        """Initialize a DeveopmentModeResponseResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeveopmentModeResponseResult object from a json dictionary."""
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
        """Return a `str` version of this DeveopmentModeResponseResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeveopmentModeResponseResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeveopmentModeResponseResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class EnableQueryStringSortResponseResult():
    """
    result of sort query string.

    :attr str id: (optional) cache id.
    :attr str value: (optional) on/off value.
    :attr bool editable: (optional) editable propery.
    :attr str modified_on: (optional) modified date.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 value: str = None,
                 editable: bool = None,
                 modified_on: str = None) -> None:
        """
        Initialize a EnableQueryStringSortResponseResult object.

        :param str id: (optional) cache id.
        :param str value: (optional) on/off value.
        :param bool editable: (optional) editable propery.
        :param str modified_on: (optional) modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EnableQueryStringSortResponseResult':
        """Initialize a EnableQueryStringSortResponseResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EnableQueryStringSortResponseResult object from a json dictionary."""
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
        """Return a `str` version of this EnableQueryStringSortResponseResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EnableQueryStringSortResponseResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EnableQueryStringSortResponseResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PurgeAllResponseResult():
    """
    purge object.

    :attr str id: (optional) purge id.
    """

    def __init__(self,
                 *,
                 id: str = None) -> None:
        """
        Initialize a PurgeAllResponseResult object.

        :param str id: (optional) purge id.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PurgeAllResponseResult':
        """Initialize a PurgeAllResponseResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PurgeAllResponseResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PurgeAllResponseResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PurgeAllResponseResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PurgeAllResponseResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class BrowserTTLResponse():
    """
    browser ttl response.

    :attr bool success: success response.
    :attr List[List[str]] errors: errors.
    :attr List[List[str]] messages: messages.
    :attr BrowserTTLResponseResult result: result object.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'BrowserTTLResponseResult') -> None:
        """
        Initialize a BrowserTTLResponse object.

        :param bool success: success response.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param BrowserTTLResponseResult result: result object.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BrowserTTLResponse':
        """Initialize a BrowserTTLResponse object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in BrowserTTLResponse JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in BrowserTTLResponse JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in BrowserTTLResponse JSON')
        if 'result' in _dict:
            args['result'] = BrowserTTLResponseResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in BrowserTTLResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BrowserTTLResponse object from a json dictionary."""
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
        """Return a `str` version of this BrowserTTLResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BrowserTTLResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BrowserTTLResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CacheLevelResponse():
    """
    cache level response.

    :attr bool success: success response.
    :attr List[List[str]] errors: errors.
    :attr List[List[str]] messages: messages.
    :attr CacheLevelResponseResult result: result.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'CacheLevelResponseResult') -> None:
        """
        Initialize a CacheLevelResponse object.

        :param bool success: success response.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param CacheLevelResponseResult result: result.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CacheLevelResponse':
        """Initialize a CacheLevelResponse object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in CacheLevelResponse JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in CacheLevelResponse JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in CacheLevelResponse JSON')
        if 'result' in _dict:
            args['result'] = CacheLevelResponseResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in CacheLevelResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CacheLevelResponse object from a json dictionary."""
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
        """Return a `str` version of this CacheLevelResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CacheLevelResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CacheLevelResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DeveopmentModeResponse():
    """
    development mode response.

    :attr bool success: success response.
    :attr List[List[str]] errors: errors.
    :attr List[List[str]] messages: messages.
    :attr DeveopmentModeResponseResult result: result object.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'DeveopmentModeResponseResult') -> None:
        """
        Initialize a DeveopmentModeResponse object.

        :param bool success: success response.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param DeveopmentModeResponseResult result: result object.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeveopmentModeResponse':
        """Initialize a DeveopmentModeResponse object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in DeveopmentModeResponse JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in DeveopmentModeResponse JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in DeveopmentModeResponse JSON')
        if 'result' in _dict:
            args['result'] = DeveopmentModeResponseResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in DeveopmentModeResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeveopmentModeResponse object from a json dictionary."""
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
        """Return a `str` version of this DeveopmentModeResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeveopmentModeResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeveopmentModeResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class EnableQueryStringSortResponse():
    """
    sort query string response.

    :attr bool success: success response true/false.
    :attr List[List[str]] errors: errors.
    :attr List[List[str]] messages: messages.
    :attr EnableQueryStringSortResponseResult result: result of sort query string.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'EnableQueryStringSortResponseResult') -> None:
        """
        Initialize a EnableQueryStringSortResponse object.

        :param bool success: success response true/false.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param EnableQueryStringSortResponseResult result: result of sort query
               string.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EnableQueryStringSortResponse':
        """Initialize a EnableQueryStringSortResponse object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in EnableQueryStringSortResponse JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in EnableQueryStringSortResponse JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in EnableQueryStringSortResponse JSON')
        if 'result' in _dict:
            args['result'] = EnableQueryStringSortResponseResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in EnableQueryStringSortResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EnableQueryStringSortResponse object from a json dictionary."""
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
        """Return a `str` version of this EnableQueryStringSortResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EnableQueryStringSortResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EnableQueryStringSortResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class PurgeAllResponse():
    """
    purge all response.

    :attr bool success: success response.
    :attr List[List[str]] errors: errors.
    :attr List[List[str]] messages: messages.
    :attr PurgeAllResponseResult result: purge object.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'PurgeAllResponseResult') -> None:
        """
        Initialize a PurgeAllResponse object.

        :param bool success: success response.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param PurgeAllResponseResult result: purge object.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PurgeAllResponse':
        """Initialize a PurgeAllResponse object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in PurgeAllResponse JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in PurgeAllResponse JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in PurgeAllResponse JSON')
        if 'result' in _dict:
            args['result'] = PurgeAllResponseResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in PurgeAllResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PurgeAllResponse object from a json dictionary."""
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
        """Return a `str` version of this PurgeAllResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PurgeAllResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PurgeAllResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
