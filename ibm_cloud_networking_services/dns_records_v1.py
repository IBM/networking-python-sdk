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
    # List all DNS records
    #########################


    def list_all_dns_records(self, *, type: str = None, name: str = None, content: str = None, page: int = None, per_page: int = None, order: str = None, direction: str = None, match: str = None, **kwargs) -> DetailedResponse:
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='list_all_dns_records')
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

        url = '/v1/{0}/zones/{1}/dns_records'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # Get a DNS record
    #########################


    def get_dns_record(self, dnsrecord_identifier: str, **kwargs) -> DetailedResponse:
        """
        Get a DNS record.

        Get the details of a DNS record for a given zone under a given service instance.

        :param str dnsrecord_identifier: Identifier of DNS record.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DnsrecordResp` object
        """

        if dnsrecord_identifier is None:
            raise ValueError('dnsrecord_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_dns_record')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/dns_records/{2}'.format(*self.encode_path_vars(self.crn, self.zone_identifier, dnsrecord_identifier))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response

    #########################
    # Create a DNS record
    #########################


    def create_dns_record(self, *, type: str = None, name: str = None, content: str = None, priority: int = None, data: object = None, **kwargs) -> DetailedResponse:
        """
        Create a DNS record.

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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='create_dns_record')
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

        url = '/v1/{0}/zones/{1}/dns_records'.format(*self.encode_path_vars(self.crn, self.zone_identifier))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Update a DNS record
    #########################


    def update_dns_record(self, dnsrecord_identifier: str, *, type: str = None, name: str = None, content: str = None, priority: int = None, proxied: bool = None, data: object = None, **kwargs) -> DetailedResponse:
        """
        Update a DNS record.

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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_dns_record')
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

        url = '/v1/{0}/zones/{1}/dns_records/{2}'.format(*self.encode_path_vars(self.crn, self.zone_identifier, dnsrecord_identifier))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Delete a DNS record
    #########################


    def delete_dns_record(self, dnsrecord_identifier: str, **kwargs) -> DetailedResponse:
        """
        Delete a DNS record.

        Delete a DNS record given its id.

        :param str dnsrecord_identifier: Identifier of DNS record.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteDnsrecordResp` object
        """

        if dnsrecord_identifier is None:
            raise ValueError('dnsrecord_identifier must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='delete_dns_record')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v1/{0}/zones/{1}/dns_records/{2}'.format(*self.encode_path_vars(self.crn, self.zone_identifier, dnsrecord_identifier))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


class ListAllDnsRecordsEnums:
    """
    Enums for list_all_dns_records parameters.
    """

    class Order(Enum):
        """
        Field by which to order list of DNS records.
        """
        TYPE = 'type'
        NAME = 'name'
        CONTENT = 'content'
        TTL = 'ttl'
        PROXIED = 'proxied'
    class Direction(Enum):
        """
        Direction in which to order results [ascending/descending order].
        """
        ASC = 'asc'
        DESC = 'desc'
    class Match(Enum):
        """
        Whether to match all (all) or atleast one search parameter (any).
        """
        ANY = 'any'
        ALL = 'all'

