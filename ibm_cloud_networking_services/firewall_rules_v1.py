# coding: utf-8

# (C) Copyright IBM Corp. 2021.
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

# IBM OpenAPI SDK Code Generator Version: 3.32.0-4c6a3129-20210514-210323
 
"""
Firewall rules
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

class FirewallRulesV1(BaseService):
    """The Firewall rules V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'firewall_rules'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'FirewallRulesV1':
        """
        Return a new client for the Firewall rules service using the specified
               parameters and external configuration.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(self,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the Firewall rules service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # Firewall rules
    #########################


    def list_all_firewall_rules(self,
        x_auth_user_token: str,
        crn: str,
        zone_identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        List all firewall rules for a zone.

        List all firewall rules for a zone.

        :param str x_auth_user_token: IBM Cloud user IAM token.
        :param str crn: Full url-encoded cloud resource name (CRN) of resource
               instance.
        :param str zone_identifier: Zone identifier of the zone for which firewall
               rules are listed.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListFirewallRulesResp` object
        """

        if x_auth_user_token is None:
            raise ValueError('x_auth_user_token must be provided')
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_identifier is None:
            raise ValueError('zone_identifier must be provided')
        headers = {
            'X-Auth-User-Token': x_auth_user_token
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_all_firewall_rules')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(crn, zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/firewall/rules'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def create_firewall_rules(self,
        x_auth_user_token: str,
        crn: str,
        zone_identifier: str,
        *,
        firewall_rule_input_with_filter_id: List['FirewallRuleInputWithFilterId'] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create firewall rules for a zone.

        Create new firewall rules for a given zone under a service instance.

        :param str x_auth_user_token: IBM Cloud user IAM token.
        :param str crn: Full url-encoded cloud resource name (CRN) of resource
               instance.
        :param str zone_identifier: Zone identifier of the zone for which firewall
               rules are created.
        :param List[FirewallRuleInputWithFilterId]
               firewall_rule_input_with_filter_id: (optional) Json objects which are used
               to create firewall rules.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `FirewallRulesResp` object
        """

        if x_auth_user_token is None:
            raise ValueError('x_auth_user_token must be provided')
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_identifier is None:
            raise ValueError('zone_identifier must be provided')
        if firewall_rule_input_with_filter_id is not None:
            firewall_rule_input_with_filter_id = [convert_model(x) for x in firewall_rule_input_with_filter_id]
        headers = {
            'X-Auth-User-Token': x_auth_user_token
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_firewall_rules')
        headers.update(sdk_headers)

        data = json.dumps(firewall_rule_input_with_filter_id)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(crn, zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/firewall/rules'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def update_firewll_rules(self,
        x_auth_user_token: str,
        crn: str,
        zone_identifier: str,
        *,
        firewall_rules_update_input_item: List['FirewallRulesUpdateInputItem'] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update firewall rules.

        Update existing firewall rules for a given zone under a given service instance.

        :param str x_auth_user_token: IBM Cloud user IAM token.
        :param str crn: Full crn of the service instance.
        :param str zone_identifier: Zone identifier (zone id).
        :param List[FirewallRulesUpdateInputItem] firewall_rules_update_input_item:
               (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `FirewallRulesResp` object
        """

        if x_auth_user_token is None:
            raise ValueError('x_auth_user_token must be provided')
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_identifier is None:
            raise ValueError('zone_identifier must be provided')
        if firewall_rules_update_input_item is not None:
            firewall_rules_update_input_item = [convert_model(x) for x in firewall_rules_update_input_item]
        headers = {
            'X-Auth-User-Token': x_auth_user_token
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_firewll_rules')
        headers.update(sdk_headers)

        data = json.dumps(firewall_rules_update_input_item)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(crn, zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/firewall/rules'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_firewall_rules(self,
        x_auth_user_token: str,
        crn: str,
        zone_identifier: str,
        id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete firewall rules.

        Delete firewall rules by filter ids.

        :param str x_auth_user_token: IBM Cloud user IAM token.
        :param str crn: Full crn of the service instance.
        :param str zone_identifier: Identifier of zone whose firewall rules are to
               be deleted.
        :param str id: ids of firewall rules which will be deleted.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteFirewallRulesResp` object
        """

        if x_auth_user_token is None:
            raise ValueError('x_auth_user_token must be provided')
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_identifier is None:
            raise ValueError('zone_identifier must be provided')
        if id is None:
            raise ValueError('id must be provided')
        headers = {
            'X-Auth-User-Token': x_auth_user_token
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_firewall_rules')
        headers.update(sdk_headers)

        params = {
            'id': id
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(crn, zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/firewall/rules'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def delete_firewall_rule(self,
        x_auth_user_token: str,
        crn: str,
        zone_identifier: str,
        firewall_rule_identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a firewall rule.

        Delete a firewall rule given its id.

        :param str x_auth_user_token: IBM Cloud user IAM token.
        :param str crn: Full crn of the service instance.
        :param str zone_identifier: Identifier of zone whose firewall rule is to be
               deleted.
        :param str firewall_rule_identifier: Identifier of the firewall rule to be
               deleted.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteFirewallRuleResp` object
        """

        if x_auth_user_token is None:
            raise ValueError('x_auth_user_token must be provided')
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_identifier is None:
            raise ValueError('zone_identifier must be provided')
        if firewall_rule_identifier is None:
            raise ValueError('firewall_rule_identifier must be provided')
        headers = {
            'X-Auth-User-Token': x_auth_user_token
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_firewall_rule')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'firewall_rule_identifier']
        path_param_values = self.encode_path_vars(crn, zone_identifier, firewall_rule_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/firewall/rules/{firewall_rule_identifier}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_firewall_rule(self,
        x_auth_user_token: str,
        crn: str,
        zone_identifier: str,
        firewall_rule_identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get firewall rule details by id.

        Get the details of a firewall rule for a given zone under a given service
        instance.

        :param str x_auth_user_token: IBM Cloud user IAM token.
        :param str crn: Full crn of the service instance.
        :param str zone_identifier: Zone identifier (zone id).
        :param str firewall_rule_identifier: Identifier of firewall rule for the
               given zone.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `FirewallRuleResp` object
        """

        if x_auth_user_token is None:
            raise ValueError('x_auth_user_token must be provided')
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_identifier is None:
            raise ValueError('zone_identifier must be provided')
        if firewall_rule_identifier is None:
            raise ValueError('firewall_rule_identifier must be provided')
        headers = {
            'X-Auth-User-Token': x_auth_user_token
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_firewall_rule')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'firewall_rule_identifier']
        path_param_values = self.encode_path_vars(crn, zone_identifier, firewall_rule_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/firewall/rules/{firewall_rule_identifier}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_firewall_rule(self,
        x_auth_user_token: str,
        crn: str,
        zone_identifier: str,
        firewall_rule_identifier: str,
        *,
        action: str = None,
        paused: bool = None,
        description: str = None,
        filter: 'FirewallRuleUpdateInputFilter' = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update a firewall rule.

        Update an existing firewall rule for a given zone under a given service instance.

        :param str x_auth_user_token: IBM Cloud user IAM token.
        :param str crn: Full crn of the service instance.
        :param str zone_identifier: Zone identifier (zone id).
        :param str firewall_rule_identifier: Identifier of firewall rule.
        :param str action: (optional) The firewall action to perform, "log" action
               is only available for enterprise plan instances.
        :param bool paused: (optional) Indicates if the firewall rule is active.
        :param str description: (optional) To briefly describe the firewall rule,
               omitted from object if empty.
        :param FirewallRuleUpdateInputFilter filter: (optional) An existing filter.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `FirewallRuleResp` object
        """

        if x_auth_user_token is None:
            raise ValueError('x_auth_user_token must be provided')
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_identifier is None:
            raise ValueError('zone_identifier must be provided')
        if firewall_rule_identifier is None:
            raise ValueError('firewall_rule_identifier must be provided')
        if filter is not None:
            filter = convert_model(filter)
        headers = {
            'X-Auth-User-Token': x_auth_user_token
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_firewall_rule')
        headers.update(sdk_headers)

        data = {
            'action': action,
            'paused': paused,
            'description': description,
            'filter': filter
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'firewall_rule_identifier']
        path_param_values = self.encode_path_vars(crn, zone_identifier, firewall_rule_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/firewall/rules/{firewall_rule_identifier}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class DeleteFirewallRuleRespResult():
    """
    Container for response information.

    :attr str id: Identifier of the firewall rule.
    """

    def __init__(self,
                 id: str) -> None:
        """
        Initialize a DeleteFirewallRuleRespResult object.

        :param str id: Identifier of the firewall rule.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteFirewallRuleRespResult':
        """Initialize a DeleteFirewallRuleRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in DeleteFirewallRuleRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteFirewallRuleRespResult object from a json dictionary."""
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
        """Return a `str` version of this DeleteFirewallRuleRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteFirewallRuleRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteFirewallRuleRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DeleteFirewallRulesRespResultItem():
    """
    DeleteFirewallRulesRespResultItem.

    :attr str id: Identifier of firewall rules.
    """

    def __init__(self,
                 id: str) -> None:
        """
        Initialize a DeleteFirewallRulesRespResultItem object.

        :param str id: Identifier of firewall rules.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteFirewallRulesRespResultItem':
        """Initialize a DeleteFirewallRulesRespResultItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in DeleteFirewallRulesRespResultItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteFirewallRulesRespResultItem object from a json dictionary."""
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
        """Return a `str` version of this DeleteFirewallRulesRespResultItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteFirewallRulesRespResultItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteFirewallRulesRespResultItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class FirewallRuleInputWithFilterIdFilter():
    """
    An existing filter.

    :attr str id: Identifier of the filter.
    """

    def __init__(self,
                 id: str) -> None:
        """
        Initialize a FirewallRuleInputWithFilterIdFilter object.

        :param str id: Identifier of the filter.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FirewallRuleInputWithFilterIdFilter':
        """Initialize a FirewallRuleInputWithFilterIdFilter object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in FirewallRuleInputWithFilterIdFilter JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FirewallRuleInputWithFilterIdFilter object from a json dictionary."""
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
        """Return a `str` version of this FirewallRuleInputWithFilterIdFilter object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'FirewallRuleInputWithFilterIdFilter') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FirewallRuleInputWithFilterIdFilter') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class FirewallRuleObjectFilter():
    """
    An existing filter.

    :attr str id: Identifier of the filter.
    :attr bool paused: Indicates if the filter is active.
    :attr str description: To briefly describe the filter, omitted from object if
          empty.
    :attr str expression: A filter expression.
    """

    def __init__(self,
                 id: str,
                 paused: bool,
                 description: str,
                 expression: str) -> None:
        """
        Initialize a FirewallRuleObjectFilter object.

        :param str id: Identifier of the filter.
        :param bool paused: Indicates if the filter is active.
        :param str description: To briefly describe the filter, omitted from object
               if empty.
        :param str expression: A filter expression.
        """
        self.id = id
        self.paused = paused
        self.description = description
        self.expression = expression

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FirewallRuleObjectFilter':
        """Initialize a FirewallRuleObjectFilter object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in FirewallRuleObjectFilter JSON')
        if 'paused' in _dict:
            args['paused'] = _dict.get('paused')
        else:
            raise ValueError('Required property \'paused\' not present in FirewallRuleObjectFilter JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError('Required property \'description\' not present in FirewallRuleObjectFilter JSON')
        if 'expression' in _dict:
            args['expression'] = _dict.get('expression')
        else:
            raise ValueError('Required property \'expression\' not present in FirewallRuleObjectFilter JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FirewallRuleObjectFilter object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'paused') and self.paused is not None:
            _dict['paused'] = self.paused
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'expression') and self.expression is not None:
            _dict['expression'] = self.expression
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FirewallRuleObjectFilter object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'FirewallRuleObjectFilter') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FirewallRuleObjectFilter') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class FirewallRuleUpdateInputFilter():
    """
    An existing filter.

    :attr str id: Identifier of the filter.
    """

    def __init__(self,
                 id: str) -> None:
        """
        Initialize a FirewallRuleUpdateInputFilter object.

        :param str id: Identifier of the filter.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FirewallRuleUpdateInputFilter':
        """Initialize a FirewallRuleUpdateInputFilter object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in FirewallRuleUpdateInputFilter JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FirewallRuleUpdateInputFilter object from a json dictionary."""
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
        """Return a `str` version of this FirewallRuleUpdateInputFilter object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'FirewallRuleUpdateInputFilter') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FirewallRuleUpdateInputFilter') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class FirewallRulesUpdateInputItem():
    """
    FirewallRulesUpdateInputItem.

    :attr str id: Identifier of the firewall rule.
    :attr str action: The firewall action to perform, "log" action is only available
          for enterprise plan instances.
    :attr bool paused: (optional) Indicates if the firewall rule is active.
    :attr str description: (optional) To briefly describe the firewall rule, omitted
          from object if empty.
    :attr FirewallRulesUpdateInputItemFilter filter: (optional) An existing filter.
    """

    def __init__(self,
                 id: str,
                 action: str,
                 *,
                 paused: bool = None,
                 description: str = None,
                 filter: 'FirewallRulesUpdateInputItemFilter' = None) -> None:
        """
        Initialize a FirewallRulesUpdateInputItem object.

        :param str id: Identifier of the firewall rule.
        :param str action: The firewall action to perform, "log" action is only
               available for enterprise plan instances.
        :param bool paused: (optional) Indicates if the firewall rule is active.
        :param str description: (optional) To briefly describe the firewall rule,
               omitted from object if empty.
        :param FirewallRulesUpdateInputItemFilter filter: (optional) An existing
               filter.
        """
        self.id = id
        self.action = action
        self.paused = paused
        self.description = description
        self.filter = filter

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FirewallRulesUpdateInputItem':
        """Initialize a FirewallRulesUpdateInputItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in FirewallRulesUpdateInputItem JSON')
        if 'action' in _dict:
            args['action'] = _dict.get('action')
        else:
            raise ValueError('Required property \'action\' not present in FirewallRulesUpdateInputItem JSON')
        if 'paused' in _dict:
            args['paused'] = _dict.get('paused')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'filter' in _dict:
            args['filter'] = FirewallRulesUpdateInputItemFilter.from_dict(_dict.get('filter'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FirewallRulesUpdateInputItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'action') and self.action is not None:
            _dict['action'] = self.action
        if hasattr(self, 'paused') and self.paused is not None:
            _dict['paused'] = self.paused
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'filter') and self.filter is not None:
            _dict['filter'] = self.filter.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FirewallRulesUpdateInputItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'FirewallRulesUpdateInputItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FirewallRulesUpdateInputItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ActionEnum(str, Enum):
        """
        The firewall action to perform, "log" action is only available for enterprise plan
        instances.
        """
        LOG = 'log'
        ALLOW = 'allow'
        CHALLENGE = 'challenge'
        JS_CHALLENGE = 'js_challenge'
        BLOCK = 'block'


class FirewallRulesUpdateInputItemFilter():
    """
    An existing filter.

    :attr str id: Identifier of the filter.
    """

    def __init__(self,
                 id: str) -> None:
        """
        Initialize a FirewallRulesUpdateInputItemFilter object.

        :param str id: Identifier of the filter.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FirewallRulesUpdateInputItemFilter':
        """Initialize a FirewallRulesUpdateInputItemFilter object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in FirewallRulesUpdateInputItemFilter JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FirewallRulesUpdateInputItemFilter object from a json dictionary."""
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
        """Return a `str` version of this FirewallRulesUpdateInputItemFilter object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'FirewallRulesUpdateInputItemFilter') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FirewallRulesUpdateInputItemFilter') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListFirewallRulesRespResultInfo():
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
        Initialize a ListFirewallRulesRespResultInfo object.

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
    def from_dict(cls, _dict: Dict) -> 'ListFirewallRulesRespResultInfo':
        """Initialize a ListFirewallRulesRespResultInfo object from a json dictionary."""
        args = {}
        if 'page' in _dict:
            args['page'] = _dict.get('page')
        else:
            raise ValueError('Required property \'page\' not present in ListFirewallRulesRespResultInfo JSON')
        if 'per_page' in _dict:
            args['per_page'] = _dict.get('per_page')
        else:
            raise ValueError('Required property \'per_page\' not present in ListFirewallRulesRespResultInfo JSON')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        else:
            raise ValueError('Required property \'count\' not present in ListFirewallRulesRespResultInfo JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in ListFirewallRulesRespResultInfo JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListFirewallRulesRespResultInfo object from a json dictionary."""
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
        """Return a `str` version of this ListFirewallRulesRespResultInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListFirewallRulesRespResultInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListFirewallRulesRespResultInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DeleteFirewallRuleResp():
    """
    DeleteFirewallRuleResp.

    :attr bool success: Operation success flag.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr DeleteFirewallRuleRespResult result: Container for response information.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'DeleteFirewallRuleRespResult') -> None:
        """
        Initialize a DeleteFirewallRuleResp object.

        :param bool success: Operation success flag.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param DeleteFirewallRuleRespResult result: Container for response
               information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteFirewallRuleResp':
        """Initialize a DeleteFirewallRuleResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in DeleteFirewallRuleResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in DeleteFirewallRuleResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in DeleteFirewallRuleResp JSON')
        if 'result' in _dict:
            args['result'] = DeleteFirewallRuleRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in DeleteFirewallRuleResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteFirewallRuleResp object from a json dictionary."""
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
        """Return a `str` version of this DeleteFirewallRuleResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteFirewallRuleResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteFirewallRuleResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DeleteFirewallRulesResp():
    """
    DeleteFirewallRulesResp.

    :attr bool success: Operation success flag.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr List[DeleteFirewallRulesRespResultItem] result: Container for response
          information.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: List['DeleteFirewallRulesRespResultItem']) -> None:
        """
        Initialize a DeleteFirewallRulesResp object.

        :param bool success: Operation success flag.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param List[DeleteFirewallRulesRespResultItem] result: Container for
               response information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteFirewallRulesResp':
        """Initialize a DeleteFirewallRulesResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in DeleteFirewallRulesResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in DeleteFirewallRulesResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in DeleteFirewallRulesResp JSON')
        if 'result' in _dict:
            args['result'] = [DeleteFirewallRulesRespResultItem.from_dict(x) for x in _dict.get('result')]
        else:
            raise ValueError('Required property \'result\' not present in DeleteFirewallRulesResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteFirewallRulesResp object from a json dictionary."""
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
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeleteFirewallRulesResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteFirewallRulesResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteFirewallRulesResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class FirewallRuleInputWithFilterId():
    """
    Json objects which are used to create firewall rule.

    :attr FirewallRuleInputWithFilterIdFilter filter: An existing filter.
    :attr str action: The firewall action to perform, "log" action is only available
          for enterprise plan instances.
    :attr str description: (optional) To briefly describe the firewall rule, omitted
          from object if empty.
    """

    def __init__(self,
                 filter: 'FirewallRuleInputWithFilterIdFilter',
                 action: str,
                 *,
                 description: str = None) -> None:
        """
        Initialize a FirewallRuleInputWithFilterId object.

        :param FirewallRuleInputWithFilterIdFilter filter: An existing filter.
        :param str action: The firewall action to perform, "log" action is only
               available for enterprise plan instances.
        :param str description: (optional) To briefly describe the firewall rule,
               omitted from object if empty.
        """
        self.filter = filter
        self.action = action
        self.description = description

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FirewallRuleInputWithFilterId':
        """Initialize a FirewallRuleInputWithFilterId object from a json dictionary."""
        args = {}
        if 'filter' in _dict:
            args['filter'] = FirewallRuleInputWithFilterIdFilter.from_dict(_dict.get('filter'))
        else:
            raise ValueError('Required property \'filter\' not present in FirewallRuleInputWithFilterId JSON')
        if 'action' in _dict:
            args['action'] = _dict.get('action')
        else:
            raise ValueError('Required property \'action\' not present in FirewallRuleInputWithFilterId JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FirewallRuleInputWithFilterId object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'filter') and self.filter is not None:
            _dict['filter'] = self.filter.to_dict()
        if hasattr(self, 'action') and self.action is not None:
            _dict['action'] = self.action
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FirewallRuleInputWithFilterId object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'FirewallRuleInputWithFilterId') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FirewallRuleInputWithFilterId') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ActionEnum(str, Enum):
        """
        The firewall action to perform, "log" action is only available for enterprise plan
        instances.
        """
        LOG = 'log'
        ALLOW = 'allow'
        CHALLENGE = 'challenge'
        JS_CHALLENGE = 'js_challenge'
        BLOCK = 'block'


class FirewallRuleObject():
    """
    FirewallRuleObject.

    :attr str id: Identifier of the firewall rule.
    :attr bool paused: Indicates if the firewall rule is active.
    :attr str description: To briefly describe the firewall rule, omitted from
          object if empty.
    :attr str action: The firewall action to perform, "log" action is only available
          for enterprise plan instances.
    :attr FirewallRuleObjectFilter filter: An existing filter.
    :attr str created_on: The creation date-time of the filter.
    :attr str modified_on: The modification date-time of the filter.
    """

    def __init__(self,
                 id: str,
                 paused: bool,
                 description: str,
                 action: str,
                 filter: 'FirewallRuleObjectFilter',
                 created_on: str,
                 modified_on: str) -> None:
        """
        Initialize a FirewallRuleObject object.

        :param str id: Identifier of the firewall rule.
        :param bool paused: Indicates if the firewall rule is active.
        :param str description: To briefly describe the firewall rule, omitted from
               object if empty.
        :param str action: The firewall action to perform, "log" action is only
               available for enterprise plan instances.
        :param FirewallRuleObjectFilter filter: An existing filter.
        :param str created_on: The creation date-time of the filter.
        :param str modified_on: The modification date-time of the filter.
        """
        self.id = id
        self.paused = paused
        self.description = description
        self.action = action
        self.filter = filter
        self.created_on = created_on
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FirewallRuleObject':
        """Initialize a FirewallRuleObject object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in FirewallRuleObject JSON')
        if 'paused' in _dict:
            args['paused'] = _dict.get('paused')
        else:
            raise ValueError('Required property \'paused\' not present in FirewallRuleObject JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError('Required property \'description\' not present in FirewallRuleObject JSON')
        if 'action' in _dict:
            args['action'] = _dict.get('action')
        else:
            raise ValueError('Required property \'action\' not present in FirewallRuleObject JSON')
        if 'filter' in _dict:
            args['filter'] = FirewallRuleObjectFilter.from_dict(_dict.get('filter'))
        else:
            raise ValueError('Required property \'filter\' not present in FirewallRuleObject JSON')
        if 'created_on' in _dict:
            args['created_on'] = _dict.get('created_on')
        else:
            raise ValueError('Required property \'created_on\' not present in FirewallRuleObject JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        else:
            raise ValueError('Required property \'modified_on\' not present in FirewallRuleObject JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FirewallRuleObject object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'paused') and self.paused is not None:
            _dict['paused'] = self.paused
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'action') and self.action is not None:
            _dict['action'] = self.action
        if hasattr(self, 'filter') and self.filter is not None:
            _dict['filter'] = self.filter.to_dict()
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = self.created_on
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = self.modified_on
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FirewallRuleObject object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'FirewallRuleObject') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FirewallRuleObject') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ActionEnum(str, Enum):
        """
        The firewall action to perform, "log" action is only available for enterprise plan
        instances.
        """
        LOG = 'log'
        ALLOW = 'allow'
        CHALLENGE = 'challenge'
        JS_CHALLENGE = 'js_challenge'
        BLOCK = 'block'


class FirewallRuleResp():
    """
    FirewallRuleResp.

    :attr bool success: Operation success flag.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr FirewallRuleObject result:
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'FirewallRuleObject') -> None:
        """
        Initialize a FirewallRuleResp object.

        :param bool success: Operation success flag.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param FirewallRuleObject result:
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FirewallRuleResp':
        """Initialize a FirewallRuleResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in FirewallRuleResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in FirewallRuleResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in FirewallRuleResp JSON')
        if 'result' in _dict:
            args['result'] = FirewallRuleObject.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in FirewallRuleResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FirewallRuleResp object from a json dictionary."""
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
        """Return a `str` version of this FirewallRuleResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'FirewallRuleResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FirewallRuleResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class FirewallRulesResp():
    """
    FirewallRulesResp.

    :attr bool success: Operation success flag.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr List[FirewallRuleObject] result: Container for response information.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: List['FirewallRuleObject']) -> None:
        """
        Initialize a FirewallRulesResp object.

        :param bool success: Operation success flag.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param List[FirewallRuleObject] result: Container for response information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FirewallRulesResp':
        """Initialize a FirewallRulesResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in FirewallRulesResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in FirewallRulesResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in FirewallRulesResp JSON')
        if 'result' in _dict:
            args['result'] = [FirewallRuleObject.from_dict(x) for x in _dict.get('result')]
        else:
            raise ValueError('Required property \'result\' not present in FirewallRulesResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FirewallRulesResp object from a json dictionary."""
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
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FirewallRulesResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'FirewallRulesResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FirewallRulesResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListFirewallRulesResp():
    """
    ListFirewallRulesResp.

    :attr bool success: Operation success flag.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr List[FirewallRuleObject] result: Container for response information.
    :attr ListFirewallRulesRespResultInfo result_info: Statistics of results.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: List['FirewallRuleObject'],
                 result_info: 'ListFirewallRulesRespResultInfo') -> None:
        """
        Initialize a ListFirewallRulesResp object.

        :param bool success: Operation success flag.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param List[FirewallRuleObject] result: Container for response information.
        :param ListFirewallRulesRespResultInfo result_info: Statistics of results.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result
        self.result_info = result_info

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListFirewallRulesResp':
        """Initialize a ListFirewallRulesResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in ListFirewallRulesResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in ListFirewallRulesResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in ListFirewallRulesResp JSON')
        if 'result' in _dict:
            args['result'] = [FirewallRuleObject.from_dict(x) for x in _dict.get('result')]
        else:
            raise ValueError('Required property \'result\' not present in ListFirewallRulesResp JSON')
        if 'result_info' in _dict:
            args['result_info'] = ListFirewallRulesRespResultInfo.from_dict(_dict.get('result_info'))
        else:
            raise ValueError('Required property \'result_info\' not present in ListFirewallRulesResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListFirewallRulesResp object from a json dictionary."""
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
        """Return a `str` version of this ListFirewallRulesResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListFirewallRulesResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListFirewallRulesResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
