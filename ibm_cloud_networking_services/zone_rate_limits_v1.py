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
    # List all rate limits
    #########################


    def list_all_zone_rate_limits(self, *, page: int = None, per_page: int = None, **kwargs) -> DetailedResponse:
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='list_all_zone_rate_limits')
        headers.update(sdk_headers)

        params = {
            'page': page,
            'per_page': per_page
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/rate_limits'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # Create a new rate limit
    #########################


    def create_zone_rate_limits(self, *, threshold: int = None, period: int = None, action: 'RatelimitInputAction' = None, match: 'RatelimitInputMatch' = None, disabled: bool = None, description: str = None, bypass: List['RatelimitInputBypassItem'] = None, correlate: 'RatelimitInputCorrelate' = None, **kwargs) -> DetailedResponse:
        """
        Create a new rate limit.

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
            bypass = [ convert_model(x) for x in bypass ]
        if correlate is not None:
            correlate = convert_model(correlate)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='create_zone_rate_limits')
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

        url = '/v1/{0}/zones/{1}/rate_limits'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Update a rate limit
    #########################


    def update_rate_limit(self, rate_limit_identifier: str, *, threshold: int = None, period: int = None, action: 'RatelimitInputAction' = None, match: 'RatelimitInputMatch' = None, disabled: bool = None, description: str = None, bypass: List['RatelimitInputBypassItem'] = None, correlate: 'RatelimitInputCorrelate' = None, **kwargs) -> DetailedResponse:
        """
        Update a rate limit.

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
            bypass = [ convert_model(x) for x in bypass ]
        if correlate is not None:
            correlate = convert_model(correlate)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_rate_limit')
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

        url = '/v1/{0}/zones/{1}/rate_limits/{2}'.format(*self.encode_path_vars(self.crn, self.zone_identifier, rate_limit_identifier))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Delete a rate limit
    #########################


    def delete_zone_rate_limit(self, rate_limit_identifier: str, **kwargs) -> DetailedResponse:
        """
        Delete a rate limit.

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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='delete_zone_rate_limit')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/rate_limits/{2}'.format(*self.encode_path_vars(self.crn, self.zone_identifier, rate_limit_identifier))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # getARateLimit
    #########################


    def get_rate_limit(self, rate_limit_identifier: str, **kwargs) -> DetailedResponse:
        """
        Get a rate limit's details by id.

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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_rate_limit')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/rate_limits/{2}'.format(*self.encode_path_vars(self.crn, self.zone_identifier, rate_limit_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

