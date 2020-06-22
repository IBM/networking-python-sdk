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
This document describes CIS Pagerule API.
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

class PageRuleApiV1(BaseService):
    """The Page Rule API V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'page_rule_api'

    @classmethod
    def new_instance(cls,
                     crn: str,
                     zone_id: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'PageRuleApiV1':
        """
        Return a new client for the Page Rule API service using the specified
               parameters and external configuration.

        :param str crn: instance id.

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
        Construct a new client for the Page Rule API service.

        :param str crn: instance id.

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
    # Page Rules
    #########################


    def get_page_rule(self, rule_id: str, **kwargs) -> DetailedResponse:
        """
        Get a page rule details.

        Get a page rule details.

        :param str rule_id: rule id.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PageRulesResponseWithoutResultInfo` object
        """

        if rule_id is None:
            raise ValueError('rule_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_page_rule')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/pagerules/{2}'.format(*self.encode_path_vars(self.crn, self.zone_id, rule_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def change_page_rule(self, rule_id: str, *, targets: List['PageRulesBodyTargetsItem'] = None, actions: List['PageRulesBodyActionsItem'] = None, priority: int = None, status: str = None, **kwargs) -> DetailedResponse:
        """
        Change a page rule.

        Change a page rule.

        :param str rule_id: rule id.
        :param List[PageRulesBodyTargetsItem] targets: (optional) targets.
        :param List[PageRulesBodyActionsItem] actions: (optional) actions.
        :param int priority: (optional) priority.
        :param str status: (optional) status.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PageRulesResponseWithoutResultInfo` object
        """

        if rule_id is None:
            raise ValueError('rule_id must be provided')
        if targets is not None:
            targets = [ convert_model(x) for x in targets ]
        if actions is not None:
            actions = [ convert_model(x) for x in actions ]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='change_page_rule')
        headers.update(sdk_headers)

        data = {
            'targets': targets,
            'actions': actions,
            'priority': priority,
            'status': status
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/pagerules/{2}'.format(*self.encode_path_vars(self.crn, self.zone_id, rule_id))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def update_page_rule(self, rule_id: str, *, targets: List['PageRulesBodyTargetsItem'] = None, actions: List['PageRulesBodyActionsItem'] = None, priority: int = None, status: str = None, **kwargs) -> DetailedResponse:
        """
        Update a page rule.

        Replace a page rule. The final rule will exactly match the data passed with this
        request.

        :param str rule_id: rule id.
        :param List[PageRulesBodyTargetsItem] targets: (optional) targets.
        :param List[PageRulesBodyActionsItem] actions: (optional) actions.
        :param int priority: (optional) priority.
        :param str status: (optional) status.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PageRulesResponseWithoutResultInfo` object
        """

        if rule_id is None:
            raise ValueError('rule_id must be provided')
        if targets is not None:
            targets = [ convert_model(x) for x in targets ]
        if actions is not None:
            actions = [ convert_model(x) for x in actions ]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_page_rule')
        headers.update(sdk_headers)

        data = {
            'targets': targets,
            'actions': actions,
            'priority': priority,
            'status': status
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/pagerules/{2}'.format(*self.encode_path_vars(self.crn, self.zone_id, rule_id))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_page_rule(self, rule_id: str, **kwargs) -> DetailedResponse:
        """
        Delete a page rule.

        Delete a page rule.

        :param str rule_id: rule id.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PageRulesDeleteResponse` object
        """

        if rule_id is None:
            raise ValueError('rule_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='delete_page_rule')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/pagerules/{2}'.format(*self.encode_path_vars(self.crn, self.zone_id, rule_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def list_page_rules(self, *, status: str = None, order: str = None, direction: str = None, match: str = None, **kwargs) -> DetailedResponse:
        """
        List page rules.

        List page rules.

        :param str status: (optional) default value: disabled. valid values:
               active, disabled.
        :param str order: (optional) default value: priority. valid values: status,
               priority.
        :param str direction: (optional) default value: desc. valid values: asc,
               desc.
        :param str match: (optional) default value: all. valid values: any, all.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PageRulesResponseListAll` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='list_page_rules')
        headers.update(sdk_headers)

        params = {
            'status': status,
            'order': order,
            'direction': direction,
            'match': match
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/pagerules'.format(*self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_page_rule(self, *, targets: List['PageRulesBodyTargetsItem'] = None, actions: List['PageRulesBodyActionsItem'] = None, priority: int = None, status: str = None, **kwargs) -> DetailedResponse:
        """
        Create a page rule.

        Create a page rule.

        :param List[PageRulesBodyTargetsItem] targets: (optional) targets.
        :param List[PageRulesBodyActionsItem] actions: (optional) actions.
        :param int priority: (optional) priority.
        :param str status: (optional) status.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PageRulesResponseWithoutResultInfo` object
        """

        if targets is not None:
            targets = [ convert_model(x) for x in targets ]
        if actions is not None:
            actions = [ convert_model(x) for x in actions ]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='create_page_rule')
        headers.update(sdk_headers)

        data = {
            'targets': targets,
            'actions': actions,
            'priority': priority,
            'status': status
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/pagerules'.format(*self.encode_path_vars(self.crn, self.zone_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

