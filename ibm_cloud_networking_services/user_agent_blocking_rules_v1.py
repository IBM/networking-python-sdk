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
User-Agent Blocking Rules
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

class UserAgentBlockingRulesV1(BaseService):
    """The User-Agent Blocking Rules V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'user_agent_blocking_rules'

    @classmethod
    def new_instance(cls,
                     crn: str,
                     zone_identifier: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'UserAgentBlockingRulesV1':
        """
        Return a new client for the User-Agent Blocking Rules service using the
               specified parameters and external configuration.

        :param str crn: Full url-encoded cloud resource name (CRN) of resource
               instance.

        :param str zone_identifier: Zone identifier of the zone for which
               user-agent rule is created.
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
        Construct a new client for the User-Agent Blocking Rules service.

        :param str crn: Full url-encoded cloud resource name (CRN) of resource
               instance.

        :param str zone_identifier: Zone identifier of the zone for which
               user-agent rule is created.

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
    # User-Agent Blocking Rules
    #########################


    def list_all_zone_user_agent_rules(self, *, page: int = None, per_page: int = None, **kwargs) -> DetailedResponse:
        """
        List all user-agent blocking rules.

        List all user agent blocking rules.

        :param int page: (optional) Page number of paginated results.
        :param int per_page: (optional) Maximum number of user-agent rules per
               page.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListUseragentRulesResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='list_all_zone_user_agent_rules')
        headers.update(sdk_headers)

        params = {
            'page': page,
            'per_page': per_page
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/firewall/ua_rules'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_zone_user_agent_rule(self, *, mode: str = None, configuration: 'UseragentRuleInputConfiguration' = None, paused: bool = None, description: str = None, **kwargs) -> DetailedResponse:
        """
        Create a new user-agent blocking rule.

        Create a new user-agent blocking rule for a given zone under a service instance.

        :param str mode: (optional) The type of action to perform.
        :param UseragentRuleInputConfiguration configuration: (optional)
               Target/Value pair to use for this rule. The value is the exact UserAgent to
               match.
        :param bool paused: (optional) Whether this user-agent rule is currently
               disabled.
        :param str description: (optional) Some useful information about this rule
               to help identify the purpose of it.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `UseragentRuleResp` object
        """

        if configuration is not None:
            configuration = convert_model(configuration)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='create_zone_user_agent_rule')
        headers.update(sdk_headers)

        data = {
            'mode': mode,
            'configuration': configuration,
            'paused': paused,
            'description': description
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/firewall/ua_rules'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_zone_user_agent_rule(self, useragent_rule_identifier: str, **kwargs) -> DetailedResponse:
        """
        Delete a user-agent blocking rule.

        Delete a user-agent blocking rule for a particular zone, given its id.

        :param str useragent_rule_identifier: Identifier of the user-agent rule to
               be deleted.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteUseragentRuleResp` object
        """

        if useragent_rule_identifier is None:
            raise ValueError('useragent_rule_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='delete_zone_user_agent_rule')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/firewall/ua_rules/{2}'.format(*self.encode_path_vars(self.crn, self.zone_identifier, useragent_rule_identifier))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_user_agent_rule(self, useragent_rule_identifier: str, **kwargs) -> DetailedResponse:
        """
        Get a user-agent blocking rule's details by id.

        For a given service instance, zone id and user-agent rule id, get the user-agent
        blocking rule details.

        :param str useragent_rule_identifier: Identifier of user-agent blocking
               rule for the given zone.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `UseragentRuleResp` object
        """

        if useragent_rule_identifier is None:
            raise ValueError('useragent_rule_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_user_agent_rule')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/firewall/ua_rules/{2}'.format(*self.encode_path_vars(self.crn, self.zone_identifier, useragent_rule_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_user_agent_rule(self, useragent_rule_identifier: str, *, mode: str = None, configuration: 'UseragentRuleInputConfiguration' = None, paused: bool = None, description: str = None, **kwargs) -> DetailedResponse:
        """
        Update a user-agent blocking rule.

        Update an existing user-agent blocking rule for a given zone under a given service
        instance.

        :param str useragent_rule_identifier: Identifier of user-agent rule.
        :param str mode: (optional) The type of action to perform.
        :param UseragentRuleInputConfiguration configuration: (optional)
               Target/Value pair to use for this rule. The value is the exact UserAgent to
               match.
        :param bool paused: (optional) Whether this user-agent rule is currently
               disabled.
        :param str description: (optional) Some useful information about this rule
               to help identify the purpose of it.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `UseragentRuleResp` object
        """

        if useragent_rule_identifier is None:
            raise ValueError('useragent_rule_identifier must be provided')
        if configuration is not None:
            configuration = convert_model(configuration)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_user_agent_rule')
        headers.update(sdk_headers)

        data = {
            'mode': mode,
            'configuration': configuration,
            'paused': paused,
            'description': description
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/firewall/ua_rules/{2}'.format(*self.encode_path_vars(self.crn, self.zone_identifier, useragent_rule_identifier))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

