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


    def list_instance_custom_pages(self,
        **kwargs
    ) -> DetailedResponse:
        """
        List all custom pages for a given instance.

        List all custom pages for a given instance.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListCustomPagesResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_instance_custom_pages')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/custom_pages'.format(
            *self.encode_path_vars(self.crn))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_instance_custom_page(self,
        page_identifier: str,
        **kwargs
    ) -> DetailedResponse:
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_instance_custom_page')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/custom_pages/{1}'.format(
            *self.encode_path_vars(self.crn, page_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_instance_custom_page(self,
        page_identifier: str,
        *,
        url: str = None,
        state: str = None,
        **kwargs
    ) -> DetailedResponse:
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_instance_custom_page')
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

        url = '/v1/{0}/custom_pages/{1}'.format(
            *self.encode_path_vars(self.crn, page_identifier))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def list_zone_custom_pages(self,
        **kwargs
    ) -> DetailedResponse:
        """
        List all custom pages for a given zone.

        List all custom pages for a given zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListCustomPagesResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_zone_custom_pages')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/custom_pages'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_zone_custom_page(self,
        page_identifier: str,
        **kwargs
    ) -> DetailedResponse:
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_zone_custom_page')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/custom_pages/{2}'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier, page_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_zone_custom_page(self,
        page_identifier: str,
        *,
        url: str = None,
        state: str = None,
        **kwargs
    ) -> DetailedResponse:
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_zone_custom_page')
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

        url = '/v1/{0}/zones/{1}/custom_pages/{2}'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier, page_identifier))
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

    class PageIdentifier(str, Enum):
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

    class PageIdentifier(str, Enum):
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

    class PageIdentifier(str, Enum):
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

    class PageIdentifier(str, Enum):
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


##############################################################################
# Models
##############################################################################


