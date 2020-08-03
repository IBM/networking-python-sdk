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


    def list_all_zone_user_agent_rules(self,
        *,
        page: int = None,
        per_page: int = None,
        **kwargs
    ) -> DetailedResponse:
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_all_zone_user_agent_rules')
        headers.update(sdk_headers)

        params = {
            'page': page,
            'per_page': per_page
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/firewall/ua_rules'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_zone_user_agent_rule(self,
        *,
        mode: str = None,
        configuration: 'UseragentRuleInputConfiguration' = None,
        paused: bool = None,
        description: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create user-agent blocking rule.

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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_zone_user_agent_rule')
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

        url = '/v1/{0}/zones/{1}/firewall/ua_rules'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_zone_user_agent_rule(self,
        useragent_rule_identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete user-agent blocking rule.

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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_zone_user_agent_rule')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/firewall/ua_rules/{2}'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier, useragent_rule_identifier))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_user_agent_rule(self,
        useragent_rule_identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get user-agent blocking rule.

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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_user_agent_rule')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/firewall/ua_rules/{2}'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier, useragent_rule_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_user_agent_rule(self,
        useragent_rule_identifier: str,
        *,
        mode: str = None,
        configuration: 'UseragentRuleInputConfiguration' = None,
        paused: bool = None,
        description: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update user-agent blocking rule.

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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_user_agent_rule')
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

        url = '/v1/{0}/zones/{1}/firewall/ua_rules/{2}'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier, useragent_rule_identifier))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class DeleteUseragentRuleRespResult():
    """
    Container for response information.

    :attr str id: ID.
    """

    def __init__(self,
                 id: str) -> None:
        """
        Initialize a DeleteUseragentRuleRespResult object.

        :param str id: ID.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteUseragentRuleRespResult':
        """Initialize a DeleteUseragentRuleRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in DeleteUseragentRuleRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteUseragentRuleRespResult object from a json dictionary."""
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
        """Return a `str` version of this DeleteUseragentRuleRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteUseragentRuleRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteUseragentRuleRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListUseragentRulesRespResultInfo():
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
        Initialize a ListUseragentRulesRespResultInfo object.

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
    def from_dict(cls, _dict: Dict) -> 'ListUseragentRulesRespResultInfo':
        """Initialize a ListUseragentRulesRespResultInfo object from a json dictionary."""
        args = {}
        if 'page' in _dict:
            args['page'] = _dict.get('page')
        else:
            raise ValueError('Required property \'page\' not present in ListUseragentRulesRespResultInfo JSON')
        if 'per_page' in _dict:
            args['per_page'] = _dict.get('per_page')
        else:
            raise ValueError('Required property \'per_page\' not present in ListUseragentRulesRespResultInfo JSON')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        else:
            raise ValueError('Required property \'count\' not present in ListUseragentRulesRespResultInfo JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in ListUseragentRulesRespResultInfo JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListUseragentRulesRespResultInfo object from a json dictionary."""
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
        """Return a `str` version of this ListUseragentRulesRespResultInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListUseragentRulesRespResultInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListUseragentRulesRespResultInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class UseragentRuleInputConfiguration():
    """
    Target/Value pair to use for this rule. The value is the exact UserAgent to match.

    :attr str target: properties.
    :attr str value: The exact UserAgent string to match with this rule.
    """

    def __init__(self,
                 target: str,
                 value: str) -> None:
        """
        Initialize a UseragentRuleInputConfiguration object.

        :param str target: properties.
        :param str value: The exact UserAgent string to match with this rule.
        """
        self.target = target
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UseragentRuleInputConfiguration':
        """Initialize a UseragentRuleInputConfiguration object from a json dictionary."""
        args = {}
        if 'target' in _dict:
            args['target'] = _dict.get('target')
        else:
            raise ValueError('Required property \'target\' not present in UseragentRuleInputConfiguration JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in UseragentRuleInputConfiguration JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UseragentRuleInputConfiguration object from a json dictionary."""
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
        """Return a `str` version of this UseragentRuleInputConfiguration object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UseragentRuleInputConfiguration') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UseragentRuleInputConfiguration') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TargetEnum(str, Enum):
        """
        properties.
        """
        UA = 'ua'


class UseragentRuleObjectConfiguration():
    """
    Target/Value pair to use for this rule. The value is the exact UserAgent to match.

    :attr str target: properties.
    :attr str value: The exact UserAgent string to match with this rule.
    """

    def __init__(self,
                 target: str,
                 value: str) -> None:
        """
        Initialize a UseragentRuleObjectConfiguration object.

        :param str target: properties.
        :param str value: The exact UserAgent string to match with this rule.
        """
        self.target = target
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UseragentRuleObjectConfiguration':
        """Initialize a UseragentRuleObjectConfiguration object from a json dictionary."""
        args = {}
        if 'target' in _dict:
            args['target'] = _dict.get('target')
        else:
            raise ValueError('Required property \'target\' not present in UseragentRuleObjectConfiguration JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in UseragentRuleObjectConfiguration JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UseragentRuleObjectConfiguration object from a json dictionary."""
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
        """Return a `str` version of this UseragentRuleObjectConfiguration object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UseragentRuleObjectConfiguration') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UseragentRuleObjectConfiguration') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TargetEnum(str, Enum):
        """
        properties.
        """
        UA = 'ua'


class DeleteUseragentRuleResp():
    """
    user agent delete response.

    :attr bool success: Operation success flag.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr DeleteUseragentRuleRespResult result: Container for response information.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'DeleteUseragentRuleRespResult') -> None:
        """
        Initialize a DeleteUseragentRuleResp object.

        :param bool success: Operation success flag.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param DeleteUseragentRuleRespResult result: Container for response
               information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteUseragentRuleResp':
        """Initialize a DeleteUseragentRuleResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in DeleteUseragentRuleResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in DeleteUseragentRuleResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in DeleteUseragentRuleResp JSON')
        if 'result' in _dict:
            args['result'] = DeleteUseragentRuleRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in DeleteUseragentRuleResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteUseragentRuleResp object from a json dictionary."""
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
        """Return a `str` version of this DeleteUseragentRuleResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteUseragentRuleResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteUseragentRuleResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListUseragentRulesResp():
    """
    user agent rules response.

    :attr bool success: Was operation successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr List[UseragentRuleObject] result: Container for response information.
    :attr ListUseragentRulesRespResultInfo result_info: Statistics of results.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: List['UseragentRuleObject'],
                 result_info: 'ListUseragentRulesRespResultInfo') -> None:
        """
        Initialize a ListUseragentRulesResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param List[UseragentRuleObject] result: Container for response
               information.
        :param ListUseragentRulesRespResultInfo result_info: Statistics of results.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result
        self.result_info = result_info

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListUseragentRulesResp':
        """Initialize a ListUseragentRulesResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in ListUseragentRulesResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in ListUseragentRulesResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in ListUseragentRulesResp JSON')
        if 'result' in _dict:
            args['result'] = [UseragentRuleObject.from_dict(x) for x in _dict.get('result')]
        else:
            raise ValueError('Required property \'result\' not present in ListUseragentRulesResp JSON')
        if 'result_info' in _dict:
            args['result_info'] = ListUseragentRulesRespResultInfo.from_dict(_dict.get('result_info'))
        else:
            raise ValueError('Required property \'result_info\' not present in ListUseragentRulesResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListUseragentRulesResp object from a json dictionary."""
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
        """Return a `str` version of this ListUseragentRulesResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListUseragentRulesResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListUseragentRulesResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class UseragentRuleObject():
    """
    user agent rule object.

    :attr str id: Identifier of the user-agent blocking rule.
    :attr bool paused: Whether this user-agent rule is currently disabled.
    :attr str description: Some useful information about this rule to help identify
          the purpose of it.
    :attr str mode: The type of action to perform.
    :attr UseragentRuleObjectConfiguration configuration: Target/Value pair to use
          for this rule. The value is the exact UserAgent to match.
    """

    def __init__(self,
                 id: str,
                 paused: bool,
                 description: str,
                 mode: str,
                 configuration: 'UseragentRuleObjectConfiguration') -> None:
        """
        Initialize a UseragentRuleObject object.

        :param str id: Identifier of the user-agent blocking rule.
        :param bool paused: Whether this user-agent rule is currently disabled.
        :param str description: Some useful information about this rule to help
               identify the purpose of it.
        :param str mode: The type of action to perform.
        :param UseragentRuleObjectConfiguration configuration: Target/Value pair to
               use for this rule. The value is the exact UserAgent to match.
        """
        self.id = id
        self.paused = paused
        self.description = description
        self.mode = mode
        self.configuration = configuration

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UseragentRuleObject':
        """Initialize a UseragentRuleObject object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in UseragentRuleObject JSON')
        if 'paused' in _dict:
            args['paused'] = _dict.get('paused')
        else:
            raise ValueError('Required property \'paused\' not present in UseragentRuleObject JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError('Required property \'description\' not present in UseragentRuleObject JSON')
        if 'mode' in _dict:
            args['mode'] = _dict.get('mode')
        else:
            raise ValueError('Required property \'mode\' not present in UseragentRuleObject JSON')
        if 'configuration' in _dict:
            args['configuration'] = UseragentRuleObjectConfiguration.from_dict(_dict.get('configuration'))
        else:
            raise ValueError('Required property \'configuration\' not present in UseragentRuleObject JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UseragentRuleObject object from a json dictionary."""
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
        if hasattr(self, 'mode') and self.mode is not None:
            _dict['mode'] = self.mode
        if hasattr(self, 'configuration') and self.configuration is not None:
            _dict['configuration'] = self.configuration.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UseragentRuleObject object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UseragentRuleObject') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UseragentRuleObject') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ModeEnum(str, Enum):
        """
        The type of action to perform.
        """
        BLOCK = 'block'
        CHALLENGE = 'challenge'
        JS_CHALLENGE = 'js_challenge'


class UseragentRuleResp():
    """
    user agent rule response.

    :attr bool success: Was operation successful.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[List[str]] messages: Array of messages returned.
    :attr UseragentRuleObject result: user agent rule object.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'UseragentRuleObject') -> None:
        """
        Initialize a UseragentRuleResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[List[str]] messages: Array of messages returned.
        :param UseragentRuleObject result: user agent rule object.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UseragentRuleResp':
        """Initialize a UseragentRuleResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in UseragentRuleResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in UseragentRuleResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in UseragentRuleResp JSON')
        if 'result' in _dict:
            args['result'] = UseragentRuleObject.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in UseragentRuleResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UseragentRuleResp object from a json dictionary."""
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
        """Return a `str` version of this UseragentRuleResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UseragentRuleResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UseragentRuleResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
