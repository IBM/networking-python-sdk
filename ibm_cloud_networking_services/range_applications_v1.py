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

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
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
    # Range Applications
    #########################


    def list_range_apps(self,
        *,
        page: int = None,
        per_page: int = None,
        order: str = None,
        direction: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List range applications.

        Get a list of currently existing Range Applications inside a zone.

        :param int page: (optional) Page number of paginated results.
        :param int per_page: (optional) Maximum number of Range applications per
               page.
        :param str order: (optional) Field by which to order the list of Range
               applications.
        :param str direction: (optional) Direction in which to order results
               [ascending/descending order].
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RangeApplications` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_range_apps')
        headers.update(sdk_headers)

        params = {
            'page': page,
            'per_page': per_page,
            'order': order,
            'direction': direction
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/range/apps'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_range_app(self,
        protocol: str,
        dns: 'RangeAppReqDns',
        *,
        origin_direct: List[str] = None,
        origin_dns: 'RangeAppReqOriginDns' = None,
        origin_port: int = None,
        ip_firewall: bool = None,
        proxy_protocol: str = None,
        edge_ips: 'RangeAppReqEdgeIps' = None,
        traffic_type: str = None,
        tls: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create Range Application.

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
        :rtype: DetailedResponse with `dict` result representing a `RangeApplicationResp` object
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_range_app')
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

        url = '/v1/{0}/zones/{1}/range/apps'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_range_app(self,
        app_identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get range application a zone.

        Get the application configuration of a specific application inside a zone.

        :param str app_identifier: application identifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RangeApplicationResp` object
        """

        if app_identifier is None:
            raise ValueError('app_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_range_app')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/range/apps/{2}'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier, app_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_range_app(self,
        app_identifier: str,
        protocol: str,
        dns: 'RangeAppReqDns',
        *,
        origin_direct: List[str] = None,
        origin_dns: 'RangeAppReqOriginDns' = None,
        origin_port: int = None,
        ip_firewall: bool = None,
        proxy_protocol: str = None,
        edge_ips: 'RangeAppReqEdgeIps' = None,
        traffic_type: str = None,
        tls: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update range application.

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
        :rtype: DetailedResponse with `dict` result representing a `RangeApplicationResp` object
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_range_app')
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

        url = '/v1/{0}/zones/{1}/range/apps/{2}'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier, app_identifier))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_range_app(self,
        app_identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete range application.

        Delete a specific application configuration.

        :param str app_identifier: application identifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `RangeApplicationResp` object
        """

        if app_identifier is None:
            raise ValueError('app_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_range_app')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/range/apps/{2}'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier, app_identifier))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


class ListRangeAppsEnums:
    """
    Enums for list_range_apps parameters.
    """

    class Order(str, Enum):
        """
        Field by which to order the list of Range applications.
        """
        PROTOCOL = 'protocol'
        APP_ID = 'app_id'
        CREATED_ON = 'created_on'
        MODIFIED_ON = 'modified_on'
        DNS = 'dns'
    class Direction(str, Enum):
        """
        Direction in which to order results [ascending/descending order].
        """
        ASC = 'asc'
        DESC = 'desc'


##############################################################################
# Models
##############################################################################


class RangeAppReqDns():
    """
    Name and type of the DNS record for this application.

    :attr str type: (optional) DNS record type.
    :attr str name: (optional) DNS record name.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 name: str = None) -> None:
        """
        Initialize a RangeAppReqDns object.

        :param str type: (optional) DNS record type.
        :param str name: (optional) DNS record name.
        """
        self.type = type
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RangeAppReqDns':
        """Initialize a RangeAppReqDns object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RangeAppReqDns object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RangeAppReqDns object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RangeAppReqDns') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RangeAppReqDns') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RangeAppReqEdgeIps():
    """
    Configures IP version for the hostname of this application. Default is
    {"type":"dynamic", "connectivity":"all"}.

    :attr str type: (optional) The type of edge IP configuration.
    :attr str connectivity: (optional) Specifies the IP version (or all).
    """

    def __init__(self,
                 *,
                 type: str = None,
                 connectivity: str = None) -> None:
        """
        Initialize a RangeAppReqEdgeIps object.

        :param str type: (optional) The type of edge IP configuration.
        :param str connectivity: (optional) Specifies the IP version (or all).
        """
        self.type = type
        self.connectivity = connectivity

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RangeAppReqEdgeIps':
        """Initialize a RangeAppReqEdgeIps object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'connectivity' in _dict:
            args['connectivity'] = _dict.get('connectivity')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RangeAppReqEdgeIps object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'connectivity') and self.connectivity is not None:
            _dict['connectivity'] = self.connectivity
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RangeAppReqEdgeIps object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RangeAppReqEdgeIps') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RangeAppReqEdgeIps') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of edge IP configuration.
        """
        DYNAMIC = 'dynamic'


    class ConnectivityEnum(str, Enum):
        """
        Specifies the IP version (or all).
        """
        IPV4 = 'ipv4'
        IPV6 = 'ipv6'
        ALL = 'all'


