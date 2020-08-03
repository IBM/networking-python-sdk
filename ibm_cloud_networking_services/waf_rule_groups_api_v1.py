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
    # WAF Rule Groups
    #########################


    def list_waf_rule_groups(self,
        pkg_id: str,
        *,
        name: str = None,
        mode: str = None,
        rules_count: str = None,
        page: int = None,
        per_page: int = None,
        order: str = None,
        direction: str = None,
        match: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List all WAF rule groups.

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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_waf_rule_groups')
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

        url = '/v1/{0}/zones/{1}/firewall/waf/packages/{2}/groups'.format(
            *self.encode_path_vars(self.crn, self.zone_id, pkg_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def get_waf_rule_group(self,
        pkg_id: str,
        group_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get WAF rule group.

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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_waf_rule_group')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/firewall/waf/packages/{2}/groups/{3}'.format(
            *self.encode_path_vars(self.crn, self.zone_id, pkg_id, group_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_waf_rule_group(self,
        pkg_id: str,
        group_id: str,
        *,
        mode: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update WAF rule group.

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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_waf_rule_group')
        headers.update(sdk_headers)

        data = {
            'mode': mode
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/firewall/waf/packages/{2}/groups/{3}'.format(
            *self.encode_path_vars(self.crn, self.zone_id, pkg_id, group_id))
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

    class Mode(str, Enum):
        """
        Whether or not the rules contained within this group are configurable/usable.
        """
        ON = 'on'
        OFF = 'off'
    class Direction(str, Enum):
        """
        Direction to order packages.
        """
        DESC = 'desc'
        ASC = 'asc'
    class Match(str, Enum):
        """
        Whether to match all search requirements or at least one (any).
        """
        ALL = 'all'
        ANY = 'any'


##############################################################################
# Models
##############################################################################


class WafGroupResponseResultInfo():
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
        Initialize a WafGroupResponseResultInfo object.

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
    def from_dict(cls, _dict: Dict) -> 'WafGroupResponseResultInfo':
        """Initialize a WafGroupResponseResultInfo object from a json dictionary."""
        args = {}
        if 'page' in _dict:
            args['page'] = _dict.get('page')
        else:
            raise ValueError('Required property \'page\' not present in WafGroupResponseResultInfo JSON')
        if 'per_page' in _dict:
            args['per_page'] = _dict.get('per_page')
        else:
            raise ValueError('Required property \'per_page\' not present in WafGroupResponseResultInfo JSON')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        else:
            raise ValueError('Required property \'count\' not present in WafGroupResponseResultInfo JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in WafGroupResponseResultInfo JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WafGroupResponseResultInfo object from a json dictionary."""
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
        """Return a `str` version of this WafGroupResponseResultInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WafGroupResponseResultInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WafGroupResponseResultInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class WafGroupsResponseResultInfo():
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
        Initialize a WafGroupsResponseResultInfo object.

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
    def from_dict(cls, _dict: Dict) -> 'WafGroupsResponseResultInfo':
        """Initialize a WafGroupsResponseResultInfo object from a json dictionary."""
        args = {}
        if 'page' in _dict:
            args['page'] = _dict.get('page')
        else:
            raise ValueError('Required property \'page\' not present in WafGroupsResponseResultInfo JSON')
        if 'per_page' in _dict:
            args['per_page'] = _dict.get('per_page')
        else:
            raise ValueError('Required property \'per_page\' not present in WafGroupsResponseResultInfo JSON')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        else:
            raise ValueError('Required property \'count\' not present in WafGroupsResponseResultInfo JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in WafGroupsResponseResultInfo JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WafGroupsResponseResultInfo object from a json dictionary."""
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
        """Return a `str` version of this WafGroupsResponseResultInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WafGroupsResponseResultInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WafGroupsResponseResultInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class WafGroupResponse():
    """
    waf group response.

    :attr bool success: Was operation successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr WafRuleProperties result: waf rule properties.
    :attr WafGroupResponseResultInfo result_info: Statistics of results.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'WafRuleProperties',
                 result_info: 'WafGroupResponseResultInfo') -> None:
        """
        Initialize a WafGroupResponse object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param WafRuleProperties result: waf rule properties.
        :param WafGroupResponseResultInfo result_info: Statistics of results.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result
        self.result_info = result_info

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WafGroupResponse':
        """Initialize a WafGroupResponse object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in WafGroupResponse JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in WafGroupResponse JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in WafGroupResponse JSON')
        if 'result' in _dict:
            args['result'] = WafRuleProperties.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in WafGroupResponse JSON')
        if 'result_info' in _dict:
            args['result_info'] = WafGroupResponseResultInfo.from_dict(_dict.get('result_info'))
        else:
            raise ValueError('Required property \'result_info\' not present in WafGroupResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WafGroupResponse object from a json dictionary."""
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
        if hasattr(self, 'result_info') and self.result_info is not None:
            _dict['result_info'] = self.result_info.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this WafGroupResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WafGroupResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WafGroupResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class WafGroupsResponse():
    """
    waf groups response.

    :attr bool success: Was operation successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr List[WafRuleProperties] result: Container for response information.
    :attr WafGroupsResponseResultInfo result_info: Statistics of results.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: List['WafRuleProperties'],
                 result_info: 'WafGroupsResponseResultInfo') -> None:
        """
        Initialize a WafGroupsResponse object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param List[WafRuleProperties] result: Container for response information.
        :param WafGroupsResponseResultInfo result_info: Statistics of results.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result
        self.result_info = result_info

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WafGroupsResponse':
        """Initialize a WafGroupsResponse object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in WafGroupsResponse JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in WafGroupsResponse JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in WafGroupsResponse JSON')
        if 'result' in _dict:
            args['result'] = [WafRuleProperties.from_dict(x) for x in _dict.get('result')]
        else:
            raise ValueError('Required property \'result\' not present in WafGroupsResponse JSON')
        if 'result_info' in _dict:
            args['result_info'] = WafGroupsResponseResultInfo.from_dict(_dict.get('result_info'))
        else:
            raise ValueError('Required property \'result_info\' not present in WafGroupsResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WafGroupsResponse object from a json dictionary."""
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
        """Return a `str` version of this WafGroupsResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WafGroupsResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WafGroupsResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class WafRuleProperties():
    """
    waf rule properties.

    :attr str id: (optional) ID.
    :attr str name: (optional) Name.
    :attr str description: (optional) Description.
    :attr int rules_count: (optional) Number of rules.
    :attr int modified_rules_count: (optional) Number of modified rules.
    :attr str package_id: (optional) Package ID.
    :attr str mode: (optional) Mode.
    :attr List[str] allowed_modes: (optional) Allowed Modes.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 name: str = None,
                 description: str = None,
                 rules_count: int = None,
                 modified_rules_count: int = None,
                 package_id: str = None,
                 mode: str = None,
                 allowed_modes: List[str] = None) -> None:
        """
        Initialize a WafRuleProperties object.

        :param str id: (optional) ID.
        :param str name: (optional) Name.
        :param str description: (optional) Description.
        :param int rules_count: (optional) Number of rules.
        :param int modified_rules_count: (optional) Number of modified rules.
        :param str package_id: (optional) Package ID.
        :param str mode: (optional) Mode.
        :param List[str] allowed_modes: (optional) Allowed Modes.
        """
        self.id = id
        self.name = name
        self.description = description
        self.rules_count = rules_count
        self.modified_rules_count = modified_rules_count
        self.package_id = package_id
        self.mode = mode
        self.allowed_modes = allowed_modes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WafRuleProperties':
        """Initialize a WafRuleProperties object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'rules_count' in _dict:
            args['rules_count'] = _dict.get('rules_count')
        if 'modified_rules_count' in _dict:
            args['modified_rules_count'] = _dict.get('modified_rules_count')
        if 'package_id' in _dict:
            args['package_id'] = _dict.get('package_id')
        if 'mode' in _dict:
            args['mode'] = _dict.get('mode')
        if 'allowed_modes' in _dict:
            args['allowed_modes'] = _dict.get('allowed_modes')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WafRuleProperties object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'rules_count') and self.rules_count is not None:
            _dict['rules_count'] = self.rules_count
        if hasattr(self, 'modified_rules_count') and self.modified_rules_count is not None:
            _dict['modified_rules_count'] = self.modified_rules_count
        if hasattr(self, 'package_id') and self.package_id is not None:
            _dict['package_id'] = self.package_id
        if hasattr(self, 'mode') and self.mode is not None:
            _dict['mode'] = self.mode
        if hasattr(self, 'allowed_modes') and self.allowed_modes is not None:
            _dict['allowed_modes'] = self.allowed_modes
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this WafRuleProperties object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WafRuleProperties') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WafRuleProperties') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
