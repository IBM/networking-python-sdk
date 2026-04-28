# coding: utf-8

# (C) Copyright IBM Corp. 2026.
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

# IBM OpenAPI SDK Code Generator Version: 3.114.0-a902401e-20260427-192904

"""
DNS records

API Version: 1.0.1
"""

from enum import Enum
from typing import Dict, List, Optional
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################


class DnsRecordsV1(BaseService):
    """The DNS Records V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'dns_records'

    @classmethod
    def new_instance(
        cls,
        crn: str,
        zone_identifier: str,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'DnsRecordsV1':
        """
        Return a new client for the DNS Records service using the specified
               parameters and external configuration.

        :param str crn: Full crn of the service instance.

        :param str zone_identifier: Zone identifier (zone id).
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

    def __init__(
        self,
        crn: str,
        zone_identifier: str,
        authenticator: Authenticator = None,
    ) -> None:
        """
        Construct a new client for the DNS Records service.

        :param str crn: Full crn of the service instance.

        :param str zone_identifier: Zone identifier (zone id).

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        if crn is None:
            raise ValueError('crn must be provided')
        if zone_identifier is None:
            raise ValueError('zone_identifier must be provided')

        BaseService.__init__(self, service_url=self.DEFAULT_SERVICE_URL, authenticator=authenticator)
        self.crn = crn
        self.zone_identifier = zone_identifier

    #########################
    # DNS Records
    #########################

    def list_all_dns_records(
        self,
        *,
        type: Optional[str] = None,
        name: Optional[str] = None,
        content: Optional[str] = None,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
        order: Optional[str] = None,
        direction: Optional[str] = None,
        match: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List all DNS records.

        List all DNS records for a given zone of a service instance.

        :param str type: (optional) Type of DNS records to display.
        :param str name: (optional) Value of name field to filter by.
        :param str content: (optional) Value of content field to filter by.
        :param int page: (optional) Page number of paginated results.
        :param int per_page: (optional) Maximum number of DNS records per page.
        :param str order: (optional) Field by which to order list of DNS records.
        :param str direction: (optional) Direction in which to order results
               [ascending/descending order].
        :param str match: (optional) Whether to match all (all) or atleast one
               search parameter (any).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListDnsrecordsResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_all_dns_records',
        )
        headers.update(sdk_headers)

        params = {
            'type': type,
            'name': name,
            'content': content,
            'page': page,
            'per_page': per_page,
            'order': order,
            'direction': direction,
            'match': match,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/dns_records'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_dns_record(
        self,
        *,
        type: Optional[str] = None,
        name: Optional[str] = None,
        ttl: Optional[int] = None,
        content: Optional[str] = None,
        priority: Optional[int] = None,
        proxied: Optional[bool] = None,
        data: Optional[dict] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create DNS record.

        Add a new DNS record for a given zone for a given service instance.

        :param str type: (optional) dns record type.
        :param str name: (optional) Required for all record types except SRV.
        :param int ttl: (optional) dns record ttl value.
        :param str content: (optional) dns record content.
        :param int priority: (optional) For MX records only.
        :param bool proxied: (optional) proxied.
        :param dict data: (optional) For LOC, SRV, CAA, DS records only.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DnsrecordResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_dns_record',
        )
        headers.update(sdk_headers)

        data = {
            'type': type,
            'name': name,
            'ttl': ttl,
            'content': content,
            'priority': priority,
            'proxied': proxied,
            'data': data,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/dns_records'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_dns_record(
        self,
        dnsrecord_identifier: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete DNS record.

        Delete a DNS record given its id.

        :param str dnsrecord_identifier: Identifier of DNS record.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteDnsrecordResp` object
        """

        if not dnsrecord_identifier:
            raise ValueError('dnsrecord_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_dns_record',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'dnsrecord_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier, dnsrecord_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/dns_records/{dnsrecord_identifier}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_dns_record(
        self,
        dnsrecord_identifier: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get DNS record.

        Get the details of a DNS record for a given zone under a given service instance.

        :param str dnsrecord_identifier: Identifier of DNS record.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DnsrecordResp` object
        """

        if not dnsrecord_identifier:
            raise ValueError('dnsrecord_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_dns_record',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'dnsrecord_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier, dnsrecord_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/dns_records/{dnsrecord_identifier}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_dns_record(
        self,
        dnsrecord_identifier: str,
        *,
        type: Optional[str] = None,
        name: Optional[str] = None,
        ttl: Optional[int] = None,
        content: Optional[str] = None,
        priority: Optional[int] = None,
        proxied: Optional[bool] = None,
        data: Optional[dict] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update DNS record.

        Update an existing DNS record for a given zone under a given service instance.

        :param str dnsrecord_identifier: Identifier of DNS record.
        :param str type: (optional) dns record type.
        :param str name: (optional) Required for all record types except SRV.
        :param int ttl: (optional) dns record ttl value.
        :param str content: (optional) content of dns record.
        :param int priority: (optional) For MX records only.
        :param bool proxied: (optional) proxied.
        :param dict data: (optional) For LOC, SRV, CAA, DS records only.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DnsrecordResp` object
        """

        if not dnsrecord_identifier:
            raise ValueError('dnsrecord_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_dns_record',
        )
        headers.update(sdk_headers)

        data = {
            'type': type,
            'name': name,
            'ttl': ttl,
            'content': content,
            'priority': priority,
            'proxied': proxied,
            'data': data,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier', 'dnsrecord_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier, dnsrecord_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/dns_records/{dnsrecord_identifier}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def batch_dns_records(
        self,
        *,
        deletes: Optional[List['BatchDnsRecordsRequestDeletesItem']] = None,
        patches: Optional[List['BatchDnsRecordsRequestPatchesItem']] = None,
        posts: Optional[List['DnsrecordInput']] = None,
        puts: Optional[List['BatchDnsRecordsRequestPutsItem']] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Batch DNS records.

        Send a Batch of DNS Record API calls to be executed together. The operations you
        specify within the /batch request body are always executed in the following order:
        deletes, patches, puts, posts.

        :param List[BatchDnsRecordsRequestDeletesItem] deletes: (optional)
        :param List[BatchDnsRecordsRequestPatchesItem] patches: (optional)
        :param List[DnsrecordInput] posts: (optional)
        :param List[BatchDnsRecordsRequestPutsItem] puts: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BatchDnsRecordsResponse` object
        """

        if deletes is not None:
            deletes = [convert_model(x) for x in deletes]
        if patches is not None:
            patches = [convert_model(x) for x in patches]
        if posts is not None:
            posts = [convert_model(x) for x in posts]
        if puts is not None:
            puts = [convert_model(x) for x in puts]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='batch_dns_records',
        )
        headers.update(sdk_headers)

        data = {
            'deletes': deletes,
            'patches': patches,
            'posts': posts,
            'puts': puts,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'zone_identifier']
        path_param_values = self.encode_path_vars(self.crn, self.zone_identifier)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/zones/{zone_identifier}/dns_records/batch'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response


