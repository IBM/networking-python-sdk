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
Zone Rate Limits
"""

from enum import Enum
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class ZoneRateLimitsV1(BaseService):
    """The Zone Rate Limits V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'zone_rate_limits'

    @classmethod
    def new_instance(cls,
                     crn: str,
                     zone_identifier: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'ZoneRateLimitsV1':
        """
        Return a new client for the Zone Rate Limits service using the specified
               parameters and external configuration.

        :param str crn: Full crn of the service instance.

        :param str zone_identifier: Zone identifier (zone id).
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
        Construct a new client for the Zone Rate Limits service.

        :param str crn: Full crn of the service instance.

        :param str zone_identifier: Zone identifier (zone id).

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
    # Zone Rate Limits
    #########################


    def list_all_zone_rate_limits(self,
        *,
        page: int = None,
        per_page: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List all rate limits.

        The details of Rate Limit for a given zone under a given service instance.

        :param int page: (optional) Page number of paginated results.
        :param int per_page: (optional) Maximum number of rate limits per page.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListRatelimitResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_all_zone_rate_limits')
        headers.update(sdk_headers)

        params = {
            'page': page,
            'per_page': per_page
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/rate_limits'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_zone_rate_limits(self,
        *,
        threshold: int = None,
        period: int = None,
        action: 'RatelimitInputAction' = None,
        match: 'RatelimitInputMatch' = None,
        disabled: bool = None,
        description: str = None,
        bypass: List['RatelimitInputBypassItem'] = None,
        correlate: 'RatelimitInputCorrelate' = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create rate limit.

        Create a new rate limit for a given zone under a service instance.

        :param int threshold: (optional) The threshold that triggers the rate limit
               mitigations, combine with period. i.e. threshold per period.
        :param int period: (optional) The time in seconds to count matching
               traffic. If the count exceeds threshold within this period the action will
               be performed.
        :param RatelimitInputAction action: (optional) action.
        :param RatelimitInputMatch match: (optional) Determines which traffic the
               rate limit counts towards the threshold. Needs to be one of "request" or
               "response" objects.
        :param bool disabled: (optional) Whether this ratelimit is currently
               disabled.
        :param str description: (optional) A note that you can use to describe the
               reason for a rate limit.
        :param List[RatelimitInputBypassItem] bypass: (optional) Criteria that
               would allow the rate limit to be bypassed, for example to express that you
               shouldn't apply a rate limit to a given set of URLs.
        :param RatelimitInputCorrelate correlate: (optional) Enable NAT based rate
               limits.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RatelimitResp` object
        """

        if action is not None:
            action = convert_model(action)
        if match is not None:
            match = convert_model(match)
        if bypass is not None:
            bypass = [convert_model(x) for x in bypass]
        if correlate is not None:
            correlate = convert_model(correlate)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_zone_rate_limits')
        headers.update(sdk_headers)

        data = {
            'threshold': threshold,
            'period': period,
            'action': action,
            'match': match,
            'disabled': disabled,
            'description': description,
            'bypass': bypass,
            'correlate': correlate
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/rate_limits'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_zone_rate_limit(self,
        rate_limit_identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete rate limit.

        Delete a rate limit given its id.

        :param str rate_limit_identifier: Identifier of the rate limit to be
               deleted.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteRateLimitResp` object
        """

        if rate_limit_identifier is None:
            raise ValueError('rate_limit_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_zone_rate_limit')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/rate_limits/{2}'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier, rate_limit_identifier))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_rate_limit(self,
        rate_limit_identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a rate limit.

        Get the details of a rate limit for a given zone under a given service instance.

        :param str rate_limit_identifier: Identifier of rate limit for the given
               zone.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RatelimitResp` object
        """

        if rate_limit_identifier is None:
            raise ValueError('rate_limit_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_rate_limit')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/rate_limits/{2}'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier, rate_limit_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_rate_limit(self,
        rate_limit_identifier: str,
        *,
        threshold: int = None,
        period: int = None,
        action: 'RatelimitInputAction' = None,
        match: 'RatelimitInputMatch' = None,
        disabled: bool = None,
        description: str = None,
        bypass: List['RatelimitInputBypassItem'] = None,
        correlate: 'RatelimitInputCorrelate' = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update rate limit.

        Update an existing rate limit for a given zone under a service instance.

        :param str rate_limit_identifier: Identifier of rate limit.
        :param int threshold: (optional) The threshold that triggers the rate limit
               mitigations, combine with period. i.e. threshold per period.
        :param int period: (optional) The time in seconds to count matching
               traffic. If the count exceeds threshold within this period the action will
               be performed.
        :param RatelimitInputAction action: (optional) action.
        :param RatelimitInputMatch match: (optional) Determines which traffic the
               rate limit counts towards the threshold. Needs to be one of "request" or
               "response" objects.
        :param bool disabled: (optional) Whether this ratelimit is currently
               disabled.
        :param str description: (optional) A note that you can use to describe the
               reason for a rate limit.
        :param List[RatelimitInputBypassItem] bypass: (optional) Criteria that
               would allow the rate limit to be bypassed, for example to express that you
               shouldn't apply a rate limit to a given set of URLs.
        :param RatelimitInputCorrelate correlate: (optional) Enable NAT based rate
               limits.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RatelimitResp` object
        """

        if rate_limit_identifier is None:
            raise ValueError('rate_limit_identifier must be provided')
        if action is not None:
            action = convert_model(action)
        if match is not None:
            match = convert_model(match)
        if bypass is not None:
            bypass = [convert_model(x) for x in bypass]
        if correlate is not None:
            correlate = convert_model(correlate)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_rate_limit')
        headers.update(sdk_headers)

        data = {
            'threshold': threshold,
            'period': period,
            'action': action,
            'match': match,
            'disabled': disabled,
            'description': description,
            'bypass': bypass,
            'correlate': correlate
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/rate_limits/{2}'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier, rate_limit_identifier))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class DeleteRateLimitRespResult():
    """
    Container for response information.

    :attr str id: ID.
    """

    def __init__(self,
                 id: str) -> None:
        """
        Initialize a DeleteRateLimitRespResult object.

        :param str id: ID.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteRateLimitRespResult':
        """Initialize a DeleteRateLimitRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in DeleteRateLimitRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteRateLimitRespResult object from a json dictionary."""
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
        """Return a `str` version of this DeleteRateLimitRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteRateLimitRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteRateLimitRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListRatelimitRespResultInfo():
    """
    Statistics of results.

    :attr int page: Page number.
    :attr int per_page: Number of results per page.
    :attr int count: Number of results.
    :attr int total_count: Total number of results.
    """

    def __init__(self,
                 page: int,
                 per_page: int,
                 count: int,
                 total_count: int) -> None:
        """
        Initialize a ListRatelimitRespResultInfo object.

        :param int page: Page number.
        :param int per_page: Number of results per page.
        :param int count: Number of results.
        :param int total_count: Total number of results.
        """
        self.page = page
        self.per_page = per_page
        self.count = count
        self.total_count = total_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListRatelimitRespResultInfo':
        """Initialize a ListRatelimitRespResultInfo object from a json dictionary."""
        args = {}
        if 'page' in _dict:
            args['page'] = _dict.get('page')
        else:
            raise ValueError('Required property \'page\' not present in ListRatelimitRespResultInfo JSON')
        if 'per_page' in _dict:
            args['per_page'] = _dict.get('per_page')
        else:
            raise ValueError('Required property \'per_page\' not present in ListRatelimitRespResultInfo JSON')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        else:
            raise ValueError('Required property \'count\' not present in ListRatelimitRespResultInfo JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in ListRatelimitRespResultInfo JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListRatelimitRespResultInfo object from a json dictionary."""
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
        """Return a `str` version of this ListRatelimitRespResultInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListRatelimitRespResultInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListRatelimitRespResultInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RatelimitInputAction():
    """
    action.

    :attr str mode: The type of action to perform.
    :attr int timeout: (optional) The time in seconds as an integer to perform the
          mitigation action. Must be the same or greater than the period. This field is
          valid only when mode is "simulate" or "ban".
    :attr RatelimitInputActionResponse response: (optional) Custom content-type and
          body to return, this overrides the custom error for the zone. This field is not
          required. Omission will result in default HTML error page.This field is valid
          only when mode is "simulate" or "ban".
    """

    def __init__(self,
                 mode: str,
                 *,
                 timeout: int = None,
                 response: 'RatelimitInputActionResponse' = None) -> None:
        """
        Initialize a RatelimitInputAction object.

        :param str mode: The type of action to perform.
        :param int timeout: (optional) The time in seconds as an integer to perform
               the mitigation action. Must be the same or greater than the period. This
               field is valid only when mode is "simulate" or "ban".
        :param RatelimitInputActionResponse response: (optional) Custom
               content-type and body to return, this overrides the custom error for the
               zone. This field is not required. Omission will result in default HTML
               error page.This field is valid only when mode is "simulate" or "ban".
        """
        self.mode = mode
        self.timeout = timeout
        self.response = response

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitInputAction':
        """Initialize a RatelimitInputAction object from a json dictionary."""
        args = {}
        if 'mode' in _dict:
            args['mode'] = _dict.get('mode')
        else:
            raise ValueError('Required property \'mode\' not present in RatelimitInputAction JSON')
        if 'timeout' in _dict:
            args['timeout'] = _dict.get('timeout')
        if 'response' in _dict:
            args['response'] = RatelimitInputActionResponse.from_dict(_dict.get('response'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitInputAction object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'mode') and self.mode is not None:
            _dict['mode'] = self.mode
        if hasattr(self, 'timeout') and self.timeout is not None:
            _dict['timeout'] = self.timeout
        if hasattr(self, 'response') and self.response is not None:
            _dict['response'] = self.response.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitInputAction object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitInputAction') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitInputAction') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ModeEnum(str, Enum):
        """
        The type of action to perform.
        """
        SIMULATE = 'simulate'
        BAN = 'ban'
        CHALLENGE = 'challenge'
        JS_CHALLENGE = 'js_challenge'


class RatelimitInputActionResponse():
    """
    Custom content-type and body to return, this overrides the custom error for the zone.
    This field is not required. Omission will result in default HTML error page.This field
    is valid only when mode is "simulate" or "ban".

    :attr str content_type: (optional) The content type of the body.
    :attr str body: (optional) The body to return, the content here should conform
          to the content_type.
    """

    def __init__(self,
                 *,
                 content_type: str = None,
                 body: str = None) -> None:
        """
        Initialize a RatelimitInputActionResponse object.

        :param str content_type: (optional) The content type of the body.
        :param str body: (optional) The body to return, the content here should
               conform to the content_type.
        """
        self.content_type = content_type
        self.body = body

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitInputActionResponse':
        """Initialize a RatelimitInputActionResponse object from a json dictionary."""
        args = {}
        if 'content_type' in _dict:
            args['content_type'] = _dict.get('content_type')
        if 'body' in _dict:
            args['body'] = _dict.get('body')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitInputActionResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'content_type') and self.content_type is not None:
            _dict['content_type'] = self.content_type
        if hasattr(self, 'body') and self.body is not None:
            _dict['body'] = self.body
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitInputActionResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitInputActionResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitInputActionResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ContentTypeEnum(str, Enum):
        """
        The content type of the body.
        """
        TEXT_PLAIN = 'text/plain'
        TEXT_XML = 'text/xml'
        APPLICATION_JSON = 'application/json'


class RatelimitInputBypassItem():
    """
    RatelimitInputBypassItem.

    :attr str name: Rate limit name.
    :attr str value: The url to bypass.
    """

    def __init__(self,
                 name: str,
                 value: str) -> None:
        """
        Initialize a RatelimitInputBypassItem object.

        :param str name: Rate limit name.
        :param str value: The url to bypass.
        """
        self.name = name
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitInputBypassItem':
        """Initialize a RatelimitInputBypassItem object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in RatelimitInputBypassItem JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in RatelimitInputBypassItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitInputBypassItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitInputBypassItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitInputBypassItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitInputBypassItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class NameEnum(str, Enum):
        """
        Rate limit name.
        """
        URL = 'url'


class RatelimitInputCorrelate():
    """
    Enable NAT based rate limits.

    :attr str by: NAT rate limits by.
    """

    def __init__(self,
                 by: str) -> None:
        """
        Initialize a RatelimitInputCorrelate object.

        :param str by: NAT rate limits by.
        """
        self.by = by

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitInputCorrelate':
        """Initialize a RatelimitInputCorrelate object from a json dictionary."""
        args = {}
        if 'by' in _dict:
            args['by'] = _dict.get('by')
        else:
            raise ValueError('Required property \'by\' not present in RatelimitInputCorrelate JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitInputCorrelate object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'by') and self.by is not None:
            _dict['by'] = self.by
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitInputCorrelate object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitInputCorrelate') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitInputCorrelate') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ByEnum(str, Enum):
        """
        NAT rate limits by.
        """
        NAT = 'nat'


class RatelimitInputMatch():
    """
    Determines which traffic the rate limit counts towards the threshold. Needs to be one
    of "request" or "response" objects.

    :attr RatelimitInputMatchRequest request: (optional) request.
    :attr RatelimitInputMatchResponse response: (optional) response.
    """

    def __init__(self,
                 *,
                 request: 'RatelimitInputMatchRequest' = None,
                 response: 'RatelimitInputMatchResponse' = None) -> None:
        """
        Initialize a RatelimitInputMatch object.

        :param RatelimitInputMatchRequest request: (optional) request.
        :param RatelimitInputMatchResponse response: (optional) response.
        """
        self.request = request
        self.response = response

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitInputMatch':
        """Initialize a RatelimitInputMatch object from a json dictionary."""
        args = {}
        if 'request' in _dict:
            args['request'] = RatelimitInputMatchRequest.from_dict(_dict.get('request'))
        if 'response' in _dict:
            args['response'] = RatelimitInputMatchResponse.from_dict(_dict.get('response'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitInputMatch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'request') and self.request is not None:
            _dict['request'] = self.request.to_dict()
        if hasattr(self, 'response') and self.response is not None:
            _dict['response'] = self.response.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitInputMatch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitInputMatch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitInputMatch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RatelimitInputMatchRequest():
    """
    request.

    :attr List[str] methods: (optional) A subset of the list HTTP methods, or
          ["_ALL_"] for selecting all methods.
    :attr List[str] schemes: (optional) HTTP schemes list, or ["_ALL_"] for
          selecting all schemes.
    :attr str url: The URL pattern to match comprised of the host and path, i.e.
          example.org/path. Wildcard are expanded to match applicable traffic, query
          strings are not matched. Use * for all traffic to your zone.
    """

    def __init__(self,
                 url: str,
                 *,
                 methods: List[str] = None,
                 schemes: List[str] = None) -> None:
        """
        Initialize a RatelimitInputMatchRequest object.

        :param str url: The URL pattern to match comprised of the host and path,
               i.e. example.org/path. Wildcard are expanded to match applicable traffic,
               query strings are not matched. Use * for all traffic to your zone.
        :param List[str] methods: (optional) A subset of the list HTTP methods, or
               ["_ALL_"] for selecting all methods.
        :param List[str] schemes: (optional) HTTP schemes list, or ["_ALL_"] for
               selecting all schemes.
        """
        self.methods = methods
        self.schemes = schemes
        self.url = url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitInputMatchRequest':
        """Initialize a RatelimitInputMatchRequest object from a json dictionary."""
        args = {}
        if 'methods' in _dict:
            args['methods'] = _dict.get('methods')
        if 'schemes' in _dict:
            args['schemes'] = _dict.get('schemes')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        else:
            raise ValueError('Required property \'url\' not present in RatelimitInputMatchRequest JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitInputMatchRequest object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'methods') and self.methods is not None:
            _dict['methods'] = self.methods
        if hasattr(self, 'schemes') and self.schemes is not None:
            _dict['schemes'] = self.schemes
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitInputMatchRequest object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitInputMatchRequest') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitInputMatchRequest') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class MethodsEnum(str, Enum):
        """
        methods.
        """
        GET = 'GET'
        POST = 'POST'
        PUT = 'PUT'
        DELETE = 'DELETE'
        PATCH = 'PATCH'
        HEAD = 'HEAD'
        ALL = '_ALL_'


    class SchemesEnum(str, Enum):
        """
        schemes.
        """
        HTTP = 'HTTP'
        HTTPS = 'HTTPS'
        ALL = '_ALL_'


class RatelimitInputMatchResponse():
    """
    response.

    :attr List[int] status: (optional) HTTP Status codes, can be one [403], many
          [401,403] or indicate all by not providing this value. This field is not
          required.
    :attr List[RatelimitInputMatchResponseHeadersItem] headers_: (optional) Array of
          response headers to match. If a response does not meet the header criteria then
          the request will not be counted towards the rate limit.
    :attr bool origin_traffic: (optional) Deprecated, please use response headers
          instead and also provide "origin_traffic:false" to avoid legacy behaviour
          interacting with the response.headers property.
    """

    def __init__(self,
                 *,
                 status: List[int] = None,
                 headers_: List['RatelimitInputMatchResponseHeadersItem'] = None,
                 origin_traffic: bool = None) -> None:
        """
        Initialize a RatelimitInputMatchResponse object.

        :param List[int] status: (optional) HTTP Status codes, can be one [403],
               many [401,403] or indicate all by not providing this value. This field is
               not required.
        :param List[RatelimitInputMatchResponseHeadersItem] headers_: (optional)
               Array of response headers to match. If a response does not meet the header
               criteria then the request will not be counted towards the rate limit.
        :param bool origin_traffic: (optional) Deprecated, please use response
               headers instead and also provide "origin_traffic:false" to avoid legacy
               behaviour interacting with the response.headers property.
        """
        self.status = status
        self.headers_ = headers_
        self.origin_traffic = origin_traffic

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitInputMatchResponse':
        """Initialize a RatelimitInputMatchResponse object from a json dictionary."""
        args = {}
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'headers' in _dict:
            args['headers_'] = [RatelimitInputMatchResponseHeadersItem.from_dict(x) for x in _dict.get('headers')]
        if 'origin_traffic' in _dict:
            args['origin_traffic'] = _dict.get('origin_traffic')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitInputMatchResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'headers_') and self.headers_ is not None:
            _dict['headers'] = [x.to_dict() for x in self.headers_]
        if hasattr(self, 'origin_traffic') and self.origin_traffic is not None:
            _dict['origin_traffic'] = self.origin_traffic
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitInputMatchResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitInputMatchResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitInputMatchResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RatelimitInputMatchResponseHeadersItem():
    """
    RatelimitInputMatchResponseHeadersItem.

    :attr str name: The name of the response header to match.
    :attr str op: The operator when matchin, eq means equals, ne means not equals.
    :attr str value: The value of the header, which will be exactly matched.
    """

    def __init__(self,
                 name: str,
                 op: str,
                 value: str) -> None:
        """
        Initialize a RatelimitInputMatchResponseHeadersItem object.

        :param str name: The name of the response header to match.
        :param str op: The operator when matchin, eq means equals, ne means not
               equals.
        :param str value: The value of the header, which will be exactly matched.
        """
        self.name = name
        self.op = op
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitInputMatchResponseHeadersItem':
        """Initialize a RatelimitInputMatchResponseHeadersItem object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in RatelimitInputMatchResponseHeadersItem JSON')
        if 'op' in _dict:
            args['op'] = _dict.get('op')
        else:
            raise ValueError('Required property \'op\' not present in RatelimitInputMatchResponseHeadersItem JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in RatelimitInputMatchResponseHeadersItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitInputMatchResponseHeadersItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'op') and self.op is not None:
            _dict['op'] = self.op
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitInputMatchResponseHeadersItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitInputMatchResponseHeadersItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitInputMatchResponseHeadersItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class OpEnum(str, Enum):
        """
        The operator when matchin, eq means equals, ne means not equals.
        """
        EQ = 'eq'
        NE = 'ne'


    class ValueEnum(str, Enum):
        """
        The value of the header, which will be exactly matched.
        """
        HIT = 'HIT'


class RatelimitObjectAction():
    """
    action.

    :attr str mode: The type of action to perform.
    :attr int timeout: (optional) The time in seconds as an integer to perform the
          mitigation action. Must be the same or greater than the period. This field is
          valid only when mode is "simulate" or "ban".
    :attr RatelimitObjectActionResponse response: (optional) Custom content-type and
          body to return, this overrides the custom error for the zone. This field is not
          required. Omission will result in default HTML error page.This field is valid
          only when mode is "simulate" or "ban".
    """

    def __init__(self,
                 mode: str,
                 *,
                 timeout: int = None,
                 response: 'RatelimitObjectActionResponse' = None) -> None:
        """
        Initialize a RatelimitObjectAction object.

        :param str mode: The type of action to perform.
        :param int timeout: (optional) The time in seconds as an integer to perform
               the mitigation action. Must be the same or greater than the period. This
               field is valid only when mode is "simulate" or "ban".
        :param RatelimitObjectActionResponse response: (optional) Custom
               content-type and body to return, this overrides the custom error for the
               zone. This field is not required. Omission will result in default HTML
               error page.This field is valid only when mode is "simulate" or "ban".
        """
        self.mode = mode
        self.timeout = timeout
        self.response = response

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitObjectAction':
        """Initialize a RatelimitObjectAction object from a json dictionary."""
        args = {}
        if 'mode' in _dict:
            args['mode'] = _dict.get('mode')
        else:
            raise ValueError('Required property \'mode\' not present in RatelimitObjectAction JSON')
        if 'timeout' in _dict:
            args['timeout'] = _dict.get('timeout')
        if 'response' in _dict:
            args['response'] = RatelimitObjectActionResponse.from_dict(_dict.get('response'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitObjectAction object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'mode') and self.mode is not None:
            _dict['mode'] = self.mode
        if hasattr(self, 'timeout') and self.timeout is not None:
            _dict['timeout'] = self.timeout
        if hasattr(self, 'response') and self.response is not None:
            _dict['response'] = self.response.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitObjectAction object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitObjectAction') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitObjectAction') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ModeEnum(str, Enum):
        """
        The type of action to perform.
        """
        SIMULATE = 'simulate'
        BAN = 'ban'
        CHALLENGE = 'challenge'
        JS_CHALLENGE = 'js_challenge'


class RatelimitObjectActionResponse():
    """
    Custom content-type and body to return, this overrides the custom error for the zone.
    This field is not required. Omission will result in default HTML error page.This field
    is valid only when mode is "simulate" or "ban".

    :attr str content_type: The content type of the body.
    :attr str body: The body to return, the content here should conform to the
          content_type.
    """

    def __init__(self,
                 content_type: str,
                 body: str) -> None:
        """
        Initialize a RatelimitObjectActionResponse object.

        :param str content_type: The content type of the body.
        :param str body: The body to return, the content here should conform to the
               content_type.
        """
        self.content_type = content_type
        self.body = body

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitObjectActionResponse':
        """Initialize a RatelimitObjectActionResponse object from a json dictionary."""
        args = {}
        if 'content_type' in _dict:
            args['content_type'] = _dict.get('content_type')
        else:
            raise ValueError('Required property \'content_type\' not present in RatelimitObjectActionResponse JSON')
        if 'body' in _dict:
            args['body'] = _dict.get('body')
        else:
            raise ValueError('Required property \'body\' not present in RatelimitObjectActionResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitObjectActionResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'content_type') and self.content_type is not None:
            _dict['content_type'] = self.content_type
        if hasattr(self, 'body') and self.body is not None:
            _dict['body'] = self.body
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitObjectActionResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitObjectActionResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitObjectActionResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ContentTypeEnum(str, Enum):
        """
        The content type of the body.
        """
        TEXT_PLAIN = 'text/plain'
        TEXT_XML = 'text/xml'
        APPLICATION_JSON = 'application/json'


class RatelimitObjectBypassItem():
    """
    RatelimitObjectBypassItem.

    :attr str name: rate limit name.
    :attr str value: The url to bypass.
    """

    def __init__(self,
                 name: str,
                 value: str) -> None:
        """
        Initialize a RatelimitObjectBypassItem object.

        :param str name: rate limit name.
        :param str value: The url to bypass.
        """
        self.name = name
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitObjectBypassItem':
        """Initialize a RatelimitObjectBypassItem object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in RatelimitObjectBypassItem JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in RatelimitObjectBypassItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitObjectBypassItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitObjectBypassItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitObjectBypassItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitObjectBypassItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class NameEnum(str, Enum):
        """
        rate limit name.
        """
        URL = 'url'


class RatelimitObjectCorrelate():
    """
    Enable NAT based rate limits.

    :attr str by: rate limit enabled by.
    """

    def __init__(self,
                 by: str) -> None:
        """
        Initialize a RatelimitObjectCorrelate object.

        :param str by: rate limit enabled by.
        """
        self.by = by

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitObjectCorrelate':
        """Initialize a RatelimitObjectCorrelate object from a json dictionary."""
        args = {}
        if 'by' in _dict:
            args['by'] = _dict.get('by')
        else:
            raise ValueError('Required property \'by\' not present in RatelimitObjectCorrelate JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitObjectCorrelate object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'by') and self.by is not None:
            _dict['by'] = self.by
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitObjectCorrelate object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitObjectCorrelate') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitObjectCorrelate') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ByEnum(str, Enum):
        """
        rate limit enabled by.
        """
        NAT = 'nat'


class RatelimitObjectMatch():
    """
    Determines which traffic the rate limit counts towards the threshold. Needs to be one
    of "request" or "response" objects.

    :attr RatelimitObjectMatchRequest request: (optional) request.
    :attr RatelimitObjectMatchResponse response: (optional) response.
    """

    def __init__(self,
                 *,
                 request: 'RatelimitObjectMatchRequest' = None,
                 response: 'RatelimitObjectMatchResponse' = None) -> None:
        """
        Initialize a RatelimitObjectMatch object.

        :param RatelimitObjectMatchRequest request: (optional) request.
        :param RatelimitObjectMatchResponse response: (optional) response.
        """
        self.request = request
        self.response = response

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitObjectMatch':
        """Initialize a RatelimitObjectMatch object from a json dictionary."""
        args = {}
        if 'request' in _dict:
            args['request'] = RatelimitObjectMatchRequest.from_dict(_dict.get('request'))
        if 'response' in _dict:
            args['response'] = RatelimitObjectMatchResponse.from_dict(_dict.get('response'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitObjectMatch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'request') and self.request is not None:
            _dict['request'] = self.request.to_dict()
        if hasattr(self, 'response') and self.response is not None:
            _dict['response'] = self.response.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitObjectMatch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitObjectMatch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitObjectMatch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RatelimitObjectMatchRequest():
    """
    request.

    :attr List[str] methods: (optional) A subset of the list HTTP methods, or
          ["_ALL_"] for selecting all methods.
    :attr List[str] schemes: (optional) HTTP schemes list, or ["_ALL_"] for
          selecting all schemes.
    :attr str url: The URL pattern to match comprised of the host and path, i.e.
          example.org/path. Wildcard are expanded to match applicable traffic, query
          strings are not matched. Use * for all traffic to your zone.
    """

    def __init__(self,
                 url: str,
                 *,
                 methods: List[str] = None,
                 schemes: List[str] = None) -> None:
        """
        Initialize a RatelimitObjectMatchRequest object.

        :param str url: The URL pattern to match comprised of the host and path,
               i.e. example.org/path. Wildcard are expanded to match applicable traffic,
               query strings are not matched. Use * for all traffic to your zone.
        :param List[str] methods: (optional) A subset of the list HTTP methods, or
               ["_ALL_"] for selecting all methods.
        :param List[str] schemes: (optional) HTTP schemes list, or ["_ALL_"] for
               selecting all schemes.
        """
        self.methods = methods
        self.schemes = schemes
        self.url = url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitObjectMatchRequest':
        """Initialize a RatelimitObjectMatchRequest object from a json dictionary."""
        args = {}
        if 'methods' in _dict:
            args['methods'] = _dict.get('methods')
        if 'schemes' in _dict:
            args['schemes'] = _dict.get('schemes')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        else:
            raise ValueError('Required property \'url\' not present in RatelimitObjectMatchRequest JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitObjectMatchRequest object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'methods') and self.methods is not None:
            _dict['methods'] = self.methods
        if hasattr(self, 'schemes') and self.schemes is not None:
            _dict['schemes'] = self.schemes
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitObjectMatchRequest object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitObjectMatchRequest') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitObjectMatchRequest') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class MethodsEnum(str, Enum):
        """
        methods.
        """
        GET = 'GET'
        POST = 'POST'
        PUT = 'PUT'
        DELETE = 'DELETE'
        PATCH = 'PATCH'
        HEAD = 'HEAD'
        ALL = '_ALL_'


    class SchemesEnum(str, Enum):
        """
        schemes.
        """
        HTTP = 'HTTP'
        HTTPS = 'HTTPS'
        ALL = '_ALL_'


class RatelimitObjectMatchResponse():
    """
    response.

    :attr List[int] status: (optional) HTTP Status codes, can be one [403], many
          [401,403] or indicate all by not providing this value. This field is not
          required.
    :attr List[RatelimitObjectMatchResponseHeadersItem] headers_: (optional) Array
          of response headers to match. If a response does not meet the header criteria
          then the request will not be counted towards the rate limit.
    :attr bool origin_traffic: (optional) Deprecated, please use response headers
          instead and also provide "origin_traffic:false" to avoid legacy behaviour
          interacting with the response.headers property.
    """

    def __init__(self,
                 *,
                 status: List[int] = None,
                 headers_: List['RatelimitObjectMatchResponseHeadersItem'] = None,
                 origin_traffic: bool = None) -> None:
        """
        Initialize a RatelimitObjectMatchResponse object.

        :param List[int] status: (optional) HTTP Status codes, can be one [403],
               many [401,403] or indicate all by not providing this value. This field is
               not required.
        :param List[RatelimitObjectMatchResponseHeadersItem] headers_: (optional)
               Array of response headers to match. If a response does not meet the header
               criteria then the request will not be counted towards the rate limit.
        :param bool origin_traffic: (optional) Deprecated, please use response
               headers instead and also provide "origin_traffic:false" to avoid legacy
               behaviour interacting with the response.headers property.
        """
        self.status = status
        self.headers_ = headers_
        self.origin_traffic = origin_traffic

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitObjectMatchResponse':
        """Initialize a RatelimitObjectMatchResponse object from a json dictionary."""
        args = {}
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'headers' in _dict:
            args['headers_'] = [RatelimitObjectMatchResponseHeadersItem.from_dict(x) for x in _dict.get('headers')]
        if 'origin_traffic' in _dict:
            args['origin_traffic'] = _dict.get('origin_traffic')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitObjectMatchResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'headers_') and self.headers_ is not None:
            _dict['headers'] = [x.to_dict() for x in self.headers_]
        if hasattr(self, 'origin_traffic') and self.origin_traffic is not None:
            _dict['origin_traffic'] = self.origin_traffic
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitObjectMatchResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitObjectMatchResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitObjectMatchResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RatelimitObjectMatchResponseHeadersItem():
    """
    RatelimitObjectMatchResponseHeadersItem.

    :attr str name: The name of the response header to match.
    :attr str op: The operator when matchin, eq means equals, ne means not equals.
    :attr str value: The value of the header, which will be exactly matched.
    """

    def __init__(self,
                 name: str,
                 op: str,
                 value: str) -> None:
        """
        Initialize a RatelimitObjectMatchResponseHeadersItem object.

        :param str name: The name of the response header to match.
        :param str op: The operator when matchin, eq means equals, ne means not
               equals.
        :param str value: The value of the header, which will be exactly matched.
        """
        self.name = name
        self.op = op
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitObjectMatchResponseHeadersItem':
        """Initialize a RatelimitObjectMatchResponseHeadersItem object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in RatelimitObjectMatchResponseHeadersItem JSON')
        if 'op' in _dict:
            args['op'] = _dict.get('op')
        else:
            raise ValueError('Required property \'op\' not present in RatelimitObjectMatchResponseHeadersItem JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in RatelimitObjectMatchResponseHeadersItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitObjectMatchResponseHeadersItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'op') and self.op is not None:
            _dict['op'] = self.op
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitObjectMatchResponseHeadersItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitObjectMatchResponseHeadersItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitObjectMatchResponseHeadersItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class OpEnum(str, Enum):
        """
        The operator when matchin, eq means equals, ne means not equals.
        """
        EQ = 'eq'
        NE = 'ne'


    class ValueEnum(str, Enum):
        """
        The value of the header, which will be exactly matched.
        """
        HIT = 'HIT'


class DeleteRateLimitResp():
    """
    rate limit delete response.

    :attr bool success: Operation success flag.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr DeleteRateLimitRespResult result: Container for response information.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'DeleteRateLimitRespResult') -> None:
        """
        Initialize a DeleteRateLimitResp object.

        :param bool success: Operation success flag.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param DeleteRateLimitRespResult result: Container for response
               information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteRateLimitResp':
        """Initialize a DeleteRateLimitResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in DeleteRateLimitResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in DeleteRateLimitResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in DeleteRateLimitResp JSON')
        if 'result' in _dict:
            args['result'] = DeleteRateLimitRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in DeleteRateLimitResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteRateLimitResp object from a json dictionary."""
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
        """Return a `str` version of this DeleteRateLimitResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteRateLimitResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteRateLimitResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListRatelimitResp():
    """
    rate limit list response.

    :attr bool success: Was operation successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr List[RatelimitObject] result: Container for response information.
    :attr ListRatelimitRespResultInfo result_info: Statistics of results.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: List['RatelimitObject'],
                 result_info: 'ListRatelimitRespResultInfo') -> None:
        """
        Initialize a ListRatelimitResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param List[RatelimitObject] result: Container for response information.
        :param ListRatelimitRespResultInfo result_info: Statistics of results.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result
        self.result_info = result_info

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListRatelimitResp':
        """Initialize a ListRatelimitResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in ListRatelimitResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in ListRatelimitResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in ListRatelimitResp JSON')
        if 'result' in _dict:
            args['result'] = [RatelimitObject.from_dict(x) for x in _dict.get('result')]
        else:
            raise ValueError('Required property \'result\' not present in ListRatelimitResp JSON')
        if 'result_info' in _dict:
            args['result_info'] = ListRatelimitRespResultInfo.from_dict(_dict.get('result_info'))
        else:
            raise ValueError('Required property \'result_info\' not present in ListRatelimitResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListRatelimitResp object from a json dictionary."""
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
        """Return a `str` version of this ListRatelimitResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListRatelimitResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListRatelimitResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RatelimitObject():
    """
    rate limit object.

    :attr str id: Identifier of the rate limit.
    :attr bool disabled: Whether this ratelimit is currently disabled.
    :attr str description: A note that you can use to describe the reason for a rate
          limit.
    :attr List[RatelimitObjectBypassItem] bypass: Criteria that would allow the rate
          limit to be bypassed, for example to express that you shouldn't apply a rate
          limit to a given set of URLs.
    :attr int threshold: The threshold that triggers the rate limit mitigations,
          combine with period. i.e. threshold per period.
    :attr int period: The time in seconds to count matching traffic. If the count
          exceeds threshold within this period the action will be performed.
    :attr RatelimitObjectCorrelate correlate: (optional) Enable NAT based rate
          limits.
    :attr RatelimitObjectAction action: action.
    :attr RatelimitObjectMatch match: Determines which traffic the rate limit counts
          towards the threshold. Needs to be one of "request" or "response" objects.
    """

    def __init__(self,
                 id: str,
                 disabled: bool,
                 description: str,
                 bypass: List['RatelimitObjectBypassItem'],
                 threshold: int,
                 period: int,
                 action: 'RatelimitObjectAction',
                 match: 'RatelimitObjectMatch',
                 *,
                 correlate: 'RatelimitObjectCorrelate' = None) -> None:
        """
        Initialize a RatelimitObject object.

        :param str id: Identifier of the rate limit.
        :param bool disabled: Whether this ratelimit is currently disabled.
        :param str description: A note that you can use to describe the reason for
               a rate limit.
        :param List[RatelimitObjectBypassItem] bypass: Criteria that would allow
               the rate limit to be bypassed, for example to express that you shouldn't
               apply a rate limit to a given set of URLs.
        :param int threshold: The threshold that triggers the rate limit
               mitigations, combine with period. i.e. threshold per period.
        :param int period: The time in seconds to count matching traffic. If the
               count exceeds threshold within this period the action will be performed.
        :param RatelimitObjectAction action: action.
        :param RatelimitObjectMatch match: Determines which traffic the rate limit
               counts towards the threshold. Needs to be one of "request" or "response"
               objects.
        :param RatelimitObjectCorrelate correlate: (optional) Enable NAT based rate
               limits.
        """
        self.id = id
        self.disabled = disabled
        self.description = description
        self.bypass = bypass
        self.threshold = threshold
        self.period = period
        self.correlate = correlate
        self.action = action
        self.match = match

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitObject':
        """Initialize a RatelimitObject object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in RatelimitObject JSON')
        if 'disabled' in _dict:
            args['disabled'] = _dict.get('disabled')
        else:
            raise ValueError('Required property \'disabled\' not present in RatelimitObject JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError('Required property \'description\' not present in RatelimitObject JSON')
        if 'bypass' in _dict:
            args['bypass'] = [RatelimitObjectBypassItem.from_dict(x) for x in _dict.get('bypass')]
        else:
            raise ValueError('Required property \'bypass\' not present in RatelimitObject JSON')
        if 'threshold' in _dict:
            args['threshold'] = _dict.get('threshold')
        else:
            raise ValueError('Required property \'threshold\' not present in RatelimitObject JSON')
        if 'period' in _dict:
            args['period'] = _dict.get('period')
        else:
            raise ValueError('Required property \'period\' not present in RatelimitObject JSON')
        if 'correlate' in _dict:
            args['correlate'] = RatelimitObjectCorrelate.from_dict(_dict.get('correlate'))
        if 'action' in _dict:
            args['action'] = RatelimitObjectAction.from_dict(_dict.get('action'))
        else:
            raise ValueError('Required property \'action\' not present in RatelimitObject JSON')
        if 'match' in _dict:
            args['match'] = RatelimitObjectMatch.from_dict(_dict.get('match'))
        else:
            raise ValueError('Required property \'match\' not present in RatelimitObject JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitObject object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'disabled') and self.disabled is not None:
            _dict['disabled'] = self.disabled
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'bypass') and self.bypass is not None:
            _dict['bypass'] = [x.to_dict() for x in self.bypass]
        if hasattr(self, 'threshold') and self.threshold is not None:
            _dict['threshold'] = self.threshold
        if hasattr(self, 'period') and self.period is not None:
            _dict['period'] = self.period
        if hasattr(self, 'correlate') and self.correlate is not None:
            _dict['correlate'] = self.correlate.to_dict()
        if hasattr(self, 'action') and self.action is not None:
            _dict['action'] = self.action.to_dict()
        if hasattr(self, 'match') and self.match is not None:
            _dict['match'] = self.match.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RatelimitObject object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitObject') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitObject') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RatelimitResp():
    """
    rate limit response.

    :attr bool success: Was operation successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr RatelimitObject result: rate limit object.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'RatelimitObject') -> None:
        """
        Initialize a RatelimitResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param RatelimitObject result: rate limit object.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RatelimitResp':
        """Initialize a RatelimitResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in RatelimitResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in RatelimitResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in RatelimitResp JSON')
        if 'result' in _dict:
            args['result'] = RatelimitObject.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in RatelimitResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RatelimitResp object from a json dictionary."""
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
        """Return a `str` version of this RatelimitResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RatelimitResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RatelimitResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