class ListCustomPagesRespResultInfo():
    """
    Statistics of results.

    :attr int page: Page number.
    :attr int per_page: Number of results per page.
    :attr int total_pages: Number of total pages.
    :attr int count: Number of results.
    :attr int total_count: Total number of results.
    """

    def __init__(self,
                 page: int,
                 per_page: int,
                 total_pages: int,
                 count: int,
                 total_count: int) -> None:
        """
        Initialize a ListCustomPagesRespResultInfo object.

        :param int page: Page number.
        :param int per_page: Number of results per page.
        :param int total_pages: Number of total pages.
        :param int count: Number of results.
        :param int total_count: Total number of results.
        """
        self.page = page
        self.per_page = per_page
        self.total_pages = total_pages
        self.count = count
        self.total_count = total_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListCustomPagesRespResultInfo':
        """Initialize a ListCustomPagesRespResultInfo object from a json dictionary."""
        args = {}
        if 'page' in _dict:
            args['page'] = _dict.get('page')
        else:
            raise ValueError('Required property \'page\' not present in ListCustomPagesRespResultInfo JSON')
        if 'per_page' in _dict:
            args['per_page'] = _dict.get('per_page')
        else:
            raise ValueError('Required property \'per_page\' not present in ListCustomPagesRespResultInfo JSON')
        if 'total_pages' in _dict:
            args['total_pages'] = _dict.get('total_pages')
        else:
            raise ValueError('Required property \'total_pages\' not present in ListCustomPagesRespResultInfo JSON')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        else:
            raise ValueError('Required property \'count\' not present in ListCustomPagesRespResultInfo JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in ListCustomPagesRespResultInfo JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListCustomPagesRespResultInfo object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'page') and self.page is not None:
            _dict['page'] = self.page
        if hasattr(self, 'per_page') and self.per_page is not None:
            _dict['per_page'] = self.per_page
        if hasattr(self, 'total_pages') and self.total_pages is not None:
            _dict['total_pages'] = self.total_pages
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListCustomPagesRespResultInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListCustomPagesRespResultInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListCustomPagesRespResultInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CustomPageObject():
    """
    custom page object.

    :attr str id: Custom page identifier.
    :attr str description: Description of custom page.
    :attr List[str] required_tokens: array of page tokens.
    :attr str preview_target: Preview target.
    :attr datetime created_on: Created date.
    :attr datetime modified_on: Modified date.
    :attr str url: A URL that is associated with the Custom Page.
    :attr str state: The Custom Page state.
    """

    def __init__(self,
                 id: str,
                 description: str,
                 required_tokens: List[str],
                 preview_target: str,
                 created_on: datetime,
                 modified_on: datetime,
                 url: str,
                 state: str) -> None:
        """
        Initialize a CustomPageObject object.

        :param str id: Custom page identifier.
        :param str description: Description of custom page.
        :param List[str] required_tokens: array of page tokens.
        :param str preview_target: Preview target.
        :param datetime created_on: Created date.
        :param datetime modified_on: Modified date.
        :param str url: A URL that is associated with the Custom Page.
        :param str state: The Custom Page state.
        """
        self.id = id
        self.description = description
        self.required_tokens = required_tokens
        self.preview_target = preview_target
        self.created_on = created_on
        self.modified_on = modified_on
        self.url = url
        self.state = state

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CustomPageObject':
        """Initialize a CustomPageObject object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in CustomPageObject JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError('Required property \'description\' not present in CustomPageObject JSON')
        if 'required_tokens' in _dict:
            args['required_tokens'] = _dict.get('required_tokens')
        else:
            raise ValueError('Required property \'required_tokens\' not present in CustomPageObject JSON')
        if 'preview_target' in _dict:
            args['preview_target'] = _dict.get('preview_target')
        else:
            raise ValueError('Required property \'preview_target\' not present in CustomPageObject JSON')
        if 'created_on' in _dict:
            args['created_on'] = string_to_datetime(_dict.get('created_on'))
        else:
            raise ValueError('Required property \'created_on\' not present in CustomPageObject JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in CustomPageObject JSON')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        else:
            raise ValueError('Required property \'url\' not present in CustomPageObject JSON')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        else:
            raise ValueError('Required property \'state\' not present in CustomPageObject JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CustomPageObject object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'required_tokens') and self.required_tokens is not None:
            _dict['required_tokens'] = self.required_tokens
        if hasattr(self, 'preview_target') and self.preview_target is not None:
            _dict['preview_target'] = self.preview_target
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = datetime_to_string(self.created_on)
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = datetime_to_string(self.modified_on)
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CustomPageObject object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CustomPageObject') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CustomPageObject') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class IdEnum(str, Enum):
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


    class RequiredTokensEnum(str, Enum):
        """
        required_tokens.
        """
        CAPTCHA_BOX = '::CAPTCHA_BOX::'
        IM_UNDER_ATTACK_BOX = '::IM_UNDER_ATTACK_BOX::'
        CLOUDFLARE_ERROR_500S_BOX = '::CLOUDFLARE_ERROR_500S_BOX::'
        CLOUDFLARE_ERROR_1000S_BOX = '::CLOUDFLARE_ERROR_1000S_BOX::'


    class StateEnum(str, Enum):
        """
        The Custom Page state.
        """
        DEFAULT = 'default'
        CUSTOMIZED = 'customized'


class CustomPageSpecificResp():
    """
    custom page specific response.

    :attr bool success: Was operation successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr CustomPageObject result: custom page object.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'CustomPageObject') -> None:
        """
        Initialize a CustomPageSpecificResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param CustomPageObject result: custom page object.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CustomPageSpecificResp':
        """Initialize a CustomPageSpecificResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in CustomPageSpecificResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in CustomPageSpecificResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in CustomPageSpecificResp JSON')
        if 'result' in _dict:
            args['result'] = CustomPageObject.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in CustomPageSpecificResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CustomPageSpecificResp object from a json dictionary."""
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
        """Return a `str` version of this CustomPageSpecificResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CustomPageSpecificResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CustomPageSpecificResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListCustomPagesResp():
    """
    list of custom pages response.

    :attr bool success: Was operation successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr List[CustomPageObject] result: custom pages array.
    :attr ListCustomPagesRespResultInfo result_info: Statistics of results.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: List['CustomPageObject'],
                 result_info: 'ListCustomPagesRespResultInfo') -> None:
        """
        Initialize a ListCustomPagesResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param List[CustomPageObject] result: custom pages array.
        :param ListCustomPagesRespResultInfo result_info: Statistics of results.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result
        self.result_info = result_info

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListCustomPagesResp':
        """Initialize a ListCustomPagesResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in ListCustomPagesResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in ListCustomPagesResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in ListCustomPagesResp JSON')
        if 'result' in _dict:
            args['result'] = [CustomPageObject.from_dict(x) for x in _dict.get('result')]
        else:
            raise ValueError('Required property \'result\' not present in ListCustomPagesResp JSON')
        if 'result_info' in _dict:
            args['result_info'] = ListCustomPagesRespResultInfo.from_dict(_dict.get('result_info'))
        else:
            raise ValueError('Required property \'result_info\' not present in ListCustomPagesResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListCustomPagesResp object from a json dictionary."""
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
            _dict['result'] = [x.to_dict() for x in self.result]
        if hasattr(self, 'result_info') and self.result_info is not None:
            _dict['result_info'] = self.result_info.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListCustomPagesResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListCustomPagesResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListCustomPagesResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
