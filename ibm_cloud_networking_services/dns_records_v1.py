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
DNS records
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

class DnsRecordsV1(BaseService):
    """The DNS Records V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'dns_records'

    @classmethod
    def new_instance(cls,
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

    def __init__(self,
                 crn: str,
                 zone_identifier: str,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the DNS Records service.

        :param str crn: Full crn of the service instance.

        :param str zone_identifier: Zone identifier (zone id).

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
    # DNS Records
    #########################


    def list_all_dns_records(self,
        *,
        type: str = None,
        name: str = None,
        content: str = None,
        page: int = None,
        per_page: int = None,
        order: str = None,
        direction: str = None,
        match: str = None,
        **kwargs
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_all_dns_records')
        headers.update(sdk_headers)

        params = {
            'type': type,
            'name': name,
            'content': content,
            'page': page,
            'per_page': per_page,
            'order': order,
            'direction': direction,
            'match': match
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/dns_records'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_dns_record(self,
        *,
        type: str = None,
        name: str = None,
        content: str = None,
        priority: int = None,
        data: object = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create DNS record.

        Add a new DNS record for a given zone for a given service instance.

        :param str type: (optional) dns record type.
        :param str name: (optional) Required for all record types except SRV.
        :param str content: (optional) dns record content.
        :param int priority: (optional) For MX records only.
        :param object data: (optional) For LOC, SRV and CAA records only.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DnsrecordResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_dns_record')
        headers.update(sdk_headers)

        data = {
            'type': type,
            'name': name,
            'content': content,
            'priority': priority,
            'data': data
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/dns_records'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_dns_record(self,
        dnsrecord_identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete DNS record.

        Delete a DNS record given its id.

        :param str dnsrecord_identifier: Identifier of DNS record.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteDnsrecordResp` object
        """

        if dnsrecord_identifier is None:
            raise ValueError('dnsrecord_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_dns_record')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/dns_records/{2}'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier, dnsrecord_identifier))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_dns_record(self,
        dnsrecord_identifier: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get DNS record.

        Get the details of a DNS record for a given zone under a given service instance.

        :param str dnsrecord_identifier: Identifier of DNS record.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DnsrecordResp` object
        """

        if dnsrecord_identifier is None:
            raise ValueError('dnsrecord_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_dns_record')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/dns_records/{2}'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier, dnsrecord_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_dns_record(self,
        dnsrecord_identifier: str,
        *,
        type: str = None,
        name: str = None,
        content: str = None,
        priority: int = None,
        proxied: bool = None,
        data: object = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update DNS record.

        Update an existing DNS record for a given zone under a given service instance.

        :param str dnsrecord_identifier: Identifier of DNS record.
        :param str type: (optional) dns record type.
        :param str name: (optional) Required for all record types except SRV.
        :param str content: (optional) content of dns record.
        :param int priority: (optional) For MX records only.
        :param bool proxied: (optional) proxied.
        :param object data: (optional) For LOC, SRV and CAA records only.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DnsrecordResp` object
        """

        if dnsrecord_identifier is None:
            raise ValueError('dnsrecord_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_dns_record')
        headers.update(sdk_headers)

        data = {
            'type': type,
            'name': name,
            'content': content,
            'priority': priority,
            'proxied': proxied,
            'data': data
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/dns_records/{2}'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier, dnsrecord_identifier))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
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


class DeleteDnsrecordRespResult():
    """
    result.

    :attr str id: dns record id.
    """

    def __init__(self,
                 id: str) -> None:
        """
        Initialize a DeleteDnsrecordRespResult object.

        :param str id: dns record id.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteDnsrecordRespResult':
        """Initialize a DeleteDnsrecordRespResult object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
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

class DeleteDnsrecordResp():
    """
    dns record delete response.

    :attr bool success: success response.
    :attr List[List[str]] errors: errors.
    :attr List[List[str]] messages: messages.
    :attr DeleteDnsrecordRespResult result: result.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'DeleteDnsrecordRespResult') -> None:
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
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in DeleteDnsrecordResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in DeleteDnsrecordResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in DeleteDnsrecordResp JSON')
        if 'result' in _dict:
            args['result'] = DeleteDnsrecordRespResult.from_dict(_dict.get('result'))
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

