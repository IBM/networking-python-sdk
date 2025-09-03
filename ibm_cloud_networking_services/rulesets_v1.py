# coding: utf-8

# (C) Copyright IBM Corp. 2025.
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

# IBM OpenAPI SDK Code Generator Version: 3.106.0-09823488-20250707-071701

"""
Rulesets Engine

API Version: 1.0.1
"""

from enum import Enum
from typing import Dict, List, Optional
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################


class RulesetsV1(BaseService):
    """The Rulesets V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'rulesets'

    @classmethod
    def new_instance(
        cls,
        crn: str,
        zone_identifier: str,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'RulesetsV1':
        """
        Return a new client for the Rulesets service using the specified parameters
               and external configuration.

        :param str crn: Full url-encoded CRN of the service instance.

        :param str zone_identifier: zone identifier.
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

    def __init__(
        self,
        crn: str,
        zone_identifier: str,
        authenticator: Authenticator = None,
    ) -> None:
        """
        Construct a new client for the Rulesets service.

        :param str crn: Full url-encoded CRN of the service instance.

        :param str zone_identifier: zone identifier.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_identifier is None:
            raise ValueError('zone_identifier must be provided')

        BaseService.__init__(self, service_url=self.DEFAULT_SERVICE_URL, authenticator=authenticator)
        self.crn = crn
        self.zone_identifier = zone_identifier

    #########################
    # Instance Rulesets
    #########################

    def get_instance_rulesets(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        List Instance rulesets.

        List all rulesets at the instance level.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListRulesetsResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_instance_rulesets',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn']
        path_param_values = self.encode_path_vars(self.crn)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/rulesets'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_instance_ruleset(
        self,
        ruleset_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get an instance ruleset.

        View a specific instance ruleset.

        :param str ruleset_id: ID of a specific ruleset.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RulesetResp` object
        """

        if not ruleset_id:
            raise ValueError('ruleset_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_instance_ruleset',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'ruleset_id']
        path_param_values = self.encode_path_vars(self.crn, ruleset_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/rulesets/{ruleset_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_instance_ruleset(
        self,
        ruleset_id: str,
        *,
        description: Optional[str] = None,
        kind: Optional[str] = None,
        name: Optional[str] = None,
        phase: Optional[str] = None,
        rules: Optional[List['RuleCreate']] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update an instance ruleset.

        Update a specific instance ruleset.

        :param str ruleset_id: ID of a specific ruleset.
        :param str description: (optional) description of the ruleset.
        :param str kind: (optional)
        :param str name: (optional) human readable name of the ruleset.
        :param str phase: (optional) The phase of the ruleset.
        :param List[RuleCreate] rules: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RulesetResp` object
        """

        if not ruleset_id:
            raise ValueError('ruleset_id must be provided')
        if rules is not None:
            rules = [convert_model(x) for x in rules]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_instance_ruleset',
        )
        headers.update(sdk_headers)

        data = {
            'description': description,
            'kind': kind,
            'name': name,
            'phase': phase,
            'rules': rules,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'ruleset_id']
        path_param_values = self.encode_path_vars(self.crn, ruleset_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/rulesets/{ruleset_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_instance_ruleset(
        self,
        ruleset_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete an instance ruleset.

        Delete a specific instance ruleset.

        :param str ruleset_id: ID of a specific ruleset.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not ruleset_id:
            raise ValueError('ruleset_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_instance_ruleset',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['crn', 'ruleset_id']
        path_param_values = self.encode_path_vars(self.crn, ruleset_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/rulesets/{ruleset_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_instance_ruleset_versions(
        self,
        ruleset_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        List version of an instance ruleset.

        List all versions of a specific instance ruleset.

        :param str ruleset_id: ID of a specific ruleset.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListRulesetsResp` object
        """

        if not ruleset_id:
            raise ValueError('ruleset_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_instance_ruleset_versions',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'ruleset_id']
        path_param_values = self.encode_path_vars(self.crn, ruleset_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/rulesets/{ruleset_id}/versions'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_instance_ruleset_version(
        self,
        ruleset_id: str,
        ruleset_version: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a specific version of an instance ruleset.

        View a specific version of a specific instance ruleset.

        :param str ruleset_id: ID of a specific ruleset.
        :param str ruleset_version: The version of the ruleset.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RulesetResp` object
        """

        if not ruleset_id:
            raise ValueError('ruleset_id must be provided')
        if not ruleset_version:
            raise ValueError('ruleset_version must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_instance_ruleset_version',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'ruleset_id', 'ruleset_version']
        path_param_values = self.encode_path_vars(self.crn, ruleset_id, ruleset_version)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/rulesets/{ruleset_id}/versions/{ruleset_version}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_instance_ruleset_version(
        self,
        ruleset_id: str,
        ruleset_version: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a specific version of an instance ruleset.

        Delete a specific version of a specific instance ruleset.

        :param str ruleset_id: ID of a specific ruleset.
        :param str ruleset_version: The version of the ruleset.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not ruleset_id:
            raise ValueError('ruleset_id must be provided')
        if not ruleset_version:
            raise ValueError('ruleset_version must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_instance_ruleset_version',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['crn', 'ruleset_id', 'ruleset_version']
        path_param_values = self.encode_path_vars(self.crn, ruleset_id, ruleset_version)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/rulesets/{ruleset_id}/versions/{ruleset_version}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_instance_entrypoint_ruleset(
        self,
        ruleset_phase: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get an instance entrypoint ruleset.

        Get the instance ruleset for the given phase's entrypoint.

        :param str ruleset_phase: The phase of the ruleset.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RulesetResp` object
        """

        if not ruleset_phase:
            raise ValueError('ruleset_phase must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_instance_entrypoint_ruleset',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'ruleset_phase']
        path_param_values = self.encode_path_vars(self.crn, ruleset_phase)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/rulesets/phases/{ruleset_phase}/entrypoint'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_instance_entrypoint_ruleset(
        self,
        ruleset_phase: str,
        *,
        description: Optional[str] = None,
        kind: Optional[str] = None,
        name: Optional[str] = None,
        phase: Optional[str] = None,
        rules: Optional[List['RuleCreate']] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update an instance entrypoint ruleset.

        Updates the instance ruleset for the given phase's entry point.

        :param str ruleset_phase: The phase of the ruleset.
        :param str description: (optional) description of the ruleset.
        :param str kind: (optional)
        :param str name: (optional) human readable name of the ruleset.
        :param str phase: (optional) The phase of the ruleset.
        :param List[RuleCreate] rules: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RulesetResp` object
        """

        if not ruleset_phase:
            raise ValueError('ruleset_phase must be provided')
        if rules is not None:
            rules = [convert_model(x) for x in rules]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_instance_entrypoint_ruleset',
        )
        headers.update(sdk_headers)

        data = {
            'description': description,
            'kind': kind,
            'name': name,
            'phase': phase,
            'rules': rules,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'ruleset_phase']
        path_param_values = self.encode_path_vars(self.crn, ruleset_phase)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/rulesets/phases/{ruleset_phase}/entrypoint'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_instance_entry_point_ruleset_versions(
        self,
        ruleset_phase: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        List an instance entry point ruleset's versions.

        Lists the instance ruleset versions for the given phase's entry point.

        :param str ruleset_phase: The phase of the ruleset.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListRulesetsResp` object
        """

        if not ruleset_phase:
            raise ValueError('ruleset_phase must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_instance_entry_point_ruleset_versions',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'ruleset_phase']
        path_param_values = self.encode_path_vars(self.crn, ruleset_phase)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/rulesets/phases/{ruleset_phase}/entrypoint/versions'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_instance_entry_point_ruleset_version(
        self,
        ruleset_phase: str,
        ruleset_version: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get an instance entry point ruleset version.

        Fetches a specific version of an instance entry point ruleset.

        :param str ruleset_phase: The phase of the ruleset.
        :param str ruleset_version: The version of the ruleset.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RulesetResp` object
        """

        if not ruleset_phase:
            raise ValueError('ruleset_phase must be provided')
        if not ruleset_version:
            raise ValueError('ruleset_version must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_instance_entry_point_ruleset_version',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'ruleset_phase', 'ruleset_version']
        path_param_values = self.encode_path_vars(self.crn, ruleset_phase, ruleset_version)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/rulesets/phases/{ruleset_phase}/entrypoint/versions/{ruleset_version}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def create_instance_ruleset_rule(
        self,
        ruleset_id: str,
        *,
        action: Optional[str] = None,
        expression: Optional[str] = None,
        action_parameters: Optional['ActionParameters'] = None,
        ratelimit: Optional['Ratelimit'] = None,
        description: Optional[str] = None,
        enabled: Optional[bool] = None,
        id: Optional[str] = None,
        logging: Optional['Logging'] = None,
        ref: Optional[str] = None,
        position: Optional['Position'] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create an instance ruleset rule.

        Create an instance ruleset rule.

        :param str ruleset_id: ID of a specific ruleset.
        :param str action: (optional) What happens when theres a match for the rule
               expression.
        :param str expression: (optional) The expression defining which traffic
               will match the rule.
        :param ActionParameters action_parameters: (optional)
        :param Ratelimit ratelimit: (optional)
        :param str description: (optional)
        :param bool enabled: (optional)
        :param str id: (optional)
        :param Logging logging: (optional)
        :param str ref: (optional) The reference of the rule (the rule ID by
               default).
        :param Position position: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RulesetResp` object
        """

        if not ruleset_id:
            raise ValueError('ruleset_id must be provided')
        if action_parameters is not None:
            action_parameters = convert_model(action_parameters)
        if ratelimit is not None:
            ratelimit = convert_model(ratelimit)
        if logging is not None:
            logging = convert_model(logging)
        if position is not None:
            position = convert_model(position)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_instance_ruleset_rule',
        )
        headers.update(sdk_headers)

        data = {
            'action': action,
            'expression': expression,
            'action_parameters': action_parameters,
            'ratelimit': ratelimit,
            'description': description,
            'enabled': enabled,
            'id': id,
            'logging': logging,
            'ref': ref,
            'position': position,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'ruleset_id']
        path_param_values = self.encode_path_vars(self.crn, ruleset_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/rulesets/{ruleset_id}/rules'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def update_instance_ruleset_rule(
        self,
        ruleset_id: str,
        rule_id: str,
        *,
        action: Optional[str] = None,
        action_parameters: Optional['ActionParameters'] = None,
        ratelimit: Optional['Ratelimit'] = None,
        description: Optional[str] = None,
        enabled: Optional[bool] = None,
        expression: Optional[str] = None,
        id: Optional[str] = None,
        logging: Optional['Logging'] = None,
        ref: Optional[str] = None,
        position: Optional['Position'] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update an instance ruleset rule.

        Update an instance ruleset rule.

        :param str ruleset_id: ID of a specific ruleset.
        :param str rule_id: ID of a specific rule.
        :param str action: (optional) What happens when theres a match for the rule
               expression.
        :param ActionParameters action_parameters: (optional)
        :param Ratelimit ratelimit: (optional)
        :param str description: (optional)
        :param bool enabled: (optional)
        :param str expression: (optional) The expression defining which traffic
               will match the rule.
        :param str id: (optional)
        :param Logging logging: (optional)
        :param str ref: (optional) The reference of the rule (the rule ID by
               default).
        :param Position position: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RulesetResp` object
        """

        if not ruleset_id:
            raise ValueError('ruleset_id must be provided')
        if not rule_id:
            raise ValueError('rule_id must be provided')
        if action_parameters is not None:
            action_parameters = convert_model(action_parameters)
        if ratelimit is not None:
            ratelimit = convert_model(ratelimit)
        if logging is not None:
            logging = convert_model(logging)
        if position is not None:
            position = convert_model(position)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_instance_ruleset_rule',
        )
        headers.update(sdk_headers)

        data = {
            'action': action,
            'action_parameters': action_parameters,
            'ratelimit': ratelimit,
            'description': description,
            'enabled': enabled,
            'expression': expression,
            'id': id,
            'logging': logging,
            'ref': ref,
            'position': position,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'ruleset_id', 'rule_id']
        path_param_values = self.encode_path_vars(self.crn, ruleset_id, rule_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/rulesets/{ruleset_id}/rules/{rule_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_instance_ruleset_rule(
        self,
        ruleset_id: str,
        rule_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete an instance ruleset rule.

        Delete an instance ruleset rule.

        :param str ruleset_id: ID of a specific ruleset.
        :param str rule_id: ID of a specific rule.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RuleResp` object
        """

        if not ruleset_id:
            raise ValueError('ruleset_id must be provided')
        if not rule_id:
            raise ValueError('rule_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_instance_ruleset_rule',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'ruleset_id', 'rule_id']
        path_param_values = self.encode_path_vars(self.crn, ruleset_id, rule_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/rulesets/{ruleset_id}/rules/{rule_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_instance_ruleset_version_by_tag(
        self,
        ruleset_id: str,
        ruleset_version: str,
        rule_tag: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        List an instance ruleset verion's rules by tag.

        Lists rules by tag for a specific version of an instance ruleset.

        :param str ruleset_id: ID of a specific ruleset.
        :param str ruleset_version: The version of the ruleset.
        :param str rule_tag: A category of the rule.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RulesetResp` object
        """

        if not ruleset_id:
            raise ValueError('ruleset_id must be provided')
        if not ruleset_version:
            raise ValueError('ruleset_version must be provided')
        if not rule_tag:
            raise ValueError('rule_tag must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_instance_ruleset_version_by_tag',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'ruleset_id', 'ruleset_version', 'rule_tag']
        path_param_values = self.encode_path_vars(self.crn, ruleset_id, ruleset_version, rule_tag)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/rulesets/{ruleset_id}/versions/{ruleset_version}/by_tag/{rule_tag}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Zone Rulesets
    #########################

    def get_zone_rulesets(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        List zone rulesets.

        List all rulesets at the zone level.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListRulesetsResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_zone_rulesets',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/rulesets'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_zone_ruleset(
        self,
        ruleset_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a zone ruleset.

        View a specific zone ruleset.

        :param str ruleset_id: ID of a specific ruleset.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RulesetResp` object
        """

        if not ruleset_id:
            raise ValueError('ruleset_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_zone_ruleset',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'ruleset_id']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier, ruleset_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/rulesets/{ruleset_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_zone_ruleset(
        self,
        ruleset_id: str,
        *,
        description: Optional[str] = None,
        kind: Optional[str] = None,
        name: Optional[str] = None,
        phase: Optional[str] = None,
        rules: Optional[List['RuleCreate']] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a zone ruleset.

        Update a specific zone ruleset.

        :param str ruleset_id: ID of a specific ruleset.
        :param str description: (optional) description of the ruleset.
        :param str kind: (optional)
        :param str name: (optional) human readable name of the ruleset.
        :param str phase: (optional) The phase of the ruleset.
        :param List[RuleCreate] rules: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RulesetResp` object
        """

        if not ruleset_id:
            raise ValueError('ruleset_id must be provided')
        if rules is not None:
            rules = [convert_model(x) for x in rules]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_zone_ruleset',
        )
        headers.update(sdk_headers)

        data = {
            'description': description,
            'kind': kind,
            'name': name,
            'phase': phase,
            'rules': rules,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'ruleset_id']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier, ruleset_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/rulesets/{ruleset_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_zone_ruleset(
        self,
        ruleset_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a zone ruleset.

        Delete a specific zone ruleset.

        :param str ruleset_id: ID of a specific ruleset.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not ruleset_id:
            raise ValueError('ruleset_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_zone_ruleset',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['crn', 'zone_identifier', 'ruleset_id']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier, ruleset_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/rulesets/{ruleset_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_zone_ruleset_versions(
        self,
        ruleset_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        List version of a zone ruleset.

        List all versions of a specific zone ruleset.

        :param str ruleset_id: ID of a specific ruleset.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListRulesetsResp` object
        """

        if not ruleset_id:
            raise ValueError('ruleset_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_zone_ruleset_versions',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'ruleset_id']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier, ruleset_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/rulesets/{ruleset_id}/versions'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_zone_ruleset_version(
        self,
        ruleset_id: str,
        ruleset_version: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a specific version of a zone ruleset.

        View a specific version of a specific zone ruleset.

        :param str ruleset_id: ID of a specific ruleset.
        :param str ruleset_version: The version of the ruleset.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RulesetResp` object
        """

        if not ruleset_id:
            raise ValueError('ruleset_id must be provided')
        if not ruleset_version:
            raise ValueError('ruleset_version must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_zone_ruleset_version',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'ruleset_id', 'ruleset_version']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier, ruleset_id, ruleset_version)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/rulesets/{ruleset_id}/versions/{ruleset_version}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_zone_ruleset_version(
        self,
        ruleset_id: str,
        ruleset_version: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a specific version of a zone ruleset.

        Delete a specific version of a specific zone ruleset.

        :param str ruleset_id: ID of a specific ruleset.
        :param str ruleset_version: The version of the ruleset.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not ruleset_id:
            raise ValueError('ruleset_id must be provided')
        if not ruleset_version:
            raise ValueError('ruleset_version must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_zone_ruleset_version',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['crn', 'zone_identifier', 'ruleset_id', 'ruleset_version']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier, ruleset_id, ruleset_version)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/rulesets/{ruleset_id}/versions/{ruleset_version}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_zone_entrypoint_ruleset(
        self,
        ruleset_phase: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a zone entrypoint ruleset.

        Get the zone ruleset for the given phase's entrypoint.

        :param str ruleset_phase: The phase of the ruleset.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RulesetResp` object
        """

        if not ruleset_phase:
            raise ValueError('ruleset_phase must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_zone_entrypoint_ruleset',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'ruleset_phase']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier, ruleset_phase)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/rulesets/phases/{ruleset_phase}/entrypoint'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_zone_entrypoint_ruleset(
        self,
        ruleset_phase: str,
        *,
        description: Optional[str] = None,
        kind: Optional[str] = None,
        name: Optional[str] = None,
        phase: Optional[str] = None,
        rules: Optional[List['RuleCreate']] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a zone entrypoint ruleset.

        Updates the instance ruleset for the given phase's entry point.

        :param str ruleset_phase: The phase of the ruleset.
        :param str description: (optional) description of the ruleset.
        :param str kind: (optional)
        :param str name: (optional) human readable name of the ruleset.
        :param str phase: (optional) The phase of the ruleset.
        :param List[RuleCreate] rules: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RulesetResp` object
        """

        if not ruleset_phase:
            raise ValueError('ruleset_phase must be provided')
        if rules is not None:
            rules = [convert_model(x) for x in rules]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_zone_entrypoint_ruleset',
        )
        headers.update(sdk_headers)

        data = {
            'description': description,
            'kind': kind,
            'name': name,
            'phase': phase,
            'rules': rules,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'ruleset_phase']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier, ruleset_phase)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/rulesets/phases/{ruleset_phase}/entrypoint'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_zone_entry_point_ruleset_versions(
        self,
        ruleset_phase: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        List a zone entry point ruleset's versions.

        Lists the zone ruleset versions for the given phase's entry point.

        :param str ruleset_phase: The phase of the ruleset.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListRulesetsResp` object
        """

        if not ruleset_phase:
            raise ValueError('ruleset_phase must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_zone_entry_point_ruleset_versions',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'ruleset_phase']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier, ruleset_phase)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/rulesets/phases/{ruleset_phase}/entrypoint/versions'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_zone_entry_point_ruleset_version(
        self,
        ruleset_phase: str,
        ruleset_version: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get a zone entry point ruleset version.

        Fetches a specific version of a zone entry point ruleset.

        :param str ruleset_phase: The phase of the ruleset.
        :param str ruleset_version: The version of the ruleset.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RulesetResp` object
        """

        if not ruleset_phase:
            raise ValueError('ruleset_phase must be provided')
        if not ruleset_version:
            raise ValueError('ruleset_version must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_zone_entry_point_ruleset_version',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'ruleset_phase', 'ruleset_version']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier, ruleset_phase, ruleset_version)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/rulesets/phases/{ruleset_phase}/entrypoint/versions/{ruleset_version}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def create_zone_ruleset_rule(
        self,
        ruleset_id: str,
        *,
        action: Optional[str] = None,
        expression: Optional[str] = None,
        action_parameters: Optional['ActionParameters'] = None,
        ratelimit: Optional['Ratelimit'] = None,
        description: Optional[str] = None,
        enabled: Optional[bool] = None,
        id: Optional[str] = None,
        logging: Optional['Logging'] = None,
        ref: Optional[str] = None,
        position: Optional['Position'] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a zone ruleset rule.

        Create a zone ruleset rule.

        :param str ruleset_id: ID of a specific ruleset.
        :param str action: (optional) What happens when theres a match for the rule
               expression.
        :param str expression: (optional) The expression defining which traffic
               will match the rule.
        :param ActionParameters action_parameters: (optional)
        :param Ratelimit ratelimit: (optional)
        :param str description: (optional)
        :param bool enabled: (optional)
        :param str id: (optional)
        :param Logging logging: (optional)
        :param str ref: (optional) The reference of the rule (the rule ID by
               default).
        :param Position position: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RulesetResp` object
        """

        if not ruleset_id:
            raise ValueError('ruleset_id must be provided')
        if action_parameters is not None:
            action_parameters = convert_model(action_parameters)
        if ratelimit is not None:
            ratelimit = convert_model(ratelimit)
        if logging is not None:
            logging = convert_model(logging)
        if position is not None:
            position = convert_model(position)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_zone_ruleset_rule',
        )
        headers.update(sdk_headers)

        data = {
            'action': action,
            'expression': expression,
            'action_parameters': action_parameters,
            'ratelimit': ratelimit,
            'description': description,
            'enabled': enabled,
            'id': id,
            'logging': logging,
            'ref': ref,
            'position': position,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'ruleset_id']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier, ruleset_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/rulesets/{ruleset_id}/rules'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def update_zone_ruleset_rule(
        self,
        ruleset_id: str,
        rule_id: str,
        *,
        action: Optional[str] = None,
        action_parameters: Optional['ActionParameters'] = None,
        ratelimit: Optional['Ratelimit'] = None,
        description: Optional[str] = None,
        enabled: Optional[bool] = None,
        expression: Optional[str] = None,
        id: Optional[str] = None,
        logging: Optional['Logging'] = None,
        ref: Optional[str] = None,
        position: Optional['Position'] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a zone ruleset rule.

        Update a zone ruleset rule.

        :param str ruleset_id: ID of a specific ruleset.
        :param str rule_id: ID of a specific rule.
        :param str action: (optional) What happens when theres a match for the rule
               expression.
        :param ActionParameters action_parameters: (optional)
        :param Ratelimit ratelimit: (optional)
        :param str description: (optional)
        :param bool enabled: (optional)
        :param str expression: (optional) The expression defining which traffic
               will match the rule.
        :param str id: (optional)
        :param Logging logging: (optional)
        :param str ref: (optional) The reference of the rule (the rule ID by
               default).
        :param Position position: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RulesetResp` object
        """

        if not ruleset_id:
            raise ValueError('ruleset_id must be provided')
        if not rule_id:
            raise ValueError('rule_id must be provided')
        if action_parameters is not None:
            action_parameters = convert_model(action_parameters)
        if ratelimit is not None:
            ratelimit = convert_model(ratelimit)
        if logging is not None:
            logging = convert_model(logging)
        if position is not None:
            position = convert_model(position)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_zone_ruleset_rule',
        )
        headers.update(sdk_headers)

        data = {
            'action': action,
            'action_parameters': action_parameters,
            'ratelimit': ratelimit,
            'description': description,
            'enabled': enabled,
            'expression': expression,
            'id': id,
            'logging': logging,
            'ref': ref,
            'position': position,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'ruleset_id', 'rule_id']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier, ruleset_id, rule_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/rulesets/{ruleset_id}/rules/{rule_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PATCH',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_zone_ruleset_rule(
        self,
        ruleset_id: str,
        rule_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete a zone ruleset rule.

        Delete an instance ruleset rule.

        :param str ruleset_id: ID of a specific ruleset.
        :param str rule_id: ID of a specific rule.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RuleResp` object
        """

        if not ruleset_id:
            raise ValueError('ruleset_id must be provided')
        if not rule_id:
            raise ValueError('rule_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_zone_ruleset_rule',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'ruleset_id', 'rule_id']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier, ruleset_id, rule_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/rulesets/{ruleset_id}/rules/{rule_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response


class GetInstanceEntrypointRulesetEnums:
    """
    Enums for get_instance_entrypoint_ruleset parameters.
    """

    class RulesetPhase(str, Enum):
        """
        The phase of the ruleset.
        """

        DDOS_L4 = 'ddos_l4'
        DDOS_L7 = 'ddos_l7'
        HTTP_CONFIG_SETTINGS = 'http_config_settings'
        HTTP_CUSTOM_ERRORS = 'http_custom_errors'
        HTTP_LOG_CUSTOM_FIELDS = 'http_log_custom_fields'
        HTTP_RATELIMIT = 'http_ratelimit'
        HTTP_REQUEST_CACHE_SETTINGS = 'http_request_cache_settings'
        HTTP_REQUEST_DYNAMIC_REDIRECT = 'http_request_dynamic_redirect'
        HTTP_REQUEST_FIREWALL_CUSTOM = 'http_request_firewall_custom'
        HTTP_REQUEST_FIREWALL_MANAGED = 'http_request_firewall_managed'
        HTTP_REQUEST_LATE_TRANSFORM = 'http_request_late_transform'
        HTTP_REQUEST_ORIGIN = 'http_request_origin'
        HTTP_REQUEST_REDIRECT = 'http_request_redirect'
        HTTP_REQUEST_SANITIZE = 'http_request_sanitize'
        HTTP_REQUEST_SBFM = 'http_request_sbfm'
        HTTP_REQUEST_SELECT_CONFIGURATION = 'http_request_select_configuration'
        HTTP_REQUEST_TRANSFORM = 'http_request_transform'
        HTTP_RESPONSE_COMPRESSION = 'http_response_compression'
        HTTP_RESPONSE_FIREWALL_MANAGED = 'http_response_firewall_managed'
        HTTP_RESPONSE_HEADERS_TRANSFORM = 'http_response_headers_transform'


class UpdateInstanceEntrypointRulesetEnums:
    """
    Enums for update_instance_entrypoint_ruleset parameters.
    """

    class RulesetPhase(str, Enum):
        """
        The phase of the ruleset.
        """

        DDOS_L4 = 'ddos_l4'
        DDOS_L7 = 'ddos_l7'
        HTTP_CONFIG_SETTINGS = 'http_config_settings'
        HTTP_CUSTOM_ERRORS = 'http_custom_errors'
        HTTP_LOG_CUSTOM_FIELDS = 'http_log_custom_fields'
        HTTP_RATELIMIT = 'http_ratelimit'
        HTTP_REQUEST_CACHE_SETTINGS = 'http_request_cache_settings'
        HTTP_REQUEST_DYNAMIC_REDIRECT = 'http_request_dynamic_redirect'
        HTTP_REQUEST_FIREWALL_CUSTOM = 'http_request_firewall_custom'
        HTTP_REQUEST_FIREWALL_MANAGED = 'http_request_firewall_managed'
        HTTP_REQUEST_LATE_TRANSFORM = 'http_request_late_transform'
        HTTP_REQUEST_ORIGIN = 'http_request_origin'
        HTTP_REQUEST_REDIRECT = 'http_request_redirect'
        HTTP_REQUEST_SANITIZE = 'http_request_sanitize'
        HTTP_REQUEST_SBFM = 'http_request_sbfm'
        HTTP_REQUEST_SELECT_CONFIGURATION = 'http_request_select_configuration'
        HTTP_REQUEST_TRANSFORM = 'http_request_transform'
        HTTP_RESPONSE_COMPRESSION = 'http_response_compression'
        HTTP_RESPONSE_FIREWALL_MANAGED = 'http_response_firewall_managed'
        HTTP_RESPONSE_HEADERS_TRANSFORM = 'http_response_headers_transform'


class GetInstanceEntryPointRulesetVersionsEnums:
    """
    Enums for get_instance_entry_point_ruleset_versions parameters.
    """

    class RulesetPhase(str, Enum):
        """
        The phase of the ruleset.
        """

        DDOS_L4 = 'ddos_l4'
        DDOS_L7 = 'ddos_l7'
        HTTP_CONFIG_SETTINGS = 'http_config_settings'
        HTTP_CUSTOM_ERRORS = 'http_custom_errors'
        HTTP_LOG_CUSTOM_FIELDS = 'http_log_custom_fields'
        HTTP_RATELIMIT = 'http_ratelimit'
        HTTP_REQUEST_CACHE_SETTINGS = 'http_request_cache_settings'
        HTTP_REQUEST_DYNAMIC_REDIRECT = 'http_request_dynamic_redirect'
        HTTP_REQUEST_FIREWALL_CUSTOM = 'http_request_firewall_custom'
        HTTP_REQUEST_FIREWALL_MANAGED = 'http_request_firewall_managed'
        HTTP_REQUEST_LATE_TRANSFORM = 'http_request_late_transform'
        HTTP_REQUEST_ORIGIN = 'http_request_origin'
        HTTP_REQUEST_REDIRECT = 'http_request_redirect'
        HTTP_REQUEST_SANITIZE = 'http_request_sanitize'
        HTTP_REQUEST_SBFM = 'http_request_sbfm'
        HTTP_REQUEST_SELECT_CONFIGURATION = 'http_request_select_configuration'
        HTTP_REQUEST_TRANSFORM = 'http_request_transform'
        HTTP_RESPONSE_COMPRESSION = 'http_response_compression'
        HTTP_RESPONSE_FIREWALL_MANAGED = 'http_response_firewall_managed'
        HTTP_RESPONSE_HEADERS_TRANSFORM = 'http_response_headers_transform'


class GetInstanceEntryPointRulesetVersionEnums:
    """
    Enums for get_instance_entry_point_ruleset_version parameters.
    """

    class RulesetPhase(str, Enum):
        """
        The phase of the ruleset.
        """

        DDOS_L4 = 'ddos_l4'
        DDOS_L7 = 'ddos_l7'
        HTTP_CONFIG_SETTINGS = 'http_config_settings'
        HTTP_CUSTOM_ERRORS = 'http_custom_errors'
        HTTP_LOG_CUSTOM_FIELDS = 'http_log_custom_fields'
        HTTP_RATELIMIT = 'http_ratelimit'
        HTTP_REQUEST_CACHE_SETTINGS = 'http_request_cache_settings'
        HTTP_REQUEST_DYNAMIC_REDIRECT = 'http_request_dynamic_redirect'
        HTTP_REQUEST_FIREWALL_CUSTOM = 'http_request_firewall_custom'
        HTTP_REQUEST_FIREWALL_MANAGED = 'http_request_firewall_managed'
        HTTP_REQUEST_LATE_TRANSFORM = 'http_request_late_transform'
        HTTP_REQUEST_ORIGIN = 'http_request_origin'
        HTTP_REQUEST_REDIRECT = 'http_request_redirect'
        HTTP_REQUEST_SANITIZE = 'http_request_sanitize'
        HTTP_REQUEST_SBFM = 'http_request_sbfm'
        HTTP_REQUEST_SELECT_CONFIGURATION = 'http_request_select_configuration'
        HTTP_REQUEST_TRANSFORM = 'http_request_transform'
        HTTP_RESPONSE_COMPRESSION = 'http_response_compression'
        HTTP_RESPONSE_FIREWALL_MANAGED = 'http_response_firewall_managed'
        HTTP_RESPONSE_HEADERS_TRANSFORM = 'http_response_headers_transform'


class GetZoneEntrypointRulesetEnums:
    """
    Enums for get_zone_entrypoint_ruleset parameters.
    """

    class RulesetPhase(str, Enum):
        """
        The phase of the ruleset.
        """

        DDOS_L4 = 'ddos_l4'
        DDOS_L7 = 'ddos_l7'
        HTTP_CONFIG_SETTINGS = 'http_config_settings'
        HTTP_CUSTOM_ERRORS = 'http_custom_errors'
        HTTP_LOG_CUSTOM_FIELDS = 'http_log_custom_fields'
        HTTP_RATELIMIT = 'http_ratelimit'
        HTTP_REQUEST_CACHE_SETTINGS = 'http_request_cache_settings'
        HTTP_REQUEST_DYNAMIC_REDIRECT = 'http_request_dynamic_redirect'
        HTTP_REQUEST_FIREWALL_CUSTOM = 'http_request_firewall_custom'
        HTTP_REQUEST_FIREWALL_MANAGED = 'http_request_firewall_managed'
        HTTP_REQUEST_LATE_TRANSFORM = 'http_request_late_transform'
        HTTP_REQUEST_ORIGIN = 'http_request_origin'
        HTTP_REQUEST_REDIRECT = 'http_request_redirect'
        HTTP_REQUEST_SANITIZE = 'http_request_sanitize'
        HTTP_REQUEST_SBFM = 'http_request_sbfm'
        HTTP_REQUEST_SELECT_CONFIGURATION = 'http_request_select_configuration'
        HTTP_REQUEST_TRANSFORM = 'http_request_transform'
        HTTP_RESPONSE_COMPRESSION = 'http_response_compression'
        HTTP_RESPONSE_FIREWALL_MANAGED = 'http_response_firewall_managed'
        HTTP_RESPONSE_HEADERS_TRANSFORM = 'http_response_headers_transform'


class UpdateZoneEntrypointRulesetEnums:
    """
    Enums for update_zone_entrypoint_ruleset parameters.
    """

    class RulesetPhase(str, Enum):
        """
        The phase of the ruleset.
        """

        DDOS_L4 = 'ddos_l4'
        DDOS_L7 = 'ddos_l7'
        HTTP_CONFIG_SETTINGS = 'http_config_settings'
        HTTP_CUSTOM_ERRORS = 'http_custom_errors'
        HTTP_LOG_CUSTOM_FIELDS = 'http_log_custom_fields'
        HTTP_RATELIMIT = 'http_ratelimit'
        HTTP_REQUEST_CACHE_SETTINGS = 'http_request_cache_settings'
        HTTP_REQUEST_DYNAMIC_REDIRECT = 'http_request_dynamic_redirect'
        HTTP_REQUEST_FIREWALL_CUSTOM = 'http_request_firewall_custom'
        HTTP_REQUEST_FIREWALL_MANAGED = 'http_request_firewall_managed'
        HTTP_REQUEST_LATE_TRANSFORM = 'http_request_late_transform'
        HTTP_REQUEST_ORIGIN = 'http_request_origin'
        HTTP_REQUEST_REDIRECT = 'http_request_redirect'
        HTTP_REQUEST_SANITIZE = 'http_request_sanitize'
        HTTP_REQUEST_SBFM = 'http_request_sbfm'
        HTTP_REQUEST_SELECT_CONFIGURATION = 'http_request_select_configuration'
        HTTP_REQUEST_TRANSFORM = 'http_request_transform'
        HTTP_RESPONSE_COMPRESSION = 'http_response_compression'
        HTTP_RESPONSE_FIREWALL_MANAGED = 'http_response_firewall_managed'
        HTTP_RESPONSE_HEADERS_TRANSFORM = 'http_response_headers_transform'


class GetZoneEntryPointRulesetVersionsEnums:
    """
    Enums for get_zone_entry_point_ruleset_versions parameters.
    """

    class RulesetPhase(str, Enum):
        """
        The phase of the ruleset.
        """

        DDOS_L4 = 'ddos_l4'
        DDOS_L7 = 'ddos_l7'
        HTTP_CONFIG_SETTINGS = 'http_config_settings'
        HTTP_CUSTOM_ERRORS = 'http_custom_errors'
        HTTP_LOG_CUSTOM_FIELDS = 'http_log_custom_fields'
        HTTP_RATELIMIT = 'http_ratelimit'
        HTTP_REQUEST_CACHE_SETTINGS = 'http_request_cache_settings'
        HTTP_REQUEST_DYNAMIC_REDIRECT = 'http_request_dynamic_redirect'
        HTTP_REQUEST_FIREWALL_CUSTOM = 'http_request_firewall_custom'
        HTTP_REQUEST_FIREWALL_MANAGED = 'http_request_firewall_managed'
        HTTP_REQUEST_LATE_TRANSFORM = 'http_request_late_transform'
        HTTP_REQUEST_ORIGIN = 'http_request_origin'
        HTTP_REQUEST_REDIRECT = 'http_request_redirect'
        HTTP_REQUEST_SANITIZE = 'http_request_sanitize'
        HTTP_REQUEST_SBFM = 'http_request_sbfm'
        HTTP_REQUEST_SELECT_CONFIGURATION = 'http_request_select_configuration'
        HTTP_REQUEST_TRANSFORM = 'http_request_transform'
        HTTP_RESPONSE_COMPRESSION = 'http_response_compression'
        HTTP_RESPONSE_FIREWALL_MANAGED = 'http_response_firewall_managed'
        HTTP_RESPONSE_HEADERS_TRANSFORM = 'http_response_headers_transform'


class GetZoneEntryPointRulesetVersionEnums:
    """
    Enums for get_zone_entry_point_ruleset_version parameters.
    """

    class RulesetPhase(str, Enum):
        """
        The phase of the ruleset.
        """

        DDOS_L4 = 'ddos_l4'
        DDOS_L7 = 'ddos_l7'
        HTTP_CONFIG_SETTINGS = 'http_config_settings'
        HTTP_CUSTOM_ERRORS = 'http_custom_errors'
        HTTP_LOG_CUSTOM_FIELDS = 'http_log_custom_fields'
        HTTP_RATELIMIT = 'http_ratelimit'
        HTTP_REQUEST_CACHE_SETTINGS = 'http_request_cache_settings'
        HTTP_REQUEST_DYNAMIC_REDIRECT = 'http_request_dynamic_redirect'
        HTTP_REQUEST_FIREWALL_CUSTOM = 'http_request_firewall_custom'
        HTTP_REQUEST_FIREWALL_MANAGED = 'http_request_firewall_managed'
        HTTP_REQUEST_LATE_TRANSFORM = 'http_request_late_transform'
        HTTP_REQUEST_ORIGIN = 'http_request_origin'
        HTTP_REQUEST_REDIRECT = 'http_request_redirect'
        HTTP_REQUEST_SANITIZE = 'http_request_sanitize'
        HTTP_REQUEST_SBFM = 'http_request_sbfm'
        HTTP_REQUEST_SELECT_CONFIGURATION = 'http_request_select_configuration'
        HTTP_REQUEST_TRANSFORM = 'http_request_transform'
        HTTP_RESPONSE_COMPRESSION = 'http_response_compression'
        HTTP_RESPONSE_FIREWALL_MANAGED = 'http_response_firewall_managed'
        HTTP_RESPONSE_HEADERS_TRANSFORM = 'http_response_headers_transform'


##############################################################################
# Models
##############################################################################


class ActionParametersResponse:
    """
    ActionParametersResponse.

    :param str content: the content to return.
    :param str content_type:
    :param int status_code: The status code to return.
    """

    def __init__(
        self,
        content: str,
        content_type: str,
        status_code: int,
    ) -> None:
        """
        Initialize a ActionParametersResponse object.

        :param str content: the content to return.
        :param str content_type:
        :param int status_code: The status code to return.
        """
        self.content = content
        self.content_type = content_type
        self.status_code = status_code

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ActionParametersResponse':
        """Initialize a ActionParametersResponse object from a json dictionary."""
        args = {}
        content = _dict.get('content')
        if content is not None:
            args['content'] = content
        else:
            raise ValueError('Required property \'content\' not present in ActionParametersResponse JSON')
        content_type = _dict.get('content_type')
        if content_type is not None:
            args['content_type'] = content_type
        else:
            raise ValueError('Required property \'content_type\' not present in ActionParametersResponse JSON')
        status_code = _dict.get('status_code')
        if status_code is not None:
            args['status_code'] = status_code
        else:
            raise ValueError('Required property \'status_code\' not present in ActionParametersResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ActionParametersResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'content') and self.content is not None:
            _dict['content'] = self.content
        if hasattr(self, 'content_type') and self.content_type is not None:
            _dict['content_type'] = self.content_type
        if hasattr(self, 'status_code') and self.status_code is not None:
            _dict['status_code'] = self.status_code
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ActionParametersResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ActionParametersResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ActionParametersResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MessageSource:
    """
    The source of this message.

    :param str pointer: A JSON pointer to the field that is the source of the
          message.
    """

    def __init__(
        self,
        pointer: str,
    ) -> None:
        """
        Initialize a MessageSource object.

        :param str pointer: A JSON pointer to the field that is the source of the
               message.
        """
        self.pointer = pointer

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MessageSource':
        """Initialize a MessageSource object from a json dictionary."""
        args = {}
        pointer = _dict.get('pointer')
        if pointer is not None:
            args['pointer'] = pointer
        else:
            raise ValueError('Required property \'pointer\' not present in MessageSource JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageSource object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'pointer') and self.pointer is not None:
            _dict['pointer'] = self.pointer
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MessageSource object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MessageSource') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MessageSource') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ActionParameters:
    """
    ActionParameters.

    :param str id: (optional) unique ID of the ruleset.
    :param Overrides overrides: (optional)
    :param str version: (optional) The version of the ruleset. Use "latest" to get
          the latest version.
    :param str ruleset: (optional) Ruleset ID of the ruleset to apply action to. Use
          "current" to apply to the current ruleset.
    :param List[str] rulesets: (optional) List of ruleset ids to apply action to.
          Use "current" to apply to the current ruleset.
    :param List[str] phases: (optional) Skips the execution of one or more phases.
    :param List[str] products: (optional) Skips specific security products that are
          not based on the Ruleset Engine.
    :param ActionParametersResponse response: (optional)
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        overrides: Optional['Overrides'] = None,
        version: Optional[str] = None,
        ruleset: Optional[str] = None,
        rulesets: Optional[List[str]] = None,
        phases: Optional[List[str]] = None,
        products: Optional[List[str]] = None,
        response: Optional['ActionParametersResponse'] = None,
    ) -> None:
        """
        Initialize a ActionParameters object.

        :param str id: (optional) unique ID of the ruleset.
        :param Overrides overrides: (optional)
        :param str version: (optional) The version of the ruleset. Use "latest" to
               get the latest version.
        :param str ruleset: (optional) Ruleset ID of the ruleset to apply action
               to. Use "current" to apply to the current ruleset.
        :param List[str] rulesets: (optional) List of ruleset ids to apply action
               to. Use "current" to apply to the current ruleset.
        :param List[str] phases: (optional) Skips the execution of one or more
               phases.
        :param List[str] products: (optional) Skips specific security products that
               are not based on the Ruleset Engine.
        :param ActionParametersResponse response: (optional)
        """
        self.id = id
        self.overrides = overrides
        self.version = version
        self.ruleset = ruleset
        self.rulesets = rulesets
        self.phases = phases
        self.products = products
        self.response = response

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ActionParameters':
        """Initialize a ActionParameters object from a json dictionary."""
        args = {}
        id = _dict.get('id')
        if id is not None:
            args['id'] = id
        overrides = _dict.get('overrides')
        if overrides is not None:
            args['overrides'] = Overrides.from_dict(overrides)
        version = _dict.get('version')
        if version is not None:
            args['version'] = version
        ruleset = _dict.get('ruleset')
        if ruleset is not None:
            args['ruleset'] = ruleset
        rulesets = _dict.get('rulesets')
        if rulesets is not None:
            args['rulesets'] = rulesets
        phases = _dict.get('phases')
        if phases is not None:
            args['phases'] = phases
        products = _dict.get('products')
        if products is not None:
            args['products'] = products
        response = _dict.get('response')
        if response is not None:
            args['response'] = ActionParametersResponse.from_dict(response)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ActionParameters object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'overrides') and self.overrides is not None:
            if isinstance(self.overrides, dict):
                _dict['overrides'] = self.overrides
            else:
                _dict['overrides'] = self.overrides.to_dict()
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'ruleset') and self.ruleset is not None:
            _dict['ruleset'] = self.ruleset
        if hasattr(self, 'rulesets') and self.rulesets is not None:
            _dict['rulesets'] = self.rulesets
        if hasattr(self, 'phases') and self.phases is not None:
            _dict['phases'] = self.phases
        if hasattr(self, 'products') and self.products is not None:
            _dict['products'] = self.products
        if hasattr(self, 'response') and self.response is not None:
            if isinstance(self.response, dict):
                _dict['response'] = self.response
            else:
                _dict['response'] = self.response.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ActionParameters object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ActionParameters') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ActionParameters') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CategoriesOverride:
    """
    CategoriesOverride.

    :param str category: (optional) The category tag name to override.
    :param bool enabled: (optional)
    :param str action: (optional) What happens when theres a match for the rule
          expression.
    """

    def __init__(
        self,
        *,
        category: Optional[str] = None,
        enabled: Optional[bool] = None,
        action: Optional[str] = None,
    ) -> None:
        """
        Initialize a CategoriesOverride object.

        :param str category: (optional) The category tag name to override.
        :param bool enabled: (optional)
        :param str action: (optional) What happens when theres a match for the rule
               expression.
        """
        self.category = category
        self.enabled = enabled
        self.action = action

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CategoriesOverride':
        """Initialize a CategoriesOverride object from a json dictionary."""
        args = {}
        category = _dict.get('category')
        if category is not None:
            args['category'] = category
        enabled = _dict.get('enabled')
        if enabled is not None:
            args['enabled'] = enabled
        action = _dict.get('action')
        if action is not None:
            args['action'] = action
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CategoriesOverride object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'category') and self.category is not None:
            _dict['category'] = self.category
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'action') and self.action is not None:
            _dict['action'] = self.action
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CategoriesOverride object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CategoriesOverride') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CategoriesOverride') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListRulesetsResp:
    """
    List rulesets response.

    :param bool success: Was operation successful.
    :param List[Message] errors: Array of errors encountered.
    :param List[Message] messages: Array of messages returned.
    :param List[ListedRuleset] result: Container for response information.
    """

    def __init__(
        self,
        success: bool,
        errors: List['Message'],
        messages: List['Message'],
        result: List['ListedRuleset'],
    ) -> None:
        """
        Initialize a ListRulesetsResp object.

        :param bool success: Was operation successful.
        :param List[Message] errors: Array of errors encountered.
        :param List[Message] messages: Array of messages returned.
        :param List[ListedRuleset] result: Container for response information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListRulesetsResp':
        """Initialize a ListRulesetsResp object from a json dictionary."""
        args = {}
        success = _dict.get('success')
        if success is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in ListRulesetsResp JSON')
        errors = _dict.get('errors')
        if errors is not None:
            args['errors'] = [Message.from_dict(v) for v in errors]
        else:
            raise ValueError('Required property \'errors\' not present in ListRulesetsResp JSON')
        messages = _dict.get('messages')
        if messages is not None:
            args['messages'] = [Message.from_dict(v) for v in messages]
        else:
            raise ValueError('Required property \'messages\' not present in ListRulesetsResp JSON')
        result = _dict.get('result')
        if result is not None:
            args['result'] = [ListedRuleset.from_dict(v) for v in result]
        else:
            raise ValueError('Required property \'result\' not present in ListRulesetsResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListRulesetsResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            errors_list = []
            for v in self.errors:
                if isinstance(v, dict):
                    errors_list.append(v)
                else:
                    errors_list.append(v.to_dict())
            _dict['errors'] = errors_list
        if hasattr(self, 'messages') and self.messages is not None:
            messages_list = []
            for v in self.messages:
                if isinstance(v, dict):
                    messages_list.append(v)
                else:
                    messages_list.append(v.to_dict())
            _dict['messages'] = messages_list
        if hasattr(self, 'result') and self.result is not None:
            result_list = []
            for v in self.result:
                if isinstance(v, dict):
                    result_list.append(v)
                else:
                    result_list.append(v.to_dict())
            _dict['result'] = result_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListRulesetsResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListRulesetsResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListRulesetsResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListedRuleset:
    """
    ListedRuleset.

    :param str description: description of the ruleset.
    :param str id: unique ID of the ruleset.
    :param str kind:
    :param str last_updated: The timestamp of when the resource was last modified.
    :param str name: human readable name of the ruleset.
    :param str phase: The phase of the ruleset.
    :param str version: The version of the ruleset.
    """

    def __init__(
        self,
        description: str,
        id: str,
        kind: str,
        last_updated: str,
        name: str,
        phase: str,
        version: str,
    ) -> None:
        """
        Initialize a ListedRuleset object.

        :param str description: description of the ruleset.
        :param str id: unique ID of the ruleset.
        :param str kind:
        :param str last_updated: The timestamp of when the resource was last
               modified.
        :param str name: human readable name of the ruleset.
        :param str phase: The phase of the ruleset.
        :param str version: The version of the ruleset.
        """
        self.description = description
        self.id = id
        self.kind = kind
        self.last_updated = last_updated
        self.name = name
        self.phase = phase
        self.version = version

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListedRuleset':
        """Initialize a ListedRuleset object from a json dictionary."""
        args = {}
        description = _dict.get('description')
        if description is not None:
            args['description'] = description
        else:
            raise ValueError('Required property \'description\' not present in ListedRuleset JSON')
        id = _dict.get('id')
        if id is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in ListedRuleset JSON')
        kind = _dict.get('kind')
        if kind is not None:
            args['kind'] = kind
        else:
            raise ValueError('Required property \'kind\' not present in ListedRuleset JSON')
        last_updated = _dict.get('last_updated')
        if last_updated is not None:
            args['last_updated'] = last_updated
        else:
            raise ValueError('Required property \'last_updated\' not present in ListedRuleset JSON')
        name = _dict.get('name')
        if name is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in ListedRuleset JSON')
        phase = _dict.get('phase')
        if phase is not None:
            args['phase'] = phase
        else:
            raise ValueError('Required property \'phase\' not present in ListedRuleset JSON')
        version = _dict.get('version')
        if version is not None:
            args['version'] = version
        else:
            raise ValueError('Required property \'version\' not present in ListedRuleset JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListedRuleset object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'kind') and self.kind is not None:
            _dict['kind'] = self.kind
        if hasattr(self, 'last_updated') and self.last_updated is not None:
            _dict['last_updated'] = self.last_updated
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'phase') and self.phase is not None:
            _dict['phase'] = self.phase
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListedRuleset object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListedRuleset') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListedRuleset') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class KindEnum(str, Enum):
        """
        kind.
        """

        MANAGED = 'managed'
        CUSTOM = 'custom'
        ROOT = 'root'
        ZONE = 'zone'


    class PhaseEnum(str, Enum):
        """
        The phase of the ruleset.
        """

        DDOS_L4 = 'ddos_l4'
        DDOS_L7 = 'ddos_l7'
        HTTP_CONFIG_SETTINGS = 'http_config_settings'
        HTTP_CUSTOM_ERRORS = 'http_custom_errors'
        HTTP_LOG_CUSTOM_FIELDS = 'http_log_custom_fields'
        HTTP_RATELIMIT = 'http_ratelimit'
        HTTP_REQUEST_CACHE_SETTINGS = 'http_request_cache_settings'
        HTTP_REQUEST_DYNAMIC_REDIRECT = 'http_request_dynamic_redirect'
        HTTP_REQUEST_FIREWALL_CUSTOM = 'http_request_firewall_custom'
        HTTP_REQUEST_FIREWALL_MANAGED = 'http_request_firewall_managed'
        HTTP_REQUEST_LATE_TRANSFORM = 'http_request_late_transform'
        HTTP_REQUEST_ORIGIN = 'http_request_origin'
        HTTP_REQUEST_REDIRECT = 'http_request_redirect'
        HTTP_REQUEST_SANITIZE = 'http_request_sanitize'
        HTTP_REQUEST_SBFM = 'http_request_sbfm'
        HTTP_REQUEST_SELECT_CONFIGURATION = 'http_request_select_configuration'
        HTTP_REQUEST_TRANSFORM = 'http_request_transform'
        HTTP_RESPONSE_COMPRESSION = 'http_response_compression'
        HTTP_RESPONSE_FIREWALL_MANAGED = 'http_response_firewall_managed'
        HTTP_RESPONSE_HEADERS_TRANSFORM = 'http_response_headers_transform'



class Logging:
    """
    Logging.

    :param bool enabled:
    """

    def __init__(
        self,
        enabled: bool,
    ) -> None:
        """
        Initialize a Logging object.

        :param bool enabled:
        """
        self.enabled = enabled

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Logging':
        """Initialize a Logging object from a json dictionary."""
        args = {}
        enabled = _dict.get('enabled')
        if enabled is not None:
            args['enabled'] = enabled
        else:
            raise ValueError('Required property \'enabled\' not present in Logging JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Logging object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Logging object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Logging') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Logging') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Message:
    """
    Message.

    :param int code: (optional) A unique code for this message.
    :param str message: A text description of this message.
    :param MessageSource source: (optional) The source of this message.
    """

    def __init__(
        self,
        message: str,
        *,
        code: Optional[int] = None,
        source: Optional['MessageSource'] = None,
    ) -> None:
        """
        Initialize a Message object.

        :param str message: A text description of this message.
        :param int code: (optional) A unique code for this message.
        :param MessageSource source: (optional) The source of this message.
        """
        self.code = code
        self.message = message
        self.source = source

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Message':
        """Initialize a Message object from a json dictionary."""
        args = {}
        code = _dict.get('code')
        if code is not None:
            args['code'] = code
        message = _dict.get('message')
        if message is not None:
            args['message'] = message
        else:
            raise ValueError('Required property \'message\' not present in Message JSON')
        source = _dict.get('source')
        if source is not None:
            args['source'] = MessageSource.from_dict(source)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Message object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'code') and self.code is not None:
            _dict['code'] = self.code
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        if hasattr(self, 'source') and self.source is not None:
            if isinstance(self.source, dict):
                _dict['source'] = self.source
            else:
                _dict['source'] = self.source.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Message object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Message') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Message') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Overrides:
    """
    Overrides.

    :param str action: (optional) What happens when theres a match for the rule
          expression.
    :param bool enabled: (optional)
    :param str sensitivity_level: (optional) The sensitivity level of the rule.
    :param List[RulesOverride] rules: (optional)
    :param List[CategoriesOverride] categories: (optional)
    """

    def __init__(
        self,
        *,
        action: Optional[str] = None,
        enabled: Optional[bool] = None,
        sensitivity_level: Optional[str] = None,
        rules: Optional[List['RulesOverride']] = None,
        categories: Optional[List['CategoriesOverride']] = None,
    ) -> None:
        """
        Initialize a Overrides object.

        :param str action: (optional) What happens when theres a match for the rule
               expression.
        :param bool enabled: (optional)
        :param str sensitivity_level: (optional) The sensitivity level of the rule.
        :param List[RulesOverride] rules: (optional)
        :param List[CategoriesOverride] categories: (optional)
        """
        self.action = action
        self.enabled = enabled
        self.sensitivity_level = sensitivity_level
        self.rules = rules
        self.categories = categories

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Overrides':
        """Initialize a Overrides object from a json dictionary."""
        args = {}
        action = _dict.get('action')
        if action is not None:
            args['action'] = action
        enabled = _dict.get('enabled')
        if enabled is not None:
            args['enabled'] = enabled
        sensitivity_level = _dict.get('sensitivity_level')
        if sensitivity_level is not None:
            args['sensitivity_level'] = sensitivity_level
        rules = _dict.get('rules')
        if rules is not None:
            args['rules'] = [RulesOverride.from_dict(v) for v in rules]
        categories = _dict.get('categories')
        if categories is not None:
            args['categories'] = [CategoriesOverride.from_dict(v) for v in categories]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Overrides object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'action') and self.action is not None:
            _dict['action'] = self.action
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'sensitivity_level') and self.sensitivity_level is not None:
            _dict['sensitivity_level'] = self.sensitivity_level
        if hasattr(self, 'rules') and self.rules is not None:
            rules_list = []
            for v in self.rules:
                if isinstance(v, dict):
                    rules_list.append(v)
                else:
                    rules_list.append(v.to_dict())
            _dict['rules'] = rules_list
        if hasattr(self, 'categories') and self.categories is not None:
            categories_list = []
            for v in self.categories:
                if isinstance(v, dict):
                    categories_list.append(v)
                else:
                    categories_list.append(v.to_dict())
            _dict['categories'] = categories_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Overrides object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Overrides') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Overrides') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class SensitivityLevelEnum(str, Enum):
        """
        The sensitivity level of the rule.
        """

        HIGH = 'high'
        MEDIUM = 'medium'
        LOW = 'low'



class Position:
    """
    Position.

    :param str before: (optional) The rule ID to place this rule before.
    :param str after: (optional) The rule ID to place this rule after.
    :param int index: (optional) The index to place this rule at.
    """

    def __init__(
        self,
        *,
        before: Optional[str] = None,
        after: Optional[str] = None,
        index: Optional[int] = None,
    ) -> None:
        """
        Initialize a Position object.

        :param str before: (optional) The rule ID to place this rule before.
        :param str after: (optional) The rule ID to place this rule after.
        :param int index: (optional) The index to place this rule at.
        """
        self.before = before
        self.after = after
        self.index = index

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Position':
        """Initialize a Position object from a json dictionary."""
        args = {}
        before = _dict.get('before')
        if before is not None:
            args['before'] = before
        after = _dict.get('after')
        if after is not None:
            args['after'] = after
        index = _dict.get('index')
        if index is not None:
            args['index'] = index
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Position object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'before') and self.before is not None:
            _dict['before'] = self.before
        if hasattr(self, 'after') and self.after is not None:
            _dict['after'] = self.after
        if hasattr(self, 'index') and self.index is not None:
            _dict['index'] = self.index
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Position object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Position') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Position') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Ratelimit:
    """
    Ratelimit.

    :param List[str] characteristics: (optional) The set of parameters that define
          how rate for this rule is tracked.
    :param str counting_expression: (optional) Expression that specifies the
          criteria you are matching traffic on.
    :param int mitigation_timeout: (optional) Once the rate is reached, the rate
          limiting rule blocks further requests for the period of time defined in this
          field.
    :param int period: (optional) The period of time to consider (in seconds) when
          evaluating the rate.
    :param int requests_per_period: (optional) The number of requests over the
          period of time that will trigger the rate limiting rule.
    """

    def __init__(
        self,
        *,
        characteristics: Optional[List[str]] = None,
        counting_expression: Optional[str] = None,
        mitigation_timeout: Optional[int] = None,
        period: Optional[int] = None,
        requests_per_period: Optional[int] = None,
    ) -> None:
        """
        Initialize a Ratelimit object.

        :param List[str] characteristics: (optional) The set of parameters that
               define how rate for this rule is tracked.
        :param str counting_expression: (optional) Expression that specifies the
               criteria you are matching traffic on.
        :param int mitigation_timeout: (optional) Once the rate is reached, the
               rate limiting rule blocks further requests for the period of time defined
               in this field.
        :param int period: (optional) The period of time to consider (in seconds)
               when evaluating the rate.
        :param int requests_per_period: (optional) The number of requests over the
               period of time that will trigger the rate limiting rule.
        """
        self.characteristics = characteristics
        self.counting_expression = counting_expression
        self.mitigation_timeout = mitigation_timeout
        self.period = period
        self.requests_per_period = requests_per_period

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Ratelimit':
        """Initialize a Ratelimit object from a json dictionary."""
        args = {}
        characteristics = _dict.get('characteristics')
        if characteristics is not None:
            args['characteristics'] = characteristics
        counting_expression = _dict.get('counting_expression')
        if counting_expression is not None:
            args['counting_expression'] = counting_expression
        mitigation_timeout = _dict.get('mitigation_timeout')
        if mitigation_timeout is not None:
            args['mitigation_timeout'] = mitigation_timeout
        period = _dict.get('period')
        if period is not None:
            args['period'] = period
        requests_per_period = _dict.get('requests_per_period')
        if requests_per_period is not None:
            args['requests_per_period'] = requests_per_period
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Ratelimit object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'characteristics') and self.characteristics is not None:
            _dict['characteristics'] = self.characteristics
        if hasattr(self, 'counting_expression') and self.counting_expression is not None:
            _dict['counting_expression'] = self.counting_expression
        if hasattr(self, 'mitigation_timeout') and self.mitigation_timeout is not None:
            _dict['mitigation_timeout'] = self.mitigation_timeout
        if hasattr(self, 'period') and self.period is not None:
            _dict['period'] = self.period
        if hasattr(self, 'requests_per_period') and self.requests_per_period is not None:
            _dict['requests_per_period'] = self.requests_per_period
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Ratelimit object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Ratelimit') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Ratelimit') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RuleCreate:
    """
    RuleCreate.

    :param str action: What happens when theres a match for the rule expression.
    :param ActionParameters action_parameters: (optional)
    :param Ratelimit ratelimit: (optional)
    :param str description: (optional)
    :param bool enabled: (optional)
    :param str expression: The expression defining which traffic will match the
          rule.
    :param str id: (optional)
    :param Logging logging: (optional)
    :param str ref: (optional) The reference of the rule (the rule ID by default).
    :param Position position: (optional)
    """

    def __init__(
        self,
        action: str,
        expression: str,
        *,
        action_parameters: Optional['ActionParameters'] = None,
        ratelimit: Optional['Ratelimit'] = None,
        description: Optional[str] = None,
        enabled: Optional[bool] = None,
        id: Optional[str] = None,
        logging: Optional['Logging'] = None,
        ref: Optional[str] = None,
        position: Optional['Position'] = None,
    ) -> None:
        """
        Initialize a RuleCreate object.

        :param str action: What happens when theres a match for the rule
               expression.
        :param str expression: The expression defining which traffic will match the
               rule.
        :param ActionParameters action_parameters: (optional)
        :param Ratelimit ratelimit: (optional)
        :param str description: (optional)
        :param bool enabled: (optional)
        :param str id: (optional)
        :param Logging logging: (optional)
        :param str ref: (optional) The reference of the rule (the rule ID by
               default).
        :param Position position: (optional)
        """
        self.action = action
        self.action_parameters = action_parameters
        self.ratelimit = ratelimit
        self.description = description
        self.enabled = enabled
        self.expression = expression
        self.id = id
        self.logging = logging
        self.ref = ref
        self.position = position

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuleCreate':
        """Initialize a RuleCreate object from a json dictionary."""
        args = {}
        action = _dict.get('action')
        if action is not None:
            args['action'] = action
        else:
            raise ValueError('Required property \'action\' not present in RuleCreate JSON')
        action_parameters = _dict.get('action_parameters')
        if action_parameters is not None:
            args['action_parameters'] = ActionParameters.from_dict(action_parameters)
        ratelimit = _dict.get('ratelimit')
        if ratelimit is not None:
            args['ratelimit'] = Ratelimit.from_dict(ratelimit)
        description = _dict.get('description')
        if description is not None:
            args['description'] = description
        enabled = _dict.get('enabled')
        if enabled is not None:
            args['enabled'] = enabled
        expression = _dict.get('expression')
        if expression is not None:
            args['expression'] = expression
        else:
            raise ValueError('Required property \'expression\' not present in RuleCreate JSON')
        id = _dict.get('id')
        if id is not None:
            args['id'] = id
        logging = _dict.get('logging')
        if logging is not None:
            args['logging'] = Logging.from_dict(logging)
        ref = _dict.get('ref')
        if ref is not None:
            args['ref'] = ref
        position = _dict.get('position')
        if position is not None:
            args['position'] = Position.from_dict(position)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuleCreate object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'action') and self.action is not None:
            _dict['action'] = self.action
        if hasattr(self, 'action_parameters') and self.action_parameters is not None:
            if isinstance(self.action_parameters, dict):
                _dict['action_parameters'] = self.action_parameters
            else:
                _dict['action_parameters'] = self.action_parameters.to_dict()
        if hasattr(self, 'ratelimit') and self.ratelimit is not None:
            if isinstance(self.ratelimit, dict):
                _dict['ratelimit'] = self.ratelimit
            else:
                _dict['ratelimit'] = self.ratelimit.to_dict()
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'expression') and self.expression is not None:
            _dict['expression'] = self.expression
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'logging') and self.logging is not None:
            if isinstance(self.logging, dict):
                _dict['logging'] = self.logging
            else:
                _dict['logging'] = self.logging.to_dict()
        if hasattr(self, 'ref') and self.ref is not None:
            _dict['ref'] = self.ref
        if hasattr(self, 'position') and self.position is not None:
            if isinstance(self.position, dict):
                _dict['position'] = self.position
            else:
                _dict['position'] = self.position.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuleCreate object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuleCreate') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuleCreate') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RuleDetails:
    """
    RuleDetails.

    :param str id: unique ID of rule.
    :param str version: (optional) The version of the rule.
    :param str action: (optional) What happens when theres a match for the rule
          expression.
    :param ActionParameters action_parameters: (optional)
    :param List[str] categories: (optional) List of categories for the rule.
    :param bool enabled: (optional) Is the rule enabled.
    :param str description: (optional) description of the rule.
    :param str expression: (optional) The expression defining which traffic will
          match the rule.
    :param str ref: (optional) The reference of the rule (the rule ID by default).
    :param Logging logging: (optional)
    :param str last_updated: (optional) The timestamp of when the resource was last
          modified.
    """

    def __init__(
        self,
        id: str,
        *,
        version: Optional[str] = None,
        action: Optional[str] = None,
        action_parameters: Optional['ActionParameters'] = None,
        categories: Optional[List[str]] = None,
        enabled: Optional[bool] = None,
        description: Optional[str] = None,
        expression: Optional[str] = None,
        ref: Optional[str] = None,
        logging: Optional['Logging'] = None,
        last_updated: Optional[str] = None,
    ) -> None:
        """
        Initialize a RuleDetails object.

        :param str id: unique ID of rule.
        :param str version: (optional) The version of the rule.
        :param str action: (optional) What happens when theres a match for the rule
               expression.
        :param ActionParameters action_parameters: (optional)
        :param List[str] categories: (optional) List of categories for the rule.
        :param bool enabled: (optional) Is the rule enabled.
        :param str description: (optional) description of the rule.
        :param str expression: (optional) The expression defining which traffic
               will match the rule.
        :param str ref: (optional) The reference of the rule (the rule ID by
               default).
        :param Logging logging: (optional)
        :param str last_updated: (optional) The timestamp of when the resource was
               last modified.
        """
        self.id = id
        self.version = version
        self.action = action
        self.action_parameters = action_parameters
        self.categories = categories
        self.enabled = enabled
        self.description = description
        self.expression = expression
        self.ref = ref
        self.logging = logging
        self.last_updated = last_updated

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuleDetails':
        """Initialize a RuleDetails object from a json dictionary."""
        args = {}
        id = _dict.get('id')
        if id is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in RuleDetails JSON')
        version = _dict.get('version')
        if version is not None:
            args['version'] = version
        action = _dict.get('action')
        if action is not None:
            args['action'] = action
        action_parameters = _dict.get('action_parameters')
        if action_parameters is not None:
            args['action_parameters'] = ActionParameters.from_dict(action_parameters)
        categories = _dict.get('categories')
        if categories is not None:
            args['categories'] = categories
        enabled = _dict.get('enabled')
        if enabled is not None:
            args['enabled'] = enabled
        description = _dict.get('description')
        if description is not None:
            args['description'] = description
        expression = _dict.get('expression')
        if expression is not None:
            args['expression'] = expression
        ref = _dict.get('ref')
        if ref is not None:
            args['ref'] = ref
        logging = _dict.get('logging')
        if logging is not None:
            args['logging'] = Logging.from_dict(logging)
        last_updated = _dict.get('last_updated')
        if last_updated is not None:
            args['last_updated'] = last_updated
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuleDetails object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'action') and self.action is not None:
            _dict['action'] = self.action
        if hasattr(self, 'action_parameters') and self.action_parameters is not None:
            if isinstance(self.action_parameters, dict):
                _dict['action_parameters'] = self.action_parameters
            else:
                _dict['action_parameters'] = self.action_parameters.to_dict()
        if hasattr(self, 'categories') and self.categories is not None:
            _dict['categories'] = self.categories
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'expression') and self.expression is not None:
            _dict['expression'] = self.expression
        if hasattr(self, 'ref') and self.ref is not None:
            _dict['ref'] = self.ref
        if hasattr(self, 'logging') and self.logging is not None:
            if isinstance(self.logging, dict):
                _dict['logging'] = self.logging
            else:
                _dict['logging'] = self.logging.to_dict()
        if hasattr(self, 'last_updated') and self.last_updated is not None:
            _dict['last_updated'] = self.last_updated
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuleDetails object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuleDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuleDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RuleResp:
    """
    List rules response.

    :param bool success: Was operation successful.
    :param List[Message] errors: Array of errors encountered.
    :param List[Message] messages: Array of messages returned.
    :param RuleDetails result:
    """

    def __init__(
        self,
        success: bool,
        errors: List['Message'],
        messages: List['Message'],
        result: 'RuleDetails',
    ) -> None:
        """
        Initialize a RuleResp object.

        :param bool success: Was operation successful.
        :param List[Message] errors: Array of errors encountered.
        :param List[Message] messages: Array of messages returned.
        :param RuleDetails result:
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuleResp':
        """Initialize a RuleResp object from a json dictionary."""
        args = {}
        success = _dict.get('success')
        if success is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in RuleResp JSON')
        errors = _dict.get('errors')
        if errors is not None:
            args['errors'] = [Message.from_dict(v) for v in errors]
        else:
            raise ValueError('Required property \'errors\' not present in RuleResp JSON')
        messages = _dict.get('messages')
        if messages is not None:
            args['messages'] = [Message.from_dict(v) for v in messages]
        else:
            raise ValueError('Required property \'messages\' not present in RuleResp JSON')
        result = _dict.get('result')
        if result is not None:
            args['result'] = RuleDetails.from_dict(result)
        else:
            raise ValueError('Required property \'result\' not present in RuleResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuleResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            errors_list = []
            for v in self.errors:
                if isinstance(v, dict):
                    errors_list.append(v)
                else:
                    errors_list.append(v.to_dict())
            _dict['errors'] = errors_list
        if hasattr(self, 'messages') and self.messages is not None:
            messages_list = []
            for v in self.messages:
                if isinstance(v, dict):
                    messages_list.append(v)
                else:
                    messages_list.append(v.to_dict())
            _dict['messages'] = messages_list
        if hasattr(self, 'result') and self.result is not None:
            if isinstance(self.result, dict):
                _dict['result'] = self.result
            else:
                _dict['result'] = self.result.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuleResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuleResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuleResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RulesOverride:
    """
    RulesOverride.

    :param str id: (optional)
    :param bool enabled: (optional)
    :param str action: (optional) What happens when theres a match for the rule
          expression.
    :param str sensitivity_level: (optional) The sensitivity level of the rule.
    :param int score_threshold: (optional) The score threshold of the rule.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        enabled: Optional[bool] = None,
        action: Optional[str] = None,
        sensitivity_level: Optional[str] = None,
        score_threshold: Optional[int] = None,
    ) -> None:
        """
        Initialize a RulesOverride object.

        :param str id: (optional)
        :param bool enabled: (optional)
        :param str action: (optional) What happens when theres a match for the rule
               expression.
        :param str sensitivity_level: (optional) The sensitivity level of the rule.
        :param int score_threshold: (optional) The score threshold of the rule.
        """
        self.id = id
        self.enabled = enabled
        self.action = action
        self.sensitivity_level = sensitivity_level
        self.score_threshold = score_threshold

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RulesOverride':
        """Initialize a RulesOverride object from a json dictionary."""
        args = {}
        id = _dict.get('id')
        if id is not None:
            args['id'] = id
        enabled = _dict.get('enabled')
        if enabled is not None:
            args['enabled'] = enabled
        action = _dict.get('action')
        if action is not None:
            args['action'] = action
        sensitivity_level = _dict.get('sensitivity_level')
        if sensitivity_level is not None:
            args['sensitivity_level'] = sensitivity_level
        score_threshold = _dict.get('score_threshold')
        if score_threshold is not None:
            args['score_threshold'] = score_threshold
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RulesOverride object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'action') and self.action is not None:
            _dict['action'] = self.action
        if hasattr(self, 'sensitivity_level') and self.sensitivity_level is not None:
            _dict['sensitivity_level'] = self.sensitivity_level
        if hasattr(self, 'score_threshold') and self.score_threshold is not None:
            _dict['score_threshold'] = self.score_threshold
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RulesOverride object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RulesOverride') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RulesOverride') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class SensitivityLevelEnum(str, Enum):
        """
        The sensitivity level of the rule.
        """

        HIGH = 'high'
        MEDIUM = 'medium'
        LOW = 'low'



class RulesetDetails:
    """
    RulesetDetails.

    :param str description: description of the ruleset.
    :param str id: unique ID of the ruleset.
    :param str kind:
    :param str last_updated: The timestamp of when the resource was last modified.
    :param str name: human readable name of the ruleset.
    :param str phase: The phase of the ruleset.
    :param str version: The version of the ruleset.
    :param List[RuleDetails] rules:
    """

    def __init__(
        self,
        description: str,
        id: str,
        kind: str,
        last_updated: str,
        name: str,
        phase: str,
        version: str,
        rules: List['RuleDetails'],
    ) -> None:
        """
        Initialize a RulesetDetails object.

        :param str description: description of the ruleset.
        :param str id: unique ID of the ruleset.
        :param str kind:
        :param str last_updated: The timestamp of when the resource was last
               modified.
        :param str name: human readable name of the ruleset.
        :param str phase: The phase of the ruleset.
        :param str version: The version of the ruleset.
        :param List[RuleDetails] rules:
        """
        self.description = description
        self.id = id
        self.kind = kind
        self.last_updated = last_updated
        self.name = name
        self.phase = phase
        self.version = version
        self.rules = rules

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RulesetDetails':
        """Initialize a RulesetDetails object from a json dictionary."""
        args = {}
        description = _dict.get('description')
        if description is not None:
            args['description'] = description
        else:
            raise ValueError('Required property \'description\' not present in RulesetDetails JSON')
        id = _dict.get('id')
        if id is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in RulesetDetails JSON')
        kind = _dict.get('kind')
        if kind is not None:
            args['kind'] = kind
        else:
            raise ValueError('Required property \'kind\' not present in RulesetDetails JSON')
        last_updated = _dict.get('last_updated')
        if last_updated is not None:
            args['last_updated'] = last_updated
        else:
            raise ValueError('Required property \'last_updated\' not present in RulesetDetails JSON')
        name = _dict.get('name')
        if name is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in RulesetDetails JSON')
        phase = _dict.get('phase')
        if phase is not None:
            args['phase'] = phase
        else:
            raise ValueError('Required property \'phase\' not present in RulesetDetails JSON')
        version = _dict.get('version')
        if version is not None:
            args['version'] = version
        else:
            raise ValueError('Required property \'version\' not present in RulesetDetails JSON')
        rules = _dict.get('rules')
        if rules is not None:
            args['rules'] = [RuleDetails.from_dict(v) for v in rules]
        else:
            raise ValueError('Required property \'rules\' not present in RulesetDetails JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RulesetDetails object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'kind') and self.kind is not None:
            _dict['kind'] = self.kind
        if hasattr(self, 'last_updated') and self.last_updated is not None:
            _dict['last_updated'] = self.last_updated
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'phase') and self.phase is not None:
            _dict['phase'] = self.phase
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(self, 'rules') and self.rules is not None:
            rules_list = []
            for v in self.rules:
                if isinstance(v, dict):
                    rules_list.append(v)
                else:
                    rules_list.append(v.to_dict())
            _dict['rules'] = rules_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RulesetDetails object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RulesetDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RulesetDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class KindEnum(str, Enum):
        """
        kind.
        """

        MANAGED = 'managed'
        CUSTOM = 'custom'
        ROOT = 'root'
        ZONE = 'zone'


    class PhaseEnum(str, Enum):
        """
        The phase of the ruleset.
        """

        DDOS_L4 = 'ddos_l4'
        DDOS_L7 = 'ddos_l7'
        HTTP_CONFIG_SETTINGS = 'http_config_settings'
        HTTP_CUSTOM_ERRORS = 'http_custom_errors'
        HTTP_LOG_CUSTOM_FIELDS = 'http_log_custom_fields'
        HTTP_RATELIMIT = 'http_ratelimit'
        HTTP_REQUEST_CACHE_SETTINGS = 'http_request_cache_settings'
        HTTP_REQUEST_DYNAMIC_REDIRECT = 'http_request_dynamic_redirect'
        HTTP_REQUEST_FIREWALL_CUSTOM = 'http_request_firewall_custom'
        HTTP_REQUEST_FIREWALL_MANAGED = 'http_request_firewall_managed'
        HTTP_REQUEST_LATE_TRANSFORM = 'http_request_late_transform'
        HTTP_REQUEST_ORIGIN = 'http_request_origin'
        HTTP_REQUEST_REDIRECT = 'http_request_redirect'
        HTTP_REQUEST_SANITIZE = 'http_request_sanitize'
        HTTP_REQUEST_SBFM = 'http_request_sbfm'
        HTTP_REQUEST_SELECT_CONFIGURATION = 'http_request_select_configuration'
        HTTP_REQUEST_TRANSFORM = 'http_request_transform'
        HTTP_RESPONSE_COMPRESSION = 'http_response_compression'
        HTTP_RESPONSE_FIREWALL_MANAGED = 'http_response_firewall_managed'
        HTTP_RESPONSE_HEADERS_TRANSFORM = 'http_response_headers_transform'



class RulesetResp:
    """
    Ruleset response.

    :param bool success: Was operation successful.
    :param List[Message] errors: Array of errors encountered.
    :param List[Message] messages: Array of messages returned.
    :param RulesetDetails result:
    """

    def __init__(
        self,
        success: bool,
        errors: List['Message'],
        messages: List['Message'],
        result: 'RulesetDetails',
    ) -> None:
        """
        Initialize a RulesetResp object.

        :param bool success: Was operation successful.
        :param List[Message] errors: Array of errors encountered.
        :param List[Message] messages: Array of messages returned.
        :param RulesetDetails result:
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RulesetResp':
        """Initialize a RulesetResp object from a json dictionary."""
        args = {}
        success = _dict.get('success')
        if success is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in RulesetResp JSON')
        errors = _dict.get('errors')
        if errors is not None:
            args['errors'] = [Message.from_dict(v) for v in errors]
        else:
            raise ValueError('Required property \'errors\' not present in RulesetResp JSON')
        messages = _dict.get('messages')
        if messages is not None:
            args['messages'] = [Message.from_dict(v) for v in messages]
        else:
            raise ValueError('Required property \'messages\' not present in RulesetResp JSON')
        result = _dict.get('result')
        if result is not None:
            args['result'] = RulesetDetails.from_dict(result)
        else:
            raise ValueError('Required property \'result\' not present in RulesetResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RulesetResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            errors_list = []
            for v in self.errors:
                if isinstance(v, dict):
                    errors_list.append(v)
                else:
                    errors_list.append(v.to_dict())
            _dict['errors'] = errors_list
        if hasattr(self, 'messages') and self.messages is not None:
            messages_list = []
            for v in self.messages:
                if isinstance(v, dict):
                    messages_list.append(v)
                else:
                    messages_list.append(v.to_dict())
            _dict['messages'] = messages_list
        if hasattr(self, 'result') and self.result is not None:
            if isinstance(self.result, dict):
                _dict['result'] = self.result
            else:
                _dict['result'] = self.result.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RulesetResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RulesetResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RulesetResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other