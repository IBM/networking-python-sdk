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
This document describes CIS WAF Rule Groups API.
"""

from enum import Enum
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class WafRuleGroupsApiV1(BaseService):
    """The WAF Rule Groups API V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'waf_rule_groups_api'

    @classmethod
    def new_instance(cls,
                     crn: str,
                     zone_id: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'WafRuleGroupsApiV1':
        """
        Return a new client for the WAF Rule Groups API service using the specified
               parameters and external configuration.

        :param str crn: cloud resource name.

        :param str zone_id: Zone ID.
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
        Construct a new client for the WAF Rule Groups API service.

        :param str crn: cloud resource name.

        :param str zone_id: Zone ID.

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
    # List WAF Rule Groups
    #########################


    def list_waf_rule_groups(self, pkg_id: str, *, name: str = None, mode: str = None, rules_count: str = None, page: int = None, per_page: int = None, order: str = None, direction: str = None, match: str = None, **kwargs) -> DetailedResponse:
        """
        List all WAF rule groups contained within a package.

        List all WAF rule groups contained within a package.

        :param str pkg_id: Package ID.
        :param str name: (optional) Name of the firewall package.
        :param str mode: (optional) Whether or not the rules contained within this
               group are configurable/usable.
        :param str rules_count: (optional) How many rules are contained within this
               group.
        :param int page: (optional) Page number of paginated results.
        :param int per_page: (optional) Number of packages per page.
        :param str order: (optional) Field to order packages by.
        :param str direction: (optional) Direction to order packages.
        :param str match: (optional) Whether to match all search requirements or at
               least one (any).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `WafGroupsResponse` object
        """

        if pkg_id is None:
            raise ValueError('pkg_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='list_waf_rule_groups')
        headers.update(sdk_headers)

        params = {
            'name': name,
            'mode': mode,
            'rules_count': rules_count,
            'page': page,
            'per_page': per_page,
            'order': order,
            'direction': direction,
            'match': match
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/firewall/waf/packages/{2}/groups'.format(*self.encode_path_vars(self.crn, self.zone_id, pkg_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # Get single WAF rule group
    #########################


    def get_waf_rule_group(self, pkg_id: str, group_id: str, **kwargs) -> DetailedResponse:
        """
        Get a single WAF rule group.

        Get a single WAF rule group.

        :param str pkg_id: Package ID.
        :param str group_id: Group ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `WafGroupResponse` object
        """

        if pkg_id is None:
            raise ValueError('pkg_id must be provided')
        if group_id is None:
            raise ValueError('group_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_waf_rule_group')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/firewall/waf/packages/{2}/groups/{3}'.format(*self.encode_path_vars(self.crn, self.zone_id, pkg_id, group_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Update WAF rule group
    #########################


    def update_waf_rule_group(self, pkg_id: str, group_id: str, *, mode: str = None, **kwargs) -> DetailedResponse:
        """
        Update the state of a WAF rule group.

        Update the state of a WAF rule group.

        :param str pkg_id: Package ID.
        :param str group_id: Group ID.
        :param str mode: (optional) Whether or not the rules contained within this
               group are configurable/usable.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `WafGroupResponse` object
        """

        if pkg_id is None:
            raise ValueError('pkg_id must be provided')
        if group_id is None:
            raise ValueError('group_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_waf_rule_group')
        headers.update(sdk_headers)

        data = {
            'mode': mode
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/firewall/waf/packages/{2}/groups/{3}'.format(*self.encode_path_vars(self.crn, self.zone_id, pkg_id, group_id))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


class ListWafRuleGroupsEnums:
    """
    Enums for list_waf_rule_groups parameters.
    """

    class Mode(Enum):
        """
        Whether or not the rules contained within this group are configurable/usable.
        """
        TRUE = 'true'
        FALSE = 'false'
    class Direction(Enum):
        """
        Direction to order packages.
        """
        DESC = 'desc'
        ASC = 'asc'
    class Match(Enum):
        """
        Whether to match all search requirements or at least one (any).
        """
        ALL = 'all'
        ANY = 'any'

