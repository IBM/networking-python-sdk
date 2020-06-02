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
Zone Lockdown
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

class ZoneLockdownV1(BaseService):
    """The Zone Lockdown V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'zone_lockdown'

    @classmethod
    def new_instance(cls,
                     crn: str,
                     zone_identifier: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'ZoneLockdownV1':
        """
        Return a new client for the Zone Lockdown service using the specified
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
        Construct a new client for the Zone Lockdown service.

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
    # List all lockdown rules
    #########################


    def list_all_zone_lockown_rules(self, *, page: int = None, per_page: int = None, **kwargs) -> DetailedResponse:
        """
        List all lockdown rules for a zone.

        List all lockdown rules for a zone.

        :param int page: (optional) Page number of paginated results.
        :param int per_page: (optional) Maximum number of lockdown rules per page.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListLockdownResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='list_all_zone_lockown_rules')
        headers.update(sdk_headers)

        params = {
            'page': page,
            'per_page': per_page
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/firewall/lockdowns'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # Get an lockdown rule
    #########################


    def get_lockdown(self, lockdown_rule_identifier: str, **kwargs) -> DetailedResponse:
        """
        Get a lockdown rule's details by id.

        For a given service instance, zone id and lockdown rule id, get the lockdown rule
        details.

        :param str lockdown_rule_identifier: Identifier of lockdown rule for the
               given zone.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LockdownResp` object
        """

        if lockdown_rule_identifier is None:
            raise ValueError('lockdown_rule_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_lockdown')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/firewall/lockdowns/{2}'.format(*self.encode_path_vars(self.crn, self.zone_identifier, lockdown_rule_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Create a new lockdown rule
    #########################


    def create_zone_lockdown_rule(self, *, urls: List[str] = None, configurations: List['LockdownInputConfigurationsItem'] = None, id: str = None, paused: bool = None, description: str = None, **kwargs) -> DetailedResponse:
        """
        Create a new lockdown rule.

        Create a new lockdown rule for a given zone under a service instance.

        :param List[str] urls: (optional) URLs to be included in this rule
               definition. Wildcards are permitted. The URL pattern entered here will be
               escaped before use. This limits the URL to just simple wildcard patterns.
        :param List[LockdownInputConfigurationsItem] configurations: (optional)
               List of IP addresses or CIDR ranges to use for this rule. This can include
               any number of ip or ip_range configurations that can access the provided
               URLs.
        :param str id: (optional) Lockdown rule identifier.
        :param bool paused: (optional) Whether this zone lockdown is currently
               paused.
        :param str description: (optional) A note that you can use to describe the
               reason for a Lockdown rule.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LockdownResp` object
        """

        if configurations is not None:
            configurations = [ convert_model(x) for x in configurations ]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='create_zone_lockdown_rule')
        headers.update(sdk_headers)

        data = {
            'urls': urls,
            'configurations': configurations,
            'id': id,
            'paused': paused,
            'description': description
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/firewall/lockdowns'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Update a lockdown rule
    #########################


    def update_lockdown_rule(self, lockdown_rule_identifier: str, *, urls: List[str] = None, configurations: List['LockdownInputConfigurationsItem'] = None, id: str = None, paused: bool = None, description: str = None, **kwargs) -> DetailedResponse:
        """
        Update a lockdown rule.

        Update an existing lockdown rule for a given zone under a given service instance.

        :param str lockdown_rule_identifier: Identifier of lockdown rule.
        :param List[str] urls: (optional) URLs to be included in this rule
               definition. Wildcards are permitted. The URL pattern entered here will be
               escaped before use. This limits the URL to just simple wildcard patterns.
        :param List[LockdownInputConfigurationsItem] configurations: (optional)
               List of IP addresses or CIDR ranges to use for this rule. This can include
               any number of ip or ip_range configurations that can access the provided
               URLs.
        :param str id: (optional) Lockdown rule identifier.
        :param bool paused: (optional) Whether this zone lockdown is currently
               paused.
        :param str description: (optional) A note that you can use to describe the
               reason for a Lockdown rule.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LockdownResp` object
        """

        if lockdown_rule_identifier is None:
            raise ValueError('lockdown_rule_identifier must be provided')
        if configurations is not None:
            configurations = [ convert_model(x) for x in configurations ]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_lockdown_rule')
        headers.update(sdk_headers)

        data = {
            'urls': urls,
            'configurations': configurations,
            'id': id,
            'paused': paused,
            'description': description
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/firewall/lockdowns/{2}'.format(*self.encode_path_vars(self.crn, self.zone_identifier, lockdown_rule_identifier))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Delete a lockdown rule
    #########################


    def delete_zone_lockdown_rule(self, lockdown_rule_identifier: str, **kwargs) -> DetailedResponse:
        """
        Delete a lockdown rule.

        Delete a lockdown rule for a particular zone, given its id.

        :param str lockdown_rule_identifier: Identifier of the lockdown rule to be
               deleted.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteLockdownResp` object
        """

        if lockdown_rule_identifier is None:
            raise ValueError('lockdown_rule_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='delete_zone_lockdown_rule')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/firewall/lockdowns/{2}'.format(*self.encode_path_vars(self.crn, self.zone_identifier, lockdown_rule_identifier))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

