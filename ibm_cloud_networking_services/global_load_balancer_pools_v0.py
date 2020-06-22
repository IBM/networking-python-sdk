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


    def list_all_load_balancer_pools(self, **kwargs) -> DetailedResponse:
        """
        List configured pools.

        List all configured load balancer pools.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListLoadBalancerPoolsResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V0', operation_id='list_all_load_balancer_pools')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/load_balancers/pools'.format(*self.encode_path_vars(self.crn))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def create_load_balancer_pool(self, *, name: str = None, check_regions: List[str] = None, origins: List['LoadBalancerPoolReqOriginsItem'] = None, description: str = None, minimum_origins: int = None, enabled: bool = None, monitor: str = None, notification_email: str = None, **kwargs) -> DetailedResponse:
        """
        Create a new pool.

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
        :rtype: DetailedResponse with `dict` result representing a `LoadBalancerPoolPack` object
        """

        if origins is not None:
            origins = [ convert_model(x) for x in origins ]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V0', operation_id='create_load_balancer_pool')
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

        url = '/v1/{0}/load_balancers/pools'.format(*self.encode_path_vars(self.crn))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_load_balancer_pool(self, pool_identifier: str, **kwargs) -> DetailedResponse:
        """
        Get details of a pool.

        Get a single configured load balancer pool.

        :param str pool_identifier: pool identifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `GetLoadBalancerPoolResp` object
        """

        if pool_identifier is None:
            raise ValueError('pool_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V0', operation_id='get_load_balancer_pool')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/load_balancers/pools/{1}'.format(*self.encode_path_vars(self.crn, pool_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def delete_load_balancer_pool(self, pool_identifier: str, **kwargs) -> DetailedResponse:
        """
        Delete a configured pool.

        Delete a specific configured load balancer pool.

        :param str pool_identifier: pool identifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteLoadBalancerPoolResp` object
        """

        if pool_identifier is None:
            raise ValueError('pool_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V0', operation_id='delete_load_balancer_pool')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/load_balancers/pools/{1}'.format(*self.encode_path_vars(self.crn, pool_identifier))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def edit_load_balancer_pool(self, pool_identifier: str, *, name: str = None, check_regions: List[str] = None, origins: List['LoadBalancerPoolReqOriginsItem'] = None, description: str = None, minimum_origins: int = None, enabled: bool = None, monitor: str = None, notification_email: str = None, **kwargs) -> DetailedResponse:
        """
        Edit a configured pool.

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
        :rtype: DetailedResponse with `dict` result representing a `LoadBalancerPoolReq` object
        """

        if pool_identifier is None:
            raise ValueError('pool_identifier must be provided')
        if origins is not None:
            origins = [ convert_model(x) for x in origins ]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V0', operation_id='edit_load_balancer_pool')
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

        url = '/v1/{0}/load_balancers/pools/{1}'.format(*self.encode_path_vars(self.crn, pool_identifier))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

