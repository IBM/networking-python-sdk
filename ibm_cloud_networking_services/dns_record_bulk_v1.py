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
Import/Export zone files
"""

from typing import BinaryIO, Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class DnsRecordBulkV1(BaseService):
    """The DNS Record Bulk V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'dns_record_bulk'

    @classmethod
    def new_instance(cls,
                     crn: str,
                     zone_identifier: str,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'DnsRecordBulkV1':
        """
        Return a new client for the DNS Record Bulk service using the specified
               parameters and external configuration.

        :param str crn: Full url-encoded CRN of the service instance.

        :param str zone_identifier: Identifier of zone.
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
        Construct a new client for the DNS Record Bulk service.

        :param str crn: Full url-encoded CRN of the service instance.

        :param str zone_identifier: Identifier of zone.

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
    # dNSRecords
    #########################


    def get_dns_records_bulk(self,
        **kwargs
    ) -> DetailedResponse:
        """
        Export zone file.

        Export zone file.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_dns_records_bulk')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/dns_records_bulk'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def post_dns_records_bulk(self,
        *,
        file: BinaryIO = None,
        file_content_type: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Import zone file.

        Import zone file.

        :param BinaryIO file: (optional) file to upload.
        :param str file_content_type: (optional) The content type of file.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DnsRecordsObject` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='post_dns_records_bulk')
        headers.update(sdk_headers)

        form_data = []
        if file:
            form_data.append(('file', (None, file, file_content_type or 'application/octet-stream')))

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/dns_records_bulk'.format(
            *self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       files=form_data)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class DnsRecordsObjectMessagesItem():
    """
    DnsRecordsObjectMessagesItem.

    :attr int code: (optional) Message code.
    :attr str message: (optional) Message corresponding to the code.
    """

    def __init__(self,
                 *,
                 code: int = None,
                 message: str = None) -> None:
        """
        Initialize a DnsRecordsObjectMessagesItem object.

        :param int code: (optional) Message code.
        :param str message: (optional) Message corresponding to the code.
        """
        self.code = code
        self.message = message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DnsRecordsObjectMessagesItem':
        """Initialize a DnsRecordsObjectMessagesItem object from a json dictionary."""
        args = {}
        if 'code' in _dict:
            args['code'] = _dict.get('code')
        if 'message' in _dict:
            args['message'] = _dict.get('message')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DnsRecordsObjectMessagesItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'code') and self.code is not None:
            _dict['code'] = self.code
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DnsRecordsObjectMessagesItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DnsRecordsObjectMessagesItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DnsRecordsObjectMessagesItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DnsRecordsObjectResult():
    """
    DNS record.

    :attr int recs_added: total records added.
    :attr int total_records_parsed: total records parsed.
    """

    def __init__(self,
                 recs_added: int,
                 total_records_parsed: int) -> None:
        """
        Initialize a DnsRecordsObjectResult object.

        :param int recs_added: total records added.
        :param int total_records_parsed: total records parsed.
        """
        self.recs_added = recs_added
        self.total_records_parsed = total_records_parsed

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DnsRecordsObjectResult':
        """Initialize a DnsRecordsObjectResult object from a json dictionary."""
        args = {}
        if 'recs_added' in _dict:
            args['recs_added'] = _dict.get('recs_added')
        else:
            raise ValueError('Required property \'recs_added\' not present in DnsRecordsObjectResult JSON')
        if 'total_records_parsed' in _dict:
            args['total_records_parsed'] = _dict.get('total_records_parsed')
        else:
            raise ValueError('Required property \'total_records_parsed\' not present in DnsRecordsObjectResult JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DnsRecordsObjectResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'recs_added') and self.recs_added is not None:
            _dict['recs_added'] = self.recs_added
        if hasattr(self, 'total_records_parsed') and self.total_records_parsed is not None:
            _dict['total_records_parsed'] = self.total_records_parsed
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DnsRecordsObjectResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DnsRecordsObjectResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DnsRecordsObjectResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DnsRecordsObjectTiming():
    """
    timing object.

    :attr str start_time: (optional) start time.
    :attr str end_time: (optional) end time.
    :attr int process_time: (optional) process time.
    """

    def __init__(self,
                 *,
                 start_time: str = None,
                 end_time: str = None,
                 process_time: int = None) -> None:
        """
        Initialize a DnsRecordsObjectTiming object.

        :param str start_time: (optional) start time.
        :param str end_time: (optional) end time.
        :param int process_time: (optional) process time.
        """
        self.start_time = start_time
        self.end_time = end_time
        self.process_time = process_time

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DnsRecordsObjectTiming':
        """Initialize a DnsRecordsObjectTiming object from a json dictionary."""
        args = {}
        if 'start_time' in _dict:
            args['start_time'] = _dict.get('start_time')
        if 'end_time' in _dict:
            args['end_time'] = _dict.get('end_time')
        if 'process_time' in _dict:
            args['process_time'] = _dict.get('process_time')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DnsRecordsObjectTiming object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'start_time') and self.start_time is not None:
            _dict['start_time'] = self.start_time
        if hasattr(self, 'end_time') and self.end_time is not None:
            _dict['end_time'] = self.end_time
        if hasattr(self, 'process_time') and self.process_time is not None:
            _dict['process_time'] = self.process_time
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DnsRecordsObjectTiming object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DnsRecordsObjectTiming') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DnsRecordsObjectTiming') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class DnsRecordsObject():
    """
    dns records objects.

    :attr bool success: Operation success flag.
    :attr List[List[str]] errors: Array of errors encountered.
    :attr List[DnsRecordsObjectMessagesItem] messages: Array of messages returned.
    :attr DnsRecordsObjectResult result: DNS record.
    :attr DnsRecordsObjectTiming timing: (optional) timing object.
    """

    def __init__(self,
                 success: bool,
                 errors: List[List[str]],
                 messages: List['DnsRecordsObjectMessagesItem'],
                 result: 'DnsRecordsObjectResult',
                 *,
                 timing: 'DnsRecordsObjectTiming' = None) -> None:
        """
        Initialize a DnsRecordsObject object.

        :param bool success: Operation success flag.
        :param List[List[str]] errors: Array of errors encountered.
        :param List[DnsRecordsObjectMessagesItem] messages: Array of messages
               returned.
        :param DnsRecordsObjectResult result: DNS record.
        :param DnsRecordsObjectTiming timing: (optional) timing object.
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result
        self.timing = timing

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DnsRecordsObject':
        """Initialize a DnsRecordsObject object from a json dictionary."""
        args = {}
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError('Required property \'success\' not present in DnsRecordsObject JSON')
        if 'errors' in _dict:
            args['errors'] = _dict.get('errors')
        else:
            raise ValueError('Required property \'errors\' not present in DnsRecordsObject JSON')
        if 'messages' in _dict:
            args['messages'] = [DnsRecordsObjectMessagesItem.from_dict(x) for x in _dict.get('messages')]
        else:
            raise ValueError('Required property \'messages\' not present in DnsRecordsObject JSON')
        if 'result' in _dict:
            args['result'] = DnsRecordsObjectResult.from_dict(_dict.get('result'))
        else:
            raise ValueError('Required property \'result\' not present in DnsRecordsObject JSON')
        if 'timing' in _dict:
            args['timing'] = DnsRecordsObjectTiming.from_dict(_dict.get('timing'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DnsRecordsObject object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = self.errors
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = [x.to_dict() for x in self.messages]
        if hasattr(self, 'result') and self.result is not None:
            _dict['result'] = self.result.to_dict()
        if hasattr(self, 'timing') and self.timing is not None:
            _dict['timing'] = self.timing.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DnsRecordsObject object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DnsRecordsObject') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DnsRecordsObject') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