class RangeAppReqOriginDns():
    """
    DNS record pointing to the origin for this Range application. This is used for
    configuring a load balancer. When specifying an individual IP address, use
    'origin_direct'. This requires 'origin_port' and can not be combined with
    'origin_direct'.

    :attr str name: Name of the origin.
    """

    def __init__(self,
                 name: str) -> None:
        """
        Initialize a RangeAppReqOriginDns object.

        :param str name: Name of the origin.
        """
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RangeAppReqOriginDns':
        """Initialize a RangeAppReqOriginDns object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in RangeAppReqOriginDns JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RangeAppReqOriginDns object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RangeAppReqOriginDns object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RangeAppReqOriginDns') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RangeAppReqOriginDns') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RangeApplicationObjectDns():
    """
    The name and type of DNS record for the Range application.

    :attr str type: (optional) The type of DNS record associated with the
          application.
    :attr str name: (optional) The name of the DNS record associated with the
          application.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 name: str = None) -> None:
        """
        Initialize a RangeApplicationObjectDns object.

        :param str type: (optional) The type of DNS record associated with the
               application.
        :param str name: (optional) The name of the DNS record associated with the
               application.
        """
        self.type = type
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RangeApplicationObjectDns':
        """Initialize a RangeApplicationObjectDns object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RangeApplicationObjectDns object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RangeApplicationObjectDns object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RangeApplicationObjectDns') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RangeApplicationObjectDns') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of DNS record associated with the application.
        """
        CNAME = 'CNAME'


class RangeApplicationObjectEdgeIps():
    """
    Configures IP version for the hostname of this application.

    :attr str type: (optional) The type of edge IP configuration.
    :attr str connectivity: (optional) Specifies the IP version (or all).
    """

    def __init__(self,
                 *,
                 type: str = None,
                 connectivity: str = None) -> None:
        """
        Initialize a RangeApplicationObjectEdgeIps object.

        :param str type: (optional) The type of edge IP configuration.
        :param str connectivity: (optional) Specifies the IP version (or all).
        """
        self.type = type
        self.connectivity = connectivity

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RangeApplicationObjectEdgeIps':
        """Initialize a RangeApplicationObjectEdgeIps object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'connectivity' in _dict:
            args['connectivity'] = _dict.get('connectivity')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RangeApplicationObjectEdgeIps object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'connectivity') and self.connectivity is not None:
            _dict['connectivity'] = self.connectivity
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RangeApplicationObjectEdgeIps object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RangeApplicationObjectEdgeIps') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RangeApplicationObjectEdgeIps') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of edge IP configuration.
        """
        DYNAMIC = 'dynamic'


    class ConnectivityEnum(str, Enum):
        """
        Specifies the IP version (or all).
        """
        IPV4 = 'ipv4'
        IPV6 = 'ipv6'
        ALL = 'all'


