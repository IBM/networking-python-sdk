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
Resource Records
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

class ResourceRecordsV1(BaseService):
    """The Resource Records V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.dns-svcs.cloud.ibm.com/v1'
    DEFAULT_SERVICE_NAME = 'resource_records'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'ResourceRecordsV1':
        """
        Return a new client for the Resource Records service using the specified
               parameters and external configuration.
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
        Construct a new client for the Resource Records service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # Resource Records
    #########################


    def list_resource_records(self,
        instance_id: str,
        dnszone_id: str,
        *,
        x_correlation_id: str = None,
        offset: int = None,
        limit: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List Resource Records.

        List the Resource Records for a given DNS zone.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param int offset: (optional) Specify how many resource records to skip
               over, the default value is 0.
        :param int limit: (optional) Specify how many resource records are
               returned, the default value is 200.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListResourceRecords` object
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
                                      operation_id='list_resource_records')
        headers.update(sdk_headers)

        params = {
            'offset': offset,
            'limit': limit
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/instances/{0}/dnszones/{1}/resource_records'.format(
            *self.encode_path_vars(instance_id, dnszone_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_resource_record(self,
        instance_id: str,
        dnszone_id: str,
        *,
        type: str = None,
        name: str = None,
        rdata: 'ResourceRecordInputRdata' = None,
        ttl: int = None,
        service: str = None,
        protocol: str = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a resource record.

        Create a resource record for a given DNS zone.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str type: (optional) Type of the resource record.
        :param str name: (optional) Name of the resource record.
        :param ResourceRecordInputRdata rdata: (optional) Content of the resource
               record.
        :param int ttl: (optional) Time to live in second.
        :param str service: (optional) Only used for SRV record.
        :param str protocol: (optional) Only used for SRV record.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceRecord` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if dnszone_id is None:
            raise ValueError('dnszone_id must be provided')
        if rdata is not None:
            rdata = convert_model(rdata)
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_resource_record')
        headers.update(sdk_headers)

        data = {
            'type': type,
            'name': name,
            'rdata': rdata,
            'ttl': ttl,
            'service': service,
            'protocol': protocol
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/instances/{0}/dnszones/{1}/resource_records'.format(
            *self.encode_path_vars(instance_id, dnszone_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_resource_record(self,
        instance_id: str,
        dnszone_id: str,
        record_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a resource record.

        Delete a resource record.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str record_id: The unique identifier of a resource record.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if dnszone_id is None:
            raise ValueError('dnszone_id must be provided')
        if record_id is None:
            raise ValueError('record_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_resource_record')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/instances/{0}/dnszones/{1}/resource_records/{2}'.format(
            *self.encode_path_vars(instance_id, dnszone_id, record_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_resource_record(self,
        instance_id: str,
        dnszone_id: str,
        record_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a resource record.

        Get details of a resource record.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str record_id: The unique identifier of a resource record.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceRecord` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if dnszone_id is None:
            raise ValueError('dnszone_id must be provided')
        if record_id is None:
            raise ValueError('record_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_resource_record')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/instances/{0}/dnszones/{1}/resource_records/{2}'.format(
            *self.encode_path_vars(instance_id, dnszone_id, record_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_resource_record(self,
        instance_id: str,
        dnszone_id: str,
        record_id: str,
        *,
        name: str = None,
        rdata: 'ResourceRecordUpdateInputRdata' = None,
        ttl: int = None,
        service: str = None,
        protocol: str = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update the properties of a resource record.

        Update the properties of a resource record.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str record_id: The unique identifier of a resource record.
        :param str name: (optional) Name of the resource record.
        :param ResourceRecordUpdateInputRdata rdata: (optional) Content of the
               resource record.
        :param int ttl: (optional) Time to live in second.
        :param str service: (optional) Only used for SRV record.
        :param str protocol: (optional) Only used for SRV record.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceRecord` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if dnszone_id is None:
            raise ValueError('dnszone_id must be provided')
        if record_id is None:
            raise ValueError('record_id must be provided')
        if rdata is not None:
            rdata = convert_model(rdata)
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_resource_record')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'rdata': rdata,
            'ttl': ttl,
            'service': service,
            'protocol': protocol
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/instances/{0}/dnszones/{1}/resource_records/{2}'.format(
            *self.encode_path_vars(instance_id, dnszone_id, record_id))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class ResourceRecordInputRdata():
    """
    Content of the resource record.

    """

    def __init__(self) -> None:
        """
        Initialize a ResourceRecordInputRdata object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
                  ", ".join(['ResourceRecordInputRdataRdataARecord', 'ResourceRecordInputRdataRdataAaaaRecord', 'ResourceRecordInputRdataRdataCnameRecord', 'ResourceRecordInputRdataRdataMxRecord', 'ResourceRecordInputRdataRdataSrvRecord', 'ResourceRecordInputRdataRdataTxtRecord', 'ResourceRecordInputRdataRdataPtrRecord']))
        raise Exception(msg)

class ResourceRecordUpdateInputRdata():
    """
    Content of the resource record.

    """

    def __init__(self) -> None:
        """
        Initialize a ResourceRecordUpdateInputRdata object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
                  ", ".join(['ResourceRecordUpdateInputRdataRdataARecord', 'ResourceRecordUpdateInputRdataRdataAaaaRecord', 'ResourceRecordUpdateInputRdataRdataCnameRecord', 'ResourceRecordUpdateInputRdataRdataMxRecord', 'ResourceRecordUpdateInputRdataRdataSrvRecord', 'ResourceRecordUpdateInputRdataRdataTxtRecord', 'ResourceRecordUpdateInputRdataRdataPtrRecord']))
        raise Exception(msg)

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

class ListResourceRecords():
    """
    List Resource Records response.

    :attr List[ResourceRecord] resource_records: An array of resource records.
    :attr int offset: Specify how many resource records to skip over, the default
          value is 0.
    :attr int limit: Specify how many resource records are returned, the default
          value is 20.
    :attr int total_count: Total number of resource records.
    :attr FirstHref first: href.
    :attr NextHref next: (optional) href.
    """

    def __init__(self,
                 resource_records: List['ResourceRecord'],
                 offset: int,
                 limit: int,
                 total_count: int,
                 first: 'FirstHref',
                 *,
                 next: 'NextHref' = None) -> None:
        """
        Initialize a ListResourceRecords object.

        :param List[ResourceRecord] resource_records: An array of resource records.
        :param int offset: Specify how many resource records to skip over, the
               default value is 0.
        :param int limit: Specify how many resource records are returned, the
               default value is 20.
        :param int total_count: Total number of resource records.
        :param FirstHref first: href.
        :param NextHref next: (optional) href.
        """
        self.resource_records = resource_records
        self.offset = offset
        self.limit = limit
        self.total_count = total_count
        self.first = first
        self.next = next

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListResourceRecords':
        """Initialize a ListResourceRecords object from a json dictionary."""
        args = {}
        if 'resource_records' in _dict:
            args['resource_records'] = [ResourceRecord.from_dict(x) for x in _dict.get('resource_records')]
        else:
            raise ValueError('Required property \'resource_records\' not present in ListResourceRecords JSON')
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        else:
            raise ValueError('Required property \'offset\' not present in ListResourceRecords JSON')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in ListResourceRecords JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in ListResourceRecords JSON')
        if 'first' in _dict:
            args['first'] = FirstHref.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in ListResourceRecords JSON')
        if 'next' in _dict:
            args['next'] = NextHref.from_dict(_dict.get('next'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListResourceRecords object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'resource_records') and self.resource_records is not None:
            _dict['resource_records'] = [x.to_dict() for x in self.resource_records]
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
        """Return a `str` version of this ListResourceRecords object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListResourceRecords') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListResourceRecords') -> bool:
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

class ResourceRecord():
    """
    Resource record details.

    :attr str id: (optional) Identifier of the resource record.
    :attr str created_on: (optional) the time when a resource record is created.
    :attr str modified_on: (optional) the recent time when a resource record is
          modified.
    :attr str name: (optional) Name of the resource record.
    :attr str type: (optional) Type of the resource record.
    :attr int ttl: (optional) Time to live in second.
    :attr object rdata: (optional) Content of the resource record.
    :attr str service: (optional) Only used for SRV record.
    :attr str protocol: (optional) Only used for SRV record.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 created_on: str = None,
                 modified_on: str = None,
                 name: str = None,
                 type: str = None,
                 ttl: int = None,
                 rdata: object = None,
                 service: str = None,
                 protocol: str = None) -> None:
        """
        Initialize a ResourceRecord object.

        :param str id: (optional) Identifier of the resource record.
        :param str created_on: (optional) the time when a resource record is
               created.
        :param str modified_on: (optional) the recent time when a resource record
               is modified.
        :param str name: (optional) Name of the resource record.
        :param str type: (optional) Type of the resource record.
        :param int ttl: (optional) Time to live in second.
        :param object rdata: (optional) Content of the resource record.
        :param str service: (optional) Only used for SRV record.
        :param str protocol: (optional) Only used for SRV record.
        """
        self.id = id
        self.created_on = created_on
        self.modified_on = modified_on
        self.name = name
        self.type = type
        self.ttl = ttl
        self.rdata = rdata
        self.service = service
        self.protocol = protocol

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceRecord':
        """Initialize a ResourceRecord object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'created_on' in _dict:
            args['created_on'] = _dict.get('created_on')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'ttl' in _dict:
            args['ttl'] = _dict.get('ttl')
        if 'rdata' in _dict:
            args['rdata'] = _dict.get('rdata')
        if 'service' in _dict:
            args['service'] = _dict.get('service')
        if 'protocol' in _dict:
            args['protocol'] = _dict.get('protocol')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceRecord object from a json dictionary."""
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
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'ttl') and self.ttl is not None:
            _dict['ttl'] = self.ttl
        if hasattr(self, 'rdata') and self.rdata is not None:
            _dict['rdata'] = self.rdata
        if hasattr(self, 'service') and self.service is not None:
            _dict['service'] = self.service
        if hasattr(self, 'protocol') and self.protocol is not None:
            _dict['protocol'] = self.protocol
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceRecord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceRecord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceRecord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Type of the resource record.
        """
        A = 'A'
        AAAA = 'AAAA'
        CNAME = 'CNAME'
        MX = 'MX'
        SRV = 'SRV'
        TXT = 'TXT'
        PTR = 'PTR'


class ResourceRecordInputRdataRdataARecord(ResourceRecordInputRdata):
    """
    The content of type-A resource record.

    :attr str ip: IPv4 address.
    """

    def __init__(self,
                 ip: str) -> None:
        """
        Initialize a ResourceRecordInputRdataRdataARecord object.

        :param str ip: IPv4 address.
        """
        # pylint: disable=super-init-not-called
        self.ip = ip

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceRecordInputRdataRdataARecord':
        """Initialize a ResourceRecordInputRdataRdataARecord object from a json dictionary."""
        args = {}
        if 'ip' in _dict:
            args['ip'] = _dict.get('ip')
        else:
            raise ValueError('Required property \'ip\' not present in ResourceRecordInputRdataRdataARecord JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceRecordInputRdataRdataARecord object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'ip') and self.ip is not None:
            _dict['ip'] = self.ip
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceRecordInputRdataRdataARecord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceRecordInputRdataRdataARecord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceRecordInputRdataRdataARecord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceRecordInputRdataRdataAaaaRecord(ResourceRecordInputRdata):
    """
    The content of type-AAAA resource record.

    :attr str ip: IPv6 address.
    """

    def __init__(self,
                 ip: str) -> None:
        """
        Initialize a ResourceRecordInputRdataRdataAaaaRecord object.

        :param str ip: IPv6 address.
        """
        # pylint: disable=super-init-not-called
        self.ip = ip

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceRecordInputRdataRdataAaaaRecord':
        """Initialize a ResourceRecordInputRdataRdataAaaaRecord object from a json dictionary."""
        args = {}
        if 'ip' in _dict:
            args['ip'] = _dict.get('ip')
        else:
            raise ValueError('Required property \'ip\' not present in ResourceRecordInputRdataRdataAaaaRecord JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceRecordInputRdataRdataAaaaRecord object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'ip') and self.ip is not None:
            _dict['ip'] = self.ip
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceRecordInputRdataRdataAaaaRecord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceRecordInputRdataRdataAaaaRecord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceRecordInputRdataRdataAaaaRecord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceRecordInputRdataRdataCnameRecord(ResourceRecordInputRdata):
    """
    The content of type-CNAME resource record.

    :attr str cname: Canonical name.
    """

    def __init__(self,
                 cname: str) -> None:
        """
        Initialize a ResourceRecordInputRdataRdataCnameRecord object.

        :param str cname: Canonical name.
        """
        # pylint: disable=super-init-not-called
        self.cname = cname

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceRecordInputRdataRdataCnameRecord':
        """Initialize a ResourceRecordInputRdataRdataCnameRecord object from a json dictionary."""
        args = {}
        if 'cname' in _dict:
            args['cname'] = _dict.get('cname')
        else:
            raise ValueError('Required property \'cname\' not present in ResourceRecordInputRdataRdataCnameRecord JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceRecordInputRdataRdataCnameRecord object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cname') and self.cname is not None:
            _dict['cname'] = self.cname
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceRecordInputRdataRdataCnameRecord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceRecordInputRdataRdataCnameRecord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceRecordInputRdataRdataCnameRecord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceRecordInputRdataRdataMxRecord(ResourceRecordInputRdata):
    """
    The content of type-MX resource record.

    :attr str exchange: Hostname of Exchange server.
    :attr int preference: Preference of the MX record.
    """

    def __init__(self,
                 exchange: str,
                 preference: int) -> None:
        """
        Initialize a ResourceRecordInputRdataRdataMxRecord object.

        :param str exchange: Hostname of Exchange server.
        :param int preference: Preference of the MX record.
        """
        # pylint: disable=super-init-not-called
        self.exchange = exchange
        self.preference = preference

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceRecordInputRdataRdataMxRecord':
        """Initialize a ResourceRecordInputRdataRdataMxRecord object from a json dictionary."""
        args = {}
        if 'exchange' in _dict:
            args['exchange'] = _dict.get('exchange')
        else:
            raise ValueError('Required property \'exchange\' not present in ResourceRecordInputRdataRdataMxRecord JSON')
        if 'preference' in _dict:
            args['preference'] = _dict.get('preference')
        else:
            raise ValueError('Required property \'preference\' not present in ResourceRecordInputRdataRdataMxRecord JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceRecordInputRdataRdataMxRecord object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'exchange') and self.exchange is not None:
            _dict['exchange'] = self.exchange
        if hasattr(self, 'preference') and self.preference is not None:
            _dict['preference'] = self.preference
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceRecordInputRdataRdataMxRecord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceRecordInputRdataRdataMxRecord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceRecordInputRdataRdataMxRecord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceRecordInputRdataRdataPtrRecord(ResourceRecordInputRdata):
    """
    The content of type-PTR resource record.

    :attr str ptrdname: Hostname of the relevant A or AAAA record.
    """

    def __init__(self,
                 ptrdname: str) -> None:
        """
        Initialize a ResourceRecordInputRdataRdataPtrRecord object.

        :param str ptrdname: Hostname of the relevant A or AAAA record.
        """
        # pylint: disable=super-init-not-called
        self.ptrdname = ptrdname

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceRecordInputRdataRdataPtrRecord':
        """Initialize a ResourceRecordInputRdataRdataPtrRecord object from a json dictionary."""
        args = {}
        if 'ptrdname' in _dict:
            args['ptrdname'] = _dict.get('ptrdname')
        else:
            raise ValueError('Required property \'ptrdname\' not present in ResourceRecordInputRdataRdataPtrRecord JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceRecordInputRdataRdataPtrRecord object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'ptrdname') and self.ptrdname is not None:
            _dict['ptrdname'] = self.ptrdname
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceRecordInputRdataRdataPtrRecord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceRecordInputRdataRdataPtrRecord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceRecordInputRdataRdataPtrRecord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceRecordInputRdataRdataSrvRecord(ResourceRecordInputRdata):
    """
    The content of type-SRV resource record.

    :attr int port: Port number of the target server.
    :attr int priority: Priority of the SRV record.
    :attr str target: Hostname of the target server.
    :attr int weight: Weight of distributing queries among multiple target servers.
    """

    def __init__(self,
                 port: int,
                 priority: int,
                 target: str,
                 weight: int) -> None:
        """
        Initialize a ResourceRecordInputRdataRdataSrvRecord object.

        :param int port: Port number of the target server.
        :param int priority: Priority of the SRV record.
        :param str target: Hostname of the target server.
        :param int weight: Weight of distributing queries among multiple target
               servers.
        """
        # pylint: disable=super-init-not-called
        self.port = port
        self.priority = priority
        self.target = target
        self.weight = weight

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceRecordInputRdataRdataSrvRecord':
        """Initialize a ResourceRecordInputRdataRdataSrvRecord object from a json dictionary."""
        args = {}
        if 'port' in _dict:
            args['port'] = _dict.get('port')
        else:
            raise ValueError('Required property \'port\' not present in ResourceRecordInputRdataRdataSrvRecord JSON')
        if 'priority' in _dict:
            args['priority'] = _dict.get('priority')
        else:
            raise ValueError('Required property \'priority\' not present in ResourceRecordInputRdataRdataSrvRecord JSON')
        if 'target' in _dict:
            args['target'] = _dict.get('target')
        else:
            raise ValueError('Required property \'target\' not present in ResourceRecordInputRdataRdataSrvRecord JSON')
        if 'weight' in _dict:
            args['weight'] = _dict.get('weight')
        else:
            raise ValueError('Required property \'weight\' not present in ResourceRecordInputRdataRdataSrvRecord JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceRecordInputRdataRdataSrvRecord object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'port') and self.port is not None:
            _dict['port'] = self.port
        if hasattr(self, 'priority') and self.priority is not None:
            _dict['priority'] = self.priority
        if hasattr(self, 'target') and self.target is not None:
            _dict['target'] = self.target
        if hasattr(self, 'weight') and self.weight is not None:
            _dict['weight'] = self.weight
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceRecordInputRdataRdataSrvRecord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceRecordInputRdataRdataSrvRecord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceRecordInputRdataRdataSrvRecord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceRecordInputRdataRdataTxtRecord(ResourceRecordInputRdata):
    """
    The content of type-TXT resource record.

    :attr str text: Human readable text.
    """

    def __init__(self,
                 text: str) -> None:
        """
        Initialize a ResourceRecordInputRdataRdataTxtRecord object.

        :param str text: Human readable text.
        """
        # pylint: disable=super-init-not-called
        self.text = text

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceRecordInputRdataRdataTxtRecord':
        """Initialize a ResourceRecordInputRdataRdataTxtRecord object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError('Required property \'text\' not present in ResourceRecordInputRdataRdataTxtRecord JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceRecordInputRdataRdataTxtRecord object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceRecordInputRdataRdataTxtRecord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceRecordInputRdataRdataTxtRecord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceRecordInputRdataRdataTxtRecord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceRecordUpdateInputRdataRdataARecord(ResourceRecordUpdateInputRdata):
    """
    The content of type-A resource record.

    :attr str ip: IPv4 address.
    """

    def __init__(self,
                 ip: str) -> None:
        """
        Initialize a ResourceRecordUpdateInputRdataRdataARecord object.

        :param str ip: IPv4 address.
        """
        # pylint: disable=super-init-not-called
        self.ip = ip

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceRecordUpdateInputRdataRdataARecord':
        """Initialize a ResourceRecordUpdateInputRdataRdataARecord object from a json dictionary."""
        args = {}
        if 'ip' in _dict:
            args['ip'] = _dict.get('ip')
        else:
            raise ValueError('Required property \'ip\' not present in ResourceRecordUpdateInputRdataRdataARecord JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceRecordUpdateInputRdataRdataARecord object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'ip') and self.ip is not None:
            _dict['ip'] = self.ip
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceRecordUpdateInputRdataRdataARecord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceRecordUpdateInputRdataRdataARecord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceRecordUpdateInputRdataRdataARecord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceRecordUpdateInputRdataRdataAaaaRecord(ResourceRecordUpdateInputRdata):
    """
    The content of type-AAAA resource record.

    :attr str ip: IPv6 address.
    """

    def __init__(self,
                 ip: str) -> None:
        """
        Initialize a ResourceRecordUpdateInputRdataRdataAaaaRecord object.

        :param str ip: IPv6 address.
        """
        # pylint: disable=super-init-not-called
        self.ip = ip

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceRecordUpdateInputRdataRdataAaaaRecord':
        """Initialize a ResourceRecordUpdateInputRdataRdataAaaaRecord object from a json dictionary."""
        args = {}
        if 'ip' in _dict:
            args['ip'] = _dict.get('ip')
        else:
            raise ValueError('Required property \'ip\' not present in ResourceRecordUpdateInputRdataRdataAaaaRecord JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceRecordUpdateInputRdataRdataAaaaRecord object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'ip') and self.ip is not None:
            _dict['ip'] = self.ip
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceRecordUpdateInputRdataRdataAaaaRecord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceRecordUpdateInputRdataRdataAaaaRecord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceRecordUpdateInputRdataRdataAaaaRecord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceRecordUpdateInputRdataRdataCnameRecord(ResourceRecordUpdateInputRdata):
    """
    The content of type-CNAME resource record.

    :attr str cname: Canonical name.
    """

    def __init__(self,
                 cname: str) -> None:
        """
        Initialize a ResourceRecordUpdateInputRdataRdataCnameRecord object.

        :param str cname: Canonical name.
        """
        # pylint: disable=super-init-not-called
        self.cname = cname

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceRecordUpdateInputRdataRdataCnameRecord':
        """Initialize a ResourceRecordUpdateInputRdataRdataCnameRecord object from a json dictionary."""
        args = {}
        if 'cname' in _dict:
            args['cname'] = _dict.get('cname')
        else:
            raise ValueError('Required property \'cname\' not present in ResourceRecordUpdateInputRdataRdataCnameRecord JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceRecordUpdateInputRdataRdataCnameRecord object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cname') and self.cname is not None:
            _dict['cname'] = self.cname
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceRecordUpdateInputRdataRdataCnameRecord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceRecordUpdateInputRdataRdataCnameRecord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceRecordUpdateInputRdataRdataCnameRecord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceRecordUpdateInputRdataRdataMxRecord(ResourceRecordUpdateInputRdata):
    """
    The content of type-MX resource record.

    :attr str exchange: Hostname of Exchange server.
    :attr int preference: Preference of the MX record.
    """

    def __init__(self,
                 exchange: str,
                 preference: int) -> None:
        """
        Initialize a ResourceRecordUpdateInputRdataRdataMxRecord object.

        :param str exchange: Hostname of Exchange server.
        :param int preference: Preference of the MX record.
        """
        # pylint: disable=super-init-not-called
        self.exchange = exchange
        self.preference = preference

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceRecordUpdateInputRdataRdataMxRecord':
        """Initialize a ResourceRecordUpdateInputRdataRdataMxRecord object from a json dictionary."""
        args = {}
        if 'exchange' in _dict:
            args['exchange'] = _dict.get('exchange')
        else:
            raise ValueError('Required property \'exchange\' not present in ResourceRecordUpdateInputRdataRdataMxRecord JSON')
        if 'preference' in _dict:
            args['preference'] = _dict.get('preference')
        else:
            raise ValueError('Required property \'preference\' not present in ResourceRecordUpdateInputRdataRdataMxRecord JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceRecordUpdateInputRdataRdataMxRecord object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'exchange') and self.exchange is not None:
            _dict['exchange'] = self.exchange
        if hasattr(self, 'preference') and self.preference is not None:
            _dict['preference'] = self.preference
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceRecordUpdateInputRdataRdataMxRecord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceRecordUpdateInputRdataRdataMxRecord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceRecordUpdateInputRdataRdataMxRecord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceRecordUpdateInputRdataRdataPtrRecord(ResourceRecordUpdateInputRdata):
    """
    The content of type-PTR resource record.

    :attr str ptrdname: Hostname of the relevant A or AAAA record.
    """

    def __init__(self,
                 ptrdname: str) -> None:
        """
        Initialize a ResourceRecordUpdateInputRdataRdataPtrRecord object.

        :param str ptrdname: Hostname of the relevant A or AAAA record.
        """
        # pylint: disable=super-init-not-called
        self.ptrdname = ptrdname

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceRecordUpdateInputRdataRdataPtrRecord':
        """Initialize a ResourceRecordUpdateInputRdataRdataPtrRecord object from a json dictionary."""
        args = {}
        if 'ptrdname' in _dict:
            args['ptrdname'] = _dict.get('ptrdname')
        else:
            raise ValueError('Required property \'ptrdname\' not present in ResourceRecordUpdateInputRdataRdataPtrRecord JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceRecordUpdateInputRdataRdataPtrRecord object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'ptrdname') and self.ptrdname is not None:
            _dict['ptrdname'] = self.ptrdname
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceRecordUpdateInputRdataRdataPtrRecord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceRecordUpdateInputRdataRdataPtrRecord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceRecordUpdateInputRdataRdataPtrRecord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceRecordUpdateInputRdataRdataSrvRecord(ResourceRecordUpdateInputRdata):
    """
    The content of type-SRV resource record.

    :attr int port: Port number of the target server.
    :attr int priority: Priority of the SRV record.
    :attr str target: Hostname of the target server.
    :attr int weight: Weight of distributing queries among multiple target servers.
    """

    def __init__(self,
                 port: int,
                 priority: int,
                 target: str,
                 weight: int) -> None:
        """
        Initialize a ResourceRecordUpdateInputRdataRdataSrvRecord object.

        :param int port: Port number of the target server.
        :param int priority: Priority of the SRV record.
        :param str target: Hostname of the target server.
        :param int weight: Weight of distributing queries among multiple target
               servers.
        """
        # pylint: disable=super-init-not-called
        self.port = port
        self.priority = priority
        self.target = target
        self.weight = weight

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceRecordUpdateInputRdataRdataSrvRecord':
        """Initialize a ResourceRecordUpdateInputRdataRdataSrvRecord object from a json dictionary."""
        args = {}
        if 'port' in _dict:
            args['port'] = _dict.get('port')
        else:
            raise ValueError('Required property \'port\' not present in ResourceRecordUpdateInputRdataRdataSrvRecord JSON')
        if 'priority' in _dict:
            args['priority'] = _dict.get('priority')
        else:
            raise ValueError('Required property \'priority\' not present in ResourceRecordUpdateInputRdataRdataSrvRecord JSON')
        if 'target' in _dict:
            args['target'] = _dict.get('target')
        else:
            raise ValueError('Required property \'target\' not present in ResourceRecordUpdateInputRdataRdataSrvRecord JSON')
        if 'weight' in _dict:
            args['weight'] = _dict.get('weight')
        else:
            raise ValueError('Required property \'weight\' not present in ResourceRecordUpdateInputRdataRdataSrvRecord JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceRecordUpdateInputRdataRdataSrvRecord object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'port') and self.port is not None:
            _dict['port'] = self.port
        if hasattr(self, 'priority') and self.priority is not None:
            _dict['priority'] = self.priority
        if hasattr(self, 'target') and self.target is not None:
            _dict['target'] = self.target
        if hasattr(self, 'weight') and self.weight is not None:
            _dict['weight'] = self.weight
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceRecordUpdateInputRdataRdataSrvRecord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceRecordUpdateInputRdataRdataSrvRecord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceRecordUpdateInputRdataRdataSrvRecord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceRecordUpdateInputRdataRdataTxtRecord(ResourceRecordUpdateInputRdata):
    """
    The content of type-TXT resource record.

    :attr str text: Human readable text.
    """

    def __init__(self,
                 text: str) -> None:
        """
        Initialize a ResourceRecordUpdateInputRdataRdataTxtRecord object.

        :param str text: Human readable text.
        """
        # pylint: disable=super-init-not-called
        self.text = text

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceRecordUpdateInputRdataRdataTxtRecord':
        """Initialize a ResourceRecordUpdateInputRdataRdataTxtRecord object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError('Required property \'text\' not present in ResourceRecordUpdateInputRdataRdataTxtRecord JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceRecordUpdateInputRdataRdataTxtRecord object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceRecordUpdateInputRdataRdataTxtRecord object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceRecordUpdateInputRdataRdataTxtRecord') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceRecordUpdateInputRdataRdataTxtRecord') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