class ListAllDnsRecordsEnums:
    """
    Enums for list_all_dns_records parameters.
    """

    class Order(str, Enum):
        """
        Field by which to order list of DNS records.
        """

        TYPE = 'type'
        NAME = 'name'
        CONTENT = 'content'
        TTL = 'ttl'
        PROXIED = 'proxied'
    class Direction(str, Enum):
        """
        Direction in which to order results [ascending/descending order].
        """

        ASC = 'asc'
        DESC = 'desc'
    class Match(str, Enum):
        """
        Whether to match all (all) or atleast one search parameter (any).
        """

        ANY = 'any'
        ALL = 'all'


##############################################################################
# Models
##############################################################################


class BatchDnsRecordsRequestDeletesItem:
    """
    BatchDnsRecordsRequestDeletesItem.

    :param str id: DNS record ID to delete.
    """

    def __init__(
        self,
        id: str,
    ) -> None:
        """
        Initialize a BatchDnsRecordsRequestDeletesItem object.

        :param str id: DNS record ID to delete.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BatchDnsRecordsRequestDeletesItem':
        """Initialize a BatchDnsRecordsRequestDeletesItem object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in BatchDnsRecordsRequestDeletesItem JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BatchDnsRecordsRequestDeletesItem object from a json dictionary."""
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
        """Return a `str` version of this BatchDnsRecordsRequestDeletesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BatchDnsRecordsRequestDeletesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BatchDnsRecordsRequestDeletesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class BatchDnsRecordsRequestPatchesItem:
    """
    BatchDnsRecordsRequestPatchesItem.

    :param str id: DNS record ID to patch.
    :param str name: (optional) Required for all record types except SRV.
    :param str type: (optional) dns record type.
    :param int ttl: (optional) dns record ttl value.
    :param str content: (optional) content of dns record.
    :param int priority: (optional) For MX records only.
    :param bool proxied: (optional) proxied.
    :param dict data: (optional) For LOC, SRV, CAA, DS records only.
    """

    def __init__(
        self,
        id: str,
        *,
        name: Optional[str] = None,
        type: Optional[str] = None,
        ttl: Optional[int] = None,
        content: Optional[str] = None,
        priority: Optional[int] = None,
        proxied: Optional[bool] = None,
        data: Optional[dict] = None,
    ) -> None:
        """
        Initialize a BatchDnsRecordsRequestPatchesItem object.

        :param str id: DNS record ID to patch.
        :param str name: (optional) Required for all record types except SRV.
        :param str type: (optional) dns record type.
        :param int ttl: (optional) dns record ttl value.
        :param str content: (optional) content of dns record.
        :param int priority: (optional) For MX records only.
        :param bool proxied: (optional) proxied.
        :param dict data: (optional) For LOC, SRV, CAA, DS records only.
        """
        self.id = id
        self.name = name
        self.type = type
        self.ttl = ttl
        self.content = content
        self.priority = priority
        self.proxied = proxied
        self.data = data

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BatchDnsRecordsRequestPatchesItem':
        """Initialize a BatchDnsRecordsRequestPatchesItem object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in BatchDnsRecordsRequestPatchesItem JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (ttl := _dict.get('ttl')) is not None:
            args['ttl'] = ttl
        if (content := _dict.get('content')) is not None:
            args['content'] = content
        if (priority := _dict.get('priority')) is not None:
            args['priority'] = priority
        if (proxied := _dict.get('proxied')) is not None:
            args['proxied'] = proxied
        if (data := _dict.get('data')) is not None:
            args['data'] = data
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BatchDnsRecordsRequestPatchesItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'ttl') and self.ttl is not None:
            _dict['ttl'] = self.ttl
        if hasattr(self, 'content') and self.content is not None:
            _dict['content'] = self.content
        if hasattr(self, 'priority') and self.priority is not None:
            _dict['priority'] = self.priority
        if hasattr(self, 'proxied') and self.proxied is not None:
            _dict['proxied'] = self.proxied
        if hasattr(self, 'data') and self.data is not None:
            _dict['data'] = self.data
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BatchDnsRecordsRequestPatchesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BatchDnsRecordsRequestPatchesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BatchDnsRecordsRequestPatchesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        dns record type.
        """

        A = 'A'
        AAAA = 'AAAA'
        CNAME = 'CNAME'
        NS = 'NS'
        MX = 'MX'
        TXT = 'TXT'
        LOC = 'LOC'
        SRV = 'SRV'
        PTR = 'PTR'
        CAA = 'CAA'
        DS = 'DS'



