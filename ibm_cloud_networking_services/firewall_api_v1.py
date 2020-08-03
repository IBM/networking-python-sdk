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
Firewall API
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

class FirewallApiV1(BaseService):
    """The Firewall  API V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'firewall_api'

    @classmethod
    def new_instance(cls,
                     crn: str,
                     zone_identifier: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'FirewallApiV1':
        """
        Return a new client for the Firewall  API service using the specified
               parameters and external configuration.

        :param str crn: cloud resource name.

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

    def __init__(self,
                 crn: str,
                 zone_identifier: str,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the Firewall  API service.

        :param str crn: cloud resource name.

        :param str zone_identifier: zone identifier.

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
    # Security Level Setting
    #########################


    def get_security_level_setting(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Get security level setting.

        For a given zone identifier, get security level setting.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SecurityLevelSettingResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_security_level_setting')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/security_level'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def set_security_level_setting(self,
        *,
        value: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Set security level setting.

        For a given zone identifier, set security level setting.

        :param str value: (optional) security level.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SecurityLevelSettingResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='set_security_level_setting')
        headers.update(sdk_headers)

        data = {
            'value': value
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/settings/security_level'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class SecurityLevelSettingRespMessagesItem():
    """
    SecurityLevelSettingRespMessagesItem.

    :attr str status: (optional) messages.
    """

    def __init__(self,
                 *,
                 status: str = None) -> None:
        """
        Initialize a SecurityLevelSettingRespMessagesItem object.

        :param str status: (optional) messages.
        """
        self.status = status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SecurityLevelSettingRespMessagesItem':
        """Initialize a SecurityLevelSettingRespMessagesItem object from a json dictionary."""
        args = {}
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SecurityLevelSettingRespMessagesItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SecurityLevelSettingRespMessagesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SecurityLevelSettingRespMessagesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SecurityLevelSettingRespMessagesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SecurityLevelSettingRespResult():
    """
    result object.

    :attr str id: identifier.
    :attr str value: value.
    :attr bool editable: editable.
    :attr str modified_on: modified date.
    """

    def __init__(self,
                 id: str,
                 value: str,
                 editable: bool,
                 modified_on: str) -> None:
        """
        Initialize a SecurityLevelSettingRespResult object.

        :param str id: identifier.
        :param str value: value.
        :param bool editable: editable.
        :param str modified_on: modified date.
        """
        self.id = id
        self.value = value
        self.editable = editable
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SecurityLevelSettingRespResult':
        """Initialize a SecurityLevelSettingRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in SecurityLevelSettingRespResult JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in SecurityLevelSettingRespResult JSON')
        if 'editable' in _dict:
            args['editable'] = _dict.get('editable')
        else:
            raise ValueError('Required property \'editable\' not present in SecurityLevelSettingRespResult JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        else:
            raise ValueError('Required property \'modified_on\' not present in SecurityLevelSettingRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SecurityLevelSettingRespResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'editable') and self.editable is not None:
            _dict['editable'] = self.editable
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = self.modified_on
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SecurityLevelSettingRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SecurityLevelSettingRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SecurityLevelSettingRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class IdEnum(str, Enum):
        """
        identifier.
        """
        SECURITY_LEVEL = 'security_level'


class ResultInfo():
    """
    result information.

    :attr int page: output pages.
    :attr int per_page: output per page.
    :attr int count: firewall hit count.
    :attr int total_count: total count.
    """

    def __init__(self,
                 page: int,
                 per_page: int,
                 count: int,
                 total_count: int) -> None:
        """
        Initialize a ResultInfo object.

        :param int page: output pages.
        :param int per_page: output per page.
        :param int count: firewall hit count.
        :param int total_count: total count.
        """
        self.page = page
        self.per_page = per_page
        self.count = count
        self.total_count = total_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResultInfo':
        """Initialize a ResultInfo object from a json dictionary."""
        args = {}
        if 'page' in _dict:
            args['page'] = _dict.get('page')
        else:
            raise ValueError('Required property \'page\' not present in ResultInfo JSON')
        if 'per_page' in _dict:
            args['per_page'] = _dict.get('per_page')
        else:
            raise ValueError('Required property \'per_page\' not present in ResultInfo JSON')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        else:
            raise ValueError('Required property \'count\' not present in ResultInfo JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in ResultInfo JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResultInfo object from a json dictionary."""
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
        """Return a `str` version of this ResultInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResultInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResultInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SecurityLevelSettingResp():
    """
    security level setting response.

    :attr SecurityLevelSettingRespResult result: result object.
    :attr ResultInfo result_info: result information.
    :attr bool success: success response.
    :attr List[List[str]] errors: array of errors.
    :attr List[SecurityLevelSettingRespMessagesItem] messages: array of messages.
    """

    def __init__(self,
                 result: 'SecurityLevelSettingRespResult',
                 result_info: 'ResultInfo',
                 success: bool,
                 errors: List[List[str]],
                 messages: List['SecurityLevelSettingRespMessagesItem']) -> None:
        """
        Initialize a SecurityLevelSettingResp object.

        :param SecurityLevelSettingRespResult result: result object.
        :param ResultInfo result_info: result information.
        :param bool success: success response.
        :param List[List[str]] errors: array of errors.
        :param List[SecurityLevelSettingRespMessagesItem] messages: array of
               messages.
        """
        self.result = result
        self.result_info = result_info
        self.success = success
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SecurityLevelSettingResp':
        """Initialize a SecurityLevelSettingResp object from a json dictionary."""
        args = {}
        if 'result' in _dict:
            args['result'] = SecurityLevelSettingRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in SecurityLevelSettingResp JSON')
        if 'result_info' in _dict:
            args['result_info'] = ResultInfo.from_dict(_dict.get('result_info'))
        else:
            raise ValueError('Required property \'result_info\' not present in SecurityLevelSettingResp JSON')
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in SecurityLevelSettingResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in SecurityLevelSettingResp JSON')
        if 'messages' in _dict:
            args['messages'] = [SecurityLevelSettingRespMessagesItem.from_dict(x) for x in _dict.get('messages')]
        else:
            raise ValueError('Required property \'messages\' not present in SecurityLevelSettingResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SecurityLevelSettingResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'result') and self.result is not None:
            _dict['result'] = self.result.to_dict()
        if hasattr(self, 'result_info') and self.result_info is not None:
            _dict['result_info'] = self.result_info.to_dict()
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = [x.to_dict() for x in self.messages]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SecurityLevelSettingResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SecurityLevelSettingResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SecurityLevelSettingResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