class DnsrecordDetails():
    """
    dns record details.

    :attr str id: (optional) dns record identifier.
    :attr str created_on: (optional) created on.
    :attr str modified_on: (optional) modified date.
    :attr str name: (optional) dns record name.
    :attr str type: (optional) dns record type.
    :attr str content: (optional) dns record content.
    :attr str zone_id: (optional) zone identifier.
    :attr str zone_name: (optional) zone name.
    :attr bool proxiable: (optional) proxiable.
    :attr bool proxied: (optional) proxied.
    :attr int ttl: (optional) dns record ttl value.
    :attr int priority: (optional) Relevant only to MX type records.
    :attr object data: (optional) Data details for the DNS record. Only for LOC,
          SRV, CAA records.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 created_on: str = None,
                 modified_on: str = None,
                 name: str = None,
                 type: str = None,
                 content: str = None,
                 zone_id: str = None,
                 zone_name: str = None,
                 proxiable: bool = None,
                 proxied: bool = None,
                 ttl: int = None,
                 priority: int = None,
                 data: object = None) -> None:
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
        :param object data: (optional) Data details for the DNS record. Only for
               LOC, SRV, CAA records.
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
        if 'content' in _dict:
            args['content'] = _dict.get('content')
        if 'zone_id' in _dict:
            args['zone_id'] = _dict.get('zone_id')
        if 'zone_name' in _dict:
            args['zone_name'] = _dict.get('zone_name')
        if 'proxiable' in _dict:
            args['proxiable'] = _dict.get('proxiable')
        if 'proxied' in _dict:
            args['proxied'] = _dict.get('proxied')
        if 'ttl' in _dict:
            args['ttl'] = _dict.get('ttl')
        if 'priority' in _dict:
            args['priority'] = _dict.get('priority')
        if 'data' in _dict:
            args['data'] = _dict.get('data')
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
        SPF = 'SPF'
        CAA = 'CAA'


class DnsrecordResp():
    """
    dns record response.

    :attr bool success: success response.
    :attr List[List[str]] errors: errors.
    :attr List[List[str]] messages: messages.
    :attr DnsrecordDetails result: dns record details.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: 'DnsrecordDetails') -> None:
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
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in DnsrecordResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in DnsrecordResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in DnsrecordResp JSON')
        if 'result' in _dict:
            args['result'] = DnsrecordDetails.from_dict(_dict.get('result'))
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

class ListDnsrecordsResp():
    """
    dns records list response.

    :attr bool success: success response.
    :attr List[List[str]] errors: errors.
    :attr List[List[str]] messages: messages.
    :attr List[DnsrecordDetails] result: dns record list.
    :attr ResultInfo result_info: result information.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List[List[str]],
                 result: List['DnsrecordDetails'],
                 result_info: 'ResultInfo') -> None:
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
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in ListDnsrecordsResp JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in ListDnsrecordsResp JSON')
        if 'messages' in _dict:
            args['messages'] = _dict.get('messages')
        else:
            raise ValueError('Required property \'messages\' not present in ListDnsrecordsResp JSON')
        if 'result' in _dict:
            args['result'] = [DnsrecordDetails.from_dict(x) for x in _dict.get('result')]
        else:
            raise ValueError('Required property \'result\' not present in ListDnsrecordsResp JSON')
        if 'result_info' in _dict:
            args['result_info'] = ResultInfo.from_dict(_dict.get('result_info'))
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
            _dict['result'] = [x.to_dict() for x in self.result]
        if hasattr(self, 'result_info') and self.result_info is not None:
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

class ResultInfo():
    """
    result information.

    :attr int page: page.
    :attr int per_page: per page.
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
