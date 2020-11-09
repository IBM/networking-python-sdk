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
    # Zone Lockdown Rules
    #########################


    def list_all_zone_lockown_rules(self,
        *,
        page: int = None,
        per_page: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List all lockdown rules.

        List all lockdown rules for a zone.

        :param int page: (optional) Page number of paginated results.
        :param int per_page: (optional) Maximum number of lockdown rules per page.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListLockdownResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_all_zone_lockown_rules')
        headers.update(sdk_headers)

        params = {
            'page': page,
            'per_page': per_page
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/firewall/lockdowns'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_zone_lockdown_rule(self,
        *,
        urls: List[str] = None,
        configurations: List['LockdownInputConfigurationsItem'] = None,
        id: str = None,
        paused: bool = None,
        description: str = None,
        priority: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create lockdown rule.

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
        :param int priority: (optional) firewall priority.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LockdownResp` object
        """

        if configurations is not None:
            configurations = [convert_model(x) for x in configurations]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_zone_lockdown_rule')
        headers.update(sdk_headers)

        data = {
            'urls': urls,
            'configurations': configurations,
            'id': id,
            'paused': paused,
            'description': description,
            'priority': priority
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/firewall/lockdowns'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_zone_lockdown_rule(self,
        lockdown_rule_identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete lockdown rule.

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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_zone_lockdown_rule')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/firewall/lockdowns/{2}'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier, lockdown_rule_identifier))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_lockdown(self,
        lockdown_rule_identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get lockdown rule.

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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_lockdown')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/firewall/lockdowns/{2}'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier, lockdown_rule_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_lockdown_rule(self,
        lockdown_rule_identifier: str,
        *,
        urls: List[str] = None,
        configurations: List['LockdownInputConfigurationsItem'] = None,
        id: str = None,
        paused: bool = None,
        description: str = None,
        priority: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update lockdown rule.

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
        :param int priority: (optional) firewall priority.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LockdownResp` object
        """

        if lockdown_rule_identifier is None:
            raise ValueError('lockdown_rule_identifier must be provided')
        if configurations is not None:
            configurations = [convert_model(x) for x in configurations]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_lockdown_rule')
        headers.update(sdk_headers)

        data = {
            'urls': urls,
            'configurations': configurations,
            'id': id,
            'paused': paused,
            'description': description,
            'priority': priority
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/firewall/lockdowns/{2}'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier, lockdown_rule_identifier))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class DeleteLockdownRespResult():
    """
    Container for response information.

    :attr str id: ID.
    """

    def __init__(self,
                 id: str) -> None:
        """
        Initialize a DeleteLockdownRespResult object.

        :param str id: ID.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteLockdownRespResult':
        """Initialize a DeleteLockdownRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in DeleteLockdownRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteLockdownRespResult object from a json dictionary."""
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
        """Return a `str` version of this DeleteLockdownRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteLockdownRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteLockdownRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListLockdownRespResultInfo():
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
        Initialize a ListLockdownRespResultInfo object.

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
    def from_dict(cls, _dict: Dict) -> 'ListLockdownRespResultInfo':
        """Initialize a ListLockdownRespResultInfo object from a json dictionary."""
        args = {}
        if 'page' in _dict:
            args['page'] = _dict.get('page')
        else:
            raise ValueError('Required property \'page\' not present in ListLockdownRespResultInfo JSON')
        if 'per_page' in _dict:
            args['per_page'] = _dict.get('per_page')
        else:
            raise ValueError('Required property \'per_page\' not present in ListLockdownRespResultInfo JSON')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        else:
            raise ValueError('Required property \'count\' not present in ListLockdownRespResultInfo JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in ListLockdownRespResultInfo JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListLockdownRespResultInfo object from a json dictionary."""
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
        """Return a `str` version of this ListLockdownRespResultInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListLockdownRespResultInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListLockdownRespResultInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class LockdownInputConfigurationsItem():
    """
    LockdownInputConfigurationsItem.

    :attr str target: properties.
    :attr str value: IP addresses or CIDR, if target is "ip", then value should be
          an IP addresses, otherwise CIDR.
    """

    def __init__(self,
                 target: str,
                 value: str) -> None:
        """
        Initialize a LockdownInputConfigurationsItem object.

        :param str target: properties.
        :param str value: IP addresses or CIDR, if target is "ip", then value
               should be an IP addresses, otherwise CIDR.
        """
        self.target = target
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LockdownInputConfigurationsItem':
        """Initialize a LockdownInputConfigurationsItem object from a json dictionary."""
        args = {}
        if 'target' in _dict:
            args['target'] = _dict.get('target')
        else:
            raise ValueError('Required property \'target\' not present in LockdownInputConfigurationsItem JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in LockdownInputConfigurationsItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LockdownInputConfigurationsItem object from a json dictionary."""
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
        """Return a `str` version of this LockdownInputConfigurationsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LockdownInputConfigurationsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LockdownInputConfigurationsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TargetEnum(str, Enum):
        """
        properties.
        """
        IP = 'ip'
        IP_RANGE = 'ip_range'


class LockdownObjectConfigurationsItem():
    """
    LockdownObjectConfigurationsItem.

    :attr str target: target.
    :attr str value: IP addresses or CIDR, if target is "ip", then value should be
          an IP addresses, otherwise CIDR.
    """

    def __init__(self,
                 target: str,
                 value: str) -> None:
        """
        Initialize a LockdownObjectConfigurationsItem object.

        :param str target: target.
        :param str value: IP addresses or CIDR, if target is "ip", then value
               should be an IP addresses, otherwise CIDR.
        """
        self.target = target
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LockdownObjectConfigurationsItem':
        """Initialize a LockdownObjectConfigurationsItem object from a json dictionary."""
        args = {}
        if 'target' in _dict:
            args['target'] = _dict.get('target')
        else:
            raise ValueError('Required property \'target\' not present in LockdownObjectConfigurationsItem JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in LockdownObjectConfigurationsItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LockdownObjectConfigurationsItem object from a json dictionary."""
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
        """Return a `str` version of this LockdownObjectConfigurationsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LockdownObjectConfigurationsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LockdownObjectConfigurationsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TargetEnum(str, Enum):
        """
        target.
        """
        IP = 'ip'
        IP_RANGE = 'ip_range'


class DeleteLockdownResp():
    """
    delete lockdown response.

    :attr bool success: Operation success flag.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr DeleteLockdownRespResult result: Container for response information.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'DeleteLockdownRespResult') -> None:
        """
        Initialize a DeleteLockdownResp object.

        :param bool success: Operation success flag.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param DeleteLockdownRespResult result: Container for response information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteLockdownResp':
        """Initialize a DeleteLockdownResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in DeleteLockdownResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in DeleteLockdownResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in DeleteLockdownResp JSON')
        if 'result' in _dict:
            args['result'] = DeleteLockdownRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in DeleteLockdownResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteLockdownResp object from a json dictionary."""
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
        """Return a `str` version of this DeleteLockdownResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteLockdownResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteLockdownResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListLockdownResp():
    """
    list lockdown response.

    :attr bool success: Was operation successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr List[LockdownObject] result: Container for response information.
    :attr ListLockdownRespResultInfo result_info: Statistics of results.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: List['LockdownObject'],
                 result_info: 'ListLockdownRespResultInfo') -> None:
        """
        Initialize a ListLockdownResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param List[LockdownObject] result: Container for response information.
        :param ListLockdownRespResultInfo result_info: Statistics of results.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result
        self.result_info = result_info

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListLockdownResp':
        """Initialize a ListLockdownResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in ListLockdownResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in ListLockdownResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in ListLockdownResp JSON')
        if 'result' in _dict:
            args['result'] = [LockdownObject.from_dict(x) for x in _dict.get('result')]
        else:
            raise ValueError('Required property \'result\' not present in ListLockdownResp JSON')
        if 'result_info' in _dict:
            args['result_info'] = ListLockdownRespResultInfo.from_dict(_dict.get('result_info'))
        else:
            raise ValueError('Required property \'result_info\' not present in ListLockdownResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListLockdownResp object from a json dictionary."""
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
        """Return a `str` version of this ListLockdownResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListLockdownResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListLockdownResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class LockdownObject():
    """
    lockdown object.

    :attr str id: Lockdown rule identifier.
    :attr int priority: (optional) firewall priority.
    :attr bool paused: Whether this zone lockdown is currently paused.
    :attr str description: A note that you can use to describe the reason for a
          Lockdown rule.
    :attr List[str] urls: URLs to be included in this rule definition. Wildcards are
          permitted. The URL pattern entered here will be escaped before use. This limits
          the URL to just simple wildcard patterns.
    :attr List[LockdownObjectConfigurationsItem] configurations: List of IP
          addresses or CIDR ranges to use for this rule. This can include any number of ip
          or ip_range configurations that can access the provided URLs.
    """

    def __init__(self,
                 id: str,
                 paused: bool,
                 description: str,
                 urls: List[str],
                 configurations: List['LockdownObjectConfigurationsItem'],
                 *,
                 priority: int = None) -> None:
        """
        Initialize a LockdownObject object.

        :param str id: Lockdown rule identifier.
        :param bool paused: Whether this zone lockdown is currently paused.
        :param str description: A note that you can use to describe the reason for
               a Lockdown rule.
        :param List[str] urls: URLs to be included in this rule definition.
               Wildcards are permitted. The URL pattern entered here will be escaped
               before use. This limits the URL to just simple wildcard patterns.
        :param List[LockdownObjectConfigurationsItem] configurations: List of IP
               addresses or CIDR ranges to use for this rule. This can include any number
               of ip or ip_range configurations that can access the provided URLs.
        :param int priority: (optional) firewall priority.
        """
        self.id = id
        self.priority = priority
        self.paused = paused
        self.description = description
        self.urls = urls
        self.configurations = configurations

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LockdownObject':
        """Initialize a LockdownObject object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in LockdownObject JSON')
        if 'priority' in _dict:
            args['priority'] = _dict.get('priority')
        if 'paused' in _dict:
            args['paused'] = _dict.get('paused')
        else:
            raise ValueError('Required property \'paused\' not present in LockdownObject JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError('Required property \'description\' not present in LockdownObject JSON')
        if 'urls' in _dict:
            args['urls'] = _dict.get('urls')
        else:
            raise ValueError('Required property \'urls\' not present in LockdownObject JSON')
        if 'configurations' in _dict:
            args['configurations'] = [LockdownObjectConfigurationsItem.from_dict(x) for x in _dict.get('configurations')]
        else:
            raise ValueError('Required property \'configurations\' not present in LockdownObject JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LockdownObject object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'priority') and self.priority is not None:
            _dict['priority'] = self.priority
        if hasattr(self, 'paused') and self.paused is not None:
            _dict['paused'] = self.paused
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'urls') and self.urls is not None:
            _dict['urls'] = self.urls
        if hasattr(self, 'configurations') and self.configurations is not None:
            _dict['configurations'] = [x.to_dict() for x in self.configurations]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LockdownObject object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LockdownObject') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LockdownObject') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class LockdownResp():
    """
    lockdown response.

    :attr bool success: Was operation successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr LockdownObject result: lockdown object.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'LockdownObject') -> None:
        """
        Initialize a LockdownResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param LockdownObject result: lockdown object.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LockdownResp':
        """Initialize a LockdownResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in LockdownResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in LockdownResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in LockdownResp JSON')
        if 'result' in _dict:
            args['result'] = LockdownObject.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in LockdownResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LockdownResp object from a json dictionary."""
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
        """Return a `str` version of this LockdownResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LockdownResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LockdownResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