class RangeApplicationObject():
    """
    range application object.

    :attr str id: (optional) Application identifier.
    :attr str protocol: (optional) Port configuration.
    :attr RangeApplicationObjectDns dns: (optional) The name and type of DNS record
          for the Range application.
    :attr List[str] origin_direct: (optional) A list of destination addresses to the
          origin.
    :attr bool ip_firewall: (optional) Enables the IP Firewall for this application.
    :attr str proxy_protocol: (optional) Allows for the true client IP to be passed
          to the service.
    :attr RangeApplicationObjectEdgeIps edge_ips: (optional) Configures IP version
          for the hostname of this application.
    :attr str tls: (optional) Specifies the TLS termination at the edge.
    :attr str traffic_type: (optional) Configure how traffic is handled at the edge.
          If set to "direct" traffic is passed through to the service. In the case of
          "http" or "https" HTTP/s features at the edge are applied ot this traffic.
    :attr datetime created_on: (optional) When the Application was created.
    :attr datetime modified_on: (optional) When the Application was last modified.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 protocol: str = None,
                 dns: 'RangeApplicationObjectDns' = None,
                 origin_direct: List[str] = None,
                 ip_firewall: bool = None,
                 proxy_protocol: str = None,
                 edge_ips: 'RangeApplicationObjectEdgeIps' = None,
                 tls: str = None,
                 traffic_type: str = None,
                 created_on: datetime = None,
                 modified_on: datetime = None) -> None:
        """
        Initialize a RangeApplicationObject object.

        :param str id: (optional) Application identifier.
        :param str protocol: (optional) Port configuration.
        :param RangeApplicationObjectDns dns: (optional) The name and type of DNS
               record for the Range application.
        :param List[str] origin_direct: (optional) A list of destination addresses
               to the origin.
        :param bool ip_firewall: (optional) Enables the IP Firewall for this
               application.
        :param str proxy_protocol: (optional) Allows for the true client IP to be
               passed to the service.
        :param RangeApplicationObjectEdgeIps edge_ips: (optional) Configures IP
               version for the hostname of this application.
        :param str tls: (optional) Specifies the TLS termination at the edge.
        :param str traffic_type: (optional) Configure how traffic is handled at the
               edge. If set to "direct" traffic is passed through to the service. In the
               case of "http" or "https" HTTP/s features at the edge are applied ot this
               traffic.
        :param datetime created_on: (optional) When the Application was created.
        :param datetime modified_on: (optional) When the Application was last
               modified.
        """
        self.id = id
        self.protocol = protocol
        self.dns = dns
        self.origin_direct = origin_direct
        self.ip_firewall = ip_firewall
        self.proxy_protocol = proxy_protocol
        self.edge_ips = edge_ips
        self.tls = tls
        self.traffic_type = traffic_type
        self.created_on = created_on
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RangeApplicationObject':
        """Initialize a RangeApplicationObject object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'protocol' in _dict:
            args['protocol'] = _dict.get('protocol')
        if 'dns' in _dict:
            args['dns'] = RangeApplicationObjectDns.from_dict(_dict.get('dns'))
        if 'origin_direct' in _dict:
            args['origin_direct'] = _dict.get('origin_direct')
        if 'ip_firewall' in _dict:
            args['ip_firewall'] = _dict.get('ip_firewall')
        if 'proxy_protocol' in _dict:
            args['proxy_protocol'] = _dict.get('proxy_protocol')
        if 'edge_ips' in _dict:
            args['edge_ips'] = RangeApplicationObjectEdgeIps.from_dict(_dict.get('edge_ips'))
        if 'tls' in _dict:
            args['tls'] = _dict.get('tls')
        if 'traffic_type' in _dict:
            args['traffic_type'] = _dict.get('traffic_type')
        if 'created_on' in _dict:
            args['created_on'] = string_to_datetime(_dict.get('created_on'))
        if 'modified_on' in _dict:
            args['modified_on'] = string_to_datetime(_dict.get('modified_on'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RangeApplicationObject object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'protocol') and self.protocol is not None:
            _dict['protocol'] = self.protocol
        if hasattr(self, 'dns') and self.dns is not None:
            _dict['dns'] = self.dns.to_dict()
        if hasattr(self, 'origin_direct') and self.origin_direct is not None:
            _dict['origin_direct'] = self.origin_direct
        if hasattr(self, 'ip_firewall') and self.ip_firewall is not None:
            _dict['ip_firewall'] = self.ip_firewall
        if hasattr(self, 'proxy_protocol') and self.proxy_protocol is not None:
            _dict['proxy_protocol'] = self.proxy_protocol
        if hasattr(self, 'edge_ips') and self.edge_ips is not None:
            _dict['edge_ips'] = self.edge_ips.to_dict()
        if hasattr(self, 'tls') and self.tls is not None:
            _dict['tls'] = self.tls
        if hasattr(self, 'traffic_type') and self.traffic_type is not None:
            _dict['traffic_type'] = self.traffic_type
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = datetime_to_string(self.created_on)
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = datetime_to_string(self.modified_on)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RangeApplicationObject object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RangeApplicationObject') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RangeApplicationObject') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ProxyProtocolEnum(str, Enum):
        """
        Allows for the true client IP to be passed to the service.
        """
        OFF = 'off'
        V1 = 'v1'
        V2 = 'v2'
        SIMPLE = 'simple'


    class TlsEnum(str, Enum):
        """
        Specifies the TLS termination at the edge.
        """
        OFF = 'off'
        FLEXIBLE = 'flexible'
        FULL = 'full'
        STRICT = 'strict'


    class TrafficTypeEnum(str, Enum):
        """
        Configure how traffic is handled at the edge. If set to "direct" traffic is passed
        through to the service. In the case of "http" or "https" HTTP/s features at the
        edge are applied ot this traffic.
        """
        DIRECT = 'direct'
        HTTP = 'http'
        HTTPS = 'https'