class BatchDnsRecordsRequestPutsItem:
    """
    BatchDnsRecordsRequestPutsItem.

    :param str id: DNS record ID to update.
    :param str name: Required for all record types except SRV.
    :param str type: dns record type.
    :param int ttl: dns record ttl value.
    :param str content: dns record content.
    :param int priority: (optional) For MX records only.
    :param bool proxied: (optional) proxied.
    :param dict data: (optional) For LOC, SRV, CAA, DS records only.
    """

    def __init__(
        self,
        id: str,
        name: str,
        type: str,
        ttl: int,
        content: str,
        *,
        priority: Optional[int] = None,
        proxied: Optional[bool] = None,
        data: Optional[dict] = None,
    ) -> None:
        """
        Initialize a BatchDnsRecordsRequestPutsItem object.

        :param str id: DNS record ID to update.
        :param str name: Required for all record types except SRV.
        :param str type: dns record type.
        :param int ttl: dns record ttl value.
        :param str content: dns record content.
        :param int priority: (optional) For MX records only.
        :param bool proxied: (optional) proxied.
        :param dict data: (optional) For LOC, SRV, CAA, DS records only.
        """
        self.id = id
        self.name = name
        self.type = type
        self.ttl = ttl
        self.content = content
        self.priority = priority
        self.proxied = proxied
        self.data = data

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BatchDnsRecordsRequestPutsItem':
        """Initialize a BatchDnsRecordsRequestPutsItem object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in BatchDnsRecordsRequestPutsItem JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError('Required property \'name\' not present in BatchDnsRecordsRequestPutsItem JSON')
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in BatchDnsRecordsRequestPutsItem JSON')
        if (ttl := _dict.get('ttl')) is not None:
            args['ttl'] = ttl
        else:
            raise ValueError('Required property \'ttl\' not present in BatchDnsRecordsRequestPutsItem JSON')
        if (content := _dict.get('content')) is not None:
            args['content'] = content
        else:
            raise ValueError('Required property \'content\' not present in BatchDnsRecordsRequestPutsItem JSON')
        if (priority := _dict.get('priority')) is not None:
            args['priority'] = priority
        if (proxied := _dict.get('proxied')) is not None:
            args['proxied'] = proxied
        if (data := _dict.get('data')) is not None:
            args['data'] = data
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BatchDnsRecordsRequestPutsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'ttl') and self.ttl is not None:
            _dict['ttl'] = self.ttl
        if hasattr(self, 'content') and self.content is not None:
            _dict['content'] = self.content
        if hasattr(self, 'priority') and self.priority is not None:
            _dict['priority'] = self.priority
        if hasattr(self, 'proxied') and self.proxied is not None:
            _dict['proxied'] = self.proxied
        if hasattr(self, 'data') and self.data is not None:
            _dict['data'] = self.data
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BatchDnsRecordsRequestPutsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BatchDnsRecordsRequestPutsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BatchDnsRecordsRequestPutsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        dns record type.
        """

        A = 'A'
        AAAA = 'AAAA'
        CNAME = 'CNAME'
        NS = 'NS'
        MX = 'MX'
        TXT = 'TXT'
        LOC = 'LOC'
        SRV = 'SRV'
        PTR = 'PTR'
        CAA = 'CAA'
        DS = 'DS'



