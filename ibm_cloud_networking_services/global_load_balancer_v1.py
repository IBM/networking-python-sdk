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
    # List load balancers
    #########################


    def list_all_load_balancers(self, **kwargs) -> DetailedResponse:
        """
        List all load balancers.

        List configured load balancers.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListLoadBalancersResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='list_all_load_balancers')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/load_balancers'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Get a load balancer
    #########################


    def get_load_balancer_settings(self, load_balancer_identifier: str, **kwargs) -> DetailedResponse:
        """
        get a load balancer.

        For a given zone identifier and load balancer id, get the load balancer settings.

        :param str load_balancer_identifier: load balancer identifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LoadBalancersResp` object
        """

        if load_balancer_identifier is None:
            raise ValueError('load_balancer_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_load_balancer_settings')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/load_balancers/{2}'.format(*self.encode_path_vars(self.crn, self.zone_identifier, load_balancer_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Create a load balancer
    #########################


    def create_load_balancer(self, *, name: str = None, fallback_pool: str = None, default_pools: List[str] = None, description: str = None, ttl: int = None, region_pools: List[object] = None, pop_pools: List[object] = None, proxied: bool = None, enabled: bool = None, session_affinity: str = None, steering_policy: str = None, **kwargs) -> DetailedResponse:
        """
        Create a load balancer.

        Create a load balancer for a given zone. The zone should be active before placing
        an order of a load balancer.

        :param str name: (optional) name.
        :param str fallback_pool: (optional) fallback pool.
        :param List[str] default_pools: (optional) default pools.
        :param str description: (optional) desc.
        :param int ttl: (optional) ttl.
        :param List[object] region_pools: (optional) region pools.
        :param List[object] pop_pools: (optional) pop pools.
        :param bool proxied: (optional) proxied.
        :param bool enabled: (optional) enabled/disabled.
        :param str session_affinity: (optional) session affinity.
        :param str steering_policy: (optional) steering policy.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LoadBalancersResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='create_load_balancer')
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

        url = '/v1/{0}/zones/{1}/load_balancers'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Delete a load balancer
    #########################


    def delete_load_balancer(self, load_balancer_identifier: str, **kwargs) -> DetailedResponse:
        """
        Delete a load balancer.

        Delete a load balancer.

        :param str load_balancer_identifier: load balancer identifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteLoadBalancersResp` object
        """

        if load_balancer_identifier is None:
            raise ValueError('load_balancer_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='delete_load_balancer')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/load_balancers/{2}'.format(*self.encode_path_vars(self.crn, self.zone_identifier, load_balancer_identifier))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Edit a load balancer
    #########################


    def edit_load_balancer(self, load_balancer_identifier: str, *, name: str = None, fallback_pool: str = None, default_pools: List[str] = None, description: str = None, ttl: int = None, region_pools: List[object] = None, pop_pools: List[object] = None, proxied: bool = None, enabled: bool = None, session_affinity: str = None, steering_policy: str = None, **kwargs) -> DetailedResponse:
        """
        Edit a load balancer.

        Edit porperties of an existing load balancer.

        :param str load_balancer_identifier: load balancer identifier.
        :param str name: (optional) name.
        :param str fallback_pool: (optional) fallback pool.
        :param List[str] default_pools: (optional) default pools.
        :param str description: (optional) desc.
        :param int ttl: (optional) ttl.
        :param List[object] region_pools: (optional) region pools.
        :param List[object] pop_pools: (optional) pop pools.
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='edit_load_balancer')
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

        url = '/v1/{0}/zones/{1}/load_balancers/{2}'.format(*self.encode_path_vars(self.crn, self.zone_identifier, load_balancer_identifier))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

