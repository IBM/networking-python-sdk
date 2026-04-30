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
CIS Lists

API Version: 1.0.0
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


class ListsApiV1(BaseService):
    """The Lists API V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.cis.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'lists_api'

    @classmethod
    def new_instance(
        cls,
        crn: str,
        item_id: str,
        list_id: str,
        operation_id: str,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> 'ListsApiV1':
        """
        Return a new client for the Lists API service using the specified
               parameters and external configuration.

        :param str crn: Full URL-encoded CRN of the service instance.

        :param str item_id: List item identifier.

        :param str list_id: List identifier.

        :param str operation_id: List operation identifier.
        """
        if crn is None:
            raise ValueError('crn must be provided')
        if item_id is None:
            raise ValueError('item_id must be provided')
        if list_id is None:
            raise ValueError('list_id must be provided')
        if operation_id is None:
            raise ValueError('operation_id must be provided')

        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            crn,
            item_id,
            list_id,
            operation_id,
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(
        self,
        crn: str,
        item_id: str,
        list_id: str,
        operation_id: str,
        authenticator: Authenticator = None,
    ) -> None:
        """
        Construct a new client for the Lists API service.

        :param str crn: Full URL-encoded CRN of the service instance.

        :param str item_id: List item identifier.

        :param str list_id: List identifier.

        :param str operation_id: List operation identifier.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        if crn is None:
            raise ValueError('crn must be provided')
        if item_id is None:
            raise ValueError('item_id must be provided')
        if list_id is None:
            raise ValueError('list_id must be provided')
        if operation_id is None:
            raise ValueError('operation_id must be provided')

        BaseService.__init__(self, service_url=self.DEFAULT_SERVICE_URL, authenticator=authenticator)
        self.crn = crn
        self.item_id = item_id
        self.list_id = list_id
        self.operation_id = operation_id

    #########################
    # Lists
    #########################

    def get_managed_lists(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        List Managed Lists.

        List available managed lists for your instance.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ManagedListsResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_managed_lists',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn']
        path_param_values = self.encode_path_vars(self.crn)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/rules/managed_lists'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_custom_lists(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        List Custom Lists.

        List the custom lists for your instance.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CustomListsResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_custom_lists',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn']
        path_param_values = self.encode_path_vars(self.crn)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/rules/lists'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def create_custom_lists(
        self,
        *,
        kind: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create Custom List.

        Create a custom list for your instance.

        :param str kind: (optional) The type of list. Each type supports specific
               list items (IP addresses, ASNs, hostnames or redirects).
        :param str name: (optional) An informative name for the list. Use this name
               in rule expressions.
        :param str description: (optional) An informative summary of the list.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CustomListResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_custom_lists',
        )
        headers.update(sdk_headers)

        data = {
            'kind': kind,
            'name': name,
            'description': description,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn']
        path_param_values = self.encode_path_vars(self.crn)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/rules/lists'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_custom_list(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get Custom List.

        Get a custom list for your instance.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CustomListResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_custom_list',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'list_id']
        path_param_values = self.encode_path_vars(self.crn, self.list_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/rules/lists/{list_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def update_custom_list(
        self,
        *,
        description: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update Custom List.

        Update the description of a custom list.

        :param str description: (optional) An informative summary of the list.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CustomListResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_custom_list',
        )
        headers.update(sdk_headers)

        data = {
            'description': description,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'list_id']
        path_param_values = self.encode_path_vars(self.crn, self.list_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/rules/lists/{list_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_custom_list(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete Custom List.

        Delete a custom list for your instance.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteResourceResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_custom_list',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'list_id']
        path_param_values = self.encode_path_vars(self.crn, self.list_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/rules/lists/{list_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_list_items(
        self,
        *,
        cursor: Optional[str] = None,
        per_page: Optional[int] = None,
        search: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get List Items.

        Get the list items for a custom list.

        :param str cursor: (optional) The pagination cursor. An opaque string token
               indicating the position from which to continue when requesting the
               next/previous set of records. Cursor values are provided under
               result_info.cursors in the response.
        :param int per_page: (optional) Amount of results to include in each
               paginated response. A non-negative 32 bit integer. Minimum 1, maximum 500.
        :param str search: (optional) A search query to filter returned items. Its
               meaning depends on the list type: IP addresses must start with the provided
               string, hostnames and bulk redirects must contain the string, and ASNs must
               match the string exactly.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListItemsResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_list_items',
        )
        headers.update(sdk_headers)

        params = {
            'cursor': cursor,
            'per_page': per_page,
            'search': search,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'list_id']
        path_param_values = self.encode_path_vars(self.crn, self.list_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/rules/lists/{list_id}/items'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_list_items(
        self,
        *,
        create_list_items_req_item: Optional[List['CreateListItemsReqItem']] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create List Items.

        Create list items for your custom list. This operation is asynchronous. To get
        current the operation status, use the get operation status API.

        :param List[CreateListItemsReqItem] create_list_items_req_item: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListOperationResp` object
        """

        if create_list_items_req_item is not None:
            create_list_items_req_item = [convert_model(x) for x in create_list_items_req_item]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_list_items',
        )
        headers.update(sdk_headers)

        data = json.dumps(create_list_items_req_item)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'list_id']
        path_param_values = self.encode_path_vars(self.crn, self.list_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/rules/lists/{list_id}/items'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_list_items(
        self,
        *,
        items: Optional[List['DeleteListItemsReqItemsItem']] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete List Items.

        Remove one or more list items from your custom list. This operation is
        asynchronous. To get current the operation status, use the get operation status
        API.

        :param List[DeleteListItemsReqItemsItem] items: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListOperationResp` object
        """

        if items is not None:
            items = [convert_model(x) for x in items]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_list_items',
        )
        headers.update(sdk_headers)

        data = {
            'items': items,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'list_id']
        path_param_values = self.encode_path_vars(self.crn, self.list_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/rules/lists/{list_id}/items'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def update_list_items(
        self,
        *,
        create_list_items_req_item: Optional[List['CreateListItemsReqItem']] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update All List Items.

        Update all list items for your custom list. This removes existing items from the
        list. This operation is asynchronous. To get current the operation status, use the
        get operation status API.

        :param List[CreateListItemsReqItem] create_list_items_req_item: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListOperationResp` object
        """

        if create_list_items_req_item is not None:
            create_list_items_req_item = [convert_model(x) for x in create_list_items_req_item]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_list_items',
        )
        headers.update(sdk_headers)

        data = json.dumps(create_list_items_req_item)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'list_id']
        path_param_values = self.encode_path_vars(self.crn, self.list_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/rules/lists/{list_id}/items'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_list_item(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get List Item.

        Get a specific list item.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListItemResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_list_item',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'list_id', 'item_id']
        path_param_values = self.encode_path_vars(self.crn, self.list_id, self.item_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/rules/lists/{list_id}/items/{item_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response

    def get_operation_status(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get List Operation Status.

        Get the operation status for a custom list operation.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `OperationStatusResp` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_operation_status',
        )
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['crn', 'operation_id']
        path_param_values = self.encode_path_vars(self.crn, self.operation_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/{crn}/rules/lists/bulk_operations/{operation_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
        )

        response = self.send(request, **kwargs)
        return response


##############################################################################
# Models
##############################################################################


class CreateListItemsReqItem:
    """
    CreateListItemsReqItem.

    :param float asn: (optional) An autonomous system number.
    :param str comment: (optional) An informative summary of the list item.
    :param str hostname: (optional) Valid characters for hostnames are ASCII(7)
          letters from a to z, the digits from 0 to 9, wildcards (*), and the hyphen (-).
    :param str ip: (optional) An IPv4 address, an IPv4 CIDR, or an IPv6 CIDR. IPv6
          CIDRs are limited to a maximum of /64.
    """

    def __init__(
        self,
        *,
        asn: Optional[float] = None,
        comment: Optional[str] = None,
        hostname: Optional[str] = None,
        ip: Optional[str] = None,
    ) -> None:
        """
        Initialize a CreateListItemsReqItem object.

        :param float asn: (optional) An autonomous system number.
        :param str comment: (optional) An informative summary of the list item.
        :param str hostname: (optional) Valid characters for hostnames are ASCII(7)
               letters from a to z, the digits from 0 to 9, wildcards (*), and the hyphen
               (-).
        :param str ip: (optional) An IPv4 address, an IPv4 CIDR, or an IPv6 CIDR.
               IPv6 CIDRs are limited to a maximum of /64.
        """
        self.asn = asn
        self.comment = comment
        self.hostname = hostname
        self.ip = ip

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreateListItemsReqItem':
        """Initialize a CreateListItemsReqItem object from a json dictionary."""
        args = {}
        if (asn := _dict.get('asn')) is not None:
            args['asn'] = asn
        if (comment := _dict.get('comment')) is not None:
            args['comment'] = comment
        if (hostname := _dict.get('hostname')) is not None:
            args['hostname'] = hostname
        if (ip := _dict.get('ip')) is not None:
            args['ip'] = ip
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateListItemsReqItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'asn') and self.asn is not None:
            _dict['asn'] = self.asn
        if hasattr(self, 'comment') and self.comment is not None:
            _dict['comment'] = self.comment
        if hasattr(self, 'hostname') and self.hostname is not None:
            _dict['hostname'] = self.hostname
        if hasattr(self, 'ip') and self.ip is not None:
            _dict['ip'] = self.ip
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CreateListItemsReqItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreateListItemsReqItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreateListItemsReqItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DeleteListItemsReqItemsItem:
    """
    DeleteListItemsReqItemsItem.

    :param str id: (optional)
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
    ) -> None:
        """
        Initialize a DeleteListItemsReqItemsItem object.

        :param str id: (optional)
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteListItemsReqItemsItem':
        """Initialize a DeleteListItemsReqItemsItem object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteListItemsReqItemsItem object from a json dictionary."""
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
        """Return a `str` version of this DeleteListItemsReqItemsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteListItemsReqItemsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteListItemsReqItemsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DeleteResourceRespResult:
    """
    DeleteResourceRespResult.

    :param str id: (optional)
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
    ) -> None:
        """
        Initialize a DeleteResourceRespResult object.

        :param str id: (optional)
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteResourceRespResult':
        """Initialize a DeleteResourceRespResult object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteResourceRespResult object from a json dictionary."""
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
        """Return a `str` version of this DeleteResourceRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteResourceRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteResourceRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListOperationRespResult:
    """
    ListOperationRespResult.

    :param str operation_id: (optional)
    """

    def __init__(
        self,
        *,
        operation_id: Optional[str] = None,
    ) -> None:
        """
        Initialize a ListOperationRespResult object.

        :param str operation_id: (optional)
        """
        self.operation_id = operation_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListOperationRespResult':
        """Initialize a ListOperationRespResult object from a json dictionary."""
        args = {}
        if (operation_id := _dict.get('operation_id')) is not None:
            args['operation_id'] = operation_id
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListOperationRespResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'operation_id') and self.operation_id is not None:
            _dict['operation_id'] = self.operation_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListOperationRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListOperationRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListOperationRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ManagedListsResultItem:
    """
    ManagedListsResultItem.

    :param str name: (optional) The name of the list to be referenced by rule
          expressions.
    :param str description: (optional) Describes the contents of the managed list.
    :param str kind: (optional) The type of resource this list contains.
    """

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
        kind: Optional[str] = None,
    ) -> None:
        """
        Initialize a ManagedListsResultItem object.

        :param str name: (optional) The name of the list to be referenced by rule
               expressions.
        :param str description: (optional) Describes the contents of the managed
               list.
        :param str kind: (optional) The type of resource this list contains.
        """
        self.name = name
        self.description = description
        self.kind = kind

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ManagedListsResultItem':
        """Initialize a ManagedListsResultItem object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (kind := _dict.get('kind')) is not None:
            args['kind'] = kind
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ManagedListsResultItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'kind') and self.kind is not None:
            _dict['kind'] = self.kind
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ManagedListsResultItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ManagedListsResultItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ManagedListsResultItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class OperationStatusRespResult:
    """
    OperationStatusRespResult.

    :param str id: (optional)
    :param str status: (optional)
    :param str completed: (optional)
    :param str error: (optional) A message describing the error when the status is
          failed.
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        status: Optional[str] = None,
        completed: Optional[str] = None,
        error: Optional[str] = None,
    ) -> None:
        """
        Initialize a OperationStatusRespResult object.

        :param str id: (optional)
        :param str status: (optional)
        :param str completed: (optional)
        :param str error: (optional) A message describing the error when the status
               is failed.
        """
        self.id = id
        self.status = status
        self.completed = completed
        self.error = error

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'OperationStatusRespResult':
        """Initialize a OperationStatusRespResult object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        if (completed := _dict.get('completed')) is not None:
            args['completed'] = completed
        if (error := _dict.get('error')) is not None:
            args['error'] = error
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a OperationStatusRespResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'completed') and self.completed is not None:
            _dict['completed'] = self.completed
        if hasattr(self, 'error') and self.error is not None:
            _dict['error'] = self.error
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this OperationStatusRespResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'OperationStatusRespResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'OperationStatusRespResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        status.
        """

        PENDING = 'pending'
        RUNNING = 'running'
        COMPLETED = 'completed'
        FAILED = 'failed'



class CustomListResp:
    """
    Create Custom List Response.

    :param bool success: Was operation successful.
    :param List[List[str]] errors: Errors.
    :param List[List[str]] messages: Messages.
    :param CustomListResult result:
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        result: 'CustomListResult',
    ) -> None:
        """
        Initialize a CustomListResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Errors.
        :param List[List[str]] messages: Messages.
        :param CustomListResult result:
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CustomListResp':
        """Initialize a CustomListResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in CustomListResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in CustomListResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in CustomListResp JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = CustomListResult.from_dict(result)
        else:
            raise ValueError('Required property \'result\' not present in CustomListResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CustomListResp object from a json dictionary."""
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
        """Return a `str` version of this CustomListResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CustomListResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CustomListResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CustomListResult:
    """
    CustomListResult.

    :param str name: (optional) The name of the list to be referenced by rule
          expressions.
    :param str id: (optional) The unique ID of the list.
    :param str description: (optional) Describes the contents of the list.
    :param str kind: (optional) The type of resource this list contains.
    :param float num_items: (optional) How many items the list contains.
    :param float num_referencing_filters: (optional) How many times the list is used
          by rule expressions.
    """

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        id: Optional[str] = None,
        description: Optional[str] = None,
        kind: Optional[str] = None,
        num_items: Optional[float] = None,
        num_referencing_filters: Optional[float] = None,
    ) -> None:
        """
        Initialize a CustomListResult object.

        :param str name: (optional) The name of the list to be referenced by rule
               expressions.
        :param str id: (optional) The unique ID of the list.
        :param str description: (optional) Describes the contents of the list.
        :param str kind: (optional) The type of resource this list contains.
        :param float num_items: (optional) How many items the list contains.
        :param float num_referencing_filters: (optional) How many times the list is
               used by rule expressions.
        """
        self.name = name
        self.id = id
        self.description = description
        self.kind = kind
        self.num_items = num_items
        self.num_referencing_filters = num_referencing_filters

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CustomListResult':
        """Initialize a CustomListResult object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (kind := _dict.get('kind')) is not None:
            args['kind'] = kind
        if (num_items := _dict.get('num_items')) is not None:
            args['num_items'] = num_items
        if (num_referencing_filters := _dict.get('num_referencing_filters')) is not None:
            args['num_referencing_filters'] = num_referencing_filters
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CustomListResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'kind') and self.kind is not None:
            _dict['kind'] = self.kind
        if hasattr(self, 'num_items') and self.num_items is not None:
            _dict['num_items'] = self.num_items
        if hasattr(self, 'num_referencing_filters') and self.num_referencing_filters is not None:
            _dict['num_referencing_filters'] = self.num_referencing_filters
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CustomListResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CustomListResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CustomListResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CustomListsResp:
    """
    List Custom Lists Response.

    :param bool success: Was operation successful.
    :param List[List[str]] errors: Errors.
    :param List[List[str]] messages: Messages.
    :param List[CustomListResult] result:
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        result: List['CustomListResult'],
    ) -> None:
        """
        Initialize a CustomListsResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Errors.
        :param List[List[str]] messages: Messages.
        :param List[CustomListResult] result:
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CustomListsResp':
        """Initialize a CustomListsResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in CustomListsResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in CustomListsResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in CustomListsResp JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = [CustomListResult.from_dict(v) for v in result]
        else:
            raise ValueError('Required property \'result\' not present in CustomListsResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CustomListsResp object from a json dictionary."""
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
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CustomListsResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CustomListsResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CustomListsResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DeleteResourceResp:
    """
    DeleteResourceResp.

    :param bool success: Was operation successful.
    :param List[List[str]] errors: Errors.
    :param List[List[str]] messages: Messages.
    :param DeleteResourceRespResult result:
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        result: 'DeleteResourceRespResult',
    ) -> None:
        """
        Initialize a DeleteResourceResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Errors.
        :param List[List[str]] messages: Messages.
        :param DeleteResourceRespResult result:
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteResourceResp':
        """Initialize a DeleteResourceResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in DeleteResourceResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in DeleteResourceResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in DeleteResourceResp JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = DeleteResourceRespResult.from_dict(result)
        else:
            raise ValueError('Required property \'result\' not present in DeleteResourceResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteResourceResp object from a json dictionary."""
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
        """Return a `str` version of this DeleteResourceResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteResourceResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteResourceResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListCursor:
    """
    ListCursor.

    :param str after: (optional) The cursor token to fetch the next page of results.
    :param str before: (optional) The cursor token to fetch the previous page of
          results.
    """

    def __init__(
        self,
        *,
        after: Optional[str] = None,
        before: Optional[str] = None,
    ) -> None:
        """
        Initialize a ListCursor object.

        :param str after: (optional) The cursor token to fetch the next page of
               results.
        :param str before: (optional) The cursor token to fetch the previous page
               of results.
        """
        self.after = after
        self.before = before

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListCursor':
        """Initialize a ListCursor object from a json dictionary."""
        args = {}
        if (after := _dict.get('after')) is not None:
            args['after'] = after
        if (before := _dict.get('before')) is not None:
            args['before'] = before
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListCursor object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'after') and self.after is not None:
            _dict['after'] = self.after
        if hasattr(self, 'before') and self.before is not None:
            _dict['before'] = self.before
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListCursor object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListCursor') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListCursor') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListItem:
    """
    ListItem.

    :param str id: (optional)
    :param float asn: (optional) An autonomous system number.
    :param str comment: (optional) An informative summary of the list item.
    :param str hostname: (optional) Valid characters for hostnames are ASCII(7)
          letters from a to z, the digits from 0 to 9, wildcards (*), and the hyphen (-).
    :param str ip: (optional) An IPv4 address, an IPv4 CIDR, or an IPv6 CIDR. IPv6
          CIDRs are limited to a maximum of /64.
    :param str created_on: (optional)
    :param str modified_on: (optional)
    """

    def __init__(
        self,
        *,
        id: Optional[str] = None,
        asn: Optional[float] = None,
        comment: Optional[str] = None,
        hostname: Optional[str] = None,
        ip: Optional[str] = None,
        created_on: Optional[str] = None,
        modified_on: Optional[str] = None,
    ) -> None:
        """
        Initialize a ListItem object.

        :param str id: (optional)
        :param float asn: (optional) An autonomous system number.
        :param str comment: (optional) An informative summary of the list item.
        :param str hostname: (optional) Valid characters for hostnames are ASCII(7)
               letters from a to z, the digits from 0 to 9, wildcards (*), and the hyphen
               (-).
        :param str ip: (optional) An IPv4 address, an IPv4 CIDR, or an IPv6 CIDR.
               IPv6 CIDRs are limited to a maximum of /64.
        :param str created_on: (optional)
        :param str modified_on: (optional)
        """
        self.id = id
        self.asn = asn
        self.comment = comment
        self.hostname = hostname
        self.ip = ip
        self.created_on = created_on
        self.modified_on = modified_on

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListItem':
        """Initialize a ListItem object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        if (asn := _dict.get('asn')) is not None:
            args['asn'] = asn
        if (comment := _dict.get('comment')) is not None:
            args['comment'] = comment
        if (hostname := _dict.get('hostname')) is not None:
            args['hostname'] = hostname
        if (ip := _dict.get('ip')) is not None:
            args['ip'] = ip
        if (created_on := _dict.get('created_on')) is not None:
            args['created_on'] = created_on
        if (modified_on := _dict.get('modified_on')) is not None:
            args['modified_on'] = modified_on
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'asn') and self.asn is not None:
            _dict['asn'] = self.asn
        if hasattr(self, 'comment') and self.comment is not None:
            _dict['comment'] = self.comment
        if hasattr(self, 'hostname') and self.hostname is not None:
            _dict['hostname'] = self.hostname
        if hasattr(self, 'ip') and self.ip is not None:
            _dict['ip'] = self.ip
        if hasattr(self, 'created_on') and self.created_on is not None:
            _dict['created_on'] = self.created_on
        if hasattr(self, 'modified_on') and self.modified_on is not None:
            _dict['modified_on'] = self.modified_on
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListItemResp:
    """
    ListItemResp.

    :param bool success: Was operation successful.
    :param List[List[str]] errors: Errors.
    :param List[List[str]] messages: Messages.
    :param ListItem result:
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        result: 'ListItem',
    ) -> None:
        """
        Initialize a ListItemResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Errors.
        :param List[List[str]] messages: Messages.
        :param ListItem result:
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListItemResp':
        """Initialize a ListItemResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in ListItemResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in ListItemResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in ListItemResp JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = ListItem.from_dict(result)
        else:
            raise ValueError('Required property \'result\' not present in ListItemResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListItemResp object from a json dictionary."""
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
        """Return a `str` version of this ListItemResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListItemResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListItemResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListItemsResp:
    """
    ListItemsResp.

    :param bool success: Was operation successful.
    :param List[List[str]] errors: Errors.
    :param List[List[str]] messages: Messages.
    :param List[ListItem] result:
    :param ListItemsResultInfo result_info: (optional)
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        result: List['ListItem'],
        *,
        result_info: Optional['ListItemsResultInfo'] = None,
    ) -> None:
        """
        Initialize a ListItemsResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Errors.
        :param List[List[str]] messages: Messages.
        :param List[ListItem] result:
        :param ListItemsResultInfo result_info: (optional)
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result
        self.result_info = result_info

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListItemsResp':
        """Initialize a ListItemsResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in ListItemsResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in ListItemsResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in ListItemsResp JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = [ListItem.from_dict(v) for v in result]
        else:
            raise ValueError('Required property \'result\' not present in ListItemsResp JSON')
        if (result_info := _dict.get('result_info')) is not None:
            args['result_info'] = ListItemsResultInfo.from_dict(result_info)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListItemsResp object from a json dictionary."""
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
        """Return a `str` version of this ListItemsResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListItemsResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListItemsResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListItemsResultInfo:
    """
    ListItemsResultInfo.

    :param ListCursor cursors: (optional)
    """

    def __init__(
        self,
        *,
        cursors: Optional['ListCursor'] = None,
    ) -> None:
        """
        Initialize a ListItemsResultInfo object.

        :param ListCursor cursors: (optional)
        """
        self.cursors = cursors

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListItemsResultInfo':
        """Initialize a ListItemsResultInfo object from a json dictionary."""
        args = {}
        if (cursors := _dict.get('cursors')) is not None:
            args['cursors'] = ListCursor.from_dict(cursors)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListItemsResultInfo object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cursors') and self.cursors is not None:
            if isinstance(self.cursors, dict):
                _dict['cursors'] = self.cursors
            else:
                _dict['cursors'] = self.cursors.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListItemsResultInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListItemsResultInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListItemsResultInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListOperationResp:
    """
    ListOperationResp.

    :param bool success: Was operation successful.
    :param List[List[str]] errors: Errors.
    :param List[List[str]] messages: Messages.
    :param ListOperationRespResult result:
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        result: 'ListOperationRespResult',
    ) -> None:
        """
        Initialize a ListOperationResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Errors.
        :param List[List[str]] messages: Messages.
        :param ListOperationRespResult result:
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListOperationResp':
        """Initialize a ListOperationResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in ListOperationResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in ListOperationResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in ListOperationResp JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = ListOperationRespResult.from_dict(result)
        else:
            raise ValueError('Required property \'result\' not present in ListOperationResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListOperationResp object from a json dictionary."""
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
        """Return a `str` version of this ListOperationResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListOperationResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListOperationResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ManagedListsResp:
    """
    List Managed Lists Response.

    :param bool success: Was operation successful.
    :param List[List[str]] errors: Errors.
    :param List[List[str]] messages: Messages.
    :param List[ManagedListsResultItem] result:
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        result: List['ManagedListsResultItem'],
    ) -> None:
        """
        Initialize a ManagedListsResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Errors.
        :param List[List[str]] messages: Messages.
        :param List[ManagedListsResultItem] result:
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ManagedListsResp':
        """Initialize a ManagedListsResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in ManagedListsResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in ManagedListsResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in ManagedListsResp JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = [ManagedListsResultItem.from_dict(v) for v in result]
        else:
            raise ValueError('Required property \'result\' not present in ManagedListsResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ManagedListsResp object from a json dictionary."""
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
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ManagedListsResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ManagedListsResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ManagedListsResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class OperationStatusResp:
    """
    OperationStatusResp.

    :param bool success: Was operation successful.
    :param List[List[str]] errors: Errors.
    :param List[List[str]] messages: Messages.
    :param OperationStatusRespResult result:
    """

    def __init__(
        self,
        success: bool,
        errors: List[List[str]],
        messages: List[List[str]],
        result: 'OperationStatusRespResult',
    ) -> None:
        """
        Initialize a OperationStatusResp object.

        :param bool success: Was operation successful.
        :param List[List[str]] errors: Errors.
        :param List[List[str]] messages: Messages.
        :param OperationStatusRespResult result:
        """
        self.success = success
        self.errors = errors
        self.messages = messages
        self.result = result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'OperationStatusResp':
        """Initialize a OperationStatusResp object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError('Required property \'success\' not present in OperationStatusResp JSON')
        if (errors := _dict.get('errors')) is not None:
            args['errors'] = errors
        else:
            raise ValueError('Required property \'errors\' not present in OperationStatusResp JSON')
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = messages
        else:
            raise ValueError('Required property \'messages\' not present in OperationStatusResp JSON')
        if (result := _dict.get('result')) is not None:
            args['result'] = OperationStatusRespResult.from_dict(result)
        else:
            raise ValueError('Required property \'result\' not present in OperationStatusResp JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a OperationStatusResp object from a json dictionary."""
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
        """Return a `str` version of this OperationStatusResp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'OperationStatusResp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'OperationStatusResp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
