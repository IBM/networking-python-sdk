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
Global Load Balancer Healthcheck Events
"""

from datetime import datetime
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class GlobalLoadBalancerEventsV1(BaseService):
    """The Global Load Balancer Events V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'global_load_balancer_events'

    @classmethod
    def new_instance(cls,
                     crn: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'GlobalLoadBalancerEventsV1':
        """
        Return a new client for the Global Load Balancer Events service using the
               specified parameters and external configuration.

        :param str crn: Full url-encoded cloud resource name (CRN) of resource
               instance.
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
        Construct a new client for the Global Load Balancer Events service.

        :param str crn: Full url-encoded cloud resource name (CRN) of resource
               instance.

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
    # Global Load Balancer Events
    #########################


    def get_load_balancer_events(self,
        **kwargs
    ) -> DetailedResponse:
        """
        List all load balancer events.

        Get load balancer events for all origins.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListEventsResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_load_balancer_events')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/load_balancers/events'.format(
            *self.encode_path_vars(self.crn))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class ListEventsRespResultInfo():
    """
    result information.

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
        Initialize a ListEventsRespResultInfo object.

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
    def from_dict(cls, _dict: Dict) -> 'ListEventsRespResultInfo':
        """Initialize a ListEventsRespResultInfo object from a json dictionary."""
        args = {}
        if 'page' in _dict:
            args['page'] = _dict.get('page')
        else:
            raise ValueError('Required property \'page\' not present in ListEventsRespResultInfo JSON')
        if 'per_page' in _dict:
            args['per_page'] = _dict.get('per_page')
        else:
            raise ValueError('Required property \'per_page\' not present in ListEventsRespResultInfo JSON')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        else:
            raise ValueError('Required property \'count\' not present in ListEventsRespResultInfo JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in ListEventsRespResultInfo JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListEventsRespResultInfo object from a json dictionary."""
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
        """Return a `str` version of this ListEventsRespResultInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListEventsRespResultInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListEventsRespResultInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListEventsRespResultItem():
    """
    ListEventsRespResultItem.

    :attr str id: (optional) ID of the event.
    :attr datetime timestamp: (optional) Time of the event.
    :attr List[ListEventsRespResultItemPoolItem] pool: (optional) Pool information.
    :attr List[ListEventsRespResultItemOriginsItem] origins: (optional) Load
          balancer origins.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 timestamp: datetime = None,
                 pool: List['ListEventsRespResultItemPoolItem'] = None,
                 origins: List['ListEventsRespResultItemOriginsItem'] = None) -> None:
        """
        Initialize a ListEventsRespResultItem object.

        :param str id: (optional) ID of the event.
        :param datetime timestamp: (optional) Time of the event.
        :param List[ListEventsRespResultItemPoolItem] pool: (optional) Pool
               information.
        :param List[ListEventsRespResultItemOriginsItem] origins: (optional) Load
               balancer origins.
        """
        self.id = id
        self.timestamp = timestamp
        self.pool = pool
        self.origins = origins

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListEventsRespResultItem':
        """Initialize a ListEventsRespResultItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'timestamp' in _dict:
            args['timestamp'] = string_to_datetime(_dict.get('timestamp'))
        if 'pool' in _dict:
            args['pool'] = [ListEventsRespResultItemPoolItem.from_dict(x) for x in _dict.get('pool')]
        if 'origins' in _dict:
            args['origins'] = [ListEventsRespResultItemOriginsItem.from_dict(x) for x in _dict.get('origins')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListEventsRespResultItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'timestamp') and self.timestamp is not None:
            _dict['timestamp'] = datetime_to_string(self.timestamp)
        if hasattr(self, 'pool') and self.pool is not None:
            _dict['pool'] = [x.to_dict() for x in self.pool]
        if hasattr(self, 'origins') and self.origins is not None:
            _dict['origins'] = [x.to_dict() for x in self.origins]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListEventsRespResultItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListEventsRespResultItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListEventsRespResultItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListEventsRespResultItemOriginsItem():
    """
    ListEventsRespResultItemOriginsItem.

    :attr str name: (optional) Origin name.
    :attr str address: (optional) Origin address.
    :attr str ip: (optional) Origin id.
    :attr bool enabled: (optional) Origin enabled.
    :attr bool healthy: (optional) Origin healthy.
    :attr str failure_reason: (optional) Origin failure reason.
    :attr bool changed: (optional) Origin changed.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 address: str = None,
                 ip: str = None,
                 enabled: bool = None,
                 healthy: bool = None,
                 failure_reason: str = None,
                 changed: bool = None) -> None:
        """
        Initialize a ListEventsRespResultItemOriginsItem object.

        :param str name: (optional) Origin name.
        :param str address: (optional) Origin address.
        :param str ip: (optional) Origin id.
        :param bool enabled: (optional) Origin enabled.
        :param bool healthy: (optional) Origin healthy.
        :param str failure_reason: (optional) Origin failure reason.
        :param bool changed: (optional) Origin changed.
        """
        self.name = name
        self.address = address
        self.ip = ip
        self.enabled = enabled
        self.healthy = healthy
        self.failure_reason = failure_reason
        self.changed = changed

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListEventsRespResultItemOriginsItem':
        """Initialize a ListEventsRespResultItemOriginsItem object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'address' in _dict:
            args['address'] = _dict.get('address')
        if 'ip' in _dict:
            args['ip'] = _dict.get('ip')
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'healthy' in _dict:
            args['healthy'] = _dict.get('healthy')
        if 'failure_reason' in _dict:
            args['failure_reason'] = _dict.get('failure_reason')
        if 'changed' in _dict:
            args['changed'] = _dict.get('changed')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListEventsRespResultItemOriginsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'address') and self.address is not None:
            _dict['address'] = self.address
        if hasattr(self, 'ip') and self.ip is not None:
            _dict['ip'] = self.ip
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'healthy') and self.healthy is not None:
            _dict['healthy'] = self.healthy
        if hasattr(self, 'failure_reason') and self.failure_reason is not None:
            _dict['failure_reason'] = self.failure_reason
        if hasattr(self, 'changed') and self.changed is not None:
            _dict['changed'] = self.changed
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListEventsRespResultItemOriginsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListEventsRespResultItemOriginsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListEventsRespResultItemOriginsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListEventsRespResultItemPoolItem():
    """
    ListEventsRespResultItemPoolItem.

    :attr str id: (optional) Pool id.
    :attr str name: (optional) Pool name.
    :attr bool healthy: (optional) Pool is healthy.
    :attr bool changed: (optional) Pool changed.
    :attr int minimum_origins: (optional) Minimum origins.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 name: str = None,
                 healthy: bool = None,
                 changed: bool = None,
                 minimum_origins: int = None) -> None:
        """
        Initialize a ListEventsRespResultItemPoolItem object.

        :param str id: (optional) Pool id.
        :param str name: (optional) Pool name.
        :param bool healthy: (optional) Pool is healthy.
        :param bool changed: (optional) Pool changed.
        :param int minimum_origins: (optional) Minimum origins.
        """
        self.id = id
        self.name = name
        self.healthy = healthy
        self.changed = changed
        self.minimum_origins = minimum_origins

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListEventsRespResultItemPoolItem':
        """Initialize a ListEventsRespResultItemPoolItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'healthy' in _dict:
            args['healthy'] = _dict.get('healthy')
        if 'changed' in _dict:
            args['changed'] = _dict.get('changed')
        if 'minimum_origins' in _dict:
            args['minimum_origins'] = _dict.get('minimum_origins')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListEventsRespResultItemPoolItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'healthy') and self.healthy is not None:
            _dict['healthy'] = self.healthy
        if hasattr(self, 'changed') and self.changed is not None:
            _dict['changed'] = self.changed
        if hasattr(self, 'minimum_origins') and self.minimum_origins is not None:
            _dict['minimum_origins'] = self.minimum_origins
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListEventsRespResultItemPoolItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListEventsRespResultItemPoolItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListEventsRespResultItemPoolItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListEventsResp():
    """
    events list response object.

    :attr bool success: Was the get successful.
    :attr List[ListEventsRespResultItem] result: Result of the operation.
    :attr ListEventsRespResultInfo result_info: result information.
    :attr List[List[str]] errors: Array of errors returned.
    :attr List[List[str]] messages: Array of messages returned.
    """

    def __init__(self,
                 success: bool,
                 result: List['ListEventsRespResultItem'],
                 result_info: 'ListEventsRespResultInfo',
                 errors: List[List[str]],
                 messages: List[List[str]]) -> None:
        """
        Initialize a ListEventsResp object.

        :param bool success: Was the get successful.
        :param List[ListEventsRespResultItem] result: Result of the operation.
        :param ListEventsRespResultInfo result_info: result information.
        :param List[List[str]] errors: Array of errors returned.
        :param List[List[str]] messages: Array of messages returned.
        """
        self.success = success
        self.result = result
        self.result_info = result_info
        self.errors = errors
        self.messages = messages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListEventsResp':
        """Initialize a ListEventsResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in ListEventsResp JSON')
        if 'result' in _dict:
            args['result'] = [ListEventsRespResultItem.from_dict(x) for x in _dict.get('result')]
        else:
            raise ValueError('Required property \'result\' not present in ListEventsResp JSON')
        if 'result_info' in _dict:
            args['result_info'] = ListEventsRespResultInfo.from_dict(_dict.get('result_info'))
        else:
            raise ValueError('Required property \'result_info\' not present in ListEventsResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in ListEventsResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in ListEventsResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListEventsResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'result') and self.result is not None:
            _dict['result'] = [x.to_dict() for x in self.result]
        if hasattr(self, 'result_info') and self.result_info is not None:
            _dict['result_info'] = self.result_info.to_dict()
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = self.messages
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListEventsResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListEventsResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListEventsResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