class BatchDnsRecordsResponseResult:
    """
    BatchDnsRecordsResponseResult.

    :param List[BatchDnsRecordDetails] deletes: (optional)
    :param List[BatchDnsRecordDetails] patches: (optional)
    :param List[BatchDnsRecordDetails] posts: (optional)
    :param List[BatchDnsRecordDetails] puts: (optional)
    """

    def __init__(
        self,
        *,
        deletes: Optional[List['BatchDnsRecordDetails']] = None,
        patches: Optional[List['BatchDnsRecordDetails']] = None,
        posts: Optional[List['BatchDnsRecordDetails']] = None,
        puts: Optional[List['BatchDnsRecordDetails']] = None,
    ) -> None:
        """
        Initialize a BatchDnsRecordsResponseResult object.

        :param List[BatchDnsRecordDetails] deletes: (optional)
        :param List[BatchDnsRecordDetails] patches: (optional)
        :param List[BatchDnsRecordDetails] posts: (optional)
        :param List[BatchDnsRecordDetails] puts: (optional)
        """
        self.deletes = deletes
        self.patches = patches
        self.posts = posts
        self.puts = puts

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BatchDnsRecordsResponseResult':
        """Initialize a BatchDnsRecordsResponseResult object from a json dictionary."""
        args = {}
        if (deletes := _dict.get('deletes')) is not None:
            args['deletes'] = [BatchDnsRecordDetails.from_dict(v) for v in deletes]
        if (patches := _dict.get('patches')) is not None:
            args['patches'] = [BatchDnsRecordDetails.from_dict(v) for v in patches]
        if (posts := _dict.get('posts')) is not None:
            args['posts'] = [BatchDnsRecordDetails.from_dict(v) for v in posts]
        if (puts := _dict.get('puts')) is not None:
            args['puts'] = [BatchDnsRecordDetails.from_dict(v) for v in puts]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BatchDnsRecordsResponseResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'deletes') and self.deletes is not None:
            deletes_list = []
            for v in self.deletes:
                if isinstance(v, dict):
                    deletes_list.append(v)
                else:
                    deletes_list.append(v.to_dict())
            _dict['deletes'] = deletes_list
        if hasattr(self, 'patches') and self.patches is not None:
            patches_list = []
            for v in self.patches:
                if isinstance(v, dict):
                    patches_list.append(v)
                else:
                    patches_list.append(v.to_dict())
            _dict['patches'] = patches_list
        if hasattr(self, 'posts') and self.posts is not None:
            posts_list = []
            for v in self.posts:
                if isinstance(v, dict):
                    posts_list.append(v)
                else:
                    posts_list.append(v.to_dict())
            _dict['posts'] = posts_list
        if hasattr(self, 'puts') and self.puts is not None:
            puts_list = []
            for v in self.puts:
                if isinstance(v, dict):
                    puts_list.append(v)
                else:
                    puts_list.append(v.to_dict())
            _dict['puts'] = puts_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BatchDnsRecordsResponseResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BatchDnsRecordsResponseResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BatchDnsRecordsResponseResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DeleteDnsrecordRespResult:
    """
    result.

    :param str id: dns record id.
    """

    def __init__(
        self,
        id: str,
    ) -> None:
        """
        Initialize a DeleteDnsrecordRespResult object.

        :param str id: dns record id.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteDnsrecordRespResult':
        """Initialize a DeleteDnsrecordRespResult object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError('Required property \'id\' not present in DeleteDnsrecordRespResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteDnsrecordRespResult object from a json dictionary."""
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
        """Return a `str` version of this DeleteDnsrecordRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteDnsrecordRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteDnsrecordRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class BatchDnsRecordDetails:
    """
    dns record details as returned by the batch API.

    :param str id: (optional) dns record identifier.
    :param str created_on: (optional) created on.
    :param str modified_on: (optional) modified date.
    :param str name: (optional) dns record name.
    :param str type: (optional) dns record type.
    :param str content: (optional) dns record content.
    :param bool proxiable: (optional) proxiable.
    :param bool proxied: (optional) proxied.
    :param int ttl: (optional) dns record ttl value.
    :param int priority: (optional) Relevant only to MX type records.
    :param dict data: (optional) Data details for the DNS record. Only for LOC, SRV,
          CAA records.
    :param dict settings: (optional) DNS record settings.
    :param dict meta: (optional) DNS record metadata.
    :param str comment: (optional) Optional comment for the DNS record.
    :param List[str] tags: (optional) Tags associated with the DNS record.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        created_on: Optional[str] = None,
        modified_on: Optional[str] = None,
        name: Optional[str] = None,
        type: Optional[str] = None,
        content: Optional[str] = None,
        proxiable: Optional[bool] = None,
        proxied: Optional[bool] = None,
        ttl: Optional[int] = None,
        priority: Optional[int] = None,
        data: Optional[dict] = None,
        settings: Optional[dict] = None,
        meta: Optional[dict] = None,
        comment: Optional[str] = None,
        tags: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize a BatchDnsRecordDetails object.

        :param str id: (optional) dns record identifier.
        :param str created_on: (optional) created on.
        :param str modified_on: (optional) modified date.
        :param str name: (optional) dns record name.
        :param str type: (optional) dns record type.
        :param str content: (optional) dns record content.
        :param bool proxiable: (optional) proxiable.
        :param bool proxied: (optional) proxied.
        :param int ttl: (optional) dns record ttl value.
        :param int priority: (optional) Relevant only to MX type records.
        :param dict data: (optional) Data details for the DNS record. Only for LOC,
               SRV, CAA records.
        :param dict settings: (optional) DNS record settings.
        :param dict meta: (optional) DNS record metadata.
        :param str comment: (optional) Optional comment for the DNS record.
        :param List[str] tags: (optional) Tags associated with the DNS record.
        """
        self.id = id
        self.created_on = created_on
        self.modified_on = modified_on
        self.name = name
        self.type = type
        self.content = content
        self.proxiable = proxiable
        self.proxied = proxied
        self.ttl = ttl
        self.priority = priority
        self.data = data
        self.settings = settings
        self.meta = meta
        self.comment = comment
        self.tags = tags

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BatchDnsRecordDetails':
        """Initialize a BatchDnsRecordDetails object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (created_on := _dict.get('created_on')) is not None:
            args['created_on'] = created_on
        if (modified_on := _dict.get('modified_on')) is not None:
            args['modified_on'] = modified_on
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (content := _dict.get('content')) is not None:
            args['content'] = content
        if (proxiable := _dict.get('proxiable')) is not None:
            args['proxiable'] = proxiable
        if (proxied := _dict.get('proxied')) is not None:
            args['proxied'] = proxied
        if (ttl := _dict.get('ttl')) is not None:
            args['ttl'] = ttl
        if (priority := _dict.get('priority')) is not None:
            args['priority'] = priority
        if (data := _dict.get('data')) is not None:
            args['data'] = data
        if (settings := _dict.get('settings')) is not None:
            args['settings'] = settings
        if (meta := _dict.get('meta')) is not None:
            args['meta'] = meta
        if (comment := _dict.get('comment')) is not None:
            args['comment'] = comment
        if (tags := _dict.get('tags')) is not None:
            args['tags'] = tags
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BatchDnsRecordDetails object from a json dictionary."""
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
        if hasattr(self, 'content') and self.content is not None:
            _dict['content'] = self.content
        if hasattr(self, 'proxiable') and self.proxiable is not None:
            _dict['proxiable'] = self.proxiable
        if hasattr(self, 'proxied') and self.proxied is not None:
            _dict['proxied'] = self.proxied
        if hasattr(self, 'ttl') and self.ttl is not None:
            _dict['ttl'] = self.ttl
        if hasattr(self, 'priority') and self.priority is not None:
            _dict['priority'] = self.priority
        if hasattr(self, 'data') and self.data is not None:
            _dict['data'] = self.data
        if hasattr(self, 'settings') and self.settings is not None:
            _dict['settings'] = self.settings
        if hasattr(self, 'meta') and self.meta is not None:
            _dict['meta'] = self.meta
        if hasattr(self, 'comment') and self.comment is not None:
            _dict['comment'] = self.comment
        if hasattr(self, 'tags') and self.tags is not None:
            _dict['tags'] = self.tags
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BatchDnsRecordDetails object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BatchDnsRecordDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BatchDnsRecordDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        dns record type.
        """

        A = 'A'
        AAAA = 'AAAA'
        CNAME = 'CNAME'
        NS = 'NS'
        MX = 'MX'
        TXT = 'TXT'
        LOC = 'LOC'
        SRV = 'SRV'
        PTR = 'PTR'
        CAA = 'CAA'
        DS = 'DS'



class BatchDnsRecordsResponse:
    """
    Batch DNS records response.

    :param bool success: success response.
    :param List[List[str]] errors: errors.
    :param List[List[str]] messages: messages.
    :param BatchDnsRecordsResponseResult result:
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        result: 'BatchDnsRecordsResponseResult',
    ) -> None:
        """
        Initialize a BatchDnsRecordsResponse object.

        :param bool success: success response.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param BatchDnsRecordsResponseResult result:
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BatchDnsRecordsResponse':
        """Initialize a BatchDnsRecordsResponse object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in BatchDnsRecordsResponse JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in BatchDnsRecordsResponse JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in BatchDnsRecordsResponse JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = BatchDnsRecordsResponseResult.from_dict(result)
        else:
            raise ValueError('Required property \'result\' not present in BatchDnsRecordsResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BatchDnsRecordsResponse object from a json dictionary."""
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
            if isinstance(self.result, dict):
                _dict['result'] = self.result
            else:
                _dict['result'] = self.result.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BatchDnsRecordsResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BatchDnsRecordsResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BatchDnsRecordsResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DeleteDnsrecordResp:
    """
    dns record delete response.

    :param bool success: success response.
    :param List[List[str]] errors: errors.
    :param List[List[str]] messages: messages.
    :param DeleteDnsrecordRespResult result: result.
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        result: 'DeleteDnsrecordRespResult',
    ) -> None:
        """
        Initialize a DeleteDnsrecordResp object.

        :param bool success: success response.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param DeleteDnsrecordRespResult result: result.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteDnsrecordResp':
        """Initialize a DeleteDnsrecordResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in DeleteDnsrecordResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in DeleteDnsrecordResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in DeleteDnsrecordResp JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = DeleteDnsrecordRespResult.from_dict(result)
        else:
            raise ValueError('Required property \'result\' not present in DeleteDnsrecordResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteDnsrecordResp object from a json dictionary."""
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
            if isinstance(self.result, dict):
                _dict['result'] = self.result
            else:
                _dict['result'] = self.result.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeleteDnsrecordResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteDnsrecordResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteDnsrecordResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DnsrecordDetails:
    """
    dns record details.

    :param str id: (optional) dns record identifier.
    :param str created_on: (optional) created on.
    :param str modified_on: (optional) modified date.
    :param str name: (optional) dns record name.
    :param str type: (optional) dns record type.
    :param str content: (optional) dns record content.
    :param str zone_id: (optional) zone identifier.
    :param str zone_name: (optional) zone name.
    :param bool proxiable: (optional) proxiable.
    :param bool proxied: (optional) proxied.
    :param int ttl: (optional) dns record ttl value.
    :param int priority: (optional) Relevant only to MX type records.
    :param dict data: (optional) Data details for the DNS record. Only for LOC, SRV,
          CAA records.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        created_on: Optional[str] = None,
        modified_on: Optional[str] = None,
        name: Optional[str] = None,
        type: Optional[str] = None,
        content: Optional[str] = None,
        zone_id: Optional[str] = None,
        zone_name: Optional[str] = None,
        proxiable: Optional[bool] = None,
        proxied: Optional[bool] = None,
        ttl: Optional[int] = None,
        priority: Optional[int] = None,
        data: Optional[dict] = None,
    ) -> None:
        """
        Initialize a DnsrecordDetails object.

        :param str id: (optional) dns record identifier.
        :param str created_on: (optional) created on.
        :param str modified_on: (optional) modified date.
        :param str name: (optional) dns record name.
        :param str type: (optional) dns record type.
        :param str content: (optional) dns record content.
        :param str zone_id: (optional) zone identifier.
        :param str zone_name: (optional) zone name.
        :param bool proxiable: (optional) proxiable.
        :param bool proxied: (optional) proxied.
        :param int ttl: (optional) dns record ttl value.
        :param int priority: (optional) Relevant only to MX type records.
        :param dict data: (optional) Data details for the DNS record. Only for LOC,
               SRV, CAA records.
        """
        self.id = id
        self.created_on = created_on
        self.modified_on = modified_on
        self.name = name
        self.type = type
        self.content = content
        self.zone_id = zone_id
        self.zone_name = zone_name
        self.proxiable = proxiable
        self.proxied = proxied
        self.ttl = ttl
        self.priority = priority
        self.data = data

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DnsrecordDetails':
        """Initialize a DnsrecordDetails object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (created_on := _dict.get('created_on')) is not None:
            args['created_on'] = created_on
        if (modified_on := _dict.get('modified_on')) is not None:
            args['modified_on'] = modified_on
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (content := _dict.get('content')) is not None:
            args['content'] = content
        if (zone_id := _dict.get('zone_id')) is not None:
            args['zone_id'] = zone_id
        if (zone_name := _dict.get('zone_name')) is not None:
            args['zone_name'] = zone_name
        if (proxiable := _dict.get('proxiable')) is not None:
            args['proxiable'] = proxiable
        if (proxied := _dict.get('proxied')) is not None:
            args['proxied'] = proxied
        if (ttl := _dict.get('ttl')) is not None:
            args['ttl'] = ttl
        if (priority := _dict.get('priority')) is not None:
            args['priority'] = priority
        if (data := _dict.get('data')) is not None:
            args['data'] = data
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DnsrecordDetails object from a json dictionary."""
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
        if hasattr(self, 'content') and self.content is not None:
            _dict['content'] = self.content
        if hasattr(self, 'zone_id') and self.zone_id is not None:
            _dict['zone_id'] = self.zone_id
        if hasattr(self, 'zone_name') and self.zone_name is not None:
            _dict['zone_name'] = self.zone_name
        if hasattr(self, 'proxiable') and self.proxiable is not None:
            _dict['proxiable'] = self.proxiable
        if hasattr(self, 'proxied') and self.proxied is not None:
            _dict['proxied'] = self.proxied
        if hasattr(self, 'ttl') and self.ttl is not None:
            _dict['ttl'] = self.ttl
        if hasattr(self, 'priority') and self.priority is not None:
            _dict['priority'] = self.priority
        if hasattr(self, 'data') and self.data is not None:
            _dict['data'] = self.data
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DnsrecordDetails object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DnsrecordDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DnsrecordDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        dns record type.
        """

        A = 'A'
        AAAA = 'AAAA'
        CNAME = 'CNAME'
        NS = 'NS'
        MX = 'MX'
        TXT = 'TXT'
        LOC = 'LOC'
        SRV = 'SRV'
        PTR = 'PTR'
        CAA = 'CAA'
        DS = 'DS'



class DnsrecordInput:
    """
    dns record input.

    :param str name: (optional) Required for all record types except SRV.
    :param str type: dns record type.
    :param int ttl: (optional) dns record ttl value.
    :param str content: (optional) dns record content.
    :param int priority: (optional) For MX records only.
    :param bool proxied: (optional) proxied.
    :param dict data: (optional) For LOC, SRV, CAA, DS records only.
    """

    def __init__(
        self,
        type: str,
        *,
        name: Optional[str] = None,
        ttl: Optional[int] = None,
        content: Optional[str] = None,
        priority: Optional[int] = None,
        proxied: Optional[bool] = None,
        data: Optional[dict] = None,
    ) -> None:
        """
        Initialize a DnsrecordInput object.

        :param str type: dns record type.
        :param str name: (optional) Required for all record types except SRV.
        :param int ttl: (optional) dns record ttl value.
        :param str content: (optional) dns record content.
        :param int priority: (optional) For MX records only.
        :param bool proxied: (optional) proxied.
        :param dict data: (optional) For LOC, SRV, CAA, DS records only.
        """
        self.name = name
        self.type = type
        self.ttl = ttl
        self.content = content
        self.priority = priority
        self.proxied = proxied
        self.data = data

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DnsrecordInput':
        """Initialize a DnsrecordInput object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError('Required property \'type\' not present in DnsrecordInput JSON')
        if (ttl := _dict.get('ttl')) is not None:
            args['ttl'] = ttl
        if (content := _dict.get('content')) is not None:
            args['content'] = content
        if (priority := _dict.get('priority')) is not None:
            args['priority'] = priority
        if (proxied := _dict.get('proxied')) is not None:
            args['proxied'] = proxied
        if (data := _dict.get('data')) is not None:
            args['data'] = data
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DnsrecordInput object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'ttl') and self.ttl is not None:
            _dict['ttl'] = self.ttl
        if hasattr(self, 'content') and self.content is not None:
            _dict['content'] = self.content
        if hasattr(self, 'priority') and self.priority is not None:
            _dict['priority'] = self.priority
        if hasattr(self, 'proxied') and self.proxied is not None:
            _dict['proxied'] = self.proxied
        if hasattr(self, 'data') and self.data is not None:
            _dict['data'] = self.data
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DnsrecordInput object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DnsrecordInput') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DnsrecordInput') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        dns record type.
        """

        A = 'A'
        AAAA = 'AAAA'
        CNAME = 'CNAME'
        NS = 'NS'
        MX = 'MX'
        TXT = 'TXT'
        LOC = 'LOC'
        SRV = 'SRV'
        PTR = 'PTR'
        CAA = 'CAA'
        DS = 'DS'



class DnsrecordResp:
    """
    dns record response.

    :param bool success: success response.
    :param List[List[str]] errors: errors.
    :param List[List[str]] messages: messages.
    :param DnsrecordDetails result: dns record details.
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        result: 'DnsrecordDetails',
    ) -> None:
        """
        Initialize a DnsrecordResp object.

        :param bool success: success response.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param DnsrecordDetails result: dns record details.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DnsrecordResp':
        """Initialize a DnsrecordResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in DnsrecordResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in DnsrecordResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in DnsrecordResp JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = DnsrecordDetails.from_dict(result)
        else:
            raise ValueError('Required property \'result\' not present in DnsrecordResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DnsrecordResp object from a json dictionary."""
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
            if isinstance(self.result, dict):
                _dict['result'] = self.result
            else:
                _dict['result'] = self.result.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DnsrecordResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DnsrecordResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DnsrecordResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListDnsrecordsResp:
    """
    dns records list response.

    :param bool success: success response.
    :param List[List[str]] errors: errors.
    :param List[List[str]] messages: messages.
    :param List[DnsrecordDetails] result: dns record list.
    :param ResultInfo result_info: result information.
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        result: List['DnsrecordDetails'],
        result_info: 'ResultInfo',
    ) -> None:
        """
        Initialize a ListDnsrecordsResp object.

        :param bool success: success response.
        :param List[List[str]] errors: errors.
        :param List[List[str]] messages: messages.
        :param List[DnsrecordDetails] result: dns record list.
        :param ResultInfo result_info: result information.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result
        self.result_info = result_info

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListDnsrecordsResp':
        """Initialize a ListDnsrecordsResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in ListDnsrecordsResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in ListDnsrecordsResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in ListDnsrecordsResp JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = [DnsrecordDetails.from_dict(v) for v in result]
        else:
            raise ValueError('Required property \'result\' not present in ListDnsrecordsResp JSON')
        if (result_info := _dict.get('result_info')) is not None:
            args['result_info'] = ResultInfo.from_dict(result_info)
        else:
            raise ValueError('Required property \'result_info\' not present in ListDnsrecordsResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListDnsrecordsResp object from a json dictionary."""
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
            result_list = []
            for v in self.result:
                if isinstance(v, dict):
                    result_list.append(v)
                else:
                    result_list.append(v.to_dict())
            _dict['result'] = result_list
        if hasattr(self, 'result_info') and self.result_info is not None:
            if isinstance(self.result_info, dict):
                _dict['result_info'] = self.result_info
            else:
                _dict['result_info'] = self.result_info.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListDnsrecordsResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListDnsrecordsResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListDnsrecordsResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ResultInfo:
    """
    result information.

    :param int page: page.
    :param int per_page: per page.
    :param int count: count.
    :param int total_count: total count.
    """

    def __init__(
        self,
        page: int,
        per_page: int,
        count: int,
        total_count: int,
    ) -> None:
        """
        Initialize a ResultInfo object.

        :param int page: page.
        :param int per_page: per page.
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
        if (page := _dict.get('page')) is not None:
            args['page'] = page
        else:
            raise ValueError('Required property \'page\' not present in ResultInfo JSON')
        if (per_page := _dict.get('per_page')) is not None:
            args['per_page'] = per_page
        else:
            raise ValueError('Required property \'per_page\' not present in ResultInfo JSON')
        if (count := _dict.get('count')) is not None:
            args['count'] = count
        else:
            raise ValueError('Required property \'count\' not present in ResultInfo JSON')
        if (total_count := _dict.get('total_count')) is not None:
            args['total_count'] = total_count
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
