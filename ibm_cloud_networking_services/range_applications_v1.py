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
Range Applications
"""

from datetime import datetime
from enum import Enum
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model, datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class RangeApplicationsV1(BaseService):
    """The Range Applications V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com/'
    DEFAULT_SERVICE_NAME = 'range_applications'

    @classmethod
    def new_instance(cls,
                     crn: str,
                     zone_identifier: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'RangeApplicationsV1':
        """
        Return a new client for the Range Applications service using the specified
               parameters and external configuration.

        :param str crn: Full url-encoded cloud resource name (CRN) of resource
               instance.

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
        Construct a new client for the Range Applications service.

        :param str crn: Full url-encoded cloud resource name (CRN) of resource
               instance.

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
    # List Range Applications
    #########################


    def list_range_apps(self, **kwargs) -> DetailedResponse:
        """
        Get a list of currently existing Range Applications inside a zone.

        Get a list of currently existing Range Applications inside a zone.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RangeApplications` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='list_range_apps')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/range/apps'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Get Range Application
    #########################


    def get_range_app(self, app_identifier: str, **kwargs) -> DetailedResponse:
        """
        Get the application configuration of a specific application inside a zone.

        Get the application configuration of a specific application inside a zone.

        :param str app_identifier: application identifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RangeApplicationObject` object
        """

        if app_identifier is None:
            raise ValueError('app_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_range_app')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/range/apps/{2}'.format(*self.encode_path_vars(self.crn, self.zone_identifier, app_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Create a Range Application
    #########################


    def create_range_app(self, protocol: str, dns: 'RangeAppReqDns', *, origin_direct: List[str] = None, origin_dns: 'RangeAppReqOriginDns' = None, origin_port: int = None, ip_firewall: bool = None, proxy_protocol: str = None, edge_ips: 'RangeAppReqEdgeIps' = None, traffic_type: str = None, tls: str = None, **kwargs) -> DetailedResponse:
        """
        Create a Range Applications inside a zone.

        Create a Range Applications inside a zone.

        :param str protocol: Defines the protocol and port for this application.
        :param RangeAppReqDns dns: Name and type of the DNS record for this
               application.
        :param List[str] origin_direct: (optional) IP address and port of the
               origin for this Range application. If configuring a load balancer, use
               'origin_dns' and 'origin_port'. This can not be combined with 'origin_dns'
               and 'origin_port'.
        :param RangeAppReqOriginDns origin_dns: (optional) DNS record pointing to
               the origin for this Range application. This is used for configuring a load
               balancer. When specifying an individual IP address, use 'origin_direct'.
               This requires 'origin_port' and can not be combined with 'origin_direct'.
        :param int origin_port: (optional) Port at the origin that listens to
               traffic from this Range application. Requires 'origin_dns' and can not be
               combined with 'origin_direct'.
        :param bool ip_firewall: (optional) Enables the IP Firewall for this
               application. Only available for TCP applications.
        :param str proxy_protocol: (optional) Allows for the true client IP to be
               passed to the service.
        :param RangeAppReqEdgeIps edge_ips: (optional) Configures IP version for
               the hostname of this application. Default is {"type":"dynamic",
               "connectivity":"all"}.
        :param str traffic_type: (optional) Configure how traffic is handled at the
               edge. If set to "direct" traffic is passed through to the service. In the
               case of "http" or "https" HTTP/s features at the edge are applied ot this
               traffic.
        :param str tls: (optional) Configure if and how TLS connections are
               terminated at the edge.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RangeApplicationObject` object
        """

        if protocol is None:
            raise ValueError('protocol must be provided')
        if dns is None:
            raise ValueError('dns must be provided')
        dns = convert_model(dns)
        if origin_dns is not None:
            origin_dns = convert_model(origin_dns)
        if edge_ips is not None:
            edge_ips = convert_model(edge_ips)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='create_range_app')
        headers.update(sdk_headers)

        data = {
            'protocol': protocol,
            'dns': dns,
            'origin_direct': origin_direct,
            'origin_dns': origin_dns,
            'origin_port': origin_port,
            'ip_firewall': ip_firewall,
            'proxy_protocol': proxy_protocol,
            'edge_ips': edge_ips,
            'traffic_type': traffic_type,
            'tls': tls
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/range/apps'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Update a Range Application
    #########################


    def update_range_app(self, app_identifier: str, protocol: str, dns: 'RangeAppReqDns', *, origin_direct: List[str] = None, origin_dns: 'RangeAppReqOriginDns' = None, origin_port: int = None, ip_firewall: bool = None, proxy_protocol: str = None, edge_ips: 'RangeAppReqEdgeIps' = None, traffic_type: str = None, tls: str = None, **kwargs) -> DetailedResponse:
        """
        Update a specific range application.

        Update a Range Application inside a zone.

        :param str app_identifier: application identifier.
        :param str protocol: Defines the protocol and port for this application.
        :param RangeAppReqDns dns: Name and type of the DNS record for this
               application.
        :param List[str] origin_direct: (optional) IP address and port of the
               origin for this Range application. If configuring a load balancer, use
               'origin_dns' and 'origin_port'. This can not be combined with 'origin_dns'
               and 'origin_port'.
        :param RangeAppReqOriginDns origin_dns: (optional) DNS record pointing to
               the origin for this Range application. This is used for configuring a load
               balancer. When specifying an individual IP address, use 'origin_direct'.
               This requires 'origin_port' and can not be combined with 'origin_direct'.
        :param int origin_port: (optional) Port at the origin that listens to
               traffic from this Range application. Requires 'origin_dns' and can not be
               combined with 'origin_direct'.
        :param bool ip_firewall: (optional) Enables the IP Firewall for this
               application. Only available for TCP applications.
        :param str proxy_protocol: (optional) Allows for the true client IP to be
               passed to the service.
        :param RangeAppReqEdgeIps edge_ips: (optional) Configures IP version for
               the hostname of this application. Default is {"type":"dynamic",
               "connectivity":"all"}.
        :param str traffic_type: (optional) Configure how traffic is handled at the
               edge. If set to "direct" traffic is passed through to the service. In the
               case of "http" or "https" HTTP/s features at the edge are applied ot this
               traffic.
        :param str tls: (optional) Configure if and how TLS connections are
               terminated at the edge.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RangeApplicationObject` object
        """

        if app_identifier is None:
            raise ValueError('app_identifier must be provided')
        if protocol is None:
            raise ValueError('protocol must be provided')
        if dns is None:
            raise ValueError('dns must be provided')
        dns = convert_model(dns)
        if origin_dns is not None:
            origin_dns = convert_model(origin_dns)
        if edge_ips is not None:
            edge_ips = convert_model(edge_ips)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_range_app')
        headers.update(sdk_headers)

        data = {
            'protocol': protocol,
            'dns': dns,
            'origin_direct': origin_direct,
            'origin_dns': origin_dns,
            'origin_port': origin_port,
            'ip_firewall': ip_firewall,
            'proxy_protocol': proxy_protocol,
            'edge_ips': edge_ips,
            'traffic_type': traffic_type,
            'tls': tls
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/range/apps/{2}'.format(*self.encode_path_vars(self.crn, self.zone_identifier, app_identifier))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Delete a Range Application
    #########################


    def delete_range_app(self, app_identifier: str, **kwargs) -> DetailedResponse:
        """
        Delete the application configuration.

        Delete a specific application configuration.

        :param str app_identifier: application identifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RangeApplicationDelete` object
        """

        if app_identifier is None:
            raise ValueError('app_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='delete_range_app')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/range/apps/{2}'.format(*self.encode_path_vars(self.crn, self.zone_identifier, app_identifier))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

