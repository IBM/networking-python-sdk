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

# IBM OpenAPI SDK Code Generator Version: 3.12.0-64fe8d3f-20200820-144050
 
"""
Global Load Balancers
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

class GlobalLoadBalancersV1(BaseService):
    """The Global Load Balancers V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.dns-svcs.cloud.ibm.com/v1'
    DEFAULT_SERVICE_NAME = 'global_load_balancers'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'GlobalLoadBalancersV1':
        """
        Return a new client for the Global Load Balancers service using the
               specified parameters and external configuration.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(self,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the Global Load Balancers service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # Global Load Balancers
    #########################


    def list_load_balancers(self,
        instance_id: str,
        dnszone_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List load balancers.

        List the Global Load Balancers for a given DNS zone.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListLoadBalancers` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if dnszone_id is None:
            raise ValueError('dnszone_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_load_balancers')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/instances/{0}/dnszones/{1}/load_balancers'.format(
            *self.encode_path_vars(instance_id, dnszone_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def create_load_balancer(self,
        instance_id: str,
        dnszone_id: str,
        *,
        name: str = None,
        fallback_pool: str = None,
        default_pools: List[str] = None,
        description: str = None,
        enabled: bool = None,
        ttl: int = None,
        az_pools: List['LoadBalancerAzPoolsItem'] = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a load balancer.

        Create a load balancer for a given DNS zone.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str name: (optional) Name of the load balancer.
        :param str fallback_pool: (optional) The pool ID to use when all other
               pools are detected as unhealthy.
        :param List[str] default_pools: (optional) A list of pool IDs ordered by
               their failover priority. Pools defined here are used by default, or when
               region_pools are not configured for a given region.
        :param str description: (optional) Descriptive text of the load balancer.
        :param bool enabled: (optional) Whether the load balancer is enabled.
        :param int ttl: (optional) Time to live in second.
        :param List[LoadBalancerAzPoolsItem] az_pools: (optional) Map availability
               zones to pool ID's.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LoadBalancer` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if dnszone_id is None:
            raise ValueError('dnszone_id must be provided')
        if az_pools is not None:
            az_pools = [convert_model(x) for x in az_pools]
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_load_balancer')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'fallback_pool': fallback_pool,
            'default_pools': default_pools,
            'description': description,
            'enabled': enabled,
            'ttl': ttl,
            'az_pools': az_pools
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/instances/{0}/dnszones/{1}/load_balancers'.format(
            *self.encode_path_vars(instance_id, dnszone_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_load_balancer(self,
        instance_id: str,
        dnszone_id: str,
        lb_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a load balancer.

        Delete a load balancer.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str lb_id: The unique identifier of a load balancer.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if dnszone_id is None:
            raise ValueError('dnszone_id must be provided')
        if lb_id is None:
            raise ValueError('lb_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_load_balancer')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/instances/{0}/dnszones/{1}/load_balancers/{2}'.format(
            *self.encode_path_vars(instance_id, dnszone_id, lb_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_load_balancer(self,
        instance_id: str,
        dnszone_id: str,
        lb_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a load balancer.

        Get details of a load balancer.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str lb_id: The unique identifier of a load balancer.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LoadBalancer` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if dnszone_id is None:
            raise ValueError('dnszone_id must be provided')
        if lb_id is None:
            raise ValueError('lb_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_load_balancer')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/instances/{0}/dnszones/{1}/load_balancers/{2}'.format(
            *self.encode_path_vars(instance_id, dnszone_id, lb_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_load_balancer(self,
        instance_id: str,
        dnszone_id: str,
        lb_id: str,
        *,
        name: str = None,
        description: str = None,
        enabled: bool = None,
        ttl: int = None,
        fallback_pool: str = None,
        default_pools: List[str] = None,
        az_pools: List['LoadBalancerAzPoolsItem'] = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update the properties of a load balancer.

        Update the properties of a load balancer.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str lb_id: The unique identifier of a load balancer.
        :param str name: (optional) Name of the load balancer.
        :param str description: (optional) Descriptive text of the load balancer.
        :param bool enabled: (optional) Whether the load balancer is enabled.
        :param int ttl: (optional) Time to live in second.
        :param str fallback_pool: (optional) The pool ID to use when all other
               pools are detected as unhealthy.
        :param List[str] default_pools: (optional) A list of pool IDs ordered by
               their failover priority. Pools defined here are used by default, or when
               region_pools are not configured for a given region.
        :param List[LoadBalancerAzPoolsItem] az_pools: (optional) Map availability
               zones to pool ID's.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LoadBalancer` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if dnszone_id is None:
            raise ValueError('dnszone_id must be provided')
        if lb_id is None:
            raise ValueError('lb_id must be provided')
        if az_pools is not None:
            az_pools = [convert_model(x) for x in az_pools]
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_load_balancer')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'description': description,
            'enabled': enabled,
            'ttl': ttl,
            'fallback_pool': fallback_pool,
            'default_pools': default_pools,
            'az_pools': az_pools
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/instances/{0}/dnszones/{1}/load_balancers/{2}'.format(
            *self.encode_path_vars(instance_id, dnszone_id, lb_id))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Pools
    #########################


    def list_pools(self,
        instance_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List load balancer pools.

        List the load balancer pools.

        :param str instance_id: The unique identifier of a service instance.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListPools` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_pools')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/instances/{0}/pools'.format(
            *self.encode_path_vars(instance_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def create_pool(self,
        instance_id: str,
        *,
        name: str = None,
        origins: List['OriginInput'] = None,
        description: str = None,
        enabled: bool = None,
        healthy_origins_threshold: int = None,
        monitor: str = None,
        notification_channel: str = None,
        healthcheck_region: str = None,
        healthcheck_subnets: List[str] = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a load balancer pool.

        Create a load balancer pool.

        :param str instance_id: The unique identifier of a service instance.
        :param str name: (optional) Name of the load balancer pool.
        :param List[OriginInput] origins: (optional) The list of origins within
               this pool. Traffic directed at this pool is balanced across all currently
               healthy origins, provided the pool itself is healthy.
        :param str description: (optional) Descriptive text of the load balancer
               pool.
        :param bool enabled: (optional) Whether the load balancer pool is enabled.
        :param int healthy_origins_threshold: (optional) The minimum number of
               origins that must be healthy for this pool to serve traffic. If the number
               of healthy origins falls below this number, the pool will be marked
               unhealthy and we will failover to the next available pool.
        :param str monitor: (optional) The ID of the load balancer monitor to be
               associated to this pool.
        :param str notification_channel: (optional) The notification channel.
        :param str healthcheck_region: (optional) Health check region of VSIs.
        :param List[str] healthcheck_subnets: (optional) Health check subnet IDs of
               VSIs.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Pool` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if origins is not None:
            origins = [convert_model(x) for x in origins]
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_pool')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'origins': origins,
            'description': description,
            'enabled': enabled,
            'healthy_origins_threshold': healthy_origins_threshold,
            'monitor': monitor,
            'notification_channel': notification_channel,
            'healthcheck_region': healthcheck_region,
            'healthcheck_subnets': healthcheck_subnets
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/instances/{0}/pools'.format(
            *self.encode_path_vars(instance_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_pool(self,
        instance_id: str,
        pool_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a load balancer pool.

        Delete a load balancer pool.

        :param str instance_id: The unique identifier of a service instance.
        :param str pool_id: The unique identifier of a load balancer pool.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if pool_id is None:
            raise ValueError('pool_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_pool')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/instances/{0}/pools/{1}'.format(
            *self.encode_path_vars(instance_id, pool_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_pool(self,
        instance_id: str,
        pool_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a load balancer pool.

        Get details of a load balancer pool.

        :param str instance_id: The unique identifier of a service instance.
        :param str pool_id: The unique identifier of a load balancer pool.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Pool` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if pool_id is None:
            raise ValueError('pool_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_pool')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/instances/{0}/pools/{1}'.format(
            *self.encode_path_vars(instance_id, pool_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_pool(self,
        instance_id: str,
        pool_id: str,
        *,
        name: str = None,
        description: str = None,
        enabled: bool = None,
        healthy_origins_threshold: int = None,
        origins: List['OriginInput'] = None,
        monitor: str = None,
        notification_channel: str = None,
        healthcheck_region: str = None,
        healthcheck_subnets: List[str] = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update the properties of a load balancer pool.

        Update the properties of a load balancer pool.

        :param str instance_id: The unique identifier of a service instance.
        :param str pool_id: The unique identifier of a load balancer pool.
        :param str name: (optional) Name of the load balancer pool.
        :param str description: (optional) Descriptive text of the load balancer
               pool.
        :param bool enabled: (optional) Whether the load balancer pool is enabled.
        :param int healthy_origins_threshold: (optional) The minimum number of
               origins that must be healthy for this pool to serve traffic. If the number
               of healthy origins falls below this number, the pool will be marked
               unhealthy and we will failover to the next available pool.
        :param List[OriginInput] origins: (optional) The list of origins within
               this pool. Traffic directed at this pool is balanced across all currently
               healthy origins, provided the pool itself is healthy.
        :param str monitor: (optional) The ID of the load balancer monitor to be
               associated to this pool.
        :param str notification_channel: (optional) The notification channel.
        :param str healthcheck_region: (optional) Health check region of VSIs.
        :param List[str] healthcheck_subnets: (optional) Health check subnet IDs of
               VSIs.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Pool` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if pool_id is None:
            raise ValueError('pool_id must be provided')
        if origins is not None:
            origins = [convert_model(x) for x in origins]
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_pool')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'description': description,
            'enabled': enabled,
            'healthy_origins_threshold': healthy_origins_threshold,
            'origins': origins,
            'monitor': monitor,
            'notification_channel': notification_channel,
            'healthcheck_region': healthcheck_region,
            'healthcheck_subnets': healthcheck_subnets
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/instances/{0}/pools/{1}'.format(
            *self.encode_path_vars(instance_id, pool_id))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Monitors
    #########################


    def list_monitors(self,
        instance_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List load balancer monitors.

        List the load balancer monitors.

        :param str instance_id: The unique identifier of a service instance.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListMonitors` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_monitors')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/instances/{0}/monitors'.format(
            *self.encode_path_vars(instance_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def create_monitor(self,
        instance_id: str,
        *,
        name: str = None,
        type: str = None,
        description: str = None,
        port: int = None,
        interval: int = None,
        retries: int = None,
        timeout: int = None,
        method: str = None,
        path: str = None,
        headers_: List['HealthcheckHeader'] = None,
        allow_insecure: bool = None,
        expected_codes: str = None,
        expected_body: str = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a load balancer monitor.

        Create a load balancer monitor.

        :param str instance_id: The unique identifier of a service instance.
        :param str name: (optional) The name of the load balancer monitor.
        :param str type: (optional) The protocol to use for the health check.
               Currently supported protocols are 'HTTP','HTTPS' and 'TCP'.
        :param str description: (optional) Descriptive text of the load balancer
               monitor.
        :param int port: (optional) Port number to connect to for the health check.
               Required for TCP checks. HTTP and HTTPS checks should only define the port
               when using a non-standard port (HTTP: default 80, HTTPS: default 443).
        :param int interval: (optional) The interval between each health check.
               Shorter intervals may improve failover time, but will increase load on the
               origins as we check from multiple locations.
        :param int retries: (optional) The number of retries to attempt in case of
               a timeout before marking the origin as unhealthy. Retries are attempted
               immediately.
        :param int timeout: (optional) The timeout (in seconds) before marking the
               health check as failed.
        :param str method: (optional) The method to use for the health check
               applicable to HTTP/HTTPS based checks, the default value is 'GET'.
        :param str path: (optional) The endpoint path to health check against. This
               parameter is only valid for HTTP and HTTPS monitors.
        :param List[HealthcheckHeader] headers_: (optional) The HTTP request
               headers to send in the health check. It is recommended you set a Host
               header by default. The User-Agent header cannot be overridden. This
               parameter is only valid for HTTP and HTTPS monitors.
        :param bool allow_insecure: (optional) Do not validate the certificate when
               monitor use HTTPS. This parameter is currently only valid for HTTPS
               monitors.
        :param str expected_codes: (optional) The expected HTTP response code or
               code range of the health check. This parameter is only valid for HTTP and
               HTTPS monitors.
        :param str expected_body: (optional) A case-insensitive sub-string to look
               for in the response body. If this string is not found, the origin will be
               marked as unhealthy. This parameter is only valid for HTTP and HTTPS
               monitors.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Monitor` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if headers_ is not None:
            headers_ = [convert_model(x) for x in headers_]
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_monitor')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'type': type,
            'description': description,
            'port': port,
            'interval': interval,
            'retries': retries,
            'timeout': timeout,
            'method': method,
            'path': path,
            'headers': headers_,
            'allow_insecure': allow_insecure,
            'expected_codes': expected_codes,
            'expected_body': expected_body
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/instances/{0}/monitors'.format(
            *self.encode_path_vars(instance_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_monitor(self,
        instance_id: str,
        monitor_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a load balancer monitor.

        Delete a load balancer monitor.

        :param str instance_id: The unique identifier of a service instance.
        :param str monitor_id: The unique identifier of a load balancer monitor.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if monitor_id is None:
            raise ValueError('monitor_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_monitor')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/instances/{0}/monitors/{1}'.format(
            *self.encode_path_vars(instance_id, monitor_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_monitor(self,
        instance_id: str,
        monitor_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a load balancer monitor.

        Get details of a load balancer monitor.

        :param str instance_id: The unique identifier of a service instance.
        :param str monitor_id: The unique identifier of a load balancer monitor.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Monitor` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if monitor_id is None:
            raise ValueError('monitor_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_monitor')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/instances/{0}/monitors/{1}'.format(
            *self.encode_path_vars(instance_id, monitor_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_monitor(self,
        instance_id: str,
        monitor_id: str,
        *,
        name: str = None,
        description: str = None,
        type: str = None,
        port: int = None,
        interval: int = None,
        retries: int = None,
        timeout: int = None,
        method: str = None,
        path: str = None,
        headers_: List['HealthcheckHeader'] = None,
        allow_insecure: bool = None,
        expected_codes: str = None,
        expected_body: str = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update the properties of a load balancer monitor.

        Update the properties of a load balancer monitor.

        :param str instance_id: The unique identifier of a service instance.
        :param str monitor_id: The unique identifier of a load balancer monitor.
        :param str name: (optional) The name of the load balancer monitor.
        :param str description: (optional) Descriptive text of the load balancer
               monitor.
        :param str type: (optional) The protocol to use for the health check.
               Currently supported protocols are 'HTTP','HTTPS' and 'TCP'.
        :param int port: (optional) Port number to connect to for the health check.
               Required for TCP checks. HTTP and HTTPS checks should only define the port
               when using a non-standard port (HTTP: default 80, HTTPS: default 443).
        :param int interval: (optional) The interval between each health check.
               Shorter intervals may improve failover time, but will increase load on the
               origins as we check from multiple locations.
        :param int retries: (optional) The number of retries to attempt in case of
               a timeout before marking the origin as unhealthy. Retries are attempted
               immediately.
        :param int timeout: (optional) The timeout (in seconds) before marking the
               health check as failed.
        :param str method: (optional) The method to use for the health check
               applicable to HTTP/HTTPS based checks, the default value is 'GET'.
        :param str path: (optional) The endpoint path to health check against. This
               parameter is only valid for HTTP and HTTPS monitors.
        :param List[HealthcheckHeader] headers_: (optional) The HTTP request
               headers to send in the health check. It is recommended you set a Host
               header by default. The User-Agent header cannot be overridden. This
               parameter is only valid for HTTP and HTTPS monitors.
        :param bool allow_insecure: (optional) Do not validate the certificate when
               monitor use HTTPS. This parameter is currently only valid for HTTP and
               HTTPS monitors.
        :param str expected_codes: (optional) The expected HTTP response code or
               code range of the health check. This parameter is only valid for HTTP and
               HTTPS monitors.
        :param str expected_body: (optional) A case-insensitive sub-string to look
               for in the response body. If this string is not found, the origin will be
               marked as unhealthy. This parameter is only valid for HTTP and HTTPS
               monitors.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Monitor` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if monitor_id is None:
            raise ValueError('monitor_id must be provided')
        if headers_ is not None:
            headers_ = [convert_model(x) for x in headers_]
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_monitor')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'description': description,
            'type': type,
            'port': port,
            'interval': interval,
            'retries': retries,
            'timeout': timeout,
            'method': method,
            'path': path,
            'headers': headers_,
            'allow_insecure': allow_insecure,
            'expected_codes': expected_codes,
            'expected_body': expected_body
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        url = '/instances/{0}/monitors/{1}'.format(
            *self.encode_path_vars(instance_id, monitor_id))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class LoadBalancerAzPoolsItem():
    """
    LoadBalancerAzPoolsItem.

    :attr str availability_zone: (optional) Availability zone.
    :attr List[str] pools: (optional) List of load balancer pools.
    """

    def __init__(self,
                 *,
                 availability_zone: str = None,
                 pools: List[str] = None) -> None:
        """
        Initialize a LoadBalancerAzPoolsItem object.

        :param str availability_zone: (optional) Availability zone.
        :param List[str] pools: (optional) List of load balancer pools.
        """
        self.availability_zone = availability_zone
        self.pools = pools

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LoadBalancerAzPoolsItem':
        """Initialize a LoadBalancerAzPoolsItem object from a json dictionary."""
        args = {}
        if 'availability_zone' in _dict:
            args['availability_zone'] = _dict.get('availability_zone')
        if 'pools' in _dict:
            args['pools'] = _dict.get('pools')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LoadBalancerAzPoolsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'availability_zone') and self.availability_zone is not None:
            _dict['availability_zone'] = self.availability_zone
        if hasattr(self, 'pools') and self.pools is not None:
            _dict['pools'] = self.pools
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LoadBalancerAzPoolsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LoadBalancerAzPoolsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LoadBalancerAzPoolsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class FirstHref():
    """
    href.

    :attr str href: (optional) href.
    """

    def __init__(self,
                 *,
                 href: str = None) -> None:
        """
        Initialize a FirstHref object.

        :param str href: (optional) href.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FirstHref':
        """Initialize a FirstHref object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FirstHref object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FirstHref object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'FirstHref') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FirstHref') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class HealthcheckHeader():
    """
    The HTTP header of health check request.

    :attr str name: The name of HTTP request header.
    :attr List[str] value: The value of HTTP request header.
    """

    def __init__(self,
                 name: str,
                 value: List[str]) -> None:
        """
        Initialize a HealthcheckHeader object.

        :param str name: The name of HTTP request header.
        :param List[str] value: The value of HTTP request header.
        """
        self.name = name
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'HealthcheckHeader':
        """Initialize a HealthcheckHeader object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in HealthcheckHeader JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError('Required property \'value\' not present in HealthcheckHeader JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a HealthcheckHeader object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this HealthcheckHeader object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'HealthcheckHeader') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'HealthcheckHeader') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListLoadBalancers():
    """
    List Global Load Balancers response.

    :attr List[LoadBalancer] load_balancers: An array of Global Load Balancers.
    :attr int offset: Page number.
    :attr int limit: Number of Global Load Balancers per page.
    :attr int count: Number of Global Load Balancers.
    :attr int total_count: Total number of Global Load Balancers.
    :attr FirstHref first: href.
    :attr NextHref next: href.
    """

    def __init__(self,
                 load_balancers: List['LoadBalancer'],
                 offset: int,
                 limit: int,
                 count: int,
                 total_count: int,
                 first: 'FirstHref',
                 next: 'NextHref') -> None:
        """
        Initialize a ListLoadBalancers object.

        :param List[LoadBalancer] load_balancers: An array of Global Load
               Balancers.
        :param int offset: Page number.
        :param int limit: Number of Global Load Balancers per page.
        :param int count: Number of Global Load Balancers.
        :param int total_count: Total number of Global Load Balancers.
        :param FirstHref first: href.
        :param NextHref next: href.
        """
        self.load_balancers = load_balancers
        self.offset = offset
        self.limit = limit
        self.count = count
        self.total_count = total_count
        self.first = first
        self.next = next

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListLoadBalancers':
        """Initialize a ListLoadBalancers object from a json dictionary."""
        args = {}
        if 'load_balancers' in _dict:
            args['load_balancers'] = [LoadBalancer.from_dict(x) for x in _dict.get('load_balancers')]
        else:
            raise ValueError('Required property \'load_balancers\' not present in ListLoadBalancers JSON')
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        else:
            raise ValueError('Required property \'offset\' not present in ListLoadBalancers JSON')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in ListLoadBalancers JSON')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        else:
            raise ValueError('Required property \'count\' not present in ListLoadBalancers JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in ListLoadBalancers JSON')
        if 'first' in _dict:
            args['first'] = FirstHref.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in ListLoadBalancers JSON')
        if 'next' in _dict:
            args['next'] = NextHref.from_dict(_dict.get('next'))
        else:
            raise ValueError('Required property \'next\' not present in ListLoadBalancers JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListLoadBalancers object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'load_balancers') and self.load_balancers is not None:
            _dict['load_balancers'] = [x.to_dict() for x in self.load_balancers]
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'first') and self.first is not None:
            _dict['first'] = self.first.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            _dict['next'] = self.next.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListLoadBalancers object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListLoadBalancers') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListLoadBalancers') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListMonitors():
    """
    List load balancer monitors response.

    :attr List[Monitor] monitors: An array of load balancer monitors.
    :attr int offset: Page number.
    :attr int limit: Number of load balancer monitors per page.
    :attr int count: Number of load balancers.
    :attr int total_count: Total number of load balancers.
    :attr FirstHref first: href.
    :attr NextHref next: href.
    """

    def __init__(self,
                 monitors: List['Monitor'],
                 offset: int,
                 limit: int,
                 count: int,
                 total_count: int,
                 first: 'FirstHref',
                 next: 'NextHref') -> None:
        """
        Initialize a ListMonitors object.

        :param List[Monitor] monitors: An array of load balancer monitors.
        :param int offset: Page number.
        :param int limit: Number of load balancer monitors per page.
        :param int count: Number of load balancers.
        :param int total_count: Total number of load balancers.
        :param FirstHref first: href.
        :param NextHref next: href.
        """
        self.monitors = monitors
        self.offset = offset
        self.limit = limit
        self.count = count
        self.total_count = total_count
        self.first = first
        self.next = next

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListMonitors':
        """Initialize a ListMonitors object from a json dictionary."""
        args = {}
        if 'monitors' in _dict:
            args['monitors'] = [Monitor.from_dict(x) for x in _dict.get('monitors')]
        else:
            raise ValueError('Required property \'monitors\' not present in ListMonitors JSON')
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        else:
            raise ValueError('Required property \'offset\' not present in ListMonitors JSON')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in ListMonitors JSON')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        else:
            raise ValueError('Required property \'count\' not present in ListMonitors JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in ListMonitors JSON')
        if 'first' in _dict:
            args['first'] = FirstHref.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in ListMonitors JSON')
        if 'next' in _dict:
            args['next'] = NextHref.from_dict(_dict.get('next'))
        else:
            raise ValueError('Required property \'next\' not present in ListMonitors JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListMonitors object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'monitors') and self.monitors is not None:
            _dict['monitors'] = [x.to_dict() for x in self.monitors]
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'first') and self.first is not None:
            _dict['first'] = self.first.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            _dict['next'] = self.next.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListMonitors object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListMonitors') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListMonitors') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListPools():
    """
    List load balancer pools response.

    :attr List[Pool] pools: An array of load balancer pools.
    :attr int offset: Page number.
    :attr int limit: Number of load balancer pools per page.
    :attr int count: Number of load balancers.
    :attr int total_count: Total number of load balancers.
    :attr FirstHref first: href.
    :attr NextHref next: href.
    """

    def __init__(self,
                 pools: List['Pool'],
                 offset: int,
                 limit: int,
                 count: int,
                 total_count: int,
                 first: 'FirstHref',
                 next: 'NextHref') -> None:
        """
        Initialize a ListPools object.

        :param List[Pool] pools: An array of load balancer pools.
        :param int offset: Page number.
        :param int limit: Number of load balancer pools per page.
        :param int count: Number of load balancers.
        :param int total_count: Total number of load balancers.
        :param FirstHref first: href.
        :param NextHref next: href.
        """
        self.pools = pools
        self.offset = offset
        self.limit = limit
        self.count = count
        self.total_count = total_count
        self.first = first
        self.next = next

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListPools':
        """Initialize a ListPools object from a json dictionary."""
        args = {}
        if 'pools' in _dict:
            args['pools'] = [Pool.from_dict(x) for x in _dict.get('pools')]
        else:
            raise ValueError('Required property \'pools\' not present in ListPools JSON')
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        else:
            raise ValueError('Required property \'offset\' not present in ListPools JSON')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in ListPools JSON')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        else:
            raise ValueError('Required property \'count\' not present in ListPools JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in ListPools JSON')
        if 'first' in _dict:
            args['first'] = FirstHref.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in ListPools JSON')
        if 'next' in _dict:
            args['next'] = NextHref.from_dict(_dict.get('next'))
        else:
            raise ValueError('Required property \'next\' not present in ListPools JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListPools object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'pools') and self.pools is not None:
            _dict['pools'] = [x.to_dict() for x in self.pools]
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'first') and self.first is not None:
            _dict['first'] = self.first.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            _dict['next'] = self.next.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListPools object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListPools') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListPools') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class LoadBalancer():
    """
    Load balancer details.

    :attr str id: (optional) Identifier of the load balancer.
    :attr str name: (optional) Name of the load balancer.
    :attr str description: (optional) Descriptive text of the load balancer.
    :attr bool enabled: (optional) Whether the load balancer is enabled.
    :attr int ttl: (optional) Time to live in second.
    :attr str health: (optional) Healthy state of the load balancer.
    :attr str fallback_pool: (optional) The pool ID to use when all other pools are
          detected as unhealthy.
    :attr List[str] default_pools: (optional) A list of pool IDs ordered by their
          failover priority. Pools defined here are used by default, or when region_pools
          are not configured for a given region.
    :attr List[LoadBalancerAzPoolsItem] az_pools: (optional) Map availability zones
          to pool ID's.
    :attr str created_on: (optional) the time when a load balancer is created.
    :attr str modified_on: (optional) the recent time when a load balancer is
          modified.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 name: str = None,
                 description: str = None,
                 enabled: bool = None,
                 ttl: int = None,
                 health: str = None,
                 fallback_pool: str = None,
                 default_pools: List[str] = None,
                 az_pools: List['LoadBalancerAzPoolsItem'] = None,
                 created_on: str = None,
                 modified_on: str = None) -> None:
        """
        Initialize a LoadBalancer object.

        :param str id: (optional) Identifier of the load balancer.
        :param str name: (optional) Name of the load balancer.
        :param str description: (optional) Descriptive text of the load balancer.
        :param bool enabled: (optional) Whether the load balancer is enabled.
        :param int ttl: (optional) Time to live in second.
        :param str health: (optional) Healthy state of the load balancer.
        :param str fallback_pool: (optional) The pool ID to use when all other
               pools are detected as unhealthy.
        :param List[str] default_pools: (optional) A list of pool IDs ordered by
               their failover priority. Pools defined here are used by default, or when
               region_pools are not configured for a given region.
        :param List[LoadBalancerAzPoolsItem] az_pools: (optional) Map availability
               zones to pool ID's.
        :param str created_on: (optional) the time when a load balancer is created.
        :param str modified_on: (optional) the recent time when a load balancer is
               modified.
        """
        self.id = id
        self.name = name
        self.description = description
        self.enabled = enabled
        self.ttl = ttl
        self.health = health
        self.fallback_pool = fallback_pool
        self.default_pools = default_pools
        self.az_pools = az_pools
        self.created_on = created_on
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LoadBalancer':
        """Initialize a LoadBalancer object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'ttl' in _dict:
            args['ttl'] = _dict.get('ttl')
        if 'health' in _dict:
            args['health'] = _dict.get('health')
        if 'fallback_pool' in _dict:
            args['fallback_pool'] = _dict.get('fallback_pool')
        if 'default_pools' in _dict:
            args['default_pools'] = _dict.get('default_pools')
        if 'az_pools' in _dict:
            args['az_pools'] = [LoadBalancerAzPoolsItem.from_dict(x) for x in _dict.get('az_pools')]
        if 'created_on' in _dict:
            args['created_on'] = _dict.get('created_on')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LoadBalancer object from a json dictionary."""
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
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'ttl') and self.ttl is not None:
            _dict['ttl'] = self.ttl
        if hasattr(self, 'health') and self.health is not None:
            _dict['health'] = self.health
        if hasattr(self, 'fallback_pool') and self.fallback_pool is not None:
            _dict['fallback_pool'] = self.fallback_pool
        if hasattr(self, 'default_pools') and self.default_pools is not None:
            _dict['default_pools'] = self.default_pools
        if hasattr(self, 'az_pools') and self.az_pools is not None:
            _dict['az_pools'] = [x.to_dict() for x in self.az_pools]
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = self.created_on
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = self.modified_on
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LoadBalancer object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LoadBalancer') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LoadBalancer') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class HealthEnum(str, Enum):
        """
        Healthy state of the load balancer.
        """
        HEALTHY = 'HEALTHY'
        DEGRADED = 'DEGRADED'
        CRITICAL = 'CRITICAL'


class Monitor():
    """
    Load balancer monitor details.

    :attr str id: (optional) Identifier of the load balancer monitor.
    :attr str name: (optional) The name of the load balancer monitor.
    :attr str description: (optional) Descriptive text of the load balancer monitor.
    :attr str type: (optional) The protocol to use for the health check. Currently
          supported protocols are 'HTTP','HTTPS' and 'TCP'.
    :attr int port: (optional) Port number to connect to for the health check.
          Required for TCP checks. HTTP and HTTPS checks should only define the port when
          using a non-standard port (HTTP: default 80, HTTPS: default 443).
    :attr int interval: (optional) The interval between each health check. Shorter
          intervals may improve failover time, but will increase load on the origins as we
          check from multiple locations.
    :attr int retries: (optional) The number of retries to attempt in case of a
          timeout before marking the origin as unhealthy. Retries are attempted
          immediately.
    :attr int timeout: (optional) The timeout (in seconds) before marking the health
          check as failed.
    :attr str method: (optional) The method to use for the health check applicable
          to HTTP/HTTPS based checks, the default value is 'GET'.
    :attr str path: (optional) The endpoint path to health check against. This
          parameter is only valid for HTTP and HTTPS monitors.
    :attr List[HealthcheckHeader] headers_: (optional) The HTTP request headers to
          send in the health check. It is recommended you set a Host header by default.
          The User-Agent header cannot be overridden. This parameter is only valid for
          HTTP and HTTPS monitors.
    :attr bool allow_insecure: (optional) Do not validate the certificate when
          monitor use HTTPS. This parameter is currently only valid for HTTPS monitors.
    :attr str expected_codes: (optional) The expected HTTP response code or code
          range of the health check. This parameter is only valid for HTTP and HTTPS
          monitors.
    :attr str expected_body: (optional) A case-insensitive sub-string to look for in
          the response body. If this string is not found, the origin will be marked as
          unhealthy. This parameter is only valid for HTTP and HTTPS monitors.
    :attr str created_on: (optional) the time when a load balancer monitor is
          created.
    :attr str modified_on: (optional) the recent time when a load balancer monitor
          is modified.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 name: str = None,
                 description: str = None,
                 type: str = None,
                 port: int = None,
                 interval: int = None,
                 retries: int = None,
                 timeout: int = None,
                 method: str = None,
                 path: str = None,
                 headers_: List['HealthcheckHeader'] = None,
                 allow_insecure: bool = None,
                 expected_codes: str = None,
                 expected_body: str = None,
                 created_on: str = None,
                 modified_on: str = None) -> None:
        """
        Initialize a Monitor object.

        :param str id: (optional) Identifier of the load balancer monitor.
        :param str name: (optional) The name of the load balancer monitor.
        :param str description: (optional) Descriptive text of the load balancer
               monitor.
        :param str type: (optional) The protocol to use for the health check.
               Currently supported protocols are 'HTTP','HTTPS' and 'TCP'.
        :param int port: (optional) Port number to connect to for the health check.
               Required for TCP checks. HTTP and HTTPS checks should only define the port
               when using a non-standard port (HTTP: default 80, HTTPS: default 443).
        :param int interval: (optional) The interval between each health check.
               Shorter intervals may improve failover time, but will increase load on the
               origins as we check from multiple locations.
        :param int retries: (optional) The number of retries to attempt in case of
               a timeout before marking the origin as unhealthy. Retries are attempted
               immediately.
        :param int timeout: (optional) The timeout (in seconds) before marking the
               health check as failed.
        :param str method: (optional) The method to use for the health check
               applicable to HTTP/HTTPS based checks, the default value is 'GET'.
        :param str path: (optional) The endpoint path to health check against. This
               parameter is only valid for HTTP and HTTPS monitors.
        :param List[HealthcheckHeader] headers_: (optional) The HTTP request
               headers to send in the health check. It is recommended you set a Host
               header by default. The User-Agent header cannot be overridden. This
               parameter is only valid for HTTP and HTTPS monitors.
        :param bool allow_insecure: (optional) Do not validate the certificate when
               monitor use HTTPS. This parameter is currently only valid for HTTPS
               monitors.
        :param str expected_codes: (optional) The expected HTTP response code or
               code range of the health check. This parameter is only valid for HTTP and
               HTTPS monitors.
        :param str expected_body: (optional) A case-insensitive sub-string to look
               for in the response body. If this string is not found, the origin will be
               marked as unhealthy. This parameter is only valid for HTTP and HTTPS
               monitors.
        :param str created_on: (optional) the time when a load balancer monitor is
               created.
        :param str modified_on: (optional) the recent time when a load balancer
               monitor is modified.
        """
        self.id = id
        self.name = name
        self.description = description
        self.type = type
        self.port = port
        self.interval = interval
        self.retries = retries
        self.timeout = timeout
        self.method = method
        self.path = path
        self.headers_ = headers_
        self.allow_insecure = allow_insecure
        self.expected_codes = expected_codes
        self.expected_body = expected_body
        self.created_on = created_on
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Monitor':
        """Initialize a Monitor object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'port' in _dict:
            args['port'] = _dict.get('port')
        if 'interval' in _dict:
            args['interval'] = _dict.get('interval')
        if 'retries' in _dict:
            args['retries'] = _dict.get('retries')
        if 'timeout' in _dict:
            args['timeout'] = _dict.get('timeout')
        if 'method' in _dict:
            args['method'] = _dict.get('method')
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        if 'headers' in _dict:
            args['headers_'] = [HealthcheckHeader.from_dict(x) for x in _dict.get('headers')]
        if 'allow_insecure' in _dict:
            args['allow_insecure'] = _dict.get('allow_insecure')
        if 'expected_codes' in _dict:
            args['expected_codes'] = _dict.get('expected_codes')
        if 'expected_body' in _dict:
            args['expected_body'] = _dict.get('expected_body')
        if 'created_on' in _dict:
            args['created_on'] = _dict.get('created_on')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Monitor object from a json dictionary."""
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
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'port') and self.port is not None:
            _dict['port'] = self.port
        if hasattr(self, 'interval') and self.interval is not None:
            _dict['interval'] = self.interval
        if hasattr(self, 'retries') and self.retries is not None:
            _dict['retries'] = self.retries
        if hasattr(self, 'timeout') and self.timeout is not None:
            _dict['timeout'] = self.timeout
        if hasattr(self, 'method') and self.method is not None:
            _dict['method'] = self.method
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self, 'headers_') and self.headers_ is not None:
            _dict['headers'] = [x.to_dict() for x in self.headers_]
        if hasattr(self, 'allow_insecure') and self.allow_insecure is not None:
            _dict['allow_insecure'] = self.allow_insecure
        if hasattr(self, 'expected_codes') and self.expected_codes is not None:
            _dict['expected_codes'] = self.expected_codes
        if hasattr(self, 'expected_body') and self.expected_body is not None:
            _dict['expected_body'] = self.expected_body
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = self.created_on
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = self.modified_on
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Monitor object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Monitor') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Monitor') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class MethodEnum(str, Enum):
        """
        The method to use for the health check applicable to HTTP/HTTPS based checks, the
        default value is 'GET'.
        """
        GET = 'GET'
        HEAD = 'HEAD'


