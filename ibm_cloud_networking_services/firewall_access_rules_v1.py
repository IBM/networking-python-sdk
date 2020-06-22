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
Instance Level Firewall Access Rules
"""

from datetime import datetime
from enum import Enum
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model, datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class FirewallAccessRulesV1(BaseService):
    """The Firewall Access Rules V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'firewall_access_rules'

    @classmethod
    def new_instance(cls,
                     crn: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'FirewallAccessRulesV1':
        """
        Return a new client for the Firewall Access Rules service using the
               specified parameters and external configuration.

        :param str crn: Full crn of the service instance.
        """
        if crn is None:
            raise ValueError('crn must be provided')

        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            crn,
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(self,
                 crn: str,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the Firewall Access Rules service.

        :param str crn: Full crn of the service instance.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        if crn is None:
            raise ValueError('crn must be provided')

        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)
        self.crn = crn


    #########################
    # Instance Level Firewall Access Rules
    #########################


    def list_all_account_access_rules(self, *, notes: str = None, mode: str = None, configuration_target: str = None, configuration_value: str = None, page: int = None, per_page: int = None, order: str = None, direction: str = None, match: str = None, **kwargs) -> DetailedResponse:
        """
        List all instance level firewall access rules.

        List all instance level firewall access rules.

        :param str notes: (optional) Search access rules by note.(Not case
               sensitive).
        :param str mode: (optional) Search access rules by mode.
        :param str configuration_target: (optional) Search access rules by
               configuration target.
        :param str configuration_value: (optional) Search access rules by
               configuration value which can be IP, IPrange, or country code.
        :param int page: (optional) Page number of paginated results.
        :param int per_page: (optional) Maximum number of access rules per page.
        :param str order: (optional) Field by which to order list of access rules.
        :param str direction: (optional) Direction in which to order results
               [ascending/descending order].
        :param str match: (optional) Whether to match all (all) or atleast one
               search parameter (any).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListAccountAccessRulesResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='list_all_account_access_rules')
        headers.update(sdk_headers)

        params = {
            'notes': notes,
            'mode': mode,
            'configuration.target': configuration_target,
            'configuration.value': configuration_value,
            'page': page,
            'per_page': per_page,
            'order': order,
            'direction': direction,
            'match': match
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/firewall/access_rules/rules'.format(*self.encode_path_vars(self.crn))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_account_access_rule(self, *, mode: str = None, notes: str = None, configuration: 'AccountAccessRuleInputConfiguration' = None, **kwargs) -> DetailedResponse:
        """
        Create an instance level firewall access rule.

        Create a new instance level firewall access rule for a given service instance.

        :param str mode: (optional) The action to apply to a matched request.
        :param str notes: (optional) A personal note about the rule. Typically used
               as a reminder or explanation for the rule.
        :param AccountAccessRuleInputConfiguration configuration: (optional)
               Configuration object specifying access rule.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AccountAccessRuleResp` object
        """

        if configuration is not None:
            configuration = convert_model(configuration)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='create_account_access_rule')
        headers.update(sdk_headers)

        data = {
            'mode': mode,
            'notes': notes,
            'configuration': configuration
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/firewall/access_rules/rules'.format(*self.encode_path_vars(self.crn))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_account_access_rule(self, accessrule_identifier: str, **kwargs) -> DetailedResponse:
        """
        Delete an instance level access rule.

        Delete an instance level access rule given its id.

        :param str accessrule_identifier: Identifier of the access rule to be
               deleted.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteAccountAccessRuleResp` object
        """

        if accessrule_identifier is None:
            raise ValueError('accessrule_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='delete_account_access_rule')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/firewall/access_rules/rules/{1}'.format(*self.encode_path_vars(self.crn, accessrule_identifier))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_account_access_rule(self, accessrule_identifier: str, **kwargs) -> DetailedResponse:
        """
        Get the details of an instance level.

        Get the details of an instance level firewall access rule for a given  service
        instance.

        :param str accessrule_identifier: Identifier of firewall access rule for
               the given zone.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AccountAccessRuleResp` object
        """

        if accessrule_identifier is None:
            raise ValueError('accessrule_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_account_access_rule')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/firewall/access_rules/rules/{1}'.format(*self.encode_path_vars(self.crn, accessrule_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_account_access_rule(self, accessrule_identifier: str, *, mode: str = None, notes: str = None, **kwargs) -> DetailedResponse:
        """
        Update an instance level firewall access rule.

        Update an existing instance level firewall access rule for a given service
        instance.

        :param str accessrule_identifier: Identifier of firewall access rule.
        :param str mode: (optional) The action to apply to a matched request.
        :param str notes: (optional) A personal note about the rule. Typically used
               as a reminder or explanation for the rule.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AccountAccessRuleResp` object
        """

        if accessrule_identifier is None:
            raise ValueError('accessrule_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_account_access_rule')
        headers.update(sdk_headers)

        data = {
            'mode': mode,
            'notes': notes
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/firewall/access_rules/rules/{1}'.format(*self.encode_path_vars(self.crn, accessrule_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


class ListAllAccountAccessRulesEnums:
    """
    Enums for list_all_account_access_rules parameters.
    """

    class Mode(Enum):
        """
        Search access rules by mode.
        """
        BLOCK = 'block'
        CHALLENGE = 'challenge'
        WHITELIST = 'whitelist'
        JS_CHALLENGE = 'js_challenge'
    class ConfigurationTarget(Enum):
        """
        Search access rules by configuration target.
        """
        IP = 'ip'
        IP_RANGE = 'ip_range'
        ASN = 'asn'
        COUNTRY = 'country'
    class Order(Enum):
        """
        Field by which to order list of access rules.
        """
        TARGET = 'target'
        VALUE = 'value'
        MODE = 'mode'
    class Direction(Enum):
        """
        Direction in which to order results [ascending/descending order].
        """
        ASC = 'asc'
        DESC = 'desc'
    class Match(Enum):
        """
        Whether to match all (all) or atleast one search parameter (any).
        """
        ANY = 'any'
        ALL = 'all'