class RangeApplicationResp():
    """
    range application response.

    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: errors.
    :attr List[List[str]] messages: messages.
    :attr RangeApplicationObject result: range application object.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'RangeApplicationObject') -> None:
        """
        Initialize a RangeApplicationResp object.

        :param bool success: Was the get successful.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param RangeApplicationObject result: range application object.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RangeApplicationResp':
        """Initialize a RangeApplicationResp object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in RangeApplicationResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in RangeApplicationResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in RangeApplicationResp JSON')
        if 'result' in _dict:
            args['result'] = RangeApplicationObject.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in RangeApplicationResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RangeApplicationResp object from a json dictionary."""
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
        """Return a `str` version of this RangeApplicationResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RangeApplicationResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RangeApplicationResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RangeApplications():
    """
    range application.

    :attr bool success: Was the get successful.
    :attr List[List[str]] errors: errors.
    :attr List[List[str]] messages: messages.
    :attr List[RangeApplicationObject] result: Container for Range application
          objects.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: List['RangeApplicationObject']) -> None:
        """
        Initialize a RangeApplications object.

        :param bool success: Was the get successful.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param List[RangeApplicationObject] result: Container for Range application
               objects.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RangeApplications':
        """Initialize a RangeApplications object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in RangeApplications JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in RangeApplications JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in RangeApplications JSON')
        if 'result' in _dict:
            args['result'] = [RangeApplicationObject.from_dict(x) for x in _dict.get('result')]
        else:
            raise ValueError('Required property \'result\' not present in RangeApplications JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RangeApplications object from a json dictionary."""
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
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RangeApplications object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RangeApplications') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RangeApplications') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