class NextHref():
    """
    href.

    :attr str href: (optional) href.
    """

    def __init__(self,
                 *,
                 href: str = None) -> None:
        """
        Initialize a NextHref object.

        :param str href: (optional) href.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'NextHref':
        """Initialize a NextHref object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NextHref object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this NextHref object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'NextHref') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'NextHref') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Origin():
    """
    Origin server.

    :attr str name: (optional) The name of the origin server.
    :attr str description: (optional) Description of the origin server.
    :attr str address: (optional) The address of the origin server. It can be a
          hostname or an IP address.
    :attr bool enabled: (optional) Whether the origin server is enabled.
    :attr bool health: (optional) The health state of the origin server.
    :attr str health_failure_reason: (optional) The failure reason of the origin
          server if it is unhealthy.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 description: str = None,
                 address: str = None,
                 enabled: bool = None,
                 health: bool = None,
                 health_failure_reason: str = None) -> None:
        """
        Initialize a Origin object.

        :param str name: (optional) The name of the origin server.
        :param str description: (optional) Description of the origin server.
        :param str address: (optional) The address of the origin server. It can be
               a hostname or an IP address.
        :param bool enabled: (optional) Whether the origin server is enabled.
        :param bool health: (optional) The health state of the origin server.
        :param str health_failure_reason: (optional) The failure reason of the
               origin server if it is unhealthy.
        """
        self.name = name
        self.description = description
        self.address = address
        self.enabled = enabled
        self.health = health
        self.health_failure_reason = health_failure_reason

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Origin':
        """Initialize a Origin object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'address' in _dict:
            args['address'] = _dict.get('address')
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'health' in _dict:
            args['health'] = _dict.get('health')
        if 'health_failure_reason' in _dict:
            args['health_failure_reason'] = _dict.get('health_failure_reason')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Origin object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'address') and self.address is not None:
            _dict['address'] = self.address
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'health') and self.health is not None:
            _dict['health'] = self.health
        if hasattr(self, 'health_failure_reason') and self.health_failure_reason is not None:
            _dict['health_failure_reason'] = self.health_failure_reason
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Origin object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Origin') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Origin') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class OriginInput():
    """
    The request data of origin server.

    :attr str name: (optional) The name of the origin server.
    :attr str description: (optional) Description of the origin server.
    :attr str address: (optional) The address of the origin server. It can be a
          hostname or an IP address.
    :attr bool enabled: (optional) Whether the origin server is enabled.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 description: str = None,
                 address: str = None,
                 enabled: bool = None) -> None:
        """
        Initialize a OriginInput object.

        :param str name: (optional) The name of the origin server.
        :param str description: (optional) Description of the origin server.
        :param str address: (optional) The address of the origin server. It can be
               a hostname or an IP address.
        :param bool enabled: (optional) Whether the origin server is enabled.
        """
        self.name = name
        self.description = description
        self.address = address
        self.enabled = enabled

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'OriginInput':
        """Initialize a OriginInput object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'address' in _dict:
            args['address'] = _dict.get('address')
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a OriginInput object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'address') and self.address is not None:
            _dict['address'] = self.address
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this OriginInput object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'OriginInput') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'OriginInput') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Pool():
    """
    Load balancer pool details.

    :attr str id: (optional) Identifier of the load balancer pool.
    :attr str name: (optional) Name of the load balancer pool.
    :attr str description: (optional) Descriptive text of the load balancer pool.
    :attr bool enabled: (optional) Whether the load balancer pool is enabled.
    :attr int healthy_origins_threshold: (optional) The minimum number of origins
          that must be healthy for this pool to serve traffic. If the number of healthy
          origins falls below this number, the pool will be marked unhealthy and we will
          failover to the next available pool.
    :attr List[Origin] origins: (optional) The list of origins within this pool.
          Traffic directed at this pool is balanced across all currently healthy origins,
          provided the pool itself is healthy.
    :attr str monitor: (optional) The ID of the load balancer monitor to be
          associated to this pool.
    :attr str notification_channel: (optional) The notification channel.
    :attr str health: (optional) Healthy state of the load balancer pool.
    :attr str healthcheck_region: (optional) Health check region of VSIs.
    :attr List[str] healthcheck_subnets: (optional) Health check subnet IDs of VSIs.
    :attr str created_on: (optional) the time when a load balancer pool is created.
    :attr str modified_on: (optional) the recent time when a load balancer pool is
          modified.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 name: str = None,
                 description: str = None,
                 enabled: bool = None,
                 healthy_origins_threshold: int = None,
                 origins: List['Origin'] = None,
                 monitor: str = None,
                 notification_channel: str = None,
                 health: str = None,
                 healthcheck_region: str = None,
                 healthcheck_subnets: List[str] = None,
                 created_on: str = None,
                 modified_on: str = None) -> None:
        """
        Initialize a Pool object.

        :param str id: (optional) Identifier of the load balancer pool.
        :param str name: (optional) Name of the load balancer pool.
        :param str description: (optional) Descriptive text of the load balancer
               pool.
        :param bool enabled: (optional) Whether the load balancer pool is enabled.
        :param int healthy_origins_threshold: (optional) The minimum number of
               origins that must be healthy for this pool to serve traffic. If the number
               of healthy origins falls below this number, the pool will be marked
               unhealthy and we will failover to the next available pool.
        :param List[Origin] origins: (optional) The list of origins within this
               pool. Traffic directed at this pool is balanced across all currently
               healthy origins, provided the pool itself is healthy.
        :param str monitor: (optional) The ID of the load balancer monitor to be
               associated to this pool.
        :param str notification_channel: (optional) The notification channel.
        :param str health: (optional) Healthy state of the load balancer pool.
        :param str healthcheck_region: (optional) Health check region of VSIs.
        :param List[str] healthcheck_subnets: (optional) Health check subnet IDs of
               VSIs.
        :param str created_on: (optional) the time when a load balancer pool is
               created.
        :param str modified_on: (optional) the recent time when a load balancer
               pool is modified.
        """
        self.id = id
        self.name = name
        self.description = description
        self.enabled = enabled
        self.healthy_origins_threshold = healthy_origins_threshold
        self.origins = origins
        self.monitor = monitor
        self.notification_channel = notification_channel
        self.health = health
        self.healthcheck_region = healthcheck_region
        self.healthcheck_subnets = healthcheck_subnets
        self.created_on = created_on
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Pool':
        """Initialize a Pool object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'healthy_origins_threshold' in _dict:
            args['healthy_origins_threshold'] = _dict.get('healthy_origins_threshold')
        if 'origins' in _dict:
            args['origins'] = [Origin.from_dict(x) for x in _dict.get('origins')]
        if 'monitor' in _dict:
            args['monitor'] = _dict.get('monitor')
        if 'notification_channel' in _dict:
            args['notification_channel'] = _dict.get('notification_channel')
        if 'health' in _dict:
            args['health'] = _dict.get('health')
        if 'healthcheck_region' in _dict:
            args['healthcheck_region'] = _dict.get('healthcheck_region')
        if 'healthcheck_subnets' in _dict:
            args['healthcheck_subnets'] = _dict.get('healthcheck_subnets')
        if 'created_on' in _dict:
            args['created_on'] = _dict.get('created_on')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Pool object from a json dictionary."""
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
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'healthy_origins_threshold') and self.healthy_origins_threshold is not None:
            _dict['healthy_origins_threshold'] = self.healthy_origins_threshold
        if hasattr(self, 'origins') and self.origins is not None:
            _dict['origins'] = [x.to_dict() for x in self.origins]
        if hasattr(self, 'monitor') and self.monitor is not None:
            _dict['monitor'] = self.monitor
        if hasattr(self, 'notification_channel') and self.notification_channel is not None:
            _dict['notification_channel'] = self.notification_channel
        if hasattr(self, 'health') and self.health is not None:
            _dict['health'] = self.health
        if hasattr(self, 'healthcheck_region') and self.healthcheck_region is not None:
            _dict['healthcheck_region'] = self.healthcheck_region
        if hasattr(self, 'healthcheck_subnets') and self.healthcheck_subnets is not None:
            _dict['healthcheck_subnets'] = self.healthcheck_subnets
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = self.created_on
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = self.modified_on
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Pool object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Pool') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Pool') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class HealthEnum(str, Enum):
        """
        Healthy state of the load balancer pool.
        """
        HEALTHY = 'HEALTHY'
        DEGRADED = 'DEGRADED'
        CRITICAL = 'CRITICAL'


    class HealthcheckRegionEnum(str, Enum):
        """
        Health check region of VSIs.
        """
        US_SOUTH = 'us-south'
        US_EAST = 'us-east'
        EU_GB = 'eu-gb'
        EU_DU = 'eu-du'
        AU_SYD = 'au-syd'
        JP_TOK = 'jp-tok'

