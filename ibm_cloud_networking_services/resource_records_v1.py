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


    def list_resource_records(self, instance_id: str, dnszone_id: str, *, x_correlation_id: str = None, offset: int = None, limit: int = None, **kwargs) -> DetailedResponse:
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='list_resource_records')
        headers.update(sdk_headers)

        params = {
            'offset': offset,
            'limit': limit
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/instances/{0}/dnszones/{1}/resource_records'.format(*self.encode_path_vars(instance_id, dnszone_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


    def create_resource_record(self, instance_id: str, dnszone_id: str, *, type: str = None, name: str = None, rdata: 'ResourceRecordInputRdata' = None, ttl: int = None, service: str = None, protocol: str = None, x_correlation_id: str = None, **kwargs) -> DetailedResponse:
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='create_resource_record')
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

        url = '/instances/{0}/dnszones/{1}/resource_records'.format(*self.encode_path_vars(instance_id, dnszone_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def delete_resource_record(self, instance_id: str, dnszone_id: str, record_id: str, *, x_correlation_id: str = None, **kwargs) -> DetailedResponse:
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='delete_resource_record')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/instances/{0}/dnszones/{1}/resource_records/{2}'.format(*self.encode_path_vars(instance_id, dnszone_id, record_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_resource_record(self, instance_id: str, dnszone_id: str, record_id: str, *, x_correlation_id: str = None, **kwargs) -> DetailedResponse:
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='get_resource_record')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/instances/{0}/dnszones/{1}/resource_records/{2}'.format(*self.encode_path_vars(instance_id, dnszone_id, record_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_resource_record(self, instance_id: str, dnszone_id: str, record_id: str, *, name: str = None, rdata: 'ResourceRecordUpdateInputRdata' = None, ttl: int = None, service: str = None, protocol: str = None, x_correlation_id: str = None, **kwargs) -> DetailedResponse:
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V1', operation_id='update_resource_record')
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

        url = '/instances/{0}/dnszones/{1}/resource_records/{2}'.format(*self.encode_path_vars(instance_id, dnszone_id, record_id))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

