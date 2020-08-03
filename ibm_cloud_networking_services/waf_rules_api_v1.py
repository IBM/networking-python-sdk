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
    # WAF Rules
    #########################


    def list_waf_rules(self,
        package_id: str,
        *,
        mode: str = None,
        priority: str = None,
        match: str = None,
        order: str = None,
        group_id: str = None,
        description: str = None,
        direction: str = None,
        page: int = None,
        per_page: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List all WAF rules.

        List all Web Application Firewall (WAF) rules.

        :param str package_id: package id.
        :param str mode: (optional) The Rule Mode.
        :param str priority: (optional) The order in which the individual rule is
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
        :param int page: (optional) Page number of paginated results. default
               value: 1; min value:1.
        :param int per_page: (optional) Number of rules per page. default value:
               50; min value:5; max value:100.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `WafRulesResponse` object
        """

        if package_id is None:
            raise ValueError('package_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_waf_rules')
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

        url = '/v1/{0}/zones/{1}/firewall/waf/packages/{2}/rules'.format(
            *self.encode_path_vars(self.crn, self.zone_id, package_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def get_waf_rule(self,
        package_id: str,
        identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get WAF rule.

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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_waf_rule')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/firewall/waf/packages/{2}/rules/{3}'.format(
            *self.encode_path_vars(self.crn, self.zone_id, package_id, identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_waf_rule(self,
        package_id: str,
        identifier: str,
        *,
        cis: 'WafRuleBodyCis' = None,
        owasp: 'WafRuleBodyOwasp' = None,
        **kwargs
    ) -> DetailedResponse:
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_waf_rule')
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

        url = '/v1/{0}/zones/{1}/firewall/waf/packages/{2}/rules/{3}'.format(
            *self.encode_path_vars(self.crn, self.zone_id, package_id, identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


class ListWafRulesEnums:
    """
    Enums for list_waf_rules parameters.
    """

    class Mode(str, Enum):
        """
        The Rule Mode.
        """
        ON = 'on'
        OFF = 'off'


##############################################################################
# Models
##############################################################################


class WafRuleBodyCis():
    """
    cis package.

    :attr str mode: mode to choose from.
    """

    def __init__(self,
                 mode: str) -> None:
        """
        Initialize a WafRuleBodyCis object.

        :param str mode: mode to choose from.
        """
        self.mode = mode

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WafRuleBodyCis':
        """Initialize a WafRuleBodyCis object from a json dictionary."""
        args = {}
        if 'mode' in _dict:
            args['mode'] = _dict.get('mode')
        else:
            raise ValueError('Required property \'mode\' not present in WafRuleBodyCis JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WafRuleBodyCis object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'mode') and self.mode is not None:
            _dict['mode'] = self.mode
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this WafRuleBodyCis object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WafRuleBodyCis') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WafRuleBodyCis') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ModeEnum(str, Enum):
        """
        mode to choose from.
        """
        DEFAULT = 'default'
        DISABLE = 'disable'
        SIMULATE = 'simulate'
        BLOCK = 'block'
        CHALLENGE = 'challenge'


class WafRuleBodyOwasp():
    """
    owasp package.

    :attr str mode: mode to choose from. 'owasp' limited modes - on and off.
    """

    def __init__(self,
                 mode: str) -> None:
        """
        Initialize a WafRuleBodyOwasp object.

        :param str mode: mode to choose from. 'owasp' limited modes - on and off.
        """
        self.mode = mode

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WafRuleBodyOwasp':
        """Initialize a WafRuleBodyOwasp object from a json dictionary."""
        args = {}
        if 'mode' in _dict:
            args['mode'] = _dict.get('mode')
        else:
            raise ValueError('Required property \'mode\' not present in WafRuleBodyOwasp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WafRuleBodyOwasp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'mode') and self.mode is not None:
            _dict['mode'] = self.mode
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this WafRuleBodyOwasp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WafRuleBodyOwasp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WafRuleBodyOwasp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ModeEnum(str, Enum):
        """
        mode to choose from. 'owasp' limited modes - on and off.
        """
        ON = 'on'
        OFF = 'off'


class WafRuleResponseResult():
    """
    Information about a Rule.

    :attr str id: (optional) ID.
    :attr str description: (optional) description.
    :attr str priority: (optional) priority.
    :attr WafRuleResponseResultGroup group: (optional) group definition.
    :attr str package_id: (optional) package id.
    :attr List[str] allowed_modes: (optional) allowed modes.
    :attr str mode: (optional) mode.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 description: str = None,
                 priority: str = None,
                 group: 'WafRuleResponseResultGroup' = None,
                 package_id: str = None,
                 allowed_modes: List[str] = None,
                 mode: str = None) -> None:
        """
        Initialize a WafRuleResponseResult object.

        :param str id: (optional) ID.
        :param str description: (optional) description.
        :param str priority: (optional) priority.
        :param WafRuleResponseResultGroup group: (optional) group definition.
        :param str package_id: (optional) package id.
        :param List[str] allowed_modes: (optional) allowed modes.
        :param str mode: (optional) mode.
        """
        self.id = id
        self.description = description
        self.priority = priority
        self.group = group
        self.package_id = package_id
        self.allowed_modes = allowed_modes
        self.mode = mode

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WafRuleResponseResult':
        """Initialize a WafRuleResponseResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'priority' in _dict:
            args['priority'] = _dict.get('priority')
        if 'group' in _dict:
            args['group'] = WafRuleResponseResultGroup.from_dict(_dict.get('group'))
        if 'package_id' in _dict:
            args['package_id'] = _dict.get('package_id')
        if 'allowed_modes' in _dict:
            args['allowed_modes'] = _dict.get('allowed_modes')
        if 'mode' in _dict:
            args['mode'] = _dict.get('mode')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WafRuleResponseResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'priority') and self.priority is not None:
            _dict['priority'] = self.priority
        if hasattr(self, 'group') and self.group is not None:
            _dict['group'] = self.group.to_dict()
        if hasattr(self, 'package_id') and self.package_id is not None:
            _dict['package_id'] = self.package_id
        if hasattr(self, 'allowed_modes') and self.allowed_modes is not None:
            _dict['allowed_modes'] = self.allowed_modes
        if hasattr(self, 'mode') and self.mode is not None:
            _dict['mode'] = self.mode
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this WafRuleResponseResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WafRuleResponseResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WafRuleResponseResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ModeEnum(str, Enum):
        """
        mode.
        """
        ON = 'on'
        OFF = 'off'


class WafRuleResponseResultGroup():
    """
    group definition.

    :attr str id: (optional) group id.
    :attr str name: (optional) group name.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 name: str = None) -> None:
        """
        Initialize a WafRuleResponseResultGroup object.

        :param str id: (optional) group id.
        :param str name: (optional) group name.
        """
        self.id = id
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WafRuleResponseResultGroup':
        """Initialize a WafRuleResponseResultGroup object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WafRuleResponseResultGroup object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this WafRuleResponseResultGroup object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WafRuleResponseResultGroup') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WafRuleResponseResultGroup') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class WafRulesResponseResultInfo():
    """
    result information.

    :attr int page: (optional) current page.
    :attr int per_page: (optional) number of data per page.
    :attr int count: (optional) count.
    :attr int total_count: (optional) total count of data.
    """

    def __init__(self,
                 *,
                 page: int = None,
                 per_page: int = None,
                 count: int = None,
                 total_count: int = None) -> None:
        """
        Initialize a WafRulesResponseResultInfo object.

        :param int page: (optional) current page.
        :param int per_page: (optional) number of data per page.
        :param int count: (optional) count.
        :param int total_count: (optional) total count of data.
        """
        self.page = page
        self.per_page = per_page
        self.count = count
        self.total_count = total_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WafRulesResponseResultInfo':
        """Initialize a WafRulesResponseResultInfo object from a json dictionary."""
        args = {}
        if 'page' in _dict:
            args['page'] = _dict.get('page')
        if 'per_page' in _dict:
            args['per_page'] = _dict.get('per_page')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WafRulesResponseResultInfo object from a json dictionary."""
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
        """Return a `str` version of this WafRulesResponseResultInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WafRulesResponseResultInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WafRulesResponseResultInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class WafRulesResponseResultItem():
    """
    WafRulesResponseResultItem.

    :attr str id: (optional) ID.
    :attr str description: (optional) description.
    :attr str priority: (optional) priority.
    :attr WafRulesResponseResultItemGroup group: (optional) group definition.
    :attr str package_id: (optional) package id.
    :attr List[str] allowed_modes: (optional) allowed modes.
    :attr str mode: (optional) mode.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 description: str = None,
                 priority: str = None,
                 group: 'WafRulesResponseResultItemGroup' = None,
                 package_id: str = None,
                 allowed_modes: List[str] = None,
                 mode: str = None) -> None:
        """
        Initialize a WafRulesResponseResultItem object.

        :param str id: (optional) ID.
        :param str description: (optional) description.
        :param str priority: (optional) priority.
        :param WafRulesResponseResultItemGroup group: (optional) group definition.
        :param str package_id: (optional) package id.
        :param List[str] allowed_modes: (optional) allowed modes.
        :param str mode: (optional) mode.
        """
        self.id = id
        self.description = description
        self.priority = priority
        self.group = group
        self.package_id = package_id
        self.allowed_modes = allowed_modes
        self.mode = mode

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WafRulesResponseResultItem':
        """Initialize a WafRulesResponseResultItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'priority' in _dict:
            args['priority'] = _dict.get('priority')
        if 'group' in _dict:
            args['group'] = WafRulesResponseResultItemGroup.from_dict(_dict.get('group'))
        if 'package_id' in _dict:
            args['package_id'] = _dict.get('package_id')
        if 'allowed_modes' in _dict:
            args['allowed_modes'] = _dict.get('allowed_modes')
        if 'mode' in _dict:
            args['mode'] = _dict.get('mode')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WafRulesResponseResultItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'priority') and self.priority is not None:
            _dict['priority'] = self.priority
        if hasattr(self, 'group') and self.group is not None:
            _dict['group'] = self.group.to_dict()
        if hasattr(self, 'package_id') and self.package_id is not None:
            _dict['package_id'] = self.package_id
        if hasattr(self, 'allowed_modes') and self.allowed_modes is not None:
            _dict['allowed_modes'] = self.allowed_modes
        if hasattr(self, 'mode') and self.mode is not None:
            _dict['mode'] = self.mode
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this WafRulesResponseResultItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WafRulesResponseResultItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WafRulesResponseResultItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ModeEnum(str, Enum):
        """
        mode.
        """
        ON = 'on'
        OFF = 'off'


class WafRulesResponseResultItemGroup():
    """
    group definition.

    :attr str id: (optional) group id.
    :attr str name: (optional) group name.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 name: str = None) -> None:
        """
        Initialize a WafRulesResponseResultItemGroup object.

        :param str id: (optional) group id.
        :param str name: (optional) group name.
        """
        self.id = id
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WafRulesResponseResultItemGroup':
        """Initialize a WafRulesResponseResultItemGroup object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WafRulesResponseResultItemGroup object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this WafRulesResponseResultItemGroup object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WafRulesResponseResultItemGroup') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WafRulesResponseResultItemGroup') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class WafRuleResponse():
    """
    waf rule response.

    :attr bool success: Was operation successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr WafRuleResponseResult result: Information about a Rule.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'WafRuleResponseResult') -> None:
        """
        Initialize a WafRuleResponse object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param WafRuleResponseResult result: Information about a Rule.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WafRuleResponse':
        """Initialize a WafRuleResponse object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in WafRuleResponse JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in WafRuleResponse JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in WafRuleResponse JSON')
        if 'result' in _dict:
            args['result'] = WafRuleResponseResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in WafRuleResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WafRuleResponse object from a json dictionary."""
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
        """Return a `str` version of this WafRuleResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WafRuleResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WafRuleResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class WafRulesResponse():
    """
    waf rule response.

    :attr bool success: Was operation successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr List[WafRulesResponseResultItem] result: Array of Rules.
    :attr WafRulesResponseResultInfo result_info: (optional) result information.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: List['WafRulesResponseResultItem'],
                 *,
                 result_info: 'WafRulesResponseResultInfo' = None) -> None:
        """
        Initialize a WafRulesResponse object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param List[WafRulesResponseResultItem] result: Array of Rules.
        :param WafRulesResponseResultInfo result_info: (optional) result
               information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result
        self.result_info = result_info

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WafRulesResponse':
        """Initialize a WafRulesResponse object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in WafRulesResponse JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in WafRulesResponse JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in WafRulesResponse JSON')
        if 'result' in _dict:
            args['result'] = [WafRulesResponseResultItem.from_dict(x) for x in _dict.get('result')]
        else:
            raise ValueError('Required property \'result\' not present in WafRulesResponse JSON')
        if 'result_info' in _dict:
            args['result_info'] = WafRulesResponseResultInfo.from_dict(_dict.get('result_info'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WafRulesResponse object from a json dictionary."""
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
        """Return a `str` version of this WafRulesResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WafRulesResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WafRulesResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
