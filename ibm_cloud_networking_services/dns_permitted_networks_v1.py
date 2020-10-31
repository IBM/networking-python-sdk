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
Permitted Networks for DNS Zones
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

class DnsPermittedNetworksV1(BaseService):
    """The DNS Permitted Networks V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.dns-svcs.cloud.ibm.com/v1'
    DEFAULT_SERVICE_NAME = 'dns_permitted_networks'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'DnsPermittedNetworksV1':
        """
        Return a new client for the DNS Permitted Networks service using the
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
        Construct a new client for the DNS Permitted Networks service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # Permitted Network
    #########################


    def list_permitted_networks(self,
        instance_id: str,
        dnszone_id: str,
        *,
        x_correlation_id: str = None,
        offset: str = None,
        limit: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List permitted networks.

        List the permitted networks for a given DNS zone.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param str offset: (optional) Specify how many permitted networks to skip
               over, the default value is 0.
        :param str limit: (optional) Specify how many permitted networks are
               returned, the default value is 10.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListPermittedNetworks` object
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
                                      operation_id='list_permitted_networks')
        headers.update(sdk_headers)

        params = {
            'offset': offset,
            'limit': limit
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/instances/{0}/dnszones/{1}/permitted_networks'.format(
            *self.encode_path_vars(instance_id, dnszone_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_permitted_network(self,
        instance_id: str,
        dnszone_id: str,
        *,
        type: str = None,
        permitted_network: 'PermittedNetworkVpc' = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a permitted network.

        Create a permitted network for a given DNS zone.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str type: (optional) The type of a permitted network.
        :param PermittedNetworkVpc permitted_network: (optional) Permitted network
               data for VPC.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PermittedNetwork` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if dnszone_id is None:
            raise ValueError('dnszone_id must be provided')
        if permitted_network is not None:
            permitted_network = convert_model(permitted_network)
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_permitted_network')
        headers.update(sdk_headers)

        data = {
            'type': type,
            'permitted_network': permitted_network
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/instances/{0}/dnszones/{1}/permitted_networks'.format(
            *self.encode_path_vars(instance_id, dnszone_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_permitted_network(self,
        instance_id: str,
        dnszone_id: str,
        permitted_network_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Remove a permitted network.

        Remove a permitted network.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str permitted_network_id: The unique identifier of a permitted
               network.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PermittedNetwork` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if dnszone_id is None:
            raise ValueError('dnszone_id must be provided')
        if permitted_network_id is None:
            raise ValueError('permitted_network_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_permitted_network')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/instances/{0}/dnszones/{1}/permitted_networks/{2}'.format(
            *self.encode_path_vars(instance_id, dnszone_id, permitted_network_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_permitted_network(self,
        instance_id: str,
        dnszone_id: str,
        permitted_network_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a permitted network.

        Get details of a permitted network.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str permitted_network_id: The unique identifier of a permitted
               network.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PermittedNetwork` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if dnszone_id is None:
            raise ValueError('dnszone_id must be provided')
        if permitted_network_id is None:
            raise ValueError('permitted_network_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_permitted_network')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/instances/{0}/dnszones/{1}/permitted_networks/{2}'.format(
            *self.encode_path_vars(instance_id, dnszone_id, permitted_network_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


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

class ListPermittedNetworks():
    """
    List permitted networks response.

    :attr List[PermittedNetwork] permitted_networks: An array of permitted networks.
    :attr int offset: Specify how many permitted networks to skip over, the default
          value is 0.
    :attr int limit: Specify how many permitted networks are returned, the default
          value is 10.
    :attr int total_count: Total number of permitted networks.
    :attr FirstHref first: href.
    :attr NextHref next: (optional) href.
    """

    def __init__(self,
                 permitted_networks: List['PermittedNetwork'],
                 offset: int,
                 limit: int,
                 total_count: int,
                 first: 'FirstHref',
                 *,
                 next: 'NextHref' = None) -> None:
        """
        Initialize a ListPermittedNetworks object.

        :param List[PermittedNetwork] permitted_networks: An array of permitted
               networks.
        :param int offset: Specify how many permitted networks to skip over, the
               default value is 0.
        :param int limit: Specify how many permitted networks are returned, the
               default value is 10.
        :param int total_count: Total number of permitted networks.
        :param FirstHref first: href.
        :param NextHref next: (optional) href.
        """
        self.permitted_networks = permitted_networks
        self.offset = offset
        self.limit = limit
        self.total_count = total_count
        self.first = first
        self.next = next

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListPermittedNetworks':
        """Initialize a ListPermittedNetworks object from a json dictionary."""
        args = {}
        if 'permitted_networks' in _dict:
            args['permitted_networks'] = [PermittedNetwork.from_dict(x) for x in _dict.get('permitted_networks')]
        else:
            raise ValueError('Required property \'permitted_networks\' not present in ListPermittedNetworks JSON')
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        else:
            raise ValueError('Required property \'offset\' not present in ListPermittedNetworks JSON')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in ListPermittedNetworks JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in ListPermittedNetworks JSON')
        if 'first' in _dict:
            args['first'] = FirstHref.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in ListPermittedNetworks JSON')
        if 'next' in _dict:
            args['next'] = NextHref.from_dict(_dict.get('next'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListPermittedNetworks object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'permitted_networks') and self.permitted_networks is not None:
            _dict['permitted_networks'] = [x.to_dict() for x in self.permitted_networks]
        if hasattr(self, 'offset') and self.offset is not None:
            _dict['offset'] = self.offset
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
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
        """Return a `str` version of this ListPermittedNetworks object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListPermittedNetworks') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListPermittedNetworks') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

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

class PermittedNetwork():
    """
    Permitted network details.

    :attr str id: (optional) Unique identifier of a permitted network.
    :attr str created_on: (optional) The time when a permitted network is created.
    :attr str modified_on: (optional) The recent time when a permitted network is
          modified.
    :attr PermittedNetworkVpc permitted_network: (optional) Permitted network data
          for VPC.
    :attr str type: (optional) The type of a permitted network.
    :attr str state: (optional) The state of a permitted network.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 created_on: str = None,
                 modified_on: str = None,
                 permitted_network: 'PermittedNetworkVpc' = None,
                 type: str = None,
                 state: str = None) -> None:
        """
        Initialize a PermittedNetwork object.

        :param str id: (optional) Unique identifier of a permitted network.
        :param str created_on: (optional) The time when a permitted network is
               created.
        :param str modified_on: (optional) The recent time when a permitted network
               is modified.
        :param PermittedNetworkVpc permitted_network: (optional) Permitted network
               data for VPC.
        :param str type: (optional) The type of a permitted network.
        :param str state: (optional) The state of a permitted network.
        """
        self.id = id
        self.created_on = created_on
        self.modified_on = modified_on
        self.permitted_network = permitted_network
        self.type = type
        self.state = state

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PermittedNetwork':
        """Initialize a PermittedNetwork object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'created_on' in _dict:
            args['created_on'] = _dict.get('created_on')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        if 'permitted_network' in _dict:
            args['permitted_network'] = PermittedNetworkVpc.from_dict(_dict.get('permitted_network'))
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PermittedNetwork object from a json dictionary."""
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
        if hasattr(self, 'permitted_network') and self.permitted_network is not None:
            _dict['permitted_network'] = self.permitted_network.to_dict()
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PermittedNetwork object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PermittedNetwork') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PermittedNetwork') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of a permitted network.
        """
        VPC = 'vpc'


    class StateEnum(str, Enum):
        """
        The state of a permitted network.
        """
        ACTIVE = 'ACTIVE'
        REMOVAL_IN_PROGRESS = 'REMOVAL_IN_PROGRESS'


class PermittedNetworkVpc():
    """
    Permitted network data for VPC.

    :attr str vpc_crn: CRN string uniquely identifies a VPC.
    """

    def __init__(self,
                 vpc_crn: str) -> None:
        """
        Initialize a PermittedNetworkVpc object.

        :param str vpc_crn: CRN string uniquely identifies a VPC.
        """
        self.vpc_crn = vpc_crn

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PermittedNetworkVpc':
        """Initialize a PermittedNetworkVpc object from a json dictionary."""
        args = {}
        if 'vpc_crn' in _dict:
            args['vpc_crn'] = _dict.get('vpc_crn')
        else:
            raise ValueError('Required property \'vpc_crn\' not present in PermittedNetworkVpc JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PermittedNetworkVpc object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'vpc_crn') and self.vpc_crn is not None:
            _dict['vpc_crn'] = self.vpc_crn
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PermittedNetworkVpc object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PermittedNetworkVpc') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PermittedNetworkVpc') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
