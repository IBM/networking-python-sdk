# coding: utf-8

# (C) Copyright IBM Corp. 2022.
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

# IBM OpenAPI SDK Code Generator Version: 3.47.1-be944570-20220406-170244
 
"""
DNS Services API

API Version: 1.0.0
"""

from enum import Enum
from typing import BinaryIO, Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class DnsSvcsV1(BaseService):
    """The DNS Svcs V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.dns-svcs.cloud.ibm.com/v1'
    DEFAULT_SERVICE_NAME = 'dns_svcs'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'DnsSvcsV1':
        """
        Return a new client for the DNS Svcs service using the specified parameters
               and external configuration.
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
        Construct a new client for the DNS Svcs service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # DNS Zones
    #########################


    def list_dnszones(self,
        instance_id: str,
        *,
        x_correlation_id: str = None,
        offset: int = None,
        limit: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List DNS zones.

        List the DNS zones for a given service instance.

        :param str instance_id: The unique identifier of a service instance.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param int offset: (optional) Specify how many resources to skip over, the
               default value is 0.
        :param int limit: (optional) Specify maximum resources might be returned.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListDnszones` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_dnszones')
        headers.update(sdk_headers)

        params = {
            'offset': offset,
            'limit': limit
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def create_dnszone(self,
        instance_id: str,
        *,
        name: str = None,
        description: str = None,
        label: str = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create DNS zone.

        Create a DNS zone for a given service instance.

        :param str instance_id: The unique identifier of a service instance.
        :param str name: (optional) Name of DNS zone.
        :param str description: (optional) The text describing the purpose of a DNS
               zone.
        :param str label: (optional) The label of a DNS zone.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Dnszone` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_dnszone')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'description': description,
            'label': label
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def delete_dnszone(self,
        instance_id: str,
        dnszone_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete DNS zone.

        Delete a DNS zone.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
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
                                      operation_id='delete_dnszone')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['instance_id', 'dnszone_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_dnszone(self,
        instance_id: str,
        dnszone_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get DNS zone.

        Get details of a DNS zone.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Dnszone` object
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
                                      operation_id='get_dnszone')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'dnszone_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def update_dnszone(self,
        instance_id: str,
        dnszone_id: str,
        *,
        description: str = None,
        label: str = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update DNS zone.

        Update the properties of a DNS zone.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str description: (optional) The text describing the purpose of a DNS
               zone.
        :param str label: (optional) The label of a DNS zone.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Dnszone` object
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
                                      operation_id='update_dnszone')
        headers.update(sdk_headers)

        data = {
            'description': description,
            'label': label
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'dnszone_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

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
        List resource records.

        List the Resource Records for a given DNS zone.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param int offset: (optional) Specify how many resources to skip over, the
               default value is 0.
        :param int limit: (optional) Specify maximum resources might be returned.
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
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'dnszone_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/resource_records'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
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
        Create resource record.

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
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'dnszone_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/resource_records'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
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
        Delete resource record.

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

        path_param_keys = ['instance_id', 'dnszone_id', 'record_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id, record_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/resource_records/{record_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
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
        Get resource record.

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
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'dnszone_id', 'record_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id, record_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/resource_records/{record_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
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
        Update resource record.

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
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'dnszone_id', 'record_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id, record_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/resource_records/{record_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def export_resource_records(self,
        instance_id: str,
        dnszone_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Export resource records to a zone file.

        Export resource records to a zone file.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
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
                                      operation_id='export_resource_records')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'text/plain; charset=utf-8'

        path_param_keys = ['instance_id', 'dnszone_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/export_resource_records'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def import_resource_records(self,
        instance_id: str,
        dnszone_id: str,
        *,
        file: BinaryIO = None,
        file_content_type: str = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Import resource records from a zone file.

        Import resource records from a zone file. The maximum size of a zone file is 8MB.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param BinaryIO file: (optional) file to upload.
        :param str file_content_type: (optional) The content type of file.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ImportResourceRecordsResp` object
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
                                      operation_id='import_resource_records')
        headers.update(sdk_headers)

        form_data = []
        if file:
            form_data.append(('file', (None, file, file_content_type or 'application/octet-stream')))

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'dnszone_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/import_resource_records'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       files=form_data)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Permitted Network
    #########################


    def list_permitted_networks(self,
        instance_id: str,
        dnszone_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List permitted networks.

        List the permitted networks for a given DNS zone.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
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

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'dnszone_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/permitted_networks'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
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
        Create permitted network.

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
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'dnszone_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/permitted_networks'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
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
        Remove permitted network.

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
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'dnszone_id', 'permitted_network_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id, permitted_network_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/permitted_networks/{permitted_network_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
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
        Get permitted network.

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
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'dnszone_id', 'permitted_network_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id, permitted_network_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/permitted_networks/{permitted_network_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Global Load Balancers
    #########################


    def list_load_balancers(self,
        instance_id: str,
        dnszone_id: str,
        *,
        x_correlation_id: str = None,
        offset: int = None,
        limit: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List load balancers.

        List the Global Load Balancers for a given DNS zone.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param int offset: (optional) Specify how many resources to skip over, the
               default value is 0.
        :param int limit: (optional) Specify maximum resources might be returned.
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

        params = {
            'offset': offset,
            'limit': limit
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'dnszone_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/load_balancers'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
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
        Create load balancer.

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
               zones to pool IDs.
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

        path_param_keys = ['instance_id', 'dnszone_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/load_balancers'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
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
        Delete load balancer.

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

        path_param_keys = ['instance_id', 'dnszone_id', 'lb_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id, lb_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/load_balancers/{lb_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
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
        Get load balancer.

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

        path_param_keys = ['instance_id', 'dnszone_id', 'lb_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id, lb_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/load_balancers/{lb_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
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
        Update load balancer.

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
               zones to pool IDs.
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

        path_param_keys = ['instance_id', 'dnszone_id', 'lb_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id, lb_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/load_balancers/{lb_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Pools
    #########################


    def list_pools(self,
        instance_id: str,
        *,
        x_correlation_id: str = None,
        offset: int = None,
        limit: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List load balancer pools.

        List the load balancer pools.

        :param str instance_id: The unique identifier of a service instance.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param int offset: (optional) Specify how many resources to skip over, the
               default value is 0.
        :param int limit: (optional) Specify maximum resources might be returned.
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

        params = {
            'offset': offset,
            'limit': limit
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/pools'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
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
        Create load balancer pool.

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
        :param List[str] healthcheck_subnets: (optional) Health check subnet CRN.
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

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/pools'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def delete_pool(self,
        instance_id: str,
        pool_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete load balancer pool.

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

        path_param_keys = ['instance_id', 'pool_id']
        path_param_values = self.encode_path_vars(instance_id, pool_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/pools/{pool_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_pool(self,
        instance_id: str,
        pool_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get load balancer pool.

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

        path_param_keys = ['instance_id', 'pool_id']
        path_param_values = self.encode_path_vars(instance_id, pool_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/pools/{pool_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
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
        Update load balancer pool.

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
        :param List[str] healthcheck_subnets: (optional) Health check subnet CRNs.
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

        path_param_keys = ['instance_id', 'pool_id']
        path_param_values = self.encode_path_vars(instance_id, pool_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/pools/{pool_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Monitors
    #########################


    def list_monitors(self,
        instance_id: str,
        *,
        x_correlation_id: str = None,
        offset: int = None,
        limit: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List load balancer monitors.

        List the load balancer monitors.

        :param str instance_id: The unique identifier of a service instance.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param int offset: (optional) Specify how many resources to skip over, the
               default value is 0.
        :param int limit: (optional) Specify maximum resources might be returned.
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

        params = {
            'offset': offset,
            'limit': limit
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/monitors'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
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
        Create load balancer monitor.

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

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/monitors'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def delete_monitor(self,
        instance_id: str,
        monitor_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete load balancer monitor.

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

        path_param_keys = ['instance_id', 'monitor_id']
        path_param_values = self.encode_path_vars(instance_id, monitor_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/monitors/{monitor_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_monitor(self,
        instance_id: str,
        monitor_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get load balancer monitor.

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

        path_param_keys = ['instance_id', 'monitor_id']
        path_param_values = self.encode_path_vars(instance_id, monitor_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/monitors/{monitor_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
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
        Update load balancer monitor.

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

        path_param_keys = ['instance_id', 'monitor_id']
        path_param_values = self.encode_path_vars(instance_id, monitor_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/monitors/{monitor_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Custom Resolvers
    #########################


    def list_custom_resolvers(self,
        instance_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List custom resolvers.

        List the custom resolvers.

        :param str instance_id: The unique identifier of a service instance.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CustomResolverList` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_custom_resolvers')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/custom_resolvers'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def create_custom_resolver(self,
        instance_id: str,
        *,
        name: str = None,
        description: str = None,
        locations: List['LocationInput'] = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a custom resolver.

        Create a custom resolver.

        :param str instance_id: The unique identifier of a service instance.
        :param str name: (optional) Name of the custom resolver.
        :param str description: (optional) Descriptive text of the custom resolver.
        :param List[LocationInput] locations: (optional) Locations on which the
               custom resolver will be running.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CustomResolver` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if locations is not None:
            locations = [convert_model(x) for x in locations]
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_custom_resolver')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'description': description,
            'locations': locations
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/custom_resolvers'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def delete_custom_resolver(self,
        instance_id: str,
        resolver_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a custom resolver.

        Delete a custom resolver.

        :param str instance_id: The unique identifier of a service instance.
        :param str resolver_id: The unique identifier of a custom resolver.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if resolver_id is None:
            raise ValueError('resolver_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_custom_resolver')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['instance_id', 'resolver_id']
        path_param_values = self.encode_path_vars(instance_id, resolver_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/custom_resolvers/{resolver_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_custom_resolver(self,
        instance_id: str,
        resolver_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a custom resolver.

        Get details of a custom resolver.

        :param str instance_id: The unique identifier of a service instance.
        :param str resolver_id: The unique identifier of a custom resolver.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CustomResolver` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if resolver_id is None:
            raise ValueError('resolver_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_custom_resolver')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'resolver_id']
        path_param_values = self.encode_path_vars(instance_id, resolver_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/custom_resolvers/{resolver_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def update_custom_resolver(self,
        instance_id: str,
        resolver_id: str,
        *,
        name: str = None,
        description: str = None,
        enabled: bool = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update a custom resolver.

        Update the properties of a custom resolver.

        :param str instance_id: The unique identifier of a service instance.
        :param str resolver_id: The unique identifier of a custom resolver.
        :param str name: (optional) Name of the custom resolver.
        :param str description: (optional) Descriptive text of the custom resolver.
        :param bool enabled: (optional) Whether the custom resolver is enabled.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CustomResolver` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if resolver_id is None:
            raise ValueError('resolver_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_custom_resolver')
        headers.update(sdk_headers)

        data = {
            'name': name,
            'description': description,
            'enabled': enabled
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'resolver_id']
        path_param_values = self.encode_path_vars(instance_id, resolver_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/custom_resolvers/{resolver_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def update_cr_locations_order(self,
        instance_id: str,
        resolver_id: str,
        *,
        locations: List[str] = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update the locations order of a custom resolver.

        Update the locations order of a custom resolver.

        :param str instance_id: The unique identifier of a service instance.
        :param str resolver_id: The unique identifier of a custom resolver.
        :param List[str] locations: (optional) Array of custom resolver location
               ID.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CustomResolver` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if resolver_id is None:
            raise ValueError('resolver_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_cr_locations_order')
        headers.update(sdk_headers)

        data = {
            'locations': locations
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'resolver_id']
        path_param_values = self.encode_path_vars(instance_id, resolver_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/custom_resolvers/{resolver_id}/locations_order'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Custom Resolver Locations
    #########################


    def add_custom_resolver_location(self,
        instance_id: str,
        resolver_id: str,
        *,
        subnet_crn: str = None,
        enabled: bool = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Add custom resolver location.

        Add custom resolver location.

        :param str instance_id: The unique identifier of a service instance.
        :param str resolver_id: The unique identifier of a custom resolver.
        :param str subnet_crn: (optional) Custom resolver location, subnet CRN.
        :param bool enabled: (optional) Enable/Disable custom resolver location.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Location` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if resolver_id is None:
            raise ValueError('resolver_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='add_custom_resolver_location')
        headers.update(sdk_headers)

        data = {
            'subnet_crn': subnet_crn,
            'enabled': enabled
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'resolver_id']
        path_param_values = self.encode_path_vars(instance_id, resolver_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/custom_resolvers/{resolver_id}/locations'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def update_custom_resolver_location(self,
        instance_id: str,
        resolver_id: str,
        location_id: str,
        *,
        enabled: bool = None,
        subnet_crn: str = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update custom resolver location.

        Update custom resolver location.

        :param str instance_id: The unique identifier of a service instance.
        :param str resolver_id: The unique identifier of a custom resolver.
        :param str location_id: Custom resolver location ID.
        :param bool enabled: (optional) Enable/Disable custom resolver location.
        :param str subnet_crn: (optional) Subnet CRN.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Location` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if resolver_id is None:
            raise ValueError('resolver_id must be provided')
        if location_id is None:
            raise ValueError('location_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_custom_resolver_location')
        headers.update(sdk_headers)

        data = {
            'enabled': enabled,
            'subnet_crn': subnet_crn
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'resolver_id', 'location_id']
        path_param_values = self.encode_path_vars(instance_id, resolver_id, location_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/custom_resolvers/{resolver_id}/locations/{location_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def delete_custom_resolver_location(self,
        instance_id: str,
        resolver_id: str,
        location_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete custom resolver location.

        Delete custom resolver location.

        :param str instance_id: The unique identifier of a service instance.
        :param str resolver_id: The unique identifier of a custom resolver.
        :param str location_id: Custom resolver location ID.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if resolver_id is None:
            raise ValueError('resolver_id must be provided')
        if location_id is None:
            raise ValueError('location_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_custom_resolver_location')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['instance_id', 'resolver_id', 'location_id']
        path_param_values = self.encode_path_vars(instance_id, resolver_id, location_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/custom_resolvers/{resolver_id}/locations/{location_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Forwarding Rules
    #########################


    def list_forwarding_rules(self,
        instance_id: str,
        resolver_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List forwarding rules.

        List the forwarding rules of the given custom resolver.

        :param str instance_id: The unique identifier of a service instance.
        :param str resolver_id: The unique identifier of a custom resolver.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ForwardingRuleList` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if resolver_id is None:
            raise ValueError('resolver_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_forwarding_rules')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'resolver_id']
        path_param_values = self.encode_path_vars(instance_id, resolver_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/custom_resolvers/{resolver_id}/forwarding_rules'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def create_forwarding_rule(self,
        instance_id: str,
        resolver_id: str,
        *,
        type: str = None,
        match: str = None,
        forward_to: List[str] = None,
        description: str = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a forwarding rule.

        Create a forwarding rule for the given custom resolver.

        :param str instance_id: The unique identifier of a service instance.
        :param str resolver_id: The unique identifier of a custom resolver.
        :param str type: (optional) Type of the forwarding rule.
        :param str match: (optional) The matching zone or hostname.
        :param List[str] forward_to: (optional) The upstream DNS servers will be
               forwarded to.
        :param str description: (optional) Descriptive text of the forwarding rule.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ForwardingRule` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if resolver_id is None:
            raise ValueError('resolver_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_forwarding_rule')
        headers.update(sdk_headers)

        data = {
            'type': type,
            'match': match,
            'forward_to': forward_to,
            'description': description
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'resolver_id']
        path_param_values = self.encode_path_vars(instance_id, resolver_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/custom_resolvers/{resolver_id}/forwarding_rules'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def delete_forwarding_rule(self,
        instance_id: str,
        resolver_id: str,
        rule_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a forwarding rule.

        Delete a forwarding rule on the given custom resolver.

        :param str instance_id: The unique identifier of a service instance.
        :param str resolver_id: The unique identifier of a custom resolver.
        :param str rule_id: The unique identifier of a rule.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if resolver_id is None:
            raise ValueError('resolver_id must be provided')
        if rule_id is None:
            raise ValueError('rule_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_forwarding_rule')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['instance_id', 'resolver_id', 'rule_id']
        path_param_values = self.encode_path_vars(instance_id, resolver_id, rule_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/custom_resolvers/{resolver_id}/forwarding_rules/{rule_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_forwarding_rule(self,
        instance_id: str,
        resolver_id: str,
        rule_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a forwarding rule.

        Get details of a forwarding rule on the given custom resolver.

        :param str instance_id: The unique identifier of a service instance.
        :param str resolver_id: The unique identifier of a custom resolver.
        :param str rule_id: The unique identifier of a rule.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ForwardingRule` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if resolver_id is None:
            raise ValueError('resolver_id must be provided')
        if rule_id is None:
            raise ValueError('rule_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_forwarding_rule')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'resolver_id', 'rule_id']
        path_param_values = self.encode_path_vars(instance_id, resolver_id, rule_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/custom_resolvers/{resolver_id}/forwarding_rules/{rule_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def update_forwarding_rule(self,
        instance_id: str,
        resolver_id: str,
        rule_id: str,
        *,
        description: str = None,
        match: str = None,
        forward_to: List[str] = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update a forwarding rule.

        Update the properties of a forwarding rule on the given custom resolver.

        :param str instance_id: The unique identifier of a service instance.
        :param str resolver_id: The unique identifier of a custom resolver.
        :param str rule_id: The unique identifier of a rule.
        :param str description: (optional) Descriptive text of the forwarding rule.
        :param str match: (optional) The matching zone or hostname.
        :param List[str] forward_to: (optional) The upstream DNS servers will be
               forwarded to.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ForwardingRule` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if resolver_id is None:
            raise ValueError('resolver_id must be provided')
        if rule_id is None:
            raise ValueError('rule_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_forwarding_rule')
        headers.update(sdk_headers)

        data = {
            'description': description,
            'match': match,
            'forward_to': forward_to
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'resolver_id', 'rule_id']
        path_param_values = self.encode_path_vars(instance_id, resolver_id, rule_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/custom_resolvers/{resolver_id}/forwarding_rules/{rule_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Secondary Zones
    #########################


    def create_secondary_zone(self,
        instance_id: str,
        resolver_id: str,
        *,
        zone: str = None,
        transfer_from: List[str] = None,
        description: str = None,
        enabled: bool = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a secondary zone.

        Create a secondary zone for the custom resolver.

        :param str instance_id: The unique identifier of a service instance.
        :param str resolver_id: The unique identifier of a custom resolver.
        :param str zone: (optional) zone name.
        :param List[str] transfer_from: (optional) The addresses of DNS servers
               where the secondary zone data should be transferred from.
        :param str description: (optional) Descriptive text of the secondary zone.
        :param bool enabled: (optional) Enable/Disable the secondary zone.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SecondaryZone` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if resolver_id is None:
            raise ValueError('resolver_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_secondary_zone')
        headers.update(sdk_headers)

        data = {
            'zone': zone,
            'transfer_from': transfer_from,
            'description': description,
            'enabled': enabled
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'resolver_id']
        path_param_values = self.encode_path_vars(instance_id, resolver_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/custom_resolvers/{resolver_id}/secondary_zones'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def list_secondary_zones(self,
        instance_id: str,
        resolver_id: str,
        *,
        x_correlation_id: str = None,
        offset: int = None,
        limit: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List secondary zones.

        List secondary zones for the custom resolver.

        :param str instance_id: The unique identifier of a service instance.
        :param str resolver_id: The unique identifier of a custom resolver.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param int offset: (optional) Specify how many resources to skip over, the
               default value is 0.
        :param int limit: (optional) Specify maximum resources might be returned.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SecondaryZoneList` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if resolver_id is None:
            raise ValueError('resolver_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_secondary_zones')
        headers.update(sdk_headers)

        params = {
            'offset': offset,
            'limit': limit
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'resolver_id']
        path_param_values = self.encode_path_vars(instance_id, resolver_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/custom_resolvers/{resolver_id}/secondary_zones'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def get_secondary_zone(self,
        instance_id: str,
        resolver_id: str,
        secondary_zone_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a secondary zone.

        Get details of a secondary zone for the custom resolver.

        :param str instance_id: The unique identifier of a service instance.
        :param str resolver_id: The unique identifier of a custom resolver.
        :param str secondary_zone_id: The unique identifier of a secondary zone.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SecondaryZone` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if resolver_id is None:
            raise ValueError('resolver_id must be provided')
        if secondary_zone_id is None:
            raise ValueError('secondary_zone_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_secondary_zone')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'resolver_id', 'secondary_zone_id']
        path_param_values = self.encode_path_vars(instance_id, resolver_id, secondary_zone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/custom_resolvers/{resolver_id}/secondary_zones/{secondary_zone_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def update_secondary_zone(self,
        instance_id: str,
        resolver_id: str,
        secondary_zone_id: str,
        *,
        description: str = None,
        enabled: bool = None,
        transfer_from: List[str] = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update a secondary zone.

        Update a secondary zone for the custom resolver.

        :param str instance_id: The unique identifier of a service instance.
        :param str resolver_id: The unique identifier of a custom resolver.
        :param str secondary_zone_id: The unique identifier of a secondary zone.
        :param str description: (optional) Descriptive text of the secondary zone.
        :param bool enabled: (optional) Enable/Disable the secondary zone.
        :param List[str] transfer_from: (optional) The addresses of DNS servers
               where the secondary zone data should be transferred from.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SecondaryZone` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if resolver_id is None:
            raise ValueError('resolver_id must be provided')
        if secondary_zone_id is None:
            raise ValueError('secondary_zone_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_secondary_zone')
        headers.update(sdk_headers)

        data = {
            'description': description,
            'enabled': enabled,
            'transfer_from': transfer_from
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'resolver_id', 'secondary_zone_id']
        path_param_values = self.encode_path_vars(instance_id, resolver_id, secondary_zone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/custom_resolvers/{resolver_id}/secondary_zones/{secondary_zone_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def delete_secondary_zone(self,
        instance_id: str,
        resolver_id: str,
        secondary_zone_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a secondary zone.

        Delete a secondary zone for the custom resolver.

        :param str instance_id: The unique identifier of a service instance.
        :param str resolver_id: The unique identifier of a custom resolver.
        :param str secondary_zone_id: The unique identifier of a secondary zone.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if resolver_id is None:
            raise ValueError('resolver_id must be provided')
        if secondary_zone_id is None:
            raise ValueError('secondary_zone_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_secondary_zone')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['instance_id', 'resolver_id', 'secondary_zone_id']
        path_param_values = self.encode_path_vars(instance_id, resolver_id, secondary_zone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/custom_resolvers/{resolver_id}/secondary_zones/{secondary_zone_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Linked Zones
    #########################


    def list_linked_zones(self,
        instance_id: str,
        *,
        x_correlation_id: str = None,
        offset: int = None,
        limit: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List linked zones.

        List linked zones in requestor's instance.

        :param str instance_id: The unique identifier of a service instance.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param int offset: (optional) Specify how many resources to skip over, the
               default value is 0.
        :param int limit: (optional) Specify maximum resources might be returned.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LinkedDnszonesList` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_linked_zones')
        headers.update(sdk_headers)

        params = {
            'offset': offset,
            'limit': limit
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/linked_dnszones'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def create_linked_zone(self,
        instance_id: str,
        *,
        owner_instance_id: str = None,
        owner_zone_id: str = None,
        description: str = None,
        label: str = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a linked zone.

        Create a linked zone.

        :param str instance_id: The unique identifier of a service instance.
        :param str owner_instance_id: (optional) Owner's instance ID.
        :param str owner_zone_id: (optional) Owner's DNS zone ID.
        :param str description: (optional) Descriptive text of the linked zone.
        :param str label: (optional) The label of linked zone.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LinkedDnszone` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_linked_zone')
        headers.update(sdk_headers)

        data = {
            'owner_instance_id': owner_instance_id,
            'owner_zone_id': owner_zone_id,
            'description': description,
            'label': label
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/linked_dnszones'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def get_linked_zone(self,
        instance_id: str,
        linked_dnszone_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a linked zone.

        Get details of a linked zone.

        :param str instance_id: The unique identifier of a service instance.
        :param str linked_dnszone_id: The unique identifier of a linked zone.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LinkedDnszone` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if linked_dnszone_id is None:
            raise ValueError('linked_dnszone_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_linked_zone')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'linked_dnszone_id']
        path_param_values = self.encode_path_vars(instance_id, linked_dnszone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/linked_dnszones/{linked_dnszone_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def update_linked_zone(self,
        instance_id: str,
        linked_dnszone_id: str,
        *,
        description: str = None,
        label: str = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update the properties of a linked zone.

        Update the properties of a linked zone.

        :param str instance_id: The unique identifier of a service instance.
        :param str linked_dnszone_id: The unique identifier of a linked zone.
        :param str description: (optional) Descriptive text of the linked zone.
        :param str label: (optional) The label of linked zone.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LinkedDnszone` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if linked_dnszone_id is None:
            raise ValueError('linked_dnszone_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_linked_zone')
        headers.update(sdk_headers)

        data = {
            'description': description,
            'label': label
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'linked_dnszone_id']
        path_param_values = self.encode_path_vars(instance_id, linked_dnszone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/linked_dnszones/{linked_dnszone_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def delete_linked_zone(self,
        instance_id: str,
        linked_dnszone_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Delete a linked zone.

        Delete a linked zone.

        :param str instance_id: The unique identifier of a service instance.
        :param str linked_dnszone_id: The unique identifier of a linked zone.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if linked_dnszone_id is None:
            raise ValueError('linked_dnszone_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_linked_zone')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['instance_id', 'linked_dnszone_id']
        path_param_values = self.encode_path_vars(instance_id, linked_dnszone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/linked_dnszones/{linked_dnszone_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Access Requests
    #########################


    def list_dnszone_access_requests(self,
        instance_id: str,
        dnszone_id: str,
        *,
        x_correlation_id: str = None,
        offset: int = None,
        limit: int = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List Access Requests.

        List access requests in owner's instance.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param int offset: (optional) Specify how many resources to skip over, the
               default value is 0.
        :param int limit: (optional) Specify maximum resources might be returned.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AccessRequestsList` object
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
                                      operation_id='list_dnszone_access_requests')
        headers.update(sdk_headers)

        params = {
            'offset': offset,
            'limit': limit
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'dnszone_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/access_requests'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def get_dnszone_access_request(self,
        instance_id: str,
        dnszone_id: str,
        request_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get an access request.

        Get details of an access request.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str request_id: The unique identifier of an access request.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AccessRequest` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if dnszone_id is None:
            raise ValueError('dnszone_id must be provided')
        if request_id is None:
            raise ValueError('request_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_dnszone_access_request')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'dnszone_id', 'request_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id, request_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/access_requests/{request_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def update_dnszone_access_request(self,
        instance_id: str,
        dnszone_id: str,
        request_id: str,
        *,
        action: str = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Update an access request.

        Update the state of an access request.

        :param str instance_id: The unique identifier of a service instance.
        :param str dnszone_id: The unique identifier of a DNS zone.
        :param str request_id: The unique identifier of an access request.
        :param str action: (optional) The action applies to the access request.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AccessRequest` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if dnszone_id is None:
            raise ValueError('dnszone_id must be provided')
        if request_id is None:
            raise ValueError('request_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='update_dnszone_access_request')
        headers.update(sdk_headers)

        data = {
            'action': action
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'dnszone_id', 'request_id']
        path_param_values = self.encode_path_vars(instance_id, dnszone_id, request_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/dnszones/{dnszone_id}/access_requests/{request_id}'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Permitted Network for Linked Zone
    #########################


    def list_linked_permitted_networks(self,
        instance_id: str,
        linked_dnszone_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List permitted networks.

        List the permitted networks for a linked zone.

        :param str instance_id: The unique identifier of a service instance.
        :param str linked_dnszone_id: The unique identifier of a linked zone.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListPermittedNetworks` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if linked_dnszone_id is None:
            raise ValueError('linked_dnszone_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_linked_permitted_networks')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'linked_dnszone_id']
        path_param_values = self.encode_path_vars(instance_id, linked_dnszone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/linked_dnszones/{linked_dnszone_id}/permitted_networks'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def create_lz_permitted_network(self,
        instance_id: str,
        linked_dnszone_id: str,
        *,
        type: str = None,
        permitted_network: 'PermittedNetworkVpc' = None,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Create a permitted network.

        Create a permitted network for a linked zone.

        :param str instance_id: The unique identifier of a service instance.
        :param str linked_dnszone_id: The unique identifier of a linked zone.
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
        if linked_dnszone_id is None:
            raise ValueError('linked_dnszone_id must be provided')
        if permitted_network is not None:
            permitted_network = convert_model(permitted_network)
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_lz_permitted_network')
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
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'linked_dnszone_id']
        path_param_values = self.encode_path_vars(instance_id, linked_dnszone_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/linked_dnszones/{linked_dnszone_id}/permitted_networks'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def delete_lz_permitted_network(self,
        instance_id: str,
        linked_dnszone_id: str,
        permitted_network_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Remove a permitted network.

        Remove a permitted network from a linked zone.

        :param str instance_id: The unique identifier of a service instance.
        :param str linked_dnszone_id: The unique identifier of a linked zone.
        :param str permitted_network_id: The unique identifier of a permitted
               network.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PermittedNetwork` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if linked_dnszone_id is None:
            raise ValueError('linked_dnszone_id must be provided')
        if permitted_network_id is None:
            raise ValueError('permitted_network_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_lz_permitted_network')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'linked_dnszone_id', 'permitted_network_id']
        path_param_values = self.encode_path_vars(instance_id, linked_dnszone_id, permitted_network_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/linked_dnszones/{linked_dnszone_id}/permitted_networks/{permitted_network_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_linked_permitted_network(self,
        instance_id: str,
        linked_dnszone_id: str,
        permitted_network_id: str,
        *,
        x_correlation_id: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Get a permitted network.

        Get a permitted network of a linked zone.

        :param str instance_id: The unique identifier of a service instance.
        :param str linked_dnszone_id: The unique identifier of a linked zone.
        :param str permitted_network_id: The unique identifier of a permitted
               network.
        :param str x_correlation_id: (optional) Uniquely identifying a request.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `PermittedNetwork` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if linked_dnszone_id is None:
            raise ValueError('linked_dnszone_id must be provided')
        if permitted_network_id is None:
            raise ValueError('permitted_network_id must be provided')
        headers = {
            'X-Correlation-ID': x_correlation_id
        }
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='get_linked_permitted_network')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'linked_dnszone_id', 'permitted_network_id']
        path_param_values = self.encode_path_vars(instance_id, linked_dnszone_id, permitted_network_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/instances/{instance_id}/linked_dnszones/{linked_dnszone_id}/permitted_networks/{permitted_network_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


##############################################################################
# Models
##############################################################################


class AccessRequestRequestor():
    """
    The information of requestor.

    :attr str account_id: (optional) The account ID of requestor.
    :attr str instance_id: (optional) The requestor's DNS service instance ID.
    :attr str linked_zone_id: (optional) The requestor's linked zone ID.
    """

    def __init__(self,
                 *,
                 account_id: str = None,
                 instance_id: str = None,
                 linked_zone_id: str = None) -> None:
        """
        Initialize a AccessRequestRequestor object.

        :param str account_id: (optional) The account ID of requestor.
        :param str instance_id: (optional) The requestor's DNS service instance ID.
        :param str linked_zone_id: (optional) The requestor's linked zone ID.
        """
        self.account_id = account_id
        self.instance_id = instance_id
        self.linked_zone_id = linked_zone_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AccessRequestRequestor':
        """Initialize a AccessRequestRequestor object from a json dictionary."""
        args = {}
        if 'account_id' in _dict:
            args['account_id'] = _dict.get('account_id')
        if 'instance_id' in _dict:
            args['instance_id'] = _dict.get('instance_id')
        if 'linked_zone_id' in _dict:
            args['linked_zone_id'] = _dict.get('linked_zone_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AccessRequestRequestor object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'account_id') and self.account_id is not None:
            _dict['account_id'] = self.account_id
        if hasattr(self, 'instance_id') and self.instance_id is not None:
            _dict['instance_id'] = self.instance_id
        if hasattr(self, 'linked_zone_id') and self.linked_zone_id is not None:
            _dict['linked_zone_id'] = self.linked_zone_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AccessRequestRequestor object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AccessRequestRequestor') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AccessRequestRequestor') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class LinkedDnszoneLinkedTo():
    """
    The owner's instance and zone that the zone is linked to.

    :attr str instance_crn: (optional) The owner's instance CRN.
    :attr str zone_id: (optional) The owner's DNS zone.
    """

    def __init__(self,
                 *,
                 instance_crn: str = None,
                 zone_id: str = None) -> None:
        """
        Initialize a LinkedDnszoneLinkedTo object.

        :param str instance_crn: (optional) The owner's instance CRN.
        :param str zone_id: (optional) The owner's DNS zone.
        """
        self.instance_crn = instance_crn
        self.zone_id = zone_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LinkedDnszoneLinkedTo':
        """Initialize a LinkedDnszoneLinkedTo object from a json dictionary."""
        args = {}
        if 'instance_crn' in _dict:
            args['instance_crn'] = _dict.get('instance_crn')
        if 'zone_id' in _dict:
            args['zone_id'] = _dict.get('zone_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LinkedDnszoneLinkedTo object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'instance_crn') and self.instance_crn is not None:
            _dict['instance_crn'] = self.instance_crn
        if hasattr(self, 'zone_id') and self.zone_id is not None:
            _dict['zone_id'] = self.zone_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LinkedDnszoneLinkedTo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LinkedDnszoneLinkedTo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LinkedDnszoneLinkedTo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

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

class PoolHealthcheckVsisItem():
    """
    PoolHealthcheckVsisItem.

    :attr str subnet: (optional) Health check VSI subnet CRN.
    :attr str ipv4_address: (optional) healthcheck VSI ip address.
    :attr str ipv4_cidr_block: (optional) ipv4 cidr block.
    :attr str vpc: (optional) vpc crn.
    """

    def __init__(self,
                 *,
                 subnet: str = None,
                 ipv4_address: str = None,
                 ipv4_cidr_block: str = None,
                 vpc: str = None) -> None:
        """
        Initialize a PoolHealthcheckVsisItem object.

        :param str subnet: (optional) Health check VSI subnet CRN.
        :param str ipv4_address: (optional) healthcheck VSI ip address.
        :param str ipv4_cidr_block: (optional) ipv4 cidr block.
        :param str vpc: (optional) vpc crn.
        """
        self.subnet = subnet
        self.ipv4_address = ipv4_address
        self.ipv4_cidr_block = ipv4_cidr_block
        self.vpc = vpc

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PoolHealthcheckVsisItem':
        """Initialize a PoolHealthcheckVsisItem object from a json dictionary."""
        args = {}
        if 'subnet' in _dict:
            args['subnet'] = _dict.get('subnet')
        if 'ipv4_address' in _dict:
            args['ipv4_address'] = _dict.get('ipv4_address')
        if 'ipv4_cidr_block' in _dict:
            args['ipv4_cidr_block'] = _dict.get('ipv4_cidr_block')
        if 'vpc' in _dict:
            args['vpc'] = _dict.get('vpc')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PoolHealthcheckVsisItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'subnet') and self.subnet is not None:
            _dict['subnet'] = self.subnet
        if hasattr(self, 'ipv4_address') and self.ipv4_address is not None:
            _dict['ipv4_address'] = self.ipv4_address
        if hasattr(self, 'ipv4_cidr_block') and self.ipv4_cidr_block is not None:
            _dict['ipv4_cidr_block'] = self.ipv4_cidr_block
        if hasattr(self, 'vpc') and self.vpc is not None:
            _dict['vpc'] = self.vpc
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this PoolHealthcheckVsisItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PoolHealthcheckVsisItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PoolHealthcheckVsisItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RecordsImportErrorModelError():
    """
    Error container.

    :attr str code: Internal service error when DNS resource created fails by
          internal error.
    :attr str message: An internal error occurred. Try again later.
    """

    def __init__(self,
                 code: str,
                 message: str) -> None:
        """
        Initialize a RecordsImportErrorModelError object.

        :param str code: Internal service error when DNS resource created fails by
               internal error.
        :param str message: An internal error occurred. Try again later.
        """
        self.code = code
        self.message = message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RecordsImportErrorModelError':
        """Initialize a RecordsImportErrorModelError object from a json dictionary."""
        args = {}
        if 'code' in _dict:
            args['code'] = _dict.get('code')
        else:
            raise ValueError('Required property \'code\' not present in RecordsImportErrorModelError JSON')
        if 'message' in _dict:
            args['message'] = _dict.get('message')
        else:
            raise ValueError('Required property \'message\' not present in RecordsImportErrorModelError JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RecordsImportErrorModelError object from a json dictionary."""
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
        """Return a `str` version of this RecordsImportErrorModelError object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RecordsImportErrorModelError') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RecordsImportErrorModelError') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

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

class AccessRequest():
    """
    Access request.

    :attr str id: Access request ID.
    :attr AccessRequestRequestor requestor: The information of requestor.
    :attr str zone_id: The zone ID that requestor requests access for.
    :attr str zone_name: The zone name that requestor requests access for.
    :attr str state: The state of the access request.
    :attr str pending_expires_at: (optional) The expired time of access request with
          state `pending`.
    :attr str created_on: (optional) The time when the linked zone is created.
    :attr str modified_on: (optional) The recent time when the linked zone is
          modified.
    """

    def __init__(self,
                 id: str,
                 requestor: 'AccessRequestRequestor',
                 zone_id: str,
                 zone_name: str,
                 state: str,
                 *,
                 pending_expires_at: str = None,
                 created_on: str = None,
                 modified_on: str = None) -> None:
        """
        Initialize a AccessRequest object.

        :param str id: Access request ID.
        :param AccessRequestRequestor requestor: The information of requestor.
        :param str zone_id: The zone ID that requestor requests access for.
        :param str zone_name: The zone name that requestor requests access for.
        :param str state: The state of the access request.
        :param str pending_expires_at: (optional) The expired time of access
               request with state `pending`.
        :param str created_on: (optional) The time when the linked zone is created.
        :param str modified_on: (optional) The recent time when the linked zone is
               modified.
        """
        self.id = id
        self.requestor = requestor
        self.zone_id = zone_id
        self.zone_name = zone_name
        self.state = state
        self.pending_expires_at = pending_expires_at
        self.created_on = created_on
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AccessRequest':
        """Initialize a AccessRequest object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in AccessRequest JSON')
        if 'requestor' in _dict:
            args['requestor'] = AccessRequestRequestor.from_dict(_dict.get('requestor'))
        else:
            raise ValueError('Required property \'requestor\' not present in AccessRequest JSON')
        if 'zone_id' in _dict:
            args['zone_id'] = _dict.get('zone_id')
        else:
            raise ValueError('Required property \'zone_id\' not present in AccessRequest JSON')
        if 'zone_name' in _dict:
            args['zone_name'] = _dict.get('zone_name')
        else:
            raise ValueError('Required property \'zone_name\' not present in AccessRequest JSON')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        else:
            raise ValueError('Required property \'state\' not present in AccessRequest JSON')
        if 'pending_expires_at' in _dict:
            args['pending_expires_at'] = _dict.get('pending_expires_at')
        if 'created_on' in _dict:
            args['created_on'] = _dict.get('created_on')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AccessRequest object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'requestor') and self.requestor is not None:
            _dict['requestor'] = self.requestor.to_dict()
        if hasattr(self, 'zone_id') and self.zone_id is not None:
            _dict['zone_id'] = self.zone_id
        if hasattr(self, 'zone_name') and self.zone_name is not None:
            _dict['zone_name'] = self.zone_name
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'pending_expires_at') and self.pending_expires_at is not None:
            _dict['pending_expires_at'] = self.pending_expires_at
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = self.created_on
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = self.modified_on
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AccessRequest object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AccessRequest') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AccessRequest') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        The state of the access request.
        """
        PENDING = 'PENDING'
        APPROVED = 'APPROVED'
        REJECTED = 'REJECTED'
        REVOKED = 'REVOKED'
        TIMEDOUT = 'TIMEDOUT'


class AccessRequestsList():
    """
    The list of access requests.

    :attr List[AccessRequest] access_requests: The list of access requests.
    :attr int offset: The number of resources to skip over.
    :attr int limit: The maximum number of resources might be returned.
    :attr int count: The number of resources are returned.
    :attr int total_count: Total number of resources.
    :attr PaginationRef first: (optional) href.
    :attr PaginationRef last: (optional) href.
    :attr PaginationRef previous: (optional) href.
    :attr PaginationRef next: (optional) href.
    """

    def __init__(self,
                 access_requests: List['AccessRequest'],
                 offset: int,
                 limit: int,
                 count: int,
                 total_count: int,
                 *,
                 first: 'PaginationRef' = None,
                 last: 'PaginationRef' = None,
                 previous: 'PaginationRef' = None,
                 next: 'PaginationRef' = None) -> None:
        """
        Initialize a AccessRequestsList object.

        :param List[AccessRequest] access_requests: The list of access requests.
        :param int offset: The number of resources to skip over.
        :param int limit: The maximum number of resources might be returned.
        :param int count: The number of resources are returned.
        :param int total_count: Total number of resources.
        :param PaginationRef first: (optional) href.
        :param PaginationRef last: (optional) href.
        :param PaginationRef previous: (optional) href.
        :param PaginationRef next: (optional) href.
        """
        self.access_requests = access_requests
        self.offset = offset
        self.limit = limit
        self.count = count
        self.total_count = total_count
        self.first = first
        self.last = last
        self.previous = previous
        self.next = next

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AccessRequestsList':
        """Initialize a AccessRequestsList object from a json dictionary."""
        args = {}
        if 'access_requests' in _dict:
            args['access_requests'] = [AccessRequest.from_dict(x) for x in _dict.get('access_requests')]
        else:
            raise ValueError('Required property \'access_requests\' not present in AccessRequestsList JSON')
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        else:
            raise ValueError('Required property \'offset\' not present in AccessRequestsList JSON')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in AccessRequestsList JSON')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        else:
            raise ValueError('Required property \'count\' not present in AccessRequestsList JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in AccessRequestsList JSON')
        if 'first' in _dict:
            args['first'] = PaginationRef.from_dict(_dict.get('first'))
        if 'last' in _dict:
            args['last'] = PaginationRef.from_dict(_dict.get('last'))
        if 'previous' in _dict:
            args['previous'] = PaginationRef.from_dict(_dict.get('previous'))
        if 'next' in _dict:
            args['next'] = PaginationRef.from_dict(_dict.get('next'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AccessRequestsList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'access_requests') and self.access_requests is not None:
            _dict['access_requests'] = [x.to_dict() for x in self.access_requests]
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
        if hasattr(self, 'last') and self.last is not None:
            _dict['last'] = self.last.to_dict()
        if hasattr(self, 'previous') and self.previous is not None:
            _dict['previous'] = self.previous.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            _dict['next'] = self.next.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AccessRequestsList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AccessRequestsList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AccessRequestsList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class CustomResolver():
    """
    custom resolver details.

    :attr str id: (optional) Identifier of the custom resolver.
    :attr str name: (optional) Name of the custom resolver.
    :attr str description: (optional) Descriptive text of the custom resolver.
    :attr bool enabled: (optional) Whether the custom resolver is enabled.
    :attr str health: (optional) Healthy state of the custom resolver.
    :attr List[Location] locations: (optional) Locations on which the custom
          resolver will be running.
    :attr str created_on: (optional) the time when a custom resolver is created,
          RFC3339 format.
    :attr str modified_on: (optional) the recent time when a custom resolver is
          modified, RFC3339 format.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 name: str = None,
                 description: str = None,
                 enabled: bool = None,
                 health: str = None,
                 locations: List['Location'] = None,
                 created_on: str = None,
                 modified_on: str = None) -> None:
        """
        Initialize a CustomResolver object.

        :param str id: (optional) Identifier of the custom resolver.
        :param str name: (optional) Name of the custom resolver.
        :param str description: (optional) Descriptive text of the custom resolver.
        :param bool enabled: (optional) Whether the custom resolver is enabled.
        :param str health: (optional) Healthy state of the custom resolver.
        :param List[Location] locations: (optional) Locations on which the custom
               resolver will be running.
        :param str created_on: (optional) the time when a custom resolver is
               created, RFC3339 format.
        :param str modified_on: (optional) the recent time when a custom resolver
               is modified, RFC3339 format.
        """
        self.id = id
        self.name = name
        self.description = description
        self.enabled = enabled
        self.health = health
        self.locations = locations
        self.created_on = created_on
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CustomResolver':
        """Initialize a CustomResolver object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'health' in _dict:
            args['health'] = _dict.get('health')
        if 'locations' in _dict:
            args['locations'] = [Location.from_dict(x) for x in _dict.get('locations')]
        if 'created_on' in _dict:
            args['created_on'] = _dict.get('created_on')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CustomResolver object from a json dictionary."""
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
        if hasattr(self, 'health') and self.health is not None:
            _dict['health'] = self.health
        if hasattr(self, 'locations') and self.locations is not None:
            _dict['locations'] = [x.to_dict() for x in self.locations]
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = self.created_on
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = self.modified_on
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CustomResolver object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CustomResolver') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CustomResolver') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class HealthEnum(str, Enum):
        """
        Healthy state of the custom resolver.
        """
        HEALTHY = 'HEALTHY'
        DEGRADED = 'DEGRADED'
        CRITICAL = 'CRITICAL'


class CustomResolverList():
    """
    List custom resolvers response.

    :attr List[CustomResolver] custom_resolvers: (optional) An array of custom
          resolvers.
    """

    def __init__(self,
                 *,
                 custom_resolvers: List['CustomResolver'] = None) -> None:
        """
        Initialize a CustomResolverList object.

        :param List[CustomResolver] custom_resolvers: (optional) An array of custom
               resolvers.
        """
        self.custom_resolvers = custom_resolvers

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CustomResolverList':
        """Initialize a CustomResolverList object from a json dictionary."""
        args = {}
        if 'custom_resolvers' in _dict:
            args['custom_resolvers'] = [CustomResolver.from_dict(x) for x in _dict.get('custom_resolvers')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CustomResolverList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'custom_resolvers') and self.custom_resolvers is not None:
            _dict['custom_resolvers'] = [x.to_dict() for x in self.custom_resolvers]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CustomResolverList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CustomResolverList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CustomResolverList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Dnszone():
    """
    DNS zone details.

    :attr str id: (optional) Unique identifier of a DNS zone.
    :attr str created_on: (optional) the time when a DNS zone is created.
    :attr str modified_on: (optional) the recent time when a DNS zone is modified.
    :attr str instance_id: (optional) Unique identifier of a service instance.
    :attr str name: (optional) Name of DNS zone.
    :attr str description: (optional) The text describing the purpose of a DNS zone.
    :attr str state: (optional) State of DNS zone.
    :attr str label: (optional) The label of a DNS zone.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 created_on: str = None,
                 modified_on: str = None,
                 instance_id: str = None,
                 name: str = None,
                 description: str = None,
                 state: str = None,
                 label: str = None) -> None:
        """
        Initialize a Dnszone object.

        :param str id: (optional) Unique identifier of a DNS zone.
        :param str created_on: (optional) the time when a DNS zone is created.
        :param str modified_on: (optional) the recent time when a DNS zone is
               modified.
        :param str instance_id: (optional) Unique identifier of a service instance.
        :param str name: (optional) Name of DNS zone.
        :param str description: (optional) The text describing the purpose of a DNS
               zone.
        :param str state: (optional) State of DNS zone.
        :param str label: (optional) The label of a DNS zone.
        """
        self.id = id
        self.created_on = created_on
        self.modified_on = modified_on
        self.instance_id = instance_id
        self.name = name
        self.description = description
        self.state = state
        self.label = label

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Dnszone':
        """Initialize a Dnszone object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'created_on' in _dict:
            args['created_on'] = _dict.get('created_on')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        if 'instance_id' in _dict:
            args['instance_id'] = _dict.get('instance_id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'label' in _dict:
            args['label'] = _dict.get('label')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Dnszone object from a json dictionary."""
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
        if hasattr(self, 'instance_id') and self.instance_id is not None:
            _dict['instance_id'] = self.instance_id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Dnszone object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Dnszone') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Dnszone') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        State of DNS zone.
        """
        PENDING_NETWORK_ADD = 'pending_network_add'
        ACTIVE = 'active'
        DISABLED = 'disabled'
        PENDING_DELETE = 'pending_delete'
        DELETED = 'deleted'


class ForwardingRule():
    """
    forwarding rule details.

    :attr str id: (optional) Identifier of the forwarding rule.
    :attr str description: (optional) Descriptive text of the forwarding rule.
    :attr str type: (optional) Type of the forwarding rule.
    :attr str match: (optional) The matching zone or hostname.
    :attr List[str] forward_to: (optional) The upstream DNS servers will be
          forwarded to.
    :attr str created_on: (optional) the time when a forwarding rule is created,
          RFC3339 format.
    :attr str modified_on: (optional) the recent time when a forwarding rule is
          modified, RFC3339 format.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 description: str = None,
                 type: str = None,
                 match: str = None,
                 forward_to: List[str] = None,
                 created_on: str = None,
                 modified_on: str = None) -> None:
        """
        Initialize a ForwardingRule object.

        :param str id: (optional) Identifier of the forwarding rule.
        :param str description: (optional) Descriptive text of the forwarding rule.
        :param str type: (optional) Type of the forwarding rule.
        :param str match: (optional) The matching zone or hostname.
        :param List[str] forward_to: (optional) The upstream DNS servers will be
               forwarded to.
        :param str created_on: (optional) the time when a forwarding rule is
               created, RFC3339 format.
        :param str modified_on: (optional) the recent time when a forwarding rule
               is modified, RFC3339 format.
        """
        self.id = id
        self.description = description
        self.type = type
        self.match = match
        self.forward_to = forward_to
        self.created_on = created_on
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ForwardingRule':
        """Initialize a ForwardingRule object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'match' in _dict:
            args['match'] = _dict.get('match')
        if 'forward_to' in _dict:
            args['forward_to'] = _dict.get('forward_to')
        if 'created_on' in _dict:
            args['created_on'] = _dict.get('created_on')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ForwardingRule object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'match') and self.match is not None:
            _dict['match'] = self.match
        if hasattr(self, 'forward_to') and self.forward_to is not None:
            _dict['forward_to'] = self.forward_to
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = self.created_on
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = self.modified_on
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ForwardingRule object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ForwardingRule') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ForwardingRule') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Type of the forwarding rule.
        """
        ZONE = 'zone'
        DEFAULT = 'default'


class ForwardingRuleList():
    """
    List of forwarding rules.

    :attr List[ForwardingRule] forwarding_rules: (optional) An array of forwarding
          rules.
    """

    def __init__(self,
                 *,
                 forwarding_rules: List['ForwardingRule'] = None) -> None:
        """
        Initialize a ForwardingRuleList object.

        :param List[ForwardingRule] forwarding_rules: (optional) An array of
               forwarding rules.
        """
        self.forwarding_rules = forwarding_rules

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ForwardingRuleList':
        """Initialize a ForwardingRuleList object from a json dictionary."""
        args = {}
        if 'forwarding_rules' in _dict:
            args['forwarding_rules'] = [ForwardingRule.from_dict(x) for x in _dict.get('forwarding_rules')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ForwardingRuleList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'forwarding_rules') and self.forwarding_rules is not None:
            _dict['forwarding_rules'] = [x.to_dict() for x in self.forwarding_rules]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ForwardingRuleList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ForwardingRuleList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ForwardingRuleList') -> bool:
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

class ImportResourceRecordsResp():
    """
    Import DNS records response.

    :attr int total_records_parsed: Number of records parsed from the zone file.
    :attr int records_added: Number of records imported successfully.
    :attr int records_failed: Number of records failed import.
    :attr RecordStatsByType records_added_by_type: Number of records classified by
          type.
    :attr RecordStatsByType records_failed_by_type: Number of records classified by
          type.
    :attr List[RecordsImportMessageModel] messages: (optional) Error messages.
    :attr List[RecordsImportErrorModel] errors: (optional) Number of records parsed
          from the zone file.
    """

    def __init__(self,
                 total_records_parsed: int,
                 records_added: int,
                 records_failed: int,
                 records_added_by_type: 'RecordStatsByType',
                 records_failed_by_type: 'RecordStatsByType',
                 *,
                 messages: List['RecordsImportMessageModel'] = None,
                 errors: List['RecordsImportErrorModel'] = None) -> None:
        """
        Initialize a ImportResourceRecordsResp object.

        :param int total_records_parsed: Number of records parsed from the zone
               file.
        :param int records_added: Number of records imported successfully.
        :param int records_failed: Number of records failed import.
        :param RecordStatsByType records_added_by_type: Number of records
               classified by type.
        :param RecordStatsByType records_failed_by_type: Number of records
               classified by type.
        :param List[RecordsImportMessageModel] messages: (optional) Error messages.
        :param List[RecordsImportErrorModel] errors: (optional) Number of records
               parsed from the zone file.
        """
        self.total_records_parsed = total_records_parsed
        self.records_added = records_added
        self.records_failed = records_failed
        self.records_added_by_type = records_added_by_type
        self.records_failed_by_type = records_failed_by_type
        self.messages = messages
        self.errors = errors

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ImportResourceRecordsResp':
        """Initialize a ImportResourceRecordsResp object from a json dictionary."""
        args = {}
        if 'total_records_parsed' in _dict:
            args['total_records_parsed'] = _dict.get('total_records_parsed')
        else:
            raise ValueError('Required property \'total_records_parsed\' not present in ImportResourceRecordsResp JSON')
        if 'records_added' in _dict:
            args['records_added'] = _dict.get('records_added')
        else:
            raise ValueError('Required property \'records_added\' not present in ImportResourceRecordsResp JSON')
        if 'records_failed' in _dict:
            args['records_failed'] = _dict.get('records_failed')
        else:
            raise ValueError('Required property \'records_failed\' not present in ImportResourceRecordsResp JSON')
        if 'records_added_by_type' in _dict:
            args['records_added_by_type'] = RecordStatsByType.from_dict(_dict.get('records_added_by_type'))
        else:
            raise ValueError('Required property \'records_added_by_type\' not present in ImportResourceRecordsResp JSON')
        if 'records_failed_by_type' in _dict:
            args['records_failed_by_type'] = RecordStatsByType.from_dict(_dict.get('records_failed_by_type'))
        else:
            raise ValueError('Required property \'records_failed_by_type\' not present in ImportResourceRecordsResp JSON')
        if 'messages' in _dict:
            args['messages'] = [RecordsImportMessageModel.from_dict(x) for x in _dict.get('messages')]
        if 'errors' in _dict:
            args['errors'] = [RecordsImportErrorModel.from_dict(x) for x in _dict.get('errors')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ImportResourceRecordsResp object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'total_records_parsed') and self.total_records_parsed is not None:
            _dict['total_records_parsed'] = self.total_records_parsed
        if hasattr(self, 'records_added') and self.records_added is not None:
            _dict['records_added'] = self.records_added
        if hasattr(self, 'records_failed') and self.records_failed is not None:
            _dict['records_failed'] = self.records_failed
        if hasattr(self, 'records_added_by_type') and self.records_added_by_type is not None:
            _dict['records_added_by_type'] = self.records_added_by_type.to_dict()
        if hasattr(self, 'records_failed_by_type') and self.records_failed_by_type is not None:
            _dict['records_failed_by_type'] = self.records_failed_by_type.to_dict()
        if hasattr(self, 'messages') and self.messages is not None:
            _dict['messages'] = [x.to_dict() for x in self.messages]
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = [x.to_dict() for x in self.errors]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ImportResourceRecordsResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ImportResourceRecordsResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ImportResourceRecordsResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class LinkedDnszone():
    """
    linked zone details.

    :attr str id: Identifier of the linked zone.
    :attr str instance_id: Unique identifier of a service instance.
    :attr str name: Name of owner's DNS zone.
    :attr str description: (optional) Descriptive text of the linked zone.
    :attr LinkedDnszoneLinkedTo linked_to: The owner's instance and zone that the
          zone is linked to.
    :attr str state: The state of linked zone.
    :attr str label: (optional) The label of linked zone.
    :attr str approval_required_before: (optional) The expired time of linked zone
          with state `approval pending`.
    :attr str created_on: (optional) The time when the linked zone is created.
    :attr str modified_on: (optional) The recent time when the linked zone is
          modified.
    """

    def __init__(self,
                 id: str,
                 instance_id: str,
                 name: str,
                 linked_to: 'LinkedDnszoneLinkedTo',
                 state: str,
                 *,
                 description: str = None,
                 label: str = None,
                 approval_required_before: str = None,
                 created_on: str = None,
                 modified_on: str = None) -> None:
        """
        Initialize a LinkedDnszone object.

        :param str id: Identifier of the linked zone.
        :param str instance_id: Unique identifier of a service instance.
        :param str name: Name of owner's DNS zone.
        :param LinkedDnszoneLinkedTo linked_to: The owner's instance and zone that
               the zone is linked to.
        :param str state: The state of linked zone.
        :param str description: (optional) Descriptive text of the linked zone.
        :param str label: (optional) The label of linked zone.
        :param str approval_required_before: (optional) The expired time of linked
               zone with state `approval pending`.
        :param str created_on: (optional) The time when the linked zone is created.
        :param str modified_on: (optional) The recent time when the linked zone is
               modified.
        """
        self.id = id
        self.instance_id = instance_id
        self.name = name
        self.description = description
        self.linked_to = linked_to
        self.state = state
        self.label = label
        self.approval_required_before = approval_required_before
        self.created_on = created_on
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LinkedDnszone':
        """Initialize a LinkedDnszone object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in LinkedDnszone JSON')
        if 'instance_id' in _dict:
            args['instance_id'] = _dict.get('instance_id')
        else:
            raise ValueError('Required property \'instance_id\' not present in LinkedDnszone JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in LinkedDnszone JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'linked_to' in _dict:
            args['linked_to'] = LinkedDnszoneLinkedTo.from_dict(_dict.get('linked_to'))
        else:
            raise ValueError('Required property \'linked_to\' not present in LinkedDnszone JSON')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        else:
            raise ValueError('Required property \'state\' not present in LinkedDnszone JSON')
        if 'label' in _dict:
            args['label'] = _dict.get('label')
        if 'approval_required_before' in _dict:
            args['approval_required_before'] = _dict.get('approval_required_before')
        if 'created_on' in _dict:
            args['created_on'] = _dict.get('created_on')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LinkedDnszone object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'instance_id') and self.instance_id is not None:
            _dict['instance_id'] = self.instance_id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'linked_to') and self.linked_to is not None:
            _dict['linked_to'] = self.linked_to.to_dict()
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label
        if hasattr(self, 'approval_required_before') and self.approval_required_before is not None:
            _dict['approval_required_before'] = self.approval_required_before
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = self.created_on
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = self.modified_on
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LinkedDnszone object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LinkedDnszone') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LinkedDnszone') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        The state of linked zone.
        """
        PENDING_APPROVAL = 'PENDING_APPROVAL'
        PENDING_NETWORK_ADD = 'PENDING_NETWORK_ADD'
        ACTIVE = 'ACTIVE'
        APPROVAL_REJECTED = 'APPROVAL_REJECTED'
        APPROVAL_TIMEDOUT = 'APPROVAL_TIMEDOUT'
        APPROVAL_REVOKED = 'APPROVAL_REVOKED'


class LinkedDnszonesList():
    """
    The list of linked zones.

    :attr List[LinkedDnszone] linked_dnszones: The list of linked zones.
    :attr int offset: The number of resources to skip over.
    :attr int limit: The maximum number of resources might be returned.
    :attr int count: The number of resources are returned.
    :attr int total_count: Total number of resources.
    :attr PaginationRef first: (optional) href.
    :attr PaginationRef last: (optional) href.
    :attr PaginationRef previous: (optional) href.
    :attr PaginationRef next: (optional) href.
    """

    def __init__(self,
                 linked_dnszones: List['LinkedDnszone'],
                 offset: int,
                 limit: int,
                 count: int,
                 total_count: int,
                 *,
                 first: 'PaginationRef' = None,
                 last: 'PaginationRef' = None,
                 previous: 'PaginationRef' = None,
                 next: 'PaginationRef' = None) -> None:
        """
        Initialize a LinkedDnszonesList object.

        :param List[LinkedDnszone] linked_dnszones: The list of linked zones.
        :param int offset: The number of resources to skip over.
        :param int limit: The maximum number of resources might be returned.
        :param int count: The number of resources are returned.
        :param int total_count: Total number of resources.
        :param PaginationRef first: (optional) href.
        :param PaginationRef last: (optional) href.
        :param PaginationRef previous: (optional) href.
        :param PaginationRef next: (optional) href.
        """
        self.linked_dnszones = linked_dnszones
        self.offset = offset
        self.limit = limit
        self.count = count
        self.total_count = total_count
        self.first = first
        self.last = last
        self.previous = previous
        self.next = next

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LinkedDnszonesList':
        """Initialize a LinkedDnszonesList object from a json dictionary."""
        args = {}
        if 'linked_dnszones' in _dict:
            args['linked_dnszones'] = [LinkedDnszone.from_dict(x) for x in _dict.get('linked_dnszones')]
        else:
            raise ValueError('Required property \'linked_dnszones\' not present in LinkedDnszonesList JSON')
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        else:
            raise ValueError('Required property \'offset\' not present in LinkedDnszonesList JSON')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in LinkedDnszonesList JSON')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        else:
            raise ValueError('Required property \'count\' not present in LinkedDnszonesList JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in LinkedDnszonesList JSON')
        if 'first' in _dict:
            args['first'] = PaginationRef.from_dict(_dict.get('first'))
        if 'last' in _dict:
            args['last'] = PaginationRef.from_dict(_dict.get('last'))
        if 'previous' in _dict:
            args['previous'] = PaginationRef.from_dict(_dict.get('previous'))
        if 'next' in _dict:
            args['next'] = PaginationRef.from_dict(_dict.get('next'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LinkedDnszonesList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'linked_dnszones') and self.linked_dnszones is not None:
            _dict['linked_dnszones'] = [x.to_dict() for x in self.linked_dnszones]
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
        if hasattr(self, 'last') and self.last is not None:
            _dict['last'] = self.last.to_dict()
        if hasattr(self, 'previous') and self.previous is not None:
            _dict['previous'] = self.previous.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            _dict['next'] = self.next.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LinkedDnszonesList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LinkedDnszonesList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LinkedDnszonesList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListDnszones():
    """
    List DNS zones response.

    :attr List[Dnszone] dnszones: An array of DNS zones.
    :attr int offset: The number of resources to skip over.
    :attr int limit: The maximum number of resources might be returned.
    :attr int count: The number of resources are returned.
    :attr int total_count: Total number of resources.
    :attr PaginationRef first: href.
    :attr PaginationRef last: href.
    :attr PaginationRef previous: (optional) href.
    :attr PaginationRef next: (optional) href.
    """

    def __init__(self,
                 dnszones: List['Dnszone'],
                 offset: int,
                 limit: int,
                 count: int,
                 total_count: int,
                 first: 'PaginationRef',
                 last: 'PaginationRef',
                 *,
                 previous: 'PaginationRef' = None,
                 next: 'PaginationRef' = None) -> None:
        """
        Initialize a ListDnszones object.

        :param List[Dnszone] dnszones: An array of DNS zones.
        :param int offset: The number of resources to skip over.
        :param int limit: The maximum number of resources might be returned.
        :param int count: The number of resources are returned.
        :param int total_count: Total number of resources.
        :param PaginationRef first: href.
        :param PaginationRef last: href.
        :param PaginationRef previous: (optional) href.
        :param PaginationRef next: (optional) href.
        """
        self.dnszones = dnszones
        self.offset = offset
        self.limit = limit
        self.count = count
        self.total_count = total_count
        self.first = first
        self.last = last
        self.previous = previous
        self.next = next

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListDnszones':
        """Initialize a ListDnszones object from a json dictionary."""
        args = {}
        if 'dnszones' in _dict:
            args['dnszones'] = [Dnszone.from_dict(x) for x in _dict.get('dnszones')]
        else:
            raise ValueError('Required property \'dnszones\' not present in ListDnszones JSON')
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        else:
            raise ValueError('Required property \'offset\' not present in ListDnszones JSON')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in ListDnszones JSON')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        else:
            raise ValueError('Required property \'count\' not present in ListDnszones JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in ListDnszones JSON')
        if 'first' in _dict:
            args['first'] = PaginationRef.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in ListDnszones JSON')
        if 'last' in _dict:
            args['last'] = PaginationRef.from_dict(_dict.get('last'))
        else:
            raise ValueError('Required property \'last\' not present in ListDnszones JSON')
        if 'previous' in _dict:
            args['previous'] = PaginationRef.from_dict(_dict.get('previous'))
        if 'next' in _dict:
            args['next'] = PaginationRef.from_dict(_dict.get('next'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListDnszones object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'dnszones') and self.dnszones is not None:
            _dict['dnszones'] = [x.to_dict() for x in self.dnszones]
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
        if hasattr(self, 'last') and self.last is not None:
            _dict['last'] = self.last.to_dict()
        if hasattr(self, 'previous') and self.previous is not None:
            _dict['previous'] = self.previous.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            _dict['next'] = self.next.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListDnszones object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListDnszones') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListDnszones') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ListLoadBalancers():
    """
    List Global Load Balancers response.

    :attr List[LoadBalancer] load_balancers: An array of Global Load Balancers.
    :attr int offset: The number of resources to skip over.
    :attr int limit: The maximum number of resources might be returned.
    :attr int count: The number of resources are returned.
    :attr int total_count: Total number of resources.
    :attr PaginationRef first: href.
    :attr PaginationRef last: href.
    :attr PaginationRef previous: (optional) href.
    :attr PaginationRef next: (optional) href.
    """

    def __init__(self,
                 load_balancers: List['LoadBalancer'],
                 offset: int,
                 limit: int,
                 count: int,
                 total_count: int,
                 first: 'PaginationRef',
                 last: 'PaginationRef',
                 *,
                 previous: 'PaginationRef' = None,
                 next: 'PaginationRef' = None) -> None:
        """
        Initialize a ListLoadBalancers object.

        :param List[LoadBalancer] load_balancers: An array of Global Load
               Balancers.
        :param int offset: The number of resources to skip over.
        :param int limit: The maximum number of resources might be returned.
        :param int count: The number of resources are returned.
        :param int total_count: Total number of resources.
        :param PaginationRef first: href.
        :param PaginationRef last: href.
        :param PaginationRef previous: (optional) href.
        :param PaginationRef next: (optional) href.
        """
        self.load_balancers = load_balancers
        self.offset = offset
        self.limit = limit
        self.count = count
        self.total_count = total_count
        self.first = first
        self.last = last
        self.previous = previous
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
            args['first'] = PaginationRef.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in ListLoadBalancers JSON')
        if 'last' in _dict:
            args['last'] = PaginationRef.from_dict(_dict.get('last'))
        else:
            raise ValueError('Required property \'last\' not present in ListLoadBalancers JSON')
        if 'previous' in _dict:
            args['previous'] = PaginationRef.from_dict(_dict.get('previous'))
        if 'next' in _dict:
            args['next'] = PaginationRef.from_dict(_dict.get('next'))
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
        if hasattr(self, 'last') and self.last is not None:
            _dict['last'] = self.last.to_dict()
        if hasattr(self, 'previous') and self.previous is not None:
            _dict['previous'] = self.previous.to_dict()
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
    :attr int offset: The number of resources to skip over.
    :attr int limit: The maximum number of resources might be returned.
    :attr int count: The number of resources are returned.
    :attr int total_count: Total number of resources.
    :attr PaginationRef first: href.
    :attr PaginationRef last: href.
    :attr PaginationRef previous: (optional) href.
    :attr PaginationRef next: (optional) href.
    """

    def __init__(self,
                 monitors: List['Monitor'],
                 offset: int,
                 limit: int,
                 count: int,
                 total_count: int,
                 first: 'PaginationRef',
                 last: 'PaginationRef',
                 *,
                 previous: 'PaginationRef' = None,
                 next: 'PaginationRef' = None) -> None:
        """
        Initialize a ListMonitors object.

        :param List[Monitor] monitors: An array of load balancer monitors.
        :param int offset: The number of resources to skip over.
        :param int limit: The maximum number of resources might be returned.
        :param int count: The number of resources are returned.
        :param int total_count: Total number of resources.
        :param PaginationRef first: href.
        :param PaginationRef last: href.
        :param PaginationRef previous: (optional) href.
        :param PaginationRef next: (optional) href.
        """
        self.monitors = monitors
        self.offset = offset
        self.limit = limit
        self.count = count
        self.total_count = total_count
        self.first = first
        self.last = last
        self.previous = previous
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
            args['first'] = PaginationRef.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in ListMonitors JSON')
        if 'last' in _dict:
            args['last'] = PaginationRef.from_dict(_dict.get('last'))
        else:
            raise ValueError('Required property \'last\' not present in ListMonitors JSON')
        if 'previous' in _dict:
            args['previous'] = PaginationRef.from_dict(_dict.get('previous'))
        if 'next' in _dict:
            args['next'] = PaginationRef.from_dict(_dict.get('next'))
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
        if hasattr(self, 'last') and self.last is not None:
            _dict['last'] = self.last.to_dict()
        if hasattr(self, 'previous') and self.previous is not None:
            _dict['previous'] = self.previous.to_dict()
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

class ListPermittedNetworks():
    """
    List permitted networks response.

    :attr List[PermittedNetwork] permitted_networks: An array of permitted networks.
    """

    def __init__(self,
                 permitted_networks: List['PermittedNetwork']) -> None:
        """
        Initialize a ListPermittedNetworks object.

        :param List[PermittedNetwork] permitted_networks: An array of permitted
               networks.
        """
        self.permitted_networks = permitted_networks

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListPermittedNetworks':
        """Initialize a ListPermittedNetworks object from a json dictionary."""
        args = {}
        if 'permitted_networks' in _dict:
            args['permitted_networks'] = [PermittedNetwork.from_dict(x) for x in _dict.get('permitted_networks')]
        else:
            raise ValueError('Required property \'permitted_networks\' not present in ListPermittedNetworks JSON')
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

class ListPools():
    """
    List load balancer pools response.

    :attr List[Pool] pools: An array of load balancer pools.
    :attr int offset: The number of resources to skip over.
    :attr int limit: The maximum number of resources might be returned.
    :attr int count: The number of resources are returned.
    :attr int total_count: Total number of resources.
    :attr PaginationRef first: href.
    :attr PaginationRef last: href.
    :attr PaginationRef previous: (optional) href.
    :attr PaginationRef next: (optional) href.
    """

    def __init__(self,
                 pools: List['Pool'],
                 offset: int,
                 limit: int,
                 count: int,
                 total_count: int,
                 first: 'PaginationRef',
                 last: 'PaginationRef',
                 *,
                 previous: 'PaginationRef' = None,
                 next: 'PaginationRef' = None) -> None:
        """
        Initialize a ListPools object.

        :param List[Pool] pools: An array of load balancer pools.
        :param int offset: The number of resources to skip over.
        :param int limit: The maximum number of resources might be returned.
        :param int count: The number of resources are returned.
        :param int total_count: Total number of resources.
        :param PaginationRef first: href.
        :param PaginationRef last: href.
        :param PaginationRef previous: (optional) href.
        :param PaginationRef next: (optional) href.
        """
        self.pools = pools
        self.offset = offset
        self.limit = limit
        self.count = count
        self.total_count = total_count
        self.first = first
        self.last = last
        self.previous = previous
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
            args['first'] = PaginationRef.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in ListPools JSON')
        if 'last' in _dict:
            args['last'] = PaginationRef.from_dict(_dict.get('last'))
        else:
            raise ValueError('Required property \'last\' not present in ListPools JSON')
        if 'previous' in _dict:
            args['previous'] = PaginationRef.from_dict(_dict.get('previous'))
        if 'next' in _dict:
            args['next'] = PaginationRef.from_dict(_dict.get('next'))
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
        if hasattr(self, 'last') and self.last is not None:
            _dict['last'] = self.last.to_dict()
        if hasattr(self, 'previous') and self.previous is not None:
            _dict['previous'] = self.previous.to_dict()
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

class ListResourceRecords():
    """
    List Resource Records response.

    :attr List[ResourceRecord] resource_records: An array of resource records.
    :attr int offset: The number of resources to skip over.
    :attr int limit: The maximum number of resources might be returned.
    :attr int count: The number of resources are returned.
    :attr int total_count: Total number of resources.
    :attr PaginationRef first: href.
    :attr PaginationRef last: href.
    :attr PaginationRef previous: (optional) href.
    :attr PaginationRef next: (optional) href.
    """

    def __init__(self,
                 resource_records: List['ResourceRecord'],
                 offset: int,
                 limit: int,
                 count: int,
                 total_count: int,
                 first: 'PaginationRef',
                 last: 'PaginationRef',
                 *,
                 previous: 'PaginationRef' = None,
                 next: 'PaginationRef' = None) -> None:
        """
        Initialize a ListResourceRecords object.

        :param List[ResourceRecord] resource_records: An array of resource records.
        :param int offset: The number of resources to skip over.
        :param int limit: The maximum number of resources might be returned.
        :param int count: The number of resources are returned.
        :param int total_count: Total number of resources.
        :param PaginationRef first: href.
        :param PaginationRef last: href.
        :param PaginationRef previous: (optional) href.
        :param PaginationRef next: (optional) href.
        """
        self.resource_records = resource_records
        self.offset = offset
        self.limit = limit
        self.count = count
        self.total_count = total_count
        self.first = first
        self.last = last
        self.previous = previous
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
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        else:
            raise ValueError('Required property \'count\' not present in ListResourceRecords JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in ListResourceRecords JSON')
        if 'first' in _dict:
            args['first'] = PaginationRef.from_dict(_dict.get('first'))
        else:
            raise ValueError('Required property \'first\' not present in ListResourceRecords JSON')
        if 'last' in _dict:
            args['last'] = PaginationRef.from_dict(_dict.get('last'))
        else:
            raise ValueError('Required property \'last\' not present in ListResourceRecords JSON')
        if 'previous' in _dict:
            args['previous'] = PaginationRef.from_dict(_dict.get('previous'))
        if 'next' in _dict:
            args['next'] = PaginationRef.from_dict(_dict.get('next'))
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
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'total_count') and self.total_count is not None:
            _dict['total_count'] = self.total_count
        if hasattr(self, 'first') and self.first is not None:
            _dict['first'] = self.first.to_dict()
        if hasattr(self, 'last') and self.last is not None:
            _dict['last'] = self.last.to_dict()
        if hasattr(self, 'previous') and self.previous is not None:
            _dict['previous'] = self.previous.to_dict()
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
          to pool IDs.
    :attr str created_on: (optional) The time when a load balancer is created.
    :attr str modified_on: (optional) The recent time when a load balancer is
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
               zones to pool IDs.
        :param str created_on: (optional) The time when a load balancer is created.
        :param str modified_on: (optional) The recent time when a load balancer is
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


class Location():
    """
    Custom resolver location.

    :attr str id: (optional) Location ID.
    :attr str subnet_crn: (optional) Subnet CRN.
    :attr bool enabled: (optional) Whether the location is enabled for the custom
          resolver.
    :attr bool healthy: (optional) Whether the DNS server in this location is
          healthy or not.
    :attr str dns_server_ip: (optional) The ip address of this dns server.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 subnet_crn: str = None,
                 enabled: bool = None,
                 healthy: bool = None,
                 dns_server_ip: str = None) -> None:
        """
        Initialize a Location object.

        :param str id: (optional) Location ID.
        :param str subnet_crn: (optional) Subnet CRN.
        :param bool enabled: (optional) Whether the location is enabled for the
               custom resolver.
        :param bool healthy: (optional) Whether the DNS server in this location is
               healthy or not.
        :param str dns_server_ip: (optional) The ip address of this dns server.
        """
        self.id = id
        self.subnet_crn = subnet_crn
        self.enabled = enabled
        self.healthy = healthy
        self.dns_server_ip = dns_server_ip

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Location':
        """Initialize a Location object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'subnet_crn' in _dict:
            args['subnet_crn'] = _dict.get('subnet_crn')
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'healthy' in _dict:
            args['healthy'] = _dict.get('healthy')
        if 'dns_server_ip' in _dict:
            args['dns_server_ip'] = _dict.get('dns_server_ip')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Location object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'subnet_crn') and self.subnet_crn is not None:
            _dict['subnet_crn'] = self.subnet_crn
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'healthy') and self.healthy is not None:
            _dict['healthy'] = self.healthy
        if hasattr(self, 'dns_server_ip') and self.dns_server_ip is not None:
            _dict['dns_server_ip'] = self.dns_server_ip
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Location object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Location') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Location') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class LocationInput():
    """
    Request to add custom resolver location.

    :attr str subnet_crn: Custom resolver location, subnet CRN.
    :attr bool enabled: (optional) Enable/Disable custom resolver location.
    """

    def __init__(self,
                 subnet_crn: str,
                 *,
                 enabled: bool = None) -> None:
        """
        Initialize a LocationInput object.

        :param str subnet_crn: Custom resolver location, subnet CRN.
        :param bool enabled: (optional) Enable/Disable custom resolver location.
        """
        self.subnet_crn = subnet_crn
        self.enabled = enabled

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LocationInput':
        """Initialize a LocationInput object from a json dictionary."""
        args = {}
        if 'subnet_crn' in _dict:
            args['subnet_crn'] = _dict.get('subnet_crn')
        else:
            raise ValueError('Required property \'subnet_crn\' not present in LocationInput JSON')
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LocationInput object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'subnet_crn') and self.subnet_crn is not None:
            _dict['subnet_crn'] = self.subnet_crn
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LocationInput object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LocationInput') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LocationInput') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

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

class PaginationRef():
    """
    href.

    :attr str href: (optional) href.
    """

    def __init__(self,
                 *,
                 href: str = None) -> None:
        """
        Initialize a PaginationRef object.

        :param str href: (optional) href.
        """
        self.href = href

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'PaginationRef':
        """Initialize a PaginationRef object from a json dictionary."""
        args = {}
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a PaginationRef object from a json dictionary."""
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
        """Return a `str` version of this PaginationRef object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'PaginationRef') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'PaginationRef') -> bool:
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
    :attr List[str] healthcheck_subnets: (optional) Health check subnet CRNs.
    :attr List[PoolHealthcheckVsisItem] healthcheck_vsis: (optional) Health check
          VSI information.
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
                 healthcheck_vsis: List['PoolHealthcheckVsisItem'] = None,
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
        :param List[str] healthcheck_subnets: (optional) Health check subnet CRNs.
        :param List[PoolHealthcheckVsisItem] healthcheck_vsis: (optional) Health
               check VSI information.
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
        self.healthcheck_vsis = healthcheck_vsis
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
        if 'healthcheck_vsis' in _dict:
            args['healthcheck_vsis'] = [PoolHealthcheckVsisItem.from_dict(x) for x in _dict.get('healthcheck_vsis')]
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
        if hasattr(self, 'healthcheck_vsis') and self.healthcheck_vsis is not None:
            _dict['healthcheck_vsis'] = [x.to_dict() for x in self.healthcheck_vsis]
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


class RecordStatsByType():
    """
    Number of records classified by type.

    :attr int a: Number of records, type A.
    :attr int aaaa: Number of records, type AAAA.
    :attr int cname: Number of records, type CNAME.
    :attr int srv: Number of records, type SRV.
    :attr int txt: Number of records, type TXT.
    :attr int mx: Number of records, type MX.
    :attr int ptr: Number of records, type PTR.
    """

    def __init__(self,
                 a: int,
                 aaaa: int,
                 cname: int,
                 srv: int,
                 txt: int,
                 mx: int,
                 ptr: int) -> None:
        """
        Initialize a RecordStatsByType object.

        :param int a: Number of records, type A.
        :param int aaaa: Number of records, type AAAA.
        :param int cname: Number of records, type CNAME.
        :param int srv: Number of records, type SRV.
        :param int txt: Number of records, type TXT.
        :param int mx: Number of records, type MX.
        :param int ptr: Number of records, type PTR.
        """
        self.a = a
        self.aaaa = aaaa
        self.cname = cname
        self.srv = srv
        self.txt = txt
        self.mx = mx
        self.ptr = ptr

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RecordStatsByType':
        """Initialize a RecordStatsByType object from a json dictionary."""
        args = {}
        if 'A' in _dict:
            args['a'] = _dict.get('A')
        else:
            raise ValueError('Required property \'A\' not present in RecordStatsByType JSON')
        if 'AAAA' in _dict:
            args['aaaa'] = _dict.get('AAAA')
        else:
            raise ValueError('Required property \'AAAA\' not present in RecordStatsByType JSON')
        if 'CNAME' in _dict:
            args['cname'] = _dict.get('CNAME')
        else:
            raise ValueError('Required property \'CNAME\' not present in RecordStatsByType JSON')
        if 'SRV' in _dict:
            args['srv'] = _dict.get('SRV')
        else:
            raise ValueError('Required property \'SRV\' not present in RecordStatsByType JSON')
        if 'TXT' in _dict:
            args['txt'] = _dict.get('TXT')
        else:
            raise ValueError('Required property \'TXT\' not present in RecordStatsByType JSON')
        if 'MX' in _dict:
            args['mx'] = _dict.get('MX')
        else:
            raise ValueError('Required property \'MX\' not present in RecordStatsByType JSON')
        if 'PTR' in _dict:
            args['ptr'] = _dict.get('PTR')
        else:
            raise ValueError('Required property \'PTR\' not present in RecordStatsByType JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RecordStatsByType object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'a') and self.a is not None:
            _dict['A'] = self.a
        if hasattr(self, 'aaaa') and self.aaaa is not None:
            _dict['AAAA'] = self.aaaa
        if hasattr(self, 'cname') and self.cname is not None:
            _dict['CNAME'] = self.cname
        if hasattr(self, 'srv') and self.srv is not None:
            _dict['SRV'] = self.srv
        if hasattr(self, 'txt') and self.txt is not None:
            _dict['TXT'] = self.txt
        if hasattr(self, 'mx') and self.mx is not None:
            _dict['MX'] = self.mx
        if hasattr(self, 'ptr') and self.ptr is not None:
            _dict['PTR'] = self.ptr
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RecordStatsByType object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RecordStatsByType') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RecordStatsByType') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RecordsImportErrorModel():
    """
    RecordsImportErrorModel.

    :attr str resource_record: resource record content in zone file.
    :attr RecordsImportErrorModelError error: Error container.
    """

    def __init__(self,
                 resource_record: str,
                 error: 'RecordsImportErrorModelError') -> None:
        """
        Initialize a RecordsImportErrorModel object.

        :param str resource_record: resource record content in zone file.
        :param RecordsImportErrorModelError error: Error container.
        """
        self.resource_record = resource_record
        self.error = error

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RecordsImportErrorModel':
        """Initialize a RecordsImportErrorModel object from a json dictionary."""
        args = {}
        if 'resource_record' in _dict:
            args['resource_record'] = _dict.get('resource_record')
        else:
            raise ValueError('Required property \'resource_record\' not present in RecordsImportErrorModel JSON')
        if 'error' in _dict:
            args['error'] = RecordsImportErrorModelError.from_dict(_dict.get('error'))
        else:
            raise ValueError('Required property \'error\' not present in RecordsImportErrorModel JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RecordsImportErrorModel object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'resource_record') and self.resource_record is not None:
            _dict['resource_record'] = self.resource_record
        if hasattr(self, 'error') and self.error is not None:
            _dict['error'] = self.error.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RecordsImportErrorModel object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RecordsImportErrorModel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RecordsImportErrorModel') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class RecordsImportMessageModel():
    """
    RecordsImportMessageModel.

    :attr str code: Code to classify import DNS records error.
    :attr str message: Message to describe import DNS records error.
    """

    def __init__(self,
                 code: str,
                 message: str) -> None:
        """
        Initialize a RecordsImportMessageModel object.

        :param str code: Code to classify import DNS records error.
        :param str message: Message to describe import DNS records error.
        """
        self.code = code
        self.message = message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RecordsImportMessageModel':
        """Initialize a RecordsImportMessageModel object from a json dictionary."""
        args = {}
        if 'code' in _dict:
            args['code'] = _dict.get('code')
        else:
            raise ValueError('Required property \'code\' not present in RecordsImportMessageModel JSON')
        if 'message' in _dict:
            args['message'] = _dict.get('message')
        else:
            raise ValueError('Required property \'message\' not present in RecordsImportMessageModel JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RecordsImportMessageModel object from a json dictionary."""
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
        """Return a `str` version of this RecordsImportMessageModel object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RecordsImportMessageModel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RecordsImportMessageModel') -> bool:
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


class SecondaryZone():
    """
    Secondary zone details.

    :attr str id: Identifier of the secondary zone.
    :attr str description: (optional) Descriptive text of the secondary zone.
    :attr str zone: zone name.
    :attr bool enabled: Enable/Disable the secondary zone.
    :attr List[str] transfer_from: The addresses of DNS servers where the secondary
          zone data should be transferred from.
    :attr str created_on: (optional) The time when a secondary zone is created.
    :attr str modified_on: (optional) The recent time when a secondary zone is
          modified.
    """

    def __init__(self,
                 id: str,
                 zone: str,
                 enabled: bool,
                 transfer_from: List[str],
                 *,
                 description: str = None,
                 created_on: str = None,
                 modified_on: str = None) -> None:
        """
        Initialize a SecondaryZone object.

        :param str id: Identifier of the secondary zone.
        :param str zone: zone name.
        :param bool enabled: Enable/Disable the secondary zone.
        :param List[str] transfer_from: The addresses of DNS servers where the
               secondary zone data should be transferred from.
        :param str description: (optional) Descriptive text of the secondary zone.
        :param str created_on: (optional) The time when a secondary zone is
               created.
        :param str modified_on: (optional) The recent time when a secondary zone is
               modified.
        """
        self.id = id
        self.description = description
        self.zone = zone
        self.enabled = enabled
        self.transfer_from = transfer_from
        self.created_on = created_on
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SecondaryZone':
        """Initialize a SecondaryZone object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in SecondaryZone JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'zone' in _dict:
            args['zone'] = _dict.get('zone')
        else:
            raise ValueError('Required property \'zone\' not present in SecondaryZone JSON')
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        else:
            raise ValueError('Required property \'enabled\' not present in SecondaryZone JSON')
        if 'transfer_from' in _dict:
            args['transfer_from'] = _dict.get('transfer_from')
        else:
            raise ValueError('Required property \'transfer_from\' not present in SecondaryZone JSON')
        if 'created_on' in _dict:
            args['created_on'] = _dict.get('created_on')
        if 'modified_on' in _dict:
            args['modified_on'] = _dict.get('modified_on')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SecondaryZone object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'zone') and self.zone is not None:
            _dict['zone'] = self.zone
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'transfer_from') and self.transfer_from is not None:
            _dict['transfer_from'] = self.transfer_from
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = self.created_on
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = self.modified_on
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SecondaryZone object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SecondaryZone') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SecondaryZone') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class SecondaryZoneList():
    """
    List of secondary zones.

    :attr List[SecondaryZone] secondary_zones: Secondary zones.
    :attr int offset: The number of resources to skip over.
    :attr int limit: The maximum number of resources might be returned.
    :attr int count: The number of resources are returned.
    :attr int total_count: Total number of resources.
    :attr PaginationRef first: (optional) href.
    :attr PaginationRef last: (optional) href.
    :attr PaginationRef previous: (optional) href.
    :attr PaginationRef next: (optional) href.
    """

    def __init__(self,
                 secondary_zones: List['SecondaryZone'],
                 offset: int,
                 limit: int,
                 count: int,
                 total_count: int,
                 *,
                 first: 'PaginationRef' = None,
                 last: 'PaginationRef' = None,
                 previous: 'PaginationRef' = None,
                 next: 'PaginationRef' = None) -> None:
        """
        Initialize a SecondaryZoneList object.

        :param List[SecondaryZone] secondary_zones: Secondary zones.
        :param int offset: The number of resources to skip over.
        :param int limit: The maximum number of resources might be returned.
        :param int count: The number of resources are returned.
        :param int total_count: Total number of resources.
        :param PaginationRef first: (optional) href.
        :param PaginationRef last: (optional) href.
        :param PaginationRef previous: (optional) href.
        :param PaginationRef next: (optional) href.
        """
        self.secondary_zones = secondary_zones
        self.offset = offset
        self.limit = limit
        self.count = count
        self.total_count = total_count
        self.first = first
        self.last = last
        self.previous = previous
        self.next = next

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SecondaryZoneList':
        """Initialize a SecondaryZoneList object from a json dictionary."""
        args = {}
        if 'secondary_zones' in _dict:
            args['secondary_zones'] = [SecondaryZone.from_dict(x) for x in _dict.get('secondary_zones')]
        else:
            raise ValueError('Required property \'secondary_zones\' not present in SecondaryZoneList JSON')
        if 'offset' in _dict:
            args['offset'] = _dict.get('offset')
        else:
            raise ValueError('Required property \'offset\' not present in SecondaryZoneList JSON')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        else:
            raise ValueError('Required property \'limit\' not present in SecondaryZoneList JSON')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        else:
            raise ValueError('Required property \'count\' not present in SecondaryZoneList JSON')
        if 'total_count' in _dict:
            args['total_count'] = _dict.get('total_count')
        else:
            raise ValueError('Required property \'total_count\' not present in SecondaryZoneList JSON')
        if 'first' in _dict:
            args['first'] = PaginationRef.from_dict(_dict.get('first'))
        if 'last' in _dict:
            args['last'] = PaginationRef.from_dict(_dict.get('last'))
        if 'previous' in _dict:
            args['previous'] = PaginationRef.from_dict(_dict.get('previous'))
        if 'next' in _dict:
            args['next'] = PaginationRef.from_dict(_dict.get('next'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SecondaryZoneList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'secondary_zones') and self.secondary_zones is not None:
            _dict['secondary_zones'] = [x.to_dict() for x in self.secondary_zones]
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
        if hasattr(self, 'last') and self.last is not None:
            _dict['last'] = self.last.to_dict()
        if hasattr(self, 'previous') and self.previous is not None:
            _dict['previous'] = self.previous.to_dict()
        if hasattr(self, 'next') and self.next is not None:
            _dict['next'] = self.next.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SecondaryZoneList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SecondaryZoneList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SecondaryZoneList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

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
