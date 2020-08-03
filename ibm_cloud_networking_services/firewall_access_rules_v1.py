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


    def list_all_account_access_rules(self,
        *,
        notes: str = None,
        mode: str = None,
        configuration_target: str = None,
        configuration_value: str = None,
        page: int = None,
        per_page: int = None,
        order: str = None,
        direction: str = None,
        match: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List instance level firewall access rules.

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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_all_account_access_rules')
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

        url = '/v1/{0}/firewall/access_rules/rules'.format(
            *self.encode_path_vars(self.crn))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_account_access_rule(self,
        *,
        mode: str = None,
        notes: str = None,
        configuration: 'AccountAccessRuleInputConfiguration' = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create instance level firewall access rule.

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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_account_access_rule')
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

        url = '/v1/{0}/firewall/access_rules/rules'.format(
            *self.encode_path_vars(self.crn))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_account_access_rule(self,
        accessrule_identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete instance level access rule.

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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_account_access_rule')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/firewall/access_rules/rules/{1}'.format(
            *self.encode_path_vars(self.crn, accessrule_identifier))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_account_access_rule(self,
        accessrule_identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get instance level firewall access rule.

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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_account_access_rule')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/firewall/access_rules/rules/{1}'.format(
            *self.encode_path_vars(self.crn, accessrule_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_account_access_rule(self,
        accessrule_identifier: str,
        *,
        mode: str = None,
        notes: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update instance level firewall access rule.

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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_account_access_rule')
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

        url = '/v1/{0}/firewall/access_rules/rules/{1}'.format(
            *self.encode_path_vars(self.crn, accessrule_identifier))
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

    class Mode(str, Enum):
        """
        Search access rules by mode.
        """
        BLOCK = 'block'
        CHALLENGE = 'challenge'
        WHITELIST = 'whitelist'
        JS_CHALLENGE = 'js_challenge'
    class ConfigurationTarget(str, Enum):
        """
        Search access rules by configuration target.
        """
        IP = 'ip'
        IP_RANGE = 'ip_range'
        ASN = 'asn'
        COUNTRY = 'country'
    class Order(str, Enum):
        """
        Field by which to order list of access rules.
        """
        TARGET = 'target'
        VALUE = 'value'
        MODE = 'mode'
    class Direction(str, Enum):
        """
        Direction in which to order results [ascending/descending order].
        """
        ASC = 'asc'
        DESC = 'desc'
    class Match(str, Enum):
        """
        Whether to match all (all) or atleast one search parameter (any).
        """
        ANY = 'any'
        ALL = 'all'


##############################################################################
# Models
##############################################################################


class AccountAccessRuleInputConfiguration():
    """
    Configuration object specifying access rule.

    :attr str target: The request property to target.
    :attr str value: The value for the selected target.For ip the value is a valid
          ip address.For ip_range the value specifies ip range limited to /16 and /24. For
          asn the value is an AS number. For country the value is a country code for the
          country.
    """

    def __init__(self,
                 target: str,
                 value: str) -> None:
        """
        Initialize a AccountAccessRuleInputConfiguration object.

        :param str target: The request property to target.
        :param str value: The value for the selected target.For ip the value is a
               valid ip address.For ip_range the value specifies ip range limited to /16
               and /24. For asn the value is an AS number. For country the value is a
               country code for the country.
        """
        self.target = target
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AccountAccessRuleInputConfiguration':
        """Initialize a AccountAccessRuleInputConfiguration object from a json dictionary."""
        args = {}
        if 'target' in _dict:
            args['target'] = _dict.get('target')
        else:
            raise ValueError('Required property \'target\' not present in AccountAccessRuleInputConfiguration JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in AccountAccessRuleInputConfiguration JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AccountAccessRuleInputConfiguration object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'target') and self.target is not None:
            _dict['target'] = self.target
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AccountAccessRuleInputConfiguration object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AccountAccessRuleInputConfiguration') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AccountAccessRuleInputConfiguration') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TargetEnum(str, Enum):
        """
        The request property to target.
        """
        IP = 'ip'
        IP_RANGE = 'ip_range'
        ASN = 'asn'
        COUNTRY = 'country'


class AccountAccessRuleObjectConfiguration():
    """
    configuration.

    :attr str target: target ip address.
    :attr str value: Value for the given target. For ip the value is a valid ip
          address.For ip_range the value specifies ip range limited to /16 and /24. For
          asn the value is an AS number. For country the value is a country code for the
          country.
    """

    def __init__(self,
                 target: str,
                 value: str) -> None:
        """
        Initialize a AccountAccessRuleObjectConfiguration object.

        :param str target: target ip address.
        :param str value: Value for the given target. For ip the value is a valid
               ip address.For ip_range the value specifies ip range limited to /16 and
               /24. For asn the value is an AS number. For country the value is a country
               code for the country.
        """
        self.target = target
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AccountAccessRuleObjectConfiguration':
        """Initialize a AccountAccessRuleObjectConfiguration object from a json dictionary."""
        args = {}
        if 'target' in _dict:
            args['target'] = _dict.get('target')
        else:
            raise ValueError('Required property \'target\' not present in AccountAccessRuleObjectConfiguration JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in AccountAccessRuleObjectConfiguration JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AccountAccessRuleObjectConfiguration object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'target') and self.target is not None:
            _dict['target'] = self.target
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AccountAccessRuleObjectConfiguration object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AccountAccessRuleObjectConfiguration') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AccountAccessRuleObjectConfiguration') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TargetEnum(str, Enum):
        """
        target ip address.
        """
        IP = 'ip'
        IP_RANGE = 'ip_range'
        ASN = 'asn'
        COUNTRY = 'country'


class AccountAccessRuleObjectScope():
    """
    The scope definition of the access rule.

    :attr str type: The scope of the access rule.
    """

    def __init__(self,
                 type: str) -> None:
        """
        Initialize a AccountAccessRuleObjectScope object.

        :param str type: The scope of the access rule.
        """
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AccountAccessRuleObjectScope':
        """Initialize a AccountAccessRuleObjectScope object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in AccountAccessRuleObjectScope JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AccountAccessRuleObjectScope object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AccountAccessRuleObjectScope object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AccountAccessRuleObjectScope') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AccountAccessRuleObjectScope') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The scope of the access rule.
        """
        ACCOUNT = 'account'
        ORGANIZATION = 'organization'


class DeleteAccountAccessRuleRespResult():
    """
    Container for response information.

    :attr str id: ID.
    """

    def __init__(self,
                 id: str) -> None:
        """
        Initialize a DeleteAccountAccessRuleRespResult object.

        :param str id: ID.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteAccountAccessRuleRespResult':
        """Initialize a DeleteAccountAccessRuleRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in DeleteAccountAccessRuleRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteAccountAccessRuleRespResult object from a json dictionary."""
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
        """Return a `str` version of this DeleteAccountAccessRuleRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteAccountAccessRuleRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteAccountAccessRuleRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListAccountAccessRulesRespResultInfo():
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
        Initialize a ListAccountAccessRulesRespResultInfo object.

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
    def from_dict(cls, _dict: Dict) -> 'ListAccountAccessRulesRespResultInfo':
        """Initialize a ListAccountAccessRulesRespResultInfo object from a json dictionary."""
        args = {}
        if 'page' in _dict:
            args['page'] = _dict.get('page')
        else:
            raise ValueError('Required property \'page\' not present in ListAccountAccessRulesRespResultInfo JSON')
        if 'per_page' in _dict:
            args['per_page'] = _dict.get('per_page')
        else:
            raise ValueError('Required property \'per_page\' not present in ListAccountAccessRulesRespResultInfo JSON')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        else:
            raise ValueError('Required property \'count\' not present in ListAccountAccessRulesRespResultInfo JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in ListAccountAccessRulesRespResultInfo JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListAccountAccessRulesRespResultInfo object from a json dictionary."""
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
        """Return a `str` version of this ListAccountAccessRulesRespResultInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListAccountAccessRulesRespResultInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListAccountAccessRulesRespResultInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class AccountAccessRuleObject():
    """
    access rule objects.

    :attr str id: Identifier of the instance level firewall access rule.
    :attr str notes: A personal note about the rule. Typically used as a reminder or
          explanation for the rule.
    :attr List[str] allowed_modes: List of modes that are allowed.
    :attr str mode: The action to be applied to a request matching the instance
          level access rule.
    :attr AccountAccessRuleObjectScope scope: (optional) The scope definition of the
          access rule.
    :attr datetime created_on: The creation date-time of the instance level firewall
          access rule.
    :attr datetime modified_on: The modification date-time of the instance level
          firewall access rule.
    :attr AccountAccessRuleObjectConfiguration configuration: configuration.
    """

    def __init__(self,
                 id: str,
                 notes: str,
                 allowed_modes: List[str],
                 mode: str,
                 created_on: datetime,
                 modified_on: datetime,
                 configuration: 'AccountAccessRuleObjectConfiguration',
                 *,
                 scope: 'AccountAccessRuleObjectScope' = None) -> None:
        """
        Initialize a AccountAccessRuleObject object.

        :param str id: Identifier of the instance level firewall access rule.
        :param str notes: A personal note about the rule. Typically used as a
               reminder or explanation for the rule.
        :param List[str] allowed_modes: List of modes that are allowed.
        :param str mode: The action to be applied to a request matching the
               instance level access rule.
        :param datetime created_on: The creation date-time of the instance level
               firewall access rule.
        :param datetime modified_on: The modification date-time of the instance
               level firewall access rule.
        :param AccountAccessRuleObjectConfiguration configuration: configuration.
        :param AccountAccessRuleObjectScope scope: (optional) The scope definition
               of the access rule.
        """
        self.id = id
        self.notes = notes
        self.allowed_modes = allowed_modes
        self.mode = mode
        self.scope = scope
        self.created_on = created_on
        self.modified_on = modified_on
        self.configuration = configuration

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AccountAccessRuleObject':
        """Initialize a AccountAccessRuleObject object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in AccountAccessRuleObject JSON')
        if 'notes' in _dict:
            args['notes'] = _dict.get('notes')
        else:
            raise ValueError('Required property \'notes\' not present in AccountAccessRuleObject JSON')
        if 'allowed_modes' in _dict:
            args['allowed_modes'] = _dict.get('allowed_modes')
        else:
            raise ValueError('Required property \'allowed_modes\' not present in AccountAccessRuleObject JSON')
        if 'mode' in _dict:
            args['mode'] = _dict.get('mode')
        else:
            raise ValueError('Required property \'mode\' not present in AccountAccessRuleObject JSON')
        if 'scope' in _dict:
            args['scope'] = AccountAccessRuleObjectScope.from_dict(_dict.get('scope'))
        if 'created_on' in _dict:
            args['created_on'] = string_to_datetime(_dict.get('created_on'))
        else:
            raise ValueError('Required property \'created_on\' not present in AccountAccessRuleObject JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        else:
            raise ValueError('Required property \'modified_on\' not present in AccountAccessRuleObject JSON')
        if 'configuration' in _dict:
            args['configuration'] = AccountAccessRuleObjectConfiguration.from_dict(_dict.get('configuration'))
        else:
            raise ValueError('Required property \'configuration\' not present in AccountAccessRuleObject JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AccountAccessRuleObject object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'notes') and self.notes is not None:
            _dict['notes'] = self.notes
        if hasattr(self, 'allowed_modes') and self.allowed_modes is not None:
            _dict['allowed_modes'] = self.allowed_modes
        if hasattr(self, 'mode') and self.mode is not None:
            _dict['mode'] = self.mode
        if hasattr(self, 'scope') and self.scope is not None:
            _dict['scope'] = self.scope.to_dict()
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = datetime_to_string(self.created_on)
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = datetime_to_string(self.modified_on)
        if hasattr(self, 'configuration') and self.configuration is not None:
            _dict['configuration'] = self.configuration.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AccountAccessRuleObject object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AccountAccessRuleObject') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AccountAccessRuleObject') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class AllowedModesEnum(str, Enum):
        """
        allowed_modes.
        """
        BLOCK = 'block'
        CHALLENGE = 'challenge'
        WHITELIST = 'whitelist'
        JS_CHALLENGE = 'js_challenge'


    class ModeEnum(str, Enum):
        """
        The action to be applied to a request matching the instance level access rule.
        """
        BLOCK = 'block'
        CHALLENGE = 'challenge'
        WHITELIST = 'whitelist'
        JS_CHALLENGE = 'js_challenge'


class AccountAccessRuleResp():
    """
    access rule response output.

    :attr bool success: Operation success flag.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages encountered.
    :attr AccountAccessRuleObject result: access rule objects.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'AccountAccessRuleObject') -> None:
        """
        Initialize a AccountAccessRuleResp object.

        :param bool success: Operation success flag.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages encountered.
        :param AccountAccessRuleObject result: access rule objects.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AccountAccessRuleResp':
        """Initialize a AccountAccessRuleResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in AccountAccessRuleResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in AccountAccessRuleResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in AccountAccessRuleResp JSON')
        if 'result' in _dict:
            args['result'] = AccountAccessRuleObject.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in AccountAccessRuleResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AccountAccessRuleResp object from a json dictionary."""
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
        """Return a `str` version of this AccountAccessRuleResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AccountAccessRuleResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AccountAccessRuleResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DeleteAccountAccessRuleResp():
    """
    delete access rule response.

    :attr bool success: Operation success flag.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages encountered.
    :attr DeleteAccountAccessRuleRespResult result: Container for response
          information.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'DeleteAccountAccessRuleRespResult') -> None:
        """
        Initialize a DeleteAccountAccessRuleResp object.

        :param bool success: Operation success flag.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages encountered.
        :param DeleteAccountAccessRuleRespResult result: Container for response
               information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteAccountAccessRuleResp':
        """Initialize a DeleteAccountAccessRuleResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in DeleteAccountAccessRuleResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in DeleteAccountAccessRuleResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in DeleteAccountAccessRuleResp JSON')
        if 'result' in _dict:
            args['result'] = DeleteAccountAccessRuleRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in DeleteAccountAccessRuleResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteAccountAccessRuleResp object from a json dictionary."""
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
        """Return a `str` version of this DeleteAccountAccessRuleResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteAccountAccessRuleResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteAccountAccessRuleResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListAccountAccessRulesResp():
    """
    access rule list response.

    :attr bool success: Operation success flag.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages encountered.
    :attr List[AccountAccessRuleObject] result: Container for response information.
    :attr ListAccountAccessRulesRespResultInfo result_info: Statistics of results.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: List['AccountAccessRuleObject'],
                 result_info: 'ListAccountAccessRulesRespResultInfo') -> None:
        """
        Initialize a ListAccountAccessRulesResp object.

        :param bool success: Operation success flag.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages encountered.
        :param List[AccountAccessRuleObject] result: Container for response
               information.
        :param ListAccountAccessRulesRespResultInfo result_info: Statistics of
               results.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result
        self.result_info = result_info

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListAccountAccessRulesResp':
        """Initialize a ListAccountAccessRulesResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in ListAccountAccessRulesResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in ListAccountAccessRulesResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in ListAccountAccessRulesResp JSON')
        if 'result' in _dict:
            args['result'] = [AccountAccessRuleObject.from_dict(x) for x in _dict.get('result')]
        else:
            raise ValueError('Required property \'result\' not present in ListAccountAccessRulesResp JSON')
        if 'result_info' in _dict:
            args['result_info'] = ListAccountAccessRulesRespResultInfo.from_dict(_dict.get('result_info'))
        else:
            raise ValueError('Required property \'result_info\' not present in ListAccountAccessRulesResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListAccountAccessRulesResp object from a json dictionary."""
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
        """Return a `str` version of this ListAccountAccessRulesResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListAccountAccessRulesResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListAccountAccessRulesResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
