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
This document describes CIS WAF Rules API.
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

class WafRulesApiV1(BaseService):
    """The WAF Rules API V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'waf_rules_api'

    @classmethod
    def new_instance(cls,
                     crn: str,
                     zone_id: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'WafRulesApiV1':
        """
        Return a new client for the WAF Rules API service using the specified
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
        Construct a new client for the WAF Rules API service.

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
    # List WAF Rules
    #########################


    def list_waf_rules(self, package_id: str, *, mode: str = None, priority: float = None, match: str = None, order: str = None, group_id: str = None, description: str = None, direction: str = None, page: float = None, per_page: float = None, **kwargs) -> DetailedResponse:
        """
        List all WAF rules.

        List all Web Application Firewall (WAF) rules.

        :param str package_id: package id.
        :param str mode: (optional) The Rule Mode.
        :param float priority: (optional) The order in which the individual rule is
               executed within the related group.
        :param str match: (optional) Whether to match all search requirements or at
               least one. default value: all. valid values: any, all.
        :param str order: (optional) Field to order rules by. valid values:
               priority, group_id, description.
        :param str group_id: (optional) WAF group identifier tag. max length: 32;
               Read-only.
        :param str description: (optional) Public description of the rule.
        :param str direction: (optional) Direction to order rules. valid values:
               asc, desc.
        :param float page: (optional) Page number of paginated results. default
               value: 1; min value:1.
        :param float per_page: (optional) Number of rules per page. default value:
               50; min value:5; max value:100.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `WafRulesResponse` object
        """

        if package_id is None:
            raise ValueError('package_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='list_waf_rules')
        headers.update(sdk_headers)

        params = {
            'mode': mode,
            'priority': priority,
            'match': match,
            'order': order,
            'group_id': group_id,
            'description': description,
            'direction': direction,
            'page': page,
            'per_page': per_page
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/firewall/waf/packages/{2}/rules'.format(*self.encode_path_vars(self.crn, self.zone_id, package_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # Get WAF Rule
    #########################


    def get_waf_rule(self, package_id: str, identifier: str, **kwargs) -> DetailedResponse:
        """
        Get WAF Rule info.

        Get individual information about a rule.

        :param str package_id: package id.
        :param str identifier: rule identifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `WafRuleResponse` object
        """

        if package_id is None:
            raise ValueError('package_id must be provided')
        if identifier is None:
            raise ValueError('identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_waf_rule')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/firewall/waf/packages/{2}/rules/{3}'.format(*self.encode_path_vars(self.crn, self.zone_id, package_id, identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Update WAF Rule
    #########################


    def update_waf_rule(self, package_id: str, identifier: str, *, cis: 'WafRuleBodyCis' = None, owasp: 'WafRuleBodyOwasp' = None, **kwargs) -> DetailedResponse:
        """
        Update WAF rule.

        Update the action the rule will perform if triggered on the zone.

        :param str package_id: package id.
        :param str identifier: rule identifier.
        :param WafRuleBodyCis cis: (optional) cis package.
        :param WafRuleBodyOwasp owasp: (optional) owasp package.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `WafRuleResponse` object
        """

        if package_id is None:
            raise ValueError('package_id must be provided')
        if identifier is None:
            raise ValueError('identifier must be provided')
        if cis is not None:
            cis = convert_model(cis)
        if owasp is not None:
            owasp = convert_model(owasp)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_waf_rule')
        headers.update(sdk_headers)

        data = {
            'cis': cis,
            'owasp': owasp
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/firewall/waf/packages/{2}/rules/{3}'.format(*self.encode_path_vars(self.crn, self.zone_id, package_id, identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

