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
Global Load Balancer
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

class GlobalLoadBalancerV1(BaseService):
    """The Global Load Balancer V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'global_load_balancer'

    @classmethod
    def new_instance(cls,
                     crn: str,
                     zone_identifier: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'GlobalLoadBalancerV1':
        """
        Return a new client for the Global Load Balancer service using the
               specified parameters and external configuration.

        :param str crn: Full CRN of the service instance.

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
        Construct a new client for the Global Load Balancer service.

        :param str crn: Full CRN of the service instance.

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
    # Global Load Balancer
    #########################


    def list_all_load_balancers(self,
        **kwargs
    ) -> DetailedResponse:
        """
        List all load balancers.

        List configured load balancers.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListLoadBalancersResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_all_load_balancers')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/load_balancers'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def create_load_balancer(self,
        *,
        name: str = None,
        fallback_pool: str = None,
        default_pools: List[str] = None,
        description: str = None,
        ttl: int = None,
        region_pools: object = None,
        pop_pools: object = None,
        proxied: bool = None,
        enabled: bool = None,
        session_affinity: str = None,
        steering_policy: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create load balancer.

        Create a load balancer for a given zone. The zone should be active before placing
        an order of a load balancer.

        :param str name: (optional) name.
        :param str fallback_pool: (optional) fallback pool.
        :param List[str] default_pools: (optional) default pools.
        :param str description: (optional) desc.
        :param int ttl: (optional) ttl.
        :param object region_pools: (optional) region pools.
        :param object pop_pools: (optional) pop pools.
        :param bool proxied: (optional) proxied.
        :param bool enabled: (optional) enabled/disabled.
        :param str session_affinity: (optional) session affinity.
        :param str steering_policy: (optional) steering policy.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LoadBalancersResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_load_balancer')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'fallback_pool': fallback_pool,
            'default_pools': default_pools,
            'description': description,
            'ttl': ttl,
            'region_pools': region_pools,
            'pop_pools': pop_pools,
            'proxied': proxied,
            'enabled': enabled,
            'session_affinity': session_affinity,
            'steering_policy': steering_policy
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/load_balancers'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def edit_load_balancer(self,
        load_balancer_identifier: str,
        *,
        name: str = None,
        fallback_pool: str = None,
        default_pools: List[str] = None,
        description: str = None,
        ttl: int = None,
        region_pools: object = None,
        pop_pools: object = None,
        proxied: bool = None,
        enabled: bool = None,
        session_affinity: str = None,
        steering_policy: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Edit load balancer.

        Edit porperties of an existing load balancer.

        :param str load_balancer_identifier: load balancer identifier.
        :param str name: (optional) name.
        :param str fallback_pool: (optional) fallback pool.
        :param List[str] default_pools: (optional) default pools.
        :param str description: (optional) desc.
        :param int ttl: (optional) ttl.
        :param object region_pools: (optional) region pools.
        :param object pop_pools: (optional) pop pools.
        :param bool proxied: (optional) proxied.
        :param bool enabled: (optional) enabled/disabled.
        :param str session_affinity: (optional) session affinity.
        :param str steering_policy: (optional) steering policy.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LoadBalancersResp` object
        """

        if load_balancer_identifier is None:
            raise ValueError('load_balancer_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='edit_load_balancer')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'fallback_pool': fallback_pool,
            'default_pools': default_pools,
            'description': description,
            'ttl': ttl,
            'region_pools': region_pools,
            'pop_pools': pop_pools,
            'proxied': proxied,
            'enabled': enabled,
            'session_affinity': session_affinity,
            'steering_policy': steering_policy
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/load_balancers/{2}'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier, load_balancer_identifier))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_load_balancer(self,
        load_balancer_identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete load balancer.

        Delete a load balancer.

        :param str load_balancer_identifier: load balancer identifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteLoadBalancersResp` object
        """

        if load_balancer_identifier is None:
            raise ValueError('load_balancer_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_load_balancer')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/load_balancers/{2}'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier, load_balancer_identifier))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_load_balancer_settings(self,
        load_balancer_identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get load balancer.

        For a given zone identifier and load balancer id, get the load balancer settings.

        :param str load_balancer_identifier: load balancer identifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LoadBalancersResp` object
        """

        if load_balancer_identifier is None:
            raise ValueError('load_balancer_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_load_balancer_settings')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/load_balancers/{2}'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier, load_balancer_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class DeleteLoadBalancersRespResult():
    """
    result.

    :attr str id: identifier.
    """

    def __init__(self,
                 id: str) -> None:
        """
        Initialize a DeleteLoadBalancersRespResult object.

        :param str id: identifier.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteLoadBalancersRespResult':
        """Initialize a DeleteLoadBalancersRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in DeleteLoadBalancersRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteLoadBalancersRespResult object from a json dictionary."""
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
        """Return a `str` version of this DeleteLoadBalancersRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteLoadBalancersRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteLoadBalancersRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DeleteLoadBalancersResp():
    """
    delete load balancers response.

    :attr bool success: success respose.
    :attr List[List[str]] errors: errors.
    :attr List[List[str]] messages: messages.
    :attr DeleteLoadBalancersRespResult result: result.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'DeleteLoadBalancersRespResult') -> None:
        """
        Initialize a DeleteLoadBalancersResp object.

        :param bool success: success respose.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param DeleteLoadBalancersRespResult result: result.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteLoadBalancersResp':
        """Initialize a DeleteLoadBalancersResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in DeleteLoadBalancersResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in DeleteLoadBalancersResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in DeleteLoadBalancersResp JSON')
        if 'result' in _dict:
            args['result'] = DeleteLoadBalancersRespResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in DeleteLoadBalancersResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteLoadBalancersResp object from a json dictionary."""
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
        """Return a `str` version of this DeleteLoadBalancersResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteLoadBalancersResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteLoadBalancersResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListLoadBalancersResp():
    """
    load balancer list response.

    :attr bool success: success response.
    :attr List[List[str]] errors: errors.
    :attr List[List[str]] messages: messages.
    :attr List[LoadBalancerPack] result: result.
    :attr ResultInfo result_info: result information.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: List['LoadBalancerPack'],
                 result_info: 'ResultInfo') -> None:
        """
        Initialize a ListLoadBalancersResp object.

        :param bool success: success response.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param List[LoadBalancerPack] result: result.
        :param ResultInfo result_info: result information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result
        self.result_info = result_info

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListLoadBalancersResp':
        """Initialize a ListLoadBalancersResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in ListLoadBalancersResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in ListLoadBalancersResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in ListLoadBalancersResp JSON')
        if 'result' in _dict:
            args['result'] = [LoadBalancerPack.from_dict(x) for x in _dict.get('result')]
        else:
            raise ValueError('Required property \'result\' not present in ListLoadBalancersResp JSON')
        if 'result_info' in _dict:
            args['result_info'] = ResultInfo.from_dict(_dict.get('result_info'))
        else:
            raise ValueError('Required property \'result_info\' not present in ListLoadBalancersResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListLoadBalancersResp object from a json dictionary."""
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
        """Return a `str` version of this ListLoadBalancersResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListLoadBalancersResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListLoadBalancersResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class LoadBalancerPack():
    """
    loadbalancer pack.

    :attr str id: identifier.
    :attr str created_on: created date.
    :attr str modified_on: modified date.
    :attr str description: desc.
    :attr str name: name.
    :attr int ttl: ttl.
    :attr str fallback_pool: fallback pool.
    :attr List[str] default_pools: default pools.
    :attr object region_pools: region pools.
    :attr object pop_pools: pop pools.
    :attr bool proxied: proxied.
    :attr bool enabled: enabled/disabled.
    :attr str session_affinity: session affinity.
    :attr str steering_policy: steering policy.
    """

    def __init__(self,
                 id: str,
                 created_on: str,
                 modified_on: str,
                 description: str,
                 name: str,
                 ttl: int,
                 fallback_pool: str,
                 default_pools: List[str],
                 region_pools: object,
                 pop_pools: object,
                 proxied: bool,
                 enabled: bool,
                 session_affinity: str,
                 steering_policy: str) -> None:
        """
        Initialize a LoadBalancerPack object.

        :param str id: identifier.
        :param str created_on: created date.
        :param str modified_on: modified date.
        :param str description: desc.
        :param str name: name.
        :param int ttl: ttl.
        :param str fallback_pool: fallback pool.
        :param List[str] default_pools: default pools.
        :param object region_pools: region pools.
        :param object pop_pools: pop pools.
        :param bool proxied: proxied.
        :param bool enabled: enabled/disabled.
        :param str session_affinity: session affinity.
        :param str steering_policy: steering policy.
        """
        self.id = id
        self.created_on = created_on
        self.modified_on = modified_on
        self.description = description
        self.name = name
        self.ttl = ttl
        self.fallback_pool = fallback_pool
        self.default_pools = default_pools
        self.region_pools = region_pools
        self.pop_pools = pop_pools
        self.proxied = proxied
        self.enabled = enabled
        self.session_affinity = session_affinity
        self.steering_policy = steering_policy

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LoadBalancerPack':
        """Initialize a LoadBalancerPack object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in LoadBalancerPack JSON')
        if 'created_on' in _dict:
            args['created_on'] = _dict.get('created_on')
        else:
            raise ValueError('Required property \'created_on\' not present in LoadBalancerPack JSON')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        else:
            raise ValueError('Required property \'modified_on\' not present in LoadBalancerPack JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError('Required property \'description\' not present in LoadBalancerPack JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in LoadBalancerPack JSON')
        if 'ttl' in _dict:
            args['ttl'] = _dict.get('ttl')
        else:
            raise ValueError('Required property \'ttl\' not present in LoadBalancerPack JSON')
        if 'fallback_pool' in _dict:
            args['fallback_pool'] = _dict.get('fallback_pool')
        else:
            raise ValueError('Required property \'fallback_pool\' not present in LoadBalancerPack JSON')
        if 'default_pools' in _dict:
            args['default_pools'] = _dict.get('default_pools')
        else:
            raise ValueError('Required property \'default_pools\' not present in LoadBalancerPack JSON')
        if 'region_pools' in _dict:
            args['region_pools'] = _dict.get('region_pools')
        else:
            raise ValueError('Required property \'region_pools\' not present in LoadBalancerPack JSON')
        if 'pop_pools' in _dict:
            args['pop_pools'] = _dict.get('pop_pools')
        else:
            raise ValueError('Required property \'pop_pools\' not present in LoadBalancerPack JSON')
        if 'proxied' in _dict:
            args['proxied'] = _dict.get('proxied')
        else:
            raise ValueError('Required property \'proxied\' not present in LoadBalancerPack JSON')
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        else:
            raise ValueError('Required property \'enabled\' not present in LoadBalancerPack JSON')
        if 'session_affinity' in _dict:
            args['session_affinity'] = _dict.get('session_affinity')
        else:
            raise ValueError('Required property \'session_affinity\' not present in LoadBalancerPack JSON')
        if 'steering_policy' in _dict:
            args['steering_policy'] = _dict.get('steering_policy')
        else:
            raise ValueError('Required property \'steering_policy\' not present in LoadBalancerPack JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LoadBalancerPack object from a json dictionary."""
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
        if hasattr(self, 'ttl') and self.ttl is not None:
            _dict['ttl'] = self.ttl
        if hasattr(self, 'fallback_pool') and self.fallback_pool is not None:
            _dict['fallback_pool'] = self.fallback_pool
        if hasattr(self, 'default_pools') and self.default_pools is not None:
            _dict['default_pools'] = self.default_pools
        if hasattr(self, 'region_pools') and self.region_pools is not None:
            _dict['region_pools'] = self.region_pools
        if hasattr(self, 'pop_pools') and self.pop_pools is not None:
            _dict['pop_pools'] = self.pop_pools
        if hasattr(self, 'proxied') and self.proxied is not None:
            _dict['proxied'] = self.proxied
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'session_affinity') and self.session_affinity is not None:
            _dict['session_affinity'] = self.session_affinity
        if hasattr(self, 'steering_policy') and self.steering_policy is not None:
            _dict['steering_policy'] = self.steering_policy
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LoadBalancerPack object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LoadBalancerPack') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LoadBalancerPack') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class SessionAffinityEnum(str, Enum):
        """
        session affinity.
        """
        NONE = 'none'
        COOKIE = 'cookie'
        IP_COOKIE = 'ip_cookie'


    class SteeringPolicyEnum(str, Enum):
        """
        steering policy.
        """
        OFF = 'off'
        GEO = 'geo'
        RANDOM = 'random'
        DYNAMIC_LATENCY = 'dynamic_latency'


class LoadBalancersResp():
    """
    load balancer response.

    :attr bool success: success response.
    :attr List[List[str]] errors: errors.
    :attr List[List[str]] messages: messages.
    :attr LoadBalancerPack result: loadbalancer pack.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'LoadBalancerPack') -> None:
        """
        Initialize a LoadBalancersResp object.

        :param bool success: success response.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param LoadBalancerPack result: loadbalancer pack.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LoadBalancersResp':
        """Initialize a LoadBalancersResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in LoadBalancersResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in LoadBalancersResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in LoadBalancersResp JSON')
        if 'result' in _dict:
            args['result'] = LoadBalancerPack.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in LoadBalancersResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LoadBalancersResp object from a json dictionary."""
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
        """Return a `str` version of this LoadBalancersResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LoadBalancersResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LoadBalancersResp') -> bool:
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
