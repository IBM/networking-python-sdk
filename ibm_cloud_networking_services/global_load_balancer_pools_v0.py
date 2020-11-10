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
GLB Pools
"""

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

class GlobalLoadBalancerPoolsV0(BaseService):
    """The Global Load Balancer Pools V0 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'global_load_balancer_pools'

    @classmethod
    def new_instance(cls,
                     crn: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'GlobalLoadBalancerPoolsV0':
        """
        Return a new client for the Global Load Balancer Pools service using the
               specified parameters and external configuration.

        :param str crn: Full CRN of the service instance.
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
        Construct a new client for the Global Load Balancer Pools service.

        :param str crn: Full CRN of the service instance.

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
    # Global Load Balancer Pool
    #########################


    def list_all_load_balancer_pools(self,
        **kwargs
    ) -> DetailedResponse:
        """
        List all pools.

        List all configured load balancer pools.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListLoadBalancerPoolsResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V0',
                                      operation_id='list_all_load_balancer_pools')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/load_balancers/pools'.format(
            *self.encode_path_vars(self.crn))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def create_load_balancer_pool(self,
        *,
        name: str = None,
        check_regions: List[str] = None,
        origins: List['LoadBalancerPoolReqOriginsItem'] = None,
        description: str = None,
        minimum_origins: int = None,
        enabled: bool = None,
        monitor: str = None,
        notification_email: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create pool.

        Create a new load balancer pool.

        :param str name: (optional) name.
        :param List[str] check_regions: (optional) regions check.
        :param List[LoadBalancerPoolReqOriginsItem] origins: (optional) origins.
        :param str description: (optional) desc.
        :param int minimum_origins: (optional) The minimum number of origins that
               must be healthy for this pool to serve traffic.
        :param bool enabled: (optional) enabled/disabled.
        :param str monitor: (optional) monitor.
        :param str notification_email: (optional) notification email.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LoadBalancerPoolResp` object
        """

        if origins is not None:
            origins = [convert_model(x) for x in origins]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V0',
                                      operation_id='create_load_balancer_pool')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'check_regions': check_regions,
            'origins': origins,
            'description': description,
            'minimum_origins': minimum_origins,
            'enabled': enabled,
            'monitor': monitor,
            'notification_email': notification_email
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/load_balancers/pools'.format(
            *self.encode_path_vars(self.crn))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_load_balancer_pool(self,
        pool_identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get pool.

        Get a single configured load balancer pool.

        :param str pool_identifier: pool identifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LoadBalancerPoolResp` object
        """

        if pool_identifier is None:
            raise ValueError('pool_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V0',
                                      operation_id='get_load_balancer_pool')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/load_balancers/pools/{1}'.format(
            *self.encode_path_vars(self.crn, pool_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def delete_load_balancer_pool(self,
        pool_identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete pool.

        Delete a specific configured load balancer pool.

        :param str pool_identifier: pool identifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteLoadBalancerPoolResp` object
        """

        if pool_identifier is None:
            raise ValueError('pool_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V0',
                                      operation_id='delete_load_balancer_pool')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/load_balancers/pools/{1}'.format(
            *self.encode_path_vars(self.crn, pool_identifier))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def edit_load_balancer_pool(self,
        pool_identifier: str,
        *,
        name: str = None,
        check_regions: List[str] = None,
        origins: List['LoadBalancerPoolReqOriginsItem'] = None,
        description: str = None,
        minimum_origins: int = None,
        enabled: bool = None,
        monitor: str = None,
        notification_email: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Edit pool.

        Edit a specific configured load balancer pool.

        :param str pool_identifier: pool identifier.
        :param str name: (optional) name.
        :param List[str] check_regions: (optional) regions check.
        :param List[LoadBalancerPoolReqOriginsItem] origins: (optional) origins.
        :param str description: (optional) desc.
        :param int minimum_origins: (optional) The minimum number of origins that
               must be healthy for this pool to serve traffic.
        :param bool enabled: (optional) enabled/disabled.
        :param str monitor: (optional) monitor.
        :param str notification_email: (optional) notification email.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LoadBalancerPoolResp` object
        """

        if pool_identifier is None:
            raise ValueError('pool_identifier must be provided')
        if origins is not None:
            origins = [convert_model(x) for x in origins]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V0',
                                      operation_id='edit_load_balancer_pool')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'check_regions': check_regions,
            'origins': origins,
            'description': description,
            'minimum_origins': minimum_origins,
            'enabled': enabled,
            'monitor': monitor,
            'notification_email': notification_email
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/load_balancers/pools/{1}'.format(
            *self.encode_path_vars(self.crn, pool_identifier))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class DeleteLoadBalancerPoolRespResult():
    """
    result.

    :attr str id: identifier.
    """

    def __init__(self,
                 id: str) -> None:
        """
        Initialize a DeleteLoadBalancerPoolRespResult object.

        :param str id: identifier.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteLoadBalancerPoolRespResult':
        """Initialize a DeleteLoadBalancerPoolRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in DeleteLoadBalancerPoolRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteLoadBalancerPoolRespResult object from a json dictionary."""
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
        """Return a `str` version of this DeleteLoadBalancerPoolRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteLoadBalancerPoolRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteLoadBalancerPoolRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class LoadBalancerPoolPackOriginsItem():
    """
    LoadBalancerPoolPackOriginsItem.

    :attr str name: (optional) name.
    :attr str address: (optional) address.
    :attr bool enabled: (optional) enabled/disabled.
    :attr bool healthy: (optional) healthy.
    :attr float weight: (optional) weight.
    :attr str disabled_at: (optional) Pool origin disabled date.
    :attr str failure_reason: (optional) Reason for failure.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 address: str = None,
                 enabled: bool = None,
                 healthy: bool = None,
                 weight: float = None,
                 disabled_at: str = None,
                 failure_reason: str = None) -> None:
        """
        Initialize a LoadBalancerPoolPackOriginsItem object.

        :param str name: (optional) name.
        :param str address: (optional) address.
        :param bool enabled: (optional) enabled/disabled.
        :param bool healthy: (optional) healthy.
        :param float weight: (optional) weight.
        :param str disabled_at: (optional) Pool origin disabled date.
        :param str failure_reason: (optional) Reason for failure.
        """
        self.name = name
        self.address = address
        self.enabled = enabled
        self.healthy = healthy
        self.weight = weight
        self.disabled_at = disabled_at
        self.failure_reason = failure_reason

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LoadBalancerPoolPackOriginsItem':
        """Initialize a LoadBalancerPoolPackOriginsItem object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'address' in _dict:
            args['address'] = _dict.get('address')
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'healthy' in _dict:
            args['healthy'] = _dict.get('healthy')
        if 'weight' in _dict:
            args['weight'] = _dict.get('weight')
        if 'disabled_at' in _dict:
            args['disabled_at'] = _dict.get('disabled_at')
        if 'failure_reason' in _dict:
            args['failure_reason'] = _dict.get('failure_reason')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LoadBalancerPoolPackOriginsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'address') and self.address is not None:
            _dict['address'] = self.address
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'healthy') and self.healthy is not None:
            _dict['healthy'] = self.healthy
        if hasattr(self, 'weight') and self.weight is not None:
            _dict['weight'] = self.weight
        if hasattr(self, 'disabled_at') and self.disabled_at is not None:
            _dict['disabled_at'] = self.disabled_at
        if hasattr(self, 'failure_reason') and self.failure_reason is not None:
            _dict['failure_reason'] = self.failure_reason
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LoadBalancerPoolPackOriginsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LoadBalancerPoolPackOriginsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LoadBalancerPoolPackOriginsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class LoadBalancerPoolReqOriginsItem():
    """
    items.

    :attr str name: (optional) name.
    :attr str address: (optional) address.
    :attr bool enabled: (optional) enabled/disabled.
    :attr float weight: (optional) weight.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 address: str = None,
                 enabled: bool = None,
                 weight: float = None) -> None:
        """
        Initialize a LoadBalancerPoolReqOriginsItem object.

        :param str name: (optional) name.
        :param str address: (optional) address.
        :param bool enabled: (optional) enabled/disabled.
        :param float weight: (optional) weight.
        """
        self.name = name
        self.address = address
        self.enabled = enabled
        self.weight = weight

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LoadBalancerPoolReqOriginsItem':
        """Initialize a LoadBalancerPoolReqOriginsItem object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'address' in _dict:
            args['address'] = _dict.get('address')
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'weight' in _dict:
            args['weight'] = _dict.get('weight')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LoadBalancerPoolReqOriginsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'address') and self.address is not None:
            _dict['address'] = self.address
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'weight') and self.weight is not None:
            _dict['weight'] = self.weight
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LoadBalancerPoolReqOriginsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LoadBalancerPoolReqOriginsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LoadBalancerPoolReqOriginsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DeleteLoadBalancerPoolResp():
    """
    load balancer pool delete response.

    :attr bool success: succcess response.
    :attr List[List[str]] errors: errors.
    :attr List[List[str]] messages: messages.
    :attr DeleteLoadBalancerPoolRespResult result: result.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'DeleteLoadBalancerPoolRespResult') -> None:
        """
        Initialize a DeleteLoadBalancerPoolResp object.

        :param bool success: succcess response.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param DeleteLoadBalancerPoolRespResult result: result.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteLoadBalancerPoolResp':
        """Initialize a DeleteLoadBalancerPoolResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in DeleteLoadBalancerPoolResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in DeleteLoadBalancerPoolResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in DeleteLoadBalancerPoolResp JSON')
        if 'result' in _dict:
            args['result'] = DeleteLoadBalancerPoolRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in DeleteLoadBalancerPoolResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteLoadBalancerPoolResp object from a json dictionary."""
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
        """Return a `str` version of this DeleteLoadBalancerPoolResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteLoadBalancerPoolResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteLoadBalancerPoolResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListLoadBalancerPoolsResp():
    """
    list load balancer pools response.

    :attr bool success: success response.
    :attr List[List[str]] errors: errors.
    :attr List[List[str]] messages: messages.
    :attr List[LoadBalancerPoolPack] result: result.
    :attr ResultInfo result_info: result information.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: List['LoadBalancerPoolPack'],
                 result_info: 'ResultInfo') -> None:
        """
        Initialize a ListLoadBalancerPoolsResp object.

        :param bool success: success response.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param List[LoadBalancerPoolPack] result: result.
        :param ResultInfo result_info: result information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result
        self.result_info = result_info

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListLoadBalancerPoolsResp':
        """Initialize a ListLoadBalancerPoolsResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in ListLoadBalancerPoolsResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in ListLoadBalancerPoolsResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in ListLoadBalancerPoolsResp JSON')
        if 'result' in _dict:
            args['result'] = [LoadBalancerPoolPack.from_dict(x) for x in _dict.get('result')]
        else:
            raise ValueError('Required property \'result\' not present in ListLoadBalancerPoolsResp JSON')
        if 'result_info' in _dict:
            args['result_info'] = ResultInfo.from_dict(_dict.get('result_info'))
        else:
            raise ValueError('Required property \'result_info\' not present in ListLoadBalancerPoolsResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListLoadBalancerPoolsResp object from a json dictionary."""
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
        """Return a `str` version of this ListLoadBalancerPoolsResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListLoadBalancerPoolsResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListLoadBalancerPoolsResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class LoadBalancerPoolPack():
    """
    load balancer pool pack.

    :attr str id: (optional) identifier.
    :attr str created_on: (optional) created date.
    :attr str modified_on: (optional) modified date.
    :attr str description: (optional) desc.
    :attr str name: name.
    :attr bool enabled: (optional) enabled/disabled.
    :attr bool healthy: (optional) healthy.
    :attr str monitor: (optional) monitor.
    :attr int minimum_origins: (optional) Minimum origin count.
    :attr List[str] check_regions: (optional) regions check.
    :attr List[LoadBalancerPoolPackOriginsItem] origins: original.
    :attr str notification_email: (optional) notification email.
    """

    def __init__(self,
                 name: str,
                 origins: List['LoadBalancerPoolPackOriginsItem'],
                 *,
                 id: str = None,
                 created_on: str = None,
                 modified_on: str = None,
                 description: str = None,
                 enabled: bool = None,
                 healthy: bool = None,
                 monitor: str = None,
                 minimum_origins: int = None,
                 check_regions: List[str] = None,
                 notification_email: str = None) -> None:
        """
        Initialize a LoadBalancerPoolPack object.

        :param str name: name.
        :param List[LoadBalancerPoolPackOriginsItem] origins: original.
        :param str id: (optional) identifier.
        :param str created_on: (optional) created date.
        :param str modified_on: (optional) modified date.
        :param str description: (optional) desc.
        :param bool enabled: (optional) enabled/disabled.
        :param bool healthy: (optional) healthy.
        :param str monitor: (optional) monitor.
        :param int minimum_origins: (optional) Minimum origin count.
        :param List[str] check_regions: (optional) regions check.
        :param str notification_email: (optional) notification email.
        """
        self.id = id
        self.created_on = created_on
        self.modified_on = modified_on
        self.description = description
        self.name = name
        self.enabled = enabled
        self.healthy = healthy
        self.monitor = monitor
        self.minimum_origins = minimum_origins
        self.check_regions = check_regions
        self.origins = origins
        self.notification_email = notification_email

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LoadBalancerPoolPack':
        """Initialize a LoadBalancerPoolPack object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'created_on' in _dict:
            args['created_on'] = _dict.get('created_on')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in LoadBalancerPoolPack JSON')
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'healthy' in _dict:
            args['healthy'] = _dict.get('healthy')
        if 'monitor' in _dict:
            args['monitor'] = _dict.get('monitor')
        if 'minimum_origins' in _dict:
            args['minimum_origins'] = _dict.get('minimum_origins')
        if 'check_regions' in _dict:
            args['check_regions'] = _dict.get('check_regions')
        if 'origins' in _dict:
            args['origins'] = [LoadBalancerPoolPackOriginsItem.from_dict(x) for x in _dict.get('origins')]
        else:
            raise ValueError('Required property \'origins\' not present in LoadBalancerPoolPack JSON')
        if 'notification_email' in _dict:
            args['notification_email'] = _dict.get('notification_email')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LoadBalancerPoolPack object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = self.created_on
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = self.modified_on
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'healthy') and self.healthy is not None:
            _dict['healthy'] = self.healthy
        if hasattr(self, 'monitor') and self.monitor is not None:
            _dict['monitor'] = self.monitor
        if hasattr(self, 'minimum_origins') and self.minimum_origins is not None:
            _dict['minimum_origins'] = self.minimum_origins
        if hasattr(self, 'check_regions') and self.check_regions is not None:
            _dict['check_regions'] = self.check_regions
        if hasattr(self, 'origins') and self.origins is not None:
            _dict['origins'] = [x.to_dict() for x in self.origins]
        if hasattr(self, 'notification_email') and self.notification_email is not None:
            _dict['notification_email'] = self.notification_email
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LoadBalancerPoolPack object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LoadBalancerPoolPack') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LoadBalancerPoolPack') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class LoadBalancerPoolResp():
    """
    get load balancer pool response.

    :attr bool success: success response.
    :attr List[List[str]] errors: errors.
    :attr List[List[str]] messages: messages.
    :attr LoadBalancerPoolPack result: load balancer pool pack.
    :attr ResultInfo result_info: result information.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'LoadBalancerPoolPack',
                 result_info: 'ResultInfo') -> None:
        """
        Initialize a LoadBalancerPoolResp object.

        :param bool success: success response.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param LoadBalancerPoolPack result: load balancer pool pack.
        :param ResultInfo result_info: result information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result
        self.result_info = result_info

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LoadBalancerPoolResp':
        """Initialize a LoadBalancerPoolResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in LoadBalancerPoolResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in LoadBalancerPoolResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in LoadBalancerPoolResp JSON')
        if 'result' in _dict:
            args['result'] = LoadBalancerPoolPack.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in LoadBalancerPoolResp JSON')
        if 'result_info' in _dict:
            args['result_info'] = ResultInfo.from_dict(_dict.get('result_info'))
        else:
            raise ValueError('Required property \'result_info\' not present in LoadBalancerPoolResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LoadBalancerPoolResp object from a json dictionary."""
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
        """Return a `str` version of this LoadBalancerPoolResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LoadBalancerPoolResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LoadBalancerPoolResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResultInfo():
    """
    result information.

    :attr int page: page number.
    :attr int per_page: per page count.
    :attr int count: count.
    :attr int total_count: total count.
    """

    def __init__(self,
                 page: int,
                 per_page: int,
                 count: int,
                 total_count: int) -> None:
        """
        Initialize a ResultInfo object.

        :param int page: page number.
        :param int per_page: per page count.
        :param int count: count.
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
